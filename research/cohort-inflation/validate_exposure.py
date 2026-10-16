#!/usr/bin/env python3
"""Offline structural audit for HO600 cohort exposure research.

Run from any working directory:
    python research/cohort-inflation/validate_exposure.py

This checks crosswalk integrity ONLY. It never calculates or certifies inflation.
GitHub Actions must remain unused unless explicitly reauthorized.
"""
from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
TIERS = {"HIGH", "MEDIUM", "LOW", "CONDITIONAL"}
PRICE_FIELD_FRAGMENTS = ("normal_price", "price_change", "pct_change", "percent_change", "漲幅", "漲跌")


def read_records(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        fields = list(reader.fieldnames or [])
        rows = list(reader)
    assert len(fields) == len(set(fields)), f"Duplicate fields: {path}"
    assert all(None not in row for row in rows), f"Columns mismatched: {path}"
    return fields, rows


def check() -> dict[str, object]:
    status = json.loads((ROOT / "canonical/status.json").read_text(encoding="utf-8"))
    _, candidates = read_records(ROOT / "data/Candidate_Pool.csv")
    map_fields, mapping = read_records(HERE / "exposure-map-v0.csv")
    audit_fields, audit = read_records(HERE / "candidate-exposure-v0.csv")

    assert status["basket_sealed"] is False and status["index_status"] == "LOCKED", "Invalid WIP state"
    assert len(candidates) == int(status["candidate_concepts"]), "Canonical candidate count drift"
    assert len(mapping) == 50 and len(audit) == len(candidates), "Research coverage drift"

    # Source quota CSV uses a title row above its actual column names: parse the
    # two identifying fields directly from raw CSV rather than assuming standard headers.
    with (ROOT / "data/Quota_Control.csv").open(encoding="utf-8-sig", newline="") as fh:
        raw_quotas = list(csv.reader(fh))
    canonical_pairs = {
        (row[0], row[1]) for row in raw_quotas
        if len(row) >= 9 and row[0] in {"食", "衣", "住／家用", "行", "育", "樂", "日常／個人"}
        and row[1] and not row[1].replace(".", "", 1).isdigit()
        and row[5].strip().isdigit()
    }
    mapped_pairs = [(row["domain"], row["subcategory"]) for row in mapping]
    assert len(mapped_pairs) == len(set(mapped_pairs)), "Duplicate subcategory key"
    assert set(mapped_pairs) == canonical_pairs and len(canonical_pairs) == 50, "Missing / extra quota keys"

    ids = [row["candidate_id"] for row in candidates]
    audit_ids = [row["candidate_id"] for row in audit]
    assert len(ids) == len(set(ids)) and len(audit_ids) == len(set(audit_ids)), "Duplicate candidate ID"
    assert set(ids) == set(audit_ids), "Unmapped / invented candidate ID"

    for field in map_fields + audit_fields:
        assert not any(term in field.lower() for term in PRICE_FIELD_FRAGMENTS), "Price-leaking field"

    rules = {(r["domain"], r["subcategory"]): r for r in mapping}
    by_id = {r["candidate_id"]: r for r in candidates}
    for row in mapping:
        assert row["worker_touchpoint"] in TIERS and row["retiree_touchpoint"] in TIERS, "Invalid tier"
        assert row["weight_status"] == "NOT_CALIBRATED" and row["lifecycle"] == "RESEARCH_ONLY"
    for row in audit:
        candidate = by_id[row["candidate_id"]]
        assert row["domain"] == candidate["ho600_domain"] and row["subcategory"] == candidate["ho600_subcategory"]
        assert row["migration_state"] == candidate["migration_state"]
        assert row["exact2020_quote_count"] == candidate["exact2020_quote_count"]
        assert row["current2026_quote_count"] == candidate["current2026_quote_count"]
        rule = rules[(row["domain"], row["subcategory"])]
        assert row["worker_touchpoint"] == rule["worker_touchpoint"]
        assert row["retiree_touchpoint"] == rule["retiree_touchpoint"]
        assert row["exposure_basis"] == rule["basis"]
        assert row["mapped_state"] == "HEURISTIC_UNVALIDATED"
        assert row["do_not_impute_weights"] == "TRUE"

    exact = sum(int(r["exact2020_quote_count"] or 0) > 0 and int(r["current2026_quote_count"] or 0) > 0 for r in candidates)
    assert exact == int(status["formal_exact_concepts"]), "Exact prequalified status drift"
    receipt = {
        "status": "PASS_STRUCTURAL_ONLY",
        "canonical_exact": exact,
        "candidate_count": len(candidates),
        "quota_subcategories": len(mapping),
        "candidate_exposure_rows": len(audit),
        "working_tiers": dict(Counter(r["worker_touchpoint"] for r in audit)),
        "retired_tiers": dict(Counter(r["retiree_touchpoint"] for r in audit)),
        "cohort_spend_weights_verified": False,
        "cohort_inflation_calculated": False,
    }
    return receipt


if __name__ == "__main__":
    print(json.dumps(check(), ensure_ascii=False, indent=2, sort_keys=True))
