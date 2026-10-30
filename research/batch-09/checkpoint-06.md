# HO600 Batch 9 — C06 progress receipt (18/20, OPEN)

Date: 2026-10-30  | Branch: `research/batch-09`  | Verified base: `0c83ff044d3bd1b3e103a64ebb204d5a3fe90f7e`

**C06 is not complete.** The WIP ledger has 31 rows: 18 research-admissible, 5 provisional, 2 product-lineage holds, and 6 prequalified duplicates. The 18 counted IDs are `001`, `002`, `008`, `010`–`012`, `014`–`016`, `019`–`024`, `027`, `028`, and `031`. No fixed 20-pair checkpoint ledger was created.

Three new research pairs passed the row-level B-evidence screen:

| ID | Pair | 2020 listed/reference price | 2026 listed price | Limit |
|---|---|---:|---:|---|
| C06-027 | VANS Old Skool `VN000D3HY28` | NT$2,380 | NT$2,080 | Same model ID; 2020 source is an annual campaign page with no exact day and displays a promotion beside the original/list price. Not a transaction or formal Exact. |
| C06-028 | NIID R1 bag | NT$2,880 | NT$2,880 | 2020 series-level listing has no EAN or exact date; price is a listed/reference price. |
| C06-031 | Lativ women's white 100% cotton crew T | NT$199 | NT$199 | 2020 consumer article records an actual purchase but no receipt/SKU; current item number does not prove 2020 SKU continuity. |

`C06-002` is retained as a B-level same-use/package-count comparison (two-pair invisible running socks). The 2026 official Decathlon product was visible in the official page's indexed rendering, while the strict raw category GET did not contain its card. That limitation is recorded and prevents an Exact or SKU-continuity claim. The Spring tissue and Dandelion hand-towel drafts (`029`/`030`) were reclassified as duplicates because their prequalified concepts and paired 2020/2026 Evidence records already exist in the Candidate Pool and `data/Evidence.csv`.

## Validation

- `python3 scripts/validate_repo.py`: all reported repository checks passed; canonical workbook SHA-256 remained `c01bce376e45e715d9b8eac4f353c61d20b5973e1e1c4e32f90a6e512bed40b9`; formal Exact remains 181/600, Basket `NOT SEALED`, Index `LOCKED`.
- Read-only CSV QC: C01–C05 100; C06 18; C07 11; C08 0; total 129 research-qualified; additional objective 69/100. B09 new-admission caps: max brand 4, max brand/subcategory 4, max same 2020 source URL 5. The repository's current CSV schemas have 23 columns; IDs were unique and accepted rows had positive prices and 2020/2026 source fields.
- No unit-test directory covers these research ledgers. No test framework or tests were added. No Actions workflow was invoked or modified.

## Source and scope limits

These are B-level price observations, not POS receipts. A campaign page's listed/original price is kept separate from its promotion and is not claimed as ordinary non-promotion checkout price. Product lineage, channel and exact dates remain qualified per row. This C06 work does not change canonical `main`, the workbook, Index, or any formal Exact admission. See [the WIP ledger](./checkpoint-06-wip-ledger.csv), [C06 status](./checkpoint-06-wip.md), and [source receipts](./checkpoint-06-source-receipts-2026-10-30.csv).

**Next:** find two additional non-duplicate C06 pairs with traceable 2020 and 2026 source evidence; then run the checkpoint-level QC before creating a fixed 20-row C06 ledger. C07 remains 11/20 and C08 remains 0/20.
