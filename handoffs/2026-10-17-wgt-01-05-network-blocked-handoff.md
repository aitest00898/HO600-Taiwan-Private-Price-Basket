# Handoff：HO600 WGT-01 至 WGT-05

**狀態：** `PARTIAL_WITH_EXTERNAL_BLOCKERS`；核心資料 Gate 維持 `HOLD`。  
**Repository：** `aitest00898/HO600-Taiwan-Private-Price-Basket`  
**分支：** `research/batch-09`  
**本輪基底 HEAD：** `3194ff4fd6bc348b536c7ae4f7966c9690bde4aa`  
**完整驗收報告：** `research/cohort-inflation/WGT-2026-10-17-acceptance-report.md`  
**來源收據：** `research/cohort-inflation/wgt-2026-10-17-source-receipt.json`

## 已完成

- 已完整閱讀 `research/cohort-inflation/LOCAL-CODEX-WGT-2026-10-17.md`。
- 官方 109 年（2020）經濟戶長職業別及年齡別頁面、XLS 及 ODS 連結已確認；兩頁均載有 2026-02-13 修訂說明。
- Mac 本機下載程式三次遇 DNS 失敗；四個格式的 `curl -I` 亦無法解析 `ws.dgbas.gov.tw`。網頁來源代理回報 cache miss、502 及 timeout。Safari 顯示官方站憑證警告；沒有繞過。
- 本機原始檔快取 `work/source-cache/` 為空。原始檔與轉檔檔案皆不存在；沒有聲稱下載、Numbers 轉檔、來源 SHA 或解析已完成。
- `validate_exposure.py` 結構檢查為 `PASS_STRUCTURAL_ONLY`；全體家庭索引摘錄的 12 類算術重算為 815,100 元／戶／年。該 CSV 原始 bytes 未驗證，不是受僱或高齡戶長權重。
- 指定 unit test 因系統 Python 3.14 與 bundled Python 3.12 均沒有 `artifact_tool`，無法收集任何測試；沒有改用不同解析器。

## WGT Gate

- **WGT-01：HOLD_NETWORK_BLOCKED** — 兩份官方原始檔均未取得。
- **WGT-02：PARTIAL** — 官方頁確認 2020 年及 2026-02-13 修訂註記；原始檔位元組與版次未驗證。
- **WGT-03：HOLD** — 未轉 XLSX、未執行 `--inspect`，工作表及欄列映射未知。
- **WGT-04：HOLD** — 全體家庭索引摘錄只能作暫存算術檢查；職業與年齡兩組的原表總額均未對帳。
- **WGT-05：HOLD，0/2** — 未建立任何 proxy 支出權重。不得從職業或戶長年齡邊際表推導交叉矩陣。

## 恢復工作後的執行順序

1. 在 Mac 恢復 `stat.gov.tw` 與 `ws.dgbas.gov.tw` 的正常 DNS 與有效 TLS 信任。不要繞過 Safari 憑證警告；在可信網路連線可用後重新執行。
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
- Canonical HO600 維持 181/600、Basket NOT SEALED、Index LOCKED。Branch workflow 為 `workflow_dispatch`，不派送 Actions。
