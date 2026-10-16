# HO600 Cohort Inflation — Revised 2020 Baseline Source Audit

**Date:** 2026-10-16 (Asia/Taipei)  
**Branch:** `research/batch-09`; study stage `SOURCE_DISCOVERY_COMPLETE / RAW_WEIGHT_IMPORT_BLOCKED`  
**Canonical:** unchanged Batch 8, 181/600 Exact research candidates, Basket NOT SEALED, Index LOCKED.

## Evidence found and decision

The **2020 (ROC 109) National Household Income and Expenditure Survey** detailed tables are directly linked from the official Taiwan statistical site:

| Artifact | Official page | Direct official format | Source QA |
| --- | --- | --- | --- |
| Occupation of economic household head, average per-household income & expenditure, Table 4 | https://www.stat.gov.tw/News_Content.aspx?n=3908&s=210989 | https://ws.dgbas.gov.tw/001/Upload/463/relfile/11530/235896/65.xls | Link confirmed, raw bytes not obtained |
| Age group of economic household head, detailed average household income & expenditure (unprinted result table) | https://www.stat.gov.tw/News_Content.aspx?n=3911&s=211017 | https://ws.dgbas.gov.tw/001/Upload/463/relfile/11531/235640/159-164.xls | Link confirmed, raw bytes not obtained |
| Age group ODF fallback | https://www.stat.gov.tw/News_Content.aspx?n=3911&s=211017 | https://ws.dgbas.gov.tw/001/Upload/463/relfile/11531/235640/159-164.ods | Same evidence provider, raw bytes not obtained |
| 2025 (ROC 114) survey | https://www.stat.gov.tw/News.aspx?n=2697&sms=10980 | not yet linked to a verified detailed cohort matrix | Release 2026-08-14 verified; raw age×occupation×category weights unknown |
| Age-specific 12 consumption divisions, Taipei only (2012–2023) | https://data.gov.tw/dataset/133235 | https://data.taipei/api/dataset/26c3817c-0713-4657-8cd8-aa842eb59f97/resource/63e4d839-ef65-46a8-b4d1-1bbfeeca5516/download | Link verified, raw bytes not obtained; not national |

**Critical revision:** The official 2020 annual and unprinted-results pages state that **on 2026-02-13** relevant tables were replaced due to corrections including original imputed owner-occupied housing, housing services, water/electricity/fuel, dwelling rent and water charges, consumer expenditure, savings and income totals. Earlier archival PDFs or local spreadsheets may be superseded. Reconstruct 2020 weights **only** from the revised version, and pin original bytes/SHA once captured.

**Source retrieval is not data extraction.** Landing-page and direct-file links have been independently identified, but all raw table downloads attempted in this session failed (502/cache miss/timeouts/other network-layer errors). This is not evidence of no data or bad official links. Do not invent any consumption share or numerical cohort inflation rate.

## Classifying the population

1. `WORK` = working employee households by household working-status definition. An **occupation of economic head** table is at most a proxy; it cannot show all employed adults, mixed households, part-time retirees, or all occupation×age cross-tabs.
2. `RETIRE` = households whose principal economic activity has ceased and whose living spending principally depends on pensions/transfers/assets. An **economic head 65+ age** table is a second proxy, **not a measurement** of retired-only households.
3. `OFFICIAL_HIGH_AGE_CPI` = separate benchmark for households where **all members are >=65**. This is not `RETIRE` or the same as age of economic head.
4. The 2020 occupation and age tables are *different marginal partitions*. They cannot be multiplied, stacked or automatically joined into an age×employment×spending matrix. If no matching joint cell exists, publish separate `WORK_OCCUPATION_PROXY` and `RETIRE_AGE_PROXY` sensitivity results only, with provenance and no claim that these are actual retired households.

## Expenditure crosswalk delivered

- `dgbas-12division-crosswalk-v0.csv`: all **50** HO600 subcategories mapped to candidate official 12-division expenditure purposes; **40** map tentatively to a single division and **10** require per-item splits.
- `dgbas-12division-coverage-gaps.csv`: all 12 official consumption divisions carried forward, with absent/partial private-price coverage explicitly recorded.
- `official-weight-source-register-2026-10-16.csv`: 9 source/alternative-format records with URL, revision, retrieval and intended scope.
- No amount, index, inferred purchase frequency or expense weight is filled in these files.

Important exclusions: category `02` alcohol/tobacco has no original HO600 allocation; `04` housing/utilities and `06` medical are absent as a complete private-price series. Other divisions contain substantial gaps. Private subset cannot be normalized to 100% of whole-household spending.

## Time-base reconciliation

1. **Baseline weights:** validated 2020 calendar-year household expenditure by all 12 divisions, captured after the 2026 revision. Frozen 2020 monetary shares by documented population and geography; avoid silently substituting later-year composition.
2. **2025 expenditure:** use separately as current-composition sensitivity after verified published 2025 values are obtained, not as if they were 2020 consumer weights.
3. **2026 prices:** original HO600 2026 Exact SKU prices are mostly specific 2026 observation dates, not 2026 annual averages. Distinguish `2020 point/list price→2026 point/list price` from an `annual-average CPI 2020→2026 YTD`. 2026 year is not complete on 2026-10-16. Compare official indices on matched month/window definitions.
4. **Housing concept:** imputed owner-occupied rental *consumption* versus cash housing costs, and mortgage principal versus mortgage interest, require separate definitions. Never double count rent plus imputed rental service for the same household. Mortgage principal is a financial transaction, not current CPI consumption expenditure.
5. **Missing or unobservable shares:** retain explicit null weight and a full-scope coverage denominator; do not renormalize only the observed HO600 subset to 100% and call it full cost-of-living.

## Acceptance gates for the next iteration

| Gate | Required evidence | Current |
| --- | --- | --- |
| WGT-01 | Original 2020 revised occupation table and age-group table bytes (SHA-256 + local receipts) | BLOCKED_DOWNLOAD |
| WGT-02 | Verify table vintage 2026-02-13 correction and final consumption subtotals | NOT_RUN |
| WGT-03 | Deterministically extract all 12 consumption categories and annual totals without duplicates/summary row double counts | NOT_RUN |
| WGT-04 | For each genuinely measured cohort, 12 divisions nonnegative, total sum within published rounding tolerance | NOT_RUN |
| WGT-05 | Freeze household cohort definition and age×job cross-tab availability; no false independent marginal join | DEFINITION_READY / MATRIX_UNOBSERVED |
| WGT-06 | Classify all private HO600 50 subcategories to official 12 divisions; split mixed-purpose records individually | 50/50 STRUCTURAL PASS; 10 splits PENDING |
| WGT-07 | Independently retrieve 2025 categories and scope-compatible historical CPI/high-age benchmarks | BLOCKED_RAW |
| WGT-08 | Publish cohort rates only when 2020 weights, matched 2020/2026 prices, >=95% household spend coverage, essential costs and all release gates pass | BLOCKED |

`>=95%` is **the project's own predeclared rule**, not an official DGBAS standard. Housing and medical are mandatory even if projected monetary coverage exceeds 95%.

## Local-only procedure

```bash
git switch research/batch-09
python3 research/cohort-inflation/fetch_official_weight_tables.py --plan
python3 research/cohort-inflation/fetch_official_weight_tables.py --download NAT20-AGE
python3 research/cohort-inflation/fetch_official_weight_tables.py --download NAT20-OCC
```

The helper writes to the operating system temporary directory by default, fails closed on HTML/invalid file signatures, does not overwrite existing downloads, and records real SHA-256 + UTC retrieval receipt. The helper **has been committed but has not run a successful official download** here. Raw parsing/weight extraction requires its own later verifiable step. GitHub Actions remain paused.

## Verification and non-claims

- No numeric consumption weights have been calculated or entered.
- No WORK, RETIRE or high-age inflation figure has been calculated.
- No original HO600 600-item release/selection/index state has changed.
- No new formal Canonical batch validation is implied by this research audit.
