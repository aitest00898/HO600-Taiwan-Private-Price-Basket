# HO600 — Batch 9 C04 working research (2026-10-16)

**Status:** WIP, **NOT** a checkpoint PASS, **NOT** a canonical workbook release. Work on `research/batch-09` only.

## Unchanged source-of-truth boundary

- Canonical `main`: Batch 8, **181/600**, remaining 419, candidate 418, evidence 1,566, Basket NOT SEALED, Index LOCKED.
- C01/C02/C03: 20/20/20 **research ADMISSIBLE**, cumulative **60**; these ledgers are not revised.
- C04 WIP: **2 leads**, of which **1 PROVISIONAL_ADMISSIBLE** and **1 HOLD**. **Zero C04 checkpoint-certified new rows**. DO NOT call this 61 or 62 fully certified research rows, or 182/600 canonical.
- Workflow correction: two C04 WIP pushes **automatically triggered** `Validate HO600` via the existing push workflow, even though nobody manually invoked Actions. They completed `success` (run IDs `38815794034` and `38815800007`). The research branch workflow was subsequently changed in commit `c3e292a28668ba5a5d40140afd028bd97f8c7244` to **manual-only** `workflow_dispatch`. Immediately after that commit, the checked run list showed no run for the guard commit. Do not dispatch it. The `main` workflow remains unchanged and can auto-trigger on future pushes/PRs; preserve the user's global Actions pause.
- Visibility audit: live GitHub repository metadata reports `visibility=public` on 2026-10-16, despite the 2026-10-16 previous handoff labeling the repository `private`. Confirm intended visibility separately; no visibility setting changed in this research run.
- No `main` mutation and no canonical workbook change.

## C04 lead table

| ID | Class | 2020 → 2026 (TWD) | Current decision | Rationale |
| --- | --- | --- | --- | --- |
| B09-C04-001 | 日常／個人 / 保養／化妝 | 39 → 39 | PROVISIONAL_ADMISSIBLE, comparability B | Dated 2020 MUJI first-party price and contemporaneous descriptive identification match 2026 MUJI product/function and normal price; historical barcode and dimensions absent |
| B09-C04-002 | 衣 / 包袋／配件 | 79 → 89 | HOLD_2020_IN_MARKET | 2020 official price was disclosed with **planned June launch**; need contemporaneous proof of retail normal price after actual release and current A3 variant continuity |

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
