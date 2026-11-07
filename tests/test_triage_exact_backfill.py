"""Regression tests for price-blind Exact-2020 research triage."""
import csv
import io
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts.triage_exact_backfill import (
    FIELDS, build_queue, read_excluded_ids, read_quota, read_table,
)


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

    def test_excluded_ids_prevent_cross_batch_requeue(self):
        rows = [item("A", "零Exact"), item("B", "零Exact"),
                item("C", "高缺口")]
        first = build_queue(rows, self.quota, limit=2)
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "previous.csv"
            with path.open("w", encoding="utf-8", newline="") as stream:
                writer = csv.DictWriter(stream, fieldnames=FIELDS)
                writer.writeheader()
                writer.writerows(first)
            excluded = read_excluded_ids([path])
        second = build_queue(rows, self.quota, limit=3, excluded_ids=excluded)
        self.assertEqual([row["candidate_id"] for row in second], ["B"])
        self.assertTrue(set(row["candidate_id"] for row in first).isdisjoint(
            row["candidate_id"] for row in second
        ))

    def test_exclusion_csv_must_be_well_formed_and_unique(self):
        cases = [
            ("other\nA\n", "needs candidate_id"),
            ("candidate_id\nA\nA\n", "duplicate candidate_id"),
            ("candidate_id\n \n", "blank candidate_id"),
            ("candidate_id,extra\nA\n", "missing exclusion field"),
            ("candidate_id\nA,extra\n", "extra exclusion field"),
        ]
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "bad.csv"
            for content, error in cases:
                with self.subTest(error=error):
                    path.write_text(content, encoding="utf-8")
                    with self.assertRaisesRegex(ValueError, error):
                        read_excluded_ids([path])

    def test_candidate_csv_rejects_duplicate_header_and_ragged_rows(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "candidate.csv"
            required = sorted({
                "candidate_id", "ho600_domain", "ho600_subcategory", "brands",
                "representative_item", "representative_spec", "channel_regions",
                "migration_state", "exact2020_quote_count", "current2026_quote_count",
            })
            path.write_text(",".join(required) + "\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "has no data rows"):
                read_table(path)

            path.write_text("candidate_id,candidate_id\nA,B\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "duplicate CSV column"):
                read_table(path)

            headers = sorted({
                "candidate_id", "ho600_domain", "ho600_subcategory", "brands",
                "representative_item", "representative_spec", "channel_regions",
                "migration_state", "exact2020_quote_count", "current2026_quote_count",
            })
            path.write_text(",".join(headers) + "\nA\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "missing CSV field"):
                read_table(path)

            path.write_text(",".join(headers) + "\nA," + ",".join(
                "x" for _ in range(len(headers))
            ) + "\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "extra CSV field"):
                read_table(path)

    def test_candidate_ids_and_counts_fail_closed(self):
        for candidate, error in [
            (item("", "零Exact"), "blank candidate ID"),
            (item(" A", "零Exact"), "surrounding whitespace"),
            (item("A", "零Exact", n20="not-a-number"), "must be integers"),
            (item("A", "零Exact", n26="-1"), "cannot be negative"),
            (item("A", "無配額"), "no canonical quota cell"),
        ]:
            with self.subTest(error=error):
                with self.assertRaisesRegex(ValueError, error):
                    build_queue([candidate], self.quota)

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
        self.assertEqual(len(quota), 50)  # 2026-10-31 post-Batch-9 subcategory rows
        self.assertFalse(any(sub == "Original target" for _, sub in quota))

    def test_quota_parser_validates_table_and_stops_before_domain_totals(self):
        header = ["Domain", "Subcategory", "Original target",
                  "Prequalified Exact concepts", "All migrated concepts",
                  "Legacy-preserving target", "New exact needed"]
        row = ["食", "稻米", "10", "0", "2", "10", "10"]
        aggregate = ["食", "", "10", "0", "2", "10", "10"]
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "quota.csv"
            with path.open("w", encoding="utf-8", newline="") as stream:
                writer = csv.writer(stream)
                writer.writerow(header)
                writer.writerow(row)
                writer.writerow([])
                writer.writerow(["Domain", "Original target", "Exact after Batch 9",
                                 "Legacy-preserving target", "New exact needed"])
                writer.writerow(aggregate)
            self.assertEqual(read_quota(path), {("食", "稻米"): (0, 10)})

            with path.open("w", encoding="utf-8", newline="") as stream:
                writer = csv.writer(stream)
                writer.writerow(["Domain", "Subcategory", "Original target", "Other",
                                 "All migrated", "Legacy target", "New exact needed"])
            with self.assertRaisesRegex(ValueError, "missing columns"):
                read_quota(path)

            bad_header = header.copy()
            bad_header[4] = bad_header[3]
            with path.open("w", encoding="utf-8", newline="") as stream:
                writer = csv.writer(stream)
                writer.writerow(bad_header)
            with self.assertRaisesRegex(ValueError, "duplicate columns"):
                read_quota(path)

            with path.open("w", encoding="utf-8", newline="") as stream:
                writer = csv.writer(stream)
                writer.writerow(header)
                writer.writerow(["食", "稻米", "10", "x", "2", "10", "10"])
            with self.assertRaisesRegex(ValueError, "Non-integer quota"):
                read_quota(path)

    def test_real_next_batch_is_disjoint_from_saved_queue(self):
        queue_path = ROOT / "research" / "batch-10" / "2026-11-07-price-blind-backfill-queue.csv"
        probes_path = ROOT / "research" / "batch-10" / "2026-11-07-source-probes.csv"
        if (not queue_path.exists() or not probes_path.exists()
                or not (ROOT / "data" / "Candidate_Pool.csv").exists()):
            self.skipTest("Canonical data, saved queue, or probe ledger unavailable")
        candidates = read_table(ROOT / "data" / "Candidate_Pool.csv")
        prior = read_excluded_ids([queue_path, probes_path])
        rows = build_queue(
            candidates, read_quota(ROOT / "data" / "Quota_Control.csv"),
            limit=30, excluded_ids=prior,
        )
        # The source-probe ledger may contain earlier batches. The queue
        # builder treats --limit as a maximum and can return fewer rows when
        # prior candidates exhaust the per-subcategory cap.
        self.assertGreater(len(rows), 0)
        self.assertLessEqual(len(rows), 30)
        self.assertTrue(prior.isdisjoint(row["candidate_id"] for row in rows))
        self.assertTrue(all(row["subcategory_remaining_gap"] > 0 for row in rows))


if __name__ == "__main__":
    unittest.main()
