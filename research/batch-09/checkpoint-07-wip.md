# HO600 Batch 9 — C07 WIP evidence log (historical snapshot)

> **Superseded status notice (2026-10-30):** This file preserves the earlier research log. The accepted fixed checkpoint is now 20/20; use [the final checkpoint receipt](./checkpoint-07.md) and fixed ledger for current counts. Earlier count statements below describe the pre-completion snapshot.

Date: 2026-10-30  | Branch: `research/batch-09`  | Base HEAD checked: `0c83ff044d3bd1b3e103a64ebb204d5a3fe90f7e`

## Current decision

**C07 has 11 row-level research-admissible pairs out of 20; the checkpoint remains open and is not fixed.** The [WIP ledger](./checkpoint-07-wip-ledger.csv) contains 11 rows, all marked `ADMISSIBLE` for research use only. Nine more qualifying pairs are required. The [source-receipt register](./checkpoint-07-source-receipts-2026-10-30.csv) has 19 capture rows with original URL, timestamp, HTTP/TLS details, body size and SHA-256.

## Counted pairs and evidence limits

- `001`–`005`: five packaged drinks with 2020 prices from one CREA Taiwan article/source; current endpoints are retailer/manufacturer listings. This is one historical publisher, not five independent witnesses. The shared source is used 5/6 times. Exact barcode/price-date/POS continuity is not established; these are B-level comparisons.
- `006`–`009`: four Annli / 壹 Hair Salon service prices from its 2020 and 2026 price lists. The salon moved from Wanhua to Zhongzheng; brand/designer continuity holds, but branch continuity does not. The 2020 figures are public list prices before member discounts, not transaction records. This single 2020 URL is used 4/6 times and uses 4/5 brand-by-subcategory slots.
- `010`: Taiyen high-iodized salt 1kg, a Candidate Pool concept missing its historical quote; 2020 news reports a retail price and 2026 PXGo lists the current item. The old barcode/store are not established, so this is B-level only.
- `011`: TaiSugar 75% alcohol wipe, 10 pulls; a 2020 CNA report gives PX Mart's announced NT$24 price, and PXGo lists the current 10-pull item at NT$24. The 2020 concentration and historical SKU/barcode are unverified, so this is B-level only.

No pair is a formal Exact admission or proof of an actual completed purchase. A row-level admissible label does not mean the 20-row checkpoint has passed.

## Search leads retained as HOLD / excluded (not counted)

- Candidate Pool food leads: I-Mei chocolate puff has an undated NT$30 listing and a current 57g/65g identity conflict; Champions eggs pair a 2020 wholesale, unbranded medium/large quote with a current retail L-grade named product. No PASS.
- Household leads: Philips bulb, Baiyan bags, White Orchid detergent, Kirkland detergent and Crocs lacked a verified 2020 same-spec ordinary price; item identity lists without prices were not used.
- Service/transport leads: the 2020 C6133 tire note is an unnamed shop with installation while the 2026 quote is another shop without installation; laundry 2020 price leads lack a current matching tariff; iRent leads are promotional or have incompatible area/return restrictions.
- SOGO 2020 flyer leads for S&B curry and Nitto milk tea show crossed-out reference values during a promotion but omit the exact flavor/variant; they remain HOLD pending independent ordinary-price and variant evidence.
- A 2020 media lead for Xiaolin salon wash was not added: strict local TLS verification failed with `Missing Subject Key Identifier`; no TLS exception or alternate trust was used. Web-indexed text was not treated as a local source receipt.

Agents and search runs produced no additional pair that met the same evidence threshold. These leads are not ledger rows and are not included in `PROVISIONAL` or `HOLD` counts.

## Batch progress and boundaries

C01–C05 have 100 fixed research pairs; C06 has 18 currently admissible WIP pairs; C07 has 11; C08 has 0. Current total is 129 research-qualified, and the user’s additional-100 objective is 69/100, leaving 31. Formal `main` remains 181/600, Basket `NOT SEALED`, Index `LOCKED`. No GitHub Actions, canonical workbook, `main`, merge or deployment was used.
