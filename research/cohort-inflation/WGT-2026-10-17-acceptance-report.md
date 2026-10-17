# WGT-01 至 WGT-05 驗收報告

**執行狀態：** `PARTIAL_WITH_EXTERNAL_BLOCKERS`；所有未取得原始證據的項目均維持 `HOLD`。  
**紀錄時間：** 2026-10-17 02:44:24 UTC（台北時間 2026-10-17 10:44:24）。  
**研究分支：** `research/batch-09`；本次網路排障開始前遠端 HEAD：`5a1fc853d96e25e413d0476d31ed5f1393460d38`，已確認與分支 HEAD 相同。  
**原始檔快取：** `work/source-cache/`，檔案數 0。未取得原檔，無原檔 SHA-256、下載大小或轉檔 SHA-256。

## 驗收判定

| Gate | 狀態 | 證據及限制 |
|---|---|---|
| WGT-01 原始資料取得 | **HOLD — TLS_CERTIFICATE_BLOCKED** | 沙箱外 DNS 已可解析官方主機；嚴格驗證 TLS 的 5 個本機 HEAD 檢查與 3 次官方下載器重試均在憑證驗證階段失敗，HTTP 000、收到 0 bytes。沒有原始位元組可驗證。 |
| WGT-02 2020 修正版確認 | **PARTIAL — 檔案版次 HOLD** | 官方 109 年（2020）職業別、年齡別統計頁均標示 2026-02-13 更新消費支出等金額。頁面與連結版本已確認；原始檔未下載，無法核對檔案內容是否確為修正版。 |
| WGT-03 表格解析 | **HOLD** | 無原始檔及 Numbers 轉出的 XLSX；沒有實際工作表、列欄、分類、單位或註腳可檢視。未建立 mapping。 |
| WGT-04 12 類與總額對帳 | **HOLD — 族群資料未對帳** | 現有全體家庭搜尋索引摘錄可作暫存算術檢查：12 類合計 815,100 元／戶／年。此摘錄標示原始 bytes 未驗證，且不是受僱或高齡戶長資料；不可當作修正版原始表的驗收。 |
| WGT-05 代理樣本權重 | **HOLD — 0/2 組** | 未產生 `OCC_HEAD_*_PROXY` 或 `AGE_HEAD_*_PROXY` 權重。不得宣稱代表全體上班族或真正退休家庭；不得計算 HO600-WORK、HO600-RETIRE 或族群通膨率。 |

## 官方來源與網路診斷

- 職業別官方頁（109 年／2020）：<https://www.stat.gov.tw/News_Content.aspx?n=3908&s=210989>
  - XLS：<https://ws.dgbas.gov.tw/001/Upload/463/relfile/11530/235896/65.xls>
  - ODS：<https://ws.dgbas.gov.tw/001/Upload/463/relfile/11530/235896/65.ods>
- 年齡別官方頁（109 年／2020）：<https://www.stat.gov.tw/News_Content.aspx?n=3911&s=211017>
  - XLS：<https://ws.dgbas.gov.tw/001/Upload/463/relfile/11531/235640/159-164.xls>
  - ODS：<https://ws.dgbas.gov.tw/001/Upload/463/relfile/11531/235640/159-164.ods>
- 兩頁均附主計總處說明：原公布表因少數原始調查資料格式差異，於 2026-02-13 更新兼業薪資、本業薪資、住宅服務、水電瓦斯、房地租及水費、消費支出、儲蓄及所得總額。

實際嘗試如下；本次連線排障時間為 2026-10-17 02:43 UTC 左右（台北時間 10:43）：

1. 預設沙箱下曾有 DNS 解析錯誤。依使用者要求改以提升網路權限作唯讀連線測試後，`www.stat.gov.tw` 解析到 `104.18.0.120`、`104.18.1.120` 及 IPv6 位址，`ws.dgbas.gov.tw` 解析到 `223.200.181.106`。這表示 DNS 沙箱阻礙已被排除到可解析階段。
2. 在一般 TLS 驗證下，以 `curl -sSIL` 測試職業官方頁及四個官方 XLS／ODS URL，共 5 個 URL；全部回報 `curl: (60) SSL certificate problem: unable to get local issuer certificate`，HTTP 狀態為 000，沒有回應本文或下載 bytes。再以 `curl --ca-native` 對職業 XLS 測試 macOS 原生信任庫，仍是相同錯誤。沒有停用 TLS 驗證。
3. 對 `NAT20-OCC` XLS、`NAT20-AGE` XLS、`NAT20-AGE-ODF` ODS 重跑專案的官方下載器；三次均為 Python `CERTIFICATE_VERIFY_FAILED: unable to get local issuer certificate`，沒有建立原檔或收據。`work/source-cache/` 仍為 0 檔。
4. 嚴格驗證的 OpenSSL 握手回報 `Verify return code: 20 (unable to get local issuer certificate)`。葉憑證主體 CN 為 `www.dgbas.gov.tw`、簽發者為 `TWCA SSL Certification Authority`，有效期為 2026-10-07 至 2027-04-23；同一握手所列的其他憑證屬於 ePKI／政府伺服器憑證鏈，無法補足該葉憑證的簽發者鏈。系統 CA 路徑存在、未發現 proxy 環境變數；未修改 DNS、憑證或網路設定。
5. 先前網頁來源代理對四種格式回報：職業 XLS cache miss、職業 ODS 502、年齡 XLS 502、年齡 ODS timeout；這些不是來源端 HTTP 收據。Safari 先前也顯示「此連線並非私人連線」，未繞過警告。
6. 一個含 `curl -k` 的憑證診斷命令遭自動審查拒絕，理由是 `-k` 會停用 TLS 憑證驗證；該命令未執行，亦未以變通方式重試。後續改用 `-verify_return_error` 等嚴格驗證診斷。

目前已排除 DNS 解析階段的沙箱限制，但 TLS 憑證鏈仍無法在本機信任庫驗證，因此不能安全取得原始資料。這不是來源不存在的證據；沒有 HTTP 成功狀態、下載時間、檔案大小或 SHA-256。

## 12 類暫存算術核對（非 WGT-04 通過）

以下數字只來自分支既有的 `general-household-2020-indexed-v0.csv`，其來源註記為官方 PDF 搜尋索引文字、`RAW_BYTES_UNVERIFIED`、`ALL_HOUSEHOLDS_GENERAL`。本次以獨立算術程式重算 12 個不同代碼、非負支出、總額一致及各類百分比；這是對該 CSV 的算術驗算，不是原始 PDF/XLS 的來源驗證，也不是族群權重。

| 代碼 | 支出類別 | 元／戶／年 | 占 815,100 元比例（%） |
|---|---|---:|---:|
| 01 | 食品及非酒精飲料 | 118,015 | 14.478592 |
| 02 | 菸酒及檳榔 | 9,187 | 1.127101 |
| 03 | 衣著鞋襪及服飾用品 | 22,396 | 2.747638 |
| 04 | 住宅服務、水電瓦斯及其他燃料 | 198,145 | 24.309287 |
| 05 | 家具設備及家務維護 | 22,907 | 2.810330 |
| 06 | 醫療保健 | 139,010 | 17.054349 |
| 07 | 交通 | 72,553 | 8.901116 |
| 08 | 通訊 | 23,191 | 2.845172 |
| 09 | 休閒與文化 | 33,993 | 4.170409 |
| 10 | 教育 | 27,471 | 3.370261 |
| 11 | 餐廳及旅館 | 106,533 | 13.069930 |
| 12 | 什項消費 | 41,699 | 5.115814 |
| **總計** | **12 類** | **815,100** | **99.999999（六位小數四捨五入）** |

先前索引摘錄中的住宅與醫療合計為 337,155 元。本次沒有收到修正版原始表，故無法比較該暫存數字是否與 2026-02-13 修正後的全體家庭數字一致；若原始表不同，須記錄為 `SOURCE_CONFLICT`，不得強行配平。

## 離線檢查

- `python3 research/cohort-inflation/validate_exposure.py`：**PASS_STRUCTURAL_ONLY**。418 個候選、418 筆 exposure、50 個子類、181 個 canonical exact；收據明示未驗證族群支出權重，未計算通膨。
- `python3 research/cohort-inflation/verify_general_2020_excerpt.py`：**PASS_INTERIM_CHECKSUM_ONLY**，12 類合計 815,100；腳本明示不是族群權重。
- 另行獨立重算：**PASS_INTERIM_CHECKSUM_ONLY**，12 個不同類別、年度總額 815,100、已存百分比合計 99.999999%；證據範圍仍僅限未驗證的全體家庭索引 CSV。
- 指定單元測試 `python3 -m unittest discover -s research/cohort-inflation -p 'test_extract_revised_2020_cohort_xlsx.py'`：本次再以系統 Python 3.14 及 Codex bundled Python 3.12 執行，皆因缺少 `artifact_tool` 回報 `ModuleNotFoundError`；實際測試數 0，狀態 **BLOCKED_TEST_COLLECTION**。未以其他試算表解析器取代，也未把 fixtures 或結構檢查稱為來源資料通過。
- `extract_revised_2020_cohort_xlsx.py --inspect` 與 `--extract`：未執行，因無轉換後 XLSX 或原始檔。

## 邊界與下一步

Canonical HO600 仍是 **181/600**，Basket **NOT SEALED**，Index **LOCKED**；沒有修改正式工作簿、`data/*.csv` 或 canonical 狀態。分支上的 `.github/workflows/validate.yml` 僅能手動 `workflow_dispatch`；本次未使用或派送 GitHub Actions，也沒有修改 `main`、合併分支、封存 Basket 或解鎖 Index。

Batch 9 C01–C03 維持 **60 項 research-level PASS**，C04 維持 **WIP**；本次 cohort extraction 仍與 private-price Basket 分開。

下一步須先由來源端或受信任網路環境提供可驗證的官方 TLS 憑證鏈；不匯入未核實憑證、不略過 TLS。之後重新下載兩份原始表（若 XLS 仍不可用，再測官方 ODS），保存原檔與時間、官方 URL、大小及 SHA-256；再用 Numbers 另存 XLSX、記錄轉檔 SHA、檢視工作表與 12 類列位，並在提供 `artifact_tool` 的本機環境完成單元測試、獨立對帳及兩組明確標為 PROXY 的樣本權重。原始資料不足時維持 HOLD。

## 2026-10-17 TLS 根因與 CSV 測試追蹤

本節為本次 `research/batch-09` follow-up 的新證據，記錄於 `2026-10-17T08:01:28Z` 起。遠端基準為 `7d87ef5d7ba05ba7f932f41c58642176daba637a`，先執行 `git pull --ff-only` 並回報 `Already up to date.`。完整憑證比對見 [`TLS-DIAGNOSTIC-RESULT-2026-10-17.md`](./TLS-DIAGNOSTIC-RESULT-2026-10-17.md)；機器收據及後續 Handoff 亦已更新。

### TLS 判定

- 診斷腳本透過嚴格 SNI/主機名/鏈驗證執行；`ws.dgbas.gov.tw` 與 `www.stat.gov.tw` 都回報 OpenSSL verify code 20（`unable to get local issuer certificate`）。兩站送出的葉憑證是同一張：SAN 含各自主機名，issuer 為 `TWCA SSL Certification Authority`，葉 AKI 為 `F2:28:D4:F9:D4:1C:7E:1A:6B:16:82:E5:EF:93:29:69:ED:CA:15:20`。
- `ws.dgbas.gov.tw` 送出葉憑證及三張 ePKI／政府伺服器憑證；三張 SKI 都不匹配葉 AKI，亦沒有 TWCA SSL CA 簽發者。`www.stat.gov.tw` 只送出葉憑證，沒有中繼憑證。
- `ssl.twca.com.tw` 的完整 3 張憑證鏈嚴格驗證成功（verify code 0）；TWCA 中繼 SKI 與其葉 AKI 相符。`curl --ca-native` 對控制站回 HTTP 200，對兩個官方主機則在 TLS 階段 error 60／HTTP 000。
- `scutil --proxy` 為空 dictionary，沒有 proxy 環境變數。分類為 **`TLS_ROOT_CAUSE_LIKELY`：官方端點送出的鏈有誤或不完整**；本機整體信任庫錯誤較不可能，但僅憑本次觀測仍不能完全排除透明網路攔截或受管理的 TLS inspection。未更改信任庫、網路、DNS 或 Safari。

### CSV 測試與資料驗算

- 首次執行新 CSV 測試集時，11 項中有 5 項通過、4 項失敗、2 項錯誤；共同根因是解析器把數值 `0` 誤當作空值。修正 `positive_number` 對 `None` 與數值零的區分後，以 Python 3.14.5 再執行 `python3 -m unittest discover -s research/cohort-inflation -p 'test_extract_revised_2020_cohort_csv.py' -v`，**11/11 PASS**。測試與解析器未匯入 `artifact_tool`，本機亦未安裝該模組；CSV 測試路徑不需要它。
- 重新核對既有全體家庭索引摘錄：代碼 01–12 共 12 類、負值 0、支出合計與列示總額均為 **815,100 元／戶／年**，儲存百分比合計 **99.999999%**；資料標記仍是 `RAW_BYTES_UNVERIFIED` 及 `ALL_HOUSEHOLDS_GENERAL`，因此只是算術檢查，不是族群來源驗收或權重。
- 本次沒有任何官方原始檔通過嚴格 HTTPS；沒有下載 XLS／ODS，沒有原始檔或 Numbers 轉檔雜湊，沒有執行 Numbers、XLSX `--inspect` 或實際資料抽取。

**Gate 狀態未升格：** WGT-01 `HOLD_TLS_CERTIFICATE_BLOCKED`；WGT-02 `PARTIAL_METADATA_ONLY`；WGT-03 `HOLD`；WGT-04 `HOLD`；WGT-05 `HOLD, 0/2`。任何職業戶長或高齡戶長樣本均不得宣稱為全體上班族或真正退休家庭。後續需先由 DGBAS/TWCA 或受信任網路管理者確認並修正鏈，再以嚴格驗證重試；若需要更改本機信任設定，須先取得使用者授權。

Canonical HO600 仍為 **181/600、Basket NOT SEALED、Index LOCKED**；沒有使用 GitHub Actions、修改 `main`、發布族群通膨率或變更正式工作簿。
