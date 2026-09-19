# Batch 9 — Internal QC Checkpoint 02

**Canonical impact: NONE.**

Formal status remains **Batch 8 / 181 / 600**. This checkpoint is research-only and must not be reported as canonical progress.

Structured row-level ledger:

- [checkpoint-02-ledger.csv](./checkpoint-02-ledger.csv)

## Checkpoint-02 final composition

| Domain / surface | Count | Research state |
|---|---:|---|
| Clothing — MUJI | 2 | ADMISSIBLE at research level; comparability B |
| Clothing — UNIQLO | 8 | ADMISSIBLE at research level; **brand new-admission cap reached → FREEZE NEW** |
| Daily/personal — 7-ELEVEN ibon color print | 1 | ADMISSIBLE; ibon print family reaches 2 variants with checkpoint-01 B/W → **FREEZE print family** |
| Daily/personal — Hami Book monthly reading package | 1 | ADMISSIBLE; A/A evidence, comparability B because content library changes |
| Education — Hahow exact-title courses | 5 | ADMISSIBLE; **brand × online-learning cap reached → FREEZE NEW** |
| Leisure — MyVideo / friDay Video / KKBOX | 3 | ADMISSIBLE; exactly fills the canonical streaming shortfall |
| **Total** | **20** | **internal QC only** |

## Important post-write corrections

The initially committed checkpoint-02 ledger was deliberately re-audited after write-back. The following corrections were made before this checkpoint was finalized:

1. **Removed the UNIQLO wireless-bra row.** The first current source was a 2024 collection page, not a defensible Exact-2026 price observation.
2. Replaced it with **UNIQLO HEATTECH printed scarf**, using a dated 2020 official price (NT$490) and an explicit 26FW official price (NT$590).
3. Corrected the current URL for **Hahow「戶外攝影實戰：用鏡頭看見台灣」** to the exact current LINE Shopping item.
4. Reduced streaming subscriptions from six proposed rows to three. The canonical subcategory was already **7 / 10**, so six additions would have structurally overfilled it to 13 / 10.
5. Removed GagaOOLala, LiTV, and CATCHPLAY+ from this checkpoint's admissible set even though their individual price evidence was usable.
6. Filled the three released slots with:
   - Hami書城月讀包 149 → 149;
   - UNIQLO 喀什米爾圓領毛衣 2,990 → 2,990;
   - UNIQLO HEATTECH針織毛帽系列 390 → 390.
7. Normalized concentration-count semantics. The ledger counts **Batch-9 new admissions**, matching the formal concentration policy; it does not add legacy canonical holdings to the new-admission cap.

## Combined Batch-9 state after checkpoint-02

Checkpoint-01: **20**

Checkpoint-02: **20**

Cumulative research-level admissible set: **40 concepts**

This is **not** formal 221 / 600. Formal progress stays 181 / 600.

Cumulative research additions by domain:

| Domain | Batch-9 research additions through C02 |
|---|---:|
| 衣 | 10 |
| 住／家用 | 5 |
| 育 | 10 |
| 樂 | 3 |
| 日常／個人 | 12 |
| 食 | 0 |
| 行 | 0 |
| **Total** | **40** |

## Structural quota projection

If all 40 research rows later survive canonical admission, the affected subcategories project as follows:

| Domain | Subcategory | Canonical Exact | Batch-9 add | Projected | Legacy-preserving target |
|---|---|---:|---:|---:|---:|
| 衣 | 上衣 | 1 | 4 | 5 | 11 |
| 衣 | 鞋 | 1 | 1 | 2 | 11 |
| 衣 | 外套 | 0 | 1 | 1 | 8 |
| 衣 | 包袋／配件 | 1 | 3 | 4 | 8 |
| 衣 | 機能／運動服飾 | 0 | 1 | 1 | 10 |
| 住／家用 | 網路／通訊固定服務 | 0 | 5 | 5 | 11 |
| 育 | 文具 | 1 | 5 | 6 | 10 |
| 育 | 線上學習 | 0 | 5 | 5 | 8 |
| 樂 | 串流影音／音樂 | 7 | 3 | **10** | **10** |
| 日常／個人 | 個人數位／會員服務 | 1 | 7 | **8** | **8** |
| 日常／個人 | 其他日常服務 | 0 | 5 | 5 | 7 |

**Overshoot count: 0.**

From checkpoint-03 onward:

- `樂 / 串流影音／音樂` → **FREEZE NEW**
- `日常／個人 / 個人數位／會員服務` → **FREEZE NEW**

## Concentration QC

Combined checkpoint-01 + checkpoint-02 research set:

- UNIQLO new admissions = **8 / 8** → **FREEZE NEW**
- PILOT × 文具 = **5 / 5** → **FREEZE NEW**
- 中華電信 × 網路／通訊固定服務 = **5 / 5** → **FREEZE NEW**
- Hahow × 線上學習 = **5 / 5** → **FREEZE NEW**
- highest reused Exact-2020 URL count = **4 / 6**
- product-family violations (>2 variants) = **0**
- brand/merchant cap violations = **0**
- brand × subcategory cap violations = **0**
- same-historical-source cap violations = **0**

Known family surfaces at the 2-variant cap include the intended paired variants documented in the ledgers; no third variant should be added without a separate family definition.

## Duplicate QC

- Exact-name duplicate against canonical Candidate_Pool Exact concepts: **0**
- Duplicate concept names inside the 40-row Batch-9 research set: **0**

Economic-concept duplicate review remains required again at canonical admission time because exact-name comparison is necessary but not sufficient.

## Source-quality notes

- MUJI rows use official Taiwan 2020 and current price surfaces.
- UNIQLO rows use dated / edition-anchored 2020 official LifeWear or official news pages and current 26FW/current official surfaces; annual garment construction changes are explicitly reflected as comparability B where appropriate.
- Hahow baseline prices come from official 2020 campaign pages that separate normal course price from discount codes. Current non-standard surfaces are graded B where the live checkout page is not directly text-readable.
- Streaming rows use normal/original prices, not promotional effective prices.
- Hami書城 uses official 2020 and current Chunghwa Telecom/Hami pricing; content-library drift is why comparability remains B.

## Branch safety

This checkpoint must remain on `research/batch-09`.

Do **not** modify:

- canonical workbook;
- `data/*.csv`;
- `canonical/status.json`;
- Basket seal state;
- Index lock state.

The formal number remains **181 / 600** until the full Batch 9 admission workflow is completed.

## Next checkpoint direction

Proceed to checkpoint-03 without sealing Batch 9.

Priority:

1. **衣** — but no additional UNIQLO; seek independent brands and especially pants/skirts, underwear/socks, shoes, outerwear, functional apparel.
2. **住／家用** — non-CHT and non-IKEA; prioritize cleaning/laundry, bedding, small-appliance consumables, home services.
3. **行** — parking, taxi/ride-hail, vehicle maintenance, wash/consumables, rental.
4. **育** — non-PILOT, non-Hahow; prioritize language/tuition and children/talent courses.
5. **日常／個人** — avoid personal digital/membership because that subcategory is projected full.
6. **食** — genuine shortfalls only; avoid already saturated meal/coffee surfaces.

Continue internal QC every ~20–25 concepts. Do not export or merge yet.
