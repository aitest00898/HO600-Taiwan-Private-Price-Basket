# HO600 Batch 9 — C08 WIP evidence log (historical snapshot)

> **Superseded status notice (2026-10-30):** This file preserves the earlier research log. The accepted fixed checkpoint is now 20/20; use [the final checkpoint receipt](./checkpoint-08.md) and fixed ledger for current counts. Earlier count statements below describe the pre-completion snapshot.

**C08 contains two row-level research-admissible pairs; the checkpoint remains open and is not fixed.** They are research evidence, not HO600 formal Exact observations.

## B09-C08-001 — T-UP Wanhua adult weekday starlight entry plus shoe rental

- **2020:** A visitor article published 2020-09-23 identifies the T-UP Wanhua location at Taipei City, Wanhua District, Dali Street 149 and states weekday evening starlight entry NT$330 including shoe rental. This is a contemporaneous public price report, not a retained point-of-sale receipt.
- **2026:** T-UP’s official Wanhua tariff lists adult weekday starlight entry (20:30–23:00) at NT$320, excluding equipment, and climbing-shoe rental at NT$100. The official page gives the same address.
- **Comparable service unit:** one adult weekday starlight admission with one rental pair, NT$330 in 2020 versus NT$420 in 2026 (NT$320 + NT$100). The 2020 source does not state the precise time window. If the customer brings their own shoes, the period components differ; do not compare NT$330 directly with NT$320. Grade B comparability and B research admission preserve these limits.
- **Sources:** [2020 visitor article](https://xenia9.pixnet.net/blog/posts/16020334518), [official current Wanhua tariff](https://tupclimbing.tw/pricing/84). Strict local TLS validation, HTTP status, retrieval time, body size, and SHA-256 are in the [C08 source-receipt register](./checkpoint-08-source-receipts-2026-10-30.csv).

## B09-C08-002 — Taipei Changchun Ambassador standard full-price admission

- **2020:** Ambassador’s official notice published 2020-06-12 links a branch-specific rate image titled “台北長春國賓影城 2020年7月3日起票價調整”; it lists the full ticket changing from NT$300 to NT$310, so NT$310 is the rate effective in 2020.
- **2026:** Ambassador’s official Taipei Changchun page lists NT$320 for a digital 2D full ticket. It identifies the same branch and address.
- **Comparable service unit:** one standard full-price ticket at the same cinema, NT$310 effective from 2020-07-03 versus NT$320 on 2026-10-30. The historical price image says “full ticket” but does not explicitly label the screening format as 2D; it separately notes version/3D and D-BOX surcharges. Comparability is therefore B, and the row does not claim every screening format is identical. Member, student/discount, premium-seat and long-runtime prices are excluded.
- **Sources:** [2020 official notice](https://www.ambassador.com.tw/home/NewsContent?ID=257), [embedded Changchun tariff image](https://www.ambassador.com.tw/Uploads/207/223d7b8e-ada1-4058-a6ca-9af4629ed271.jpg), [2026 official Changchun theater price table](https://www.ambassador.com.tw/home/theater_intro_a5). TLS/HTTP/size/SHA receipts are recorded below.

## De-duplication and boundary

T-UP Wanhua and Ambassador Taipei Changchun do not appear as the same concepts in the 418-row `data/Candidate_Pool.csv` or the C01–C07 ledgers/WIP; the existing cinema candidates are MUVIE CINEMAS at a different site, not Ambassador. Each C08 row uses a distinct 2020 source and merchant. Quota Control lists nine remaining additions in `樂／健身／運動` and one in `樂／電影`; these research pairs do not change canonical quota or Exact counts.

C01–C05 remain 100 fixed research pairs. Latest WIP ledgers show C06=18/20 and C07=11/20. With these two C08 pairs, total research-qualified pairs are 131; the additional-100 target is 71/100, leaving 29. C06 and C07 remain open, and C08 is open at 2/20. Formal `main` remains 181/600; Basket `NOT SEALED`; Index `LOCKED`. No canonical workbook, main branch, or GitHub Actions were changed.
