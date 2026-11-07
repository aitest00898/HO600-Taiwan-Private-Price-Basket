#!/usr/bin/env python3
"""Read-only, price-blind triage for HO600 Exact-2020 backfills.

Use current canonical Candidate_Pool and Quota_Control, not research checkpoints.
This ranks investigation leads; it NEVER grants Exact admission.
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import sys
from collections import defaultdict
from pathlib import Path

DOMAINS = ("食", "住／家用", "日常／個人", "衣", "行", "育", "樂")
FIELDS = (
    "candidate_id", "domain", "subcategory", "brand_or_merchant",
    "representative_item", "representative_spec", "channel_regions",
    "known_2026_quote_count", "subcategory_formal_exact",
    "subcategory_remaining_gap", "queue_status", "blocking_requirement",
)
REQUIRED_CANDIDATE = {
    "candidate_id", "ho600_domain", "ho600_subcategory", "brands",
    "representative_item", "representative_spec", "channel_regions",
    "migration_state", "exact2020_quote_count", "current2026_quote_count",
}
REQUIRED_QUOTA = ("Domain", "Subcategory", "Prequalified Exact concepts", "New exact needed")


def read_table(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        if reader.fieldnames is None:
            raise ValueError(f"{path}: CSV header missing")
        if len(reader.fieldnames) != len(set(reader.fieldnames)):
            raise ValueError(f"{path}: duplicate CSV column")
        missing = REQUIRED_CANDIDATE.difference(reader.fieldnames)
        if missing:
            raise ValueError(
                f"{path}: Candidate_Pool missing columns: {', '.join(sorted(missing))}"
            )
        rows = []
        for line_number, row in enumerate(reader, start=2):
            if None in row:
                raise ValueError(f"{path}: extra CSV field on row {line_number}")
            if any(value is None for value in row.values()):
                raise ValueError(f"{path}: missing CSV field on row {line_number}")
            rows.append(row)
        if not rows:
            raise ValueError(f"{path}: Candidate_Pool has no data rows")
        return rows


def read_excluded_ids(paths: list[Path]) -> set[str]:
    """Read previously queued or probed candidate IDs for cross-batch dedupe."""
    excluded: set[str] = set()
    for path in paths:
        with path.open(encoding="utf-8-sig", newline="") as stream:
            reader = csv.DictReader(stream)
            if reader.fieldnames is None:
                raise ValueError(f"{path}: exclusion CSV header missing")
            if len(reader.fieldnames) != len(set(reader.fieldnames)):
                raise ValueError(f"{path}: duplicate exclusion CSV column")
            if "candidate_id" not in reader.fieldnames:
                raise ValueError(f"{path}: exclusion CSV needs candidate_id column")
            file_ids: set[str] = set()
            for line_number, row in enumerate(reader, start=2):
                if None in row:
                    raise ValueError(f"{path}: extra exclusion field on row {line_number}")
                if any(value is None for value in row.values()):
                    raise ValueError(f"{path}: missing exclusion field on row {line_number}")
                candidate_id = row["candidate_id"]
                if not candidate_id or not candidate_id.strip():
                    raise ValueError(f"{path}: blank candidate_id on row {line_number}")
                if candidate_id != candidate_id.strip():
                    raise ValueError(f"{path}: padded candidate_id on row {line_number}")
                if candidate_id in file_ids:
                    raise ValueError(
                        f"{path}: duplicate candidate_id {candidate_id} on row {line_number}"
                    )
                file_ids.add(candidate_id)
            excluded.update(file_ids)
    return excluded


def read_quota(path: Path) -> dict[tuple[str, str], tuple[int, int]]:
    # Quota_Control.csv contains several tables. Select only the named subcategory
    # table and stop at the first blank/domain-total header.
    with path.open(encoding="utf-8-sig", newline="") as stream:
        raw = list(csv.reader(stream))
    start = next(
        (i for i, row in enumerate(raw)
         if len(row) >= 7 and row[0] == "Domain"
         and row[1] == "Subcategory" and row[6] == "New exact needed"),
        None,
    )
    if start is None:
        raise ValueError("Quota_Control subcategory header not found")
    header = raw[start]
    # The canonical quota CSV contains multiple side-by-side tables with
    # intentionally repeated headers; validate only the seven-column
    # subcategory table selected above.
    subcategory_header = header[:7]
    if len(subcategory_header) != len(set(subcategory_header)):
        raise ValueError("Quota_Control subcategory header has duplicate columns")
    missing = set(REQUIRED_QUOTA).difference(subcategory_header)
    if missing:
        raise ValueError(
            "Quota_Control subcategory header missing columns: "
            + ", ".join(sorted(missing))
        )
    exact_index = subcategory_header.index("Prequalified Exact concepts")
    gap_index = subcategory_header.index("New exact needed")
    quota: dict[tuple[str, str], tuple[int, int]] = {}
    for line_number, row in enumerate(raw[start + 1:], start=start + 2):
        if not row or row[0] not in DOMAINS:
            break
        if len(row) != len(header):
            raise ValueError(f"Truncated or over-wide quota row {line_number}")
        key = (row[0], row[1])
        if not row[1].strip():
            raise ValueError(f"Blank quota subcategory on row {line_number}")
        if key in quota:
            raise ValueError(f"Duplicate quota cell: {key}")
        try:
            exact, gap = int(row[exact_index]), int(row[gap_index])
        except (TypeError, ValueError) as exc:
            raise ValueError(f"Non-integer quota count on row {line_number}") from exc
        if exact < 0 or gap < 0:
            raise ValueError(f"Negative quota count: {key}")
        quota[key] = (exact, gap)
    if not quota:
        raise ValueError("No quota cells")
    return quota


def build_queue(candidates: list[dict[str, str]],
                quota: dict[tuple[str, str], tuple[int, int]],
                limit: int = 30, max_per_subcategory: int = 3,
                excluded_ids: set[str] | None = None,
                ) -> list[dict[str, str | int]]:
    if limit < 1 or max_per_subcategory < 1:
        raise ValueError("Limit and max-per-subcategory must be positive")
    excluded = excluded_ids or set()
    groups: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    seen: set[str] = set()
    for item in candidates:
        if not REQUIRED_CANDIDATE.issubset(item):
            raise ValueError("Canonical Candidate_Pool is missing columns")
        cid = item["candidate_id"]
        if not cid or not cid.strip():
            raise ValueError("Canonical Candidate_Pool has a blank candidate ID")
        if cid != cid.strip():
            raise ValueError(f"Candidate ID contains surrounding whitespace: {cid!r}")
        if cid in seen:
            raise ValueError(f"Duplicate candidate ID: {cid}")
        seen.add(cid)
        try:
            exact2020 = int(item["exact2020_quote_count"])
            current2026 = int(item["current2026_quote_count"])
        except (TypeError, ValueError) as exc:
            raise ValueError(f"Candidate {cid}: quote counts must be integers") from exc
        if exact2020 < 0 or current2026 < 0:
            raise ValueError(f"Candidate {cid}: quote counts cannot be negative")
        if cid in excluded:
            continue
        if item["migration_state"] != "RESEARCHABLE-CURRENT-ONLY":
            continue
        if exact2020 != 0 or current2026 < 1:
            continue
        key = (item["ho600_domain"], item["ho600_subcategory"])
        if key not in quota:
            raise ValueError(f"Candidate {cid}: no canonical quota cell for {key}")
        if quota[key][1] == 0:
            continue
        groups[key].append(item)

    for group in groups.values():
        group.sort(key=lambda item: item["candidate_id"])

    # Structural priority ONLY: zero-formal-Exact cells, size of remaining gap,
    # broad life-cost domain, stable ID. Never examine observed price movement.
    ordered = sorted(groups, key=lambda key: (
        0 if quota[key][0] == 0 else 1, -quota[key][1],
        DOMAINS.index(key[0]), key[1],
    ))
    selected: list[dict[str, str | int]] = []
    for turn in range(max_per_subcategory):
        for key in ordered:
            group = groups[key]
            if turn >= len(group):
                continue
            item = group[turn]
            exact, gap = quota[key]
            selected.append({
                "candidate_id": item["candidate_id"],
                "domain": key[0], "subcategory": key[1],
                "brand_or_merchant": item["brands"],
                "representative_item": item["representative_item"],
                "representative_spec": item["representative_spec"],
                "channel_regions": item["channel_regions"],
                "known_2026_quote_count": int(item["current2026_quote_count"]),
                "subcategory_formal_exact": exact,
                "subcategory_remaining_gap": gap,
                "queue_status": "BACKFILL_RESEARCH_NOT_EXACT",
                "blocking_requirement":
                    "VERIFY_2020_NORMAL_PRICE_AND_2026_IDENTITY_CHANNEL_SOURCE_CAPS",
            })
            if len(selected) >= limit:
                return selected
    return selected


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path,
                        default=Path(__file__).resolve().parents[1])
    parser.add_argument("--limit", type=int, default=30)
    parser.add_argument("--max-per-subcategory", type=int, default=3)
    parser.add_argument(
        "--exclude-csv", type=Path, action="append", default=[],
        help="Previous queue/probe CSV with candidate_id; may be repeated to avoid re-queuing prior batches",
    )
    args = parser.parse_args(argv)
    root = args.repo_root
    exclusion_paths = [
        path if path.is_absolute() else root / path for path in args.exclude_csv
    ]
    queue = build_queue(
        read_table(root / "data" / "Candidate_Pool.csv"),
        read_quota(root / "data" / "Quota_Control.csv"),
        args.limit, args.max_per_subcategory, read_excluded_ids(exclusion_paths),
    )
    output = csv.DictWriter(sys.stdout, fieldnames=FIELDS, lineterminator="\n")
    output.writeheader()
    output.writerows(queue)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
