# HO600 Batch 9 — C06 checkpoint receipt

Date: 2026-10-30  | Branch: `research/batch-09`  | Fixed ledger: [checkpoint-06-ledger.csv](./checkpoint-06-ledger.csv)

## Decision and scope

**CHECKPOINT-06 = PASS_RESEARCH_ONLY_WITH_EVIDENCE_LIMITATIONS (20/20).** These are B-level 2020/2026 published or displayed price observations for research. They are not 2020/2026 POS receipts, formal Exact admissions, a representative household price sample, or an HO600 index result.

C06 WIP has 31 rows: 20 `ADMISSIBLE`, 3 `PROVISIONAL_ADMISSIBLE`, 2 `HOLD_PRODUCT_LINEAGE`, and 6 `DUPLICATE_PREQUALIFIED_CANDIDATE`. The fixed 20-row ledger equals the admissible WIP extract and the 20 `ADMISSIBLE` WIP rows exactly. Non-admitted rows remain in the WIP record and are excluded from the fixed set.

## Fixed set

The 20 accepted IDs are `001`, `002`, `003`, `005`, `008`, `010`–`012`, `014`–`016`, `019`–`024`, `027`, `028`, and `031`. They cover clothing and shoes, food and drink, hair and hotel guest laundry, personal care and household cooking oil. Both period prices are positive and both cited source fields are HTTPS.

Important limitations remain row-specific in the ledger. Examples include series rather than SKU continuity, non-identical 2020/2026 retailers, a published campaign/list price rather than a transaction, and Xitou Shante laundry services restricted to hotel guests. The hotel laundry entries are not public self-service laundry market prices. The three C06 provisional rows and six candidate-pool duplicates are not counted.

## Source and cross-check receipts

The C06 receipt register has 45 records. All records report strict TLS verification; 40 are HTTP 200, while non-200 outcomes remain recorded as source-search diagnostics. Every source URL used by the fixed 20 rows has a matching strict-TLS HTTP-200 receipt. Receipt bodies are represented by captured-body SHA-256 values; not every historical response body is retained locally.

Independent fixed-ledger checks across C01–C08 found 160 rows, 160 unique IDs, 23 columns per row, `ADMISSIBLE` for all fixed rows, positive 2020/2026 prices, and HTTPS sources. Grouped maxima are 8 admissions per merchant, 5 per merchant/subcategory, 6 rows per exact 2020 source URL, and 2 variants per recorded product family. These are research concentration controls, not proof of price representativeness.

C01–C05 remain 100 fixed pairs; C06–C08 add 60, for **160 fixed research pairs**. The requested additional-100 objective counts C04–C08, 20 per checkpoint, and is **100/100 at research level**. Formal main remains 181/600, Basket `NOT SEALED`, Index `LOCKED`.

Repository validation passed. The dashboard Python suite passed 24/24. The broad cohort-inflation suite had 54 passing cases and one import error because `artifact_tool` is not installed for the unrelated XLSX test module; details are in [the 2026-10-30 Handoff](./HANDOFF-2026-10-30.md). No canonical workbook, `main`, Index or Actions were changed.
