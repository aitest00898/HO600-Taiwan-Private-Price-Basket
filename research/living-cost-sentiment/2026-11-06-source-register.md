# 2026-11-06｜民間生活成本／體感通膨來源整理（非 HO600 正式價格證據）

- Repo: `aitest00898/HO600-Taiwan-Private-Price-Basket`
- Data: [2026-11-06-evidence-observations.csv](./2026-11-06-evidence-observations.csv)
- Extraction cutoff: 2026-11-06 (Asia/Taipei).
- Record count: **28** metric observations across **6 source groups** (one report can contain several metrics).
- **Classification:** research-only source context / price leads. These are NOT `Exact-2020 ↔ Exact-2026` private normal/list/base-price pairs. Core admission: **0**.
- `main` canonical must remain **199/600**, Candidate Pool **434**, Evidence **1,600**, Basket **NOT SEALED**, Index **LOCKED** until full workbook QC and formal promotion. This research CSV is intentionally outside the 7-sheet canonical and `data/Evidence.csv`.

## Source catalogue and disposition

| Source ID | Publisher and period | Evidence type | Use | Limitation |
|---|---|---|---|---|
| MIRAI-20261007 | [未來流通研究所，2026-10-07](https://www.mirai.com.tw/the-cpi-for-food-away-from-home-in-taiwan-have-risen-by-a-cumulative-20-2-over-the-past-five-years/) | **Secondary analysis using category CPI-derived indices** | Standalone context only | The publisher is private but underlying price index is not independent private store collection. **DO NOT use as HO600 private-price data or private weights**. 2021 vs 2026H1 cannot replace Exact-2020/2026. |
| CATHAY-20261020 | [國泰金控，2026-10-20](https://www.cathayholdings.com/holdings/lastest_news/news_archive/newsarticle?newsID=4xjN1IyKjUyQOwUvy-wreA) | **Private survey, 2026-10-01–07, 13,461 valid responses** | Sentiment/expectations layer only | Cathay website members / bank customers are a selected respondent population; opinions and expected inflation are not observed retail prices. |
| SINICA-202606 | [經濟日報 2026-09-07 數字報導](https://money.udn.com/money/story/10869/9739955); [中研院 2026-06-09–28 調查公告](https://www.rchss.sinica.edu.tw/main/posts/13408) | **Academic survey of expected living costs, quoted by secondary media** | External survey reference only | Primary survey fieldwork verified, but first-party numeric result table not independently checked here; use secondary attribution. This is not a private collected price, nor inflation realized. |
| PTT-20260919 | [PTT 雞腿飯貼文，2026-09-19](https://www.ptt.cc/bbs/Gossiping/M.1789770197.A.748.html) | **One anonymous self-report, previous/current 125/135 TWD** | Shop-price lead only | Merchant, address, earlier date, portion and receipts not verified. 125→135 is **8.0% within the claimed pair**, NOT a verified year-over-year inflation rate. |
| PTT-20260923 | [PTT 豬肉泡菜便當貼文，2026-09-23](https://www.ptt.cc/bbs/Gossiping/M.1790136432.A.F82.html) | **One anonymous self-report, previous/current 120/125 TWD** | Shop-price lead only | Current attached picture does not establish prior price or merchant/spec identity. 120→125 is **about 4.17% within the claimed pair**, NOT verified year-over-year inflation. |
| PTT-20260629 | [PTT 外食預算討論，2026-06-29](https://www.ptt.cc/bbs/Gossiping/M.1782720919.A.74D.html) | **Illustrative consumption budget** | Behavioral context only | Breakfast 65 + lunch 120 + dinner 120 = 305 TWD/day; 30 days = 9,150 TWD. Not an observed price series. |

## Directly checkable key values

- MIRAI: 2021 to 2026H1, overall eating-out index +20.2%; Chinese breakfast +29.0%; Western breakfast +25.4%; Western fast food +13.6%; hand-shaken drinks / takeout coffee +12.7%. Street stalls, hotpot and bento: **strictly greater than +22%** (not exactly 22%).
- Cathay survey: 2026 annual inflation **expected** mean 2.52%; 52% expect above 2.5%; 32% report no obvious household financial gain from growth; 14% report worse household finances.
- Academia survey (secondary-reported): 67.55% expect higher total living expenditure in 12 months; 43.18% expect a rise of **at least** 10%; 58.97% expect a rise of **at least** 5%.
- PTT: the 125→135 and 120→125 claims have no directly verifiable, comparable Exact-2020 baseline and cannot enter the index.

## Strict guardrails

1. **Do not** add these records to `Candidate_Pool.csv`, `Evidence.csv`, canonical workbook, `Basket_600`, or `Index_Calc`. No observed movement, percentages, or trend fields in the Candidate Pool.
2. **No** government-collected prices or CPI weights in HO600 core. MIRAI's index-derived figures are explicitly quarantined as external commentary, even though published by a private organization.
3. **No** year substitution (2021 is not 2020), interpolation, invented merchant/branch, mix of units, promotion prices, delivery markups, or treating anonymous posts as independent verified prices.
4. The survey percentages are expectation *shares*, not household's actual inflation; multi-year accumulated changes are not annual rates. PTT price anecdotes are not population estimates.
5. Before any potential PTT conversion to formal HO600 evidence, verify shop identity, location/channel, old and new source dates, comparable item/spec/normal prices, photo/receipt provenance and direct Exact-2020 and Exact-2026 evidence; otherwise HOLD.
6. Copy only limited public numerical facts and links; don't mirror restricted article figures, full posts, paywalled content or respondent private information. Only GitHub connector writes; no GitHub Actions or automatic merge.

## Validation performed for this research import

- Parsed/reviewed publisher text of MIRAI and Cathay directly; checked source post text and publication dates for all three PTT discussions.
- Academia survey fieldwork period verified via primary organizer; **June numeric breakdown sourced to 2026-09-07 news report**, not claimed as first-party extraction.
- Every machine-readable record has a URL, evidence class, unit, period, and explicit `core_exact_eligibility=NO`.
- Research-only import: **28 rows**, **0 canonical additions**, no workbook edits, no CI/Actions acceptance claimed.
