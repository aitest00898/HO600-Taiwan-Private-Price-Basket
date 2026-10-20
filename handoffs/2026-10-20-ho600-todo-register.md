# HO600 TODO registration handoff — 2026-10-20 (Asia/Taipei)

**Outcome:** Persistent HO600 project TODOs registered and deduplicated in the existing [Linear TPI-001 project](https://linear.app/001dev/project/tpi-001ho600-台灣私人物價籃-46e14167f961). This handoff records management changes only, **not research/program completion**.

## Counts and provenance

- Existing five issues **OO1-102–106** retained and updated with latest evidence; `OO1-102` renamed to reflect C01–03 60/60 researcher-admissible and C04 two WIP entries.
- **37 new Linear issues OO1-130–166**, all `Todo`; no duplicate Linear project created. **Total in TPI-001 = 42 Todo**: **P0 6, P1 27, P2 9**, Done 0.
- Six represented domains: GitHub governance & safety, formal 600-item shortfalls and Batch9, Taipei 2020 age-head + CPI 12-class mapping, national WGT-01–05, IUI Dashboard V0 actual Mac/iPhone acceptance and deployment assessment, final workbook/seal/index gates.
- Nine issues have **24 actual Linear blockedBy relationships**: `OO1-103`, `OO1-105`, `OO1-154`, `OO1-159`, `OO1-161`, `OO1-162`, `OO1-163`, `OO1-164`, `OO1-166`; examples were independently read back via `get_issue(includeRelations=true)`.
- GitHub snapshot: [`TODO.md`](../TODO.md) plus [machine-readable CSV](../research/todo/HO600-TODO-2026-10-20.csv). Each of 42 rows links the actual Linear ID, priority, source, acceptance summary and prerequisite IDs.
- Latest baseline before these two GitHub docs was research HEAD `a8e1532389cd9b89b033c6c60b18ff4775e55e36`, main `88fa2b53774067faf740868bb8e168a04e47a8bf`. GitHub documents themselves were created at commits `947429fbe46350fd9d43e954e663d1afd4b4395a` (CSV) and `7235769b6edffa261b5608195a26eed7eb33b508` (TODO.md).

## P0 immediate subset

- [OO1-130](https://linear.app/001dev/issue/OO1-130) — verify real Actions disable state and main auto triggers **read-only**.
- [OO1-131](https://linear.app/001dev/issue/OO1-131) — investigate prior 2026-10-15 push-triggered workflow runs; no rerun.
- [OO1-147](https://linear.app/001dev/issue/OO1-147) — verify high-impact category 09 entertainment mapping.
- [OO1-160](https://linear.app/001dev/issue/OO1-160) — Mac local Python 18/Node syntax check.
- [OO1-161](https://linear.app/001dev/issue/OO1-161) — Mac Safari functional acceptance, depends on OO1-160.
- [OO1-162](https://linear.app/001dev/issue/OO1-162) — real iPhone Safari acceptance, depends on OO1-160/161.

## Explicit HOLDs

- **Formal main:** 181/600, remaining 419, `Basket NOT SEALED`, `Index LOCKED`; Linear task creation never changes these values.
- **2020 Taipei:** age-head proxy only, seven full age-inflation values `HOLD`; 09 class provisional and 01 food/04 housing/06 medical mandatory mapping insufficient.
- **National WGT:** government 2020 corrected source not retrieved under strict TLS; national working/retired weights 0/2.
- **Dashboard:** 10 files committed, native Python/Node/browser/iPhone and cloud website deployment pending; no CI/Actions triggered.
- **Repo policy:** Public visibility observed, original sources reuse/legal rights pending review. No secrets or restricted original files newly uploaded as part of task registration.

## Next workflow

Linear is the task/state authority. GitHub only holds **snapshot** and receipts. When tasks are executed, owner must link tested SHA/raw evidence and explicitly separate `WIP`, `PASS`, `HOLD`, formal `main` acceptance and deployment; incrementally update Linear first, then regenerate GitHub TODO index from current project source. Never assume a successful write of a TODO is a successful execution of that task.

**No GitHub Actions, main changes, official workbook writes, merges, staging deploys or release policy changes were undertaken for this task.**
