"""Regression tests for price-blind Exact-2020 research triage."""
import csv
import io
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts.triage_exact_backfill import FIELDS, build_queue, read_quota


def item(cid, sub, state="RESEARCHABLE-CURRENT-ONLY", n20="0", n26="1"):
    return {
        "candidate_id": cid, "ho600_domain": "食", "ho600_subcategory": sub,
        "brands": "Brand", "representative_item": "Item",
        "representative_spec": "100g", "channel_regions": "retail",
        "migration_state": state, "exact2020_quote_count": n20,
        "current2026_quote_count": n26,
    }


class BackfillQueueTests(unittest.TestCase):
    def setUp(self):
        self.quota = {("食", "零Exact"): (0, 3), ("食", "高缺口"): (1, 9),
                      ("食", "飽和"): (3, 0)}

    def test_zero_exact_first_and_round_robin(self):
        inp = [item("C3", "高缺口"), item("C2", "零Exact"),
               item("C1", "零Exact"), item("C4", "高缺口")]
        rows = build_queue(inp, self.quota, limit=4)
        self.assertEqual([r["candidate_id"] for r in rows],
                         ["C1", "C3", "C2", "C4"])
        self.assertTrue(all(r["queue_status"] == "BACKFILL_RESEARCH_NOT_EXACT"
                            for r in rows))

    def test_ignore_historical_complete_and_no_current_and_saturated(self):
        inp = [item("A", "零Exact", n20="1"),
               item("B", "零Exact", n26="0"),
               item("C", "飽和"),
               item("D", "零Exact", state="RESEARCHABLE-IDENTITY-ONLY"),
               item("E", "零Exact")]
        self.assertEqual([r["candidate_id"] for r in build_queue(inp, self.quota)],
                         ["E"])

    def test_price_blind_output_and_deterministic(self):
        inp = [item("B", "零Exact"), item("A", "高缺口")]
        self.assertEqual(build_queue(inp, self.quota),
                         build_queue(list(reversed(inp)), self.quota))
        self.assertFalse(any(
            name in FIELDS
            for name in ("observed_price", "price_2020", "price_2026",
                         "price_change", "inflation", "return_pct")
        ))

    def test_duplicates_fail_closed(self):
        with self.assertRaisesRegex(ValueError, "Duplicate candidate ID"):
            build_queue([item("A", "零Exact"), item("A", "零Exact")],
                        self.quota)

    def test_invalid_limits(self):
        with self.assertRaises(ValueError):
            build_queue([item("A", "零Exact")], self.quota, limit=0)

    def test_read_real_canonical_if_available(self):
        if not (ROOT / "data" / "Candidate_Pool.csv").exists():
            self.skipTest("Canonical data unavailable")
        with (ROOT / "data" / "Candidate_Pool.csv").open(
                encoding="utf-8-sig", newline="") as f:
            candidates = list(csv.DictReader(f))
        quota = read_quota(ROOT / "data" / "Quota_Control.csv")
        rows = build_queue(candidates, quota, limit=30)
        self.assertEqual(len(rows), 30)
        self.assertEqual(len({r["candidate_id"] for r in rows}), 30)
        self.assertTrue(all(r["subcategory_remaining_gap"] > 0 for r in rows))
        self.assertEqual(len(quota), 57)  # 2026-10-31 post-Batch-9 snapshot


if __name__ == "__main__":
    unittest.main()
