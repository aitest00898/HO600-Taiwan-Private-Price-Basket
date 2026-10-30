#!/usr/bin/env python3
"""Validate Batch 9 fixed ledgers and exact-admission preaudit artifacts."""

from __future__ import annotations

import csv
import re
import sys
from collections import Counter, defaultdict
from decimal import Decimal, InvalidOperation
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
LEDGER_DIR = ROOT / "research" / "batch-09"
EXPECTED_HEADER = [
    "research_id", "domain", "subcategory", "brand_or_merchant", "concept",
    "model_sku_plan", "specification", "channel_geography", "source_2020",
    "date_2020", "normal_price_2020", "source_2026", "date_2026",
    "normal_price_2026", "comparability", "evidence_grade_2020",
    "evidence_grade_2026", "brand_count", "brand_subcategory_count",
    "product_family_count", "historical_source_count", "decision", "notes",
]
EXPECTED_PREAUDIT_HEADER = [
    "research_id", "checkpoint", "candidate_pool_ids", "candidate_link_state",
    "domain", "subcategory", "brand_or_merchant", "corporate_group_id",
    "corporate_group_status", "concept", "model_sku_plan", "specification",
    "channel_geography", "source_2020", "source_2020_final_url", "date_2020", "price_2020",
    "source_2020_receipt_id", "source_2020_http_status", "source_2020_tls_status",
    "source_2020_sha256", "source_2026", "source_2026_final_url", "date_2026", "price_2026",
    "source_2026_receipt_id", "source_2026_http_status", "source_2026_tls_status",
    "source_2026_sha256", "normal_vs_promo_2020", "normal_vs_promo_2026",
    "sku_identity_check", "channel_spec_check", "comparability",
    "evidence_grade_2020", "evidence_grade_2026", "decision",
    "preaudit_status", "reason", "missing_evidence", "formal_exact_delta",
]
VALID_STATUSES = {"EXACT_READY_CANDIDATE", "NEEDS_EVIDENCE", "RESEARCH_ONLY", "HOLD"}


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        return list(reader.fieldnames or []), list(reader)


def decimal_positive(value: str) -> bool:
    try:
        return Decimal(value.strip()) > 0
    except (InvalidOperation, AttributeError):
        return False


def valid_https(value: str) -> bool:
    return value.startswith("https://") and bool(re.match(r"^https://[^/]+", value))


def validate(root: Path = ROOT) -> tuple[list[str], dict[str, object]]:
    base = root / "research" / "batch-09"
    errors: list[str] = []
    rows: list[dict[str, str]] = []
    by_id: dict[str, dict[str, str]] = {}
    checkpoint_rows: dict[int, list[dict[str, str]]] = {}

    for checkpoint in range(1, 9):
        path = base / f"checkpoint-{checkpoint:02d}-ledger.csv"
        if not path.is_file():
            errors.append(f"missing ledger: {path.name}")
            continue
        header, part = read_csv(path)
        if header != EXPECTED_HEADER:
            errors.append(f"{path.name}: schema/header mismatch")
        if len(part) != 20:
            errors.append(f"{path.name}: expected 20 rows, found {len(part)}")
        checkpoint_rows[checkpoint] = part
        for index, row in enumerate(part, start=1):
            rid = row.get("research_id", "")
            if not re.fullmatch(rf"B09-C{checkpoint:02d}-\d{{3}}", rid):
                errors.append(f"{path.name}:{index + 1}: invalid checkpoint-scoped research_id {rid!r}")
            if None in row:
                errors.append(f"{path.name}:{index + 1}: CSV row has fields beyond the fixed schema")
            if rid in by_id:
                errors.append(f"duplicate research_id: {rid}")
            by_id[rid] = row
            rows.append(row)

            required = ("domain", "subcategory", "brand_or_merchant", "concept", "model_sku_plan", "specification", "channel_geography", "notes")
            if any(not row.get(field, "").strip() for field in required):
                errors.append(f"{rid}: required descriptive field missing")
            if not decimal_positive(row.get("normal_price_2020", "")):
                errors.append(f"{rid}: invalid/nonpositive 2020 price")
            if not decimal_positive(row.get("normal_price_2026", "")):
                errors.append(f"{rid}: invalid/nonpositive 2026 price")
            if "2020" not in row.get("date_2020", ""):
                errors.append(f"{rid}: 2020 date/year is not explicit")
            if "2026" not in row.get("date_2026", ""):
                errors.append(f"{rid}: 2026 date/year is not explicit")
            if not valid_https(row.get("source_2020", "")) or not valid_https(row.get("source_2026", "")):
                errors.append(f"{rid}: source URL must use HTTPS")
            if row.get("comparability") not in {"A", "B"}:
                errors.append(f"{rid}: invalid comparability {row.get('comparability')!r}")
            if row.get("evidence_grade_2020") not in {"A", "B", "C"}:
                errors.append(f"{rid}: invalid 2020 evidence grade")
            if row.get("evidence_grade_2026") not in {"A", "B"}:
                errors.append(f"{rid}: invalid 2026 evidence grade")
            if row.get("decision") != "ADMISSIBLE":
                errors.append(f"{rid}: fixed decision is not ADMISSIBLE")
            try:
                family_count = int(row.get("product_family_count", ""))
            except ValueError:
                family_count = 0
            if family_count not in {1, 2}:
                errors.append(f"{rid}: product family count must be 1 or 2")

    if len(rows) != 160:
        errors.append(f"fixed ledger total must be 160 rows, found {len(rows)}")
    if len(by_id) != len(rows):
        errors.append("research IDs are not unique")

    source_urls = {row.get("source_2020", "") for row in rows} | {row.get("source_2026", "") for row in rows}
    source_receipt_path = base / "source-readability-receipts-2026-10-30.csv"
    _, source_receipts = read_csv(source_receipt_path) if source_receipt_path.is_file() else ([], [])
    if not source_receipt_path.is_file():
        errors.append("missing full fixed-source readability receipts")
    receipt_urls = [row.get("requested_url", "") for row in source_receipts]
    if len(source_receipts) != 229 or len(set(receipt_urls)) != 229 or set(receipt_urls) != source_urls:
        errors.append("strict source-readability receipts must cover exactly the 229 unique fixed-ledger URLs")
    for receipt in source_receipts:
        result = receipt.get("result", "")
        tls = receipt.get("tls_validation", "")
        if result == "TLS_ERROR" and not tls.startswith("FAIL"):
            errors.append(f"TLS error recorded as passing: {receipt.get('requested_url')}")
        if result in {"HTTP_BODY_READ", "HTTP_ERROR"} and not tls.startswith("PASS"):
            errors.append(f"HTTP response recorded without strict TLS pass: {receipt.get('requested_url')}")
        if any(token in (tls + receipt.get("error", "")).lower() for token in ("-k", "cert_none", "verify=false", "insecure")):
            errors.append(f"TLS bypass indicator in source receipt: {receipt.get('requested_url')}")

    url_counts = Counter(row.get("source_2020", "") for row in rows)
    for url, count in url_counts.items():
        if url and count > 6:
            errors.append(f"2020 source concentration exceeds 6: {count} rows at {url}")

    brand_counts = Counter(row.get("brand_or_merchant", "") for row in rows)
    for brand, count in brand_counts.items():
        if brand and count > 8:
            errors.append(f"brand concentration exceeds 8: {brand}={count}")
    brand_subcategory_counts = Counter((row.get("brand_or_merchant", ""), row.get("subcategory", "")) for row in rows)
    for (brand, subcategory), count in brand_subcategory_counts.items():
        if count > 5:
            errors.append(f"brand/subcategory concentration exceeds 5: {brand}/{subcategory}={count}")

    # Exact duplicate identity tuples are rejected even if a new research ID is used.
    identity_keys: dict[tuple[str, str, str, str, str], str] = {}
    for row in rows:
        sku = re.sub(r"\s+", " ", row.get("model_sku_plan", "").strip().lower())
        concept = re.sub(r"\s+", " ", row.get("concept", "").strip().lower())
        key = (row.get("brand_or_merchant", "").strip(), row.get("subcategory", "").strip(), concept, sku, row.get("channel_geography", "").strip())
        previous = identity_keys.get(key)
        if previous and sku:
            errors.append(f"duplicate product/service identity: {previous} and {row.get('research_id')}")
        identity_keys[key] = row.get("research_id", "")

    group_path = base / "batch09-brand-corporate-group-crosswalk.csv"
    group_header, group_rows = read_csv(group_path) if group_path.is_file() else ([], [])
    if not group_path.is_file():
        errors.append("missing batch09-brand-corporate-group-crosswalk.csv")
    group_by_brand = {row.get("brand_or_merchant", ""): row for row in group_rows}
    labels = set(brand_counts)
    for brand in sorted(labels - set(group_by_brand)):
        errors.append(f"corporate group attribution missing: {brand}")
    if len(group_by_brand) != len(group_rows):
        errors.append("corporate group crosswalk contains duplicate brand labels")
    group_counts: Counter[str] = Counter()
    unresolved_groups = set()
    for row in rows:
        mapping = group_by_brand.get(row.get("brand_or_merchant", ""), {})
        gid = mapping.get("corporate_group_id", "")
        status = mapping.get("attribution_status", "")
        if not gid or status not in {"VERIFIED_CONSOLIDATED_GROUP", "UNRESOLVED_SINGLETON"}:
            errors.append(f"{row.get('research_id')}: invalid corporate-group mapping")
            continue
        if status == "VERIFIED_CONSOLIDATED_GROUP":
            group_counts[gid] += 1
        else:
            unresolved_groups.add(gid)
    for group, count in group_counts.items():
        if count > 16:
            errors.append(f"consolidated corporate group exceeds 16: {group}={count}")

    family_path = base / "batch09-product-family-crosswalk.csv"
    family_header, family_rows = read_csv(family_path) if family_path.is_file() else ([], [])
    if not family_path.is_file():
        errors.append("missing batch09-product-family-crosswalk.csv")
    if family_header != ["research_id", "family_key", "declared_family_count", "review_status", "basis"]:
        errors.append("product-family crosswalk schema/header mismatch")
    family_by_id = {row.get("research_id", ""): row for row in family_rows}
    if len(family_by_id) != len(family_rows):
        errors.append("product-family crosswalk contains duplicate research IDs")
    if set(family_by_id) != set(by_id):
        errors.append("product-family crosswalk does not cover exactly the 160 fixed rows")
    for rid, row in by_id.items():
        family = family_by_id.get(rid, {})
        if family.get("declared_family_count") != row.get("product_family_count"):
            errors.append(f"{rid}: family crosswalk declared count differs from fixed ledger")
    family_members: Counter[str] = Counter(row.get("family_key", "") for row in family_rows)
    for family_key, count in family_members.items():
        if not family_key or count > 2:
            errors.append(f"invalid/over-cap product family key: {family_key!r}={count}")

    pool_path = root / "data" / "Candidate_Pool.csv"
    if not pool_path.is_file():
        errors.append("missing data/Candidate_Pool.csv")
        candidate_by_id: dict[str, dict[str, str]] = {}
    else:
        _, pool_rows = read_csv(pool_path)
        candidate_by_id = {row.get("candidate_id", ""): row for row in pool_rows}
        if len(pool_rows) != 418:
            errors.append(f"Candidate Pool must contain 418 rows, found {len(pool_rows)}")
        if len(candidate_by_id) != len(pool_rows):
            errors.append("Candidate Pool has duplicate candidate_id values")
    link_path = base / "batch09-candidate-pool-dedup.csv"
    _, link_rows = read_csv(link_path) if link_path.is_file() else ([], [])
    if not link_path.is_file():
        errors.append("missing batch09-candidate-pool-dedup.csv")
    link_by_research: dict[str, list[dict[str, str]]] = defaultdict(list)
    for link in link_rows:
        rid = link.get("research_id", "")
        if rid not in by_id:
            errors.append(f"candidate dedup row references unknown research_id: {rid}")
        link_by_research[rid].append(link)
        cid = link.get("candidate_id", "").strip()
        if cid and cid not in candidate_by_id:
            errors.append(f"candidate dedup row references unknown Candidate Pool ID: {cid}")
        if link.get("candidate_pool_rows_reviewed") != "418":
            errors.append(f"{rid}: candidate dedup must record review against all 418 Candidate Pool concepts")
        state = link.get("link_state", "")
        if state not in {"EXACT_CONCEPT_MATCH", "CONDITIONAL_CONCEPT_MATCH", "EXISTING_PAIR_ALREADY_PRESENT", "REJECTED_DIFFERENT_CONCEPT", "NO_CONFIRMED_LINK"}:
            errors.append(f"{rid}: invalid Candidate Pool dedup state {state!r}")
    for rid in by_id:
        if rid not in link_by_research:
            errors.append(f"candidate dedup crosswalk missing row: {rid}")

    preaudit_path = base / "exact-admission-preaudit-2026-10-30.csv"
    preaudit_header, preaudit_rows = read_csv(preaudit_path) if preaudit_path.is_file() else ([], [])
    if not preaudit_path.is_file():
        errors.append("missing exact-admission-preaudit-2026-10-30.csv")
    if preaudit_header != EXPECTED_PREAUDIT_HEADER:
        errors.append("preaudit matrix schema/header mismatch")
    if len(preaudit_rows) != 160:
        errors.append(f"preaudit matrix must contain 160 rows, found {len(preaudit_rows)}")
    preaudit_by_id = {row.get("research_id", ""): row for row in preaudit_rows}
    if len(preaudit_by_id) != len(preaudit_rows) or set(preaudit_by_id) != set(by_id):
        errors.append("preaudit matrix IDs must exactly cover the 160 fixed ledger IDs")
    for row in preaudit_rows:
        if row.get("preaudit_status") not in VALID_STATUSES:
            errors.append(f"{row.get('research_id')}: invalid preaudit status")
        if not row.get("reason", "").strip():
            errors.append(f"{row.get('research_id')}: preaudit reason is required")
        if not row.get("missing_evidence", "").strip():
            errors.append(f"{row.get('research_id')}: evidence limitation/action must be explicit")
        if row.get("preaudit_status") == "EXACT_READY_CANDIDATE":
            if row.get("source_2020_http_status") != "200" or row.get("source_2026_http_status") != "200":
                errors.append(f"{row.get('research_id')}: Exact-ready candidate lacks HTTP 200 readback on both years")
            if "PASS" not in row.get("source_2020_tls_status", "") or "PASS" not in row.get("source_2026_tls_status", ""):
                errors.append(f"{row.get('research_id')}: Exact-ready candidate lacks strict TLS receipts")
            if not row.get("candidate_pool_ids", "").strip():
                errors.append(f"{row.get('research_id')}: Exact-ready candidate must map to an existing Candidate Pool concept")
            if row.get("formal_exact_delta") != "1 candidate; not yet admitted":
                errors.append(f"{row.get('research_id')}: Exact-ready row must state one conditional candidate delta")

    expected_ready = {"B09-C08-016", "B09-C08-017"}
    actual_ready = {row.get("research_id") for row in preaudit_rows if row.get("preaudit_status") == "EXACT_READY_CANDIDATE"}
    if actual_ready != expected_ready:
        errors.append(f"Exact-ready candidates differ from the source-adjudicated set: {sorted(actual_ready)}")

    near_path = base / "batch09-candidate-pool-top5-2026-10-30.csv"
    _, near_rows = read_csv(near_path) if near_path.is_file() else ([], [])
    if not near_path.is_file():
        errors.append("missing batch09-candidate-pool-top5-2026-10-30.csv")
    if len(near_rows) != 160 * 5:
        errors.append(f"Candidate Pool similarity review must contain 5 ranked suggestions per fixed row; found {len(near_rows)}")
    near_counts = Counter(row.get("research_id", "") for row in near_rows)
    if any(near_counts.get(rid, 0) != 5 for rid in by_id):
        errors.append("Candidate Pool top-five review does not cover every fixed research row exactly five times")

    candidate_list_path = base / "exact-admission-candidate-list-2026-10-30.csv"
    _, candidate_list_rows = read_csv(candidate_list_path) if candidate_list_path.is_file() else ([], [])
    if not candidate_list_path.is_file():
        errors.append("missing exact-admission-candidate-list-2026-10-30.csv")
    for row in candidate_list_rows:
        if row.get("candidate_id") not in candidate_by_id:
            errors.append(f"candidate list references unknown Candidate Pool ID: {row.get('candidate_id')}")
        if row.get("research_id") not in by_id:
            errors.append(f"candidate list references unknown research ID: {row.get('research_id')}")
    if sum(row.get("preaudit_status") == "EXACT_READY_CANDIDATE" for row in candidate_list_rows) != 2:
        errors.append("candidate list must contain exactly two Exact-ready preaudit rows")

    statuses = Counter(row.get("preaudit_status", "") for row in preaudit_rows)
    summary: dict[str, object] = {
        "rows": len(rows),
        "unique_ids": len(by_id),
        "checkpoint_counts": {f"C{n:02d}": len(checkpoint_rows.get(n, [])) for n in range(1, 9)},
        "brand_labels": len(labels),
        "unique_source_urls": len(source_urls),
        "source_readback_counts": dict(Counter(row.get("result", "") + ":" + (row.get("http_status", "") or "TLS_ERROR") for row in source_receipts)),
        "unresolved_corporate_group_labels": sum(1 for r in group_rows if r.get("attribution_status") == "UNRESOLVED_SINGLETON"),
        "verified_corporate_group_counts": dict(group_counts),
        "preaudit_status_counts": dict(statuses),
        "candidate_ready_count": statuses.get("EXACT_READY_CANDIDATE", 0),
        "candidate_pool_count": len(candidate_by_id),
        "errors": errors,
    }
    return errors, summary


def main() -> int:
    errors, summary = validate()
    print(f"BATCH09_FIXED_ROWS={summary['rows']}")
    print(f"BATCH09_UNIQUE_IDS={summary['unique_ids']}")
    print(f"BRAND_LABELS={summary['brand_labels']}")
    print(f"UNRESOLVED_GROUP_LABELS={summary['unresolved_corporate_group_labels']}")
    print(f"CORPORATE_GROUP_COUNTS={summary['verified_corporate_group_counts']}")
    print(f"PREAUDIT_STATUS_COUNTS={summary['preaudit_status_counts']}")
    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        print(f"VALIDATION=FAIL errors={len(errors)}")
        return 1
    print("VALIDATION=PASS errors=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
