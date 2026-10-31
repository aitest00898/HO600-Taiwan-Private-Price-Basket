# HO600 Batch 9 Exact-18 release acceptance — 2026-10-31

## Scope and authority

- Release branch: `release/ho600-batch09-exact18-20261031`, created from main baseline `88fa2b53774067faf740868bb8e168a04e47a8bf`; release branch started at `9762df01ecc7f5188da5fd84141f9e058d264909`.
- Research evidence pinned to `research/batch-09` commit `4dd948a21d4526a0298d2667ab5837be3a1bfa66`.
- Release scope: [`2026-10-31-ho600-batch09-exact18-release-scope.md`](./2026-10-31-ho600-batch09-exact18-release-scope.md).
- Owner approval is limited to historical 2020 evidence backfills for the two existing Candidate Pool concepts `LEG-EC-041` and `LEG-EC-042`. It creates no Candidate Pool concepts and does not raise or waive the Dudu 房 8/8 brand cap. It does not authorize a general `KEEP LEGACY / FREEZE NEW` exception.
- For `LEG-EC-041`, NT$350/day is permanently described as the **daily maximum tariff cap**, never an average or typical payment, in the concept item, specification, selection note, and all linked Evidence notes.

## Admitted release scope

The release contains 16 new economic concepts with 32 paired 2020/2026 Evidence rows, plus one 2020 Evidence row each for existing concepts `LEG-EC-041` and `LEG-EC-042`. It adds 18 Exact candidates but only 16 Candidate Pool concepts.

| Dataset | Main baseline | Release branch |
| --- | ---: | ---: |
| Prequalified Exact concepts | 181 | 199 |
| Candidate Pool concepts | 418 | 434 |
| Evidence records | 1,566 | 1,600 |
| Basket selected | 0 | 0 |
| Basket seal | NOT SEALED | NOT SEALED |
| Index | LOCKED | LOCKED |

All 181 incumbent Exact IDs and prior Evidence rows are retained. The two THSRC concepts each retain their two existing 2026 Evidence rows; no duplicate 2026 record or Candidate Pool concept was added. Candidate_Pool remains price blind. The 16 new IDs are unique and the 34 added Evidence IDs are unique.

The THSRC pairs are `LEG-EC-042` at NT$40/hour (2020) versus NT$50/hour (2026), and `LEG-EC-041` at a NT$240/day maximum (2020) versus a NT$350/day maximum (2026). These are posted tariffs, not observed transaction averages.

The 16 new concepts are PILOT stationery (5), Chunghwa Telecom fixed services (5), FamilyMart parcel service (1), Apple One tiers (2), and Amway Home SKUs 1068, 1069, and 1070 (3). Their identity, normal/list-price semantics, source receipts, dates, and prices are recorded in the release Candidate_Pool and Evidence snapshots and the pinned research decision matrix.

## Source and concentration acceptance

- Research decision matrix: [`exact-admission-final-adjudication-2026-10-31.csv`](https://github.com/aitest00898/HO600-Taiwan-Private-Price-Basket/blob/research/batch-09/research/batch-09/exact-admission-final-adjudication-2026-10-31.csv), SHA-256 `a6a21a09524c151c9343232d63e90b172dbe7c7457b2322c2f1398d4f2021d3b`.
- Candidate/source receipt crosswalk: [`exact-admission-candidate-list-2026-10-31.csv`](https://github.com/aitest00898/HO600-Taiwan-Private-Price-Basket/blob/research/batch-09/research/batch-09/exact-admission-candidate-list-2026-10-31.csv), SHA-256 `bb2d512ca1655a32e4fa3db0b6a043ac35cb1acbcd65581cd648c711f4027295`.
- Source receipt ledger: [`exact-admission-source-receipts-2026-10-31.csv`](https://github.com/aitest00898/HO600-Taiwan-Private-Price-Basket/blob/research/batch-09/research/batch-09/exact-admission-source-receipts-2026-10-31.csv), SHA-256 `ff1ddfa72fc64a7ebb8b4a8b1071c00d09f4ee57b5ceb432ef02e52387eaf47d`.
- All 18 selected source pairs have verified captures and normal/list-price semantics. The 22 distinct selected official-source URLs passed HTTP 200, strict TLS verification, and capture SHA-256 checks. The research source-receipt suite also checks all successful captures against their saved hashes.
- Proposal 2020 source use has a maximum of four concepts per URL against the six-use cap, across ten 2020 source URLs; these URLs have zero use in the incumbent Exact-181 baseline. Package group and family checks pass: PILOT 5/16, Chunghwa Telecom pool 11/16, FamilyMart 5/16, Apple 6/16, Amway 3/16, and THSRC related group pool 8/16. PILOT-SVS, Chunghwa Telecom speed-tier and change-fee, Apple One, Amway detergent, and THSRC P1 families each remain at 2/2; softener is 1/2 and all other families are at most 1/2. The Dudu 房 Candidate Pool remains 8/8.
- Existing top-five brand concentration is 56/40 (+16 legacy), and top-ten is 85/60 (+25 legacy); both are retained under `KEEP LEGACY / FREEZE NEW`. No new top-five brand concept was added. Corporate-group attribution remains unresolved for 135 unrelated incumbent Exact rows; no full incumbent group census is claimed.
- Historical promotions/effective prices are excluded from the admitted normal-price observations.

## Canonical workbook and snapshots

The main-source workbook was imported, edited, exported, re-imported, and verified using Mac JavaScript `@oai/artifact-tool` v2.8.106 with Node v24.22.1. The final release artifact is `workbook/HO600-WIP_shortfall-search_batch8.xlsx`, SHA-256 `5a801585b5352a71255deb5999707d2039980a62f514f61ae729705fd58c1808`.

- All seven original worksheet names and data areas are preserved.
- Candidate_Pool, Evidence, Quota_Control, README_Status, and Validation_Release snapshots match the exported/re-imported workbook data.
- All 1,600 Evidence IDs and all 434 Candidate Pool IDs are unique. The pre-release 181 Exact concepts remain present.
- No formulas or formula-error cells were found. Export/re-import matrix parity passed.
- Quota_Control reflects the post-admission category and domain totals; its existing legacy concentration tables and chart layout are preserved.
- `canonical/status.json`, `canonical/MANIFEST.sha256`, and `README.md` match the final workbook SHA and release counts.

## Local acceptance record

The final release acceptance commands and exit codes are recorded here after execution. The canonical main state changes only when this release is merged; a branch-local workbook or status snapshot by itself does not publish a formal main count.

- Runtime: Python 3.15.1, Node v24.22.1, `@oai/artifact-tool` v2.8.106.
- Repository validator: `python3 scripts/validate_repo.py` — PASS, exit 0; canonical SHA, workbook architecture, CSV snapshots, counts, Basket, and Index checks all passed.
- Batch 9 fixed-ledger tests: `python3 -m unittest discover -s research/batch-09 -p 'test_validate_batch09_exact_preaudit.py' -v` — 21/21, exit 0.
- Exact-admission tests: `python3 -m unittest discover -s research/batch-09 -p 'test_exact_admission_review_2026_10_31.py' -v` — 12/12, exit 0.
- Fixed-ledger validator: `python3 research/batch-09/validate_batch09_exact_preaudit.py` — PASS, 160 unique IDs, exit 0.
- Isolated release assertions: `python3 scripts/validate_batch09_exact18_release.py` — PASS, 2,206 assertions, exit 0, including category/domain reconciliation, group and family limits, and source-use checks.
- CSV snapshots retain the repository's CRLF line endings; `git -c core.whitespace=cr-at-eol diff --check` — PASS, exit 0.

## GitHub Actions setting and publication status

- Opening PR #1 automatically triggered GitHub Actions workflow `Validate HO600`, run `41160717451`, event `pull_request`, at `2026-10-31T02:35:44Z`; it completed with conclusion `success`. This was an automatic GitHub run, not a local acceptance input. It remains in the GitHub run history and is not cleared or treated as acceptance evidence.
- The repository Actions permission endpoint initially returned `enabled=true`. After the owner-authorized repository-scoped `gh api --method PUT repos/aitest00898/HO600-Taiwan-Private-Price-Basket/actions/permissions -F enabled=false`, a fresh GET returned `{"enabled":false,"sha_pinning_required":false}`. The setting was re-read as `enabled=false` immediately before release-record correction; it is to remain disabled through merge and final readback.
- No GitHub Actions workflow was manually started or rerun, and no Actions result was used as acceptance evidence. No workflow file was changed. No deployment, force push, research-branch merge, Basket seal, Index unlock, or index headline was used or authorized by this acceptance receipt.
