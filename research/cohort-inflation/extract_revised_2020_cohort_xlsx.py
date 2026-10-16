#!/usr/bin/env python3
"""Fail-closed DGBAS cohort weight extraction from *reviewed* converted XLSX.

Use Apple's Numbers to convert an authenticated official .xls/.ods into .xlsx
on the user's Mac. This program uses only artifact_tool to read spreadsheets;
conversion is not proof of original source authenticity.

1) --inspect converted.xlsx (discover actual sheet/row/column positions)
2) Fill an independent reviewed mapping JSON, never guess row assignments.
3) --extract converted.xlsx --mapping mapping.json --raw original.xls --out DIR

No GitHub Actions, no canonical workbook modifications, no cohort inflation.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
import re
from decimal import Decimal, InvalidOperation
from pathlib import Path
from artifact_tool import Blob, SpreadsheetFile

TOKENS = {
    "01": ("食品", "非酒精"),
    "02": ("菸酒", "檳榔"),
    "03": ("衣著", "鞋襪"),
    "04": ("住宅", "水電"),
    "05": ("家具", "家務"),
    "06": ("醫療", "保健"),
    "07": ("交通",),
    "08": ("通訊",),
    "09": ("休閒", "文化"),
    "10": ("教育",),
    "11": ("餐廳", "旅館"),
    "12": ("什項", "消費"),
}
ALLOWED_SOURCE_PREFIXES = {"NAT20-AGE": "AGE_HEAD_", "NAT20-OCC": "OCC_HEAD_"}
EXPECTED_CODES = [f"{n:02d}" for n in range(1, 13)]

def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def normalize(value) -> str:
    return re.sub(r"[\s,，、:：./（）()\[\]【】－\-]+", "", str(value or ""))

def col_index(letters: str) -> int:
    assert re.fullmatch(r"[A-Z]{1,3}", letters), "Column must be Excel A:ZZZ"
    index = 0
    for letter in letters:
        index = index * 26 + ord(letter) - 64
    return index - 1

def cell_ref(column: str, row: int) -> str:
    assert isinstance(row, int) and 1 <= row <= 2000
    return f"{column}{row}"

def value(sheet, column: str, row: int):
    return sheet.get_range(cell_ref(column, row)).values[0][0]

def decimal_amount(v) -> Decimal:
    if isinstance(v, bool) or v is None:
        raise ValueError("No numeric cell value")
    try:
        n = Decimal(str(v).replace(",", "").strip())
    except (InvalidOperation, ValueError) as exc:
        raise ValueError(f"Not a numeric amount: {v!r}") from exc
    if not n.is_finite() or n < 0:
        raise ValueError(f"Negative or non-finite amount: {v}")
    return n

def load_xlsx(file: Path):
    if file.suffix.lower() != ".xlsx":
        raise ValueError("Use converted .xlsx only. Preserve original .xls/.ods bytes separately.")
    return SpreadsheetFile.import_xlsx(Blob.load(str(file)))

def inspect(file: Path, max_rows: int = 180, max_cols: int = 20) -> None:
    wb = load_xlsx(file)
    for si in range(len(wb.worksheets.items)):
        ws = wb.worksheets.get_item_at(si)
        print("SHEET", si, ws.name)
        grid = ws.get_range_by_indexes(0, 0, max_rows, max_cols).values
        for i, row in enumerate(grid, 1):
            visible = []
            for j, v in enumerate(row):
                if v is not None and str(v).strip():
                    col = ""
                    x = j + 1
                    while x:
                        x, rem = divmod(x - 1, 26)
                        col = chr(65 + rem) + col
                    visible.append(f"{col}:{str(v)[:65]}")
            if visible:
                print(f"{i:4d} ", " | ".join(visible[:10]))

def extract(file: Path, mapping_path: Path, raw_path: Path, out: Path) -> dict:
    conf = json.loads(mapping_path.read_text(encoding="utf-8"))
    needed = {"source_id", "source_url", "year", "cohort_code", "sheet",
              "label_col", "amount_col", "category_rows", "total_row", "total_label_col",
              "raw_sha256", "converted_sha256", "reviewed"}
    if set(conf) != needed:
        raise ValueError(f"Mapping fields must exactly match: {sorted(needed)}")
    src = conf["source_id"]
    if src not in ALLOWED_SOURCE_PREFIXES or conf["year"] != 2020:
        raise ValueError("Only revised national 2020 age/occupation sources are allowed")
    cohort = conf["cohort_code"]
    if not cohort.startswith(ALLOWED_SOURCE_PREFIXES[src]) or not cohort.endswith("_PROXY"):
        raise ValueError("Unqualified WORK/RETIRE labels prohibited; specify a proxy cohort")
    if conf["reviewed"] is not True:
        raise ValueError("A human-reviewed, frozen cell map is required")
    if len(conf["category_rows"]) != 12 or sorted(conf["category_rows"]) != EXPECTED_CODES:
        raise ValueError("Exactly twelve official category codes required")
    if len(set(conf["category_rows"].values())) != 12:
        raise ValueError("Category rows must be distinct")
    for c in (conf["label_col"], conf["amount_col"], conf["total_label_col"]):
        col_index(c)
    actual_raw = sha(raw_path)
    actual_converted = sha(file)
    if actual_raw != conf["raw_sha256"] or actual_converted != conf["converted_sha256"]:
        raise ValueError("Source SHA mismatch: never read altered, substituted or old files")
    if not conf["source_url"].startswith("https://ws.dgbas.gov.tw/"):
        raise ValueError("Official DGBAS source URL required")
    wb = load_xlsx(file)
    ws = wb.worksheets.get_item(conf["sheet"])
    entries = []
    for code in EXPECTED_CODES:
        row = conf["category_rows"][code]
        label = value(ws, conf["label_col"], row)
        norm = normalize(label)
        if not all(token in norm for token in TOKENS[code]):
            raise ValueError(f"{code} label mismatch at {conf['label_col']}{row}: {label!r}")
        amount = decimal_amount(value(ws, conf["amount_col"], row))
        entries.append((code, str(label), str(amount), cell_ref(conf["amount_col"], row), amount))
    total_row = conf["total_row"]
    total_label = normalize(value(ws, conf["total_label_col"], total_row))
    if "消費支出" not in total_label:
        raise ValueError("Total row must be a directly labelled 消費支出 cell")
    total = decimal_amount(value(ws, conf["amount_col"], total_row))
    if total <= 0:
        raise ValueError("Total expenditure must be positive")
    summed = sum((entry[4] for entry in entries), Decimal(0))
    # Source tables can round each of 12 categories to whole TWD; allowing
    # up to 12 TWD but do not silently modify or rebalance the source amounts.
    if abs(total - summed) > Decimal(12):
        raise ValueError(f"STOP category-total mismatch {summed} vs {total}")
    out.mkdir(parents=True, exist_ok=True)
    dest = out / (src + "-" + cohort + "-weights-unreleased.csv")
    receipt = out / (src + "-" + cohort + ".receipt.json")
    if dest.exists() or receipt.exists():
        raise FileExistsError("Never overwrite prior cohort extraction/receipt")
    fields = ["source_id", "year", "scope", "cohort_code", "category_code",
              "source_category", "amount_twd_per_household_year", "source_cell",
              "weight_fraction", "total_twd_per_household_year", "source_url",
              "source_raw_sha256", "converted_sha256", "research_status"]
    with dest.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(fields)
        for code, label, amount, position, numeric in entries:
            writer.writerow([src, 2020, "TAIWAN", cohort, code, label, amount,
                position, format(numeric / total, ".12f"), str(total), conf["source_url"],
                actual_raw, actual_converted, "PROXY_RAW_PARSED_RESEARCH_ONLY"])
    info = {
        "result": "PASSED_STRUCTURAL_EXTRACTION_NOT_A_RELEASE",
        "year": 2020, "cohort": cohort, "source_id": src, "source_raw_sha256": actual_raw,
        "converted_sha256": actual_converted, "xlsx_sheet": conf["sheet"],
        "category_count": 12, "source_total": str(total),
        "category_sum": str(summed), "difference": str(summed-total),
        "unit": "TWD per household per year", "raw_path": str(raw_path),
        "mapping_sha256": sha(mapping_path),
        "cohort_is_actual_retired_or_all_worker_population": False,
        "2020_to_2026_inflation_calculated": False,
        "publication_authorized": False
    }
    receipt.write_text(json.dumps(info, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return info

def main():
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--inspect", type=Path)
    mode.add_argument("--extract", type=Path)
    parser.add_argument("--mapping", type=Path)
    parser.add_argument("--raw", type=Path)
    parser.add_argument("--out", type=Path, default=Path("/tmp/ho600-cohort-weight-qc"))
    args = parser.parse_args()
    if args.inspect:
        inspect(args.inspect)
        return
    if not args.mapping or not args.raw:
        parser.error("--extract requires --mapping and --raw")
    print(json.dumps(extract(args.extract, args.mapping, args.raw, args.out),
                     ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
