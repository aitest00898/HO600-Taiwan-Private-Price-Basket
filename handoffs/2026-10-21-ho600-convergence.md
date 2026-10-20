# HO600 — 2026-10-21 convergence execution handoff

**Result:** Two carefully scoped issues completed, one CPI source issue advanced, three GitHub evidence documents and one 50-class CSV committed. This work is **real evidence processing**, not merely a fresh 42-item backlog.

## Actual Linear changes

- [OO1-131](https://linear.app/001dev/issue/OO1-131) **DONE**: historical Actions push incidents audited against original exact workflow blobs and individual runs; [receipt](../research/triage/HO600-ACTIONS-HISTORICAL-ROOTCAUSE-2026-10-21.md). Did **not** verify repository-level Actions enabled/disabled status.
- [OO1-135](https://linear.app/001dev/issue/OO1-135) **DONE**: cross-joined 50 subcategories, 418 candidates, legacy raw evidence; [priority and provenance CSV](../research/triage/HO600-50-SUBCATEGORY-GAP-2026-10-21.csv). 50 subcategories; **181 Exact + 419 missing = 600**; **22 have zero Exact, 16 have zero candidates**. 1,267 of 1,566 evidence rows link directly to candidates; 299 `LEGACY_EVIDENCE_LEDGER` rows intentionally lack candidate ID, so **not lost and not candidates**. Quoted historical observations and sample URLs are **not requalified exact pricing**.
- [OO1-147](https://linear.app/001dev/issue/OO1-147) **IN PROGRESS**: official Taipei city CPI 2024-04-09 published data confirms domestic/foreign package group travel contributes to CPI 娛樂費用 (2021-base). This **corrects the old premise that tour spending was necessarily outside entertainment CPI**; does not certify all household 09 (books, equipment, culture), so **09 PROVISIONAL and seven full CPI rates HOLD**. [Official evidence review](../research/cohort-inflation/CPI-09-OFFICIAL-TOUR-INCLUSION-REVIEW-2026-10-21.md).
- [OO1-130](https://linear.app/001dev/issue/OO1-130) **TODO**: main workflow YAML still has automatic triggers. Connector rejected `actions/permissions`, `actions/workflows` and workflow settings endpoints; **platform-wide enabled/disabled switch UNKNOWN**, must be viewed by authorized user/admin, no security control changes without separate permission.
- [OO1-160](https://linear.app/001dev/issue/OO1-160) **TODO**: V8 compile syntax of fetched actual Dashboard `app.js`, `snapshot.js`, and `browser-smoke.js` **3/3 PASS**, blob SHA recorded on issue; this is NOT Mac Node, Python 18 tests, Safari or iPhone native acceptance.
- [OO1-134](https://linear.app/001dev/issue/OO1-134) remains **TODO**: manual Linear→GitHub status sync proved, but repeatable automated drift alerts/tested generator not yet built.

## Durable GitHub artifacts

- [`TODO.md`](../TODO.md): current task totals and progress, original full priority/dependency lists maintained.
- [`research/todo/HO600-TODO-2026-10-20.csv`](../research/todo/HO600-TODO-2026-10-20.csv): all 42 task IDs and 2026-10-21 status reconciliation despite original dated filename for backward compatibility.
- [`research/triage/HO600-ACTIONS-HISTORICAL-ROOTCAUSE-2026-10-21.md`](../research/triage/HO600-ACTIONS-HISTORICAL-ROOTCAUSE-2026-10-21.md).
- [`research/triage/HO600-50-SUBCATEGORY-GAP-2026-10-21.csv`](../research/triage/HO600-50-SUBCATEGORY-GAP-2026-10-21.csv).
- [`research/cohort-inflation/CPI-09-OFFICIAL-TOUR-INCLUSION-REVIEW-2026-10-21.md`](../research/cohort-inflation/CPI-09-OFFICIAL-TOUR-INCLUSION-REVIEW-2026-10-21.md).

## Current task counts

**42 issue total: 39 Todo / 1 In Progress / 2 Done** (40 unresolved). Keep 6 initial P0 issues in their original priority tier until independently reviewed. Existing `blockedBy` relations remain; a Done prerequisite does not authorize publication or new main writes.

## Next critical path

1. **Safety blocker** [OO1-130](https://linear.app/001dev/issue/OO1-130): authorized settings-only read to establish Actions repository enabled/disabled. Current GitHub public repo Actions history has 22 records, none after 2026-10-15 UTC; **no new runs observed is not proof of off**. If future main workflow edits are considered, get explicit authorization first.
2. **Research returns**: prioritized first source discovery for **16 subcategories with no existing candidate** and 22 categories zero Exact, based on actual [50-row gap ledger](../research/triage/HO600-50-SUBCATEGORY-GAP-2026-10-21.csv); separately check Batch 9 C04 historical MUJI product A3 launch/actual in-market proof, not advance a planned-release price.
3. **City CPI**: get exact **2021-base CPI item list** from official source and map all four 2020 household 09 subitems; distinguish tourism included in CPI from full 09 mapping accepted. Do not fabricate price class relatives.
4. **Dashboard native acceptance** [OO1-160→161→162]: in user's actual Mac checkout run `python3 dashboard/tools/rebuild_snapshot_js.py --check`, `python3 -m unittest discover -s dashboard/tests -v`, `node --check dashboard/app.js`, `node --check dashboard/snapshot.js`, `node --check dashboard/tests/browser-smoke.js`; only then open `dashboard/index.html?smoke=1` in Mac Safari followed by actual iPhone. Real output needed; we cannot infer it from V8 compile.

## Nonnegotiable boundaries

Main is still `88fa2b53774067faf740868bb8e168a04e47a8bf`, canonical Batch8 `181/600`, Basket **NOT SEALED**, Index **LOCKED**. C01–03 60 research PASS remain unpromoted; C04 two WIP, no C04 checkpoint certified. National WGT 0/2 and seven complete Taipei cohort rates 0/7. No GH Actions, main writes, merge, original dataset overwrite, deployment, or permissions changes performed during this convergence execution.

**Audit disposition:** `TWO_TASKS_CLOSED_WITH_RECEIPTS`, `ONE_CPI_MAPPING_PARTIALLY_RESOLVED`, `THREE_V8_SYNTAX_COMPILES_PASS_NATIVE_PENDING`, `FORTY_UNRESOLVED`.
