import csv
import hashlib
import io
import unittest
from audit_taipei_cpi_period_coverage import audit, parse_month


def fixture(drop=None, val="101.2", duplicate=False):
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(["縣市別代碼", "統計期", "基本分類", "原始值[統計數值]", "年增率[%]"])
    for y in (2020, 2026):
        for m in range(1, 10):
            for cat in ("食物類", "居住類"):
                if (y,m,cat)==drop:
                    continue
                w.writerow(["63000", f"{y}/{m:02d}", cat, val, "2.0"])
    if duplicate:
        w.writerow(["63000", "2020/01", "食物類", val, "2.0"])
    raw=buf.getvalue().encode("utf-8-sig")
    receipt={"sha256":hashlib.sha256(raw).hexdigest(),"raw_bytes":len(raw),
             "final_url":"https://data.taipei/api/frontstage/tpeod/dataset/resource.download?rid=sample",
             "http_code":200,"source_id":"TPE-CPI-BASIC-MONTH"}
    return raw,receipt


class Tests(unittest.TestCase):
    def test_roc_month(self):
        self.assertEqual(parse_month("民國109年9月"),(2020,9))
    def test_gregorian_compact(self):
        self.assertEqual(parse_month("202609"),(2026,9))
    def test_complete_grid(self):
        raw,r=fixture()
        r["final_url"]="https://tsis.dbas.gov.taipei/statis/webMain.aspx?outkind=3"
        x=audit(raw,r)
        self.assertEqual(x["full_pair_class_count"],2)
        self.assertFalse(x["2020_to_2026_inflation_computed"])
    def test_incomplete_grid(self):
        raw,r=fixture(drop=(2026,9,"居住類"))
        x=audit(raw,r)
        self.assertEqual(x["full_pair_class_count"],1)
        self.assertEqual(x["missing_by_class"]["居住類"]["2026"],[9])
    def test_reject_wrong_checksum(self):
        raw,r=fixture();r["sha256"]="f"*64
        with self.assertRaisesRegex(ValueError,"SHA"):
            audit(raw,r)
    def test_reject_untrusted_host(self):
        raw,r=fixture();r["final_url"]="https://example.com/nope"
        with self.assertRaisesRegex(ValueError,"HTTPS"):
            audit(raw,r)
    def test_reject_duplicate(self):
        raw,r=fixture(duplicate=True)
        with self.assertRaisesRegex(ValueError,"Duplicate"):
            audit(raw,r)
    def test_reject_zero(self):
        raw,r=fixture(val="0")
        with self.assertRaisesRegex(ValueError,"Nonpositive"):
            audit(raw,r)
    def test_reject_ambiguous_year(self):
        with self.assertRaisesRegex(ValueError,"Unrecognized"):
            parse_month("110-year-month-5")

if __name__ == "__main__": unittest.main()
