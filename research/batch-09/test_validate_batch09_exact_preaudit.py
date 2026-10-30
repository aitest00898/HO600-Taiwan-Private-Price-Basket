from __future__ import annotations

import csv
import shutil
import tempfile
import unittest
from pathlib import Path

from validate_batch09_exact_preaudit import validate


REPO_ROOT = Path(__file__).resolve().parents[2]
LEDGER_FILES = [f"checkpoint-{number:02d}-ledger.csv" for number in range(1, 9)]
SUPPORT_FILES = [
    "batch09-brand-corporate-group-crosswalk.csv",
    "batch09-product-family-crosswalk.csv",
    "batch09-candidate-pool-dedup.csv",
    "batch09-candidate-pool-top5-2026-10-30.csv",
    "exact-admission-preaudit-2026-10-30.csv",
    "exact-admission-candidate-list-2026-10-30.csv",
    "source-readability-receipts-2026-10-30.csv",
]


class Batch09PreauditValidatorTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        target = self.root / "research" / "batch-09"
        target.mkdir(parents=True)
        for name in LEDGER_FILES + SUPPORT_FILES:
            shutil.copy2(REPO_ROOT / "research" / "batch-09" / name, target / name)
        (self.root / "data").mkdir()
        shutil.copy2(REPO_ROOT / "data" / "Candidate_Pool.csv", self.root / "data" / "Candidate_Pool.csv")

    def tearDown(self) -> None:
        self.temp.cleanup()

    def path(self, name: str) -> Path:
        return self.root / "research" / "batch-09" / name

    def read(self, name: str) -> tuple[list[str], list[dict[str, str]]]:
        with self.path(name).open("r", encoding="utf-8-sig", newline="") as stream:
            reader = csv.DictReader(stream)
            return list(reader.fieldnames or []), list(reader)

    def write(self, name: str, fields: list[str], rows: list[dict[str, str]]) -> None:
        with self.path(name).open("w", encoding="utf-8-sig", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=fields, extrasaction="ignore")
            writer.writeheader()
            writer.writerows(rows)

    def errors(self) -> list[str]:
        return validate(self.root)[0]

    def test_all_eight_ledgers_and_preaudit_pass(self) -> None:
        errors, summary = validate(self.root)
        self.assertEqual(errors, [])
        self.assertEqual(summary["rows"], 160)
        self.assertEqual(summary["unique_ids"], 160)
        self.assertEqual(summary["candidate_ready_count"], 2)

    def test_missing_checkpoint_is_rejected(self) -> None:
        self.path("checkpoint-08-ledger.csv").unlink()
        self.assertTrue(any("missing ledger" in error for error in self.errors()))

    def test_wrong_csv_header_is_rejected(self) -> None:
        fields, rows = self.read("checkpoint-01-ledger.csv")
        fields[0] = "unexpected_id"
        self.write("checkpoint-01-ledger.csv", fields, rows)
        self.assertTrue(any("schema/header mismatch" in error for error in self.errors()))

    def test_extra_field_in_csv_row_is_rejected(self) -> None:
        path = self.path("checkpoint-01-ledger.csv")
        lines = path.read_text(encoding="utf-8").splitlines()
        lines[1] += ",unexpected-extra-field"
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        self.assertTrue(any("CSV row has fields beyond the fixed schema" in error for error in self.errors()))

    def test_duplicate_global_id_is_rejected(self) -> None:
        fields, rows = self.read("checkpoint-02-ledger.csv")
        rows[0]["research_id"] = "B09-C01-001"
        self.write("checkpoint-02-ledger.csv", fields, rows)
        self.assertTrue(any("duplicate research_id" in error for error in self.errors()))

    def test_nonpositive_price_is_rejected(self) -> None:
        fields, rows = self.read("checkpoint-01-ledger.csv")
        rows[0]["normal_price_2020"] = "0"
        self.write("checkpoint-01-ledger.csv", fields, rows)
        self.assertTrue(any("invalid/nonpositive 2020 price" in error for error in self.errors()))

    def test_non_2020_observation_year_is_rejected(self) -> None:
        fields, rows = self.read("checkpoint-03-ledger.csv")
        rows[0]["date_2020"] = "2021-01-01"
        self.write("checkpoint-03-ledger.csv", fields, rows)
        self.assertTrue(any("2020 date/year is not explicit" in error for error in self.errors()))

    def test_unaccepted_decision_state_is_rejected(self) -> None:
        fields, rows = self.read("checkpoint-01-ledger.csv")
        rows[0]["decision"] = "HOLD"
        self.write("checkpoint-01-ledger.csv", fields, rows)
        self.assertTrue(any("fixed decision is not ADMISSIBLE" in error for error in self.errors()))

    def test_non_https_source_is_rejected(self) -> None:
        fields, rows = self.read("checkpoint-01-ledger.csv")
        rows[0]["source_2020"] = "http://example.com/source"
        self.write("checkpoint-01-ledger.csv", fields, rows)
        self.assertTrue(any("source URL must use HTTPS" in error for error in self.errors()))

    def test_tls_failure_cannot_be_recorded_as_pass(self) -> None:
        fields, rows = self.read("source-readability-receipts-2026-10-30.csv")
        row = next(item for item in rows if item["result"] == "TLS_ERROR")
        row["tls_validation"] = "PASS: invalid fixture"
        self.write("source-readability-receipts-2026-10-30.csv", fields, rows)
        self.assertTrue(any("TLS error recorded as passing" in error for error in self.errors()))

    def test_2020_source_concentration_over_six_is_rejected(self) -> None:
        fields, rows = self.read("checkpoint-01-ledger.csv")
        for row in rows[:7]:
            row["source_2020"] = "https://example.com/shared-source"
        self.write("checkpoint-01-ledger.csv", fields, rows)
        self.assertTrue(any("source concentration exceeds 6" in error for error in self.errors()))

    def test_brand_concentration_over_eight_is_rejected(self) -> None:
        fields, rows = self.read("checkpoint-01-ledger.csv")
        for row in rows[:9]:
            row["brand_or_merchant"] = "Cap Test Brand"
        self.write("checkpoint-01-ledger.csv", fields, rows)
        self.assertTrue(any("brand concentration exceeds 8" in error for error in self.errors()))

    def test_product_family_over_two_is_rejected(self) -> None:
        fields, rows = self.read("batch09-product-family-crosswalk.csv")
        for row in rows[:3]:
            row["family_key"] = "FAMILY-OVER-CAP"
        self.write("batch09-product-family-crosswalk.csv", fields, rows)
        self.assertTrue(any("over-cap product family" in error for error in self.errors()))

    def test_family_crosswalk_must_match_declared_ledger_count(self) -> None:
        fields, rows = self.read("batch09-product-family-crosswalk.csv")
        rows[0]["declared_family_count"] = "2" if rows[0]["declared_family_count"] == "1" else "1"
        self.write("batch09-product-family-crosswalk.csv", fields, rows)
        self.assertTrue(any("family crosswalk declared count differs" in error for error in self.errors()))

    def test_ledger_family_count_over_two_is_rejected(self) -> None:
        fields, rows = self.read("checkpoint-01-ledger.csv")
        rows[0]["product_family_count"] = "3"
        self.write("checkpoint-01-ledger.csv", fields, rows)
        self.assertTrue(any("product family count must be 1 or 2" in error for error in self.errors()))

    def test_missing_corporate_group_attribution_is_rejected(self) -> None:
        fields, rows = self.read("batch09-brand-corporate-group-crosswalk.csv")
        rows = rows[1:]
        self.write("batch09-brand-corporate-group-crosswalk.csv", fields, rows)
        self.assertTrue(any("corporate group attribution missing" in error for error in self.errors()))

    def test_consolidated_corporate_group_over_sixteen_is_rejected(self) -> None:
        fields, ledger_rows = self.read("checkpoint-01-ledger.csv")
        brands = {row["brand_or_merchant"] for row in ledger_rows}
        for number in range(2, 9):
            _, part = self.read(f"checkpoint-{number:02d}-ledger.csv")
            brands.update(row["brand_or_merchant"] for row in part)
        group_fields, group_rows = self.read("batch09-brand-corporate-group-crosswalk.csv")
        for row in group_rows:
            if row["brand_or_merchant"] in brands:
                row["corporate_group_id"] = "TEST-OVER-CAP-GROUP"
                row["attribution_status"] = "VERIFIED_CONSOLIDATED_GROUP"
        self.write("batch09-brand-corporate-group-crosswalk.csv", group_fields, group_rows)
        self.assertTrue(any("consolidated corporate group exceeds 16" in error for error in self.errors()))

    def test_unknown_candidate_pool_id_is_rejected(self) -> None:
        fields, rows = self.read("batch09-candidate-pool-dedup.csv")
        link = next(row for row in rows if row["candidate_id"])
        link["candidate_id"] = "LEG-EC-99999"
        self.write("batch09-candidate-pool-dedup.csv", fields, rows)
        self.assertTrue(any("unknown Candidate Pool ID" in error for error in self.errors()))

    def test_duplicate_product_identity_is_rejected(self) -> None:
        fields, rows = self.read("checkpoint-01-ledger.csv")
        rows[1]["brand_or_merchant"] = rows[0]["brand_or_merchant"]
        rows[1]["subcategory"] = rows[0]["subcategory"]
        rows[1]["concept"] = rows[0]["concept"]
        rows[1]["model_sku_plan"] = rows[0]["model_sku_plan"]
        rows[1]["channel_geography"] = rows[0]["channel_geography"]
        self.write("checkpoint-01-ledger.csv", fields, rows)
        self.assertTrue(any("duplicate product/service identity" in error for error in self.errors()))

    def test_missing_row_level_reason_is_rejected(self) -> None:
        fields, rows = self.read("exact-admission-preaudit-2026-10-30.csv")
        rows[0]["reason"] = ""
        self.write("exact-admission-preaudit-2026-10-30.csv", fields, rows)
        self.assertTrue(any("preaudit reason is required" in error for error in self.errors()))

    def test_each_row_must_compare_all_418_candidates(self) -> None:
        fields, rows = self.read("batch09-candidate-pool-dedup.csv")
        rows[0]["candidate_pool_rows_reviewed"] = "417"
        self.write("batch09-candidate-pool-dedup.csv", fields, rows)
        self.assertTrue(any("review against all 418" in error for error in self.errors()))


if __name__ == "__main__":
    unittest.main(verbosity=2)
