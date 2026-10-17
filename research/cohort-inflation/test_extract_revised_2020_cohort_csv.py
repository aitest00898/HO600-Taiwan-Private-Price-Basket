#!/usr/bin/env python3
"""Independent synthetic unit tests for Numbers CSV fallback; NO actual cohort data."""
import csv
import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("cohort_csv", HERE / "extract_revised_2020_cohort_csv.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
LABELS = [
    "食品及非酒精飲料", "菸酒及檳榔", "衣著鞋襪及服飾用品",
    "住宅服務水電瓦斯及其他燃料", "家具設備及家務維護",
    "醫療保健", "交通", "通訊", "休閒與文化",
    "教育", "餐廳及旅館", "什項消費",
]

class NumberCSVTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.raw = self.root / "official-fixture.xls"
        self.raw.write_bytes(bytes.fromhex("D0CF11E0A1B11AE1") + b"THIS_IS_ONLY_A_SYNTHETIC_FIXTURE")
        self.csv = self.root / "numbers-export.csv"
        self.map = self.root / "mapping.json"
        self.rows = [["科目", "每戶消費支出"]] + [
            [LABELS[i], str(100+i)] for i in range(12)
        ] + [["消費支出總計", "1266"]]
        self.write_csv()
        self.conf = {
            "source_id":"NAT20-AGE", "source_url":
            "https://ws.dgbas.gov.tw/001/Upload/463/relfile/11531/235640/159-164.xls",
            "reference_year":2020, "cohort_code":"AGE_HEAD_65PLUS_PROXY",
            "source_sheet":"SYNTHETIC SHEET (no historical source)",
            "numbers_export_confirmed":True, "manual_reviewed":True,
            "original_sha256":module.checksum(self.raw),
            "csv_sha256":module.checksum(self.csv),
            "label_column":1, "amount_column":2, "total_label_column":1,
            "category_rows":{f"{i:02d}":i+1 for i in range(1,13)},
            "total_row":14, "total_tolerance_twd":0
        }
        self.write_conf()

    def write_csv(self):
        with self.csv.open("w", encoding="utf-8", newline="") as f:
            csv.writer(f).writerows(self.rows)

    def write_conf(self):
        self.map.write_text(json.dumps(self.conf, ensure_ascii=False), encoding="utf-8")

    def call(self):
        return module.run(self.raw, self.csv, self.map, self.root / "output")

    def test_synthetic_success(self):
        a = self.call()
        self.assertEqual(a["category_count"], 12)
        self.assertEqual(a["source_total"], "1266")
        self.assertFalse(a["released"])
        p = self.root / "output/NAT20-AGE-AGE_HEAD_65PLUS_PROXY-unreleased.csv"
        with p.open(encoding="utf-8", newline="") as f:
            r=list(csv.DictReader(f))
        self.assertEqual(len(r), 12)
        self.assertEqual(r[0]["category_code"], "01")
        self.assertEqual(r[0]["evidence_status"], "PROXY_RESEARCH_NOT_RELEASED")

    def test_reject_unreviewed(self):
        self.conf["manual_reviewed"]=False
        self.write_conf()
        with self.assertRaisesRegex(ValueError, "manual review"):
            self.call()

    def test_reject_unqualified_cohort(self):
        self.conf["cohort_code"]="RETIRE"
        self.write_conf()
        with self.assertRaisesRegex(ValueError, "PROXY"):
            self.call()

    def test_reject_wrong_source_url(self):
        self.conf["source_url"]="https://example.com/source.xls"
        self.write_conf()
        with self.assertRaisesRegex(ValueError, "exact URL"):
            self.call()

    def test_reject_original_hash_error(self):
        self.conf["original_sha256"]="0"*64
        self.write_conf()
        with self.assertRaisesRegex(ValueError, "SHA-256 mismatch"):
            self.call()

    def test_reject_fake_html_source(self):
        self.raw.write_bytes(b"<html>error</html>")
        self.conf["original_sha256"]=module.checksum(self.raw)
        self.write_conf()
        with self.assertRaisesRegex(ValueError, "OLE2"):
            self.call()

    def test_reject_duplicate_category_row(self):
        self.conf["category_rows"]["12"]=2
        self.write_conf()
        with self.assertRaisesRegex(ValueError, "distinct"):
            self.call()

    def test_reject_category_label_swap(self):
        self.conf["category_rows"]["01"]=3
        self.conf["category_rows"]["02"]=2
        self.write_conf()
        with self.assertRaisesRegex(ValueError, "label mismatch"):
            self.call()

    def test_reject_nonmatching_total(self):
        self.rows[-1][1]="1000"
        self.write_csv()
        self.conf["csv_sha256"]=module.checksum(self.csv)
        self.write_conf()
        with self.assertRaisesRegex(ValueError, "sum mismatch"):
            self.call()

    def test_dont_overwrite_receipts(self):
        self.call()
        with self.assertRaises(FileExistsError):
            self.call()

    def test_reject_blind_weight_tolerance(self):
        self.conf["total_tolerance_twd"]=100
        self.write_conf()
        with self.assertRaisesRegex(ValueError, "12 TWD"):
            self.call()

if __name__=="__main__":
    unittest.main()
