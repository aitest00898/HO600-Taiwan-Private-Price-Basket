# Batch 9 Checkpoint 03 — Research-only QC

Date: 2026-10-04  
Branch: `research/batch-09`

## Status

- Checkpoint-03 admissible research concepts: **20**
- Cumulative Batch-9 research checkpoints: **60 concepts** (C01 20 + C02 20 + C03 20)
- This checkpoint is **research-only** and does **not** change canonical progress.
- Canonical `main` remains **181 / 600**, remaining **419**.
- `Basket_600`: **NOT SEALED**
- `Index_Calc`: **LOCKED**
- Price-change blindness remains in force; checkpoint research must not be interpreted as a sealed basket or headline index.

## QC corrections made before commit

1. **FarGlory Ocean Park** — the 2020 FamiPort NT$890 amount is a promotional selling price. The normal/suggested adult full ticket is **NT$990**, so the admitted pair is **990 → 990**.
2. **Shallop Full Care mouthwash SKU 168832** — admitted as the same-SKU normal-price pair **225 → 225**. Earlier conversational 197/249 figures were not used.
3. **GUM 960ml lead** — removed from C03 because the 2020 normal-price evidence was weaker. It was replaced by the stronger exact-SKU **GUM periodontal toothpaste 130g, SKU 129537**, normal-price pair **169 → 199**.
4. **Listerine / 3M leads** — not admitted in this checkpoint because Exact-2020 evidence quality was weaker than the final 20.
5. **Costco membership and Microsoft 365 annual-plan ideas** — rejected as C03 duplicates/product-family duplication because C01 already admitted the corresponding economic concepts/families.
6. **Logistics variants** — retained only one S60 concept per operator. S90/S120/S150 variants were not used to avoid filling a cell from one price schedule.

## Projected quota effects after C01 + C02 + C03

| Cell | Before C03 | C03 adds | Projected | Action |
|---|---:|---:|---:|---|
| 日常／個人 — 其他日常服務 | 5 / 7 | +2 | **7 / 7** | FREEZE NEW |
| 日常／個人 — 盥洗／衛生用品 | 1 / 14 | +4 | **5 / 14** | continue |
| 樂 — 電影 | 10 / 11 | +1 | **11 / 11** | FREEZE NEW |
| 樂 — 樂園／休閒 | 6 / 8 | +2 | **8 / 8** | FREEZE NEW |
| 樂 — 體驗／休閒場館 | 3 / 8 | +5 | **8 / 8** | FREEZE NEW |
| 行 — 停車 | 0 / 11 | +3 | **3 / 11** | continue |
| 行 — 民營交通服務 | 6 / 8 | +2 | **8 / 8** | FREEZE NEW |
| 食 — 便利即食 | 7 / 14 | +1 | **8 / 14** | continue |

## Concentration QC

- No new brand exceeds the Batch-9 reference cap of 8.
- No brand × subcategory exceeds 5.
- No historical source exceeds the source cap of 6.
- Logistics 2020 source: **2 concepts**.
- Taipei private-parking 2020 source: **3 concepts**.
- Kinmen aviation 2020 source: **2 concepts**.
- Juming/Miramar 2020 travel source: **2 concepts**.
- Brushle mouthwash family: **2 variants → FREEZE FAMILY**.
- Taipei 101 parking family: **2 variants → FREEZE FAMILY**.
- GUM has 2 Batch-9 admissions but they are different product families (mouthwash / toothpaste).
- Duplicate gate passed against canonical Candidate_Pool, canonical Evidence, C01 and C02.

## Public-host evidence clarification

Several historical URLs are hosted by public bodies (Legislative Yuan, Taipei City, Kinmen County). They are used **only as dated evidence carriers for prices set by private operators**:

- private parcel operators,
- private parking operators,
- private airlines.

The admitted core prices are not government-administered tariffs. This checkpoint does **not** relax the HO600 rule excluding government-set prices.

## Decision

**CHECKPOINT-03 = PASS (research-only).**

The 20 rows in `checkpoint-03-ledger.csv` are admissible for Batch-9 research continuation, but they are not canonical admissions until the eventual Batch-9 workbook is exported, re-imported and fully validated on `main`.
