# HO600 IUI Dashboard V0 — research-only delivery and acceptance ledger

**As-of:** 2026-10-19 (Taipei). **Repository:** `aitest00898/HO600-Taiwan-Private-Price-Basket`. **Working branch:** `research/batch-09`.

## Actual artifact

A new mobile-responsive, read-only, no-dependency static app resides in [`dashboard/index.html`](./index.html). It is **not** a GitHub Pages / cloud deployment and has no online app URL. On Mac, `open dashboard/index.html`; no server is required because `snapshot.js` is included as an ordinary local script, not fetched through an HTTP API.

**Files:** `index.html`, `styles.css`, `app.js`, `snapshot.json`, `snapshot.js`, `README.md`, `tools/rebuild_snapshot_js.py`, `tests/test_dashboard.py`.

**Functional views:** project overview, seven-domain quota/B09 research, Taipei age-head budget and CPI partial contribution, evidence/source/acceptance. Client interactions: responsive tab navigation, select A/B CPI windows, conservative excluding 09 (default) versus provisional 09 (explicit), per-age selector, crosswalk-status filter, per-view CSV download, links to exact GitHub sources. No network fetch, cookies, storage, logins, write APIs or Actions.

## Actual source snapshot and authority

- **Formal main pinned commit:** `88fa2b53774067faf740868bb8e168a04e47a8bf`; 181/600, remaining 419, candidates 418, evidence 1,566, seven-domain preserved-target sum 600; Basket NOT SEALED, Index LOCKED. Main `data/Validation_Release.csv`: 20/20 recorded checks PASS.
- **Prior research data pinned commit:** `fd30af9e3ba08e7855c289ad347fd0f2bec4d909`; Batch 9 C01–C03 = 60 research PASS, C04 = one provisional and one HOLD, no formal promotion.
- **Taipei source-validated survey:** seven age-head groups × 12 classes (84 weighted cells), 2020 source CSV and PDF parent-class values previously 96/96 matched and totals 8/8.
- **Taipei CPI original verified research:** monthly 16,560 records, annual 1,344, 48/48 class monthly grid valid up to 2026-09. *None of these rows is a complete age-head CPI rate.*
- **Crosswalk truth:** original analysis had 3 labelled `MAPPED`; later child-expense review found 09 `休閒與文化` ↔ `娛樂費用` high-risk provisional due to 40–50% package travel. Display classified **2 reliable-in-current-study, 1 PROVISIONAL, 8 SPLIT_REQUIRED, 1 UNMAPPED**. Historical results preserved, and conservative excluded-09 contributions are the **default** dashboard view.
- The exact reviewed sources and blob SHAs (seven files), branch commits and GitHub links are recorded inside `dashboard/snapshot.json`. Dataset is a **fixed snapshot, not a live GitHub feed**.

## Actually executed QA in assistant environment

- Used GitHub connector to retrieve and validate the authentic `main` and research data, independently assemble snapshot and check quota sums `181+419=600`, 7 age-head rows, both A/B windows, 12 crosswalk rows and zero full cohort rates.
- After commits, **fetched all browser assets and both snapshot formats back from GitHub** and executed **13 connector-side structural and quantitative invariant checks: 13/13 PASS**. Those include exact JSON/JS equality, seven quota totals, 60 research-only checkpoints, provisional 09, complete no-release gate, four navigation tabs, responsive CSS, real event controls and CSV export code, and no network-fetch use.
- A Python `unittest` suite with **15 authored cases** now exists, including one optional Node.js syntax check. **Not yet run in a local checkout; do not call it PASS.** Browser/Safari rendering and actual UI click/CSV export also **not yet executed** in this assistant environment because its container could not DNS-resolve even public GitHub raw files. The page was inspected via source and readback, not a browser screenshot.
- Generated assets remain **research-only** and do not modify canonical workbook or official release status.

## Minimal Mac/native verification (remaining genuine environment blocker)

```bash
git switch research/batch-09
git pull --ff-only
python3 dashboard/tools/rebuild_snapshot_js.py --check
python3 -m unittest discover -s dashboard/tests -v
node --check dashboard/app.js
node --check dashboard/snapshot.js
open dashboard/index.html
```

Manually inspect actual Safari (including iPhone-width responsive view). Check opening Overview card values; Basket quota `181/600`; Cohorts default `保守：排除09`, A window, age `65歲及以上` coverage `2.538838%`, partial `+0.044728 pp`; toggle `暫定：納入09` and verify `7.569986%`, `+1.901797 pp`; switch B and age labels; source links open correct GitHub pinned blob; export CSV and verify selected period/mode and no full age-rate column. Recheck after every repair.

If a specific tested behavior fails, fix **research branch only**, rerun and record exact results. There is no permission to re-enable GitHub Actions, deploy website, mutate repository visibility, update main or publish index.

## Unfinished by design

No full WORK/RETIRE rates; no national 2020 corrected source; no HO600 historical headline or final Index; no write-capable manager, backend, scheduled refresh, authorization, live apps or deployed domain.

**Delivery status:** `CODE_AND_VERIFIED_SNAPSHOT_COMMITTED`; `CONNECTOR_STATIC_CONTRACT_13_OF_13_PASS`; `NATIVE_BROWSER_ACCEPTANCE_PENDING`; `GITHUB_PAGES_NOT_CONFIGURED`; `CANONICAL_181_OF_600_LOCKED`.
