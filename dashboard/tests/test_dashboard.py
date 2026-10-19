"""HO600 static IUI V0 release guards. Read-only, no network, no Actions."""
from __future__ import annotations

from decimal import Decimal
import json
from pathlib import Path
import re
import shutil
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]
SNAP = ROOT / "snapshot.json"
JS_SNAP = ROOT / "snapshot.js"
APP = ROOT / "app.js"
HTML = ROOT / "index.html"
CSS = ROOT / "styles.css"


class DashboardV0Acceptance(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads(SNAP.read_text(encoding="utf-8"))
        js = JS_SNAP.read_text(encoding="utf-8")
        prefix = "window.HO600_SNAPSHOT = "
        assert prefix in js
        cls.embedded = json.loads(js.split(prefix, 1)[1].strip().removesuffix(";"))
        cls.app = APP.read_text(encoding="utf-8")
        cls.html = HTML.read_text(encoding="utf-8")
        cls.css = CSS.read_text(encoding="utf-8")

    def test_json_and_file_snapshot_match_exactly(self):
        self.assertEqual(self.embedded, self.data)

    def test_canonical_main_invariants(self):
        c = self.data["canonical"]
        self.assertEqual(c["target"], 600)
        self.assertEqual((c["accepted"], c["remaining"]), (181, 419))
        self.assertEqual((c["candidates"], c["evidence"]), (418, 1566))
        self.assertFalse(c["basketSealed"])
        self.assertEqual(c["indexStatus"], "LOCKED")
        self.assertEqual(c["batch"], 8)

    def test_source_branch_identity(self):
        d = self.data["identity"]
        self.assertEqual(d["authoritativeBranch"], "main")
        self.assertEqual(d["researchBranch"], "research/batch-09")
        self.assertEqual(len(d["canonicalCommit"]), 40)
        self.assertEqual(len(d["researchCommit"]), 40)
        self.assertNotEqual(d["canonicalCommit"], d["researchCommit"])

    def test_quota_seven_domains_balanced(self):
        q = self.data["canonical"]["quota"]
        self.assertEqual(len(q), 7)
        self.assertEqual(sum(x["accepted"] for x in q), 181)
        self.assertEqual(sum(x["needed"] for x in q), 419)
        self.assertEqual(sum(x["target"] for x in q), 600)
        self.assertTrue(all(x["accepted"] + x["needed"] == x["target"] for x in q))

    def test_batch9_research_not_canonical(self):
        checkpoints = self.data["research"]["checkpoints"]
        self.assertEqual([x["id"] for x in checkpoints], ["C01", "C02", "C03", "C04"])
        self.assertEqual([x["accepted"] for x in checkpoints], [20,20,20,0])
        self.assertEqual((checkpoints[-1]["provisional"], checkpoints[-1]["hold"]), (1,1))
        self.assertEqual([x["status"] for x in checkpoints], ["PASS","PASS","PASS","WIP"])

    def test_original_age_spending_reconciles(self):
        t = self.data["cohort"]
        self.assertEqual((t["groupCount"], t["weightCells"]), (7, 84))
        self.assertEqual((t["officialAgeCsvPdfParentChecks"], t["publishedTotals"]), ("96/96","8/8"))
        self.assertEqual(len(t["age"]), 7)
        for age in t["age"]:
            self.assertLessEqual(abs(age["annual12Sum"]-age["annualSpend"]),2)
            housing = Decimal(str(age["housing"])) / Decimal(str(age["annual12Sum"])) * 100
            health = Decimal(str(age["health"])) / Decimal(str(age["annual12Sum"])) * 100
            self.assertLess(abs(housing + health - Decimal(str(age["housingHealthShare"]))),Decimal("0.00015"))

    def test_cpi_periods_source_completeness(self):
        t = self.data["cohort"]
        self.assertEqual((t["cpiMonthlyRows"],t["cpiAnnualRows"]), (16560,1344))
        self.assertEqual((t["cpiClassCount"],t["cpiThrough"]),(48,"2026-09"))
        self.assertIn("2020 年 1–9 月",t["periods"]["A"])
        self.assertIn("2025 全年",t["periods"]["B"])

    def test_crosswalk_is_conservative_and_exact(self):
        t = self.data["cohort"]
        self.assertEqual([x["code"] for x in t["crosswalk"]],[f"{i:02d}" for i in range(1,13)])
        self.assertEqual(t["crosswalkSummary"],{"mapped":2,"provisional":1,"split":8,"unmapped":1})
        self.assertEqual([x["code"] for x in t["crosswalk"] if x["status"]=="PROVISIONAL"],["09"])
        self.assertTrue(all(x["status"]!="MAPPED" for x in t["crosswalk"] if x["code"] in {"01","04","06"}))

    def test_no_full_cohort_rate_can_be_released(self):
        t=self.data["cohort"]
        self.assertEqual(t["fullCohortRatesReleased"],0)
        self.assertEqual(t["nationalWeightStatus"],"HOLD")
        self.assertEqual(t["nationalWorkerRetireProxies"],"0/2")
        for age in t["age"]:
            for p in ["A","B"]:
                v=age["periods"][p]
                self.assertLess(v["coverage"],95)
                self.assertLessEqual(v["strictCoverage"],v["coverage"])
                self.assertAlmostEqual(v["partial"]-v["strictPartial"],v["assumption09"],places=4)
                self.assertFalse(v["released"])

    def test_verified_source_provenance_links(self):
        sources=self.data["sources"]
        self.assertEqual(len(sources),7)
        for s in sources:
            self.assertRegex(s["blobSha"],r"^[0-9a-f]{40}$")
            self.assertIn("https://github.com/",s["link"])
            self.assertIn(s["ref"],("main","research/batch-09"))

    def test_html_four_valid_pages_with_mobile_layout(self):
        for tab in ("overview","basket","cohorts","evidence"):
            self.assertIn(f'data-tab="{tab}"',self.html)
        self.assertIn('aria-label="HO600 導覽"',self.html)
        self.assertIn('name="viewport"',self.html)
        self.assertIn("@media(max-width:760px)",self.css)
        self.assertIn("snapshot.js",self.html)

    def test_controls_are_real_and_export_current_selection(self):
        for control in ("[data-period]","[data-mode]","ageSelect","statusSelect","exportCSV","data-tab"):
            self.assertIn(control,self.app)
        self.assertIn("const k=strict?\"strictCoverage\":\"coverage\"",self.app)
        self.assertIn("window.addEventListener(\"hashchange\"",self.app)
        self.assertIn("text/csv;charset=utf-8",self.app)

    def test_no_live_network_write_or_token_requirement(self):
        self.assertNotIn("fetch(",self.app)
        self.assertNotIn("XMLHttpRequest",self.app)
        self.assertNotIn("localStorage",self.app)
        self.assertNotIn("Authorization",self.app)
        self.assertNotIn("github_token",self.app.lower())
        self.assertNotIn("https://cdn.",self.html)
        self.assertFalse(any(x for x in ("<form","input type=\"password\"") if x in self.html.lower()))

    def test_smoke_mode_is_explicit_opt_in(self):
        self.assertIn('get("smoke") === "1"', self.html)
        self.assertIn("./tests/browser-smoke.js", self.html)
        self.assertNotIn('<script defer src="./tests/browser-smoke.js">', self.html)

    def test_mobile_navigation_tap_outside_closes(self):
        self.assertIn('id="mobileBackdrop"', self.html)
        self.assertIn('getElementById("mobileBackdrop").addEventListener("click",closeNav)',self.app)
        self.assertIn('.workspace.menu-open .mobile-backdrop',self.css)
        self.assertNotIn(".topbar::after",self.css)

    def test_browser_smoke_has_export_period_mapping_checks(self):
        smoke=(ROOT/"tests"/"browser-smoke.js").read_text(encoding="utf-8")
        for term in (
            'data-mode="strict"',
            'data-mode="provisional"',
            'data-period="B"',
            '"45～54歲"',
            'HOLD_NOT_A_FULL_RATE',
            'exportedBlob',
            'scrollWidth',
            'mobileBackdrop',
            'HO600_BROWSER_SMOKE_RESULT',
        ):
            self.assertIn(term,smoke)
        self.assertNotIn("fetch(",smoke)
        self.assertNotIn("localStorage",smoke)

    def test_workflow_pause_preserved(self):
        self.assertEqual(self.data["controls"]["githubActions"],"PAUSED_BY_USER")
        self.assertEqual(self.data["controls"]["indexRelease"],"LOCKED")

    @unittest.skipUnless(shutil.which("node"),"Node.js unavailable; validate JS in Safari")
    def test_js_syntax(self):
        for path in (APP,JS_SNAP):
            proc=subprocess.run(["node","--check",str(path)],capture_output=True,text=True,timeout=15)
            self.assertEqual(proc.returncode,0,proc.stderr)


if __name__=="__main__":
    unittest.main()
