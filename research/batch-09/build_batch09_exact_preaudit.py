#!/usr/bin/env python3
"""Build the reviewable 160-row Batch 9 Exact-admission preaudit."""

from __future__ import annotations

import csv
import hashlib
import json
import re
import ssl
import subprocess
from collections import Counter, defaultdict
from datetime import datetime, timezone
from difflib import SequenceMatcher
from pathlib import Path
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "research" / "batch-09"
POOL_PATH = ROOT / "data" / "Candidate_Pool.csv"
MATRIX_PATH = BASE / "exact-admission-preaudit-2026-10-30.csv"
LINK_PATH = BASE / "batch09-candidate-pool-dedup.csv"
GROUP_PATH = BASE / "batch09-brand-corporate-group-crosswalk.csv"
FAMILY_PATH = BASE / "batch09-product-family-crosswalk.csv"
NEAR_MATCH_PATH = BASE / "batch09-candidate-pool-top5-2026-10-30.csv"
CANDIDATE_PATH = BASE / "exact-admission-candidate-list-2026-10-30.csv"
SUMMARY_PATH = BASE / "exact-admission-preaudit-summary-2026-10-30.json"
NOTEBOOK_PATH = BASE / "exact-admission-preaudit-2026-10-30.ipynb"

GROUPS: dict[str, tuple[str, str]] = {}


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        return list(reader.fieldnames or []), list(reader)


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def fixed_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for checkpoint in range(1, 9):
        _, part = read_csv(BASE / f"checkpoint-{checkpoint:02d}-ledger.csv")
        rows.extend(part)
    return rows


def load_receipts() -> dict[str, dict[str, str]]:
    paths = [
        BASE / "source-readability-receipts-2026-10-30.csv",
        BASE / "source-readability-c01-c05-2026-10-30.csv",
        BASE / "c03-grade-source-readback-2026-10-30.csv",
        BASE / "checkpoint-06-source-receipts-2026-10-30.csv",
        BASE / "checkpoint-07-source-receipts-2026-10-30.csv",
        BASE / "checkpoint-08-source-receipts-2026-10-30.csv",
        BASE / "exact-candidate-source-receipts-2026-10-30.csv",
    ]
    receipts: dict[str, dict[str, str]] = {}
    exact_securetransport_urls: set[str] = set()
    for path in paths:
        if not path.is_file():
            continue
        _, part = read_csv(path)
        for row in part:
            url = row.get("requested_url", "").strip()
            if not url:
                continue
            if path.name == "exact-candidate-source-receipts-2026-10-30.csv":
                receipts[url] = row
                exact_securetransport_urls.add(url)
                continue
            if url in exact_securetransport_urls:
                continue
            previous = receipts.get(url)
            if previous is None or row.get("retrieved_at_utc", "") >= previous.get("retrieved_at_utc", ""):
                receipts[url] = row
    return receipts


def stable_receipt_id(url: str, receipt: dict[str, str]) -> str:
    if receipt.get("receipt_id"):
        return receipt["receipt_id"]
    digest = hashlib.sha256((url + receipt.get("sha256", "")).encode("utf-8")).hexdigest()[:12].upper()
    if "c03-grade-source-readback" in str(receipt.get("_source_file", "")):
        return f"C03R-{digest}"
    return f"READBACK-{digest}"


def group_assignments(brands: set[str]) -> dict[str, dict[str, str]]:
    official_groups: dict[str, tuple[str, str]] = {}
    uni = [
        "7-ELEVEN", "統一陽光", "統一純喫茶", "統一 來一客", "統一飲冰室茶集",
        "統一Dr.Milker", "統一麥香", "統一", "左岸咖啡館",
    ]
    for brand in uni:
        official_groups[brand] = (
            "UNIPRESIDENT_GROUP",
            "Prior Batch 9 ownership reconciliation; Uni-President 2020 annual report: https://ir.sp88.tw/upload/file/fin_202312140946486458.pdf",
        )
    for brand in ["DECATHLON 迪卡儂", "FORCLAZ 迪卡儂", "KALENJI 迪卡儂", "KIPRUN 迪卡儂", "QUECHUA 迪卡儂"]:
        official_groups[brand] = ("DECATHLON_GROUP", "Official Taiwan brand/store: https://www.decathlon.tw/")
    for brand in ["FamilyMart Collection 全家", "FamilyMart 全家", "FamilyMart 全家 / FAMI COLLECTION"]:
        official_groups[brand] = ("FAMILYMART_GROUP", "Brand labels and official Taiwan service site: https://www.family.com.tw/")
    for brand in ["Costco 好市多", "Kirkland Signature 科克蘭"]:
        official_groups[brand] = ("COSTCO_GROUP", "Costco Taiwan and Kirkland private-label attribution: https://www.costco.com.tw/")
    for brand in ["中華電信", "Hami書城"]:
        official_groups[brand] = ("CHT_GROUP", "Chunghwa Telecom/Hami official service site: https://www.cht.com.tw/")
    for brand in ["Coca-Cola 可口可樂", "可口可樂紅茶花傳"]:
        official_groups[brand] = ("COCA_COLA_GROUP", "Official Taiwan Coca-Cola brand site: https://www.coca-cola.com/tw/"
        )
    for brand in ["Doritos 多力多滋", "Lay's 樂事"]:
        official_groups[brand] = ("PEPSICO_GROUP", "PepsiCo official brands list: https://www.pepsico.com/brands")
    official_groups["嘟嘟房"] = (
        "CHUNGHSIN_GROUP",
        "THSRC official Taichung parking page labels the operator logo 中興電工(嘟嘟房): https://www.thsrc.com.tw/ArticleContent/3301e395-46b8-47aa-aa37-139e15708779",
    )

    result: dict[str, dict[str, str]] = {}
    for brand in sorted(brands):
        if brand in official_groups:
            group, basis = official_groups[brand]
            result[brand] = {
                "brand_or_merchant": brand,
                "corporate_group_id": group,
                "attribution_status": "VERIFIED_CONSOLIDATED_GROUP",
                "attribution_basis": basis,
            }
        else:
            result[brand] = {
                "brand_or_merchant": brand,
                "corporate_group_id": f"UNRESOLVED::{brand}",
                "attribution_status": "UNRESOLVED_SINGLETON",
                "attribution_basis": "No cross-brand consolidation asserted in this preaudit; exact ledger label retained. Parent-group ownership remains unverified.",
            }
    return result


FAMILY_GROUPS: list[tuple[str, list[str], str]] = [
    ("PILOT-INSTAWRT", ["B09-C01-004", "B09-C01-005"], "Checkpoint notes identify two Instant-writing family variants."),
    ("CHT-FIBER-PLANS", ["B09-C01-006", "B09-C01-007"], "Same Chunghwa Fiber service family; different speed tiers."),
    ("CHT-MOVE-FEES", ["B09-C01-008", "B09-C01-009"], "Same Chunghwa Fiber installation/move-fee family; distinct fee definitions."),
    ("APPLE-ONE", ["B09-C01-017", "B09-C01-018"], "Same Apple One plan family; individual and family variants."),
    ("MICROSOFT-365", ["B09-C01-019", "B09-C01-020"], "Same Microsoft 365 family; individual and household variants."),
    ("UNIQLO-HEATTECH-ACCESSORY", ["B09-C02-003", "B09-C02-020"], "Checkpoint notes identify scarf and knit-hat variants in one Heattech accessory family."),
    ("UNIQLO-CASHMERE", ["B09-C02-008", "B09-C02-019"], "Checkpoint notes identify two cashmere sweater variants."),
    ("UNIQLO-AIRISM-TOPS", ["B09-C02-004", "B09-C02-005"], "Same AIRism cotton top family; sleeve and fit variants."),
    ("IBON-PRINT", ["B09-C01-016", "B09-C02-009"], "Checkpoint notes identify black-and-white and color printing as two ibon print-family variants."),
    ("SHALLOP-MOUTHWASH", ["B09-C03-005", "B09-C03-006"], "Checkpoint notes explicitly identify two Shallop mouthwash family variants."),
    ("TAIPEI101-PARKING", ["B09-C03-015", "B09-C03-016"], "Same facility and vehicle/hourly rate family; weekday/weekend variants."),
    ("MITSUI-PARKING", ["B09-C04-011", "B09-C04-012"], "Same Mitsui outlet facility; weekday/weekend hourly variants."),
    ("GLORIA-PARKING", ["B09-C04-013", "B09-C04-014"], "Same Gloria facility; weekday/weekend hourly variants."),
    ("EA-PLAY", ["B09-C04-020", "B09-C04-021"], "Same EA Play plan family; monthly/annual billing variants."),
    ("EA-PLAY-PRO", ["B09-C04-022", "B09-C04-023"], "Same EA Play Pro plan family; monthly/annual billing variants."),
    ("KUANGCHUAN-SOY-DRINK", ["B09-C04-029", "B09-C04-030"], "Checkpoint notes identify two related Kuang Chuan 375 ml soy-drink variants."),
    ("PURE-CUI-COFFEE", ["B09-C07-002", "B09-C07-003"], "Checkpoint notes identify two Pure Clean coffee flavors in one family."),
    ("UNIFIED-TEA-COLLECTION", ["B09-C07-012", "B09-C07-013"], "Checkpoint notes identify red and green milk-tea variants."),
    ("HUCC-TILAPIA", ["B09-C08-012", "B09-C08-013"], "Checkpoint notes identify skinless and skin-on variants."),
    ("THSRC-TAICHUNG-P1-PARKING", ["B09-C08-016", "B09-C08-017"], "Same Taichung P1 site; hourly rate and daily maximum are two distinct tariff units."),
]


LINKS: dict[str, list[dict[str, str]]] = {
    "B09-C01-017": [
        ("NEW-LEISURE-APPLE-ARCADE-MONTHLY", "REJECTED_DIFFERENT_CONCEPT", "Apple One bundles Apple services; standalone Apple Arcade is only a component, not the same plan."),
    ],
    "B09-C03-008": [
        ("NEW-LEISURE-DINGDONG-ADULT", "REJECTED_DIFFERENT_CONCEPT", "Different park/operator and admission concept."),
        ("NEW-LEISURE-EDA-ADULT", "REJECTED_DIFFERENT_CONCEPT", "Different park/operator and admission concept."),
        ("NEW-LEISURE-NINE-ADULT", "REJECTED_DIFFERENT_CONCEPT", "Different park/operator and admission concept."),
    ],
    "B09-C04-001": [
        ("LEG-EC-156", "REJECTED_DIFFERENT_CONCEPT", "MUJI cotton pads are not a facial foaming net."),
        ("LEG-EC-161", "REJECTED_DIFFERENT_CONCEPT", "MUJI cotton pads are not a facial foaming net."),
    ],
    "B09-C04-009": [
        ("LEG-EC-178", "REJECTED_DIFFERENT_CONCEPT", "A4 file box dimensions differ from the existing deep storage box."),
    ],
    "B09-C05-009": [
        ("LEG-EC-015", "REJECTED_DIFFERENT_CONCEPT", "Existing candidate is Pure Tea red tea; this row is unsweetened green tea."),
    ],
    "B09-C05-014": [
        ("LEG-EC-150", "REJECTED_DIFFERENT_CONCEPT", "Anti-sensitivity gum-care 120 g differs from the existing triple-action 160 g product."),
        ("LEG-EC-149", "REJECTED_DIFFERENT_CONCEPT", "Different toothpaste formula and multi-pack concept."),
    ],
    "B09-C05-018": [
        ("LEG-EC-175", "REJECTED_DIFFERENT_CONCEPT", "Facial tissue multipack differs from existing toilet-roll product and unit."),
    ],
    "B09-C06-008": [
        ("LEG-EC-320", "REJECTED_DIFFERENT_CONCEPT", "A 24-can 250 ml case differs from the existing 600 ml single bottle."),
    ],
    "B09-C06-027": [
        ("NEW-CLOTH-VANS-OLDSKOOL-VN000D3HY28", "EXISTING_PAIR_ALREADY_PRESENT", "Same exact VN000D3HY28 model and black-white variant; Candidate Pool already has 2020 and 2026 quotes, so Batch 9 adds no gap reduction."),
    ],
    "B09-C06-028": [
        ("NEW-CLOTH-NIID-R1", "EXISTING_PAIR_ALREADY_PRESENT", "Same R1 series; Candidate Pool already has 2020 and 2026 quotes. The 2020 SKU/EAN lineage remains unverified, so this row does not improve the candidate."),
    ],
    "B09-C07-010": [
        ("LEG-EC-315", "CONDITIONAL_CONCEPT_MATCH", "Same named 1 kg Taiyen iodized salt; 2020 report does not identify store/barcode and 2026 quotes are multiple retailers."),
    ],
    "B09-C08-016": [
        ("LEG-EC-042", "EXACT_CONCEPT_MATCH", "Same Dudu House/Taichung THSRC P1 parking facility, car hourly rate, location, and tariff definition; 2020 and 2026 official rate pages read successfully."),
    ],
    "B09-C08-017": [
        ("LEG-EC-041", "EXACT_CONCEPT_MATCH", "Same Dudu House/Taichung THSRC P1 parking facility, car daily maximum, location, and tariff definition; the cap is not an average payment."),
    ],
}


def normalize(value: str) -> str:
    value = value.lower()
    return re.sub(r"[^0-9a-z\u4e00-\u9fff]+", "", value)


def cjk_grams(value: str, size: int = 2) -> set[str]:
    normalized = normalize(value)
    return {normalized[i : i + size] for i in range(max(0, len(normalized) - size + 1))}


def jaccard(left: set[str], right: set[str]) -> float:
    return len(left & right) / len(left | right) if left | right else 0.0


def build_groups(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    mapping = group_assignments({row["brand_or_merchant"] for row in rows})
    write_csv(GROUP_PATH, ["brand_or_merchant", "corporate_group_id", "attribution_status", "attribution_basis"], list(mapping.values()))
    return mapping


def build_families(rows: list[dict[str, str]]) -> None:
    id_to_group: dict[str, tuple[str, str]] = {}
    for family_key, ids, basis in FAMILY_GROUPS:
        for rid in ids:
            id_to_group[rid] = (family_key, basis)
    family_rows = []
    for row in rows:
        rid = row["research_id"]
        if rid in id_to_group:
            family_key, basis = id_to_group[rid]
            review_status = "EXPLICIT_MULTI_VARIANT_FAMILY"
        elif row["product_family_count"] == "2":
            family_key = f"UNRESOLVED_EXTERNAL::{rid}"
            basis = "Ledger declares two variants, but no same-batch counterpart was confidently assigned in this audit."
            review_status = "DECLARED_FAMILY_UNRESOLVED"
        else:
            family_key = f"SINGLETON::{rid}"
            basis = "No same-batch family counterpart identified; unique row key retained."
            review_status = "SINGLETON_IN_FIXED_BATCH"
        family_rows.append({
            "research_id": rid,
            "family_key": family_key,
            "declared_family_count": row["product_family_count"],
            "review_status": review_status,
            "basis": basis,
        })
    write_csv(FAMILY_PATH, ["research_id", "family_key", "declared_family_count", "review_status", "basis"], family_rows)


def build_links(rows: list[dict[str, str]], pool: list[dict[str, str]]) -> tuple[dict[str, list[dict[str, str]]], list[dict[str, str]]]:
    pool_by_id = {row["candidate_id"]: row for row in pool}
    links_by_research: dict[str, list[dict[str, str]]] = defaultdict(list)
    link_rows = []
    for row in rows:
        rid = row["research_id"]
        selected = LINKS.get(rid)
        if not selected:
            selected = [("", "NO_CONFIRMED_LINK", "No exact product/service identity link was confirmed in the 418-row Candidate Pool review; name/category similarity alone is insufficient.")]
        for candidate_id, state, reason in selected:
            candidate = pool_by_id.get(candidate_id, {})
            record = {
                "research_id": rid,
                "candidate_id": candidate_id,
                "link_state": state,
                "candidate_pool_rows_reviewed": str(len(pool)),
                "existing_2020_quote_count": candidate.get("exact2020_quote_count", ""),
                "existing_2026_quote_count": candidate.get("current2026_quote_count", ""),
                "gap_reduction_if_admitted": "1" if state in {"EXACT_CONCEPT_MATCH", "CONDITIONAL_CONCEPT_MATCH"} and candidate.get("exact2020_quote_count") == "0" else "0",
                "adjudication_reason": reason,
            }
            link_rows.append(record)
            links_by_research[rid].append(record)
    fields = ["research_id", "candidate_id", "link_state", "candidate_pool_rows_reviewed", "existing_2020_quote_count", "existing_2026_quote_count", "gap_reduction_if_admitted", "adjudication_reason"]
    write_csv(LINK_PATH, fields, link_rows)
    return links_by_research, link_rows


def build_top_matches(rows: list[dict[str, str]], pool: list[dict[str, str]], links: list[dict[str, str]]) -> None:
    manual = {(r["research_id"], r["candidate_id"]): r for r in links if r["candidate_id"]}
    ranked_rows = []
    for row in rows:
        row_brand = normalize(row["brand_or_merchant"])
        row_blob = " ".join([row["concept"], row["specification"], row["model_sku_plan"], row["channel_geography"]])
        row_grams = cjk_grams(row_blob)
        candidates = []
        for candidate in pool:
            candidate_blob = " ".join([candidate["representative_item"], candidate["representative_spec"], candidate["brands"], candidate["channel_regions"]])
            candidate_brand = normalize(candidate["brands"])
            brand_match = bool(row_brand and (row_brand in candidate_brand or candidate_brand in row_brand))
            subcategory_match = normalize(row["subcategory"]) == normalize(candidate["ho600_subcategory"])
            concept_similarity = SequenceMatcher(None, normalize(row["concept"]), normalize(candidate["representative_item"])).ratio()
            tokens = re.findall(r"[A-Za-z0-9]{4,}", row_blob.lower())
            pool_tokens = set(re.findall(r"[A-Za-z0-9]{4,}", candidate_blob.lower()))
            sku_match = any(token in pool_tokens for token in tokens)
            score = 0.50 * jaccard(row_grams, cjk_grams(candidate_blob)) + 0.20 * brand_match + 0.20 * subcategory_match + 0.05 * sku_match + 0.05 * concept_similarity
            candidates.append((score, brand_match, subcategory_match, sku_match, concept_similarity, candidate))
        candidates.sort(key=lambda item: item[0], reverse=True)
        for rank, (score, brand_match, sub_match, sku_match, similarity, candidate) in enumerate(candidates[:5], start=1):
            manual_link = manual.get((row["research_id"], candidate["candidate_id"]))
            if manual_link:
                status = manual_link["link_state"]
                reason = manual_link["adjudication_reason"]
            else:
                status = "NEAR_MATCH_REVIEWED_NO_IDENTITY"
                reason = "Ranked name/category/specification similarity only; no exact SKU, service unit, branch, and channel identity was verified."
            ranked_rows.append({
                "research_id": row["research_id"],
                "rank": str(rank),
                "candidate_id": candidate["candidate_id"],
                "score": f"{score:.4f}",
                "brand_match": str(brand_match).upper(),
                "subcategory_match": str(sub_match).upper(),
                "sku_token_match": str(sku_match).upper(),
                "concept_similarity": f"{similarity:.4f}",
                "adjudication": status,
                "reason": reason,
            })
    write_csv(NEAR_MATCH_PATH, ["research_id", "rank", "candidate_id", "score", "brand_match", "subcategory_match", "sku_token_match", "concept_similarity", "adjudication", "reason"], ranked_rows)


def source_info(url: str, receipts: dict[str, dict[str, str]]) -> dict[str, str]:
    receipt = receipts.get(url)
    if not receipt:
        return {"id": "NOT_RECORDED", "final": "", "status": "NOT_RECORDED", "tls": "NOT_VERIFIED", "sha": ""}
    result = receipt.get("result", "")
    status = receipt.get("http_status", "") or "TLS_ERROR"
    tls = receipt.get("tls_validation", "NOT_RECORDED")
    if not tls:
        tls = "NOT_RECORDED"
    rid = receipt.get("receipt_id") or f"READBACK-{hashlib.sha256((url + receipt.get('sha256','')).encode()).hexdigest()[:12].upper()}"
    return {"id": rid, "final": receipt.get("final_url", ""), "status": status, "tls": tls, "sha": receipt.get("sha256", "")}


def row_status(row: dict[str, str], links: list[dict[str, str]], src20: dict[str, str], src26: dict[str, str]) -> tuple[str, str, str]:
    rid = row["research_id"]
    if rid == "B09-C03-008":
        return (
            "HOLD",
            "The cited page was published in 2021 and displays adult NT$850 without tying that tariff to 2020; Wayback CDX returned zero 2020 official-page snapshots. This cannot establish an Exact-2020 baseline.",
            "Contemporaneous 2020 official tariff or a dated 2020 official capture that explicitly shows normal adult price; do not substitute the 2021 page.",
        )
    exact = [link for link in links if link["link_state"] == "EXACT_CONCEPT_MATCH"]
    if exact and src20["status"] == "200" and src26["status"] == "200" and "PASS" in src20["tls"] and "PASS" in src26["tls"]:
        return (
            "EXACT_READY_CANDIDATE",
            exact[0]["adjudication_reason"] + " Both official source bodies were read by Mac curl SecureTransport with strict TLS; the 2020 effective date and 2026 station tariff are explicit. Python OpenSSL strict probes separately failed on Missing Subject Key Identifier, so the client-verifier divergence is retained in the receipts; no TLS bypass was used.",
            "No additional source-gate gap identified in this research preaudit. Formal canonical admission remains a separate authorized workflow.",
        )

    conditional = [link for link in links if link["link_state"] in {"CONDITIONAL_CONCEPT_MATCH", "EXISTING_PAIR_ALREADY_PRESENT"}]
    missing: list[str] = []
    for period, source in (("2020", src20), ("2026", src26)):
        if source["status"] != "200":
            missing.append(f"{period} source body not readable in this strict-TLS check (HTTP {source['status']}).")
        if "FAIL" in source["tls"]:
            missing.append(f"{period} certificate/hostname validation failed; do not bypass TLS.")
        elif source["tls"] == "NOT_VERIFIED":
            missing.append(f"{period} source has no source-readability receipt in this audit.")
    if rid == "B09-C07-010":
        missing.append("2020 report lacks seller/store and barcode; reconcile the reported 1 kg product with the existing Candidate Pool retail concept.")
    if rid == "B09-C06-027":
        missing.append("2020 annual marketplace page does not give an exact observation date; existing Candidate Pool already has a 2020/2026 pair, so no current-only gap is reduced.")
    if rid == "B09-C06-028":
        missing.append("2020 source lacks exact SKU/EAN lineage; existing Candidate Pool already has a 2020/2026 series-level pair, so no current-only gap is reduced.")
    if rid == "B09-C03-007":
        missing.append("2026 official Vieshow page returned HTTP 403; independently re-read the current normal 2D adult fare before admission.")
    if rid == "B09-C03-014":
        missing.append("2026 reseller shows a starting price, not a confirmed operator normal weekday tariff.")
    if row["evidence_grade_2020"] == "C" and rid not in {"B09-C03-008", "B09-C03-010", "B09-C03-013"}:
        missing.append("2020 evidence is grade C; retain source-level corroboration and do not promote from the grade label alone.")
    if conditional or missing:
        reason = "; ".join(missing) if missing else "A candidate-pool linkage is present, but the 2020/2026 evidence needs row-specific identity and source review."
        return "NEEDS_EVIDENCE", reason, reason

    if src20["status"] != "200" or src26["status"] != "200" or "FAIL" in src20["tls"] or "FAIL" in src26["tls"]:
        reason = "; ".join(missing) if missing else f"Source readability failed or was blocked (2020 HTTP {src20['status']}; 2026 HTTP {src26['status']}); no alternate source was substituted."
        return "NEEDS_EVIDENCE", reason, reason

    if rid in {"B09-C03-010", "B09-C03-013"}:
        reason = "Both source bodies are readable and the dated 2020 visitor pages state general-admission prices, but the 2020 evidence remains third-party grade C and no same-concept Candidate Pool gap was identified."
        return "RESEARCH_ONLY", reason, "Independent 2020 operator tariff or equivalent corroboration; a validated same-concept Candidate Pool link if this should reduce an existing gap."

    reason = "Source URLs passed strict-TLS body readability, but no same-identity Candidate Pool concept was confirmed for this fixed row. The ledger's ADMISSIBLE label is research intake only and does not itself satisfy formal Exact review."
    return "RESEARCH_ONLY", reason, "If proposed for formal Exact later: independently re-check both source bodies for normal price, exact item/service identity, specification, channel/branch, and date; perform a candidate-pool identity check before adding a concept."


def build_matrix(rows: list[dict[str, str]], groups: dict[str, dict[str, str]], links_by_research: dict[str, list[dict[str, str]]], receipts: dict[str, dict[str, str]]) -> list[dict[str, str]]:
    result = []
    for row in rows:
        rid = row["research_id"]
        src20 = source_info(row["source_2020"], receipts)
        src26 = source_info(row["source_2026"], receipts)
        links = links_by_research.get(rid, [])
        status, reason, missing = row_status(row, links, src20, src26)
        group = groups[row["brand_or_merchant"]]
        if rid in {"B09-C08-016", "B09-C08-017"}:
            semantics20 = "OFFICIAL_FIXED_TARIFF; 2020 effective date and charge unit stated"
            semantics26 = "OFFICIAL_FIXED_TARIFF; 2026 station page lists the same charge unit"
            identity = "SAME_TAICHUNG_P1_SITE_AND_VEHICLE_TARIFF_UNIT_VERIFIED"
            channel = "SAME_STATION_P1; source page identifies Dudu House parking operator"
        elif rid == "B09-C07-010":
            semantics20 = "REPORTED_RETAIL_PRICE; no promotion stated; seller not identified"
            semantics26 = "PXGO_LISTED_ITEM_PRICE; no crossed-out promotion in recorded page"
            identity = "1KG_PRODUCT_NAME_MATCH; 2020 BARCODE_UNVERIFIED"
            channel = "2020 SELLER_UNKNOWN; 2026 PXGO; RETAIL_CHANNEL_CONTINUITY_UNPROVEN"
        elif rid == "B09-C03-008":
            semantics20 = "NOT_ESTABLISHED_FOR_2020; cited page published 2021"
            semantics26 = "OFFICIAL_CURRENT_ADULT_LIST_PRICE; current discount excluded"
            identity = "ADULT_TICKET_IDENTIFIED; HISTORICAL_YEAR_LINK_NOT_ESTABLISHED"
            channel = "TAOYUAN PARK; HISTORICAL OFFICIAL TARIFF NOT FOUND"
        else:
            notes = row["notes"]
            promo_explicit = any(term in notes for term in ("原價", "正常價", "原標價", "牌告", "不採促銷", "促銷價排除", "優惠價排除"))
            semantics20 = "LEDGER_NOTES_IDENTIFY_NORMAL_OR_LIST_PRICE; source-body semantics not independently re-extracted" if promo_explicit else "PRICE_SEMANTICS_NOT_REVERIFIED"
            semantics26 = "LEDGER_NOTES_IDENTIFY_NORMAL_OR_LIST_PRICE; source-body semantics not independently re-extracted" if promo_explicit else "PRICE_SEMANTICS_NOT_REVERIFIED"
            identity = "LEDGER_IDENTITY_ASSERTION; SKU/LINEAGE LIMITS REMAIN IN NOTES"
            channel = "LEDGER_CHANNEL_ASSERTION; row-specific operator/channel review remains"
        result.append({
            "research_id": rid,
            "checkpoint": rid.split("-")[1],
            "candidate_pool_ids": ";".join(sorted({link["candidate_id"] for link in links if link["candidate_id"]})) or "NONE_CONFIRMED",
            "candidate_link_state": ";".join(sorted({link["link_state"] for link in links})),
            "domain": row["domain"],
            "subcategory": row["subcategory"],
            "brand_or_merchant": row["brand_or_merchant"],
            "corporate_group_id": group["corporate_group_id"],
            "corporate_group_status": group["attribution_status"],
            "concept": row["concept"],
            "model_sku_plan": row["model_sku_plan"],
            "specification": row["specification"],
            "channel_geography": row["channel_geography"],
            "source_2020": row["source_2020"],
            "source_2020_final_url": src20["final"],
            "date_2020": row["date_2020"],
            "price_2020": row["normal_price_2020"],
            "source_2020_receipt_id": src20["id"],
            "source_2020_http_status": src20["status"],
            "source_2020_tls_status": src20["tls"],
            "source_2020_sha256": src20["sha"],
            "source_2026": row["source_2026"],
            "source_2026_final_url": src26["final"],
            "date_2026": row["date_2026"],
            "price_2026": row["normal_price_2026"],
            "source_2026_receipt_id": src26["id"],
            "source_2026_http_status": src26["status"],
            "source_2026_tls_status": src26["tls"],
            "source_2026_sha256": src26["sha"],
            "normal_vs_promo_2020": semantics20,
            "normal_vs_promo_2026": semantics26,
            "sku_identity_check": identity,
            "channel_spec_check": channel,
            "comparability": row["comparability"],
            "evidence_grade_2020": row["evidence_grade_2020"],
            "evidence_grade_2026": row["evidence_grade_2026"],
            "decision": row["decision"],
            "preaudit_status": status,
            "reason": reason,
            "missing_evidence": missing,
            "formal_exact_delta": "1 candidate; not yet admitted" if status == "EXACT_READY_CANDIDATE" else "0 formal Exact; research status unchanged",
        })
    fields = list(result[0])
    write_csv(MATRIX_PATH, fields, result)
    return result


def build_candidate_list(rows: list[dict[str, str]], matrix: list[dict[str, str]], links: list[dict[str, str]], pool: list[dict[str, str]]) -> None:
    by_row = {row["research_id"]: row for row in rows}
    by_matrix = {row["research_id"]: row for row in matrix}
    pool_by_id = {row["candidate_id"]: row for row in pool}
    selected = [link for link in links if link["candidate_id"]]
    out = []
    for link in selected:
        rid = link["research_id"]
        row = by_row[rid]
        matrix_row = by_matrix[rid]
        candidate = pool_by_id[link["candidate_id"]]
        out.append({
            "candidate_id": link["candidate_id"],
            "research_id": rid,
            "preaudit_status": matrix_row["preaudit_status"],
            "link_state": link["link_state"],
            "existing_2020_quote_count": candidate.get("exact2020_quote_count", ""),
            "existing_2026_quote_count": candidate.get("current2026_quote_count", ""),
            "price_2020": row["normal_price_2020"],
            "price_2026": row["normal_price_2026"],
            "source_2020": row["source_2020"],
            "source_2026": row["source_2026"],
            "confirmed_gap_reduction_if_admitted": "1" if link["link_state"] == "EXACT_CONCEPT_MATCH" and candidate.get("exact2020_quote_count") == "0" else "0",
            "additional_conditional_gap_reduction_after_evidence": "1" if link["link_state"] == "CONDITIONAL_CONCEPT_MATCH" and candidate.get("exact2020_quote_count") == "0" else "0",
            "remaining_gate_or_adjudication": matrix_row["missing_evidence"],
            "reason": link["adjudication_reason"],
        })
    fields = ["candidate_id", "research_id", "preaudit_status", "link_state", "existing_2020_quote_count", "existing_2026_quote_count", "price_2020", "price_2026", "source_2020", "source_2026", "confirmed_gap_reduction_if_admitted", "additional_conditional_gap_reduction_after_evidence", "remaining_gate_or_adjudication", "reason"]
    write_csv(CANDIDATE_PATH, fields, out)


def write_notebook() -> None:
    cells = [
        {"cell_type": "markdown", "metadata": {}, "source": ["# Batch 9 Exact-admission preaudit\n", "Reproduce the 160-row status counts from the fixed ledgers and inspect the three existing Candidate Pool gap concepts. This notebook performs no admission or workbook write."]},
        {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": ["import csv\n", "from collections import Counter\n", "from pathlib import Path\n", "\n", "base = Path('research/batch-09')\n", "with (base / 'exact-admission-preaudit-2026-10-30.csv').open(encoding='utf-8-sig', newline='') as f:\n", "    matrix = list(csv.DictReader(f))\n", "assert len(matrix) == 160\n", "Counter(row['preaudit_status'] for row in matrix)\n"]},
        {"cell_type": "code", "execution_count": None, "metadata": {}, "outputs": [], "source": ["with (base / 'exact-admission-candidate-list-2026-10-30.csv').open(encoding='utf-8-sig', newline='') as f:\n", "    candidates = list(csv.DictReader(f))\n", "[(row['candidate_id'], row['research_id'], row['preaudit_status'], row['confirmed_gap_reduction_if_admitted'], row['additional_conditional_gap_reduction_after_evidence']) for row in candidates if row['link_state'] == 'EXACT_CONCEPT_MATCH' or row['link_state'] == 'CONDITIONAL_CONCEPT_MATCH']\n"]},
        {"cell_type": "markdown", "metadata": {}, "source": ["Current-only gap reduction remains conditional on later authorized admission. The two exact-ready rows are review candidates; no formal count was changed by this research preaudit."]},
    ]
    notebook = {"cells": cells, "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}, "language_info": {"name": "python", "version": "3"}}, "nbformat": 4, "nbformat_minor": 5}
    NOTEBOOK_PATH.write_text(json.dumps(notebook, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    rows = fixed_rows()
    _, pool = read_csv(POOL_PATH)
    if len(rows) != 160 or len(pool) != 418:
        raise SystemExit(f"expected 160 fixed rows and 418 Candidate Pool concepts; got {len(rows)} and {len(pool)}")
    brands = build_groups(rows)
    build_families(rows)
    links_by_research, links = build_links(rows, pool)
    build_top_matches(rows, pool, links)
    receipts = load_receipts()
    matrix = build_matrix(rows, brands, links_by_research, receipts)
    build_candidate_list(rows, matrix, links, pool)
    write_notebook()
    status_counts = Counter(row["preaudit_status"] for row in matrix)
    source_rows = {}
    for name in [
        "source-readability-receipts-2026-10-30.csv",
        "source-readability-c01-c05-2026-10-30.csv",
        "c03-grade-source-readback-2026-10-30.csv",
        "exact-candidate-source-receipts-2026-10-30.csv",
    ]:
        path = BASE / name
        if path.exists():
            _, receipt_rows = read_csv(path)
            source_rows[name] = dict(Counter(r.get("result", "") + ":" + (r.get("http_status", "") or "") for r in receipt_rows))
    try:
        head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    except Exception:
        head = "NOT_READ"
    summary = {
        "generated_at_utc": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "base_head": head,
        "fixed_ledger_rows": len(rows),
        "candidate_pool_rows_compared": len(pool),
        "preaudit_status_counts": dict(status_counts),
        "exact_ready_candidate_count": status_counts.get("EXACT_READY_CANDIDATE", 0),
        "confirmed_current_only_gap_reduction_if_admitted": sum(int(r["gap_reduction_if_admitted"]) for r in links if r["link_state"] == "EXACT_CONCEPT_MATCH"),
        "conditional_current_only_gap_reduction_after_evidence": sum(int(r["gap_reduction_if_admitted"]) for r in links if r["link_state"] == "CONDITIONAL_CONCEPT_MATCH"),
        "upper_bound_current_only_gap_reduction_if_all_three_pass": sum(int(r["gap_reduction_if_admitted"]) for r in links if r["link_state"] in {"EXACT_CONCEPT_MATCH", "CONDITIONAL_CONCEPT_MATCH"}),
        "formal_exact_count_before_and_after_research": 181,
        "formal_exact_delta": 0,
        "basket": "NOT SEALED",
        "index": "LOCKED",
        "source_readability_http_counts": source_rows,
        "notes": [
            "Exact-ready candidates remain research-branch review candidates, not formal admissions.",
            "Corporate owners not affirmatively consolidated are marked UNRESOLVED_SINGLETON; reported group maxima are a verified lower bound.",
            "The source-readability probe verifies strict TLS and HTTP response/body availability only; it does not prove the price text by itself.",
            "Python urllib/OpenSSL strict validation failed on 10 of 229 URLs (including both THSRC pages); direct Mac curl SecureTransport strict verification returned HTTP 200 and ssl_verify_result=0 for the two THSRC candidate pages. Both outcomes are retained; no verifier was weakened.",
        ],
    }
    SUMMARY_PATH.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
