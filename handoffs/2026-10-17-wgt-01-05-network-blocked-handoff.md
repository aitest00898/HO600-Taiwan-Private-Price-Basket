# Handoff：HO600 WGT-01 至 WGT-05

**狀態：** `PARTIAL_WITH_EXTERNAL_BLOCKERS`；核心資料 Gate 維持 `HOLD`。  
**Repository：** `aitest00898/HO600-Taiwan-Private-Price-Basket`  
**分支：** `research/batch-09`  
**本地更新時間：** 2026-10-17 02:44:24 UTC（台北時間 10:44:24）  
**網路排障開始時遠端 HEAD：** `5a1fc853d96e25e413d0476d31ed5f1393460d38`（與 `research/batch-09` HEAD 相同）  
**完整驗收報告：** `research/cohort-inflation/WGT-2026-10-17-acceptance-report.md`  
**來源收據：** `research/cohort-inflation/wgt-2026-10-17-source-receipt.json`

## 已完成

- 已完整閱讀 `research/cohort-inflation/LOCAL-CODEX-WGT-2026-10-17.md`。
- 官方 109 年（2020）經濟戶長職業別及年齡別頁面、XLS 及 ODS 連結已確認；兩頁均載有 2026-02-13 修訂說明。
- 在提升網路權限下 DNS 已成功解析官方主機；五個嚴格 TLS HEAD 檢查（官方職業頁及四個 XLS／ODS URL）均於簽發者驗證失敗、HTTP 000。`curl --ca-native` 亦失敗。
- 官方下載器重試職業 XLS、年齡 XLS、年齡 ODS 三次均因 `CERTIFICATE_VERIFY_FAILED: unable to get local issuer certificate` 中止，原始快取仍為 0 檔。OpenSSL 嚴格驗證回傳 code 20；本機沒有修改 DNS／CA／憑證，也未略過 Safari 警告。
- 網頁來源代理先前回報 cache miss、502 及 timeout。自動審查拒絕了一個含 `curl -k` 的診斷命令，理由為該旗標停用 TLS 驗證；該命令未執行，也未再試圖繞過。
- 本機原始檔快取 `work/source-cache/` 為空。原始檔與轉檔檔案皆不存在；沒有聲稱下載、Numbers 轉檔、來源 SHA 或解析已完成。
- `validate_exposure.py` 結構檢查為 `PASS_STRUCTURAL_ONLY`；全體家庭索引摘錄的 12 類算術重算為 815,100 元／戶／年。該 CSV 原始 bytes 未驗證，不是受僱或高齡戶長權重。
- 指定 unit test 因系統 Python 3.14 與 bundled Python 3.12 均沒有 `artifact_tool`，無法收集任何測試；沒有改用不同解析器。

## WGT Gate

- **WGT-01：HOLD_TLS_CERTIFICATE_BLOCKED** — DNS 沙箱阻礙已排除至可解析；TLS 鏈無法驗證，兩份官方原始檔均未取得。
- **WGT-02：PARTIAL** — 官方頁確認 2020 年及 2026-02-13 修訂註記；原始檔位元組與版次未驗證。
- **WGT-03：HOLD** — 未轉 XLSX、未執行 `--inspect`，工作表及欄列映射未知。
- **WGT-04：HOLD** — 全體家庭索引摘錄只能作暫存算術檢查；職業與年齡兩組的原表總額均未對帳。
- **WGT-05：HOLD，0/2** — 未建立任何 proxy 支出權重。不得從職業或戶長年齡邊際表推導交叉矩陣。

## 恢復工作後的執行順序

1. 先由來源端或受信任網路環境提供可驗證的官方 TLS 憑證鏈。不要匯入未核實憑證或繞過 Safari 憑證警告；在有效 TLS 可用後重新執行下載。
2. 先確認 `work/source-cache/` 沒有既有檔案；以 `fetch_official_weight_tables.py` 下載 `NAT20-OCC` 和 `NAT20-AGE`。若 XLS 受阻，依官方頁測試年齡別 ODS。官方頁也提供職業 ODS；目前 extractor whitelist 只列職業 XLS，若改用該 ODS，先在研究分支擴充來源登記及測試。
3. 僅在實際拿到有效原始二進位檔後記錄下載 UTC 時間、官方 URL、HTTP 狀態、大小、簽章與 SHA-256。保留原檔，不覆寫，也不把原始 XLS／ODS 推上 GitHub。
4. 使用 Mac Numbers 將原檔另存為獨立 XLSX；保留原檔與轉檔檔案，記錄兩份 SHA-256。不得以 XLSX 雜湊替代原檔雜湊。
5. 在提供專案所需 `artifact_tool` Python module 的環境中先執行 `extract_revised_2020_cohort_xlsx.py --inspect <converted.xlsx>`，人工核實年份、工作表、標題、單位、註腳、12 類、戶長分組及明列總額。
6. 依實際單元格逐一覆核 mapping，分別建立 `OCC_HEAD_*_PROXY` 與 `AGE_HEAD_*_PROXY` 權重。只有類別列和來源總額獨立核對後才設 `reviewed: true`。
7. 執行原 extractor、完整 unit tests、`validate_exposure.py` 及獨立數值對帳。每組 12 類需非負、12 個不同列、合計在官方總額 12 元內；資料不足時保持 HOLD。
8. 同步報告、機器收據及 Handoff 至 `research/batch-09`。不修改 `main`、Actions、正式工作簿、Basket 或 Index。

## 必須持續遵守

- 經濟戶長職業別不代表所有受僱家庭；經濟戶長年齡別不代表真正退休家庭。
- 不用不同邊際表推導年齡 × 職業聯合樣本。
- 不從 proxy 推算 `HO600-WORK`、`HO600-RETIRE` 或「經驗通膨」。
- 若修正版原表與索引摘錄不同，記錄 `SOURCE_CONFLICT`；不得硬配 815,100。
- Canonical HO600 維持 181/600、Basket NOT SEALED、Index LOCKED。Batch 9 C01–C03 維持 60 項 research-level PASS，C04 維持 WIP；cohort extraction 與 private-price Basket 分開。Branch workflow 為 `workflow_dispatch`，不派送 Actions。

## 補充：2026-10-17 TLS 鏈問題與無相依的 CSV 驗收路徑

此段是新增研究計畫，不修改前述 Codex 原始執行紀錄、也不將任何 Gate 升格。

- 官方 TWCA 在 2026-04-15 公告 2026-05-04 更新新 CYBER Root 鏈，並警告部分 IIS 站台在 macOS/iOS 可能顯示不信任；公告：https://ssl.twca.com.tw/news_detail/ad2496ee-39cf-4d74-b44a-410470f99570 。此為**背景線索，並非已證實 DGBAS 使用 IIS**。
- 本機收據顯示 DGBAS leaf issuer = `TWCA SSL Certification Authority`，但另一批伺服器送出的憑證為 ePKI 政府 CA；應優先檢查伺服器中繼鏈是否缺失／不符，並確認 leaf SAN 是否包含 `ws.dgbas.gov.tw`。僅憑 leaf CN 為 `www.dgbas.gov.tw` 不能判斷 SAN 是否吻合。也不能排除本機系統 TLS 代理或憑證信任問題。
- [只讀 TLS 診斷程式](../research/cohort-inflation/diagnose_official_tls_readonly.sh) 使用 OpenSSL SNI+完整主機名驗證，比較 ws.dgbas、www.stat 及 TWCA 自有 HTTPS 站，收集葉憑證 SAN/issuer/AIA；**不安裝 CA、不停用驗證、不下載研究資料**。
- [原因判斷與排障規格](../research/cohort-inflation/TLS-ROOT-CAUSE-AND-CSV-FALLBACK-2026-10-17.md)。遇到需修改 Mac 信任庫時必須先取得明確許可；優先由伺服器/官方提供正確憑證鏈或已驗證的官方替代路徑。
- 本機 `artifact_tool` 缺少屬**獨立環境問題**：新增 [純 Python 標準函式庫 Numbers CSV 解析器](../research/cohort-inflation/extract_revised_2020_cohort_csv.py)、[11 個合成安全測試](../research/cohort-inflation/test_extract_revised_2020_cohort_csv.py)、[未覆核的 CSV mapping 範本](../research/cohort-inflation/cohort-weight-csv-mapping.template.json)。無須安裝新的 Python 試算表套件；但仍必須先合法、安全地取得原始 XLS/ODS、保存 SHA，再由 Numbers 匯出 CSV 並**人工覆核**列欄才能執行。
- 已將官方職業別 ODS `65.ods` 加入來源清冊、XLSX 解析器及 CSV 解析器的白名單。此為格式替代，**仍使用同一官方 TLS 主機，不能因此解決 TLS 問題**。
- 此次新增檔案均屬研究分支，尚未於使用者本機執行。2020 職業/年齡權重仍 0/2，WGT-01~05 不變，正式 main 181/600 且 Index LOCKED，Actions 依舊停用。

## Follow-up result — 2026-10-17 08:01 UTC

This follow-up supersedes the earlier TLS diagnosis protocol with actual local observations. Current branch base was `7d87ef5d7ba05ba7f932f41c58642176daba637a`; `git pull --ff-only` returned `Already up to date.`

- Strict OpenSSL handshakes: `ws.dgbas.gov.tw` and `www.stat.gov.tw` both failed verify code 20. Both received the same DGBAS leaf certificate; its SAN includes both hostnames, issuer is `TWCA SSL Certification Authority`, and AKI is absent from all ePKI certificates sent by `ws`. `www.stat.gov.tw` sent only the leaf. `ssl.twca.com.tw` passed verify code 0 with a key-identifier-matched chain; `curl --ca-native` to it returned HTTP 200 while the two official endpoints failed before HTTP (000).
- Classification: `TLS_ROOT_CAUSE_LIKELY`, a wrong/incomplete chain as presented by the official DGBAS endpoints. Empty macOS proxy configuration and no proxy environment variables make a configured proxy less likely. Transparent interception or managed TLS inspection is not conclusively ruled out. No TLS bypass, Safari warning bypass, CA trust change, or network setting change was made. The diagnostic results and private raw-log SHA-256 values are in `research/cohort-inflation/TLS-DIAGNOSTIC-RESULT-2026-10-17.md` and the source receipt.
- New pure-Python CSV tests: the first run found a zero-tolerance parsing bug. After correcting `positive_number` so numeric zero is not treated as empty, all 11 tests pass under Python 3.14.5. The test and extractor have no `artifact_tool` import; `artifact_tool` is not installed and is not needed for this CSV route.
- Independent general-household excerpt check: 12 categories, no negative values, category sum = declared total = 815,100 TWD/household/year; stored percentages total 99.999999%. Source bytes remain unverified and scope remains `ALL_HOUSEHOLDS_GENERAL`, so this does not pass WGT-04 or establish any proxy weights.
- No official raw XLS/ODS passed strict HTTPS. No file was downloaded, so raw and Numbers-converted SHA-256 values remain absent; Numbers conversion and actual XLSX/CSV extraction remain unperformed.

WGT-01 remains `HOLD_TLS_CERTIFICATE_BLOCKED`; WGT-02 partial metadata only; WGT-03/04 HOLD; WGT-05 HOLD 0/2. Next step is for DGBAS/TWCA or a trusted network operator to confirm/correct the certificate chain. If local trust changes are proposed, stop for explicit user authorization. No Actions, `main`, canonical workbook, Basket, Index, or cohort inflation release was touched.

## 2026-10-17 — Alternative official source feasibility review

After verifying Codex's latest TLS diagnostic and **11/11 synthetic CSV unit test PASS**, an external review found additional official alternative datasets, detailed in [`ALTERNATE-OFFICIAL-SOURCES-2026-10-17.md`](../research/cohort-inflation/ALTERNATE-OFFICIAL-SOURCES-2026-10-17.md).

- Taipei City official historical **head-age × 12 consumption division** CSV: https://data.gov.tw/dataset/133235 (the 2012–2023 source includes year 2020); **different** hostname `data.taipei`, but the raw CSV remains **NOT RETRIEVED** after web fetch errors / model-container DNS failure. This is a useful Taipei-only age proxy, *not* national WGT-01 and not actual retirees.
- Taipei district × consumption dataset: https://data.taipei/dataset/detail?id=d4142821-6cb6-4678-8fd6-709f620ced26; district not age/occupation; useful independent structural QA only.
- Official national account 12-consumption-group file: https://data.gov.tw/dataset/44226, but it is national accounts' private consumption not age/occupation household weights, **not** a WGT substitute. 2024 total-only age × income quintile dataset https://data.gov.tw/dataset/108265 also lacks 12-category detail.
- A separately labelled 2024+ Taipei district schema includes **13** divisions and renamed groups, requiring a documented classification bridge; do not naively join 2020 12-category values.
- Prior macOS TLS receipt strongly indicates bad/missing DGBAS intermediate. Optional diagnostic: authenticate the *exact* candidate intermediate using TWCA's officially HTTPS-served repository, compare AKI/SKI and cryptographic signature, run offline `openssl verify` with *system roots* remaining the exclusive trust anchors, without CA installs, `partial_chain`, or disabling TLS. Do not presume an intermediate's label establishes identity. Any later download must itself strictly validate hostname/chain; otherwise maintain WGT-01 HOLD.
- No original or cohort expenditure data downloaded in this follow-up. No Mac work or 11 synthetic tests rerun here. All WGT-01..05 outcomes unchanged; canonical main 181/600 and Index LOCKED, Batch9 C01..03 60 research PASS, Actions paused.



## 2026-10-17 — Exact official TWCA chain resources + Taipei CSV native-CA downloader

Research-only follow-up written to [TWCA-CERTIFICATE-AND-TAIPEI-RAW-RECOVERY-2026-10-17.md](../research/cohort-inflation/TWCA-CERTIFICATE-AND-TAIPEI-RAW-RECOVERY-2026-10-17.md). No WGT gate is promoted by adding the recovery code.

1. TWCA 2026-04-15 announcement supplies **exact issuer-chain HTTPS links** `https://sslserver.twca.com.tw/cacert/Cyber_SSL_2023.crt` and `https://sslserver.twca.com.tw/cacert/GlobalCrossCyber_2022.crt`. TWCA SSL CA subject and issuer are documented in the published CA inventory; live DER bytes **NOT downloaded**. The former matches DGBAS leaf's AIA URL after changing only scheme HTTP→HTTPS, confirmed by TWCA's own official link. Do not install root/intermediate.
2. New [Mac read-only native-CA issuer chain diagnosis](../research/cohort-inflation/verify_twca_chain_macos_readonly.sh): verified HTTPS fetch TWCA intermediates, records SHA/signature fields; native `security verify-cert -c leaf -c intermediate -c cross -p ssl -n ws.dgbas.gov.tw -L` uses existing **system anchors only** (no `-r`, no trust setting mutation). Even if offline chain validation succeeds, require independent real `curl --ca-native` strict HTTP success before downloading official XLS. WGT-01 remains HOLD otherwise.
3. New [Taipei historical age-head CSV official downloader](../research/cohort-inflation/fetch_taipei_age_2020_official_csv.py): original 2012–2023 source on `data.taipei`, official UUID `63e4d839-ef65-46a8-b4d1-1bbfeeca5516`, uses macOS `curl --ca-native`, checks 2020/ROC109 existence, expected detailed spending columns and UTF-8/CP950, rejects unexpected redirect, HTML/error and duplicate/nonstandard headers; stores SHA/source receipt only after valid bytes. [11 new synthetic tests](../research/cohort-inflation/test_fetch_taipei_age_2020_official_csv.py) are committed but **NOT RUN ON MAC**.
4. Local model container network for `data.taipei` and TWCA remained DNS-blocked; web fetch for CSV and PKIX certificates could not expose raw bytes. No 2020 city weights computed, original 2020 national raw source files still 0, national proxy weights 0/2. Taipei city is **not** nationwide and head age is **not** retirement.
5. Execute these two streams on the user's own Mac, record exact curl output/receipt and test results, fast-forward the research branch only. C01–C03 research 60 PASS, C04 WIP, canonical main 181/600 NOT SEALED/LOCKED, GitHub Actions paused.


## 2026-10-17 assistant-side execution completed; Mac-only tasks isolated

The assistant has itself attempted real original-binary downloads, not only researched possible sources. See the full audit [SELF-EXECUTION-AND-RESIDUAL-HANDOFF-2026-10-17.md](../research/cohort-inflation/SELF-EXECUTION-AND-RESIDUAL-HANDOFF-2026-10-17.md).

- Actual container DNS to four target hosts failed; direct Taipei CSV download via helper failed, web clicks on two official CSV links returned web-gateway `(400) OK`, and the two officially linked TWCA PKIX CA certificates could not be fetched as byte blobs due to unsupported media in web and local DNS failures. No Mac network success was inferred.
- NEW alternate source: the **official complete 2020 Taipei municipal household survey PDF** hosted by `www-ws.gov.taipei`, whose searchable index contains **Table 8: age-of-household-head × consumption expenses**. This gives an independent host/source **candidate** for regional 2020 12-category analysis if `data.taipei` CSV is inaccessible. Raw PDF retrieval and screenshot failed (cache miss); no numeric cells have been source-authenticated.
- Added [strict original report PDF fetcher](../research/cohort-inflation/fetch_taipei_2020_report_pdf.py) (native CA TLS, origin host check, PDF signature and EOF, timestamp and SHA-256 receipt, municipal-only scope), [7 offline PDF test fixtures](../research/cohort-inflation/test_fetch_taipei_2020_report_pdf.py). Source register now has 13 entries, including 2020 Taipei official report as `PDF_RAW_BYTES_NOT_RETRIEVED`.
- The assistant's Python container **does** have `artifact_tool` and successfully completed a 12-row synthetic XLSX export/re-import arithmetic smoke check; this does not authenticate actual sources and does not retroactively imply that original 7 repository tests passed on the user's Mac. The small conversation fixture XLSX is synthetic, not a genuine national cohort table.
- Minimum residual Mac steps: use [runbook](../research/cohort-inflation/SELF-EXECUTION-AND-RESIDUAL-HANDOFF-2026-10-17.md) for read-only TWCA chain check, 11 city CSV / 7 city PDF offline tests, strict native TLS city CSV and official PDF retrieval. Real government bytes first; proxy spend calculation only after exact age/12-category/page validation; retain national WGT-01..05 HOLD.
- This increment has **not** run anything on the user's Mac, has not changed system trust, has not published a CPI rate, and has not touched canonical `main` or dispatched GitHub Actions.

## 2026-10-17 follow-up: independent age-budget contrast and official Taipei CPI discovery

Verified GitHub HEAD at commencement: `552975440d437e6c96d7f367d9cdfaff675f1620`; independently inspected all 84 outputs of `TPE_AGE_HEAD_EXPENDITURE_PROXY_WEIGHTS_2020.csv`, compared original Mac reconciliations, and recalculated 7 age-group housing/health category sums and contrasts without projecting future prices.

- New [seven-age-group, 2020 Taipei budget-share summary CSV](../research/cohort-inflation/results/tpe-2020-age-head-proxy-20261017/tpe-2020-age-share-summary.csv) and [analysis](../research/cohort-inflation/TAIPEI-2020-COHORT-BUDGET-EXPOSURE-ANALYSIS-2026-10-17.md). 65+ household-head housing+health **51.6574%**, 45–54 **38.0520%** (+13.6054 pp), but respective *absolute* housing+health expense NT$456,319 versus NT$452,666 (+NT$3,653). **Higher share is not higher medical nominal outlays**: 65+ NT$153,271 medical, 45–54 NT$157,252. Different household spending denominators.
- New publicly verified official Taipei CPI datasets: [basic monthly](https://data.gov.tw/dataset/131822), [basic annual](https://data.taipei/dataset/detail?id=7ee57050-4d27-482c-bae5-ebd15ca86702), [broad monthly](https://data.taipei/dataset/detail?id=0cf1d853-b63c-4366-a611-217b2c419a1e), indexed in [`taipei-cpi-official-source-register-2026-10-17.csv`](../research/cohort-inflation/taipei-cpi-official-source-register-2026-10-17.csv). Annual metadata ends 2025; monthly must be examined for the **actual** latest 2026 month. Old broad-group CPI cannot be paired directly with twelve expenditure classes.
- New [strict official Taipei CPI basic month/year source capture utility](../research/cohort-inflation/fetch_taipei_cpi_basic_official.py), with two official direct resource URLs and [13 synthetic stdlib test cases](../research/cohort-inflation/test_fetch_taipei_cpi_basic_official.py). At this handoff, these tests are **committed, NOT RUN**; no CPI data bytes/real index/class mapping obtained. Native host container DNS failed for government and GitHub download domains; the authenticated Mac network is required for real data retrieval.
- Next Mac step only: execute 13 fixtures `python3 -m unittest discover -s research/cohort-inflation -p 'test_fetch_taipei_cpi_basic_official.py' -v`, then `python3 research/cohort-inflation/fetch_taipei_cpi_basic_official.py --source TPE-CPI-BASIC-MONTH --out /tmp/ho600-tpe-cpi-month` and `... --source TPE-CPI-BASIC-YEAR --out /tmp/ho600-tpe-cpi-year` using strict macOS CA TLS. Record authentic bytes, SHA/URL/time, actual period labels, base reference, class names and bridge, not a guessed rate.
- **Formal gates unchanged**: national 2020 revised XLS and both genuine worker/retired household populations missing; `NATIONAL_WGT01-05=HOLD/PARTIAL`, `TAIPEI_PRICE_SERIES=UNVERIFIED`, `TAIPEI_CPI_RATE=NOT_CALCULATED`, `HO600 181/600, Basket NOT SEALED, Index LOCKED`, Actions disabled. The research memo concerns observed 2020 spending *shares* only, **not historical inflation**.

## 2026-10-17 — Taipei CPI 2026-09 metadata and month-grid audit

**Assistant actually searched and attempted raw retrieval again**, rather than immediately delegating to Mac:

- Current official Taipei 7-major-class CPI press release (2026-10-07): **Sep 2026 113.95 (2021=100), Sep YoY +2.65%, Jan–Sep 2026 vs Jan–Sep 2025 +1.74%**. These are **all-consumer official values**, not age-head inflation or 2020→2026 rate. Source https://dbas.gov.taipei/News_Content.aspx?n=61D456768E73CD92&s=E89309C4919E6F57, [research-only benchmark CSV](../research/cohort-inflation/taipei-cpi-2026-09-all-consumers-official-press-benchmark.csv).
- Official basic monthly CPI source lists through **2026-09-30** (https://data.taipei/dataset/detail?id=f47d7930-c507-4b5d-9ad3-907746a28342), basic annual through **2025-12-31** (https://data.taipei/dataset/detail?id=7ee57050-4d27-482c-bae5-ebd15ca86702). Official general-CPI [bridging data](https://data.taipei/dataset/detail?id=a046606e-818a-45dd-8395-b0e004551347) separately identified in the [four-source catalog](../research/cohort-inflation/taipei-cpi-official-source-register-2026-10-17.csv).
- Actual assistant raw attempts: web clicked current monthly frontend CSV link (cache miss); direct official legacy monthly endpoint (gateway 400/OK), annual frontend CSV (gateway rejects `text/csv`), and container.download (failed). Container DNS lookup `data.taipei` failed. **No original CPI CSV has been authenticated in this turn, no bytes/size/SHA or age-specific price figures**.
- Updated [CPI official capture utility](../research/cohort-inflation/fetch_taipei_cpi_basic_official.py) to accept either current `統計期` or legacy `年月別`/`年別` headers, first try the official monthly frontend download URL, and use the official legacy endpoint only as *same-dataset fallback*, preserving failure attempts. [16 offline synthetic schema tests](../research/cohort-inflation/test_fetch_taipei_cpi_basic_official.py) committed but **not yet executed on Mac**.
- Independently authored and executed a separate [month/class-grid completeness auditor](../research/cohort-inflation/audit_taipei_cpi_period_coverage.py) with [nine fixtures](../research/cohort-inflation/test_audit_taipei_cpi_period_coverage.py). Assistant local container showed **9/9 synthetic PASS** and Python compile PASS, including 2020 vs 2026 missing Sept, duplicate month/class and untrusted source SHA/host. GitHub copies of those two scripts are committed; no actual CPI raw data were passed through them. Re-run tests in checked-out project for exact-commit acceptance.
- [Pending 12-expenditure-class to seven-CPI-group crosswalk](../research/cohort-inflation/taipei-2020-spending-vs-7-cpi-class-crosswalk-PENDING.csv) explicitly leaves **12/12 price relative accepted = NO** pending official basic-group subcategory definitions and source time series; transport+communication and education+leisure cannot be split from coarse 7 groups. [Period and release acceptance gates](../research/cohort-inflation/TAIPEI-CPI-2026-09-PERIOD-AND-CROSSWALK-GATES-2026-10-17.md) freeze both **2020 Jan–Sep vs 2026 Jan–Sep** and independent **2020 annual vs 2025 annual** controls, with publication HOLD.

Minimal remaining **Mac-only** actions (using existing strict TLS; no system changes):
```bash
git switch research/batch-09
git pull --ff-only
python3 -m unittest discover -s research/cohort-inflation -p 'test_fetch_taipei_cpi_basic_official.py' -v
python3 -m unittest discover -s research/cohort-inflation -p 'test_audit_taipei_cpi_period_coverage.py' -v
python3 research/cohort-inflation/fetch_taipei_cpi_basic_official.py --source TPE-CPI-BASIC-MONTH --out /tmp/ho600-cpi-monthly-original
python3 research/cohort-inflation/fetch_taipei_cpi_basic_official.py --source TPE-CPI-BASIC-YEAR --out /tmp/ho600-cpi-yearly-original
python3 research/cohort-inflation/audit_taipei_cpi_period_coverage.py --csv /tmp/ho600-cpi-monthly-original/TPE-CPI-BASIC-MONTH-official-original.csv --receipt /tmp/ho600-cpi-monthly-original/TPE-CPI-BASIC-MONTH-receipt.json --out /tmp/ho600-cpi-month-grid-audit.json
```
If a fixture fails, repair in **research branch only**, rerun, record original error. If download fails, keep CPI price HOLD with actual TLS/HTTP error receipt, and do NOT compute rates. If raw arrives, pin real source SHA and inspect class base/category lineage, complete months and all 12 expenditures before computing any `TAIPEI_AGE_HEAD_CPI_PROXY`. National work/retire population `0/2`, WGT-01 still HOLD, canonical main **181/600, NOT SEALED, INDEX LOCKED**, GitHub Actions disabled.

## Follow-up — 2026-10-18: Taipei CPI source retrieval and partial crosswalk

This follow-up records work completed after the earlier dated handoff; it does not change national WGT status.

- Began on `research/batch-09` at `a0a4f6b55ae37f4dd78bb4cf706c430a1b39e543` after `git pull --ff-only`. The first network attempt was blocked by sandbox DNS; after the user-authorized network permission, GitHub and the official Taipei sources resolved normally. No TLS bypass or CA trust change was used.
- The official dataset pages' current direct download anchors point to `tsis.dbas.gov.taipei`. Their strict native-CA HTTP 200 originals are archived in `research/cohort-inflation/source-archive/tpe-cpi-20261018/`. Monthly: 881,570 bytes, SHA-256 `7d3d3b3f09080cd0f9f374a0bcf8e5c89750f1c54374734159221429618ed8ed`, 2026-10-17 23:56:25.829701 UTC. Annual: 64,481 bytes, SHA-256 `318de9dbcd7e95e4e626d1327a9284a38c955b08f7c167020db1da774f2f0d40`, 2026-10-17 23:56:26.413780 UTC. Capture receipts preserve exact URLs, final URLs, HTTP status, response type, strict TLS result, bytes, and hashes.
- The prior `data.taipei` monthly and annual API download routes each yielded HTTP 200 with an empty payload; the monthly legacy route yielded HTTP 500. The current official dataset page links were inspected and then used with strict TLS.
- Both required test suites passed on this checkout: downloader **16/16**, period auditor **9/9**. The actual period audit has **48/48** basic classes with complete 2020 Jan–Sep and 2026 Jan–Sep records; annual 2020–2025 is complete. Monthly/annual index pairs across all 48 classes and six years differ by at most 0.005 index points. The 2026-09 `總指數` value 113.95 matches the official Taipei release, and all 48 annual 2021 class indices equal 100.00.
- New crosswalk `research/cohort-inflation/taipei-2020-age-head-to-cpi-basic-crosswalk-20261018.csv` reviews all 12 household divisions: 3 `MAPPED`, 8 `SPLIT_REQUIRED`, and 1 `UNMAPPED`. A standard-library analysis applied the original, unchanged 84 Taipei age-head spending weights only to the three accepted CPI classes. Coverage is 7.57%–15.26%; food, housing, and medical mandatory classes remain unresolved, so no complete rate is released and mapped weights are not normalized.
- Two preselected comparisons are reported as partial mapped-category contributions only: 2020 Jan–Sep to 2026 Jan–Sep, and 2020 full year to 2025 full year. A separate Fraction-based program independently matches all 14 age-period summaries and 42 category contributions; maximum numeric difference is below `5.1e-13`.
- Full details: `research/cohort-inflation/TAIPEI-CPI-2026-10-18-DATA-CROSSWALK-PARTIAL-RESULT.md`; machine outputs: `research/cohort-inflation/results/tpe-cpi-20261018/`. The dated source register is `research/cohort-inflation/taipei-cpi-official-source-register-2026-10-18.csv`.
- Remaining blockers: item-level household expenditure decomposition and directly comparable Taipei price classes for divisions 01, 02, 04–08, 11, and 12; the city CPI file contains no standalone communications-service class and no hotel-accommodation basic class. National revised WGT-01 remains HOLD. The Taipei 65+ household-head group is not a retired-household sample.

Formal state remains `HO600=181/600`, Basket `NOT SEALED`, Index `LOCKED`, national WGT-01 `HOLD`, GitHub Actions unused. The final research-branch remote SHA is recorded in the delivery response.


## 2026-10-18 — 58-column original household CSV child categories and division-09 audit

Following Mac CPI delivery at `10a9bd48b7fd0602798267898778dc77a63f4202`, assistant reread Github's **actual original** city 2020 58-column household age CSV and 42 previously verified class contributions. Found previously under-used **true 2020 within-parent** spending splits (not merely 12 high-level divisions).

- [Original 2020 subcomponent audit](../research/cohort-inflation/results/tpe-cpi-20261018/tpe-2020-recovered-child-expenditure-audit.csv): seven age groups, parents 04 Housing, 07 Transportation, 09 Leisure/Culture, each reconciles to its source child amounts within **±NT$1**. Housing old split is **rent PLUS water** vs **electricity/fuel**; cannot falsely treat as CPI standalone `房租` and `水電燃氣`. Transport divides 4 component expenses but CPI `交通及通訊設備` still mixes communications.
- [Critical 09 assumption sensitivity](../research/cohort-inflation/results/tpe-cpi-20261018/division09-mapping-hold-sensitivity.csv): 2020 leisure/culture contains **40.25%–50.01% package travel** plus entertainment services/books/recreation goods. The provisional direct map of entire division 09 → CPI `(二)娛樂費用` requires official item-scope verification before publication. 09 generated 85.4%–97.6% of the previous A-period **three-division partial contribution** and 89.1%–99.0% of B. Excluding 09 leaves **2.54%–8.95% coverage**, and 65+ A partial contribution falls from **+1.9018 pp** to **+0.0447 pp**. Neither version is a complete cohort inflation rate.
- Full interpretation in [audit memo](../research/cohort-inflation/TAIPEI-2020-CHILD-SPENDING-AND-ENTERTAINMENT-SENSITIVITY-2026-10-18.md). Reproducible **source-SHA-bound Python stdlib verifier** [verify_taipei_child_sensitivity_20261018.py](../research/cohort-inflation/verify_taipei_child_sensitivity_20261018.py) was committed, but *has not been executed directly from Mac checkout* in this assistant-only follow-up. Independently recomputed 7×3 parent-child source totals and 14 sensitivity rows in connector JS; all passed numeric checks. Existing PDF-to-CSV 96/96 audit of **parent** categories does not guarantee PDF-level independent verification of child category cells.
- Next research should prioritize **2020 age-head per-item spending detail** for 01,04,06,11 and an official entertainment price-item definition. The present 48-class CPI and split household subcategory values are insufficient to claim >=95% coverage. Retain original `MAPPED` results as historic exploratory version, interpret 09 as `MAPPED_PROVISIONAL_SCOPE_REVIEW`, do not overwrite original data or raise gate.
- Canonical 181/600, Basket NOT SEALED, Index LOCKED; national WGT01 HOLD, national WORK/RETIRE 0/2, 2020–26 city full age-head CPI HOLD; no main writes, merges or GitHub Actions.

