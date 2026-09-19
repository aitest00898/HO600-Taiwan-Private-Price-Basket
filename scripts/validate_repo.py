#!/usr/bin/env python3
from __future__ import annotations

import csv
import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
STATUS_PATH = ROOT / "canonical" / "status.json"

EXPECTED_SHEETS = [
    "README_Status",
    "Candidate_Pool",
    "Basket_600",
    "Evidence",
    "Quota_Control",
    "Index_Calc",
    "Validation_Release",
]

FORBIDDEN_CANDIDATE_HEADER_PATTERNS = [
    re.compile(r"2020.*price", re.I),
    re.compile(r"2026.*price", re.I),
    re.compile(r"price.*change", re.I),
    re.compile(r"pct.*change", re.I),
    re.compile(r"percent.*change", re.I),
    re.compile(r"漲幅"),
    re.compile(r"漲跌"),
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def pass_(message: str) -> None:
    print(f"PASS: {message}")


def read_csv(path: Path) -> list[list[str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.reader(f))


def to_int(value: str) -> int:
    text = str(value).strip()
    if not text:
        return 0
    try:
        return int(float(text))
    except ValueError:
        fail(f"Expected numeric value, got {value!r}")
        return 0


def workbook_sheet_names(workbook: Path) -> list[str]:
    with zipfile.ZipFile(workbook) as zf:
        root = ET.fromstring(zf.read("xl/workbook.xml"))
    ns = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
    return [node.attrib["name"] for node in root.findall("m:sheets/m:sheet", ns)]


def workbook_error_cells(workbook: Path) -> list[tuple[str, str]]:
    errors: list[tuple[str, str]] = []
    ns = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
    with zipfile.ZipFile(workbook) as zf:
        for name in zf.namelist():
            if not re.fullmatch(r"xl/worksheets/sheet\d+\.xml", name):
                continue
            root = ET.fromstring(zf.read(name))
            for cell in root.findall(".//m:c[@t='e']", ns):
                ref = cell.attrib.get("r", "?")
                value = cell.findtext("m:v", default="?", namespaces=ns)
                errors.append((f"{name}!{ref}", value))
    return errors


def main() -> int:
    if not STATUS_PATH.exists():
        fail("canonical/status.json is missing")
    status = json.loads(STATUS_PATH.read_text(encoding="utf-8"))

    workbook = ROOT / status["canonical_workbook"]
    if not workbook.exists():
        fail(f"Canonical workbook missing: {workbook.relative_to(ROOT)}")

    actual_sha = hashlib.sha256(workbook.read_bytes()).hexdigest()
    expected_sha = status["canonical_workbook_sha256"]
    if actual_sha != expected_sha:
        fail(f"Workbook SHA-256 mismatch: {actual_sha} != {expected_sha}")
    pass_(f"canonical workbook SHA-256 = {actual_sha}")

    sheets = workbook_sheet_names(workbook)
    if sheets != EXPECTED_SHEETS:
        fail(f"Workbook sheet architecture drift: {sheets!r}")
    pass_("active workbook architecture = 7 expected sheets")

    error_cells = workbook_error_cells(workbook)
    if error_cells:
        fail(f"Workbook contains formula/error cells: {error_cells[:10]!r}")
    pass_("workbook error-cell scan = 0")

    required_csvs = [ROOT / "data" / f"{name}.csv" for name in EXPECTED_SHEETS]
    missing = [str(p.relative_to(ROOT)) for p in required_csvs if not p.exists()]
    if missing:
        fail(f"Missing CSV snapshots: {missing}")
    pass_("all 7 CSV snapshots present")

    candidate_rows = read_csv(ROOT / "data" / "Candidate_Pool.csv")
    if not candidate_rows:
        fail("Candidate_Pool.csv is empty")
    headers = candidate_rows[0]
    forbidden = [
        h for h in headers
        if h and any(pattern.search(h) for pattern in FORBIDDEN_CANDIDATE_HEADER_PATTERNS)
    ]
    if forbidden:
        fail(f"Candidate_Pool price-blindness violated by headers: {forbidden}")
    pass_("Candidate_Pool remains blind to price/change columns")

    candidate_count = len(candidate_rows) - 1
    if candidate_count != int(status["candidate_concepts"]):
        fail(f"Candidate count mismatch: {candidate_count} != {status['candidate_concepts']}")
    pass_(f"candidate concepts = {candidate_count}")

    header_index = {name: idx for idx, name in enumerate(headers)}
    for required in ("exact2020_quote_count", "current2026_quote_count"):
        if required not in header_index:
            fail(f"Candidate_Pool missing required column: {required}")
    exact_count = sum(
        1
        for row in candidate_rows[1:]
        if to_int(row[header_index["exact2020_quote_count"]]) > 0
        and to_int(row[header_index["current2026_quote_count"]]) > 0
    )
    if exact_count != int(status["formal_exact_concepts"]):
        fail(f"Exact concept count mismatch: {exact_count} != {status['formal_exact_concepts']}")
    pass_(f"formal Exact-2020↔2026 concepts = {exact_count}")

    target = int(status["target_concepts"])
    remaining = target - exact_count
    if remaining != int(status["remaining_concepts"]):
        fail(f"Remaining count mismatch: {remaining} != {status['remaining_concepts']}")
    pass_(f"remaining concepts = {remaining}")

    evidence_rows = read_csv(ROOT / "data" / "Evidence.csv")
    evidence_count = len(evidence_rows) - 1
    if evidence_count != int(status["evidence_records"]):
        fail(f"Evidence count mismatch: {evidence_count} != {status['evidence_records']}")
    pass_(f"evidence records = {evidence_count}")

    validation = read_csv(ROOT / "data" / "Validation_Release.csv")
    if not validation or validation[0][:4] != ["Check", "Result", "Expected", "Status"]:
        fail("Validation_Release.csv header is unexpected")
    non_pass = [row for row in validation[1:] if row and any(row) and len(row) > 3 and row[3] != "PASS"]
    if non_pass:
        fail(f"Validation_Release contains non-PASS rows: {non_pass[:5]!r}")
    pass_("Validation_Release rows = PASS")

    basket = read_csv(ROOT / "data" / "Basket_600.csv")
    flat_basket = [cell for row in basket for cell in row]
    if status["basket_sealed"] is False and "NOT SEALED" not in flat_basket:
        fail("Basket status mismatch: expected NOT SEALED")
    pass_("Basket_600 = NOT SEALED")

    index_rows = read_csv(ROOT / "data" / "Index_Calc.csv")
    flat_index = [cell for row in index_rows for cell in row]
    if status["index_status"] not in flat_index:
        fail(f"Index lock mismatch: expected {status['index_status']}")
    pass_(f"Index_Calc = {status['index_status']}")

    print("\nHO600 repository validation: ALL CHECKS PASSED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
