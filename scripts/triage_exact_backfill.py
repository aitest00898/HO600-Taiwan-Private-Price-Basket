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
        return list(csv.DictReader(stream))


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
    quota: dict[tuple[str, str], tuple[int, int]] = {}
    for row in raw[start + 1:]:
        if not row or row[0] not in DOMAINS:
            break
        if len(row) < 7:
            raise ValueError("Truncated quota row")
        key = (row[0], row[1])
        if key in quota:
            raise ValueError(f"Duplicate quota cell: {key}")
        exact, gap = int(row[3]), int(row[6])
        if exact < 0 or gap < 0:
            raise ValueError(f"Negative quota count: {key}")
        quota[key] = (exact, gap)
    if not quota:
        raise ValueError("No quota cells")
    return quota


def build_queue(candidates: list[dict[str, str]],
                quota: dict[tuple[str, str], tuple[int, int]],
                limit: int = 30, max_per_subcategory: int = 3
                ) -> list[dict[str, str | int]]:
    if limit < 1 or max_per_subcategory < 1:
        raise ValueError("Limit and max-per-subcategory must be positive")
    groups: dict[tuple[str, str], list[dict[str, str]]] = defaultdict(list)
    seen: set[str] = set()
    for item in candidates:
        if not REQUIRED_CANDIDATE.issubset(item):
            raise ValueError("Canonical Candidate_Pool is missing columns")
        cid = item["candidate_id"]
        if cid in seen:
            raise ValueError(f"Duplicate candidate ID: {cid}")
        seen.add(cid)
        if item["migration_state"] != "RESEARCHABLE-CURRENT-ONLY":
            continue
        if int(item["exact2020_quote_count"]) != 0 or int(item["current2026_quote_count"]) < 1:
            continue
        key = (item["ho600_domain"], item["ho600_subcategory"])
        if key not in quota or quota[key][1] == 0:
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
    args = parser.parse_args(argv)
    root = args.repo_root
    queue = build_queue(
        read_table(root / "data" / "Candidate_Pool.csv"),
        read_quota(root / "data" / "Quota_Control.csv"),
        args.limit, args.max_per_subcategory,
    )
    output = csv.DictWriter(sys.stdout, fieldnames=FIELDS, lineterminator="\n")
    output.writeheader()
    output.writerows(queue)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
