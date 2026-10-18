# HO600 Taipei CPI source, coverage, and age-head proxy result

**Run date:** 2026-10-18 Asia/Taipei
**Branch:** `research/batch-09`
**Result:** `PARTIAL_WITH_EXTERNAL_BLOCKERS`
**Scope label:** `TAIPEI_AGE_HEAD_CPI_PROXY`
**Full age-head rate:** `HOLD_NO_NORMALIZATION`

## Executive result

Both official Taipei basic CPI originals were retrieved successfully over HTTPS with macOS native CA verification. Their matched monthly and annual series pass period, class, positivity, base, and cross-series checks. The official raw records support the two preselected price windows, but the 12 household expenditure divisions cannot all be priced from the 48 CPI classes without unsupported splits. Only divisions 03, 09, and 10 are mapped. The other nine divisions remain `SPLIT_REQUIRED` or `UNMAPPED`, including required food, housing, and medical coverage. Every age-head group's mapped share is below the project gate of 95%, so only mapped-category contributions are reported; no complete cohort inflation rate is released.

The seven weight groups are **Taipei City household-head-age samples**. They are not nationwide households, employment-status groups, or retired households. The existing 84-cell 2020 budget weight file was read as-is and was not regenerated or modified.

## Official source retrieval and receipts

The live official [monthly CPI dataset page](https://data.taipei/dataset/detail?id=f47d7930-c507-4b5d-9ad3-907746a28342) and [annual CPI dataset page](https://data.taipei/dataset/detail?id=7ee57050-4d27-482c-bae5-ebd15ca86702) linked directly to the Taipei City DGBAS statistical information system. The current linked URLs and their landing-page snapshots are preserved with the originals in [`source-archive/tpe-cpi-20261018/`](source-archive/tpe-cpi-20261018/).

| Source | HTTP / TLS | Retrieved UTC | Bytes | SHA-256 | Actual period |
| --- | --- | --- | ---: | --- | --- |
| Monthly basic CPI | 200; `curl --ca-native`, strict system trust and hostname verification | 2026-10-17 23:56:25.829701 | 881,570 | `7d3d3b3f09080cd0f9f374a0bcf8e5c89750f1c54374734159221429618ed8ed` | 1998-01 to 2026-09 |
| Annual basic CPI | 200; `curl --ca-native`, strict system trust and hostname verification | 2026-10-17 23:56:26.413780 | 64,481 | `318de9dbcd7e95e4e626d1327a9284a38c955b08f7c167020db1da774f2f0d40` | 1998 to 2025 |

Both files are UTF-8 with BOM (`utf-8-sig`) and have fields `統計期`, `基本分類`, `原始值[統計數值]`, `年增率[%]`, `縣市別代碼`. Their final URLs are the exact official page download links recorded in the JSON receipts. The monthly dataset metadata says its last covered date is 2026-09-30, updated 2026-10-07 18:58:16; the annual dataset covers through 2025-12-31, metadata updated 2026-09-16 16:03:53. The CSV does not provide a row-level revision history, so historical revisions cannot be reconstructed from this release.

The previous `data.taipei` API routes did not return usable CSV bytes: the monthly frontstage route and annual frontstage route each returned HTTP 200 with an empty body; the monthly legacy download route returned HTTP 500. The new URLs were taken from the download anchors in the official dataset pages, then fetched with native trust and HTTPS-only redirects. No TLS verification was disabled and no CA settings were changed.

The two raw originals, JSON capture receipts, and landing-page snapshots are archived without replacing earlier evidence. The detailed, versioned [source register](taipei-cpi-official-source-register-2026-10-18.csv) records the URLs, response metadata, timestamps, row counts, and hashes.

## Period, class, and index-base checks

- The monthly original has 16,560 rows, 48 distinct basic-class labels, and a complete 345-month grid from 1998-01 through 2026-09. Every month has the same 48 labels; no duplicate period/class keys, blank labels, nonnumeric values, zeros, or negative index values were found. Every row is Taipei City code `63000`.
- 2020 has all 12 months for all 48 classes. The requested 2020 Jan–Sep baseline has 432 class-month rows (48 × 9). The requested 2026 Jan–Sep target also has 432 rows; all nine months are present for all 48 classes.
- The annual original has 1,344 rows: 28 complete years (1998–2025) × 48 classes. 2020–2025 therefore has six complete annual observations per class (288 rows). Monthly and annual class-name sets are identical. The source has no separate CPI-class code field, so identity is verified by stable labels and full-grid coverage, not by a code field.
- The [Taipei City September 2026 CPI release](https://dbas.gov.taipei/News_Content.aspx?n=61D456768E73CD92&s=E89309C4919E6F57) identifies the index base as 2021=100 and September all-items CPI as 113.95. The original monthly file's 2026-09 `總指數` is 113.95; all 48 official 2021 annual class indices equal 100.00. The downloaded series is already presented on this current common base; no separate rebasing factor was applied.
- For each of the 288 class/year pairs in 2020–2025, the arithmetic mean of the 12 published monthly indices agrees with the official annual index within 0.005 index points, the maximum difference attributable to displayed two-decimal precision.
- A scan of 3,888 consecutive class-to-month pairs from 2020-01 through 2026-09 found eight moves with absolute month-over-month change of at least 20%. The largest were in apparel around September–October, eggs, vegetables, and fuel. These are retained and flagged for subject-matter review; the scan alone does not classify them as source errors. No values were deleted, smoothed, or imputed.

The committed [`monthly-period-coverage-audit.json`](results/tpe-cpi-20261018/monthly-period-coverage-audit.json) records the requested 2020/2026 Jan–Sep month-grid audit and 48/48 complete classes. The fuller source-profile and reconciliation evidence is in [`age-head-partial-cpi-analysis.json`](results/tpe-cpi-20261018/age-head-partial-cpi-analysis.json).

## Twelve household divisions mapped to CPI detail

The detailed [12-division crosswalk](taipei-2020-age-head-to-cpi-basic-crosswalk-20261018.csv) uses the actual classes in the official Taipei CPI files and their official release descriptions. It assigns all 12 rows a controlled status:

| Status | Divisions | Count |
| --- | --- | ---: |
| `MAPPED` | 03 clothing, 09 leisure/culture to `(二)娛樂費用`, 10 education to `(一)教養費用` | 3 |
| `SPLIT_REQUIRED` | 01, 02, 04, 05, 06, 07, 11, 12 | 8 |
| `UNMAPPED` | 08 communication | 1 |

The old broad seven-group CPI labels do not support an automatic one-to-one mapping. The downloaded basic detail does resolve education versus entertainment into separate indices, so it is those specific indices, rather than the whole `教養娛樂類` group, that are used for 09 and 10. The main remaining gaps are:

- Food CPI includes `外食費`, while household restaurant/hotel expenditure is a separate division. The available 12-division weights cannot strip or reweight that component.
- Alcohol and tobacco/betel are in different CPI basic classes, but the household weights combine them.
- CPI `居住類` contains rent, repair, household goods, household management, and utilities; household divisions 04 and 05 separate those purposes differently. No required within-division household shares are available to build separate price relatives.
- CPI medical classes cover medical expenses, drugs/supplements, and equipment. DGBAS says National Health Insurance premiums are outside CPI scope, but the published household table has no NHI-premium row to reconcile inclusion and scope.
- CPI groups transport with communications; one published basic class itself combines transport and communications equipment. Taipei's 48-class file has no standalone communications-service index. Division 08 is therefore unmapped, and division 07 requires a split.
- Household restaurants and hotels combine eating-out food and lodging; the Taipei 48-class series has no separate hotel-accommodation basic class. The miscellaneous division is also too broad and overlaps the tobacco/betel CPI class.

Official scope references used for the crosswalk include the Taipei September 2026 release, the [DGBAS CPI scope note](https://ws.dgbas.gov.tw/001/Upload/463/relfile/0/3931/%E7%B5%B1%E8%A8%88%E7%9F%A5%E8%AD%98cpi%E7%B0%A1%E4%BB%8B.pdf), the DGBAS [housing CPI explanation](https://www.dgbas.gov.tw/News_Content.aspx?n=3987&s=230873), and the [110-base CPI checked-item classification and weights](https://ws.dgbas.gov.tw/001/Upload/463/relfile/11021/233436/c9ba0697-c83c-4c34-a5e6-757e74e913bc.pdf). National classification references are used only to understand CPI scope; no national price observations or weights are substituted for the Taipei series.

## Conditional calculation: verified mapped contributions only

The calculation applies the existing 2020 age-head household-spending shares to the accepted CPI classes and leaves all unpriced shares uncovered. It does not renormalize mapped weights. The two comparisons are:

- **A:** average monthly index Jan–Sep 2020 to average monthly index Jan–Sep 2026.
- **B:** official annual index 2020 to official annual index 2025.

The Taipei all-items CPI change calculated from the same raw file is **+14.2168% for A** and **+12.2969% for B**. These are general CPI changes for Taipei consumers. They are shown as a benchmark; they are not comparable as complete age-head rates to the partial contributions below. The official September 2026 press release's +1.74% compares Jan–Sep 2026 with Jan–Sep 2025, so it is not the 2020-to-2026 value used in A.

| CPI class mapped to household division | A price change | B price change |
| --- | ---: | ---: |
| 03 clothing → `二.衣著類` | +0.6121% | −0.2627% |
| 09 leisure/culture → `(二)娛樂費用` | +36.9114% | +33.6436% |
| 10 education → `(一)教養費用` | +5.9469% | +4.1808% |

The following are **partial mapped-category contributions**, in percentage points, with each age group's unpriced share retained:

| Household-head age | Mapped coverage | Uncovered | A partial contribution | B partial contribution |
| --- | ---: | ---: | ---: | ---: |
| 未滿30歲 | 10.24% | 89.76% | +2.3453 pp | +2.0991 pp |
| 30～34歲 | 9.55% | 90.45% | +2.1107 pp | +1.8871 pp |
| 35～39歲 | 11.47% | 88.53% | +2.3581 pp | +2.0911 pp |
| 40～44歲 | 14.38% | 85.62% | +2.5055 pp | +2.1887 pp |
| 45～54歲 | 15.26% | 84.74% | +2.7130 pp | +2.3734 pp |
| 55～64歲 | 12.00% | 88.00% | +2.6765 pp | +2.3875 pp |
| 65歲及以上 | 7.57% | 92.43% | +1.9018 pp | +1.7103 pp |

The mapped-contribution difference for 65+ minus 45–54 is **−0.8112 pp for A** and **−0.6631 pp for B**. These are differences in the three mapped contributions only, not differences in full age-group inflation.

Sensitivity: if division 09 is withheld because its `休閒與文化` to `娛樂費用` alignment needs stricter item-level confirmation, A mapped coverage falls to 2.54%–8.95% across the seven groups. The 65+ partial contribution falls from +1.9018 pp to +0.0447 pp. This shows why entertainment's large price relative is not a basis for filling the other expenditure divisions.

## Verification and release gate

- Downloader unit tests: **16/16 PASS**.
- Monthly period-auditor unit tests: **9/9 PASS**.
- Real source audit: **48/48** CPI classes complete for both required Jan–Sep windows; no missing months.
- Independent `Fraction` recomputation: **14/14 age-period summaries and 42/42 category contribution rows match** the primary Decimal calculation; maximum absolute numerical difference is below `5.1e-13`.
- The project release rule requires at least 95% weighted coverage for every age group and full food, housing, and medical coverage. Actual coverage is 7.57%–15.26%; mandatory divisions 01, 04, and 06 remain split-required. **Full `TAIPEI_AGE_HEAD_CPI_PROXY` rate stays HOLD.**

Machine-readable results are in [`age-head-partial-contributions.csv`](results/tpe-cpi-20261018/age-head-partial-contributions.csv), [`age-head-partial-cpi-analysis.json`](results/tpe-cpi-20261018/age-head-partial-cpi-analysis.json), and [`independent-recalculation-receipt.json`](results/tpe-cpi-20261018/independent-recalculation-receipt.json). The executable primary and independent calculations are [`analyze_taipei_age_head_cpi_coverage.py`](analyze_taipei_age_head_cpi_coverage.py) and [`independently_recalculate_taipei_age_head_partial_cpi.py`](independently_recalculate_taipei_age_head_partial_cpi.py).

## Project boundaries

National revised 2020 WGT-01 remains `HOLD`; Taipei age-head weights are not a national substitute. No claim is made that age-65+ household heads are retired, or that the 45–54 group represents all workers. HO600 remains 181/600; Basket remains `NOT SEALED`; Index remains `LOCKED`. No official workbook, candidate data, `main`, or GitHub Actions was changed or used.
