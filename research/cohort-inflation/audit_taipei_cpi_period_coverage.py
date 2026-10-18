#!/usr/bin/env python3
"""Audit official Taipei CPI monthly time/class coverage; never calculate cohort inflation."""
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

PERIOD_NAME = {"統計期", "年月別"}
OFFICIAL_CPI_HOSTS = {"data.taipei", "tsis.dbas.gov.taipei"}


def parse_month(text: str) -> tuple[int, int]:
    s = str(text).strip().replace("民國", "").replace("西元", "")
    match = re.fullmatch(r"(\d{2,4})\s*(?:年|[/.-])?\s*(\d{1,2})\s*月?", s)
    if not match:
        raise ValueError(f"Unrecognized monthly CPI period: {text!r}")
    year, month = map(int, match.groups())
    if year < 200:
        year += 1911
    if not 1990 <= year <= 2100 or not 1 <= month <= 12:
        raise ValueError(f"Out of bounds CPI period: {text!r}")
    return year, month


def load_csv(raw: bytes) -> tuple[list[str], list[list[str]], str]:
    for encoding in ("utf-8-sig", "cp950"):
        try:
            text = raw.decode(encoding)
        except UnicodeDecodeError:
            continue
        records = list(csv.reader(io.StringIO(text)))
        if not records:
            continue
        head = records[0]
        if len(head) != 5 or len(head) != len(set(head)):
            continue
        if not any(x.strip() in PERIOD_NAME for x in head):
            continue
        if "基本分類" not in head or not any("原始值" in x for x in head):
            continue
        return head, [row for row in records[1:] if any(x.strip() for x in row)], encoding
    raise ValueError("Expected five unique CPI columns with period/basic-class/index")


def audit(raw: bytes, receipt: dict) -> dict:
    digest = hashlib.sha256(raw).hexdigest()
    if digest != receipt.get("sha256") or len(raw) != receipt.get("raw_bytes"):
        raise ValueError("Government original bytes do not match pinned SHA or size")
    url = urlsplit(receipt.get("final_url", ""))
    if url.scheme != "https" or url.hostname not in OFFICIAL_CPI_HOSTS or receipt.get("http_code") != 200:
        raise ValueError("Unverified government HTTPS source receipt")
    if receipt.get("source_id") != "TPE-CPI-BASIC-MONTH":
        raise ValueError("Only official monthly basic-category CPI is accepted")
    header, rows, encoding = load_csv(raw)
    ip = next(i for i, x in enumerate(header) if x.strip() in PERIOD_NAME)
    ic = header.index("基本分類")
    iv = next(i for i, x in enumerate(header) if "原始值" in x)
    if "縣市別代碼" not in header:
        raise ValueError("Missing city-scope field")
    igeo = header.index("縣市別代碼")
    values = {}
    city_codes = set()
    for row in rows:
        if len(row) != len(header):
            raise ValueError("Nonrectangular CPI CSV")
        city_codes.add(row[igeo].strip())
        period, label = parse_month(row[ip]), row[ic].strip()
        if not label:
            raise ValueError("Empty CPI classification")
        key = (period, label)
        if key in values:
            raise ValueError(f"Duplicate month/class CPI record: {key}")
        try:
            index = Decimal(row[iv].replace(",", "").strip())
        except (InvalidOperation, ValueError) as e:
            raise ValueError(f"Invalid price index at {key}") from e
        if not index.is_finite() or index <= 0:
            raise ValueError(f"Nonpositive/nonfinite price index at {key}")
        values[key] = index
    if city_codes != {"63000"}:
        raise ValueError(f"Expected Taipei City 63000 only, observed {sorted(city_codes)}")
    all_classes = sorted(set(k[1] for k in values))
    wanted = list(range(1, 10))
    eligible = []
    missing_by_class = {}
    for label in all_classes:
        missing = {str(y): [m for m in wanted if ((y, m), label) not in values]
                   for y in (2020, 2026)}
        if all(not missed for missed in missing.values()):
            eligible.append(label)
        else:
            missing_by_class[label] = missing
    return {
        "status": "RAW_CLASS_PERIOD_AUDIT_ONLY_NO_INFLATION_CALCULATED",
        "source_raw_sha256": digest,
        "encoding": encoding,
        "official_month_rows": len(values),
        "city_codes": sorted(city_codes),
        "number_distinct_classes": len(all_classes),
        "period_2020_months_present": sorted(set(p[1] for (p, label) in values if p[0] == 2020)),
        "period_2026_months_present": sorted(set(p[1] for (p, label) in values if p[0] == 2026)),
        "class_labels_with_9_plus_9_complete_months": eligible,
        "full_pair_class_count": len(eligible),
        "class_count_with_missing_months": len(missing_by_class),
        "missing_by_class": missing_by_class,
        "CPI_base_2021_cross_class_confirmed": False,
        "12_household_spending_divisions_mapped": False,
        "2020_to_2026_inflation_computed": False,
        "national_WGT01_satisfied": False,
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--csv", required=True, type=Path)
    p.add_argument("--receipt", required=True, type=Path)
    p.add_argument("--out", required=True, type=Path)
    args = p.parse_args()
    if args.out.exists():
        raise FileExistsError("No evidence overwrite")
    result = audit(args.csv.read_bytes(), json.loads(args.receipt.read_text(encoding="utf-8")))
    args.out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"status": result["status"], "matched_classes": result["full_pair_class_count"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
