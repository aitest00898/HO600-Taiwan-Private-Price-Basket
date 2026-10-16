#!/usr/bin/env python3
"""Manual local-only retrieval of OFFICIAL HO600 cohort expenditure tables.

No GitHub Actions; no auth/cookies/proxy bypass; no synthetic prices or weights.
Examples:
    python research/cohort-inflation/fetch_official_weight_tables.py --plan
    python research/cohort-inflation/fetch_official_weight_tables.py --download NAT20-AGE --output-dir /tmp/ho600-sources
Requires the official source register alongside this script.
"""
from __future__ import annotations
import argparse
import csv
import hashlib
import json
import pathlib
import urllib.parse
import urllib.request
from datetime import datetime, timezone

HERE = pathlib.Path(__file__).resolve().parent
REGISTER = HERE / "official-weight-source-register-2026-10-16.csv"
ALLOWED_HOSTS = {"ws.dgbas.gov.tw", "data.taipei"}
MAX_BYTES = 30_000_000

def load_sources():
    with REGISTER.open(encoding="utf-8-sig", newline="") as f:
        records = list(csv.DictReader(f))
    assert len(records) == 9, "Source register changed: explicit review required"
    ids = [r["source_id"] for r in records]
    assert len(ids) == len(set(ids)), "Duplicate source ID"
    return {r["source_id"]: r for r in records}

def validate_url(url):
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme != "https" or parsed.hostname not in ALLOWED_HOSTS:
        raise ValueError("Only registered official HTTPS hosts permitted")
    if parsed.username or parsed.password:
        raise ValueError("URL credentials forbidden")
    return parsed

def classify(raw, suffix):
    head = raw[:128].lstrip().lower()
    if head.startswith((b"<!doctype html", b"<html", b"<?xml version")) and suffix != ".ods":
        raise ValueError("Not a verified table: HTML/XML response")
    if suffix == ".xls":
        if not (raw.startswith(bytes.fromhex("D0CF11E0A1B11AE1")) or raw.startswith(b"PK\x03\x04")):
            raise ValueError("Not an Excel XLS/OLE workbook")
    elif suffix == ".ods":
        if not raw.startswith(b"PK\x03\x04"):
            raise ValueError("Not an ODF/ZIP spreadsheet")
    elif suffix == ".csv":
        if b"\x00" in raw[:4096]:
            raise ValueError("Binary/invalid CSV payload")
    else:
        raise ValueError("Unsupported extension: " + suffix)

def fetch(record, output_dir):
    source_id = record["source_id"]
    url = record["exact_download_url"]
    if not url:
        raise ValueError(source_id + ": no official raw download URL")
    parsed = validate_url(url)
    suffix = pathlib.PurePosixPath(parsed.path).suffix.lower()
    if suffix not in {".xls", ".ods", ".csv"}:
        raise ValueError("Unsupported raw source extension")
    req = urllib.request.Request(url, headers={"User-Agent": "HO600-research-source-audit/1.0", "Accept": "*/*"})
    with urllib.request.urlopen(req, timeout=20) as response:
        actual_url = response.geturl()
        validate_url(actual_url)
        raw = response.read(MAX_BYTES + 1)
        content_type = response.headers.get("Content-Type", "")
        status_code = response.status
    if status_code != 200 or not raw or len(raw) > MAX_BYTES:
        raise ValueError("Non-200, empty or oversized official source")
    classify(raw, suffix)
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / (source_id + suffix)
    if target.exists():
        raise FileExistsError(str(target) + " exists; never overwrite provenance")
    target.write_bytes(raw)
    receipt = {
        "source_id": source_id,
        "download_url": url,
        "final_url": actual_url,
        "http_status": status_code,
        "content_type": content_type,
        "retrieved_utc": datetime.now(timezone.utc).isoformat(),
        "raw_bytes": len(raw),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "path": str(target),
        "parsing_validated": False,
        "expenditure_weights_verified": False
    }
    (output_dir / (source_id + ".receipt.json")).write_text(
        json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return receipt

def main():
    parser = argparse.ArgumentParser()
    mx = parser.add_mutually_exclusive_group(required=True)
    mx.add_argument("--plan", action="store_true")
    mx.add_argument("--download", metavar="SOURCE_ID")
    parser.add_argument("--output-dir", type=pathlib.Path, default=HERE / "_local-only-not-for-git")
    args = parser.parse_args()
    sources = load_sources()
    if args.plan:
        for r in sources.values():
            print(json.dumps({"id": r["source_id"], "year": r["year"],
                "status": r["raw_data_state"], "has_direct_url": bool(r["exact_download_url"])},
                ensure_ascii=False))
        return
    if args.download not in sources:
        parser.error("Unknown registered SOURCE_ID")
    receipt = fetch(sources[args.download], args.output_dir)
    print(json.dumps(receipt, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
