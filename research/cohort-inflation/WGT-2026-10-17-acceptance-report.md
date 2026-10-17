# WGT-01 至 WGT-05 驗收報告

**執行狀態：** `PARTIAL_WITH_EXTERNAL_BLOCKERS`；所有未取得原始證據的項目均維持 `HOLD`。  
**紀錄時間：** 2026-10-17 02:35:49 UTC（台北時間 2026-10-17 10:35:49）。  
**研究分支：** `research/batch-09`；本輪開始時遠端 HEAD：`3194ff4fd6bc348b536c7ae4f7966c9690bde4aa`。  
**原始檔快取：** `work/source-cache/`，目前空白。未取得原檔，無原檔 SHA-256、下載大小或轉檔 SHA-256。

## 驗收判定

| Gate | 狀態 | 證據及限制 |
|---|---|---|
| WGT-01 原始資料取得 | **HOLD — NETWORK_BLOCKED** | 主計總處 2020 職業別 XLS／ODS、年齡別 XLS／ODS 共四個官方連結均已測試；Mac DNS 無法解析官方主機，且資料代理回報 cache miss、502 或 timeout。沒有任何原始位元組可驗證。 |
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

實際嘗試如下；所有時間均落在 2026-10-17（台北時間）：

1. 在 Mac 使用專案的 `fetch_official_weight_tables.py` 分別下載 `NAT20-OCC` XLS、`NAT20-AGE` XLS、`NAT20-AGE-ODF` ODS。三次均於 DNS 階段失敗：`urllib.error.URLError: [Errno 8] nodename nor servname provided, or not known`，沒有 HTTP 狀態或回應 bytes。
2. 對四個 XLS／ODS URL 各執行一次本機 `curl -I`；四次均回報 `curl: (6) Could not resolve host: ws.dgbas.gov.tw`。請求未到達來源主機，沒有重試。
3. 透過網頁來源連結各測試四種格式一次：職業 XLS 回報 cache miss、職業 ODS 回報 502、年齡 XLS 回報 502、年齡 ODS 回報 timeout。此代理工具沒有提供來源端 HTTP 收據。
4. Safari 開啟官方統計頁出現「此連線並非私人連線」憑證警告；未繞過警告，未繼續連線。

因此，目前可確認的是本機 DNS 及瀏覽器信任鏈阻止資料取得；不能推論來源不存在，也不能提供真實的下載時間、HTTP 狀態、檔案大小或 SHA-256。沒有更改 DNS、憑證或其他網路設定。

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
- 指定單元測試 `python3 -m unittest discover -s research/cohort-inflation -p 'test_extract_revised_2020_cohort_xlsx.py'`：**BLOCKED，測試未收集**。系統 Python 3.14 及 Codex bundled Python 3.12 都缺少 `artifact_tool`，回報 `ModuleNotFoundError`。未以其他試算表解析器取代；因此沒有把 fixtures 或結構測試誤稱為來源資料通過。
- `extract_revised_2020_cohort_xlsx.py --inspect` 與 `--extract`：未執行，因無轉換後 XLSX 或原始檔。

## 邊界與下一步

Canonical HO600 仍是 **181/600**，Basket **NOT SEALED**，Index **LOCKED**；沒有修改正式工作簿、`data/*.csv` 或 canonical 狀態。分支上的 `.github/workflows/validate.yml` 僅能手動 `workflow_dispatch`；本次未使用或派送 GitHub Actions，也沒有修改 `main`、合併分支、封存 Basket 或解鎖 Index。

下一步先恢復 Mac 對 `stat.gov.tw` 與 `ws.dgbas.gov.tw` 的正常 DNS 與有效 TLS 信任，再從上述官方頁下載兩份原始表（若 XLS 仍不可用，測試官方 ODS 替代格式）。保存原檔與時間、官方 URL、大小及 SHA-256；再用 Numbers 另存 XLSX、記錄轉檔 SHA、實際檢視工作表與 12 類列位，最後在提供 `artifact_tool` 的本機環境完成單元測試、獨立對帳及兩組明確標為 PROXY 的樣本權重。原始資料不足時維持 HOLD。
