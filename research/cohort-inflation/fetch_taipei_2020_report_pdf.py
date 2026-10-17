#!/usr/bin/env python3
"""Strict-HTTPS retrieval of the official Taipei 2020 Family Survey report PDF.

SCOPE: Taipei City 2020, not corrected NATIONAL 2020 age/occupation source.
Does NOT extract numeric weights or authorize a cohort index. Stdlib only.
"""
from __future__ import annotations
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
from urllib.parse import urlsplit

PDF_URL = (
    "https://www-ws.gov.taipei/Download.ashx?icon=.pdf&"
    "n=MTA55bm06Ie65YyX5biC5a625bqt5pS25pSv6Kiq5ZWP6Kq%2F5p%2Bl5aCx5ZGKLnBkZg%3D%3D&"
    "u=LzAwMS9VcGxvYWQvMzY3L3JlbGZpbGUvNDU2NzIvODQ3MTQxNy8wNjFmMDZlMy1iZjE1LTQzODYtOWNhYi1iMWM1YzdiNzBkZDMucGRm"
)
MAX_SIZE = 50_000_000

def validate_pdf_bytes(content: bytes) -> None:
    if not content or len(content) > MAX_SIZE:
        raise ValueError("Empty or oversized report")
    if not content.startswith(b"%PDF-"):
        raise ValueError("NOT_PDF: no PDF file signature; refuse HTML/error responses")
    if b"%%EOF" not in content[-8192:]:
        raise ValueError("TRUNCATED_PDF_OR_MALFORMED: no trailing PDF EOF marker")

def download(out: Path) -> dict:
    if out.exists() and any(out.iterdir()):
        raise FileExistsError("Use a new empty output directory; original bytes must not be overwritten")
    with tempfile.TemporaryDirectory(prefix="ho600-tpe-pdf-") as tmp:
        dest = Path(tmp) / "actual_report.part"
        command = [
            "curl", "--ca-native", "--fail", "--show-error", "--silent", "--location",
            "--proto", "=https", "--proto-redir", "=https", "--max-redirs", "2",
            "--connect-timeout", "12", "--max-time", "60", "--max-filesize", str(MAX_SIZE),
            "--output", str(dest), "--write-out",
            "%{url_effective}\n%{http_code}\n%{content_type}\n",
            PDF_URL,
        ]
        got = subprocess.run(command, capture_output=True, text=True, timeout=70, check=False)
        if got.returncode:
            raise RuntimeError(f"Official PDF TLS/HTTP download failed (curl {got.returncode}): {got.stderr[:250]}")
        meta = got.stdout.strip().splitlines()
        if len(meta) != 3 or meta[1] != "200":
            raise RuntimeError("Unexpected HTTP response; no PDF accepted")
        final = urlsplit(meta[0])
        if final.scheme != "https" or final.hostname != "www-ws.gov.taipei":
            raise ValueError("Unreviewed HTTPS redirect to another host; hold for source review")
        content = dest.read_bytes()
        validate_pdf_bytes(content)
        out.mkdir(parents=True, exist_ok=True)
        save = out / "taipei-2020-family-income-expenditure-official.pdf"
        receipt = out / "taipei-2020-family-income-expenditure-official.receipt.json"
        if save.exists() or receipt.exists():
            raise FileExistsError("Do not overwrite original report or receipt")
        save.write_bytes(content)
        result = {
            "status": "ORIGINAL_PDF_RAW_RETRIEVED_NO_DATA_EXTRACTION",
            "source_id": "TPE20-FAMILY-SURVEY-TABLE8-PDF",
            "official_landing": "https://data.gov.tw/dataset/133235",
            "requested_url": PDF_URL,
            "actual_final_url": meta[0],
            "response_type": meta[2],
            "http_code": 200,
            "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
            "raw_file_size_bytes": len(content),
            "raw_sha256": hashlib.sha256(content).hexdigest(),
            "year": 2020,
            "geo": "TAIPEI_CITY_ONLY",
            "table_candidate": "Table 8: Family Income and Expenditure by Age of Household Head",
            "numeric_table_extraction_verified": False,
            "household_age_proxy_weights_released": False,
            "retirement_population_inferred": False,
            "national_WGT01_satisfied": False,
        }
        receipt.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        return result

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--out", required=True, type=Path)
    args = p.parse_args()
    print(json.dumps(download(args.out), ensure_ascii=False, indent=2))
if __name__ == "__main__":
    main()
