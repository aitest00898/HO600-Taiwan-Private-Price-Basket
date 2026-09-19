# HO600 — Taiwan Private Historical-Observable Price Basket

HO600 (Historical-Observable Balanced 600) is a research project to construct a **600-economic-concept Taiwan private-price basket** in which every admitted concept has a directly verifiable **Exact-2020 ↔ Exact-2026** normal/list/base-price pair.

## Canonical status

| Field | Current canonical value |
|---|---:|
| Canonical batch | **Batch 8** |
| Formal Exact-2020↔2026 concepts | **181 / 600** |
| Remaining | **419** |
| Candidate concepts | **418** |
| Evidence records | **1,566** |
| Basket_600 | **NOT SEALED** |
| Index_Calc | **LOCKED** |

**Important:** research checkpoints do **not** change the formal number. Formal progress changes only after a workbook is exported, re-imported, validated, committed to `main`, and its canonical status is updated consistently.

## Research objective

The goal is not to collect 600 prices. The goal is to construct 600 controlled **economic concepts**, each with:

- Exact-2020 evidence;
- Exact-2026 evidence;
- normal/list/base price semantics;
- comparable identity, specification, channel, and geography;
- traceable source URLs and dating;
- no substitution of 2019/2021 for 2020;
- no promotion-derived, BOGO-derived, member-effective, coupon-effective, bundle-derived, or delivery-markup price.

## Source of truth

Priority order:

1. `main` canonical workbook + `canonical/status.json`
2. validated CSV snapshots under `data/`
3. validation records
4. research branches / issues / notes
5. chat or verbal progress

Current canonical workbook:

`workbook/HO600-WIP_shortfall-search_batch8.xlsx`

SHA-256:

`c01bce376e45e715d9b8eac4f353c61d20b5973e1e1c4e32f90a6e512bed40b9`

## Repository workflow

- `main`: validated canonical state only.
- `research/batch-XX`: active archaeology and candidate work.
- Internal checkpoints every ~20–25 admissible concepts are **research QC only**.
- A large batch normally targets ~75–100 high-quality Exact concepts, but evidence quality overrides throughput.
- A batch may merge only after validation passes.

See:

- [`docs/methodology.md`](docs/methodology.md)
- [`docs/evidence-gate.md`](docs/evidence-gate.md)
- [`docs/concentration-policy.md`](docs/concentration-policy.md)
- [`docs/source-of-truth.md`](docs/source-of-truth.md)
- [`docs/research-workflow.md`](docs/research-workflow.md)

## Selection blindness

`Candidate_Pool` must remain blind to observed price movement. It must not contain 2020 price, 2026 price, change, percentage change, or inflation columns. Candidate selection is based on structural shortfall, identity/specification, channel, brand/source diversity, comparability, and evidence quality.

## Validation

Run locally:

```bash
python scripts/validate_repo.py
```

The GitHub Actions workflow runs the same checks on pushes and pull requests.

## License

No open-source license has been selected yet. Public visibility does not itself grant reuse rights.
