# HO600 — Batch 9 C04 working research (2026-10-16)

**Status:** WIP, **NOT** a checkpoint PASS, **NOT** a canonical workbook release. Work on `research/batch-09` only.

## Unchanged source-of-truth boundary

- Canonical `main`: Batch 8, **181/600**, remaining 419, candidate 418, evidence 1,566, Basket NOT SEALED, Index LOCKED.
- C01/C02/C03: 20/20/20 **research ADMISSIBLE**, cumulative **60**; these ledgers are not revised.
- C04 WIP: **4 leads**, of which **1 PROVISIONAL_ADMISSIBLE** and **3 HOLD** (B09-C04-003/004 added 2026-10-26). **Zero C04 checkpoint-certified new rows**. DO NOT call this 61 or 62 fully certified research rows, or 182/600 canonical.
- Workflow correction: two C04 WIP pushes **automatically triggered** `Validate HO600` via the existing push workflow, even though nobody manually invoked Actions. They completed `success` (run IDs `38815794034` and `38815800007`). The research branch workflow was subsequently changed in commit `c3e292a28668ba5a5d40140afd028bd97f8c7244` to **manual-only** `workflow_dispatch`. Immediately after that commit, the checked run list showed no run for the guard commit. Do not dispatch it. The `main` workflow remains unchanged and can auto-trigger on future pushes/PRs; preserve the user's global Actions pause.
- Visibility audit: live GitHub repository metadata reports `visibility=public` on 2026-10-16, despite the 2026-10-16 previous handoff labeling the repository `private`. Confirm intended visibility separately; no visibility setting changed in this research run.
- No `main` mutation and no canonical workbook change.

## C04 lead table

| ID | Class | 2020 → 2026 (TWD) | Current decision | Rationale |
| --- | --- | --- | --- | --- |
| B09-C04-001 | 日常／個人 / 保養／化妝 | 39 → 39 | PROVISIONAL_ADMISSIBLE, comparability B | Dated 2020 MUJI first-party price and contemporaneous descriptive identification match 2026 MUJI product/function and normal price; historical barcode and dimensions absent |
| B09-C04-002 | 衣 / 包袋／配件 | 79 → 89 | HOLD_2020_IN_MARKET | 2020 official price was disclosed with **planned June launch**; need contemporaneous proof of retail normal price after actual release and current A3 variant continuity |
| B09-C04-003 | 食 / 超市／自煮基礎食品 | 93 → 93 (both list/nonpromotion benchmark) | HOLD_FIXED_CHANNEL_AND_SKU | 2020 FamilyMart standard one-bottle price and 2026 Wanjiafu regular/struck-through list price agree; not same channel, and 2020 barcode not independently confirmed. Do not confuse 2026 NT$88 sale price with NT$93 ordinary reference. |
| B09-C04-004 | 日常／個人 / 盥洗／衛生用品 | 149 → 149 (listed **original** prices, NOT current discounted checkout) | HOLD_2020_ARCHIVE_AND_SKU | 2020-era original COSMED flyer index says Whisper liquid-material 34cm/10pcs original NT$149; 2026 COSMED eShop index says 34cm/10pcs original 149 vs promo 129. Archived first-party PDF now redirects and cannot be visually rechecked; exact dated issue and historical SKU/packaging unresolved. |

### Evidence directly retrieved 2026-10-16

1. B09-C04-001 Exact-2020 first-party Taiwan article, dated **2020-06-29**: <https://shop.muji.tw/muji-journal/news/news/200629.html> — **洗臉用網狀起泡網 39元**; fine-mesh foaming net. 2026 live official retail: <https://shop.muji.tw/SalePage/Index/8919853?lang=zh-TW> — **NT$39**, polyethylene, ~21cm, barcode 4550182045031. Semantically the same identified product purpose, but historical article lacks barcode/size: **B lineage**, not proven exact barcode.
2. B09-C04-002 Exact-2020 dated official advance announcement **2020-03-06**: <https://shop.muji.tw/muji-journal/news/news/200306.html> — B5 / A4 / A3 59 / 69 / 79, with explicit **新品預計6月上市**. 2026 live official catalog <https://shop.muji.tw/v2/official/SalePageCategory/483062> — **黃麻購物袋原色A3 $89**. 2023 official historical price-adjustment <https://shop.muji.tw/muji-journal/news/news/230302.html> notes jute family 49–79 to 59–89 (not SKU-specific 2020 price proof). 2022 official <https://shop.muji.tw/muji-journal/news/news/221229.html> notes jute A3 among family with 49–79 range (not 2020 proof). Hence HOLD.

### Duplicate avoidance: caught before creating C04 rows

- `LEG-EC-156` **原色化妝棉180入 79→110** and `LEG-EC-161` **壓邊化妝棉189入 79→110** already exist in the canonical prequalified Exact data, as independently checked against both `Candidate_Pool.csv` and `Evidence.csv`. They are **not new C04 concepts**.
- Search of `Candidate_Pool.csv`, all C01–C03 ledgers, and `Evidence.csv` found no matching economic concept name for the two C04 leads. **Name-only nonduplicate is not a full semantic/group audit**.
- **A4 jute bag** also has plausible 69→79 official sources, but one independent 2020 article displays a conflicting image caption mapping size/prices, and the 2026 official category lists A4 under **sold out**. It is **not** a C04 admitted concept; verify before pursuing. Sources: <https://shop.muji.tw/muji-journal/news/news/200306.html>, <https://www.vogue.com.tw/lifestyle/article/muji-2020-ss>, <https://shop.muji.tw/SalePage/Index/11966875>.

### Concentration / quota preflight

- Canonical `Quota_Control.csv`: 日常／個人/保養／化妝 prequalified **2**, target **10**; 衣/包袋／配件 prequalified **1**, target **8**. C02 already added **MUJI backpack** in this clothing subcategory. C04 WIP does not overfill either.
- MUJI research admissions before C04 = **2** (C02 MUJI shoes + backpack). If C04-001 survives checkpoint QC, projected **3 ≤ 8**. If A3 later also survives, projected **4 ≤ 8**. Legacy excess caps still checked at release.
- The 2020 face-net URL also has a canonical legacy usage for an **unrelated cotton pad**; historical source concentration across canonical + new additions needs full recalculation. Current WIP alone does not prove entire-policy PASS.
- `PROVISIONAL_ADMISSIBLE` and `HOLD_2020_IN_MARKET` are working-sheet dispositions, **not** canonical or final QC decisions.

## Next operator execution order

1. Prioritize a dated **after-June-2020** original price for MUJI A3 jute (or keep HOLD); verify A3 historical size and normal-price semantics. Resolve face-net historical material/size/barcode or retain B with explicit reviewer justification.
2. Return to **197 legacy `RESEARCHABLE-CURRENT-ONLY` candidates** before adding unrelated new concepts. Especially clothes other than UNIQLO, household cleaning/bedding, private parking/vehicle upkeep, childcare/language, grooming, pets, grocery/packaged goods. Do not resurrect frozen quota cells or reuse already admitted economic concepts.
3. Gather independently traceable 2020/2026 normal price pairs and maintain dated in-source evidence. Reject promotional/starting price, branch drift, and retrospective 2021 reports masquerading as 2020 originals.
4. Only after roughly 20–25 checked clean C04 concepts, compile `checkpoint-04-ledger.csv` / `checkpoint-04.md` and run full quota, normalized group/brand/source/family concentration, semantic duplicate, identity/spec/channel, and original-source QC. Until then C04 remains WIP.
5. Do not touch `main`, the seven-sheet formal workbook, the canonical status, seal state, index, or GitHub Actions without explicit validated release workflow.

Source-of-truth: `research/batch-09/HANDOFF-2026-10-16.md`, `docs/evidence-gate.md`, `docs/concentration-policy.md`, `data/Quota_Control.csv` and canonical `main` artifacts.


## 2026-10-22 independent cross-year recheck — A3 remains HOLD

1. Official [MUJI 2020-03-06 spring/summer new-products statement](https://shop.muji.tw/muji-journal/news/news/200306.html) says A3 黄麻袋 original NT$79 and explicitly **「新品預計6月上市」**, *not actual on-sale confirmation*.
2. [Girlstalk 2021-05-21 retrospective](https://www.girlstalk.cc/article/72391) describes the three sizes B5/A4/A3 at 59/69/79 and says **「近期台灣也悄悄上市啦」**. This is a **2021 dated secondary report of available goods**, and **does not certify 2020 introduction date**. Relative language 「近期」 cannot be backdated to June 2020.
3. [Vogue Taiwan 2020 spring/summer](https://www.vogue.com.tw/lifestyle/article/muji-2020-ss) also says **預計於6月上市** and contains an internally ambiguous image-caption mapping of B5/A4/A3 to 79/69/59. Prioritize the dated official text for *planned* sizes/prices, but do not infer actual 2020 store distribution.
4. Current [MUJI category](https://shop.muji.tw/v2/official/SalePageCategory/483062) lists an A3 jute bag at NT$89, with another A3 listing sold out; variant continuity/barcode still lacks 2020 contemporaneous identity evidence.

**Disposition (no change): `B09-C04-002 = HOLD_2020_IN_MARKET`**, C04 checkpoint PASS = 0/20, Batch9 previous 60 PASS unchanged, canonical 181/600. The exact missing evidence is (a) **after launch** in-year 2020 Taiwanese first-party in-store/on-sale material (not just an announcement), (b) A3 model/color/specimen parity with the current retail unit, and (c) observed 2020 **normal selling** price. Do not reclassify from this 2021 secondary article alone.

## 2026-10-26 supplementary first-party retail lead — date unverified

An additional search-indexed **MUJI Taiwan official Facebook post** was located under the page `muji.tw`, post numeric ID `3499166323460790`, headed **「【#新品上市】黃麻購物袋全門市販售中！」**. Its indexed text says that the jute shopping bags are available in all stores and lists B5/A4/A3 sizes with prices 59/69/**79** TWD. This is a **first-party on-sale assertion**, a different type of evidence from the previously cited 2020-03-06 *planned* launch announcement.

**Limitations (critical):** the search result does **not** expose a verifiable original posting date, and the Facebook post body could not be directly loaded for independent inspection. It therefore **does not prove availability during calendar 2020**. The 2020 A3 SKU/barcode and continuity with the current 2026 A3 (89 TWD) remain unverified. Do not infer a 2020 date from the Facebook numeric post ID or from later articles. The indexed first-party claim is a **lead requiring original post timestamp and identity corroboration**, not an accepted historic price observation.

Source locator (exact indexed original): https://www.facebook.com/muji.tw/posts/%E6%96%B0%E5%93%81%E4%B8%8A%E5%B8%82%E9%BB%83%E9%BA%BB%E8%B3%BC%E7%89%A9%E8%A2%8B-%E5%85%A8%E9%96%80%E5%B8%82%E8%B2%A9%E5%94%AE%E4%B8%AD-%E9%80%99%E5%B9%BE%E5%A4%A9%E5%9C%A8%E9%96%80%E5%B8%82%E6%98%AF%E5%90%A6%E7%9C%8B%E5%88%B0%E9%80%99%E6%AC%BE%E6%96%B0%E5%93%81%E5%91%A2-%E9%BB%83%E9%BA%BB%E5%8F%AF%E5%90%B8%E9%99%84%E4%BA%8C%E6%B0%A7%E5%8C%96%E7%A2%B3%E8%83%BD%E8%87%AA%E7%84%B6%E5%88%86%E8%A7%A3%E6%96%BC%E5%9C%9F%E5%A3%A4%E6%98%AF%E4%B8%80%E6%AC%BE%E5%B0%8D%E7%92%B0%E5%A2%83%E5%8F%8B%E5%96%84%E7%9A%84%E7%B4%A0%E6%9D%90%E6%88%91%E5%80%91%E5%B0%87%E9%BB%83%E9%BA%BB%E4%BB%A5%E6%A8%B8%E8%B3%AA%E5%B7%A5%E6%B3%95%E8%A3%BD%E6%88%90-%E9%BB%83%E9%BA%BB%E8%B3%BC%E7%89%A9%E8%A2%8B%E6%9D%90/3499166323460790/

**Disposition unchanged:** `B09-C04-002 = HOLD_2020_IN_MARKET`; C04 certified 0/20; C01–C03 research 60; `main` 181/600, Index LOCKED. No existing research evidence, price, or Gate is overwritten.


## 2026-10-26 direct evidence improvement — contemporaneous 2020 on-sale report

A newly located, **independently indexed 2020-09-21 publication** from **POPBEE**, [「在日本一袋難求……MUJI 超熱銷麻布手袋，台灣正式發售！」](https://popbee.com/accessories/handbags/muji-jute-shopping-bag-tote-bag-taiwan-release), says at the time of reporting that the MUJI undyed jute tote was **actually for sale in Taiwan in physical stores and on the official website**, with listed sizes B5/A4/A3 and ordinary published prices **NT$59 / NT$69 / NT$79** respectively. The web search record explicitly dates it **Sep 21, 2020**; the currently extracted article body lacks an inline standalone publication date, so retain the distinction between *indexed metadata date* and *article text* (which itself describes actual retail stock and price). This is a contemporaneous **secondary** retailer-observation report, not a later 2021 retrospective or a first-party MUJI sales receipt.

Evidence triangulation for B09-C04-002:

1. **Primary 2020 planned announcement**: [MUJI Taiwan 2020-03-06](https://shop.muji.tw/muji-journal/news/news/200306.html) identifies **A3 undyed jute bag NT$79**, the plain yellow-jute textile with cotton handle, and planned June launch. This alone does not prove sale.
2. **Independent contemporaneous on-sale report**: [POPBEE, indexed 2020-09-21](https://popbee.com/accessories/handbags/muji-jute-shopping-bag-tote-bag-taiwan-release) explicitly asserts 2020 actual Taiwan in-store/online availability of A3 **NT$79**. **Important evidence gain**: actual 2020 market presence is now corroborated at secondary-source level, substantially narrowing the previous launch-date blocker. The previously identified 2021 Girlstalk relative phrase is not used to backdate the 2020 launch.
3. **Contemporary current primary normal-price reference**: [MUJI Taiwan current category](https://shop.muji.tw/v2/official/SalePageCategory/483062) lists **黃麻購物袋原色A3 NT$89** as one live listing, *and* a separate **黃麻購物袋A3原色 NT$89** sold-out listing. [The separate product page](https://shop.muji.tw/SalePage/Index/11559259) describes the sold-out listing with article code **EG0DRA6S**, barcode **4548076173687**, jute body/cotton handle, India manufacture and NT$89; this barcode is **2026-side only** and **not** a 2020 identity proof. Avoid conflating the two 2026 listings.
4. The [MUJI 2022 official sales report](https://shop.muji.tw/muji-journal/news/news/221229.html) describes A3 in the jute bag line and the line's 49–79 TWD range; [2023 official product pricing](https://shop.muji.tw/muji-journal/news/news/231227.html) confirms 59–89 across the family; these support product-family trajectory but not 2020 SKU-level identity or A3 price independently.

**Updated research interpretation:** “No 2020 on-sale evidence at all” is no longer accurate; the 2020 on-sale report is **evidence found (secondary, dated by search index)**. But the existing strict C04 working disposition stays **`HOLD_2020_IN_MARKET` for compatibility** because **(i)** first-party dated actual on-sale proof has not been authenticated, **(ii)** the 2020 A3 barcode, model and dimensions have not been linked to a particular 2026 live listing, and **(iii)** final brand/source/semantic duplicate and concentration QC has not run. Do **not** turn secondary corroboration into an Exact-A admission, or treat planned March 2020 price as proven checkout transaction. Candidate remains B-lineage, **0 additional C04 checkpoint-certified rows**; previous **60** Batch-9 research PASS and main **181/600, NOT SEALED, LOCKED** unchanged.

**Next evidence that could change disposition (not a new Gate):** original timestamp and text of [MUJI Taiwan's first-party “全門市販售中” Facebook post](https://www.facebook.com/muji.tw/posts/3499166323460790/), or a dated post-June-2020 MUJI store/catalog product record; pair its A3 model/spec to the specific currently buyable A3 listing before full C04 QC. If unavailable, stop retrying this identical blocker and switch to other underfilled legacy candidates.


## 2026-10-26 legacy food candidate — B09-C04-003 (LEG-EC-311)

**Target reused (not a new invented concept):** canonical `main/data/Candidate_Pool.csv` `LEG-EC-311`, 光泉全脂鮮乳 936ml, `RESEARCHABLE-CURRENT-ONLY`, 食／超市／自煮基礎食品 (baseline 1/34; 33 missing). In `main/data/Evidence.csv`, the same candidate has already been recorded with a 2026 **NT$93** source from 萬家福, and **NT$88** from 全聯, but **no 2020 observation**. The research concept therefore reuses its ID rather than creating a second price-basket item.

**New 2020 original observation:** [班班美食生活圈, publication visibly dated **2020-04-08**](https://benlife.tw/20200408famimartnew/), contemporaneous published coverage of FamilyMart's 04/08–05/05 retail campaign, explicitly specifies **「光泉 全脂/低脂鮮乳936ML (原價93元，特價任選兩件169元)」**. The **2020 normal single-unit reference is NT$93**: the multi-buy promotion **NT$169/2 must not be entered** as a normal-price observation. Source is an independent dated secondary report of an operator promotion, **not first-party archived FamilyMart tariff/list**. The source groups full-fat and low-fat products; only the stated full-fat SKU concept is considered here.

**2026 current corroboration:**
- The [Wanjiafu / Uni-Prosperity live merchant product page](https://online.uni-prosperity.com.tw/zh/%E5%85%89%E6%B3%89/1501003300101.html) names **光泉100%純全脂鮮乳(無調整) 936ml**, shows **NT$93 crossed-out/list reference** and **NT$88 actual promotional selling price**. For a comparison of regular/reference prices, use **93** only, recording the active **88** discount as excluded; do **not** claim NT$93 is its payable 2026 checkout price. Official indexed [Taiwan GreenPoint product entry](https://sys.greenpoint.org.tw/GpConsumerApp/Function/CommodityMgt/Edit.aspx?SystemId=76ce91a4-4b09-40e2-a125-e70a6240322e), when searchable, additionally shows barcode **4710105010113**, product 936ml and **recommended price NT$93**, with program listing period 2023-10-01 to 2030-12-31; the GreenPoint direct open gives HTTP **403**, so this is *search-indexed supplementary metadata*, **not directly fetched first-party evidence**.
- [FamilyMart's currently indexed 2026 official eligible-products list](https://500.gov.tw/registrant/intro/vendor-1.html) includes 光泉全脂鮮乳936ml, establishing item availability but **does not state a 2026 normal selling price at FamilyMart**.
- The original **2020 label “全脂鮮乳”** and current **“100%純全脂鮮乳(無調整)”** need 2020 barcode, formulation and packaging continuity check; numeric volume/brand alone are not proof of same SKU.

**Disposition: `HOLD_FIXED_CHANNEL_AND_SKU`, comparability B provisional, evidence 2020 = secondary dated non-sale-price (B), evidence 2026 = direct merchant price with explicitly excluded discount (A).** The source pair **93 → 93** is a useful cross-channel *reference-price lead only*, **not** a verified fixed-channel historic basket pair. Missing old-channel FamilyMart 2026 normal price or 2020 Wanjiafu normal price, and source of 2020 barcode. If the source/channel mismatch cannot be resolved, retain HOLD rather than promote. Check identity, concentration quotas and duplicate semantics as part of existing C04 QC, no new Gate.

**Counts:** C04 WIP now **3 leads** (1 provisional, 2 HOLD); **C04 checkpoint PASS 0/20**; C01–C03 **60 research PASS**; `main` **181/600**, basket **NOT SEALED**, index **LOCKED**. No canonical workbook or GitHub Actions change.


## 2026-10-26 C04-003 same-merchant bridging evidence: FamilyMart 2024 retail standard price

**Target:** B09-C04-003 = existing `LEG-EC-311`, 光泉全脂鮮乳 936ml. Evidence improvement **without adding a new candidate**, revising the existing cross-channel 2020↔2026 benchmark, or promoting HOLD.

1. **2020 FamilyMart standard retail reference — NT$93:** [班班 2020-04-08 contemporaneous record](https://benlife.tw/20200408famimartnew/), in-page dated **2020.04.08**, explicitly reports brand/whole-fat/936ml, original one-bottle NT$93, two-bottle promotional NT$169. The promotional two-pack is excluded.
2. **2024 *same retailer* FamilyMart standard retail reference — NT$100:** [onelife archived FamilyMart 2024-03-20–2024-04-16 breakfast campaign](https://onelife.tw/a/20391), explicitly lists 光泉全脂鮮乳936ml **原價100元/瓶** in its FamilyMart pairing promotion, distinct from the discounted bundle **109元** with artisan toast. This is a contemporaneous secondary report, with in-page campaign start/end dates, so it **only supports price in 2024**, not directly 2026.
3. **2026 FamilyMart merchant on *delivery platform* — NT$100 listed checkout price (separate channel):** [Uber Eats indexed FamilyMart catalogue (三重新運店)](https://www.ubereats.com/tw/brand-city/sanchong-nwt/family-mart) shows 光泉全脂鮮乳936ml **NT$100** in the indexed catalogue. The dynamic page redirects to Uber Eats landing when opened without location/session; therefore this is **search-indexed, not directly inspected in-browser** and delivery pricing **may differ from FamilyMart in-store**. Do **not** describe it as a verified FamilyMart 2026 walk-in normal shelf price or replace the existing cross-channel 2026 WanJiaFu NT$93 evidence.
4. **Independent first-party product availability at current FamilyMart, no price:** [FamilyMart cross-store redemption product table](https://nevent.family.com.tw/Preorder/EA/) explicitly lists 光泉全脂鮮乳936ml and the separate low-fat variety; source dynamically updated and **undated**, so it supports family/item presence but not its 2026 price and not old-to-new UPC continuity.

**Evidence-bound interpretation:** 2020 `FamilyMart in-store original NT$93` versus 2024 `FamilyMart in-store original NT$100` is a genuine within-retailer time-bridge (2020→2024), with 2026 FamilyMart delivery listing also at NT$100 as *supplemental* support. **Do not calculate or publish an official 2020→2026 93→100 price change** until 2026 walk-in ordinary-price proof and 2020 UPC identity/spec continuity are independently established. Original `B09-C04-003` ledger 2020→2026 `93→93` continues to represent *different-retailer reference prices* (2020 FamilyMart / 2026 Wanjiafu), **not** an admitted consistent-channel price observation.

**Existing disposition unchanged:** `HOLD_FIXED_CHANNEL_AND_SKU`, comparability B provisional, no C04 checkpoint admission and no new formal Exact. Both the new 2024 retail evidence and 2026 third-party delivery index explicitly retain their evidence quality limits; no third-party marketplace or purchase coupon used as a normal store price. After this bridge, stop probing this specific unresolved price proof without distinct primary evidence; return to other price-change-blind underfilled legacy candidates.


## 2026-10-26 legacy hygiene candidate — B09-C04-004 (LEG-EC-164)

**Selected BEFORE looking at price change** from 197 existing `RESEARCHABLE-CURRENT-ONLY` concepts by uncovered quota: `main/data/Candidate_Pool.csv` `LEG-EC-164`, 日常／個人／盥洗／衛生用品, 好自在經典款液體衛生棉34cm 10片, current canonical item source `POYA 9950671`. The baseline subcategory is only **1/14** Exact (13 unfilled); one current 2026 POYA price **149** already exists twice as source-role bookkeeping in `main/data/Evidence.csv`. This is the **same pre-existing economic concept**, not a new fourth economic item beyond the WIP lead.

### Indexed first-party price observations — both explicitly normal/list price

1. **Historic COSMED first-party flyer indexed as circa 2020, but primary PDF NOT recoverable:** [COSMED official archived catalogue `upload/ebook/23/pdf/0706.pdf`](https://www.cosmed.com.tw/upload/ebook/23/pdf/0706.pdf) is surfaced by public search indexing as published **around 6.3 years before 2026-10**, with the exact group **「好自在液體材質衛生棉 24cm10片／27cm10片／34cm10片」**, and says **「原價$149、任選三件$258」**. The historical **normal one-pack reference is NT$149**; **$258/3 is a multi-buy promotion and excluded**. **Critical retrieval limit:** opening the original URL redirects to current `https://www.cosmed.com.tw/index.aspx` (web fetched **HTML, not the old PDF**). Hence the indexed excerpt (not a directly inspected or screenshot-verified original PDF page) is the only evidence currently accessible here. The original campaign date is **not verified**; path `0706` must **not** be converted into an invented 2020-07-06 date. Archive origin/type and approx. year are indexed leads, not direct archival certification.
2. **Current 2026 COSMED original/list price, separate from discount:** COSMED's [official online `好自在夜用` product category](https://shop.cosmed.com.tw/tagCategory/%E5%A5%BD%E8%87%AA%E5%9C%A8%2C%E5%A4%9C%E7%94%A8) and [current COSMED merchandising list](https://shop.cosmed.com.tw/v2/official/SalePageCategory/464744) are indexed with **「whisper好自在 液體材質衛生棉34cm10片（包裝隨機出貨）」, original NT$149, promotion NT$129**. The web-extracted live page is client-rendered (brief iframe/empty main text), so this is a first-party site with a **search-indexed price**, not a direct in-page commerce/checkout verification. **Exclude the NT$129 discount.**
3. **Independent 2026 normal reference on a second retailer, already captured:** `main/data/Evidence.csv` for LEG-EC-164 points to POYA [official product `9950671`](https://www.poyabuy.com.tw/SalePage/Index/9950671?lang=zh-TW) at **NT$149**. This independently corroborates the product family's current original/reference price but does **not** fill the missing 2020 SKU or prove retailer parity.
4. **Bridge, not a new 2020 quote:** [2025-10 COSMED official digital flyer, search-indexed](https://www.cosmed.com.tw/upload/ebook/119/pdf/2025_10.pdf), still shows original 149 for 24/27/34cm, single 129 and two for 219. Same original domain currently redirects on click; 2025 evidence is not substituted for 2020.

**Disposition: `HOLD_2020_ARCHIVE_AND_SKU`.** 2020 observation is **first-party-hosted document *indexed only*** with unverified original issue date / page; current 2026 COSMED site is **first-party indexed, dynamic page not inspected**. The label/length/unit (liquid 34cm/10pcs) is consistent at a *product-family* level, but 2020 vs 2026 barcode, material variation, packaging ("經典款" vs "液體材質"; current pack randomized), COSMED offline-store vs eShop channel and normal-price meaning all require the **existing** source/identity/retailer QC. **No claim that the old PDF was opened, screenshotted, or confirmed to show the exact item**, no Exact A, no price increase inference from promotional discounts. This is a *candidate* with a promising same-retailer-brand list-price trail, not a certified 2020/2026 observation.

**Next concrete evidence to change this decision (no added gate):** obtain readable archived 2020 COSMED flyer page with original issue date or a dated original 2020 COSMED listing, and independently link the 2020 34cm10pcs pack identity to current COSMED eShop item; otherwise leave HOLD and move to another underfilled older-current candidate. Do not retry this same redirect twice without a different original URL.

**Counts unchanged at release boundary:** C04 **4 WIP leads = 1 provisional + 3 HOLD**, C04 checkpoint-certified **0**, C01–C03 **60 research-qualified**, `main` **181/600**, NOT SEALED, LOCKED. Mac Dashboard accepted; iPhone acceptance postponed by user, unrelated to price evidence.
