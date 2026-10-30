# HO600 Batch 9 — C07 checkpoint receipt

Date: 2026-10-30  | Branch: `research/batch-09`  | Fixed ledger: [checkpoint-07-ledger.csv](./checkpoint-07-ledger.csv)

## Decision and scope

**CHECKPOINT-07 = PASS_RESEARCH_ONLY_WITH_EVIDENCE_LIMITATIONS (20/20).** The fixed ledger consists of 20 row-level `ADMISSIBLE` research pairs. It does not certify transaction prices or formal HO600 Exact admission.

The set contains five packaged drink observations from one 2020 CREA article, four Annli/壹 Hair Salon services from one 2020 published price list, a salt product, a single-pack alcohol wipe, six ready-to-drink milk teas, and three Amway Home laundry products. The exact concepts, prices, period details, evidence grades and qualifications are recorded in the 23-column ledger.

## Evidence limitations and concentration

- The five CREA drink pairs share one 2020 publisher/article. They are five products, not five independent historical sources.
- Four salon prices share one 2020 price-list URL. The salon moved from Wanhua to Zhongzheng; the evidence supports brand/designer continuity but not the same branch. Prices are published list prices, not transactions.
- C07-011 compares the named 10-pull TaiSugar alcohol wipe at NT$24 in a 2020 CNA retailer-announcement report and the 2026 PXGo listing. The historical report does not establish the old barcode or alcohol concentration; those remain unverified.
- Other rows preserve missing old barcodes, changing beverage formulations, retailer differences and standard-price versus promotion semantics as written in each ledger note.

The receipt register has 30 records, each reporting HTTP 200 and strict TLS validation; seven linked C07 raw captures were independently hash-matched to their receipt SHA-256. `SRC-20261030-07-17` contains a truncated SHA string; it is retained as originally recorded. The same source was reacquired with strict TLS as `SRC-20261030-07-19` with a valid 64-character SHA-256 and is explicitly marked as the corrective receipt. No fixed-ledger source URL is missing a strict, successful receipt.

The C07 fixed set has no duplicate research IDs against C01–C06 or C08. Across the C06–C08 additions, grouped maxima are 6 per merchant, 4 per merchant/subcategory and 6 per exact historical URL; all remain within the Batch-9 reference caps.

C01–C05 remain 100; C06–C08 add 60, for 160 fixed research pairs. The additional-100 objective (C04–C08) is 100/100 at research level. Formal main remains 181/600; Basket `NOT SEALED`; Index `LOCKED`. See [C07 WIP evidence log](./checkpoint-07-wip.md) and [receipt register](./checkpoint-07-source-receipts-2026-10-30.csv).
