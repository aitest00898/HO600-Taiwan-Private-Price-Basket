#!/usr/bin/env python3
"""Pure-stdlib synthetic fixtures for government CPI *capture* (not numeric release)."""
import csv
import importlib.util
import io
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location("cpi",ROOT/"fetch_taipei_cpi_basic_official.py")
cpi=importlib.util.module_from_spec(sp)
sp.loader.exec_module(cpi)

MONTH="TPE-CPI-BASIC-MONTH"
YEAR="TPE-CPI-BASIC-YEAR"

def fixture(source=MONTH, year="109/01", include2026=True, header=None, encoding="utf-8-sig"):
    if header is None:
        header=["縣市別代碼","年月別" if source==MONTH else "年別","基本分類",
                "原始值[統計數值]","年增率[%]"]
    rows=[header]
    for i, cls in enumerate(["總指數","食物類","居住類","醫療保健","教育","交通"]):
        rows.append(["63000",year,cls,str(100+i),"1.1"])
    if include2026:
        period="115/08" if source==MONTH else "115"
        rows.extend([["63000",period,cls,"120.0","2.0"] for cls in ["總指數","居住類"]])
    ss=io.StringIO()
    csv.writer(ss).writerows(rows)
    return ss.getvalue().encode(encoding)

class CPIAuthenticityChecks(unittest.TestCase):
    def test_valid_month(self):
        profile=cpi.decode_table(fixture(),MONTH)
        self.assertEqual(profile["period_2020_rows"],6)
        self.assertEqual(profile["period_2026_rows"],2)
        self.assertFalse(profile["2020_to_2026_rebased"])
        self.assertFalse(profile["published_inflation_rate"])

    def test_annual_no2026_legitimate(self):
        profile=cpi.decode_table(fixture(source=YEAR,year="109",include2026=False),YEAR)
        self.assertEqual(profile["period_2020_rows"],6)
        self.assertFalse(profile["has_2026_data"])

    def test_compact_monthly_roc(self):
        profile=cpi.decode_table(fixture(year="10901"),MONTH)
        self.assertEqual(profile["period_2020_rows"],6)

    def test_compact_monthly_gregorian(self):
        profile=cpi.decode_table(fixture(year="202001"),MONTH)
        self.assertEqual(profile["period_2020_rows"],6)

    def test_new_official_stat_period_header_month(self):
        raw=fixture(header=["縣市別代碼","統計期","基本分類","原始值[統計數值]","年增率[%]"])
        profile=cpi.decode_table(raw,MONTH)
        self.assertEqual(profile["date_field"],"統計期")
        self.assertEqual(profile["period_2020_rows"],6)

    def test_new_official_stat_period_header_year(self):
        raw=fixture(source=YEAR,year="109",include2026=False,
                    header=["縣市別代碼","統計期","基本分類","原始值[統計數值]","年增率[%]"])
        profile=cpi.decode_table(raw,YEAR)
        self.assertEqual(profile["date_field"],"統計期")
        self.assertEqual(profile["period_2020_rows"],6)

    def test_reject_two_competing_period_headers(self):
        raw=fixture(header=["年月別","統計期","基本分類","原始值[統計數值]","年增率[%]"])
        with self.assertRaisesRegex(ValueError,"ambiguous"):
            cpi.decode_table(raw,MONTH)

    def test_cp950(self):
        profile=cpi.decode_table(fixture(encoding="cp950"),MONTH)
        self.assertEqual(profile["file_encoding"],"cp950")

    def test_reject_no2020(self):
        with self.assertRaisesRegex(ValueError,"2020/ROC109"):
            cpi.decode_table(fixture(year="110/01",include2026=True),MONTH)

    def test_reject_html(self):
        with self.assertRaisesRegex(ValueError,"HTML"):
            cpi.decode_table(b"<html>error</html>",MONTH)

    def test_reject_json(self):
        with self.assertRaisesRegex(ValueError,"HTML"):
            cpi.decode_table(b'{"error":"session expired"}',MONTH)

    def test_reject_duplicate_period_category(self):
        with self.assertRaisesRegex(ValueError,"Duplicate"):
            cpi.decode_table(fixture(year="109/01")+b"63000,109/01,"+
              "總指數,101.0,1.0\n".encode("utf-8"),MONTH)

    def test_reject_missing_class_column(self):
        hdr=["縣市別代碼","年月別","未分類","原始值[統計數值]","年增率[%]"]
        with self.assertRaisesRegex(ValueError,"Missing or ambiguous"):
            cpi.decode_table(fixture(header=hdr),MONTH)

    def test_reject_missing_period_column(self):
        hdr=["縣市別代碼","自編年號","基本分類","原始值[統計數值]","年增率[%]"]
        with self.assertRaisesRegex(ValueError,"Missing or ambiguous"):
            cpi.decode_table(fixture(header=hdr),MONTH)

    def test_reject_empty(self):
        with self.assertRaisesRegex(ValueError,"Empty"):
            cpi.decode_table(b"",MONTH)

    def test_official_origins_allowlist(self):
        self.assertEqual(set(cpi.URLS),{MONTH,YEAR})
        self.assertTrue(all(x.startswith("https://tsis.dbas.gov.taipei/") for x in cpi.URLS.values()))
        self.assertEqual(cpi.OFFICIAL_HOSTS,{"data.taipei","tsis.dbas.gov.taipei"})
        self.assertEqual(set(cpi.LANDING_URLS),{MONTH,YEAR})

if __name__=="__main__":
    unittest.main()
