#!/usr/bin/env python3
"""Independent Fraction-based verification of the Taipei partial CPI output."""
from __future__ import annotations

import argparse
import csv
from decimal import Decimal
from fractions import Fraction
import json
from pathlib import Path


def dec_fraction(value: str) -> Fraction:
    return Fraction(Decimal(value))


def month_key(value: str) -> tuple[int, int]:
    year_text, month_text = value.strip().replace("月", "").split("年", 1)
    year = int(year_text.strip())
    if year < 200:
        year += 1911
    return year, int(month_text.strip())


def year_key(value: str) -> int:
    year = int(value.strip().removesuffix("年"))
    return year + 1911 if year < 200 else year


def as_decimal(value: Fraction) -> Decimal:
    return Decimal(value.numerator) / Decimal(value.denominator)


def near(left: str, right: Fraction) -> Decimal:
    return abs(Decimal(left) - as_decimal(right))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--monthly", required=True, type=Path)
    ap.add_argument("--annual", required=True, type=Path)
    ap.add_argument("--weights", required=True, type=Path)
    ap.add_argument("--crosswalk", required=True, type=Path)
    ap.add_argument("--analysis-json", required=True, type=Path)
    ap.add_argument("--contributions-csv", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    args = ap.parse_args()
    if args.out.exists():
        raise FileExistsError("No independent receipt overwrite")

    with args.monthly.open(encoding="utf-8-sig", newline="") as f:
        monthly_rows = list(csv.DictReader(f))
    with args.annual.open(encoding="utf-8-sig", newline="") as f:
        annual_rows = list(csv.DictReader(f))
    with args.weights.open(encoding="utf-8-sig", newline="") as f:
        weight_rows = list(csv.DictReader(f))
    with args.crosswalk.open(encoding="utf-8-sig", newline="") as f:
        crosswalk_rows = list(csv.DictReader(f))
    analysis = json.loads(args.analysis_json.read_text(encoding="utf-8"))
    with args.contributions_csv.open(encoding="utf-8-sig", newline="") as f:
        contribution_rows = list(csv.DictReader(f))

    monthly = {(month_key(r["統計期"]), r["基本分類"]): dec_fraction(r["原始值[統計數值]"]) for r in monthly_rows}
    annual = {(year_key(r["統計期"]), r["基本分類"]): dec_fraction(r["原始值[統計數值]"]) for r in annual_rows}
    weights = {(r["household_head_age_group"], int(r["category_number"])): Fraction(int(r["annual_expenditure_nt_per_household"]), int(r["sum_of_12_categories_nt"])) for r in weight_rows}
    ages = list(dict.fromkeys(r["household_head_age_group"] for r in weight_rows))
    category_labels = {int(r["category_number"]): r["category_label_zh"] for r in weight_rows}
    mapped = {int(r["expense_division"]): r["taipei_cpi_basic_classifications"].strip() for r in crosswalk_rows if r["mapping_status"] == "MAPPED"}
    if set(mapped) != {3, 9, 10}:
        raise ValueError(f"Unexpected accepted mapping set: {sorted(mapped)}")

    specs = {
        "A_2020_JAN_SEP_TO_2026_JAN_SEP": "monthly",
        "B_2020_FULL_YEAR_TO_2025_FULL_YEAR": "annual",
    }
    summary_expected = {}
    contribution_expected = {}
    for comparison, kind in specs.items():
        relatives = {}
        for cat, label in mapped.items():
            if kind == "monthly":
                base = sum((monthly[((2020, m), label)] for m in range(1, 10)), Fraction(0)) / 9
                target = sum((monthly[((2026, m), label)] for m in range(1, 10)), Fraction(0)) / 9
            else:
                base, target = annual[(2020, label)], annual[(2025, label)]
            relatives[cat] = (base, target, target / base)
        general_label = "總指數"
        if kind == "monthly":
            general_base = sum((monthly[((2020, m), general_label)] for m in range(1, 10)), Fraction(0)) / 9
            general_target = sum((monthly[((2026, m), general_label)] for m in range(1, 10)), Fraction(0)) / 9
        else:
            general_base, general_target = annual[(2020, general_label)], annual[(2025, general_label)]
        general_change = (general_target / general_base - 1) * 100
        for age in ages:
            coverage = sum((weights[(age, cat)] for cat in mapped), Fraction(0))
            partial = Fraction(0)
            for cat, (base, target, relative) in relatives.items():
                weight = weights[(age, cat)]
                pp = weight * (relative - 1) * 100
                partial += pp
                contribution_expected[(comparison, age, cat)] = (weight, base, target, relative, pp, coverage, 1 - coverage)
            summary_expected[(comparison, age)] = (coverage, 1 - coverage, partial, general_change)

    summary_errors = []
    summary_rows = analysis["age_head_partial_summary"]
    if len(summary_rows) != len(summary_expected):
        summary_errors.append("summary row count")
    max_delta = Decimal(0)
    for row in summary_rows:
        key = (row["comparison"], row["household_head_age_group"])
        expected = summary_expected.get(key)
        if expected is None:
            summary_errors.append(f"unexpected summary key {key}")
            continue
        for field, fraction in zip(("mapped_coverage_share", "uncovered_share", "partial_mapped_contribution_percentage_points", "official_general_cpi_change_percent"), expected):
            delta = near(row[field], fraction)
            max_delta = max(max_delta, delta)
            if delta > Decimal("0.000000000001"):
                summary_errors.append(f"{key} {field} differs by {delta}")

    csv_errors = []
    if len(contribution_rows) != len(contribution_expected):
        csv_errors.append(f"contribution row count {len(contribution_rows)} != {len(contribution_expected)}")
    seen = set()
    fields = ("weight_share_2020", "baseline_index", "target_index", "price_relative", "contribution_percentage_points", "mapped_coverage_share", "uncovered_share")
    for row in contribution_rows:
        key = (row["comparison"], row["household_head_age_group"], int(row["expense_division"]))
        if key in seen:
            csv_errors.append(f"duplicate contribution {key}")
            continue
        seen.add(key)
        expected = contribution_expected.get(key)
        if expected is None:
            csv_errors.append(f"unexpected contribution key {key}")
            continue
        for field, fraction in zip(fields, expected):
            delta = near(row[field], fraction)
            max_delta = max(max_delta, delta)
            if delta > Decimal("0.000000000001"):
                csv_errors.append(f"{key} {field} differs by {delta}")
        if row["full_rate_release"] != "NO_HOLD":
            csv_errors.append(f"full-rate gate not held for {key}")

    result = {
        "status": "PASS_INDEPENDENT_FRACTION_RECALCULATION" if not summary_errors and not csv_errors else "FAIL_INDEPENDENT_RECALCULATION",
        "method": "Independent Fraction arithmetic from original official CSVs and 2020 spending records; no import of the primary analysis module",
        "summaries_checked": len(summary_rows),
        "contribution_rows_checked": len(contribution_rows),
        "expected_mapped_classes": mapped,
        "max_abs_numeric_delta": str(max_delta),
        "summary_errors": summary_errors,
        "contribution_errors": csv_errors,
        "full_age_head_rate_release": "HOLD_NO_NORMALIZATION",
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], "summaries_checked": result["summaries_checked"], "contributions_checked": result["contribution_rows_checked"], "max_abs_numeric_delta": result["max_abs_numeric_delta"], "errors": len(summary_errors) + len(csv_errors)}, ensure_ascii=False))
    if summary_errors or csv_errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
