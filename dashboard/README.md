# HO600 IUI Dashboard V0

**狀態：研究分支上的唯讀靜態 Dashboard 原型。非正式指數，不是已部署網站。**

## 直接在 Mac 開啟

```bash
git switch research/batch-09
git pull --ff-only
open dashboard/index.html
```

**不需要本機 server、npm、登入、GitHub API token、第三方 CDN 或網路。** `index.html` 載入同資料夾的 `snapshot.js`、`app.js`、`styles.css`；`snapshot.js` 是為了 `file://` 離線使用由 `snapshot.json` 複製產生的受審資料。iPhone 可透過本機或自架靜態 HTTP 服務檢視；本次**沒有**設定或聲稱 GitHub Pages 已上線。

如果要在同一網路的 iPhone 連入 Mac，可由使用者自行啟動唯讀伺服器：
```bash
python3 -m http.server 8765 --directory dashboard
```
之後在手機 Safari 使用 Mac 實際 LAN IP 和埠號 8765 開啟；請在私人可信網路中操作，並注意此伺服器未設定登入保護。這不是雲端部署。

## V0 可操作內容

| 分頁 | 內容 | 互動 |
| --- | --- | --- |
| 總覽 | 181/600、419 缺口、Batch 9 研究 60、正式 Index LOCKED、七領域分布 | 分頁導航、來源連結、CSV 匯出 |
| 價格籃 | 七大領域配額、C01–C03 PASS、C04 WIP、正式 workbook 20/20 驗證記錄 | 詳細表、Checkpoint 追溯、匯出 |
| 戶長年齡與 CPI | 臺北市七組 2020 支出、48/48 CPI 分類、A/B 期間的**部分**貢獻、權重覆蓋、12 類 crosswalk | 期間切換、保守排除 09／暫定納入 09、年齡組切換、對照狀態過濾、匯出目前情境 |
| 證據與驗收 | pinned GitHub blob SHA、main 與 research 分流、安全與方法學風險 | 點選原始來源、匯出來源清單 |

## 資料與方法約束

- 正式進度來自 `main` 的 `canonical/status.json`、`data/Quota_Control.csv` 與 `data/Validation_Release.csv`。Branch commit pinned `88fa2b53774067faf740868bb8e168a04e47a8bf`。
- Batch 9 與臺北 CPI 研究快照 pinned `research/batch-09` 原成果 commit `fd30af9e3ba08e7855c289ad347fd0f2bec4d909`，見 `snapshot.json.sources` 的原始 blob SHA 與 GitHub 追溯連結。**Dashboard 自身的開發提交不等於研究數據已更新。**
- 所有圖表都是**快照、非即時、不可寫入**。切換標籤只變更顯示，並不重新讀取 GitHub。
- 2020 年臺北市七組年齡資料是「戶長年齡代理」。不代表全國、實際上班族或真正退休戶。
- `TAIPEI_AGE_HEAD_CPI_PROXY` 僅記載**部分已對應類別的百分點貢獻**。沒有任何完整年齡組通膨率。預設排除需複核的第 09 類休閒文化 → CPI 娛樂費用映射。
- 12 類狀態：2 已初步對應、1 暫定、8 需拆分、1 無獨立對應。食品、住宅與醫療無法發表完整率；95% 是本研究設定的發布門檻，不是政府標準。
- `main` 正式 Basket 為 `NOT SEALED`，`Index_Calc = LOCKED`。
- Repo 目前是 **Public**；切勿將私鑰、帳號或無權限的私人內容加入 Dashboard。
- GitHub Actions 按使用者全域決策保持停止使用。本程式不建立 workflow、不觸發 Actions、不修改 main 或原正式工作簿。

## 內部檔案

```text
dashboard/
  index.html         # 靜態導覽及語意架構
  styles.css         # 桌面 / iPhone 響應式設計
  app.js             # 圖表、過濾、CSV 匯出、來源跳轉
  snapshot.json      # 經 main / research 實際來源對帳後產生的來源快照
  snapshot.js        # 和 snapshot.json 等值的 file:// 可用離線資料
  README.md
  tests/
    test_dashboard.py # 本機 V0 唯讀規格和快照一致性測試
```

## 本機驗收

```bash
python3 -m unittest discover -s dashboard/tests -v
node --check dashboard/app.js
node --check dashboard/snapshot.js
```

如果沒有安裝 `node`，Python 的數據及靜態語意測試仍可先執行；瀏覽器腳本語法與實際互動需由 Safari 及其他可用環境進一步核對。

### V0 尚不包含

- 雲端部署網址、使用者登入、雲端持續更新、背景排程或 GitHub Actions。
- 正式 HO600 指數、工作／退休家庭完整通膨率、人口 × 職業真正交叉分組。
- 寫入 GitHub、改動 workbook、核准研究候選、交易或任務調度。

如後續要導入 Netlify、Cloudflare Pages 或其他靜態網站部署，應在獨立驗證與明確發布決策後處理，尤其須確認目前 Public 倉庫與研究證據的可見範圍。
