# HO600 — synchronized progress and handoff · 2026-10-26

**Project:** TPI-001｜HO600 台灣私人物價籃  
**Repository:** [aitest00898/HO600-Taiwan-Private-Price-Basket](https://github.com/aitest00898/HO600-Taiwan-Private-Price-Basket)  
**Research branch:** `research/batch-09`  
**Directive:** GitHub Actions remain USER-PAUSED. Never dispatch, rerun, enable, or add Actions, and do not edit `main`, main workflow, canonical workbook, release controls or indexes in this handoff.

**Update note:** The sections below preserve the initial 2026-10-26 sync as history. The native acceptance continuation at the end supersedes its pending-test conclusions and earlier task counts.

## 1. Actual work synchronized on 2026-10-26

The latest authorized Linear TPI-001 readback contains 42 issue records. Compared with the existing committed GitHub CSV, **exactly one issue changed**:

| Issue | Previously pinned | Current authoritative Linear | Resolution |
|---|---|---|---|
| [OO1-154](https://linear.app/001dev/issue/OO1-154) | `Todo / P1` | `Backlog / P2` | Preserve Linear decision, update research-branch snapshots and tests, no Linear issue mutation |

At that initial readback, all other 41 issue IDs, statuses, priorities and Linear issue URLs matched the existing snapshot. **Initial same-day state: 35 Todo, 1 Backlog, 4 In Progress, 2 Done** = 42, **40 unresolved**. Priorities: **P0 6, P1 26, P2 10**. 24 registered `blockedBy` dependencies across 9 issues. This manual snapshot was dated **2026-10-26**; it was not a recurring or live synchronization.

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


## 2026-10-26 continuation: actual V8 interaction-logic execution (not device acceptance)

The continuation fetched **actual committed sources** from `research/batch-09` using the authorized GitHub connection and executed `dashboard/app.js` in the V8 JavaScript engine with a deliberately **mocked document/window, synthetic DOM event dispatch, URL and Blob**. Unlike earlier static string inspection and syntax parsing, this exercised real app initialization, filtering, view rendering and CSV generation logic. It is **not** a real browser engine/DOM, Apple Safari, Mac Node, native Python, or an iPhone test.

- **13/13 PASS**: price JSON/offline JS equivalence, task JSON/offline JS equivalence, original task CSV Git blob SHA matching snapshot pin (`20751e59f495c975fbef99a118ca221d82997695`), canonical lock invariants, tasks page initialization, default 40 unresolved rows, sole OO1-154 Backlog row, filtered Backlog CSV content, task export `2026-10-26` filename, OPEN P0 = 5 rows, ALL P0 = 6 rows, IUI P0 = 3 rows and IUI OPEN P0 = 3 rows.
- **10/10 PASS**: cohort page initialization, conservative 65+ A = 2.54%/+0.0447pp, full-rate HOLD guard, provisional 65+ A = 7.57%/+1.9018pp, provisional 65+ B = +1.7103pp, provisional 45–54 B = +2.3734pp, SPLIT_REQUIRED = 8 rows, actual generated CSV A/strict with 7 age rows, CSV explicitly `HOLD_NOT_A_FULL_RATE`, and CPI export retains independent older `2026-10-19` snapshot date.
- **Total newly executed logic assertions: 23/23 PASS, 0 FAIL**. Input app Git blob `2663d30955cb870533ee4b89d9a3a54efa1d73a3`; research report snapshot blob `be2be324ed67cb25c52d29f2f4c828cc34edf22c`; task snapshot blob `bf7dbbf5de28a118f35fc57185daa5f5eefd463c`. Mocked event tests are not counted as browser-native receipts or added to the authored 24 Python methods.
- **Environment blocker:** a direct GitHub clone from the separate execution container failed at DNS resolution (`Could not resolve host: github.com`); the repository was accessed instead through the authorized GitHub connector. Consequently the user's local Mac repository, 24 Python tests, Node runtime, Safari DOM, and actual iPhone are **not** claimed validated.
- **Remaining original gate, unchanged:** run the existing commands in section 4 on the user's Mac, retain actual Python/Node/real Safari smoke receipts; iPhone acceptance separate. No new Gate or new issue. OO1-160 stays Todo, OO1-166 In Progress, `main` 181/600 Basket NOT SEALED Index LOCKED. No Actions.
## 2026-10-26 continuation: native Mac checks and Safari DOM acceptance

This continuation supersedes the earlier pending-native-acceptance statements and status counts in the historical handoff above.

- The local `research/batch-09` checkout was clean at `10a9bd48b7fd0602798267898778dc77a63f4202` before `git pull --ff-only`; the pull fast-forwarded it to `ace4dbb39c2c9a9d9a0c47cb473fa759352accbf` (confirmed by Git reflog). No local edits were discarded.
- Runtime: Python 3.15.1, Node v22.23.1, macOS 27.0.1, Safari 27.0.1, Git 2.54.0 (Apple Git-157).
- `python3 dashboard/tools/check_todo_snapshot.py`: exit 0, local snapshot PASS; by design the no-export invocation reports `LIVE_LINEAR_DRIFT=UNVERIFIED_NO_EXPORT`. Fresh full 42-issue Linear export parity: exit 0, `PROVIDED_LINEAR_EXPORT_DRIFT=NONE`; counts 33 Todo / 1 Backlog / 4 In Progress / 4 Done.
- `python3 dashboard/tools/rebuild_snapshot_js.py --check`: exit 0, `SNAPSHOT_SYNC=PASS (semantically identical)`.
- `python3 -m unittest discover -s dashboard/tests -v`: exit 0, **24/24** cases passed.
- Node `--check`: exit 0 for `dashboard/app.js`, `dashboard/snapshot.js`, `dashboard/todo-snapshot.js`, and `dashboard/tests/browser-smoke.js` (4/4). `git diff --check`: exit 0.
- Task snapshot source CSV Git blob SHA: `f37a4e65bd2de56d6e55ba72ffa6507819caae2c`; JSON and offline JS are semantically identical. Snapshot totals are 42 issues, 38 unresolved, 24 dependency edges; priorities remain P0 6 / P1 26 / P2 10.
- The first real Safari smoke found one stale test expectation: after OO1-160/161 became Done, OO1-162 correctly displayed its prerequisites as closed. The smoke assertion was updated to match that verified state. A reload that retained `#tasks` also started away from the Overview page; the final run used the clean `?smoke=1` URL without a fragment.
- Native Mac Safari loaded the local `dashboard/index.html?smoke=1` page and exercised real DOM clicks, select changes, tabs, cohort modes/periods, CSV Blob content (download intercepted by the smoke), task filters, and dependency display. Final result: **37/37 PASS, 0 FAIL**, viewport 1470 × 746. Safari Web Inspector Console showed the single `HO600_BROWSER_SMOKE_RESULT` info record and no error or warning entries.
- Safari UA: `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/27.0.1 Safari/605.1.15`.
- Linear TPI-001 still contains 42 issues: **33 Todo / 1 Backlog / 4 In Progress / 4 Done**. OO1-160 and OO1-161 are Done with actual receipts; OO1-162 remains Todo for its separate physical-iPhone acceptance. The physical iPhone was not tested.
- Formal boundary unchanged: main 181/600, Basket NOT SEALED, Index LOCKED. No formal workbook edits, Actions, deployment, merge, or main changes.

### Complete captured `HO600_BROWSER_SMOKE_RESULT`

```json
{
  "passed": 37,
  "failed": 0,
  "total": 37,
  "cases": [
    {
      "name": "首頁正常渲染",
      "passed": true,
      "detail": ""
    },
    {
      "name": "首頁正式 419 缺口",
      "passed": true,
      "detail": ""
    },
    {
      "name": "首頁沒有完整年齡通膨率",
      "passed": true,
      "detail": ""
    },
    {
      "name": "行動選單遮罩元件已建立",
      "passed": true,
      "detail": ""
    },
    {
      "name": "價格籃分頁可切換",
      "passed": true,
      "detail": ""
    },
    {
      "name": "七個正式領域都有進度條",
      "passed": true,
      "detail": ""
    },
    {
      "name": "研究 C04 不視為正式完成",
      "passed": true,
      "detail": ""
    },
    {
      "name": "臺北市 CPI 分頁可切換",
      "passed": true,
      "detail": ""
    },
    {
      "name": "保守排除 09 為預設",
      "passed": true,
      "detail": ""
    },
    {
      "name": "保守 65+ A 覆蓋率 2.54%",
      "passed": true,
      "detail": ""
    },
    {
      "name": "保守 65+ A 部分貢獻 +0.0447 pp",
      "passed": true,
      "detail": ""
    },
    {
      "name": "完整年齡率仍 HOLD",
      "passed": true,
      "detail": ""
    },
    {
      "name": "暫定含 09 切換有效",
      "passed": true,
      "detail": ""
    },
    {
      "name": "暫定 65+ A 為 7.57%、+1.9018 pp",
      "passed": true,
      "detail": ""
    },
    {
      "name": "期間 B 可切換",
      "passed": true,
      "detail": ""
    },
    {
      "name": "暫定 65+ B 為 +1.7103 pp",
      "passed": true,
      "detail": ""
    },
    {
      "name": "年齡組切換可用",
      "passed": true,
      "detail": ""
    },
    {
      "name": "暫定 45–54 B 為 +2.3734 pp",
      "passed": true,
      "detail": ""
    },
    {
      "name": "需拆分類別篩選為八筆",
      "passed": true,
      "detail": ""
    },
    {
      "name": "CSV 匯出按鈕實際運作且測試下載被攔截",
      "passed": true,
      "detail": ""
    },
    {
      "name": "匯出檔反映 A 與 strict 模式",
      "passed": true,
      "detail": ""
    },
    {
      "name": "匯出檔明確 HOLD 非完整通膨率",
      "passed": true,
      "detail": ""
    },
    {
      "name": "匯出檔包含七個年齡組",
      "passed": true,
      "detail": ""
    },
    {
      "name": "證據分頁載入",
      "passed": true,
      "detail": ""
    },
    {
      "name": "至少七筆來源與 SHA 追溯",
      "passed": true,
      "detail": ""
    },
    {
      "name": "GitHub Actions 標記暫停",
      "passed": true,
      "detail": ""
    },
    {
      "name": "正式指數依然 LOCKED",
      "passed": true,
      "detail": ""
    },
    {
      "name": "Linear TODO 第五頁可切換",
      "passed": true,
      "detail": ""
    },
    {
      "name": "42張快照預設僅顯示38張未結任務",
      "passed": true,
      "detail": ""
    },
    {
      "name": "Linear狀態為33 Todo 1 Backlog 4進行中 4已完成",
      "passed": true,
      "detail": ""
    },
    {
      "name": "Backlog僅 OO1-154 一項",
      "passed": true,
      "detail": ""
    },
    {
      "name": "P0 篩選只保留未完成任務",
      "passed": true,
      "detail": ""
    },
    {
      "name": "P0 全部含結案共6張",
      "passed": true,
      "detail": ""
    },
    {
      "name": "IUI P0 共三張真機驗收任務",
      "passed": true,
      "detail": ""
    },
    {
      "name": "已完成前置狀態可見",
      "passed": true,
      "detail": ""
    },
    {
      "name": "IUI P0 僅 OO1-162 未完成",
      "passed": true,
      "detail": ""
    },
    {
      "name": "瀏覽器 viewport 有效",
      "passed": true,
      "detail": "手機寬度請在 Safari 響應式模式另測"
    }
  ],
  "viewport": {
    "w": 1470,
    "h": 746
  },
  "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/27.0.1 Safari/605.1.15"
}
```


## 2026-10-26 next research continuation — C04 3 WIP leads; current-only food 2020 quote

**Price research resumed at user request; iPhone OO1-162 intentionally deferred (unchanged Todo), independent of Batch 9.** Following original 197 `RESEARCHABLE-CURRENT-ONLY` candidates on `main`, target selected by original underfilled food subcategory (超市／自煮基礎食品 1/34, 33 missing), **not by observed price changes**.

- Existing `LEG-EC-311` = 光泉全脂鮮乳 936ml (not a new economic concept). Fresh verified contemporary [2020-04-08 FamilyMart campaign record](https://benlife.tw/20200408famimartnew/) explicitly reports **single-unit original/normal retail list NT$93**; **two-unit discount NT$169 is excluded**. This is dated third-party reporting and does not identify old barcode.
- [2026 live Wanjiafu merchant listing](https://online.uni-prosperity.com.tw/zh/%E5%85%89%E6%B3%89/1501003300101.html): 光泉100%純全脂鮮乳無調整 936ml **normal/struck-through NT$93**, **actual current promotion NT$88**. Original `main/data/Evidence.csv` already contained both 2026 normal 93 and other-channel 88, so do not reissue an existing current-price admission. Additional [search-indexed GreenPoint entry](https://sys.greenpoint.org.tw/GpConsumerApp/Function/CommodityMgt/Edit.aspx?SystemId=76ce91a4-4b09-40e2-a125-e70a6240322e) indicates barcode 4710105010113 and suggested 93 from the current registration, but direct opening 403 means this is **supplementary unverified source metadata**.
- **Price pair 93 → 93 is presently a cross-channel *benchmark* only**, **not an admissible Exact pair**. Historical FamilyMart vs current Wanjiafu merchant, old barcode/formulation unverified; status `HOLD_FIXED_CHANNEL_AND_SKU` and comparability provisional B. No 2020 shopping transaction price, no in-channel matching, no false 2026 93 payable-price claim.
- Appended **B09-C04-003** to existing [C04 WIP ledger](../research/batch-09/checkpoint-04-wip-ledger.csv) and detailed [C04 note](../research/batch-09/checkpoint-04-wip.md). C04 now **3 WIP leads: 1 PROVISIONAL, 2 HOLD**. The prior B09-C04-002 MUJI jute 2020 on-sale finding remains HOLD for primary dated and SKU continuity, despite contemporaneous third-party evidence.
- Prior MUJI 2026 adjustments for `LEG-EC-151/152/153/171/172`, and 2026 price increases for `LEG-EC-154/157/158/162/163`, were **already in canonical Evidence**, and were not rewritten or double-counted.
- **Still C04 0 checkpoint-certified**, C01–C03 **60 research-qualified**, `main` **181/600**, 419 formal missing, NOT SEALED, LOCKED. No Actions, main, workbook, release, new gate or deployment.
- **Target for next legitimate advancement:** find original 2020/2026 **same-channel** normal list evidence and old identity continuity for `LEG-EC-311`; otherwise retain HOLD and immediately pivot to another underfilled legacy candidate. Do not search this same blocker indefinitely. Mac Dashboard acceptance remains closed (OO1-160/161 Done) and physical iPhone Todo is not a blocker.


## 2026-10-26 continuing product research — same-merchant milk list-price time bridge

User requested next substantive step and explicitly deferred physical-iPhone acceptance. No Dashboard retest, Actions use, or main release.

Reusing current-only `LEG-EC-311` / `B09-C04-003` (no new concept), independent retrieved observations:

- **2020-04-08**: [FamilyMart third-party contemporaneous campaign account](https://benlife.tw/20200408famimartnew/), 光泉全脂/低脂鮮乳936ml *one bottle normal/original list price NT$93*, excluding promo two for NT$169.
- **2024-03-20 to 2024-04-16**: [onelife's FamilyMart event account](https://onelife.tw/a/20391), 光泉全脂鮮乳936ml **original single-item price NT$100**. This is the same **merchant** retail normal-price benchmark as the 2020 FamilyMart report, but **2024, not 2026**; exclude the bundled toast combination NT$109.
- **2026 indexed current delivery listing**: [Uber Eats FamilyMart (Sanchong) store catalogue](https://www.ubereats.com/tw/brand-city/sanchong-nwt/family-mart), 光泉全脂鮮乳936ml **NT$100**, source retrievable in the search index but not as directly opened product page without location/session. **Delivery-channel listing != FamilyMart walk-in shelf normal price**, so not a completed 2020→2026 price pair. [FamilyMart actual redemption table](https://nevent.family.com.tw/Preorder/EA/) supports current product availability, **not a dated price**.

**Interpretation:** the additional evidence shows a plausible **93 (2020)→100 (2024)** time bridge *within FamilyMart*, but **not** a formally accepted 2020→2026 pair. The existing WIP-ledger `93→93` continues to be a **cross-retailer benchmark** between 2020 FamilyMart and 2026 Wanjiafu list price, not an admitted observation; no inflation gain is computed from mixing those prices. 2020 full-fat UPC and 2026 in-store ordinary price still missing. B09-C04-003 stays `HOLD_FIXED_CHANNEL_AND_SKU`. See detailed [checkpoint-04-wip](../research/batch-09/checkpoint-04-wip.md) and original [WIP ledger](../research/batch-09/checkpoint-04-wip-ledger.csv). Recheck against real first-party evidence only; no repeated searches of the same unavailable primary source without new lead.

**Unchanged release/accounting:** C04 3 WIP (1 provisional + 2 HOLD), C04 checkpoint-certified 0, C01–C03 60 research PASS, formal main 181/600, NOT SEALED, Index LOCKED; Mac Dashboard OO1-160/161 Done, iPhone OO1-162 Todo deferred. No Actions.


## 2026-10-26 continuation — current-only hygiene C04-004, COSMED historical archive indexed only

**Research product:** original `LEG-EC-164` (Whisper 好自在液體衛生棉 34cm 10片), one of 197 existing current-only concepts, targeted due to scarce 日常／個人／盥洗／衛生用品 Exact (1/14, 13 lacking). Checked C01–C03 ledgers and main `Candidate_Pool.csv`/`Evidence.csv`; none of the three C01–C03 ledgers already admits this family, and original main Evidence already contains POYA 2026 NT$149, so no duplicate current price observation.

- **Search-indexed original COSMED brochure**: <https://www.cosmed.com.tw/upload/ebook/23/pdf/0706.pdf> surfaced with approximate circa-2020 publication and explicit 34cm10pcs **original NT$149**, separate from multi-buy **3 for NT$258**. However **the original PDF currently redirects to COSMED homepage (HTML)**, so its original page image and exact issue date **could not be independently inspected**. Do not claim an archival PDF screenshot, a verified 2020-07-06 date, or a certified primary observation.
- **Current official COSMED eShop, index only**: <https://shop.cosmed.com.tw/tagCategory/%E5%A5%BD%E8%87%AA%E5%9C%A8%2C%E5%A4%9C%E7%94%A8> describes Whisper liquid-material 34cm10pcs **normal/list NT$149 vs promotional NT$129**, with a **random package variant** caveat. Browser extraction only yields a JS iframe, not an independently inspected checkout; original label and channel remain tentative. POYA current NT$149 was already canonical evidence.
- **Research work unit added:** [C04-004 WIP](../research/batch-09/checkpoint-04-wip.md) + fourth 23-column row in [C04 WIP CSV](../research/batch-09/checkpoint-04-wip-ledger.csv), decision `HOLD_2020_ARCHIVE_AND_SKU`, pending original PDF/date, pack/barcode/generation, and offline-DM-vs-online-eShop channel parity. Do not substitute coupon/multi-buy price or assume same exact SKU. Original registered WIP format is preserved; no new governance prerequisites.
- **C04 WIP = 4 concepts (1 provisional + 3 HOLD)**, C04 checkpoint pass still 0, C01–C03 research pass 60, `main` 181/600 NOT SEALED INDEX LOCKED. iPhone OO1-162 intentionally deferred; native Mac OO1-160/161 closed and not retested. No GitHub Actions.
