#!/usr/bin/env python3
"""Verify source-bound Taipei 2020 child expenditure and entertainment sensitivity.
Only stored official 2020 Taipei 58-column household-age CSV + original partial
CPI contribution rows. Research audit, NOT a complete inflation calculation.
Does not modify files. Python standard library only.
"""
from __future__ import annotations

import csv
from decimal import Decimal
import hashlib
from pathlib import Path

ROOT=Path(__file__).resolve().parent
AGE_SOURCE=ROOT/"source-archive/tpe-2020-age-head/TPE_AGE_2012_2023_official_raw.csv"
CONTRIB=ROOT/"results/tpe-cpi-20261018/age-head-partial-contributions.csv"
CHILD_AUDIT=ROOT/"results/tpe-cpi-20261018/tpe-2020-recovered-child-expenditure-audit.csv"
SENSITIVITY=ROOT/"results/tpe-cpi-20261018/division09-mapping-hold-sensitivity.csv"
PINNED_SOURCE_SHA="d75682e408db19704c9c6dae726be3c54ab57560487697acc2d7a478ce801434"
AGE_GROUPS=("未滿30歲","30～34歲","35～39歲","40～44歲","45～54歲","55～64歲","65歲及以上")
PERIODS=("A_2020_JAN_SEP_TO_2026_JAN_SEP","B_2020_FULL_YEAR_TO_2025_FULL_YEAR")

def rows(path,encoding):
    with path.open("r",encoding=encoding,newline="") as f:
        reader=csv.DictReader(f)
        if not reader.fieldnames or len(reader.fieldnames)!=len(set(reader.fieldnames)):
            raise ValueError(f"Duplicate or missing headings: {path}")
        data=list(reader)
    if any(None in r for r in data):
        raise ValueError(f"Nonrectangular CSV: {path}")
    return data

def d(x):
    return Decimal(str(x).strip())

def approx(a,b,tol=Decimal("0.000011")):
    if abs(d(a)-d(b))>tol:
        raise ValueError(f"Independent numeric disagreement: {a} vs {b}")

def verify():
    actual_sha=hashlib.sha256(AGE_SOURCE.read_bytes()).hexdigest()
    if actual_sha!=PINNED_SOURCE_SHA:
        raise ValueError("Official source raw SHA-256 mismatch")
    src=rows(AGE_SOURCE,"cp950")
    selected=[r for r in src if r["年別"]=="109年" and r["經濟戶長年齡組"]!="總平均"]
    if len(selected)!=7 or set(x["經濟戶長年齡組"] for x in selected)!=set(AGE_GROUPS):
        raise ValueError("Wrong age-head source 2020 grain")
    original=rows(CONTRIB,"utf-8-sig")
    child=rows(CHILD_AUDIT,"utf-8-sig")
    sensitivity=rows(SENSITIVITY,"utf-8-sig")
    if len(original)!=42 or len(child)!=7 or len(sensitivity)!=14:
        raise ValueError("Input/output sample grain mismatch")
    by_age={x["household_head_age"]:x for x in child}
    by_case={(x["age"],x["comparison"]):x for x in sensitivity}
    if set(by_age)!=set(AGE_GROUPS) or len(by_case)!=14:
        raise ValueError("Duplicate or missing age/case")
    for age in AGE_GROUPS:
        v=next(r for r in selected if r["經濟戶長年齡組"]==age)
        c=by_age[age]
        key={
          "housing_total_nt":"4.住宅服務水電瓦斯及其他燃料[NT]",
          "rent_and_water_nt":"[1]房地租及水費[NT]",
          "electric_and_fuel_nt":"[2]電費及燃料[NT]",
          "transport_total_nt":"7.交通[NT]",
          "vehicle_purchase_nt":"[1]個人交通工具之購置[NT]",
          "vehicle_maintenance_nt":"[2]個人交通設備使用管理及保養費[NT]",
          "transport_services_nt":"[3]乘交通設備及其他交通服務[NT]",
          "vehicle_insurance_nt":"[4]汽機車保險費[NT]",
          "leisure_total_nt":"9.休閒與文化[NT]",
          "package_tour_nt":"[1]套裝旅遊[不含自助旅遊][NT]",
          "entertainment_culture_services_nt":"[2]娛樂消遣及文化服務[NT]",
          "books_stationery_nt":"[3]書報雜誌文具[NT]",
          "recreation_equipment_nt":"[4]教育消遣康樂器材及其附屬品[NT]"
        }
        for target,source in key.items():
            if d(c[target])!=d(v[source]):
                raise ValueError(f"Child source cell mismatch {age} {target}")
        for parent,children,delta in [
            ("housing_total_nt",("rent_and_water_nt","electric_and_fuel_nt"),"housing_rounding_delta_nt"),
            ("transport_total_nt",("vehicle_purchase_nt","vehicle_maintenance_nt","transport_services_nt","vehicle_insurance_nt"),"transport_rounding_delta_nt"),
            ("leisure_total_nt",("package_tour_nt","entertainment_culture_services_nt","books_stationery_nt","recreation_equipment_nt"),"leisure_rounding_delta_nt"),
        ]:
            diff=sum((d(c[x]) for x in children),Decimal(0))-d(c[parent])
            if diff!=d(c[delta]) or abs(diff)>1:
                raise ValueError(f"Child rounding discrepancy in {age}: {parent}")
        approx(c["package_tour_share_of_leisure_pct"],
               d(c["package_tour_nt"])*100/d(c["leisure_total_nt"]))
        approx(c["entertainment_services_share_of_leisure_pct"],
               d(c["entertainment_culture_services_nt"])*100/d(c["leisure_total_nt"]))
        for period in PERIODS:
            items=[x for x in original if x["household_head_age_group"]==age and x["comparison"]==period]
            indexed={int(x["expense_division"]):x for x in items}
            if len(items)!=3 or set(indexed)!={3,9,10}:
                raise ValueError(f"Expected only original three divisions {age} {period}")
            row=by_case[(age,period)]
            frac=lambda col:sum((d(indexed[i]["weight_share_2020"]) for i in col),Decimal(0))*100
            contrib=lambda col:sum((d(indexed[i]["contribution_percentage_points"]) for i in col),Decimal(0))
            three=contrib((3,9,10))
            approx(row["three_division_coverage_pct"],frac((3,9,10)))
            approx(row["exclude_division09_coverage_pct"],frac((3,10)))
            approx(row["original_three_class_partial_pp"],three)
            approx(row["exclude_division09_partial_pp"],contrib((3,10)))
            approx(row["09_price_mapping_dependent_pp"],contrib((9,)))
            approx(row["09_share_of_original_partial_pct"],100*contrib((9,))/three)
            if row["release_status"]!="NO_FULL_COHORT_RATE":
                raise ValueError("Unexpected release status")
    return {"status":"PASS_SOURCE_BOUND_CHILD_ARITHMETIC_AND_09_SENSITIVITY_NOT_RATE",
            "original_household_raw_sha256":actual_sha,
            "age_groups_verified":len(selected),
            "child_parent_reconciliations":len(selected)*3,
            "partial_scenarios_verified":len(sensitivity),
            "CPI_09_alignment_accepted":False,
            "complete_cohort_rate_authorized":False}

if __name__=="__main__":
    import json
    print(json.dumps(verify(),ensure_ascii=False,indent=2))
