# HO600 WGT — Taipei 2020 validated age-of-household-head exposure analysis

**Date:** 2026-10-17, analysis branch `research/batch-09`. **Input** [verified 84-row city proxy CSV](./results/tpe-2020-age-head-proxy-20261017/TPE_AGE_HEAD_EXPENDITURE_PROXY_WEIGHTS_2020.csv) with [PDF Table 8 / city CSV reconciliation](./results/tpe-2020-age-head-proxy-20261017/tpe-2020-age-head-proxy-reconciliation.json): **96/96 spending cells** and **8/8 published totals** match, max absolute printed table sum error NT$2. Seven age-head proxies and 12 official 2020 household spending divisions. This report contains **budget shares, NOT inflation**.

## Head age and 2020 budget mix (Taipei per-household annual average)

| Age of household head | Total annual spend NT$ | Housing/energy % | Health % | Combined % | Education % | Transport % |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| 未滿30歲 | 1,126,300 | 24.68 | 17.29 | **41.97** | 1.13 | 6.36 |
| 30～34歲 | 1,113,976 | 28.43 | 14.14 | **42.57** | 0.89 | 5.95 |
| 35～39歲 | 1,147,520 | 26.07 | 13.73 | **39.80** | 2.93 | 8.12 |
| 40～44歲 | 1,157,326 | 26.22 | 12.94 | **39.16** | 5.87 | 6.74 |
| 45～54歲 | 1,189,599 | 24.83 | 13.22 | **38.05** | 6.19 | 6.86 |
| 55～64歲 | 1,172,784 | 26.92 | 13.54 | **40.46** | 2.29 | 7.08 |
| 65歲及以上 | 883,356 | 34.31 | 17.35 | **51.66** | 0.55 | 4.69 |

**65+ household-head proxy**: housing NT$303,048 (34.31%); health NT$153,271 (17.35%); combined **51.66%**. Their average total annual spending is NT$883,356.

**45–54 household-head proxy**: housing NT$295,414 (24.83%); health NT$157,252 (13.22%); combined **38.05%**. Their average total annual spending is NT$1,189,599.

The combined share differs by **13.6054 percentage points**. Yet the **absolute** housing+health outlays are **NT$456,319 for 65+ versus NT$452,666 for 45–54** (difference **NT$3,653**). In fact, per-household medical spending is slightly lower for age-head 65+ (NT$153,271) than for 45–54 (NT$157,252). **The age difference in budget share cannot be treated as evidence of higher nominal medical spending or more rapid medical inflation.** Smaller overall spending denominators matter, and average household composition differs. The source reports age-head 65+ households have **0.43 employed people per household**; they are **not** all retirees.

## 65+ versus 45–54, all 12 classes

| Division | Category | 65+ share % | 45–54 share % | 65+ minus 45–54, percentage points |
| --- | --- | ---: | ---: | ---: |
| 01 | 食品及非酒精飲料 | 14.62 | 14.68 | -0.06 |
| 02 | 菸酒及檳榔 | 0.55 | 0.74 | -0.20 |
| 03 | 衣著鞋襪及服飾用品 | 1.99 | 2.76 | -0.77 |
| 04 | 住宅服務水電瓦斯及其他燃料 | 34.31 | 24.83 | +9.47 |
| 05 | 家具設備及家務維護 | 3.22 | 3.24 | -0.02 |
| 06 | 醫療保健 | 17.35 | 13.22 | +4.13 |
| 07 | 交通 | 4.69 | 6.86 | -2.17 |
| 08 | 通訊 | 1.92 | 2.48 | -0.56 |
| 09 | 休閒與文化 | 5.03 | 6.31 | -1.28 |
| 10 | 教育 | 0.55 | 6.19 | -5.65 |
| 11 | 餐廳及旅館 | 11.14 | 13.61 | -2.48 |
| 12 | 什項消費 | 4.64 | 5.07 | -0.44 |

All twelve categories are retained, including tobacco/alcohol, housing, and medical. Percentages use the sum of the twelve published category amounts, not the independently reported grand total, because the published rounded numbers differ by up to NT$2; no category is dropped and no delta is silently spread across rows. The regional data is not national 2020 revised data; its 65+ **household-head age** variable is not retirement status.

## CPI discovery: candidate official Taipei reference series (NO raw index imported)

Recent public metadata of Taipei City Government's statistical open data catalog identifies:

1. [臺北市消費者物價指數基本分類月指數](https://data.gov.tw/dataset/131822) — official `年月別, 基本分類, 原始值[統計數值], 年增率`, monthly, possible finer-grained crosswalk.
2. [臺北市消費者物價指數按月別](https://data.taipei/dataset/detail?id=0cf1d853-b63c-4366-a611-217b2c419a1e) — historic from 1998 with monthly overall, food, clothing, housing, rent, transport/communications, medical, education/recreation and miscellaneous groups; **this is not one-to-one with the 2020 household 12-division expenditure categories**.
3. [臺北市消費者物價指數基本分類年指數](https://data.taipei/dataset/detail?id=7ee57050-4d27-482c-bae5-ebd15ca86702) — official yearly basic-category series, through **2025** per current published metadata; monthly data needed for 2026 YTD.
4. [臺北市消費者物價總指數銜接表](https://data.gov.tw/dataset/132040) — essential for handling index reference-base changes; rebase all actual monthly series to a consistent 2020 reference.

**Source availability is not acceptance.** No actual CPI raw CSV from these datasets has been ingested, no classification to 12 divisions audited, and no 2020→2026 numeric relative verified. The standard official broad-group CPI has fewer categories than household expenditures; direct same-number ordinal matching is *forbidden*. 2026 is in progress and must use a matched month window; for 2020 full-year versus 2026 Jan–Sep/YTD comparisons define price periods in advance, avoiding unadjusted seasonality. 2025 full-year can be an independently labelled preliminary reference if both yearly series and classifications are validated.

## Next measurable research task

- Retrieve official **2020–2026 Sept** monthly Taipei CPI category series over native validated HTTPS, capturing actual original bytes/SHA/URL/date and detailed group labels.
- Create `tpe_2020_expense_to_cpi_crosswalk_v1.csv` with exactly 12 spending categories, many-to-one/one-to-many mappings and `MAPPED|SPLIT_REQUIRED|UNMAPPED` status after inspecting actual CPI series classification. Important: explicit exclusion or incomplete coverage must keep `TPE_COHORT_CPI = HOLD`, not renormalize surviving categories.
- Verify index base rebasing, class scope, matching periods and source category balance. Compute a proper 2020 fixed weight regional age-head price index only **when** enough actual CPI relatives are independently verified, and label it `TAIPEI_AGE_HEAD_CPI_PROXY`, not HO600-WORK/RETIRE or HO600 private historical exact index.
- National corrected 2020 XLS/ODS and genuine WORK/RETIRE household status remain blocked; no national WGT gate is changed.

**WGT status after this analysis:** `TAIPEI_2020_AGE_SPEND=PASSED_RECONCILIATION`, `TAIPEI_PRICE_SERIES=NOT_RETRIEVED`, `TAIPEI_CPI_RATE=NOT_CALCULATED`, `NATIONAL_WGT01=HOLD`, `WORK/RETIRE=0/2`, `CANONICAL_MAIN=181/600_NOT_SEALED_LOCKED`. No GitHub Actions.
