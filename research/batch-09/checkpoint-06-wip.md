# HO600 Batch 9 — C06 WIP evidence log (historical snapshot)

> **Superseded status notice (2026-10-30):** This file preserves the earlier research log. The accepted fixed checkpoint is now 20/20; use [the final checkpoint receipt](./checkpoint-06.md) and fixed ledger for current counts. Earlier count statements below describe the pre-completion snapshot.

Date: 2026-10-30  | Branch: `research/batch-09`  | Base HEAD checked: `0c83ff044d3bd1b3e103a64ebb204d5a3fe90f7e`

## Current count

**C06 has 18/20 research-admissible pairs and remains OPEN. No fixed 20-row C06 checkpoint was created.** The authoritative source is [the 31-row WIP ledger](./checkpoint-06-wip-ledger.csv):

- 18 `ADMISSIBLE`
- 5 `PROVISIONAL_ADMISSIBLE` (`003`–`006`, `013`)
- 2 `HOLD_PRODUCT_LINEAGE` (`007`, `009`)
- 6 `DUPLICATE_PREQUALIFIED_CANDIDATE` (`017`, `018`, `025`, `026`, `029`, `030`)

Rows `029` and `030` were initially drafted as new pairs, then excluded after the cross-batch check found the same Spring tissue and Dandelion hand-towel concepts already prequalified in `Candidate_Pool.csv` with paired records in `data/Evidence.csv`. Their new source captures remain documented, but they do not count toward C06 or the additional-pair objective. The 18-row [admissible WIP extract](./checkpoint-06-admissible-subset-wip.csv) is not a fixed checkpoint.

The 18 counted IDs are `001`, `002`, `008`, `010`–`012`, `014`–`016`, `019`–`024`, `027`, `028`, and `031`.

## New rows and source limits

This turn added three countable pairs: VANS Old Skool exact model `VN000D3HY28` (2020 Rakuten listed price NT$2,380; 2026 PChome ABC-MART listed price NT$2,080), NIID R1 series (NT$2,880 in both observations), and a Lativ women's 100% cotton crew T (NT$199 in both observations). All are B-level research price comparisons, not verified transactions or formal Exact admissions; their SKU, formulation, channel, or date limitations are recorded in the ledger.

`B09-C06-002` is counted as a category-level B comparison of two-pair invisible running socks. The current official Decathlon category's indexed rendering identifies KIPRUN RUN500 light invisible socks, two pairs, NT$99. A strict raw GET of that category did not contain the product card; the indexed page rendering did. This weaker retrieval is recorded separately from the raw-body receipt. The 2020 source does not identify a matching SKU or fiber, so this is not an exact product-lineage claim; if later evidence shows the specs cannot be reconciled, downgrade it rather than treating the current price as proof of continuity.

For the new B09 admissions, the highest same-brand count is 4, highest same-brand/subcategory count is 4, and highest repeated 2020 URL count is 5 (the Bella shampoo article and CREA drink article each have five rows). Rakuten is used by four counted C06 concepts, below the same-historical-source cap of six. The 2020 Rakuten page is a single publisher, not four independent historical witnesses.

The new Rakuten source-receipt rows capture the 2020 campaign page and current product pages without retaining response bodies. Receipt `SRC-20261030-06-NEW-07` is only a raw Decathlon category GET; its body hash does **not** prove the KIPRUN product card. The official indexed rendering is explicitly documented as weaker evidence.

## Remaining work and formal boundary

C01–C05 remain 100 fixed research pairs. Current counts are C06=18, C07=11, C08=0, for 129 total research-qualified pairs and 69/100 toward the additional objective (C04+C05 contribute 40). C06 needs two more qualifying non-duplicate pairs; C07 needs nine; C08 needs twenty. No count is a formal Exact admission. `main` remains 181/600, Basket `NOT SEALED`, Index `LOCKED`; the canonical workbook and Index were not changed. GitHub Actions were not run.

The official `scripts/validate_repo.py` passed all of its reported checks. A separate read-only CSV QC verified 23-column schemas, unique research IDs, positive prices, dated 2020/2026 source URLs, WIP/admissible counts, and the B09 brand, brand/subcategory, and 2020-source caps. See [C06 source receipts](./checkpoint-06-source-receipts-2026-10-30.csv) and [C07 source receipts](./checkpoint-07-source-receipts-2026-10-30.csv). No C06 checkpoint acceptance is claimed until the 20-row target and required QC are met.
