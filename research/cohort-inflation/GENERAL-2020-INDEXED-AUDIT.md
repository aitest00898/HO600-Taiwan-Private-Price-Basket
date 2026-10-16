# 2020 National General Household Consumption Shares — Interim Audit

**This is NOT WORK or RETIRE spending weights. Not an inflation rate. Not a released cohort index.**

## Official source and evidence level

- Source: DGBAS (2020 / ROC 109) Family Income and Expenditure Survey 2020, official 2026-hosted PDF: https://ws.dgbas.gov.tw/001/Upload/463/ebook/ebook_357924/pdf/full.pdf
- Published 2020 household total: **NT$815,100 per household annually**.
- Official search-indexed text explicitly contains all 12 expenditure values, independently visible in the 2020 report's occupation and farm/non-farm tables. **Both belong to the same official report, not two independent publishing organizations.**
- Original source PDF and corrected XLS/ODS **bytes were not retrieved** in this turn; file signature, PDF page screenshot and SHA-256 **NOT VALIDATED**. This is therefore **INTERIM_INDEXED_EXCERPT**, not a final national weight-import gate PASS.
- Official 2020 table landing: https://www.stat.gov.tw/News_Content.aspx?n=3908&s=210989 ; its accompanying notice says affected 2020 tables were corrected and republished on **2026-02-13**. The first independent future raw import must verify that the PDF/indexed numbers agree with the revised 2020 XLS/ODS tables.
- Data rows: [general-household-2020-indexed-v0.csv](./general-household-2020-indexed-v0.csv)

## Arithmetic reconciliation

- 12 expenditure divisions add to exactly **NT$815,100** (pass).
- 12 weights generated directly from category/815100; unrounded sum 100.000000%.
- Housing/energy class 04 **198,145**, medical class 06 **139,010**; combined **337,155** or **41.363636%** of general household expenditure.
- This important coverage warning cannot be substituted as 41.36% of spending for retirees or employees, because those subpopulations have different exposure and unverified splits.
- Cohort `ALL_HOUSEHOLDS_GENERAL` is the **sole** observed population. `WORK` and `RETIRE` national price-weight rows remain **0**.
- Annual **2020 consumption shares** differ conceptually from 2020→2026 HO600 *normal-list-price* relatives. They are an aggregation input only after price, cohort and coverage gates are independently passed.

## Interpretation and blockers

Do not place these weights inside the canonical seven-sheet HO600 workbook, `Candidate_Pool`, or any released `Index_Calc` field. They remain in research only.

**Provenance blocker**: official PDF screenshot/raw bytes not obtainable via current browser; source table extraction reproduced here only as indexed-text transcription. Verify all 12 rows from the 2026-02-revised canonical official XLS/ODS before upgrading to official BASELINE_ACCEPTED.

**Working/retired-specific blocker**: no cohort demographic expenditure matrix retrieved. Even a verified household-head occupation or age table cannot be labeled a direct representative employee household or an actual retired household without the corresponding survey definitions.

**2025 discovery update**: official report/e-book directory lists 114-year 2025 Survey Report as an available report, and official year-by-area spreadsheets enumerate 114 (2025): https://www.stat.gov.tw/cp.aspx?n=2696 and https://www.stat.gov.tw/cp.aspx?n=3984 . These are real official *entry points*, but **do not yet prove the 2025 12-category occupation-by-age cross-tab or verified raw data**. Correct prior blanket statement that only the press release was findable.

## QA requirements for promotion

1. Recover and hash the corrected original official XLS/ODS (2020 age and occupation); pin source DOI/URL, retrieval timestamp, exact sheet tab, 12 rows.
2. Numerically reconcile the national general totals with this 12-row index-excerpt CSV within the official rounding allowance; a mismatch yields STOP / SOURCE_CONFLICT, not automatic overwrite.
3. For employee proxy and head-age proxy separately, verify cohort column header, units, age/occupation coding and category subtotals. No marginal-table cross multiplication.
4. No actual `WORK`/`RETIRE` inflation rate until measured applicable weights, external essential price series and coverage gates are satisfied.
