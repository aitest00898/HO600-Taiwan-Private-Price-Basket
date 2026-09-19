# Batch 9 — checkpoint-01 (revised structured QC)

This is an **internal research checkpoint only**. It does not modify the canonical workbook, CSV snapshots, or `canonical/status.json`.

- Formal canonical progress remains **181 / 600** (Batch 8).
- Checkpoint size: **20 research concepts**.
- Structured row-level ledger: [checkpoint-01-ledger.csv](./checkpoint-01-ledger.csv)
- Every listed core price uses normal/list/base/original-price semantics; promotional effective prices are excluded.
- Admission here means **research-level ADMISSIBLE**, not canonical Exact. Formal Exact can increase only after Batch 9 export, re-import, validation, CI, PR and merge.

## Revised composition

| Group | Concepts | QC result |
|---|---:|---|
| PILOT stationery | 5 | ADMISSIBLE; `brand × subcategory = 5`; **FREEZE NEW** after this checkpoint |
| Chunghwa Telecom / MOD | 5 | ADMISSIBLE; deliberately reduced from the earlier 8-concept draft to respect concentration policy; **FREEZE NEW** |
| Costco memberships | 2 | ADMISSIBLE; 2020 evidence is dated contemporary private reporting (B), current is official (A); comparability B |
| FamilyMart services | 2 | ADMISSIBLE; store-to-store normal fee 60→60 and A4 B/W 3→3 |
| 7-ELEVEN services | 2 | ADMISSIBLE; seller-shipping normal fee 60→60 and ibon A4 B/W 3→3; 2020 evidence B |
| Apple One | 2 | ADMISSIBLE; official A/A; Individual 315→390, Family 395→490 |
| Microsoft 365 | 2 | ADMISSIBLE; official A/A evidence; Personal 219→309, Family 320→419; **comparability B** because current plans add Copilot/expanded service scope |
| **Total** | **20** | research checkpoint only |

## Corrections from the original oral checkpoint

1. **CHT 8 → 5.** The earlier 8-concept idea would collide with concentration controls, especially `brand × subcategory ≤ 5`. The retained five are 16M/3M circuit monthly fee, 100M/40M circuit monthly fee, connection fee, outside-relocation fee, and MOD platform fee.
2. **OKmart → HOLD / removed from the 20-row admissible ledger.** Exact-2020 evidence was not direct enough.
3. **Apple One ×2 added** using Taiwan Apple official 2020 and current pages.
4. **Microsoft 365 ×2 added** using Taiwan Microsoft official monthly prices. These are not treated as comparability A because current plans include material feature expansion.
5. **Print-service prices rechecked.** The 2020 evidence supports FamilyMart A4 B/W at 3 and 7-ELEVEN A4 B/W at 3; current official pages are also 3. Historical print evidence is graded B rather than A.
6. The ledger records concentration surfaces and evidence grades explicitly; no price/change fields are added to canonical `Candidate_Pool`.

## Concentration status after checkpoint-01

- PILOT: 5 in stationery → at the `brand × subcategory` reference cap; **FREEZE NEW**.
- CHT: 5 in fixed communications / platform-service area → no further CHT additions in Batch 9.
- Same historical source: the 2020 CHT xDSL schedule supports 4 concepts, below the cap of 6.
- PILOT 瞬筆 product family uses 2 variants, exactly at the family cap.
- Apple One family uses 2 variants, exactly at the family cap.
- Microsoft 365 consumer family uses 2 variants, exactly at the family cap.
- Costco membership family uses 2 variants, exactly at the family cap.

## Next action

Proceed directly to **checkpoint-02 (20–25 concepts)** from the Batch 8 current-only pool and unresolved shortfalls. Priority remains:

**衣 → 住／家用（non-CHT, non-IKEA） → 行 → 育（other stationery brands / courses） → 日常／個人 → genuine food gaps.**

Do not seal Batch 9 at this checkpoint. Continue until the Batch 9 admissible set is large enough (normally +75–100, but evidence quality and marginal yield govern the stopping point).
