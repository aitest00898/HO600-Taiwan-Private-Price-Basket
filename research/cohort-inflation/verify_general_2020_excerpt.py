#!/usr/bin/env python3
"""Local CSV checksum audit; provisional 2020 national all-household indexed text only."""
import csv
from decimal import Decimal
from pathlib import Path
path = Path(__file__).with_name("general-household-2020-indexed-v0.csv")
with path.open(encoding="utf-8-sig", newline="") as fh:
    rows=list(csv.DictReader(fh))
assert len(rows)==12
assert sorted(x["category_code"] for x in rows)==[f"{i:02d}" for i in range(1,13)]
assert all(x["reference_year"]=="2020" and x["cohort"]=="ALL_HOUSEHOLDS_GENERAL" for x in rows)
assert all(x["evidence_status"].endswith("RAW_BYTES_UNVERIFIED") for x in rows)
assert all(x["data_limit"].startswith("NOT WORK OR RETIRE") for x in rows)
vals=[int(x["expenditure_twd_per_household_year"]) for x in rows]
total=sum(vals)
assert total==815100 and all(int(x["annual_consumption_total_twd"])==total for x in rows)
weights=[Decimal(str(x["weight_pct_calculated"])) for x in rows]
for x,w in zip(rows,weights):
    exact=Decimal(int(x["expenditure_twd_per_household_year"]))*100/Decimal(total)
    assert abs(w-exact)<=Decimal("0.00000051")
assert abs(sum(weights)-Decimal(100))<=Decimal("0.000006")
by_code={x["category_code"]:int(x["expenditure_twd_per_household_year"]) for x in rows}
assert by_code["04"]==198145 and by_code["06"]==139010
assert by_code["04"]+by_code["06"]==337155
print("PASS_INTERIM_CHECKSUM_ONLY: 12 categories, total 815100, housing+health 337155, not cohort weights")
