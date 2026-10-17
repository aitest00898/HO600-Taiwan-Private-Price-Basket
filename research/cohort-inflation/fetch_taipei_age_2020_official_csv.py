#!/usr/bin/env python3
"""Strict-HTTPS 2020-containing Taipei age-head official CSV download and audit.

Separate regional evidence; NEVER a Taiwan-national WGT-01 source.
Uses macOS native CA curl with full TLS verification. No network sandbox bypass,
no TLS -k, no CA changes, no artifact_tool and no GitHub Actions.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
import pathlib
import re
import subprocess
import tempfile
from datetime import datetime, timezone
from urllib.parse import urlsplit

DATASET_URL = "https://data.taipei/dataset/detail?id=26c3817c-0713-4657-8cd8-aa842eb59f97"
CANDIDATES = (
    "https://data.taipei/api/frontstage/tpeod/dataset/resource.download?rid=63e4d839-ef65-46a8-b4d1-1bbfeeca5516",
    "https://data.taipei/api/dataset/26c3817c-0713-4657-8cd8-aa842eb59f97/resource/63e4d839-ef65-46a8-b4d1-1bbfeeca5516/download",
)
MAX_BYTES = 1_000_000

def fingerprint(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()

def year_2020(s: str) -> bool:
    return bool(re.search(r"(?<![0-9])(?:109|2020)(?![0-9])", s))

def parse_csv(raw: bytes) -> dict:
    if not raw or len(raw) > MAX_BYTES:
        raise ValueError("Empty or oversized official CSV")
    if raw.lstrip()[:30].lower().startswith((b"<html", b"<!doctype html", b"{")):
        raise ValueError("HTML/JSON is not official CSV")
    errors = []
    for encoding in ("utf-8-sig", "cp950"):
        try:
            text = raw.decode(encoding)
            reader = list(csv.reader(text.splitlines()))
            if len(reader) < 2:
                raise ValueError("CSV missing data rows")
            header = reader[0]
            if len(header) < 25 or len(set(header)) != len(header):
                raise ValueError("Not the expected detailed household age CSV header")
            if not any("年別" in x for x in header):
                raise ValueError("No year column")
            if not any("年齡" in x and "戶長" in x for x in header):
                raise ValueError("No age-of-head column")
            if not any("消費支出" in x for x in header) or not any("醫療保健" in x for x in header):
                raise ValueError("No complete 12-class spending structure")
            year_col = next(i for i, x in enumerate(header) if "年別" in x)
            age_col = next(i for i, x in enumerate(header) if "年齡" in x and "戶長" in x)
            data = [row for row in reader[1:] if len(row) > max(year_col, age_col)]
            year_rows = [row for row in data if year_2020(row[year_col])]
            if not year_rows:
                raise ValueError("2020 / ROC109 not found, no invented baseline")
            return {
                "encoding": encoding,
                "data_rows": len(data),
                "column_count": len(header),
                "year2020_rows": len(year_rows),
                "age_groups_2020": sorted(set(row[age_col] for row in year_rows)),
                "header_sha256": fingerprint(",".join(header).encode("utf-8")),
                "category_2020_values_verified": False,
                "cohort_proxy_weights_generated": False,
                "geographic_scope": "TAIPEI_ONLY",
                "national_WGT01_satisfied": False,
            }
        except (UnicodeError, ValueError, csv.Error) as ex:
            errors.append(f"{encoding}: {ex}")
    raise ValueError("CSV content validation failed: " + "; ".join(errors))

def download_one(url: str, tmpfile: pathlib.Path) -> tuple[bytes, str, str]:
    if url not in CANDIDATES:
        raise ValueError("Not a registered official city download")
    command = [
        "curl", "--ca-native", "--fail", "--silent", "--show-error",
        "--location", "--proto", "=https", "--proto-redir", "=https",
        "--max-redirs", "2", "--connect-timeout", "12", "--max-time", "45",
        "--output", str(tmpfile), "--write-out",
        "%{url_effective}\n%{http_code}\n%{content_type}\n", url,
    ]
    done = subprocess.run(command, capture_output=True, text=True, timeout=55, check=False)
    if done.returncode != 0:
        raise RuntimeError(f"TLS/HTTP failure: curl exit {done.returncode}: {done.stderr[:300]}")
    meta = done.stdout.strip().splitlines()
    if len(meta) != 3 or meta[1] != "200":
        raise ValueError(f"HTTP non-200 or bad metadata: {meta!r}")
    actual = meta[0]
    final = urlsplit(actual)
    if final.scheme != "https" or final.hostname != "data.taipei":
        raise ValueError(f"Unreviewed redirect hostname; refuse URL {actual}")
    raw = tmpfile.read_bytes()
    if not raw:
        raise ValueError("Official CSV response empty")
    return raw, actual, meta[2]

def run(out: pathlib.Path) -> dict:
    if out.exists() and any(out.iterdir()):
        raise FileExistsError("Output dir must be new or empty to avoid overwriting receipts")
    observations = []
    for url in CANDIDATES:
        with tempfile.TemporaryDirectory(prefix="ho600-tpe-") as td:
            try:
                raw, final_url, content_type = download_one(url, pathlib.Path(td)/"data.tmp")
                qa = parse_csv(raw)
            except (RuntimeError, ValueError, subprocess.TimeoutExpired) as ex:
                observations.append({"url": url, "state": "FAILED_OR_REJECTED", "error": str(ex)})
                continue
            out.mkdir(parents=True, exist_ok=True)
            target = out/"TPE_AGE_2012_2023_official_raw.csv"
            target.write_bytes(raw)
            receipt = {
                "source_id": "TPE-AGE-2012-2023", "source_landing": DATASET_URL,
                "requested_url": url, "final_url": final_url,
                "http_status": 200, "response_content_type": content_type,
                "utc_retrieved": datetime.now(timezone.utc).isoformat(),
                "raw_bytes": len(raw), "sha256": fingerprint(raw),
                "data_profile": qa,
                "classification": "OFFICIAL_RAW_RETRIEVED_SCHEMA_INSPECTED_NOT_NATIONAL",
                "weights_status": "NOT_EXTRACTED",
                "cannot_replace_national_WGT01": True,
            }
            (out/"TPE_AGE_2012_2023.receipt.json").write_text(
                json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            return receipt
    return {
        "classification":"NO_TRUSTED_OR_SCHEMA_VALID_OFFICIAL_CSV",
        "candidate_attempts":observations,
        "raw_files":0,
        "Taipei_weights":"HOLD",
        "national_WGT01":"HOLD"
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--out", required=True, type=pathlib.Path)
    args=p.parse_args()
    print(json.dumps(run(args.out),ensure_ascii=False,indent=2))

if __name__=="__main__":
    main()
