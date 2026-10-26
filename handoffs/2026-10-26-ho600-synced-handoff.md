# HO600 — synchronized progress and handoff · 2026-10-26

**Project:** TPI-001｜HO600 台灣私人物價籃  
**Repository:** [aitest00898/HO600-Taiwan-Private-Price-Basket](https://github.com/aitest00898/HO600-Taiwan-Private-Price-Basket)  
**Research branch:** `research/batch-09`  
**Directive:** GitHub Actions remain USER-PAUSED. Never dispatch, rerun, enable, or add Actions, and do not edit `main`, main workflow, canonical workbook, release controls or indexes in this handoff.

## 1. Actual work synchronized on 2026-10-26

The latest authorized Linear TPI-001 readback contains 42 issue records. Compared with the existing committed GitHub CSV, **exactly one issue changed**:

| Issue | Previously pinned | Current authoritative Linear | Resolution |
|---|---|---|---|
| [OO1-154](https://linear.app/001dev/issue/OO1-154) | `Todo / P1` | `Backlog / P2` | Preserve Linear decision, update research-branch snapshots and tests, no Linear issue mutation |

All other 41 issue IDs, statuses, priorities and Linear issue URLs matched existing snapshot. **Latest state: 35 Todo, 1 Backlog, 4 In Progress, 2 Done** = 42, **40 unresolved**. Priorities: **P0 6, P1 26, P2 10**. 24 registered `blockedBy` dependencies across 9 issues. This latest snapshot is **2026-10-26**; it is not a recurring or live synchronization.

The only two Done issues remain [OO1-131](https://linear.app/001dev/issue/OO1-131) (historical Actions trigger forensics) and [OO1-135](https://linear.app/001dev/issue/OO1-135) (50-subcategory gap ledger). Existing In Progress: [OO1-147](https://linear.app/001dev/issue/OO1-147) (CPI class 09), [OO1-143](https://linear.app/001dev/issue/OO1-143) (Batch9 C04), [OO1-134](https://linear.app/001dev/issue/OO1-134) (snapshot consistency checks), [OO1-166](https://linear.app/001dev/issue/OO1-166) (IUI TODO tab). **No new Done has been claimed.**

### Changed files in this synchronization

- [Research TODO CSV](../research/todo/HO600-TODO-2026-10-20.csv) (historical filename retained so prior links stay valid): only OO1-154's `status` and `priority` columns changed.
- [`dashboard/todo-snapshot.json`](../dashboard/todo-snapshot.json) and [`todo-snapshot.js`](../dashboard/todo-snapshot.js): same 42 IDs and source URLs, date revised to `2026-10-26`, and pinned to updated TODO CSV's **Git blob SHA**. JSON and offline JS are exactly equivalent.
- [`dashboard/app.js`](../dashboard/app.js): `BACKLOG` is an unresolved state in the 42-record Gate; task filter now offers Backlog explicitly; headline includes Backlog; filtered task CSV export filename uses the **task snapshot date** instead of the older CPI/pricing date. Default unfinished view remains **40** rows, not 39.
- [`dashboard/tools/check_todo_snapshot.py`](../dashboard/tools/check_todo_snapshot.py): read-only Backlog validation, per-state totals, CSV SHA pin and optional authorized fresh Linear JSON parity. Without export it prints `LIVE_LINEAR_DRIFT=UNVERIFIED_NO_EXPORT`.
- [`dashboard/tests/test_dashboard.py`](../dashboard/tests/test_dashboard.py) and [`tests/browser-smoke.js`](../dashboard/tests/browser-smoke.js): author-defined methods remain **24** and optional DOM smoke now checks the singleton `OO1-154` Backlog filter. No browser-native PASS is claimed.
- [`TODO.md`](../TODO.md): status and P0/P1/P2 totals corrected, actual OO1-154 row moved **P1 table → P2 table**, historical 10/21–22 notes preserved; [`dashboard/README.md`](../dashboard/README.md) and [source-of-truth contract](../research/todo/LINEAR-GITHUB-SNAPSHOT-SYNC-CONTRACT-2026-10-22.md) revised additively.

### Actual checks in assistant's connector / JS engine

**25/25 GitHub + latest Linear cross-source structural checks PASS**, including:
- all 42 IDs and issue URLs matched Linear and GitHub source CSV;
- current status/priority of **all 42** matched, only OO1-154 changed;
- JSON and file:// JS payload identical, TODO CSV's Git blob SHA matched pin;
- 35+1+4+2=42; 6+26+10=42; 40 unresolved, 24 dependency edges, no cross-project links;
- `main` preserved 181/600 and Index LOCKED;
- Backlog filter/guard, task-specific export date, five tabs and smoke check present;
- Python test file contains 24 **authored methods**;
- `app.js`, `todo-snapshot.js` and `browser-smoke.js` each successfully parsed by **V8 3/3**.

**Important limitation:** These checks were readback and JavaScript syntax/structure checks only. The 24 Python tests, Mac Node runtime checks, actual Safari DOM click/CSV, and a physical iPhone have **not** been run or accepted on user's device. Do not conflate static/compiled code with native acceptance.

## 2. Formal price / CPI gate unchanged

- **Authoritative `main`** `88fa2b53774067faf740868bb8e168a04e47a8bf`, Batch 8 formal **181/600**, **419 missing**, 418 candidate concepts, 1,566 evidence records. Canonical workbook `workbook/HO600-WIP_shortfall-search_batch8.xlsx` with recorded SHA-256 `c01bce376e45e715d9b8eac4f353c61d20b5973e1e1c4e32f90a6e512bed40b9`. **Basket NOT SEALED**, **Index LOCKED**.
- **Batch 9 C01–C03** 60 **research-grade** `ADMISSIBLE` entries, **0 formal promotions**. C04: one `PROVISIONAL_ADMISSIBLE` and one `HOLD_2020_IN_MARKET` (MUJI A3 in-market 2020 not proven). No new Exact.
- [50-subcategory gap ledger](../research/triage/HO600-50-SUBCATEGORY-GAP-2026-10-21.csv): 22 subcategories have zero Exact, 16 have no candidate, now prioritized without price-change cherry-picking.
- **Taipei 2020 age-head**: 7 groups × 12 spending classes, 84 reviewed weight cells; CPI monthly 16,560 and yearly 1,344; full cohort rates **0/7 HOLD**. Class 09 tourism inclusion is supported by first-party source, but **whole class mapping remains PROVISIONAL**, not an accepted full rate.
- **National WGT**: original corrected nationwide XLS/ODS remains unconfirmed under strict TLS; nationwide work/retired household cohort weights **0/2**.
- **Price/CPI dashboard data snapshot** remains fixed to its older reviewed provenance (price & CPI UI as-of 2026-10-19). **Only task snapshot refreshed to 2026-10-26.** A successful TODO sync does not update financial source dates.

## 3. GitHub Actions safety

- The user explicitly requires **not using GitHub Actions**. No workflow was invoked, rerun, enabled or configured in this session; no push to `main`, no PR merge.
- On readback the research branch workflow has `workflow_dispatch` only, **but this is not authorization to dispatch it**. The untouched `main` workflow YAML still has `push` / `pull_request` rules.
- Workflow run history most recently shown at **2026-10-15 22:15:03 UTC**. No newly triggered run has been observed, but **repository-wide Actions enablement still UNKNOWN** because a settings-level authenticated read was not obtained. If ever necessary, [OO1-130](https://linear.app/001dev/issue/OO1-130) requires settings-only read; never restart Actions to test.

## 4. Smallest safe next steps / local acceptance (without Actions)

In the existing checked-out HO600 repository on Mac:

```bash
git switch research/batch-09
git pull --ff-only
python3 dashboard/tools/check_todo_snapshot.py
python3 dashboard/tools/rebuild_snapshot_js.py --check
python3 -m unittest discover -s dashboard/tests -v
node --check dashboard/app.js
node --check dashboard/snapshot.js
node --check dashboard/todo-snapshot.js
node --check dashboard/tests/browser-smoke.js
open -a Safari "$(python3 -c 'from pathlib import Path; print(Path("dashboard/index.html").resolve().as_uri()+"?smoke=1")')"
```

Record actual exit codes, Python case count, `HO600_BROWSER_SMOKE_RESULT`, and device version; only then evaluate [OO1-160](https://linear.app/001dev/issue/OO1-160) / [OO1-161](https://linear.app/001dev/issue/OO1-161). Physical iPhone [OO1-162](https://linear.app/001dev/issue/OO1-162) remains separate (private trusted LAN only).

Price/CPI work can proceed independently from [OO1-143](https://linear.app/001dev/issue/OO1-143) (C04 authentic normal historical price) and [OO1-147](https://linear.app/001dev/issue/OO1-147) (2021-base CPI item crosswalk). The stalled national WGT workflow is not a valid reason to prevent independent price or Dashboard checks. Do not add new Gate requirements or duplicate already-accepted receipts.

## 5. Handoff conclusion

**Disposition:** `RESEARCH_BRANCH_SYNCED` · `TASK_DRIFT_RESOLVED_ONE_ISSUE` · `STATIC_CROSSCHECK_25_OF_25_PASS` · `V8_PARSE_3_OF_3_PASS` · `NATIVE_PYTHON_SAFARI_IPHONE_PENDING` · `ACTIONS_USER_PAUSED` · `MAIN_UNCHANGED_INDEX_LOCKED`.

**Task authority:** [Linear TPI-001](https://linear.app/001dev/project/tpi-001ho600-台灣私人物價籃-46e14167f961).  
**Working branch:** `research/batch-09`.  
**No new governance project, no automatic schedules, no GitHub Actions, no canonical writes.**
