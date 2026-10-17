#!/usr/bin/env python3
"""Reconcile Taipei's 2020 age-head CSV to official PDF Table 8, then derive city-only expenditure shares.

This is research evidence for TAIPEI_CITY + HOUSEHOLD_HEAD_AGE only. It never
creates national, employed-household, or retirement weights. PDF reading uses
pdfplumber from the Codex bundled Python runtime; no artifact_tool is needed.
"""
from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import urlsplit

import pdfplumber


AGE_ROWS = (
    "總平均",
    "未滿30歲",
    "30～34歲",
    "35～39歲",
    "40～44歲",
    "45～54歲",
    "55～64歲",
    "65歲及以上",
)
AGE_PROXY_IDS = {
    "未滿30歲": "TPE_AGE_HEAD_UNDER_30_PROXY",
    "30～34歲": "TPE_AGE_HEAD_30_34_PROXY",
    "35～39歲": "TPE_AGE_HEAD_35_39_PROXY",
    "40～44歲": "TPE_AGE_HEAD_40_44_PROXY",
    "45～54歲": "TPE_AGE_HEAD_45_54_PROXY",
    "55～64歲": "TPE_AGE_HEAD_55_64_PROXY",
    "65歲及以上": "TPE_AGE_HEAD_65_PLUS_PROXY",
}
NUMBER = re.compile(r"^(?:\d{1,3}(?:,\d{3})+|\d+)$")
CATEGORY_PREFIX = re.compile(r"^(?:[1-9]|1[0-2])\.")


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def checked_receipt(path: Path, raw_path: Path, *, kind: str) -> dict:
    receipt = json.loads(path.read_text(encoding="utf-8"))
    if kind == "csv":
        actual_sha = receipt.get("sha256")
        actual_size = receipt.get("raw_bytes")
        url = receipt.get("final_url", "")
        status = receipt.get("http_status")
        valid_host = urlsplit(url).hostname == "data.taipei"
    else:
        actual_sha = receipt.get("raw_sha256")
        actual_size = receipt.get("raw_file_size_bytes")
        url = receipt.get("actual_final_url", "")
        status = receipt.get("http_code")
        valid_host = urlsplit(url).hostname == "www-ws.gov.taipei"
    if status != 200 or not url.startswith("https://") or not valid_host:
        raise ValueError(f"{kind} receipt is not a strict HTTPS 200 from its registered government host")
    if actual_sha != sha256(raw_path) or actual_size != raw_path.stat().st_size:
        raise ValueError(f"{kind} receipt hash/size does not match the preserved original")
    return receipt


def numeric_row(page, y: float, bounds: list[float]) -> list[int]:
    words = page.extract_words(x_tolerance=1, y_tolerance=2)
    out = []
    for left, right in zip(bounds, bounds[1:]):
        matches = [
            word for word in words
            if abs(word["top"] - y) <= 1.25
            and left <= word["x0"] < right
            and NUMBER.fullmatch(word["text"])
        ]
        if len(matches) != 1:
            raise ValueError(f"PDF numeric cell is ambiguous at y={y}, x=[{left},{right}): {matches}")
        out.append(int(matches[0]["text"].replace(",", "")))
    return out


def pdf_table8_values(pdf_path: Path) -> tuple[dict, dict]:
    # The official bilingual Table 8 is printed on pages 78-81 (PDF pages 90-93).
    # PDF pages 92 and 93 contain the expenditure section, split into four age
    # columns each. Positions are validated against the printed Table 8 labels.
    with pdfplumber.open(str(pdf_path)) as pdf:
        if len(pdf.pages) < 93:
            raise ValueError("Official PDF is missing the Table 8 pages")
        first = pdf.pages[91]  # General average, under 30, 30-34, 35-39
        second = pdf.pages[92]  # 40-44, 45-54, 55-64, 65+
        page_text = second.extract_text() or ""
        normalized_page_text = re.sub(r"\s+", "", page_text).lower()
        if "table8familyincomeandexpenditureperhousehold" not in normalized_page_text or "2020" not in page_text:
            raise ValueError("Official 2020 Table 8 heading not found on the expected continuation page")

        labels = {}
        for word in second.extract_words(x_tolerance=1, y_tolerance=2):
            match = re.match(r"^(1[0-2]|[1-9])\.", word["text"])
            if match and 340 <= word["x0"] <= 540 and 250 < word["top"] < 710:
                labels[int(match.group(1))] = word["top"]
        if sorted(labels) != list(range(1, 13)):
            raise ValueError(f"PDF Table 8 does not expose exactly 12 expenditure category labels: {labels}")

        # Each page has four aligned age columns. Bounds are between observed
        # column clusters, while the label positions provide the row anchors.
        blocks = (
            (first, [280, 340, 410, 477, 540], AGE_ROWS[:4]),
            (second, [0, 145, 212, 280, 340], AGE_ROWS[4:]),
        )
        categories: dict[str, dict[int, int]] = {age: {} for age in AGE_ROWS}
        totals: dict[str, int] = {}
        for page, bounds, ages in blocks:
            grouped: dict[float, list[dict]] = {}
            for word in page.extract_words(x_tolerance=1, y_tolerance=2):
                if NUMBER.fullmatch(word["text"]) and word["x0"] < bounds[-1]:
                    grouped.setdefault(round(word["top"], 1), []).append(word)

            total_rows = []
            for y, words in grouped.items():
                if 230 <= y <= 255:
                    try:
                        total_rows.append((y, numeric_row(page, y, bounds)))
                    except ValueError:
                        pass
            if len(total_rows) != 1:
                raise ValueError(f"Could not uniquely identify the Table 8 consumption-total row: {total_rows}")
            for age, value in zip(ages, total_rows[0][1]):
                totals[age] = value

            for category_number, label_y in labels.items():
                possible_rows = []
                for y in grouped:
                    if abs(y - label_y) > 8.5:
                        continue
                    try:
                        cells = numeric_row(page, y, bounds)
                    except ValueError:
                        continue
                    possible_rows.append((abs(y - label_y), y, cells))
                if not possible_rows:
                    raise ValueError(f"Missing PDF category {category_number} row near y={label_y}")
                _, _, cells = min(possible_rows, key=lambda row: row[0])
                for age, value in zip(ages, cells):
                    categories[age][category_number] = value
        if set(totals) != set(AGE_ROWS) or any(len(v) != 12 for v in categories.values()):
            raise ValueError("PDF Table 8 did not yield all eight rows and twelve category values")
        return categories, totals


def run(csv_path: Path, csv_receipt_path: Path, pdf_path: Path, pdf_receipt_path: Path, out: Path) -> dict:
    if out.exists() and any(out.iterdir()):
        raise FileExistsError("Output directory must be new or empty; no existing research output will be overwritten")
    csv_receipt = checked_receipt(csv_receipt_path, csv_path, kind="csv")
    pdf_receipt = checked_receipt(pdf_receipt_path, pdf_path, kind="pdf")

    with csv_path.open("r", encoding="cp950", newline="") as stream:
        source_rows = list(csv.reader(stream))
    header = source_rows[0]
    if len(header) != 58 or len(set(header)) != len(header):
        raise ValueError(f"Unexpected CSV schema: {len(header)} columns, unique={len(set(header)) == len(header)}")
    year_col = header.index("年別")
    age_col = header.index("經濟戶長年齡組")
    total_col = header.index("[三]消費支出[NT]")
    category_stop = header.index("可支配所得[NT]")
    category_cols = [i for i in range(total_col + 1, category_stop) if CATEGORY_PREFIX.match(header[i])]
    if len(category_cols) != 12:
        raise ValueError(f"Expected exactly 12 expenditure categories; found {len(category_cols)}")
    category_labels = [re.sub(r"\[NT\]$", "", header[i]) for i in category_cols]
    category_labels = [re.sub(r"^\d+\.", "", label) for label in category_labels]

    rows_2020 = [row for row in source_rows[1:] if row[year_col] == "109年"]
    csv_by_age = {row[age_col]: row for row in rows_2020}
    if len(rows_2020) != 8 or len(csv_by_age) != 8 or set(csv_by_age) != set(AGE_ROWS):
        raise ValueError(f"Expected one 109-year row for each of eight published age rows: {list(csv_by_age)}")

    csv_categories = {}
    csv_totals = {}
    sums = {}
    for age, row in csv_by_age.items():
        values = [int(row[col].replace(",", "")) for col in category_cols]
        total = int(row[total_col].replace(",", ""))
        if any(value < 0 for value in values):
            raise ValueError(f"Negative expenditure cell in {age}")
        csv_categories[age] = {number: value for number, value in enumerate(values, start=1)}
        csv_totals[age] = total
        sums[age] = sum(values)
        if abs(sums[age] - total) > 2:
            raise ValueError(f"12-class sum differs from published total by more than NT$2 in {age}")

    pdf_categories, pdf_totals = pdf_table8_values(pdf_path)
    category_matches = 0
    for age in AGE_ROWS:
        if csv_totals[age] != pdf_totals[age]:
            raise ValueError(f"PDF/CSV consumption total differs for {age}: {pdf_totals[age]} vs {csv_totals[age]}")
        for category_number in range(1, 13):
            if csv_categories[age][category_number] != pdf_categories[age][category_number]:
                raise ValueError(
                    f"PDF/CSV mismatch for {age}, category {category_number}: "
                    f"{pdf_categories[age][category_number]} vs {csv_categories[age][category_number]}"
                )
            category_matches += 1

    out.mkdir(parents=True, exist_ok=True)
    weight_path = out / "TPE_AGE_HEAD_EXPENDITURE_PROXY_WEIGHTS_2020.csv"
    recon_path = out / "tpe-2020-age-head-proxy-reconciliation.json"
    fieldnames = (
        "geographic_scope", "reference_year", "proxy_id", "household_head_age_group",
        "category_number", "category_label_zh", "annual_expenditure_nt_per_household",
        "published_consumption_total_nt", "sum_of_12_categories_nt", "weight_denominator_nt",
        "weight_share",
    )
    with weight_path.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        for age in AGE_ROWS[1:]:
            denominator = sums[age]
            for category_number, category_label in enumerate(category_labels, start=1):
                value = csv_categories[age][category_number]
                writer.writerow({
                    "geographic_scope": "TAIPEI_CITY_ONLY",
                    "reference_year": "2020 / ROC109",
                    "proxy_id": AGE_PROXY_IDS[age],
                    "household_head_age_group": age,
                    "category_number": category_number,
                    "category_label_zh": category_label,
                    "annual_expenditure_nt_per_household": value,
                    "published_consumption_total_nt": csv_totals[age],
                    "sum_of_12_categories_nt": sums[age],
                    "weight_denominator_nt": denominator,
                    "weight_share": format(Decimal(value) / Decimal(denominator), ".12f"),
                })

    now = datetime.now(timezone.utc).isoformat()
    result = {
        "status": "PASS_TAIPEI_CITY_AGE_HEAD_PROXY_ONLY",
        "verified_at_utc": now,
        "scope": "TAIPEI_CITY household-head age groups; annual average expenditure per household; NT dollars",
        "proxy_definition": "12-class expenditure shares by household-head age group; age 65+ is not retirement status",
        "retirement_population_inferred": False,
        "national_WGT01_satisfied": False,
        "official_csv": {
            "landing": csv_receipt["source_landing"],
            "final_url": csv_receipt["final_url"],
            "resource_id": csv_receipt["source_id"],
            "retrieved_at_utc": csv_receipt["utc_retrieved"],
            "raw_bytes": csv_path.stat().st_size,
            "sha256": sha256(csv_path),
            "rows": len(source_rows) - 1,
            "columns": len(header),
            "encoding": "cp950 / Big5",
            "survey_year": "2020 / ROC109",
            "age_rows_including_total_average": 8,
        },
        "official_pdf": {
            "landing": pdf_receipt["official_landing"],
            "final_url": pdf_receipt["actual_final_url"],
            "retrieved_at_utc": pdf_receipt["retrieved_at_utc"],
            "raw_bytes": pdf_path.stat().st_size,
            "sha256": sha256(pdf_path),
            "table": "Table 8, Taipei household income and expenditure by household-head age, 2020 / ROC109",
            "pdf_table_pages_printed": "78-81",
        },
        "checks": {
            "all_12_category_columns_present": True,
            "category_values_compared_pdf_to_csv": f"{category_matches}/96 exact",
            "published_totals_compared_pdf_to_csv": "8/8 exact",
            "twelve_category_sum_max_absolute_delta_nt": max(abs(v) for v in (sums[a] - csv_totals[a] for a in AGE_ROWS)),
            "sum_delta_by_age_group_nt": {age: sums[age] - csv_totals[age] for age in AGE_ROWS},
            "rounding_tolerance_nt": 2,
            "weights_generated_for_age_groups": list(AGE_ROWS[1:]),
            "weights_normalized_by": "sum of the twelve published category cells per age group; avoids spreading the source's <= NT$2 display-rounding delta",
        },
        "weight_output": weight_path.name,
        "weights_sha256": sha256(weight_path),
    }
    recon_path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--csv", required=True, type=Path)
    parser.add_argument("--csv-receipt", required=True, type=Path)
    parser.add_argument("--pdf", required=True, type=Path)
    parser.add_argument("--pdf-receipt", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()
    print(json.dumps(run(args.csv, args.csv_receipt, args.pdf, args.pdf_receipt, args.out), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
