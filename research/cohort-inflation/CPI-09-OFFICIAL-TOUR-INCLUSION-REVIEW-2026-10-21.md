# HO600 — CPI expense division 09: official evidence that tours are INCLUDED in 娛樂費用

**Date:** 2026-10-21 (Asia/Taipei). **Linear:** [OO1-147](https://linear.app/001dev/issue/OO1-147). **Status:** IMPORTANT PARTIAL SOURCE RESOLUTION; `MAPPED_PROVISIONAL_SCOPE_REVIEW` remains, no accepted new CPI relative or cohort rate.

## Counterevidence to the earlier overly broad tourism caution

The previous [research sensitivity memo](./TAIPEI-2020-CHILD-SPENDING-AND-ENTERTAINMENT-SENSITIVITY-2026-10-18.md) noted that **40.25–50.01%** of the 2020 Taipei age-head household `09 休閒與文化` spending is `[1]套裝旅遊(不含自助旅遊)`. It correctly warned that the household spending division spans multiple item types and the entire 09→CPI 娛樂費用 mapping must not be auto-approved. However **package tours themselves are not a prima facie exclusion** from the entertainment index.

**Official first-party Taipei city price release (2024-04-09, March 2024 data):**

[臺北市主計處「113年3月臺北市物價變動概況」](https://dbas.gov.taipei/News_Content.aspx?n=61D456768E73CD92&s=38EB273A807DA02A&sms=72544237BBE4C5F6) specifically uses the example **娛樂費用（如國內、外旅遊團費）** and explains that the foreign package-travel fee contributed to movement of the entertainment expense price class. The stated index base is 民國110年=100 (2021=100). This is **direct city-government proof of inclusion of domestic and foreign group travel fees in entertainment expenses during that report**, not proof that the entire 2020 surveyed household division maps one-to-one.

The city's [2020 household expenditure item hierarchy](https://tsis.dbas.gov.taipei/statis/webMain.aspx?barf=&k1=A22002504) lists four **distinct** leisure/culture spending components:
1. `套裝旅遊(不含自助旅遊)`
2. `娛樂消遣及文化服務`
3. `書報雜誌文具`
4. `教育消遣康樂器材及其附屬品`.

The [original city 2021-base CPI monthly raw archive](./source-archive/tpe-cpi-20261018/TPE-CPI-BASIC-MONTH-official-original.csv) has 48 basic classes, including `六.教養娛樂類`, `(一)教養費用`, `(二)娛樂費用`, but **does not publish a separate time series for all four 2020 age-head household 09 child categories**. A 2024 release describing selected entertainment-price items does not supply precise category aggregation weights, tourism-only price series, equipment/print-item placement, or 2020→2026 matched weights.

Additional item-scope research leads: [DGBAS 2021-base CPI item/weight tables (official)](https://www.stat.gov.tw/News_Content.aspx?n=2664&s=233436) and [DGBAS CPI 2021-base changeover item comparison](https://www.stat.gov.tw/News_Content.aspx?n=2664&s=230346). Their **full item membership has not been downloaded/reconciled** in this step; do not claim country table automatically equals Taipei class membership.

## Corrected decision / requirement

**No longer valid:** treating substantial `套裝旅遊` spending as itself evidence that CPI entertainment excludes the category. Official first-party evidence contradicts that exclusion premise.

**Still unverified:** 100% weight assignment of the 2020 09 parent to the `(二)娛樂費用` 2021-base class; alignment of `書報雜誌文具` and `教育消遣康樂器材` plus any scope overlaps; tourism price basket within entertainment vs same 2020 age-head purposes; one aggregate CPI relative applied to all four children.

**Preserved:** `CPI_09 = MAPPED_PROVISIONAL_SCOPE_REVIEW`, original historical 3-class partial contribution and the sensitivity excluding 09 **both remain valid arithmetic scenarios**, but the exclusion is now a **deliberately conservative uncertainty sensitivity**, not a fact that tourism is out of CPI. **No full seven-age inflation rates are released.**

## Smallest follow-up to close OO1-147

1. Collect the **actual official 2021-base CPI item and weight file(s)** and item membership used by Taipei CPI entertainment; pin exact 2021, 2024, 2026 scope if changed.
2. For four household 09 children, make a matrix of **definite CPI entertainment inclusion, definite exclusion, or unknown** with item-code-specific references and whether coverage by city 48 basic class is sufficient.
3. Recompute what can be mapped *without assigning one broad CPI sub-index to incompatible household children or normalizing missing weights*. Validate A/B independently against the raw original month/year receipts. Only then consider promoting any portion of 09 into the accepted mapping.
4. Until complete, remain `PARTIAL` with no 95%/full-cohort publication.

No changes to main, CPI raw data, previously reported rates, official workbook, branch merges, or GitHub Actions.
