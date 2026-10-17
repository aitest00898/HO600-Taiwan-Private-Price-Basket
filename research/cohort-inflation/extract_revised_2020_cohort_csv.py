#!/usr/bin/env python3
"""Offline revised-2020 DGBAS XLS/ODS -> Numbers CSV -> reviewed proxy weights.

Standard Python library only; no artifact_tool, pip, TLS bypass or network calls.
CSV must be exported from a manually selected Numbers source sheet and cross-
checked visually against original government XLS/ODS. No final CPI index.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
from decimal import Decimal, InvalidOperation
from pathlib import Path
import re

SOURCE_URLS = {
    "NAT20-OCC": {
        "https://ws.dgbas.gov.tw/001/Upload/463/relfile/11530/235896/65.xls",
        "https://ws.dgbas.gov.tw/001/Upload/463/relfile/11530/235896/65.ods",
    },
    "NAT20-AGE": {
        "https://ws.dgbas.gov.tw/001/Upload/463/relfile/11531/235640/159-164.xls",
        "https://ws.dgbas.gov.tw/001/Upload/463/relfile/11531/235640/159-164.ods",
    },
}
NAMES = {
    "01": ["食品", "非酒精"], "02": ["菸酒", "檳榔"],
    "03": ["衣著", "鞋襪"], "04": ["住宅", "水電"],
    "05": ["家具", "家務"], "06": ["醫療", "保健"],
    "07": ["交通"], "08": ["通訊"], "09": ["休閒", "文化"],
    "10": ["教育"], "11": ["餐廳", "旅館"], "12": ["什項", "消費"],
}
CODES = [f"{i:02d}" for i in range(1, 13)]

def checksum(file):
    h = hashlib.sha256()
    with file.open("rb") as stream:
        for block in iter(lambda: stream.read(65536), b""):
            h.update(block)
    return h.hexdigest()

def check_original(file):
    with file.open("rb") as stream:
        magic = stream.read(8)
    if file.suffix.lower() == ".xls":
        if magic != bytes.fromhex("D0CF11E0A1B11AE1"):
            raise ValueError("Original XLS must have OLE2 binary signature")
    elif file.suffix.lower() == ".ods":
        if magic[:4] != bytes.fromhex("504B0304"):
            raise ValueError("Original ODS must have ZIP binary signature")
    else:
        raise ValueError("Only original official XLS or ODS accepted")

def positive_number(value):
    s = str(value or "").strip().replace(",", "").replace("，", "")
    try:
        num = Decimal(s)
    except (InvalidOperation, ValueError) as exc:
        raise ValueError(f"Invalid official numeric cell: {value!r}") from exc
    if not num.is_finite() or num < 0:
        raise ValueError(f"Missing, negative or nonfinite official amount: {value!r}")
    return num

def norm(value):
    return re.sub(r"[\s,，、.．:：()（）／/–—\-]+", "", str(value))

def run(original, csv_file, map_file, out_dir):
    conf = json.loads(map_file.read_text(encoding="utf-8"))
    required = {"source_id", "source_url", "reference_year", "cohort_code",
                "source_sheet", "numbers_export_confirmed", "manual_reviewed",
                "original_sha256", "csv_sha256", "label_column", "amount_column",
                "category_rows", "total_row", "total_label_column", "total_tolerance_twd"}
    if set(conf) != required:
        raise ValueError("Unreviewed mapping schema / unknown fields")
    src = conf["source_id"]
    if src not in SOURCE_URLS or conf["source_url"] not in SOURCE_URLS[src]:
        raise ValueError("Official source ID and exact URL do not match")
    if conf["reference_year"] != 2020:
        raise ValueError("Only revised 2020 annual data accepted")
    prefix = "AGE_HEAD_" if src == "NAT20-AGE" else "OCC_HEAD_"
    group = conf["cohort_code"]
    if not group.startswith(prefix) or not group.endswith("_PROXY"):
        raise ValueError("Actual WORK or RETIRE status not proven: PROXY label required")
    if conf["manual_reviewed"] is not True or conf["numbers_export_confirmed"] is not True:
        raise ValueError("Require visually confirmed Numbers CSV export and manual review")
    if not conf["source_sheet"].strip():
        raise ValueError("Actual government sheet name must be recorded")
    if set(conf["category_rows"]) != set(CODES):
        raise ValueError("Exactly 12 official division code rows required")
    rs = list(conf["category_rows"].values())
    if not all(type(i) is int and i >= 1 for i in rs) or len(set(rs)) != 12:
        raise ValueError("Category row positions must be distinct positive integers")
    if type(conf["total_row"]) is not int or conf["total_row"] < 1 or conf["total_row"] in rs:
        raise ValueError("Total row missing / collides with category row")
    cols = [conf["label_column"], conf["amount_column"], conf["total_label_column"]]
    if not all(type(c) is int and c >= 1 and c <= 200 for c in cols):
        raise ValueError("Columns must be 1-based positive integer offsets")
    tolerance = positive_number(conf["total_tolerance_twd"])
    if tolerance > 12:
        raise ValueError("Total rounding tolerance must not exceed 12 TWD")
    check_original(original)
    if checksum(original) != conf["original_sha256"] or checksum(csv_file) != conf["csv_sha256"]:
        raise ValueError("Raw official XLS/ODS or reviewed CSV SHA-256 mismatch")
    with csv_file.open(newline="", encoding="utf-8-sig") as stream:
        rows = list(csv.reader(stream))
    needed_rows = max(*rs, conf["total_row"])
    if len(rows) < needed_rows or any(len(row) < max(cols) for row in rows):
        raise ValueError("CSV dimensions do not contain all reviewed source cells")
    def cell(r, c):
        return rows[r - 1][c - 1]
    data = []
    for code in CODES:
        row = conf["category_rows"][code]
        label = cell(row, conf["label_column"])
        if not all(part in norm(label) for part in NAMES[code]):
            raise ValueError(f"Source label mismatch {code} CSV row {row}: {label!r}")
        amount = positive_number(cell(row, conf["amount_column"]))
        data.append((code, label, row, amount))
    total_label = norm(cell(conf["total_row"], conf["total_label_column"]))
    if "消費支出" not in total_label:
        raise ValueError("Total must be explicitly labelled 消費支出")
    total = positive_number(cell(conf["total_row"], conf["amount_column"]))
    if total <= 0:
        raise ValueError("Zero or missing annual consumption total")
    observed = sum((x[3] for x in data), Decimal(0))
    if abs(observed - total) > tolerance:
        raise ValueError(f"Expenditure sum mismatch: {observed} vs {total}")
    out_dir.mkdir(parents=True, exist_ok=True)
    dest = out_dir / f"{src}-{group}-unreleased.csv"
    receipt = out_dir / f"{src}-{group}.receipt.json"
    if dest.exists() or receipt.exists():
        raise FileExistsError("Never overwrite prior output or receipt")
    with dest.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.writer(stream)
        writer.writerow(["source_id","year","scope","cohort_proxy","category_code",
            "official_category","source_csv_row","spend_twd_per_household_year",
            "total_twd_per_household_year","weight_fraction","original_sha256",
            "numbers_csv_sha256","evidence_status"])
        for code, label, row, amount in data:
            writer.writerow([src, 2020, "TAIWAN", group, code, label, row,
                str(amount), str(total), format(amount/total, ".12f"),
                checksum(original), checksum(csv_file), "PROXY_RESEARCH_NOT_RELEASED"])
    payload = {
        "gate":"PARSED_PROXY_ONLY_NOT_WGT01_SOURCE_VERIFIED",
        "source_id":src, "source_url":conf["source_url"], "year":2020,
        "proxy":group, "category_count":12, "category_sum":str(observed),
        "source_total":str(total), "difference":str(observed - total),
        "original_sha256":checksum(original), "numbers_csv_sha256":checksum(csv_file),
        "mapping_sha256":checksum(map_file), "source_sheet":conf["source_sheet"],
        "not_actual_retire_or_employed_household":True,
        "index_calculated":False, "released":False,
    }
    receipt.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return payload

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--original", required=True, type=Path)
    p.add_argument("--csv", required=True, type=Path)
    p.add_argument("--mapping", required=True, type=Path)
    p.add_argument("--out", type=Path, default=Path("/tmp/ho600-cohort-csv-qc"))
    args = p.parse_args()
    print(json.dumps(run(args.original, args.csv, args.mapping, args.out),
                     ensure_ascii=False, indent=2))
if __name__ == "__main__":
    main()
