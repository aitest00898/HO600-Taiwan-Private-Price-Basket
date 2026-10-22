# HO600 IUI + CPI + Batch9 acceptance ledger — 2026-10-22

**Summary:** The user explicitly paused ALL GitHub Actions use. This change set performs only research-branch GitHub file writes, official evidence reading and Linear issue updates. It did not use Actions, edit main, change repo settings, merge or deploy.

## Delivered program features

- `dashboard/index.html`: new fifth `專案 TODO` navigation tab and `todo-snapshot.js` load; four original pages preserved.
- `dashboard/app.js`: renders current **reviewed historical 42 Linear issues** with 36 Todo, 4 In Progress, 2 Done; status, P0/P1/P2, work line, registered outstanding dependencies, issue links, source links, and **filtered CSV** export. Default shows **40 not Done**. Every label and URL is escaped; no new HTTP fetch, authentication, storage or API write. Header now displays the **TODO as-of 2026-10-22** independently from original financial data snapshot 2026-10-19.
- `dashboard/todo-snapshot.json`, `dashboard/todo-snapshot.js`: identical task data, 42 unique Linear OO1 IDs, 24 dependency links, exact Git blob SHA pin of updated source CSV.
- `research/todo/HO600-TODO-2026-10-20.csv`: preserved historical filename for existing references but synced actual **2026-10-22** Linear statuses; fixed three truncated/missing blob URLs.
- `dashboard/tools/check_todo_snapshot.py`: fail-closed, **network-free**, Python stdlib source consistency (CSV blob SHA, JSON/JS parity, status and blockers, acceptance, source) and optional `--linear-export` explicit fresh Linear readback. When no export supplied, it never claims live drift was checked; output should state `LIVE_LINEAR_DRIFT=UNVERIFIED_NO_EXPORT`.
- `dashboard/tests/test_dashboard.py`: authored **24** test methods (up from 18). `dashboard/tests/browser-smoke.js`: opted-in actual DOM checks now include fifth tab, filters and dependencies, alongside original CPI/CSV/mobile controls.
- [Manual authority/refresh/role contract](../research/todo/LINEAR-GITHUB-SNAPSHOT-SYNC-CONTRACT-2026-10-22.md).

## Independent actual checks performed in ChatGPT code environment

**GitHub connector readback + V8 assertions: 19/19 PASS** at the reviewed source state:
1. 36 Todo, 4 In Progress, 2 Done
2. All 42 unique IDs
3. JSON equals JS
4. CSV blob SHA pin
5. 42 CSV task records
6. Priority counts 6/27/9
7. 24 registered blocker edges
8. All blocker IDs stay in project
9. 40 unresolved default rows
10. Five unresolved P0 rows
11. Six total P0 rows
12. Three IUI P0 rows
13. No truncated task source links
14. Fifth tab wired
15. Independent per-tab snapshot time
16. No HTTP fetch in app or smoke
17. Local source-checker verifies pinned hash and states freshness limit
18. Python suite has 24 authored test methods
19. Canonical main 181/600 and LOCKED.

**Actual V8 compile:** `dashboard/app.js`, `dashboard/todo-snapshot.js`, `dashboard/tests/browser-smoke.js`: **3/3 PASS**. This is only source-level JavaScript compile and numeric/snapshot assertions, **not** Mac Node, Safari DOM or iPhone hardware validation.

## Non-IUI tasks progressed (never promoted to new Exact)

- Batch 9 C04 A3 MUJI planned launch 2020-03-06 vs 2021-05-21 Taiwan retrospective: evidence conflict; no proof of 2020 actually offered normal price; **C04-002 HOLD**. [Research ledger](../research/batch-09/checkpoint-04-wip.md).
- Taipei CPI division 09: September 2026 official Taipei CPI press also ties overseas group tours to `娛樂費用` annual +4.84% and month −1.76%; tour inclusion supported, but books/equipment and the entire survey 09 denominator **not** proven comparable. [Memo](../research/cohort-inflation/CPI-09-OFFICIAL-TOUR-INCLUSION-REVIEW-2026-10-21.md). **No complete age-inflation rates (0/7).**

## Mac-native verification still outstanding

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

The Mac must record Python method count/exit code, source snapshot hash check, Node syntax checks and the browser `HO600_BROWSER_SMOKE_RESULT` receipt. An actual iPhone Safari run over a trusted private LAN remains separate. **No native Python or browser PASS is asserted in this ledger.**

## Linear task statuses

- [OO1-134](https://linear.app/001dev/issue/OO1-134), [OO1-166](https://linear.app/001dev/issue/OO1-166), [OO1-143](https://linear.app/001dev/issue/OO1-143), [OO1-147](https://linear.app/001dev/issue/OO1-147): `In Progress`.
- Previously completed `OO1-131` historical actions root cause and `OO1-135` fifty-class gap index stay `Done`.
- Other **36 Todo**, including native browser, official full CPI and nationwide WGT gate. GitHub Actions execution remains user-paused.

**CANONICAL**: main Batch8 181/600, Basket NOT SEALED, Index LOCKED. Do not infer formal progress from new IUI task controls, partial CPI contribution or C04 announcements.
