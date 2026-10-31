#!/usr/bin/env python3
"""Fail-closed local assertions for the scoped Batch 9 Exact-18 release."""
from __future__ import annotations

import csv
import hashlib
import json
import subprocess
import zipfile
from collections import Counter
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
BASELINE = "88fa2b53774067faf740868bb8e168a04e47a8bf"
EXPECTED_WORKBOOK = "workbook/HO600-WIP_shortfall-search_batch8.xlsx"
EXPECTED_SHEETS = [
    "README_Status",
    "Candidate_Pool",
    "Basket_600",
    "Evidence",
    "Quota_Control",
    "Index_Calc",
    "Validation_Release",
]
CAP_PHRASE = "每日最高收費上限"
CHECKS_PASSED = 0

NEW_CONCEPTS = {
    "NEW-EDU-PILOT-BAC1SF": (380, 380, "2020-03-13", "2026-09-19", "https://www.pilot-pen.com.tw/news.php?seqno=124", "https://www.pilot-pen.com.tw/product.php?seqno=193"),
    "NEW-EDU-PILOT-SPF12": (48, 48, "2020-04-14", "2026-09-19", "https://www.pilot-pen.com.tw/news.php?seqno=127", "https://www.pilot-pen.com.tw/product.php?seqno=285"),
    "NEW-EDU-PILOT-SFL10SL": (40, 45, "2020-12-08", "2026-09-19", "https://www.pilot-pen.com.tw/news.php?seqno=135", "https://www.pilot-pen.com.tw/product.php?seqno=26"),
    "NEW-EDU-PILOT-SVS70FDM": (230, 230, "2020-10-27", "2026-09-19", "https://www.pilot-pen.com.tw/news.php?seqno=133", "https://www.pilot-pen.com.tw/product.php?seqno=313"),
    "NEW-EDU-PILOT-PSVS30KK": (100, 100, "2020-10-27", "2026-09-19", "https://www.pilot-pen.com.tw/news.php?seqno=133", "https://www.pilot-pen.com.tw/product.php?seqno=313"),
    "NEW-HOME-CHT-FTTX-16M3M": (302, 281, "2020-04-01", "2026-04-01", "https://www.cht.com.tw/home/cht/-/media/Web/PDF/messages/2020/X-Price-xDSL.pdf?la=zh-TW", "https://www.cht.com.tw/home/cht/-/media/web/pdf/messages/2026/broadband/1150401_fttx-internet-service_x-value_ch.pdf?sc_lang=zh-tw"),
    "NEW-HOME-CHT-FTTX-100M40M": (454, 425, "2020-04-01", "2026-04-01", "https://www.cht.com.tw/home/cht/-/media/Web/PDF/messages/2020/X-Price-xDSL.pdf?la=zh-TW", "https://www.cht.com.tw/home/cht/-/media/web/pdf/messages/2026/broadband/1150401_fttx-internet-service_x-value_ch.pdf?sc_lang=zh-tw"),
    "NEW-HOME-CHT-CONNECTION-FEE": (1500, 1500, "2020-04-01", "2026-04-01", "https://www.cht.com.tw/home/cht/-/media/Web/PDF/messages/2020/X-Price-xDSL.pdf?la=zh-TW", "https://www.cht.com.tw/home/cht/-/media/web/pdf/messages/2026/broadband/1150401_fttx-internet-service_x-value_ch.pdf?sc_lang=zh-tw"),
    "NEW-HOME-CHT-OUTSIDE-RELOCATION": (500, 500, "2020-04-01", "2026-04-01", "https://www.cht.com.tw/home/cht/-/media/Web/PDF/messages/2020/X-Price-xDSL.pdf?la=zh-TW", "https://www.cht.com.tw/home/cht/-/media/web/pdf/messages/2026/broadband/1150401_fttx-internet-service_x-value_ch.pdf?sc_lang=zh-tw"),
    "NEW-HOME-CHT-MOD-PLATFORM": (89, 89, "2020-06-03", "2026-09-19", "https://www.cht.com.tw/home/cht/-/media/web/pdf/messages/2020/bbmod10906031100402.pdf?sc_lang=zh-tw", "https://www.cht.com.tw/home/consumer/mod-ott/promo/43"),
    "NEW-SERVICE-FAMI-STORE-TO-STORE": (60, 60, "2020-06", "2026-09-19", "https://www.family.com.tw/Web_EnterPrise/page/NewsContent.aspx?ID=696", "https://famistore.famiport.com.tw/"),
    "NEW-LEISURE-APPLE-ONE-INDIVIDUAL": (315, 390, "2020-09-15", "2026-09-19", "https://www.apple.com/tw/newsroom/2020/09/apple-one-makes-enjoying-apple-subscription-services-easier-than-ever/", "https://www.apple.com/tw/apple-one/"),
    "NEW-LEISURE-APPLE-ONE-FAMILY": (395, 490, "2020-09-15", "2026-09-19", "https://www.apple.com/tw/newsroom/2020/09/apple-one-makes-enjoying-apple-subscription-services-easier-than-ever/", "https://www.apple.com/tw/apple-one/"),
    "NEW-HOME-AMWAY-SA8-LIQUID-1068": (370, 370, "2020 (2020-2產品總目錄; pp.46-47)", "2026-10-30", "https://pic.amwaynet.com.tw/PR/ishare/article/8098/2020-2-%E7%94%A2%E5%93%81%E7%B8%BD%E7%9B%AE%E9%8C%84A.pdf", "https://shop.amway.com.tw/products/1068"),
    "NEW-HOME-AMWAY-SA8-DELICATE-1069": (435, 435, "2020 (2020-2產品總目錄; pp.46-47)", "2026-10-30", "https://pic.amwaynet.com.tw/PR/ishare/article/8098/2020-2-%E7%94%A2%E5%93%81%E7%B8%BD%E7%9B%AE%E9%8C%84A.pdf", "https://shop.amway.com.tw/products/1069"),
    "NEW-HOME-AMWAY-SOFTENER-1070": (160, 160, "2020 (2020-2產品總目錄; pp.46-47)", "2026-10-30", "https://pic.amwaynet.com.tw/PR/ishare/article/8098/2020-2-%E7%94%A2%E5%93%81%E7%B8%BD%E7%9B%AE%E9%8C%84A.pdf", "https://shop.amway.com.tw/products/1070"),
}
HSR = {
    "LEG-EC-042": (40, "2020-02-01生效", 50, "2026"),
    "LEG-EC-041": (240, "2020-02-01生效", 350, "2026"),
}
PACKAGE_FAMILIES = {
    "NEW-EDU-PILOT-BAC1SF": "PILOT-BAC1SF-singleton",
    "NEW-EDU-PILOT-SPF12": "PILOT-SPF12-singleton",
    "NEW-EDU-PILOT-SFL10SL": "PILOT-SFL10SL-singleton",
    "NEW-EDU-PILOT-SVS70FDM": "PILOT-SVS-INSTAWRT",
    "NEW-EDU-PILOT-PSVS30KK": "PILOT-SVS-INSTAWRT",
    "NEW-HOME-CHT-FTTX-16M3M": "CHT-FTTX-SPEED-TIER",
    "NEW-HOME-CHT-FTTX-100M40M": "CHT-FTTX-SPEED-TIER",
    "NEW-HOME-CHT-CONNECTION-FEE": "CHT-FTTX-CHANGE-FEES",
    "NEW-HOME-CHT-OUTSIDE-RELOCATION": "CHT-FTTX-CHANGE-FEES",
    "NEW-HOME-CHT-MOD-PLATFORM": "CHT-MOD-PLATFORM-FEE",
    "NEW-SERVICE-FAMI-STORE-TO-STORE": "FAMILYMART-PARCEL-SERVICE",
    "NEW-LEISURE-APPLE-ONE-INDIVIDUAL": "APPLE-ONE-TIERS",
    "NEW-LEISURE-APPLE-ONE-FAMILY": "APPLE-ONE-TIERS",
    "NEW-HOME-AMWAY-SA8-LIQUID-1068": "SA8-LAUNDRY-DETERGENTS",
    "NEW-HOME-AMWAY-SA8-DELICATE-1069": "SA8-LAUNDRY-DETERGENTS",
    "NEW-HOME-AMWAY-SOFTENER-1070": "SA8-FABRIC-SOFTENER",
    "LEG-EC-041": "THSRC-P1-PARKING-TARIFF",
    "LEG-EC-042": "THSRC-P1-PARKING-TARIFF",
}


def check(name: str, condition: bool, detail: str = "") -> None:
    global CHECKS_PASSED
    if not condition:
        raise AssertionError(f"FAIL: {name}: {detail}")
    CHECKS_PASSED += 1


def csv_rows(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        reader = csv.DictReader(stream)
        return list(reader.fieldnames or []), list(reader)


def csv_matrix(path: Path) -> list[list[str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        return list(csv.reader(stream))


def baseline_csv(relative_path: str) -> list[dict[str, str]]:
    raw = subprocess.check_output(["git", "show", f"{BASELINE}:{relative_path}"], cwd=ROOT)
    text = raw.decode("utf-8-sig")
    return list(csv.DictReader(text.splitlines()))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    status = json.loads((ROOT / "canonical/status.json").read_text(encoding="utf-8"))
    workbook_path = ROOT / status["canonical_workbook"]
    pool_headers, pool = csv_rows(ROOT / "data/Candidate_Pool.csv")
    evidence_headers, evidence = csv_rows(ROOT / "data/Evidence.csv")
    quota_matrix = csv_matrix(ROOT / "data/Quota_Control.csv")
    quota_header_index = next(i for i, row in enumerate(quota_matrix) if row[:2] == ["Domain", "Subcategory"])
    quota_headers = quota_matrix[quota_header_index]
    quota = [dict(zip(quota_headers, row)) for row in quota_matrix[quota_header_index + 1:] if row and row[0]]
    release_headers, release = csv_rows(ROOT / "data/Validation_Release.csv")

    check("canonical batch", status["canonical_batch"] == 9, str(status["canonical_batch"]))
    check("status counts", (status["formal_exact_concepts"], status["remaining_concepts"], status["candidate_concepts"], status["evidence_records"]) == (199, 401, 434, 1600))
    actual_hash = sha256(workbook_path)
    check("canonical workbook hash", actual_hash == status["canonical_workbook_sha256"], actual_hash)
    manifest = (ROOT / "canonical/MANIFEST.sha256").read_text(encoding="utf-8").strip()
    check("manifest hash", manifest == f"{actual_hash}  {status['canonical_workbook']}", manifest)
    check("all seven workbook sheets", workbook_sheets(workbook_path) == EXPECTED_SHEETS)

    check("Candidate_Pool schema", len(pool_headers) == 24 and "2020 price" not in " ".join(pool_headers).lower())
    check("Evidence schema", len(evidence_headers) == 20)
    check("Candidate Pool row count", len(pool) == 434, str(len(pool)))
    check("Evidence row count", len(evidence) == 1600, str(len(evidence)))
    pool_by_id = {row["candidate_id"]: row for row in pool}
    evidence_by_id = {row["evidence_record_id"]: row for row in evidence}
    check("Candidate Pool ID uniqueness", len(pool_by_id) == len(pool))
    check("Evidence ID uniqueness", len(evidence_by_id) == len(evidence))
    check("16 new concept IDs", set(pool_by_id) - {row["candidate_id"] for row in baseline_csv("data/Candidate_Pool.csv")} == set(NEW_CONCEPTS))
    new_pool_rows = [pool_by_id[candidate_id] for candidate_id in NEW_CONCEPTS]
    check("new brand counts", Counter(row["brands"] for row in new_pool_rows) == Counter({"PILOT": 5, "中華電信": 5, "FamilyMart 全家": 1, "Apple": 2, "安麗 Amway Home": 3}))
    check("new corporate group counts", Counter(row["corporate_group"] for row in new_pool_rows) == Counter({"PILOT_CORPORATION_GROUP": 5, "CHT_GROUP": 5, "FAMILYMART_GROUP": 1, "APPLE_INC": 2, "ALTICOR_AMWAY_GROUP": 3}))
    check("new subcategory counts", Counter((row["ho600_domain"], row["ho600_subcategory"]) for row in new_pool_rows) == Counter({("育", "文具"): 5, ("住／家用", "網路／通訊固定服務"): 5, ("日常／個人", "其他日常服務"): 1, ("日常／個人", "個人數位／會員服務"): 2, ("住／家用", "清潔／洗衣用品"): 3}))
    check("new brand reference caps", all(count <= 8 for count in Counter(row["brands"] for row in new_pool_rows).values()))
    check("package product family mapping is complete", set(PACKAGE_FAMILIES) == set(NEW_CONCEPTS) | set(HSR))
    family_counts = Counter(PACKAGE_FAMILIES.values())
    check("package product family reference caps", all(count <= 2 for count in family_counts.values()), str(family_counts))
    check("THSRC family remains at two existing concepts", family_counts["THSRC-P1-PARKING-TARIFF"] == 2)

    prior_pool = baseline_csv("data/Candidate_Pool.csv")
    prior_evidence = baseline_csv("data/Evidence.csv")
    prior_exact_ids = {
        row["candidate_id"]
        for row in prior_pool
        if int(float(row["exact2020_quote_count"] or 0)) > 0
        and int(float(row["current2026_quote_count"] or 0)) > 0
    }
    check("all baseline Candidate Pool IDs retained", {r["candidate_id"] for r in prior_pool} <= set(pool_by_id))
    check("all 181 baseline Exact IDs retained", sum(1 for r in prior_pool if int(float(r["exact2020_quote_count"] or 0)) > 0 and int(float(r["current2026_quote_count"] or 0)) > 0) == 181)
    allowed_pool_fields = {"representative_item", "representative_spec", "migration_state", "exact2020_quote_count", "corporate_group", "selection_note", "source_count_2020", "evidence_link_status"}
    old_pool_by_id = {r["candidate_id"]: r for r in prior_pool}
    for candidate_id, old in old_pool_by_id.items():
        current = pool_by_id[candidate_id]
        if candidate_id in HSR:
            changed = {key for key in old if old[key] != current[key]}
            check("scoped HSR Candidate Pool changes", changed <= allowed_pool_fields, candidate_id + ": " + ",".join(sorted(changed)))
        else:
            check("baseline Candidate Pool row retained " + candidate_id, old == current)
    old_evidence_by_id = {r["evidence_record_id"]: r for r in prior_evidence}
    check("all baseline Evidence IDs retained", set(old_evidence_by_id) <= set(evidence_by_id))
    cap_note_ids = {"MIG-00443", "EV-00559"}
    for record_id, old in old_evidence_by_id.items():
        current = evidence_by_id[record_id]
        if record_id in cap_note_ids:
            changed = {key for key in old if old[key] != current[key]}
            check("scoped cap-note change " + record_id, changed == {"semantic_note"})
        else:
            check("baseline Evidence row retained " + record_id, old == current)

    check("new Evidence record IDs", {key for key in evidence_by_id if key.startswith("HO600-B9-")} == {f"HO600-B9-{index:05d}" for index in range(1568, 1602)})
    for candidate_id, (p2020, p2026, d2020, d2026, url2020, url2026) in NEW_CONCEPTS.items():
        row = pool_by_id[candidate_id]
        check("Exact classification " + candidate_id, row["migration_state"] == "PREQUALIFIED-EXACT2020" and row["exact2020_quote_count"] == "1" and row["current2026_quote_count"] == "1")
        linked = [record for record in evidence if record["candidate_id"] == candidate_id]
        baseline = [record for record in linked if record["observation_role"] == "BASELINE_2020" and record["observation_year"] == "2020"]
        current = [record for record in linked if record["observation_role"] == "CURRENT_2026" and record["observation_year"] == "2026"]
        check("paired evidence rows " + candidate_id, len(baseline) == len(current) == 1)
        b, c = baseline[0], current[0]
        check("2020 source and price " + candidate_id, float(b["observed_price"]) == p2020 and b["source_url"] == url2020 and b["observation_date"] == d2020)
        check("2026 source and price " + candidate_id, float(c["observed_price"]) == p2026 and c["source_url"] == url2026 and c["observation_date"] == d2026)
        check("normal-price admission " + candidate_id, b["decision_status"] == c["decision_status"] == "ADMIT-NORMAL-REFERENCE")
        check("positive price evidence " + candidate_id, float(b["observed_price"]) > 0 and float(c["observed_price"]) > 0)

    for candidate_id, (price2020, date2020, price2026, _) in HSR.items():
        row = pool_by_id[candidate_id]
        linked = [record for record in evidence if record["candidate_id"] == candidate_id]
        historical = [record for record in linked if record["observation_role"] == "BASELINE_2020" and record["observation_year"] == "2020"]
        current = [record for record in linked if record["observation_year"] == "2026"]
        check("approved HSR pair " + candidate_id, len(historical) == 1 and float(historical[0]["observed_price"]) == price2020 and historical[0]["observation_date"] == date2020 and historical[0]["source_url"] == "https://www.thsrc.com.tw/ArticleContent/46ee4b1e-771d-46b5-a20c-3a547323d687" and historical[0]["decision_status"] == "ADMIT-NORMAL-REFERENCE")
        check("no duplicate HSR current quote " + candidate_id, len(current) == 2 and all(float(record["observed_price"]) == price2026 for record in current))
        check("HSR Exact status " + candidate_id, row["migration_state"] == "PREQUALIFIED-EXACT2020" and row["exact2020_quote_count"] == "1")
    daily = pool_by_id["LEG-EC-041"]
    daily_rows = [record for record in evidence if record["candidate_id"] == "LEG-EC-041"]
    check("350 daily cap label", "最高收費上限" in daily["representative_spec"] and all(CAP_PHRASE in record["semantic_note"] for record in daily_rows))
    check("Dudu房 cap remains 8/8", sum(1 for row in pool if row["brands"] == "嘟嘟房") == 8)

    package_ids = set(NEW_CONCEPTS) | set(HSR)
    package_2020 = [row for row in evidence if row["candidate_id"] in package_ids and row["observation_role"] == "BASELINE_2020" and row["observation_year"] == "2020"]
    package_source_uses = Counter(row["source_url"] for row in package_2020)
    prior_exact_source_uses = Counter(row["source_url"] for row in prior_evidence if row["candidate_id"] in prior_exact_ids and row["observation_year"] == "2020")
    check("release package has 18 2020 observations", len(package_2020) == 18, str(len(package_2020)))
    check("release package has 10 unique 2020 sources", len(package_source_uses) == 10, str(len(package_source_uses)))
    check("release package source maximum is four", max(package_source_uses.values()) == 4, str(package_source_uses))
    check("release package sources stay within six-use cap", all(count <= 6 for count in package_source_uses.values()))
    check("package 2020 sources unused by main Exact-181", all(prior_exact_source_uses[url] == 0 for url in package_source_uses))

    exact_rows = [row for row in pool if int(float(row["exact2020_quote_count"] or 0)) > 0 and int(float(row["current2026_quote_count"] or 0)) > 0]
    counts = Counter(row["brands"] for row in exact_rows)
    ranked = sorted(counts.values(), reverse=True)
    check("legacy top-five concentration", sum(ranked[:5]) == 56)
    check("legacy top-ten concentration", sum(ranked[:10]) == 85)
    check("no price columns in Candidate_Pool", not any("price" in name.lower() or "change" in name.lower() for name in pool_headers))

    quota_by_category = {
        (row["Domain"], row["Subcategory"]): row
        for row in quota
        if row.get("Domain")
        and row.get("Subcategory")
        and row["Domain"] != "Domain"
        and row["Subcategory"] != "Original target"
        and not row["Subcategory"].isdigit()
    }
    exact_by_category = Counter((row["ho600_domain"], row["ho600_subcategory"]) for row in exact_rows)
    for key, row in quota_by_category.items():
        if key[1] == "Original target":
            continue
        exact = exact_by_category[key]
        target = int(float(row["Legacy-preserving target"]))
        check("quota reconciliation " + key[1], int(float(row["Prequalified Exact concepts"])) == exact and int(float(row["New exact needed"])) == max(0, target - exact))

    domain_summary_header = next(i for i, row in enumerate(quota_matrix) if row[:2] == ["Domain", "Original target"])
    domain_summary_fields = quota_matrix[domain_summary_header]
    domain_summary = [
        dict(zip(domain_summary_fields, row))
        for row in quota_matrix[domain_summary_header + 1 :]
        if row and row[0] and row[0] != "Domain"
    ]
    exact_by_domain = Counter(row["ho600_domain"] for row in exact_rows)
    check("seven-domain quota summary", len(domain_summary) == 7, str(len(domain_summary)))
    for row in domain_summary:
        domain = row["Domain"]
        exact = exact_by_domain[domain]
        target = int(float(row["Legacy-preserving target"]))
        check("domain summary exact " + domain, int(float(row["Exact after Batch 9"])) == exact)
        check("domain summary remaining " + domain, int(float(row["New exact needed"])) == max(0, target - exact))
        check("domain summary final share " + domain, abs(float(row["Final share"]) - target / 600) < 1e-12)
        check("domain summary interpretation " + domain, row["Interpretation"] == "Legacy overage retained; remaining allocation rebalanced proportionally.")
    check("domain summary total", sum(int(float(row["Exact after Batch 9"])) for row in domain_summary) == 199)

    release_by_check = {row["Check"]: row for row in release}
    check("all Validation_Release checks pass", bool(release) and all(row["Status"] == "PASS" for row in release))
    check("Validation_Release Exact count", release_by_check["Exact-2020 economic concepts"]["Result"] == "199")
    check("Validation_Release Candidate Pool count", release_by_check["Candidate concepts now"]["Result"] == "434")
    basket = csv_matrix(ROOT / "data/Basket_600.csv")
    basket_text = " ".join(value for row in basket for value in row)
    check("Basket remains NOT SEALED and zero selected", "NOT SEALED" in basket_text and basket[3][0] == "NOT SEALED" and basket[3][1] == "0")
    index = csv_matrix(ROOT / "data/Index_Calc.csv")
    index_text = " ".join(value for row in index for value in row)
    check("Index remains LOCKED", "LOCKED" in index_text)
    check("README canonical status", "199 / 600" in (ROOT / "README.md").read_text(encoding="utf-8") and "434" in (ROOT / "README.md").read_text(encoding="utf-8"))
    check("validation receipt includes release Handoff", (ROOT / "handoffs/2026-10-31-ho600-batch09-exact18-release-acceptance.md").is_file())
    print(f"BATCH09_EXACT18_LOCAL_ASSERTIONS=PASS ({CHECKS_PASSED} assertions)")
    return 0


def workbook_sheets(path: Path) -> list[str]:
    ns = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
    with zipfile.ZipFile(path) as archive:
        root = ET.fromstring(archive.read("xl/workbook.xml"))
    return [sheet.attrib["name"] for sheet in root.findall("m:sheets/m:sheet", ns)]


if __name__ == "__main__":
    raise SystemExit(main())
