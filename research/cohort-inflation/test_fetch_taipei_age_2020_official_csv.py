#!/usr/bin/env python3
"""Pure stdlib offline fixtures. No real government rows or network calls."""
from __future__ import annotations
import csv
import importlib.util
import io
import unittest
from pathlib import Path

root=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location("tpe_source",root/"fetch_taipei_age_2020_official_csv.py")
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)

HEADERS=["年別","經濟戶長年齡組","家庭戶數","每戶就業人數","[三]消費支出[NT]",
         "1.食品及非酒精飲料[NT]","2.菸酒及檳榔[NT]","3.衣著鞋襪及服飾用品[NT]",
         "4.住宅服務水電瓦斯及其他燃料[NT]","5.家具設備及家務維護[NT]",
         "6.醫療保健[NT]","7.交通[NT]","8.通訊[NT]","9.休閒與文化[NT]",
         "10.教育[NT]","11.餐廳及旅館[NT]","12.什項消費[NT]",
         "可支配所得[NT]","消費支出[NT]","儲蓄[NT]","所得總額[NT]",
         "所得收入[NT]","每戶人數","每戶成年人數","所得收入人數"]

def fixture(year="109年", age="65歲以上", encoding="utf-8-sig", header=HEADERS):
    rows=[header,[year,age]+["100"]*(len(header)-2)]
    buf=io.StringIO()
    csv.writer(buf).writerows(rows)
    return buf.getvalue().encode(encoding)

class ParserTests(unittest.TestCase):
    def test_valid_2020(self):
        x=mod.parse_csv(fixture())
        self.assertEqual(x["year2020_rows"],1)
        self.assertEqual(x["geographic_scope"],"TAIPEI_ONLY")
        self.assertFalse(x["national_WGT01_satisfied"])
        self.assertFalse(x["cohort_proxy_weights_generated"])

    def test_year_2020_and_109(self):
        self.assertTrue(mod.year_2020("2020"))
        self.assertTrue(mod.year_2020("109年"))
        self.assertFalse(mod.year_2020("2019"))
        self.assertFalse(mod.year_2020("110年"))

    def test_cp950_valid(self):
        x=mod.parse_csv(fixture(encoding="cp950"))
        self.assertEqual(x["encoding"],"cp950")

    def test_no_2020(self):
        with self.assertRaisesRegex(ValueError,"2020 / ROC109"):
            mod.parse_csv(fixture(year="110年"))

    def test_reject_html(self):
        with self.assertRaisesRegex(ValueError,"HTML/JSON"):
            mod.parse_csv(b"<html><body>unavailable</body></html>")

    def test_reject_json(self):
        with self.assertRaisesRegex(ValueError,"HTML/JSON"):
            mod.parse_csv(b'{"status": "error"}')

    def test_reject_missing_age_column(self):
        hs=HEADERS.copy()
        hs[1]="未知分組"
        with self.assertRaisesRegex(ValueError,"age-of-head"):
            mod.parse_csv(fixture(header=hs))

    def test_reject_duplicate_headings(self):
        hs=HEADERS.copy()
        hs[2]=hs[3]
        with self.assertRaisesRegex(ValueError,"header"):
            mod.parse_csv(fixture(header=hs))

    def test_reject_wrong_small_summary(self):
        with self.assertRaisesRegex(ValueError,"header"):
            mod.parse_csv(fixture(header=["年別","經濟戶長年齡組","消費支出","醫療保健"]))

    def test_reject_empty(self):
        with self.assertRaisesRegex(ValueError,"Empty"):
            mod.parse_csv(b"")

    def test_allowlisted_urls(self):
        self.assertEqual(len(mod.CANDIDATES),2)
        self.assertTrue(all(url.startswith("https://data.taipei/") for url in mod.CANDIDATES))
        self.assertTrue(all("63e4d839-ef65-46a8-b4d1-1bbfeeca5516" in url for url in mod.CANDIDATES))

if __name__=="__main__":
    unittest.main()
