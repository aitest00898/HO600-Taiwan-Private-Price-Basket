"""Regression checks for the 2026-10-31 Batch 9 Exact-admission preaudit."""
import csv
import hashlib
import json
import unittest
import xml.etree.ElementTree as ET
import zipfile
from collections import Counter
from pathlib import Path

BASE = Path(__file__).resolve().parent
REPO = BASE.parents[1]


def read_csv(name):
    with (BASE / name).open(encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


class ExactAdmissionReviewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.matrix = read_csv("exact-admission-review-matrix-2026-10-31.csv")
        cls.candidates = read_csv("exact-admission-candidate-list-2026-10-31.csv")
        cls.triage = read_csv("exact-admission-needs-evidence-triage-2026-10-31.csv")
        cls.receipts = read_csv("exact-admission-source-receipts-2026-10-31.csv")
        cls.crosswalk = read_csv("batch09-brand-corporate-group-crosswalk.csv")
        cls.preaudit = read_csv("exact-admission-preaudit-2026-10-30.csv")
        cls.summary = json.loads((BASE / "exact-admission-review-summary-2026-10-31.json").read_text())

    def test_review_matrix_has_expected_scope_and_unique_ids(self):
        self.assertEqual(len(self.matrix), 22)
        ids = [r["research_id"] for r in self.matrix]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(Counter(r["reviewed_status"] for r in self.matrix), {
            "EXACT_READY_CANDIDATE": 18,
            "RESEARCH_ONLY": 1,
            "NEEDS_EVIDENCE": 3,
        })

    def test_candidate_list_matches_all_exact_ready_rows(self):
        ready = {r["research_id"] for r in self.matrix if r["reviewed_status"] == "EXACT_READY_CANDIDATE"}
        actual = [r["research_id"] for r in self.candidates]
        self.assertEqual(len(actual), 18)
        self.assertEqual(set(actual), ready)
        self.assertEqual(len(actual), len(set(actual)))
        self.assertEqual(Counter(r["candidate_type"] for r in self.candidates), {
            "NEW_CONCEPT": 16,
            "EXISTING_POOL_2020_BACKFILL": 2,
        })

    def test_each_candidate_has_two_positive_prices_and_source_receipts(self):
        receipt_pairs = {(r["requested_url"], r["sha256"]) for r in self.receipts if r["http_status"] == "200"}
        for row in self.candidates:
            for year in ("2020", "2026"):
                self.assertGreater(float(row[f"price_{year}"]), 0, row["research_id"])
                self.assertIn("https://", row[f"source_{year}_url"], row["research_id"])
                self.assertEqual(len(row[f"source_{year}_sha256"]), 64, row["research_id"])
                self.assertIn((row[f"source_{year}_url"], row[f"source_{year}_sha256"]), receipt_pairs, row["research_id"])

    def test_all_successful_source_captures_match_sha256(self):
        successful = [r for r in self.receipts if r["http_status"] == "200"]
        self.assertEqual(len(self.receipts), 45)
        self.assertEqual(len(successful), 40)
        for row in successful:
            path = REPO / row["capture_path"]
            self.assertTrue(path.is_file(), row["capture_path"])
            self.assertEqual(hashlib.sha256(path.read_bytes()).hexdigest(), row["sha256"], row["capture_path"])

    def test_selected_aaa_slice_has_no_automatic_promotions(self):
        selected = [r for r in self.preaudit if r["preaudit_status"] == "RESEARCH_ONLY"
                    and r["comparability"] == "A"
                    and r["evidence_grade_2020"] == "A"
                    and r["evidence_grade_2026"] == "A"]
        self.assertEqual(len(selected), 17)
        by_id = {r["research_id"]: r for r in self.matrix}
        self.assertEqual(sum(by_id[r["research_id"]]["reviewed_status"] == "EXACT_READY_CANDIDATE" for r in selected), 16)
        self.assertEqual(by_id["B09-C03-009"]["reviewed_status"], "RESEARCH_ONLY")
        self.assertIn("voucher", by_id["B09-C03-009"]["row_decision_and_reason"].lower())

    def test_semantics_are_brand_specific(self):
        by_id = {r["research_id"]: r for r in self.candidates}
        for rid in ("B09-C01-001", "B09-C01-002", "B09-C01-003", "B09-C01-004", "B09-C01-005"):
            self.assertIn("PILOT", by_id[rid]["normal_price_semantics_2020"])
            self.assertIn("PILOT", by_id[rid]["normal_price_semantics_2026"])
            self.assertNotIn("中華電信", by_id[rid]["normal_price_semantics_2020"])
        self.assertIn("89元", by_id["B09-C01-010"]["normal_price_semantics_2020"])
        self.assertIn("MOD", by_id["B09-C01-010"]["normal_price_semantics_2026"])
        self.assertIn("會員", by_id["B09-C07-018"]["normal_price_semantics_2020"])

    def test_exact_ready_group_attribution_is_verified(self):
        exact_ids = {r["research_id"] for r in self.matrix if r["reviewed_status"] == "EXACT_READY_CANDIDATE"}
        self.assertEqual(len(exact_ids), 18)
        self.assertTrue(all(r["corporate_group_status"] == "VERIFIED_CONSOLIDATED_GROUP" for r in self.matrix if r["research_id"] in exact_ids))
        mapping = {r["brand_or_merchant"]: r for r in self.crosswalk}
        self.assertEqual(mapping["PILOT"]["corporate_group_id"], "PILOT_CORPORATION_GROUP")
        self.assertEqual(mapping["Apple"]["corporate_group_id"], "APPLE_INC")
        self.assertEqual(mapping["安麗 Amway Home"]["corporate_group_id"], "ALTICOR_AMWAY_GROUP")

    def test_thsrc_existing_pool_backfills_keep_day_cap_semantics(self):
        by_id = {r["research_id"]: r for r in self.candidates}
        self.assertEqual(by_id["B09-C08-016"]["candidate_pool_target"], "LEG-EC-042")
        self.assertEqual(by_id["B09-C08-017"]["candidate_pool_target"], "LEG-EC-041")
        self.assertEqual(by_id["B09-C08-016"]["price_2020"], "40")
        self.assertEqual(by_id["B09-C08-016"]["price_2026"], "50")
        self.assertEqual(by_id["B09-C08-017"]["price_2020"], "240")
        self.assertEqual(by_id["B09-C08-017"]["price_2026"], "350")
        self.assertIn("最高收費", by_id["B09-C08-017"]["normal_price_semantics_2026"])
        self.assertIn("不是一般每日實付或平均值", by_id["B09-C08-017"]["normal_price_semantics_2026"])
        matrix = {r["research_id"]: r for r in self.matrix}
        for rid in ("B09-C08-016", "B09-C08-017"):
            self.assertEqual(matrix[rid]["candidate_pool_delta_if_admitted"], "0")
            self.assertIn("不增加", matrix[rid]["brand_or_subcategory_count_after"])
        self.assertIn("8/8", by_id["B09-C08-016"]["concentration_and_source_caps"])
        self.assertIn("owner approved on 2026-10-31", by_id["B09-C08-016"]["formal_status_note"].lower())
        self.assertIn("cap remains 8/8", by_id["B09-C08-016"]["formal_status_note"].lower())
        self.assertIn("BRAND_CAP", matrix["B09-C08-016"]["preflight_state"])

    def test_hsr_pool_concepts_each_have_one_unfilled_2020_price_pair(self):
        workbook = REPO / "workbook/HO600-WIP_shortfall-search_batch8.xlsx"
        ns = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
              "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships"}
        with zipfile.ZipFile(workbook) as z:
            wb = ET.fromstring(z.read("xl/workbook.xml"))
            rel = ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))
            targets = {x.attrib["Id"]: x.attrib["Target"] for x in rel}
            shared = []
            if "xl/sharedStrings.xml" in z.namelist():
                root = ET.fromstring(z.read("xl/sharedStrings.xml"))
                shared = ["".join(t.text or "" for t in si.findall(".//m:t", ns)) for si in root.findall("m:si", ns)]

            def worksheet(name):
                sh = next(x for x in wb.findall(".//m:sheet", ns) if x.attrib["name"] == name)
                target = targets[sh.attrib["{" + ns["r"] + "}id"]].lstrip("/")
                target = target if target.startswith("xl/") else "xl/" + target
                out = []
                for row in ET.fromstring(z.read(target)).findall(".//m:sheetData/m:row", ns):
                    record = {}
                    for cell in row:
                        ref = cell.attrib.get("r", "")
                        col = "".join(ch for ch in ref if ch.isalpha())
                        value = cell.find("m:v", ns)
                        value = value.text if value is not None else ""
                        if cell.attrib.get("t") == "s" and value:
                            value = shared[int(value)]
                        record[col] = value
                    out.append(record)
                return out

            pool = worksheet("Candidate_Pool")[1:]
            evidence = worksheet("Evidence")[1:]
        pool_ids = [r.get("A", "") for r in pool]
        self.assertEqual(pool_ids.count("LEG-EC-041"), 1)
        self.assertEqual(pool_ids.count("LEG-EC-042"), 1)
        for candidate in ("LEG-EC-041", "LEG-EC-042"):
            observations = [r for r in evidence if r.get("B") == candidate]
            self.assertEqual([r.get("F") for r in observations].count("2020"), 0)
            current = [r for r in observations if r.get("F") == "2026"]
            self.assertEqual(len(current), 2)  # Same current observation in migrated and evidence rows.
            self.assertEqual(len({(r.get("G"), r.get("H"), r.get("M")) for r in current}), 1)

    def test_needs_evidence_triage_keeps_three_followups_unadmitted(self):
        self.assertEqual(len(self.triage), 30)
        self.assertEqual(Counter(r["followup_status"] for r in self.triage), {
            "FOLLOWED_UP_RETAIN_NEEDS_EVIDENCE": 3,
            "NO_TARGETED_RETRY_NO_VERIFIED_INCREMENTAL_GAP": 27,
        })
        self.assertTrue(all(r["formal_exact_delta"] == "0" for r in self.triage))
        followup_ids = {r["research_id"] for r in self.triage if r["followup_status"].startswith("FOLLOWED_UP")}
        self.assertEqual(followup_ids, {"B09-C07-010", "B09-C08-014", "B09-C08-015"})

    def test_formal_candidate_pool_dedup_matches_backfill_and_new_concept_types(self):
        workbook = REPO / "workbook/HO600-WIP_shortfall-search_batch8.xlsx"
        ns = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main",
              "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships"}
        with zipfile.ZipFile(workbook) as z:
            wb = ET.fromstring(z.read("xl/workbook.xml"))
            rel = ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))
            targets = {x.attrib["Id"]: x.attrib["Target"] for x in rel}
            sheet = next(x for x in wb.findall(".//m:sheet", ns) if x.attrib["name"] == "Candidate_Pool")
            target = targets[sheet.attrib["{" + ns["r"] + "}id"]].lstrip("/")
            target = target if target.startswith("xl/") else "xl/" + target
            shared = []
            if "xl/sharedStrings.xml" in z.namelist():
                root = ET.fromstring(z.read("xl/sharedStrings.xml"))
                shared = ["".join(t.text or "" for t in si.findall(".//m:t", ns)) for si in root.findall("m:si", ns)]
            ids = []
            for row in ET.fromstring(z.read(target)).findall(".//m:sheetData/m:row", ns):
                if row.attrib.get("r") == "1":
                    continue
                cell = next((c for c in row if c.attrib.get("r", "").startswith("A")), None)
                if cell is None:
                    continue
                value = cell.find("m:v", ns)
                text = value.text if value is not None else ""
                if cell.attrib.get("t") == "s" and text:
                    text = shared[int(text)]
                ids.append(text)
        ids = [x for x in ids if x]
        self.assertEqual(len(ids), 418)
        self.assertEqual(len(ids), len(set(ids)))
        existing = {r["research_id"]: r["proposed_candidate_id"] for r in self.candidates if r["candidate_type"] == "EXISTING_POOL_2020_BACKFILL"}
        self.assertTrue(set(existing.values()) <= set(ids))
        new_ids = {r["proposed_candidate_id"] for r in self.candidates if r["candidate_type"] == "NEW_CONCEPT"}
        self.assertFalse(new_ids & set(ids))

    def test_scoped_owner_approval_updates_local_projection_without_canonical_change(self):
        self.assertEqual(self.summary["formal_exact_current"], "181/600")
        self.assertEqual(self.summary["formal_exact_delta_if_all_candidates_admitted"], 18)
        self.assertEqual(self.summary["formal_exact_projected_if_all_admitted"], 199)
        self.assertEqual(self.summary["formal_exact_projected_if_hsr_backfills_blocked_by_brand_freeze"], 197)
        self.assertEqual(self.summary["scoped_owner_approved_existing_pool_backfills"], 2)
        final = self.summary["final_formal_adjudication"]
        self.assertEqual(final["decision_counts"]["READY_UNDER_EXISTING_POLICY"], 18)
        self.assertEqual(final["decision_counts"]["REQUIRES_OWNER_POLICY_DECISION"], 0)
        self.assertEqual(final["basket_selected"], 0)
        self.assertIn("no new Candidate Pool concepts", final["owner_approval"])
        self.assertFalse(self.summary["canonical_workbook_modified"])
        self.assertEqual(self.summary["basket"], "NOT SEALED")
        self.assertEqual(self.summary["index"], "LOCKED")


if __name__ == "__main__":
    unittest.main()
