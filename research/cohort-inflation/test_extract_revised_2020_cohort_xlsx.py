#!/usr/bin/env python3
"""Offline synthetic tests, NOT a real cohort weight extraction."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

from artifact_tool import Workbook, SpreadsheetFile

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("cohort_extract", HERE / "extract_revised_2020_cohort_xlsx.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

LABELS = [
    "1.食品及非酒精飲料", "2.菸酒及檳榔", "3.衣著鞋襪及服飾用品",
    "4.住宅服務水電瓦斯及其他燃料", "5.家具設備及家務維護",
    "6.醫療保健", "7.交通", "8.通訊", "9.休閒與文化",
    "10.教育", "11.餐廳及旅館", "12.什項消費"
]

class CohortExtractionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.raw = self.root / "NAT20-AGE-original.xls"
        self.raw.write_bytes(bytes.fromhex("D0CF11E0A1B11AE1") + b"FIXTURE_ONLY")
        self.xlsx = self.root / "converted.xlsx"
        self.mapping = self.root / "reviewed.json"
        workbook = Workbook.create()
        sh = workbook.worksheets.add("Original Sheet")
        sh.get_range("A1:B14").values = [["概念", "每戶年支出"]] + [
            [LABELS[i], 100 + i] for i in range(12)
        ] + [["消費支出總計", sum(range(100,112))]]
        SpreadsheetFile.export_xlsx(workbook).save(str(self.xlsx))
        self.config = dict(
            source_id="NAT20-AGE",
            source_url="https://ws.dgbas.gov.tw/001/Upload/463/relfile/11531/235640/159-164.xls",
            year=2020, cohort_code="AGE_HEAD_65PLUS_PROXY",
            sheet="Original Sheet",label_col="A",amount_col="B",total_label_col="A",
            category_rows={f"{i+1:02d}":i+2 for i in range(12)},total_row=14,
            raw_sha256=mod.sha(self.raw),converted_sha256=mod.sha(self.xlsx),
            reviewed=True)
        self.write_config()

    def tearDown(self):
        self.temp.cleanup()

    def write_config(self):
        self.mapping.write_text(json.dumps(self.config,ensure_ascii=False),encoding="utf-8")

    def run_extract(self):
        return mod.extract(self.xlsx,self.mapping,self.raw,self.root / "output")

    def test_valid_research_proxy(self):
        receipt=self.run_extract()
        self.assertEqual(receipt["category_count"],12)
        self.assertEqual(receipt["source_total"],"1266")
        self.assertFalse(receipt["publication_authorized"])
        import csv
        with (self.root/"output/NAT20-AGE-AGE_HEAD_65PLUS_PROXY-weights-unreleased.csv").open(newline="") as f:
            records=list(csv.DictReader(f))
        self.assertEqual(len(records),12)
        self.assertEqual(records[0]["category_code"],"01")

    def test_reject_unreviewed(self):
        self.config["reviewed"]=False
        self.write_config()
        with self.assertRaisesRegex(ValueError,"reviewed"):
            self.run_extract()

    def test_reject_sha_mismatch(self):
        self.config["raw_sha256"]="a"*64
        self.write_config()
        with self.assertRaisesRegex(ValueError,"SHA mismatch"):
            self.run_extract()

    def test_reject_not_proxy(self):
        self.config["cohort_code"]="RETIRE"
        self.write_config()
        with self.assertRaisesRegex(ValueError,"PROXY"):
            self.run_extract()

    def test_reject_duplicate_row_map(self):
        self.config["category_rows"]["12"]=2
        self.write_config()
        with self.assertRaisesRegex(ValueError,"distinct"):
            self.run_extract()

    def test_reject_label_swap(self):
        self.config["category_rows"]["01"]=3
        self.config["category_rows"]["02"]=2
        self.write_config()
        with self.assertRaisesRegex(ValueError,"label mismatch"):
            self.run_extract()

    def test_never_overwrites_previous_evidence(self):
        self.run_extract()
        with self.assertRaises(FileExistsError):
            self.run_extract()

if __name__=="__main__":
    unittest.main()
