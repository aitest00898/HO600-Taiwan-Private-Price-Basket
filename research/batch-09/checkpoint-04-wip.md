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
