# HO600 Batch 9 — 18-Exact canonical release scope (2026-10-31)

## Baselines and authority

- Release branch: `release/ho600-batch09-exact18-20261031`, branched directly from canonical main at `88fa2b53774067faf740868bb8e168a04e47a8bf`.
- Research evidence source: `research/batch-09` commit `4dd948a21d4526a0298d2667ab5837be3a1bfa66`.
- User instructed proceeding to the next formal admission step, following the prior proposal of admitting 18 Exact candidates with local validation and conditional main merge. The prior narrow policy approval applies **only** to `LEG-EC-041` and `LEG-EC-042`: historic 2020 tariff backfill to existing concepts, with 嘟嘟房 capped at 8/8; no blanket policy exception.
- This file records the bounded release intent; **its presence is not proof of successful canonical admission**.

## Required canonical change (only after Mac local workbook verification)

| Dataset | Baseline main | Expected after all 18 admitted |
| --- | ---: | ---: |
| `PREQUALIFIED-EXACT2020` concepts | 181 | 199 |
| Candidate Pool concepts | 418 | 434 (+16 new) |
| Evidence records | 1,566 | 1,600 (+34) |
| Basket_600 selected | 0 | 0 |
| Basket seal | NOT SEALED | NOT SEALED |
| Index | LOCKED | LOCKED |

- 16 newly distinct economic concepts: `B09-C01-001` through `010`, `B09-C01-013`, `B09-C01-017` and `018`, and `B09-C07-018` through `020`.
- Existing `LEG-EC-042` (Taichung THSRC P1 car hourly rate) requires **one** 2020 evidence observation: NTD 40/hour against the existing 2026 NTD 50/hour. Do not create a new Pool concept or duplicate 2026 price records.
- Existing `LEG-EC-041` (Taichung THSRC P1 daily maximum) requires **one** 2020 evidence observation: NTD 240/day maximum against existing 2026 NTD 350/day maximum. Explicitly mark NTD 350 as **a daily cap, not average or typical payment**, in all release evidence and concept descriptions.
- New 16 concept evidence: +32 paired 2020 and 2026 observations. Exact 18 must not be conflated with 18 new Candidate Pool concepts.
- Retain existing 181 prequalified concepts and all prior Evidence rows, including legitimate legacy overages; no forced pruning. Existing top five and top ten concentration overages are legacy (56/40, 85/60), not a reason to drop valid existing concepts. Corporate group attribution of unrelated legacy rows is incomplete; do not claim a full census.

## Scope controls

- The release must be assembled from this main-derived branch. **Do not merge or fast-forward `research/batch-09` wholesale**: the latter is 269 commits and 296 files ahead and includes a `.github/workflows/validate.yml` change unrelated to this release.
- Do not modify or invoke GitHub Actions, alter other workflows, change Basket seal or Index lock, deploy a dashboard, or make unrelated research changes.
- Canonical `workbook/HO600-WIP_shortfall-search_batch8.xlsx`, `data/Candidate_Pool.csv`, `data/Evidence.csv`, `data/Quota_Control.csv`, `data/Validation_Release.csv`, `data/README_Status.csv`, `canonical/status.json`, and `canonical/MANIFEST.sha256` must be mutually consistent where affected; name changes or batch-numbering changes only if required by existing rules.
- Use Mac's already validated JS `@oai/artifact-tool` workbook import/edit/export/reimport path and project validators, plus new localized release assertions. Record the actual post-edit SHA-256. Never reuse the preflight copy hash as if it were the canonical release hash.
- No force push. Commit only a tested, complete release to this branch, open a narrowly scoped PR targeting main, check the changed-file allowlist and actual test artifacts; merge only on full required PASS and unchanged expected main SHA. Do not depend on GitHub Actions for acceptance.
- If canonical workbook cannot be edited or any validation fails, **stop before main merge** and report the specific blocker. Never update only the `status.json` count.

## Evidence and previously passed isolation

- [Source adjudication](https://github.com/aitest00898/HO600-Taiwan-Private-Price-Basket/blob/research/batch-09/research/batch-09/exact-admission-final-adjudication-2026-10-31.csv)
- [Isolated XLSX receipt](https://github.com/aitest00898/HO600-Taiwan-Private-Price-Basket/blob/research/batch-09/research/batch-09/exact-admission-workbook-preflight-2026-10-31.json)
- [Tests and release notes](https://github.com/aitest00898/HO600-Taiwan-Private-Price-Basket/blob/research/batch-09/research/batch-09/HANDOFF-2026-10-31.md)
- Prior locally accepted isolated workbook SHA: `be5287f217a11883f2ad0715e8914682455840e4ad3d2edb9a353f89c1d194c3` (not a main release).
- Base canonical workbook SHA: `c01bce376e45e715d9b8eac4f353c61d20b5973e1e1c4e32f90a6e512bed40b9`.
