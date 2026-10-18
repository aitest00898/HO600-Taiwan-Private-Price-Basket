#!/usr/bin/env python3
"""Validate Taipei CPI series and calculate mapped-category contributions only.

This tool is research-only. It never fills missing CPI classes, renormalizes
unmapped spending, or emits a complete cohort inflation rate below the gate.
"""
from __future__ import annotations

import argparse
import csv
from decimal import Decimal, InvalidOperation
import hashlib
import io
import json
from pathlib import Path
import re
from urllib.parse import urlsplit

OFFICIAL_HOSTS = {"data.taipei", "tsis.dbas.gov.taipei"}
AGE_WEIGHT_SOURCE = "TPE_AGE_HEAD_EXPENDITURE_PROXY_WEIGHTS_2020.csv"
REQUIRED_MAPPED_CLASSES = {1, 4, 6}
MIN_COVERAGE = Decimal("0.95")


def decode_dict_rows(raw: bytes) -> tuple[list[dict[str, str]], str]:
    for encoding in ("utf-8-sig", "cp950"):
        try:
            text = raw.decode(encoding)
            rows = list(csv.DictReader(io.StringIO(text)))
            if rows and rows[0] and None not in rows[0]:
                return rows, encoding
        except (UnicodeError, csv.Error):
            pass
    raise ValueError("Cannot decode tabular data as UTF-8-SIG or CP950")


def check_receipt(raw: bytes, receipt_path: Path, expected_source: str) -> dict:
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    if receipt.get("source_id") != expected_source:
        raise ValueError(f"Wrong receipt source_id: {receipt.get('source_id')}")
    if hashlib.sha256(raw).hexdigest() != receipt.get("sha256"):
        raise ValueError(f"SHA-256 mismatch for {expected_source}")
    if len(raw) != receipt.get("raw_bytes") or receipt.get("http_code") != 200:
        raise ValueError(f"Size or HTTP status mismatch for {expected_source}")
    if "PASS" not in receipt.get("tls_verification", ""):
        raise ValueError(f"Strict TLS receipt missing for {expected_source}")
    final = urlsplit(receipt.get("final_url", ""))
    landing = urlsplit(receipt.get("official_landing_url", ""))
    if final.scheme != "https" or final.hostname not in OFFICIAL_HOSTS:
        raise ValueError(f"Untrusted official final URL for {expected_source}")
    if landing.scheme != "https" or landing.hostname != "data.taipei":
        raise ValueError(f"Untrusted official landing URL for {expected_source}")
    return receipt


def parse_month(value: str) -> tuple[int, int]:
    text = str(value).strip().replace("民國", "").replace("西元", "")
    match = re.fullmatch(r"(\d{2,4})\s*(?:年\s*)?(\d{1,2})\s*月?", text)
    if not match:
        match = re.fullmatch(r"(\d{2,4})[/.-](\d{1,2})", text)
    if not match:
        match = re.fullmatch(r"(\d{4})(\d{2})", text)
    if not match:
        raise ValueError(f"Unrecognized monthly period: {value!r}")
    year, month = map(int, match.groups())
    if year < 200:
        year += 1911
    if not 1990 <= year <= 2100 or not 1 <= month <= 12:
        raise ValueError(f"Out-of-range monthly period: {value!r}")
    return year, month


def parse_year(value: str) -> int:
    match = re.fullmatch(r"(\d{2,4})\s*年?", str(value).strip().replace("民國", "").replace("西元", ""))
    if not match:
        raise ValueError(f"Unrecognized annual period: {value!r}")
    year = int(match.group(1))
    return year + 1911 if year < 200 else year


def make_month_grid(first: tuple[int, int], last: tuple[int, int]) -> list[tuple[int, int]]:
    out = []
    year, month = first
    while (year, month) <= last:
        out.append((year, month))
        month += 1
        if month == 13:
            year += 1
            month = 1
    return out


def load_series(raw: bytes, source: str, monthly: bool) -> tuple[dict, dict, str, set[str]]:
    rows, encoding = decode_dict_rows(raw)
    period_key = next((k for k in ("統計期", "年月別", "年別") if k in rows[0]), None)
    if not period_key or "基本分類" not in rows[0] or "原始值[統計數值]" not in rows[0] or "縣市別代碼" not in rows[0]:
        raise ValueError(f"Missing required official fields for {source}")
    values: dict[tuple, Decimal] = {}
    classes: set[str] = set()
    periods: set[tuple] = set()
    for row in rows:
        if row.get("縣市別代碼", "").strip() != "63000":
            raise ValueError(f"Non-Taipei geographic row in {source}: {row.get('縣市別代碼')!r}")
        label = row.get("基本分類", "").strip()
        if not label:
            raise ValueError(f"Blank CPI class in {source}")
        try:
            period = parse_month(row[period_key]) if monthly else parse_year(row[period_key])
            val = Decimal(row["原始值[統計數值]"].replace(",", "").strip())
        except (KeyError, InvalidOperation, ValueError) as exc:
            raise ValueError(f"Invalid period or CPI index in {source}: {row!r}") from exc
        if not val.is_finite() or val <= 0:
            raise ValueError(f"Nonpositive/nonfinite CPI index in {source}: {row!r}")
        key = (period, label)
        if key in values:
            raise ValueError(f"Duplicate CPI grain {key} in {source}")
        values[key] = val
        classes.add(label)
        periods.add(period)
    by_period: dict[tuple, set[str]] = {}
    for period, label in values:
        by_period.setdefault(period, set()).add(label)
    if any(labels != classes for labels in by_period.values()):
        raise ValueError(f"CPI classification coverage changes within {source}")
    return values, by_period, encoding, classes


def format_decimal(value: Decimal) -> str:
    return format(value, ".12f").rstrip("0").rstrip(".") or "0"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--monthly", required=True, type=Path)
    parser.add_argument("--monthly-receipt", required=True, type=Path)
    parser.add_argument("--annual", required=True, type=Path)
    parser.add_argument("--annual-receipt", required=True, type=Path)
    parser.add_argument("--weights", required=True, type=Path)
    parser.add_argument("--crosswalk", required=True, type=Path)
    parser.add_argument("--out-json", required=True, type=Path)
    parser.add_argument("--out-contributions", required=True, type=Path)
    args = parser.parse_args()
    if args.out_json.exists() or args.out_contributions.exists():
        raise FileExistsError("No evidence overwrite; choose unused output paths")

    monthly_raw = args.monthly.read_bytes()
    annual_raw = args.annual.read_bytes()
    monthly_receipt = check_receipt(monthly_raw, args.monthly_receipt, "TPE-CPI-BASIC-MONTH")
    annual_receipt = check_receipt(annual_raw, args.annual_receipt, "TPE-CPI-BASIC-YEAR")
    month, month_classes, month_encoding, month_labels = load_series(monthly_raw, "monthly", True)
    year, year_classes, year_encoding, year_labels = load_series(annual_raw, "annual", False)
    if month_labels != year_labels:
        raise ValueError("Monthly and annual CPI class sets differ")

    expected_months = make_month_grid((1998, 1), (2026, 9))
    observed_months = sorted(month_classes)
    if observed_months != expected_months:
        raise ValueError("Monthly CPI periods are not a complete 1998-01 through 2026-09 grid")
    expected_years = list(range(1998, 2026))
    observed_years = sorted(year_classes)
    if observed_years != expected_years:
        raise ValueError("Annual CPI years are not a complete 1998 through 2025 grid")
    for period in ((2020, m) for m in range(1, 10)):
        if month_classes.get(period) != month_labels:
            raise ValueError(f"Incomplete 2020 Jan-Sep CPI class grid at {period}")
    for period in ((2026, m) for m in range(1, 10)):
        if month_classes.get(period) != month_labels:
            raise ValueError(f"Incomplete 2026 Jan-Sep CPI class grid at {period}")

    annual_reconciliation = []
    max_annual_monthly_delta = Decimal(0)
    for y in range(2020, 2026):
        for label in sorted(month_labels):
            average = sum((month[((y, m), label)] for m in range(1, 13)), Decimal(0)) / Decimal(12)
            delta = abs(average - year[(y, label)])
            max_annual_monthly_delta = max(max_annual_monthly_delta, delta)
            annual_reconciliation.append(delta)
    if max_annual_monthly_delta > Decimal("0.005"):
        raise ValueError(f"Monthly-average versus annual-series delta exceeds 0.005: {max_annual_monthly_delta}")

    monthly_changes = []
    for label in sorted(month_labels):
        for previous, current in zip(observed_months, observed_months[1:]):
            if current < (2020, 1):
                continue
            previous_value = month[(previous, label)]
            current_value = month[(current, label)]
            change = (current_value / previous_value - 1) * 100
            monthly_changes.append({
                "class": label,
                "previous_period": f"{previous[0]}-{previous[1]:02d}",
                "period": f"{current[0]}-{current[1]:02d}",
                "change_percent": change,
                "absolute_change_percent": abs(change),
                "previous_index": previous_value,
                "index": current_value,
            })
    large_changes = [x for x in monthly_changes if x["absolute_change_percent"] >= Decimal("20")]
    largest_changes = sorted(monthly_changes, key=lambda x: x["absolute_change_percent"], reverse=True)[:10]

    # The official 2026-09 Taipei release states CPI base 2021=100 and all-items 113.95.
    all_items_sep = month[((2026, 9), "總指數")]
    annual_2021_base_values = {year[(2021, label)] for label in month_labels}
    if all_items_sep != Decimal("113.95") or annual_2021_base_values != {Decimal("100.00")}:
        raise ValueError("Index-base/headline cross-check failed")

    weights_raw = args.weights.read_bytes()
    crosswalk_raw = args.crosswalk.read_bytes()
    weight_rows, weight_encoding = decode_dict_rows(weights_raw)
    weights: dict[tuple[str, int], Decimal] = {}
    category_labels: dict[int, str] = {}
    group_totals: dict[str, Decimal] = {}
    group_denominators: dict[str, int] = {}
    group_categories: dict[str, set[int]] = {}
    for row in weight_rows:
        if row.get("geographic_scope") != "TAIPEI_CITY_ONLY" or row.get("reference_year") != "2020 / ROC109":
            raise ValueError("Age-head weight scope/year mismatch")
        group = row["household_head_age_group"]
        cat = int(row["category_number"])
        expenditure = Decimal(row["annual_expenditure_nt_per_household"])
        denominator = int(row["sum_of_12_categories_nt"])
        stored = Decimal(row["weight_share"])
        share = expenditure / Decimal(denominator)
        if abs(share - stored) > Decimal("0.0000000000005"):
            raise ValueError(f"Stored age-head weight does not reconcile: {group}/{cat}")
        key = (group, cat)
        if key in weights:
            raise ValueError(f"Duplicate age-head weight row: {key}")
        weights[key] = share
        category_labels[cat] = row["category_label_zh"]
        group_totals[group] = group_totals.get(group, Decimal(0)) + share
        group_denominators[group] = denominator
        group_categories.setdefault(group, set()).add(cat)
    age_groups = sorted(group_totals, key=lambda g: next(i for i, r in enumerate(weight_rows) if r["household_head_age_group"] == g))
    if len(weights) != 84 or len(age_groups) != 7 or any(group_categories[g] != set(range(1, 13)) for g in age_groups):
        raise ValueError("Expected exactly 7 x 12 Taipei age-head household spending weights")

    crosswalk_rows, crosswalk_encoding = decode_dict_rows(crosswalk_raw)
    if len(crosswalk_rows) != 12 or {int(r["expense_division"]) for r in crosswalk_rows} != set(range(1, 13)):
        raise ValueError("Crosswalk must contain exactly the 12 spending divisions")
    mapped: dict[int, str] = {}
    status_counts = {"MAPPED": 0, "SPLIT_REQUIRED": 0, "UNMAPPED": 0}
    for row in crosswalk_rows:
        status = row["mapping_status"]
        if status not in status_counts:
            raise ValueError(f"Unrecognized crosswalk state: {status}")
        status_counts[status] += 1
        if status == "MAPPED":
            if row.get("price_relative_accepted") != "YES":
                raise ValueError("Mapped class must have an accepted price relative")
            classes = [x.strip() for x in row["taipei_cpi_basic_classifications"].split(";")]
            if len(classes) != 1 or classes[0] not in month_labels:
                raise ValueError(f"Mapped CPI class absent/ambiguous for division {row['expense_division']}")
            mapped[int(row["expense_division"])] = classes[0]
        elif row.get("price_relative_accepted") != "NO":
            raise ValueError("Split/unmapped category cannot accept a price relative")
    if len(mapped) != status_counts["MAPPED"]:
        raise ValueError("Crosswalk map count differs from mapped state count")

    period_specs = {
        "A_2020_JAN_SEP_TO_2026_JAN_SEP": ("monthly", (2020, 1), (2026, 1)),
        "B_2020_FULL_YEAR_TO_2025_FULL_YEAR": ("annual", 2020, 2025),
    }
    category_result = []
    summary_result = []
    csv_rows = []
    for period_name, (kind, baseline, target) in period_specs.items():
        relatives: dict[int, tuple[Decimal, Decimal, Decimal]] = {}
        for cat, label in mapped.items():
            if kind == "monthly":
                base_value = sum((month[((2020, m), label)] for m in range(1, 10)), Decimal(0)) / Decimal(9)
                target_value = sum((month[((2026, m), label)] for m in range(1, 10)), Decimal(0)) / Decimal(9)
            else:
                base_value = year[(2020, label)]
                target_value = year[(2025, label)]
            relatives[cat] = (base_value, target_value, target_value / base_value)
            category_result.append({
                "comparison": period_name, "expense_division": cat,
                "expense_label_zh": category_labels[cat], "cpi_class": label,
                "baseline_index": format_decimal(base_value),
                "target_index": format_decimal(target_value),
                "price_relative": format_decimal(target_value / base_value),
                "price_change_percent": format_decimal(((target_value / base_value) - 1) * 100),
            })
        if kind == "monthly":
            general_base = sum((month[((2020, m), "總指數")] for m in range(1, 10)), Decimal(0)) / Decimal(9)
            general_target = sum((month[((2026, m), "總指數")] for m in range(1, 10)), Decimal(0)) / Decimal(9)
        else:
            general_base = year[(2020, "總指數")]
            general_target = year[(2025, "總指數")]
        general_change = (general_target / general_base - 1) * 100
        for group in age_groups:
            coverage = sum((weights[(group, cat)] for cat in mapped), Decimal(0))
            partial_pp = Decimal(0)
            for cat, (base_value, target_value, relative) in relatives.items():
                weight = weights[(group, cat)]
                contribution = weight * (relative - 1) * 100
                partial_pp += contribution
                csv_rows.append({
                    "label": "TAIPEI_AGE_HEAD_CPI_PROXY_PARTIAL_CONTRIBUTION",
                    "comparison": period_name,
                    "household_head_age_group": group,
                    "expense_division": cat,
                    "expense_label_zh": category_labels[cat],
                    "cpi_class": mapped[cat],
                    "weight_share_2020": format_decimal(weight),
                    "baseline_index": format_decimal(base_value),
                    "target_index": format_decimal(target_value),
                    "price_relative": format_decimal(relative),
                    "contribution_percentage_points": format_decimal(contribution),
                    "mapped_coverage_share": format_decimal(coverage),
                    "uncovered_share": format_decimal(Decimal(1) - coverage),
                    "full_rate_release": "NO_HOLD",
                })
            missing_mandatory = sorted(REQUIRED_MAPPED_CLASSES - set(mapped))
            eligible = coverage >= MIN_COVERAGE and not missing_mandatory
            summary_result.append({
                "comparison": period_name,
                "household_head_age_group": group,
                "mapped_categories": sorted(mapped),
                "mapped_coverage_share": format_decimal(coverage),
                "uncovered_share": format_decimal(Decimal(1) - coverage),
                "partial_mapped_contribution_percentage_points": format_decimal(partial_pp),
                "official_general_cpi_change_percent": format_decimal(general_change),
                "mandatory_unmapped_categories": missing_mandatory,
                "coverage_threshold": format_decimal(MIN_COVERAGE),
                "full_age_head_rate_release_eligible": eligible,
            })

    age_differences = []
    for period_name, (kind, baseline, target) in period_specs.items():
        summaries = {r["household_head_age_group"]: r for r in summary_result if r["comparison"] == period_name}
        senior = summaries.get("65歲及以上")
        comparator = summaries.get("45～54歲")
        if senior and comparator:
            age_differences.append({
                "comparison": period_name,
                "measure": "difference in mapped-category contributions only; not a full cohort inflation gap",
                "65_plus_minus_45_54_percentage_points": format_decimal(Decimal(senior["partial_mapped_contribution_percentage_points"]) - Decimal(comparator["partial_mapped_contribution_percentage_points"])),
            })

    sensitivity = []
    if 9 in mapped:
        narrower_categories = set(mapped) - {9}
        for period_name, (kind, baseline, target) in period_specs.items():
            for group in age_groups:
                contribution = Decimal(0)
                for cat in narrower_categories:
                    label = mapped[cat]
                    if kind == "monthly":
                        base_value = sum((month[((2020, m), label)] for m in range(1, 10)), Decimal(0)) / Decimal(9)
                        target_value = sum((month[((2026, m), label)] for m in range(1, 10)), Decimal(0)) / Decimal(9)
                    else:
                        base_value, target_value = year[(2020, label)], year[(2025, label)]
                    contribution += weights[(group, cat)] * (target_value / base_value - 1) * 100
                coverage = sum((weights[(group, cat)] for cat in narrower_categories), Decimal(0))
                sensitivity.append({
                    "comparison": period_name,
                    "household_head_age_group": group,
                    "scenario": "withhold_division_09_leisure_entertainment_mapping",
                    "mapped_coverage_share": format_decimal(coverage),
                    "uncovered_share": format_decimal(Decimal(1) - coverage),
                    "partial_mapped_contribution_percentage_points": format_decimal(contribution),
                    "full_rate_release": "NO_HOLD",
                })

    output = {
        "result": "PARTIAL_WITH_EXTERNAL_BLOCKERS",
        "label": "TAIPEI_AGE_HEAD_CPI_PROXY",
        "status": "VERIFIED_CLASS_CONTRIBUTIONS_ONLY_FULL_AGE_RATE_HOLD",
        "weight_scope": "Taipei City household-head-age expenditure proxy; not nationwide, not worker-only, and not retired-household status",
        "source_receipts": {
            "monthly": {k: monthly_receipt.get(k) for k in ("sha256", "raw_bytes", "http_code", "final_url", "retrieved_utc", "tls_verification")},
            "annual": {k: annual_receipt.get(k) for k in ("sha256", "raw_bytes", "http_code", "final_url", "retrieved_utc", "tls_verification")},
        },
        "input_profiles": {
            "monthly": {"encoding": month_encoding, "rows": len(month), "classes": len(month_labels), "class_labels": sorted(month_labels), "month_count": len(observed_months), "first_period": f"{observed_months[0][0]}-{observed_months[0][1]:02d}", "last_period": f"{observed_months[-1][0]}-{observed_months[-1][1]:02d}", "2020_jan_sep_months": list(range(1, 10)), "2020_jan_sep_rows": 9 * len(month_labels), "2026_jan_sep_months": list(range(1, 10)), "2026_jan_sep_rows": 9 * len(month_labels), "city_codes": ["63000"]},
            "annual": {"encoding": year_encoding, "rows": len(year), "classes": len(year_labels), "class_labels": sorted(year_labels), "years": observed_years, "first_year": min(observed_years), "last_year": max(observed_years), "2020_2025_years": list(range(2020, 2026)), "2020_2025_rows": 6 * len(year_labels), "city_codes": ["63000"]},
            "weights_sha256": hashlib.sha256(weights_raw).hexdigest(),
            "weights_encoding": weight_encoding,
            "crosswalk_sha256": hashlib.sha256(crosswalk_raw).hexdigest(),
            "crosswalk_encoding": crosswalk_encoding,
        },
        "classification_and_integrity": {
            "monthly_annual_class_sets_identical": True,
            "monthly_complete_all_classes_all_months_1998_01_to_2026_09": True,
            "annual_complete_all_classes_1998_to_2025": True,
            "positive_finite_index_values_only": True,
            "duplicate_period_class_rows": 0,
            "2021_annual_all_class_indices_unique_values": sorted(str(x) for x in annual_2021_base_values),
            "official_2021_base_headline_reconciliation": {"official_2026_09_all_items": "113.95", "raw_series_2026_09_all_items": str(all_items_sep), "match": True},
            "monthly_average_vs_official_annual_max_abs_index_delta_2020_2025": format_decimal(max_annual_monthly_delta),
            "monthly_average_vs_official_annual_pairs_checked": len(annual_reconciliation),
            "monthly_average_vs_official_annual_within_half_cent_index_rounding": True,
            "recent_month_over_month_pairs_2020_01_to_2026_09": len(monthly_changes),
            "absolute_month_over_month_changes_at_least_20_percent": len(large_changes),
            "largest_absolute_month_over_month_changes": [{k: (format_decimal(v) if isinstance(v, Decimal) else v) for k, v in x.items() if k not in ("absolute_change_percent",)} for x in largest_changes],
            "large_monthly_moves_are_flagged_for_review_not_silently_smoothed": True,
        },
        "crosswalk": {"total_divisions": 12, "status_counts": status_counts, "mapped_price_classes": {str(k): v for k, v in mapped.items()}},
        "release_gate": {"minimum_coverage": format_decimal(MIN_COVERAGE), "mandatory_categories": sorted(REQUIRED_MAPPED_CLASSES), "unmapped_or_split_mandatory_categories": sorted(REQUIRED_MAPPED_CLASSES - set(mapped)), "full_rate_release": "HOLD_NO_NORMALIZATION"},
        "mapped_category_price_results": category_result,
        "age_head_partial_summary": summary_result,
        "partial_65_plus_vs_45_54_contribution_difference": age_differences,
        "partial_mapping_sensitivity": sensitivity,
        "not_calculated": ["complete age-head CPI rate", "national worker/retired inflation", "HO600 official index"],
    }
    args.out_json.parent.mkdir(parents=True, exist_ok=True)
    args.out_json.write_text(json.dumps(output, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    with args.out_contributions.open("x", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(csv_rows[0]))
        writer.writeheader()
        writer.writerows(csv_rows)
    print(json.dumps({"result": output["result"], "mapped": status_counts["MAPPED"], "split_required": status_counts["SPLIT_REQUIRED"], "unmapped": status_counts["UNMAPPED"], "full_rate": "HOLD_NO_NORMALIZATION", "summary_rows": len(summary_result), "contribution_rows": len(csv_rows)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
