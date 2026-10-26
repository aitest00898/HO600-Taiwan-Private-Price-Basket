# Linear ↔ GitHub ↔ IUI task snapshot contract · HO600 TPI-001

**Prepared 2026-10-22 Asia/Taipei.** The `TPI-001｜HO600 台灣私人物價籃` project is the only task-status authority. GitHub research branch hosts a reviewed historical **copy**, and IUI consumes this frozen offline copy. Other projects or teams must never enter this file.

## Source-of-truth responsibilities

| Surface | Role | Who may change | Not authoritative for |
|---|---|---|---|
| Linear TPI-001 Issue (OO1-xxx) | Issue ID, title, priority, status, blockers, completion criteria, receipt links | Authorized human/Linear connector write | Canonical prices/index |
| `main` canonical HO600 data | Formal Exact counts, workbook, evidence, release gates | Separate explicit canonical admission process | Task completion |
| `research/batch-09/research/todo/HO600-TODO-2026-10-20.csv` | Human-reviewed machine-readable task register | Research-branch reviewer following Linear readback | Live Linear status or admission |
| `dashboard/todo-snapshot.json` + `todo-snapshot.js` | IUI immutable `file://` view with reference to CSV Git *blob* SHA | Research-branch reviewer after CSV and Linear crosscheck | Real-time monitoring, grants |
| `dashboard/snapshot.json` | **Separate** formal and Taipei CPI numerical research snapshot | Research-branch reviewer after independently verifying `main` and study sources | Linear tasks |

The frozen issue set is **42** (as of 2026-10-22): **36 Todo, 4 In Progress, 2 Done**, 6 P0, 27 P1, 9 P2; 24 registered dependency edges across nine issues. **40 not Done**. Provenance: Linear TPI-001 connector readback compared with actual GitHub TODO CSV; no GitHub Actions used.

## 2026-10-26 revision (additive to the 2026-10-22 baseline)

Fresh authorized Linear readback yielded exactly **one issue change**: `OO1-154` transitioned from `Todo / P1` to `Backlog / P2`. The 2026-10-26 first snapshot recorded **35 Todo, 1 Backlog, 4 In Progress, 2 Done**; **6 P0, 26 P1, 10 P2**; 42 total / 40 unfinished / 24 links. A later same-day native Dashboard acceptance continuation is recorded below. Readback and sync are manual, not periodic/background and do not authorize workflow automation. `BACKLOG` is an unresolved planning state, not `DONE`, nor a hold/release decision in canonical pricing.

### 2026-10-26 native Dashboard acceptance continuation

After the initial task snapshot above, local Mac checks and real Safari DOM interaction passed. Linear OO1-160 and OO1-161 were then updated to `Done` with execution receipts; latest same-day distribution is **33 Todo, 1 Backlog, 4 In Progress, 4 Done** (38 unresolved; priorities P0 6 / P1 26 / P2 10; 24 dependency edges). The research CSV and offline JSON/JS snapshot pin these two completed records. OO1-162 remains `Todo` pending its separate physical-iPhone test. The Dashboard reflects the latest manual task readback only; this does not alter the separate CPI snapshot or canonical state.

## Update protocol (explicit/manual, not a background sync)

1. **Read** fresh complete Linear TPI-001 issues and their blockers (including exact issue IDs and URLs). Scope exact project `P-OO1-11`. Check correct membership, count, title, status, priority and updated-at time.
2. **Compare** to last reviewed GitHub TODO CSV. A status mismatch is not an error to be silently overwritten: reconcile each changed issue and attach real evidence/acceptance receipt; leave blocked tasks not Done when validation is missing.
3. **Review** 42 source and Linear URLs; GitHub source links must be full `/blob/<ref>/...` or other known valid repo routes, never a truncated ellipsis.
4. **Update** research-branch CSV only; do not modify formal `main`, workbook, Index, or Actions.
5. Pin **Git blob SHA** of updated CSV in `dashboard/todo-snapshot.json.authority.githubTaskCsvBlobSha`, and update JSON task rows (status, links, acceptance, dependencies) from reviewed Linear + CSV. Generate identical `todo-snapshot.js` (for direct `file://` usage). A new snapshot is a visible versioned event, never silently treated as live.
6. Run `python3 dashboard/tools/check_todo_snapshot.py` and `python3 -m unittest discover -s dashboard/tests -v`; run Node syntax and Safari actual UI tests when possible.
7. If a **fresh complete** Linear export is available as local JSON, run `python3 dashboard/tools/check_todo_snapshot.py --linear-export /path/to/export.json`. Any mismatch exits nonzero and must be investigated. If no fresh export, checker says **`LIVE_LINEAR_DRIFT=UNVERIFIED_NO_EXPORT`**; it only proves local source parity.
8. Read back remote GitHub files and updated commit SHA; record completed tests versus tests merely authored. Do not label device acceptance successful without an actual test receipt.

## Safety and status semantics

- `Todo`, `Backlog`, `In Progress`, `Done` are **workflow states**, not formal index release gates. `Done` means that one issue's specific deliverable has receipts; an upstream completed blocker does not automatically finish a downstream issue.
- `blockedBy` includes only **explicitly registered** dependencies. Empty dependency list is **NOT** proof the issue is immediately executable; external sources, approvals, hardware or official classification can still block.
- Tasks paused by user (especially GH Actions) remain as research work history but must **not** be executed or automatically resumed. This update explicitly does not use GH Actions.
- At the first 2026-10-26 snapshot the Dashboard defaulted to 40 unresolved tasks; following native acceptance, the current default is **38 unresolved tasks**. `taskStatus=ALL` reveals four Done issues (two earlier completions plus OO1-160/161). Filters affect only presentation/export; nothing writes to Linear.
- Freshness cannot be verified by a GitHub file alone. Report `NO_FRESH_LINEAR_EXPORT` rather than claiming current Linear state unless the connector was actually queried in that turn.

## Known unverified elements

- The 24 Python methods and true Mac Safari/iPhone DOM tests are **authored**, **not yet executed on user hardware**. V8 compile and GitHub SHA/readback are not equivalent.
- GitHub settings-level Actions enablement unknown. Preserve pause; do not attempt manual dispatch, modify workflow or merge into main.
- No recurring/offline scheduler is being created; every snapshot refresh requires a new explicit review workflow.

**Status:** `MANUAL_SNAPSHOT_PROTOCOL_IMPLEMENTED` / `OFFLINE_CHECKER_CODE_COMMITTED` / `DEVICE_ACCEPTANCE_PENDING`. Related Linear: [OO1-134](https://linear.app/001dev/issue/OO1-134) (in progress), [OO1-166](https://linear.app/001dev/issue/OO1-166) (in progress).
