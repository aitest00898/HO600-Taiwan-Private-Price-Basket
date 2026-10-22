# HO600 handoff — 2026-10-22 | Continue non-GitHub-Actions work

**Directive:** User explicitly said *暫不使用 GitHub Actions，其餘任務繼續*. No workflow dispatched, rerun, configured, or changed in this continuation. `main` preserved.

## Actual newly committed outcomes

- **IUI fifth tab `專案 TODO` delivered as research-only source:** [dashboard/index.html](../dashboard/index.html) + [app.js](../dashboard/app.js), offline [42-issue JSON](../dashboard/todo-snapshot.json) and [file:// JS](../dashboard/todo-snapshot.js). State now **36 Todo / 4 In Progress / 2 Done**. Priority/group/status/registered blockers, filtered export and Linear/source links; normal offline app has no API.
- **Manual no-Actions drift contract + fail-closed checker:** [contract](../research/todo/LINEAR-GITHUB-SNAPSHOT-SYNC-CONTRACT-2026-10-22.md) and [script](../dashboard/tools/check_todo_snapshot.py), compares CSV Git blob SHA to JSON/JS, validates registered dependencies, optional current Linear export. Without a fresh Linear export its successful result must still state **LIVE_LINEAR_DRIFT=UNVERIFIED_NO_EXPORT**.
- **Source links fixed:** 3 previously truncated/invalid GitHub source URLs repaired in both the [CSV](../research/todo/HO600-TODO-2026-10-20.csv) and offline snapshots.
- **Quality checks (actually run by assistant):** 19/19 GitHub readback/semantic invariants; 3/3 source JS V8 syntax compile. **New Python suite now has 24 authored methods**; not run on user's Mac. Real Safari/iPhone remains pending.
- **Batch 9 C04:** 2021 dated secondary "recent Taiwan launch" is not proof that the March 2020 projected June launch actually occurred. C04-002 remains `HOLD_2020_IN_MARKET`; no C04 checkpoint-certified rows. [WIP memo](../research/batch-09/checkpoint-04-wip.md).
- **Taipei CPI 09:** September 2026 official Taipei first-party release again confirms overseas tour fees affect entertainment CPI, but whole 09 household 2020 spending cannot be indiscriminately assigned. `09_PROVISIONAL`, complete age rates 0/7 [scope memo](../research/cohort-inflation/CPI-09-OFFICIAL-TOUR-INCLUSION-REVIEW-2026-10-21.md).
- Linear statuses progressed: [OO1-134](https://linear.app/001dev/issue/OO1-134), [OO1-166](https://linear.app/001dev/issue/OO1-166), [OO1-143](https://linear.app/001dev/issue/OO1-143) now In Progress, previous [OO1-147](https://linear.app/001dev/issue/OO1-147) remains In Progress. No extra Done claimed.

## Verified authority / open gates

Formal `main` commit `88fa2b53774067faf740868bb8e168a04e47a8bf` remains Batch8 **181/600**, remaining 419; 418 candidates and 1566 evidence, Basket **NOT SEALED**, Index **LOCKED**. Research C01–C03 60 admissible not formally promoted; C04 2 WIP. National WGT 0/2, age-head complete CPI 0/7. User-paused Actions stay paused; repository platform toggle unknown, no attempt to use settings API for state changes.

## Remaining shortest permitted next steps (independent streams)

1. **IUI Mac-native:** run `python3 dashboard/tools/check_todo_snapshot.py`, `python3 dashboard/tools/rebuild_snapshot_js.py --check`, `python3 -m unittest discover -s dashboard/tests -v` (**24 authored methods**), `node --check` four JS files, Safari `dashboard/index.html?smoke=1` and real iPhone local-lan smoke. Store receipt, fix issues in research branch, no main writes.
2. **Price research:** work first from [50-class prioritized source index](../research/triage/HO600-50-SUBCATEGORY-GAP-2026-10-21.csv) with 16 subcategories having no candidate and 22 zero Exact. Additional prospective sources must be actual contemporaneous 2020 list/normal price and matching 2026 identity, with source/brand caps; do not add unverified items to formal index.
3. **CPI research:** acquire official 2021-base CPI item list and map all four age-head leisure/culture child categories; 2026 official press only confirms tours in entertainment category. National WGT official verified original files remain a separate gate. No complete group inflation claims.
4. **Linear:** task-state authority is [Linear TPI-001](https://linear.app/001dev/project/tpi-001ho600-台灣私人物價籃-46e14167f961). Dashboard is a manually reviewed fixed snapshot. New issue completions require explicit receipt and review, then regenerated CSV/JSON/JS. No background automatic synchronizer has been set up.

[Full new acceptance ledger](../dashboard/ACCEPTANCE-2026-10-22.md) has specific checks, honest limitations, and Mac commands.

**Status at handoff:** `RESEARCH_SOURCE_AND_IUI_V0_TODO_TAB_DELIVERED`; `19_STATIC_INVARIANTS_PASS`, `3_JS_V8_COMPILE_PASS`; `PYTHON24_NATIVE_PENDING`, `SAFARI_IPHONE_NATIVE_PENDING`; `ACTIONS_USER_PAUSED`; `CANONICAL_NOT_RELEASED`.
