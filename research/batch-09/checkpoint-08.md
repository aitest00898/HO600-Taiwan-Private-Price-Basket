# HO600 Batch 9 — C08 checkpoint receipt

Date: 2026-10-30  | Branch: `research/batch-09`  | Fixed ledger: [checkpoint-08-ledger.csv](./checkpoint-08-ledger.csv)

## Decision and scope

**CHECKPOINT-08 = PASS_RESEARCH_ONLY_WITH_EVIDENCE_LIMITATIONS (20/20).** Each row is an admissible research comparison of published/listed prices; none is POS proof, formal Exact admission, a representative Taiwan-wide household sample, or a HO600 index result.

| IDs | Concept group | 2020 → 2026 NT$ | Evidence boundary |
|---|---|---:|---|
| 001 | T-UP Wanhua adult weekday starlight admission plus shoe rental | 330 → 420 | 2020 visitor report vs 2026 official split tariff; same-address service comparison, but 2020 time window is not stated. |
| 002 | Ambassador Taipei Changchun standard full ticket | 310 → 320 | Branch-specific official 2020 notice/rate image vs current branch table; 2020 screening format is not explicit. |
| 003–004 | MORE FIT Shida and Fit Plant single-entry gym visits | 150 → 200; 150 → 150 | Public price observations; exact Fit Plant branch/time scope is not established. |
| 005–007 | Three PC Steam games | 438 → 438; 590 → 590; 349 → 378 | Dated 2020 media reports vs current Taiwan Steam API list prices; no purchase receipts. |
| 008–013 | Six HUCC products: two rices, pickled cucumber, grass tea, tilapia and skin-on tilapia | 240 → 280; 295 → 295; 65 → 85; 155 → 155; 100 → 115; 100 → 115 | Official 2020 weekly bulletin vs current official HUCC product listings. Promo prices are excluded. One historic PDF supports all six rows (source cap reached). Fish barcode/producer continuity is not established; grass tea has seasonal availability limits. |
| 014–015 | Kuokuang 1826 and UBus 1620 full three-row Taipei–Taichung fares | 300 → 334; 300 → 337 | 2020 dated fare comparison vs current official TaiwanBus route tables. Full fares are separated from promotional/time fares. |
| 016–017 | THSRC Taichung P1 parking hourly rate and daily cap | 40 → 50 per hour; 240 → 350 per day | Official 2020 THSRC rate notice vs current Taichung station page. These are two units for the same P1 site/family; the daily cap is not an observed daily payment. They backfill current-only Candidate Pool LEG-EC-042 and LEG-EC-041, respectively. |
| 018 | Banqiao Mega City ordinary parking hourly price | 60 → 60 | 2020 article groups four Far Eastern branches; 2026 official mall rate is branch-specific, so historical evidence is B-level. |
| 019 | Yoga Planter CAY 90-minute group class, one class | 550 → 550 | Owner-published schedules; instructor and class duration align, exact venue continuity does not. Current November–December price is used; October price and packages are excluded. |
| 020 | GiveLi Da-Fang gym base minute rate | 1 → 1.5 per minute | 2020 third-party visit and current business listing; registration fee and cheaper bulk top-ups are excluded. Neither is a POS receipt. |

## Receipt and concentration audit

The C08 source register has 33 receipt rows: all 33 report HTTP 200 and strict TLS validation. Twenty-eight captured response bodies are stored under [`source-captures/2026-10-30/C08`](./source-captures/2026-10-30/C08) and independently hash-matched to their receipt SHA-256. The other five receipt rows remain hash-only records without retained bodies; their source-note limitations are retained.

The 2020 HUCC PDF was downloaded with strict TLS, SHA-256 recorded and its first three pages checked visually and by text extraction. The bulletin distinguishes standard and promotional amounts; only standard/list prices are used. Full-page details and URLs are in the WIP ledger and receipt register. The single HUCC PDF is used exactly six times, at the source cap. The Fit Plant historical PTT URL also reaches six uses, so neither source is available for further additions.

The P1 hourly and daily-cap concepts share a product family, recorded as variants 1 and 2. All fixed rows have positive prices and HTTPS source fields. C08 concepts were checked against the existing Candidate Pool and C01–C07 ledgers; the only canonical candidates directly backfilled in this set are the two disclosed P1 current-only concepts.

C08 fixed IDs are 20 unique `ADMISSIBLE` rows. Across C01–C08, 160 fixed IDs are unique; maximum grouped concentration is 8 per merchant, 5 per merchant/subcategory and 6 per exact 2020 source URL. C01–C05 remain 100; the C06–C08 additions make the user’s C04–C08 additional-100 objective 100/100 at research level. Formal main remains 181/600, Basket `NOT SEALED`, Index `LOCKED`.

See [C08 WIP evidence log](./checkpoint-08-wip.md) and [source receipt register](./checkpoint-08-source-receipts-2026-10-30.csv). The primary official current sources include the [HUCC product catalogue](https://collection.hucc-coop.tw/), [TaiwanBus route 1826](https://www.taiwanbus.tw/eBUSPage/json/TMSQuery.aspx?app=true&routedata=182601), [TaiwanBus route 1620](https://www.taiwanbus.tw/eBUSPage/json/TMSQuery.aspx?app=true&routedata=162001), and [THSRC Taichung station parking rates](https://www.thsrc.com.tw/ArticleContent/3301e395-46b8-47aa-aa37-139e15708779).
