# 2020 Taipei age-head budget detail audit and CPI division 09 mapping sensitivity

**Date:** 2026-10-18. **Research classification:** `TAIPEI_CITY_HOUSEHOLD_HEAD_AGE_ONLY`. This is not national WORK/RETIRE and **NOT an inflation rate**.

## New finding from already authenticated official city CSV

The `TPE_AGE_2012_2023_official_raw.csv` source archived at
`source-archive/tpe-2020-age-head/` is more detailed than the 12 parent consumption divisions already accepted: its 58 columns contain officially labelled **child expenditure fields** for parent 04 (housing), 07 (transport) and 09 (leisure & culture), in all seven 2020 household-head age groups.

The prior source verification is **96/96 parent division PDF-to-CSV**, 8/8 aggregate totals, raw CSV SHA
`d75682e408db19704c9c6dae726be3c54ab57560487697acc2d7a478ce801434`. **The child expenditure numbers here were independently read from that same raw CSV, not each independently matched to PDF cells.** Do not misrepresent them as new 96/96 PDF evidence.

Reconciled results: parent and child totals differ by at most **NT$1 per age group** for each of the three parent divisions. Source rounding differences are **retained** and no missing values were filled. Full seven-age-group numeric output:
[`tpe-2020-recovered-child-expenditure-audit.csv`](./results/tpe-cpi-20261018/tpe-2020-recovered-child-expenditure-audit.csv).

### Explicit 2020 hierarchy usable for future classification QA

| Parent | 2020 official child columns in age-head CSV | Difference | Price-alignment consequence |
| --- | --- | --- | --- |
| 04 Housing/energy | `[1]房地租及水費`, `[2]電費及燃料` | ≤NT$1 | The first **combines rent with water** whereas CPI `房租` and `水電燃氣` are split differently. The second mixes fuel/electric while the CPI `水電燃氣` also includes water. **No clean independent class relative yet**. |
| 07 Transport | purchase of personal transport vehicles, personal equipment use/maintenance, transport services, vehicle insurance | ≤NT$1 | More spending-grain evidence, but CPI `交通及通訊設備` mixes transport with communication equipment; maintenance and fuel categories also differ. **Requires further price-scope matching**. |
| 09 Leisure/culture | package travel, cultural/entertainment service, books/stationery, recreation/education equipment | ≤NT$1 | The parent contains 4 substantively different spending classes; using the **single** CPI `(二)娛樂費用` for all four is a **critical publishing-time assumption requiring official item-scope validation**. |

**Age-head 65+** has NT$21,942 package travel within NT$44,443 leisure spending, **49.37%**. Age-head **45–54** spends NT$35,137 package travel within NT$75,023 leisure, **46.84%**. Across all seven age groups, package travel is **40.25%–50.01%** of parent 09.

The 65+ housing parent NT$303,048 contains NT$288,133 in combined rent/water and NT$14,914 electricity/fuel (child total NT$303,047; 1-NT rounding difference). Most of the elderly household-head exposure is in rent/water, but an exact independent `房租` price relative cannot simply be assigned to combined rent+water.

### Materiality of provisional mapping 09

The previously published **three-mapped-division** result for 2020 Jan–Sep versus 2026 Jan–Sep (A) and 2020 full year versus 2025 full year (B) remains a *historic, clearly partial* calculation. To quantify model risk, independently recompute the original contribution from divisions 03, 09 and 10, **then exclude 09 entirely**, without changing raw CPI observations, household expenditure weights or prior outputs. This does not assert the existing map is definitively wrong; it assesses **unresolved correspondence risk**.

[`division09-mapping-hold-sensitivity.csv`](./results/tpe-cpi-20261018/division09-mapping-hold-sensitivity.csv) records all **14 age × period scenarios**:

| Age-head group | A original 3-class partial (pp) | A exclude 09 (pp) | Exclude 09 covered share |
| --- | ---: | ---: | ---: |
| Under 30 | +2.345266 | +0.085517 | 4.12% |
| 30–34 | +2.110724 | +0.072203 | 4.02% |
| 35–39 | +2.358091 | +0.190824 | 5.60% |
| 40–44 | +2.505499 | +0.365651 | 8.58% |
| 45–54 | +2.713018 | +0.385167 | 8.95% |
| 55–64 | +2.676450 | +0.153731 | 5.16% |
| 65+ | +1.901797 | **+0.044728** | **2.54%** |

`(二)娛樂費用` carries **85.41%–97.65% of the A partial three-class contribution** and **89.11%–98.97% of the B partial contribution**, even though the household leisure parent includes package travel, equipment and print goods. Therefore, the original three-class contribution alone cannot substantiate differences in historical inflation exposure between age groups. The exclusion version also is **NOT** a full cohort rate.

## Next verifiable official-source tasks, ranked by value

1. **Confirm CPI entertainment item definitions against 2020 survey child fields** and list exactly which of its four child purposes the official `(二)娛樂費用` index covers. The amount of child **tour package** spending (40%–50% of parent 09) makes this the most material current model risk. Until confirmed, mark 09 as **`MAPPED_PROVISIONAL_SCOPE_REVIEW`** in interpretation; the existing historical crosswalk/results must retain their original provenance rather than silently rewriting them.
2. **Housing**: seek official 2020 **age-head** rent vs water item-level expenses. The existing source only supplies rent+water, and 2024+ publications use a different classification schema. Never misapply a later year's housing split to 2020.
3. **Food, restaurants/hotels, and medical**: seek contemporaneous official household item data at the same geographic and age-head grain. The 48-class CPI file alone cannot manufacture 2020 demographic within-division expenditure shares.
4. **Additional independent source**: look for survey item-code microdata/public use files, if lawfully and publicly available, or official same-age itemized tables. Record public rights/availability; do not contact agencies without explicit user request.
5. Keep **2020 Jan–Sep to 2026 Jan–Sep** and **2020 full-year to 2025 full-year** comparisons distinct. Use no false <95% coverage promotion.

## Release and repository boundaries

`TPE_CHILD_EXPENSES=SOURCE_RETRIEVED_ARITHMETIC_RECONCILED`;
`09_ENTERTAINMENT_MAP=PROVISIONAL_SCOPE_REVIEW`;
`TPE_2020_2026_COHORT_FULL_CPI=HOLD`;
`NATIONAL_WGT01=HOLD`;
`NATIONAL_WORK_RETIRE=0/2`;
`CANONICAL_HO600=181/600_BASKET_NOT_SEALED_INDEX_LOCKED`.

No Actions, main writes, canonical workbook changes or category-weight retroactive overwrites. The two new CSV files are **supplemental research audit/sensitivity artifacts**, not replaced source or corrected published CPI rates.
