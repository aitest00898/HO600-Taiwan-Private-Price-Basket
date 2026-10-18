# Taipei age-head inflation research — latest 2026 CPI periods and classification acceptance

**2026-10-17 (Taipei). Status: PRICE_SOURCE_METADATA_VERIFIED, CPI_RAW_BYTES_HOLD, AGE_COHORT_INFLATION_NOT_CALCULATED.** Research branch only; canonical HO600 `main` remains 181/600, Basket NOT SEALED, Index LOCKED. No GitHub Actions or published inflation rate.

## 1. Confirmed official 2026 benchmark

Taipei City DGBAS office issued the [2026-09 CPI bulletin](https://dbas.gov.taipei/News_Content.aspx?n=61D456768E73CD92&s=E89309C4919E6F57) on **2026-10-07**. It states CPI `2021=100`, **September 2026 all-consumer index 113.95**, month-on-month +0.64%, year-on-year +2.65%, and Jan–Sep 2026 average **+1.74% versus Jan–Sep 2025**. It specifically describes **seven main CPI groups**, not the 12 household survey expense categories.

These values are saved in [the official news release benchmark CSV](./taipei-cpi-2026-09-all-consumers-official-press-benchmark.csv). **They do not imply Jan–Sep 2020→Jan–Sep 2026 cumulative inflation or any 2020 age-head cohort figure.** Rounded index 113.95 and published percentage +2.65% should not be independently forced to reproduce each other exactly; source release rounding differs.

Current official [Taipei basic monthly open-data landing](https://data.taipei/dataset/detail?id=f47d7930-c507-4b5d-9ad3-907746a28342) declares range **1998-01-01 through 2026-09-30**, metadata updated 2026-10-07. Official [basic annual series](https://data.taipei/dataset/detail?id=7ee57050-4d27-482c-bae5-ebd15ca86702) covers through **2025-12-31**. Both are free official datasets but **neither original CPI CSV has been retrieved in this assistant environment**: the current model container failed DNS for the official host; official download links returned web-gateway cache miss or unsupported text/csv; direct container download failed. These are not successful HTTPS source receipts.

Also [official general index bridge data](https://data.taipei/dataset/detail?id=a046606e-818a-45dd-8395-b0e004551347) were found, linked in the four-row [CPI source register](./taipei-cpi-official-source-register-2026-10-17.csv), but this **does not itself provide 12 CPI price classes**.

## 2. Exact price observation windows

| Comparison | Baseline prices | Target prices | 2020 age expenditure weights | Required status |
| --- | --- | --- | --- | --- |
| Regional age-head early result, matched partial years | **Jan–Sep 2020** official monthly CPI, same classes | **Jan–Sep 2026** same classes | Taipei 2020 age-head 12 spending categories, separately validated | `HOLD_CPI_RAW_AND_CLASS_BRIDGE` |
| Completed-years control | **2020 January–December** or verified 2020 official annual class index | **2025 January–December** or verified 2025 annual index, consistent base | Same 2020 weights | `HOLD_CPI_RAW_AND_CLASS_BRIDGE` |
| Official 2026 headline | Already published **Sep 2026 index 113.95** | Official +2.65% Sep YoY, +1.74% Jan–Sep 2026 versus **2025**, not 2020 | None; official aggregate CPI uses its own weighting system | `OFFICIAL_PRESS_BENCHMARK_ONLY` |

The 2026 year is not yet completed on 2026-10-17; never silently compare `2020 full calendar year` against `2026 Jan–Sep` without seasonal/period qualification.

## 3. Crucial CPI expense classification mismatch

The published monthly Taipei CPI headline comprises **seven major groups**:

`食物類、衣著類、居住類、交通及通訊類、醫藥保健類、教養娛樂類、雜項類`.

The 2020 Taipei household survey has **12 different expenditure divisions**. In particular:
- `交通` and `通訊` are separate expenditure divisions but share the major CPI `交通及通訊類` class. An unqualified two-way split would be invented prices.
- `教育` and `休閒與文化` share major CPI `教養娛樂類`, but may have different underlying trends.
- `食品及非酒精飲料` and `餐廳及旅館` cannot be independently backed by the broad `食物類` index alone. Restaurants and hotels also have distinct scopes.
- `住宅服務水電瓦斯及其他燃料` includes consumer housing service and administered utility effects; `居住類` may not match every survey component.
- `醫療保健` vs `醫藥保健類` is a **candidate correspondence**, not guaranteed identical in CPI coverage.

The 12-row [conservative proposed category map](./taipei-2020-spending-vs-7-cpi-class-crosswalk-PENDING.csv) marks every class `price_relative_accepted=NO` until deeper actual `基本分類` rows and definition documents have been reviewed. Even the 2 `SEMANTIC_CANDIDATE` entries are **not yet approved**. It is **forbidden** to map 12 values to 7 indices merely because the class names sound similar.

## 4. Reproducible research-only source retrieval changes

[`fetch_taipei_cpi_basic_official.py`](./fetch_taipei_cpi_basic_official.py):
- Native strict `curl --ca-native` HTTPS, only real `data.taipei` domains and official pre-approved resource UUIDs.
- Monthly: first try the *current official clickable frontend* `rid=4a4ea957-c620-4056-89bb-50c7a4bd7325`, then **the same resource** by its official legacy endpoint on failure. These are **two transport routes to one dataset, NOT independent validation**.
- Annual: current official frontend `rid=3e6ed9d0-0e86-4d99-8047-2fa68fb4ec90`.
- Accept historic header `年月別` / `年別` **or** updated `統計期`, validate basic-class labels and presence of 2020; do **not** assume 2026 monthly values just from metadata.
- The response bytes, original source URL, status, SHA-256, retrieval UTC, index fields, year rows and any failed attempt evidence are preserved **only** after successfully authenticated original CSV data and parsed schema.
- Explicitly no category split, class rebase, 2020→2026 inflation rate or canonical result computation.
- [16 offline synthetic fixture tests](./test_fetch_taipei_cpi_basic_official.py) include year/period formats, modern `統計期`, ambiguous field rejects, invalid HTML/JSON and duplicate observations. **Committed but not yet run on user's Mac.** The assistant container cannot access the GitHub source file through its public DNS, so it does not assert a successful Python test run.

## 5. Gates for a cohort age proxy CPI release

1. `TPE-PRICE-01 SOURCE`: original official monthly CSV real HTTPS 200, original bytes, UTC receipt, official URL, SHA-256, permission and source version.
2. `TPE-PRICE-02 GRAIN`: unique city+period+class keys, actual class labels, positive original CPI observations, unchanged index-basis labels and source classification lineage.
3. `TPE-PRICE-03 PERIOD`: 2020 Jan–Sep and 2026 Jan–Sep matched **all nine months** for every mapped class; 2020 and 2025 completed annual references independently verified.
4. `TPE-PRICE-04 BASE`: one verified index reference base (`2021=100`) or separately proved rebasing/linking factors **for each needed subcategory**; an all-items bridge table alone cannot automatically repair class-level base changes.
5. `TPE-PRICE-05 CROSSWALK`: item-level definition/coverage map from all 12 household expenditure categories to actual CPI subcategories, with audited many-to-one and split rules. Each mapped category must have a price relative and documented consistent geographic scope.
6. `TPE-PRICE-06 COVERAGE`: calculate baseline *share-weighted coverage* for **each** age-head group; project policy >=95% and full mandatory housing/medical/food coverage. This threshold is project-defined, **not a Taipei government rule**.
7. `TPE-PRICE-07 ARITHMETIC`: fixed 2020 cohort weights, same-season 2020/2026 CPI class relatives, denominator QA, no silently renormalized missing classes, independent re-run.
8. `TPE-PRICE-08 LABEL`: only `TAIPEI_AGE_HEAD_*_CPI_PROXY`, **not** actual retired households, worker households, national DGBAS WGT-01 or the original private HO600 600-item basket.

Until all gates, **cohort age inflation = NOT_CALCULATED**. The published official September 2026 general CPI still serves as a verifiable benchmark for its own population and periods.

## Follow-up — 2026-10-18

The dated status above records the 2026-10-17 source state. On 2026-10-18, official monthly and annual Taipei basic CPI CSVs were retrieved from the current download anchors on the official dataset pages with strict native TLS, then audited over the requested periods. See [the 2026-10-18 source, crosswalk, and partial-contribution result](./TAIPEI-CPI-2026-10-18-DATA-CROSSWALK-PARTIAL-RESULT.md). The source/period/base gates passed, but only 3 of 12 household divisions were mapped; weighted coverage remains 7.57%–15.26%, below the 95% policy threshold, with mandatory food, housing, and medical categories unresolved. Full age-head CPI remains HOLD.
