#!/usr/bin/env python3
"""Strict-TLS readability receipts for URLs already present in Batch 9 ledgers.

This tool does not discover or replace sources. It performs bounded GETs only for
the fixed ledger URLs, records response metadata and a capped body hash, and never
disables certificate or hostname verification.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import ssl
import threading
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[2]
LEDGER_DIR = ROOT / "research" / "batch-09"
OUTPUT_DEFAULT = LEDGER_DIR / "source-readability-c01-c05-2026-10-30.csv"
MAX_BODY_BYTES = 2_000_000
TIMEOUT_SECONDS = 12
MAX_WORKERS = 4

FIELDS = [
    "requested_url",
    "final_url",
    "retrieved_at_utc",
    "http_status",
    "tls_validation",
    "content_type",
    "declared_content_length",
    "bytes_read",
    "sha256",
    "hash_kind",
    "result",
    "error",
]


def ledger_urls(checkpoints: range) -> list[str]:
    urls: set[str] = set()
    for checkpoint in checkpoints:
        path = LEDGER_DIR / f"checkpoint-{checkpoint:02d}-ledger.csv"
        with path.open("r", encoding="utf-8-sig", newline="") as stream:
            for row in csv.DictReader(stream):
                for field in ("source_2020", "source_2026"):
                    value = row[field].strip()
                    if value:
                        urls.add(value)
    return sorted(urls)


def probe(url: str, context: ssl.SSLContext, host_locks: dict[str, threading.Semaphore], map_lock: threading.Lock) -> dict[str, str]:
    host = urlsplit(url).netloc
    with map_lock:
        semaphore = host_locks.setdefault(host, threading.Semaphore(1))

    with semaphore:
        row = {field: "" for field in FIELDS}
        row.update(
            requested_url=url,
            retrieved_at_utc=dt.datetime.now(dt.timezone.utc).isoformat().replace("+00:00", "Z"),
            tls_validation="PASS: ssl.create_default_context; CERT_REQUIRED; hostname verification enabled",
            bytes_read="0",
        )
        request = urllib.request.Request(
            url,
            headers={
                "User-Agent": "HO600-Batch09-source-readability-audit/2026-10-30",
                "Accept": "text/html,application/json,application/pdf,*/*",
            },
        )
        try:
            with urllib.request.urlopen(request, context=context, timeout=TIMEOUT_SECONDS) as response:
                digest = hashlib.sha256()
                size = 0
                while size < MAX_BODY_BYTES:
                    chunk = response.read(min(65_536, MAX_BODY_BYTES - size))
                    if not chunk:
                        break
                    digest.update(chunk)
                    size += len(chunk)
                truncated = size == MAX_BODY_BYTES and response.read(1) != b""
                row.update(
                    final_url=response.geturl(),
                    http_status=str(response.status),
                    content_type=response.headers.get("Content-Type", ""),
                    declared_content_length=response.headers.get("Content-Length", ""),
                    bytes_read=str(size),
                    sha256=digest.hexdigest(),
                    hash_kind=(
                        f"SHA-256 of first {MAX_BODY_BYTES} response-body bytes (read capped)"
                        if truncated
                        else "SHA-256 of complete response body"
                    ),
                    result="HTTP_BODY_READ",
                )
        except urllib.error.HTTPError as error:
            body = error.read(MAX_BODY_BYTES)
            row.update(
                final_url=error.geturl(),
                http_status=str(error.code),
                content_type=error.headers.get("Content-Type", ""),
                declared_content_length=error.headers.get("Content-Length", ""),
                bytes_read=str(len(body)),
                sha256=hashlib.sha256(body).hexdigest(),
                hash_kind="SHA-256 of HTTP error response body (capped)",
                result="HTTP_ERROR",
                error=f"HTTPError: {error.code}",
            )
        except Exception as error:  # record failures; do not retry or weaken TLS
            row.update(result="FETCH_ERROR", error=f"{type(error).__name__}: {error}")
            reason = getattr(error, "reason", None)
            if isinstance(error, ssl.SSLError) or isinstance(reason, ssl.SSLError):
                row["tls_validation"] = "FAIL: strict TLS handshake/certificate validation failed"
                row["result"] = "TLS_ERROR"
        return row


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--first-checkpoint", type=int, default=1)
    parser.add_argument("--last-checkpoint", type=int, default=5)
    parser.add_argument("--out", type=Path, default=OUTPUT_DEFAULT)
    args = parser.parse_args()
    if not 1 <= args.first_checkpoint <= args.last_checkpoint <= 8:
        parser.error("checkpoint range must be within 1..8")

    urls = ledger_urls(range(args.first_checkpoint, args.last_checkpoint + 1))
    context = ssl.create_default_context()
    context.verify_mode = ssl.CERT_REQUIRED
    context.check_hostname = True
    host_locks: dict[str, threading.Semaphore] = {}
    map_lock = threading.Lock()
    args.out.parent.mkdir(parents=True, exist_ok=True)

    with args.out.open("w", encoding="utf-8-sig", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=FIELDS)
        writer.writeheader()
        stream.flush()
        results: list[dict[str, str]] = []
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
            futures = [executor.submit(probe, url, context, host_locks, map_lock) for url in urls]
            for index, future in enumerate(as_completed(futures), start=1):
                row = future.result()
                results.append(row)
                writer.writerow(row)
                stream.flush()
                if index % 20 == 0 or index == len(urls):
                    print(f"read {index}/{len(urls)} fixed ledger URLs", flush=True)

    failures = sum(row["result"] != "HTTP_BODY_READ" or row["http_status"] != "200" for row in results)
    print(f"urls={len(urls)} failures_or_non_200={failures} output={args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
