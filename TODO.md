# HO600｜完整待解 TODO 總表（2026-10-20）

**任務系統權威：[Linear TPI-001｜HO600](https://linear.app/001dev/project/tpi-001ho600-台灣私人物價籃-46e14167f961)。** 此檔案只是研究分支中、以原始 Linear issue ID 建立的唯讀對帳索引；編修 GitHub 清單**不會**自動修改 Linear issue 狀態，Linear 的 Todo/Done 也不等於價格或軟體驗收。

## 最新盤點基準

- GitHub Repo：[aitest00898/HO600-Taiwan-Private-Price-Basket](https://github.com/aitest00898/HO600-Taiwan-Private-Price-Basket)；本次寫入僅 `research/batch-09`，無 main 寫入、無 GitHub Actions、無部署。
- `main` HEAD `88fa2b53774067faf740868bb8e168a04e47a8bf`，Batch 8：正式 181/600、419 缺口、418 候選、1,566 證據；Basket NOT SEALED、Index LOCKED。
- 本次 TODO 登錄前研究 HEAD `a8e1532389cd9b89b033c6c60b18ff4775e55e36`；Batch 9 C01–C03 = 60 研究級 PASS；C04 1 PROVISIONAL + 1 HOLD；正式新增 0。
- 臺北市 2020 年 7 組 × 12 類 84 權重已完成部分來源查核；CPI 48 類月資料 16,560 筆／年資料 1,344 筆；第 09 類屬暫定映射，完整七組通膨率 0/7。
- 全國 WGT-01–05 部分 HOLD／PARTIAL；全國工作/退休權重 0/2。
- IUI Dashboard V0 原始程式有 10 檔；18 項本機 Python 測試、Mac Safari、iPhone 原生與部署皆待驗收。

## TODO 統計

| 類別 | 數量 |
|---|---:|
| **全部 TODO** | **42** |
| 新建（本輪） | 37 |
| 既有去重更新（本輪） | 5 |
| **P0／緊急** | **6** |
| **P1／高** | **27** |
| **P2／中** | **9** |
| Todo | **39** |
| In Progress | **1**（OO1-147） |
| **Done** | **2**（OO1-131、OO1-135） |
| **尚未完成** | **40**（Todo + In Progress） |
| Linear 明確前置依賴的 issue | 9 |
| 已設定的 blockedBy 邊 | 24 |

所有 `blockedBy` 是**必要的前置證據／測試**，不是解鎖正式發布的充分條件。完成後仍須遵循權限和使用者明確核准。


## 2026-10-21 實際執行收斂（非單純盤點）

- **OO1-131 = Done**：2026-10-15 UTC 三個 GitHub Actions `push` run 已查明是當時含 `research/**` 自動觸發的 workflow；比對三個 commit 的原始 YAML SHA 皆為 `048a5022...`。研究分支後以 `c3e292a` 改為手動觸發。**平台層是否全停用依然 UNKNOWN**，由 [OO1-130](https://linear.app/001dev/issue/OO1-130) 接續唯讀確認。詳細：[歷史根因收據](./research/triage/HO600-ACTIONS-HISTORICAL-ROOTCAUSE-2026-10-21.md)。
- **OO1-135 = Done**：從 `main` 三份配額／候選／證據 CSV 完成 [50 子分類 gap/來源索引](./research/triage/HO600-50-SUBCATEGORY-GAP-2026-10-21.csv)：`181 + 419 = 600`、418 候選、22 子分類零 Exact、16 子分類零候選。按 candidate_id 可連結 1,267 筆證據；餘下 299 筆是 **candidate_id 空白的 LEGACY_EVIDENCE_LEDGER**，非遺失、不得重複計入候選；來源 URL/2020 quote 仍未逐筆重新認證。
- **OO1-147 = In Progress**：臺北市 2024 年 3 月官方 CPI 新聞稿明列 `娛樂費用` 包含 **國內／外旅遊團費**；修正「套裝旅遊本身在娛樂 CPI 之外」的錯誤前提，但 2020 家庭休閒支出的書報文具／器材等尚缺精確歸屬，所以第 09 類仍 **PROVISIONAL**，七組完整率仍 **HOLD**。詳見 [官方納入範圍查證](./research/cohort-inflation/CPI-09-OFFICIAL-TOUR-INCLUSION-REVIEW-2026-10-21.md)。
- **Remaining 40**：包含 Mac Python 18 項、Safari／iPhone 真機、全國 WGT、正式 419 概念等。任務權威是 [Linear TPI-001](https://linear.app/001dev/project/tpi-001ho600-台灣私人物價籃-46e14167f961)，詳細當前狀態以 Linear 為準；本 CSV 是 2026-10-21 校準後的狀態快照（保留原檔名 2026-10-20 以免破壞既有連結）。

## P0｜首先核對

| 編號 | 工作線 | 待辦項目 | 前置阻擋 |
|---|---|---|---|
| [OO1-130](https://linear.app/001dev/issue/OO1-130/tpi-g01-github-actions-停用狀態與-main-自動觸發風險核實) | 安全／治理 | GitHub Actions 停用狀態與 main 自動觸發風險核實 | — |
| [OO1-131](https://linear.app/001dev/issue/OO1-131/tpi-g02-調查-20261015-actions-push-紀錄與重啟風險) | 安全／治理 | 調查 2026/10/15 Actions push 紀錄與重啟風險 | — |
| [OO1-147](https://linear.app/001dev/issue/OO1-147/tpi-c01-核實第09類休閒文化與-cpi-娛樂費用的官方範圍) | 臺北市 CPI | 核實第09類休閒文化與 CPI 娛樂費用的官方範圍 | — |
| [OO1-160](https://linear.app/001dev/issue/OO1-160/tpi-i01-iui-dashboard-v0-本機python-18項與node語法驗收) | IUI Dashboard | IUI Dashboard V0 本機Python 18項與Node語法驗收 | — |
| [OO1-161](https://linear.app/001dev/issue/OO1-161/tpi-i02-iui-dashboard-v0-mac-safari-四頁互動與csv匯出原生驗收) | IUI Dashboard | IUI Dashboard V0 Mac Safari 四頁互動與CSV匯出原生驗收 | [OO1-160](https://linear.app/001dev/issue/OO1-160/tpi-i01-iui-dashboard-v0-本機python-18項與node語法驗收) |
| [OO1-162](https://linear.app/001dev/issue/OO1-162/tpi-i03-iui-dashboard-v0-真正-iphone-safari-窄螢幕觸控驗收) | IUI Dashboard | IUI Dashboard V0 真正 iPhone Safari 窄螢幕觸控驗收 | [OO1-160](https://linear.app/001dev/issue/OO1-160/tpi-i01-iui-dashboard-v0-本機python-18項與node語法驗收)、[OO1-161](https://linear.app/001dev/issue/OO1-161/tpi-i02-iui-dashboard-v0-mac-safari-四頁互動與csv匯出原生驗收) |

## P1｜主要研究與驗收

| 編號 | 工作線 | 待辦項目 | 前置阻擋 |
|---|---|---|---|
| [OO1-103](https://linear.app/001dev/issue/OO1-103/ho600181600-正式概念增量與工作簿匯出驗證程序) | 正式匯入驗收 | HO600｜181/600 正式概念增量與工作簿匯出驗證程序 | [OO1-102](https://linear.app/001dev/issue/OO1-102/ho600batch-9-c01-c03-60-筆研究級證據複驗與-c04-接續)、[OO1-145](https://linear.app/001dev/issue/OO1-145/tpi-b11-重新驗證-batch-9-品牌來源集中上限與20筆可比性-b)、[OO1-146](https://linear.app/001dev/issue/OO1-146/tpi-b12-維持-candidate-pool-價格變化盲選與跨批去重) |
| [OO1-156](https://linear.app/001dev/issue/OO1-156/tpi-w01-dgbas-全國2020修正版-xlsods-嚴格-tls-原始取得) | 全國工作／退休權重 | DGBAS 全國2020修正版 XLS／ODS 嚴格 TLS 原始取得 | — |
| [OO1-157](https://linear.app/001dev/issue/OO1-157/tpi-w02-全國-wgt02-2020-修正版來源與版次一致性) | 全國工作／退休權重 | 全國 WGT02 2020 修正版來源與版次一致性 | — |
| [OO1-158](https://linear.app/001dev/issue/OO1-158/tpi-w03-全國-wgt03-定義工作與退休家庭不以戶長年齡冒充) | 全國工作／退休權重 | 全國 WGT03 定義工作與退休家庭，不以戶長年齡冒充 | — |
| [OO1-159](https://linear.app/001dev/issue/OO1-159/tpi-w04-全國-wgt0405-兩類12目的支出權重計算及驗收) | 全國工作／退休權重 | 全國 WGT04／05 兩類12目的支出權重計算及驗收 | [OO1-156](https://linear.app/001dev/issue/OO1-156/tpi-w01-dgbas-全國2020修正版-xlsods-嚴格-tls-原始取得)、[OO1-157](https://linear.app/001dev/issue/OO1-157/tpi-w02-全國-wgt02-2020-修正版來源與版次一致性)、[OO1-158](https://linear.app/001dev/issue/OO1-158/tpi-w03-全國-wgt03-定義工作與退休家庭不以戶長年齡冒充) |
| [OO1-106](https://linear.app/001dev/issue/OO1-106/ho600public-倉庫公開範圍來源授權與敏感檔稽核) | 安全／治理 | HO600｜Public 倉庫公開範圍、來源授權與敏感檔稽核 | — |
| [OO1-132](https://linear.app/001dev/issue/OO1-132/tpi-g03-對研究分支-127-commits-做分期審查與-pr-分界) | 安全／治理 | 對研究分支 127 commits 做分期審查與 PR 分界 | — |
| [OO1-133](https://linear.app/001dev/issue/OO1-133/tpi-g04-建立非-github-actions-的本機重現與完整驗收清單) | 安全／治理 | 建立非 GitHub Actions 的本機重現與完整驗收清單 | — |
| [OO1-104](https://linear.app/001dev/issue/OO1-104/tpi臺北市七年齡代理-cpi-的-12-類家庭支出缺口補證) | 臺北市 CPI | TPI｜臺北市七年齡代理 CPI 的 12 類家庭支出缺口補證 | — |
| [OO1-148](https://linear.app/001dev/issue/OO1-148/tpi-c02-cpi-01食品與11餐廳旅館外食及住宿拆分證據) | 臺北市 CPI | CPI 01食品與11餐廳旅館：外食及住宿拆分證據 | — |
| [OO1-149](https://linear.app/001dev/issue/OO1-149/tpi-c03-cpi-04住宅能源及05家具家務租金水燃料口徑對帳) | 臺北市 CPI | CPI 04住宅能源及05家具家務：租金／水／燃料口徑對帳 | — |
| [OO1-150](https://linear.app/001dev/issue/OO1-150/tpi-c04-cpi-06醫療保健與健保費確認價格指數涵蓋範圍) | 臺北市 CPI | CPI 06醫療保健與健保費：確認價格指數涵蓋範圍 | — |
| [OO1-151](https://linear.app/001dev/issue/OO1-151/tpi-c05-cpi-07交通與08通訊拆分設備服務及通訊缺失) | 臺北市 CPI | CPI 07交通與08通訊：拆分設備、服務及通訊缺失 | — |
| [OO1-153](https://linear.app/001dev/issue/OO1-153/tpi-c07-調查2020臺北市戶長年齡更細支出表公開微資料) | 臺北市 CPI | 調查2020臺北市戶長年齡更細支出表／公開微資料 | — |
| [OO1-154](https://linear.app/001dev/issue/OO1-154/tpi-c08-臺北7年齡代理cpi覆蓋率95percent與獨立重算-gate) | 臺北市 CPI | 臺北7年齡代理CPI覆蓋率≥95%與獨立重算 Gate | [OO1-147](https://linear.app/001dev/issue/OO1-147/tpi-c01-核實第09類休閒文化與-cpi-娛樂費用的官方範圍)、[OO1-148](https://linear.app/001dev/issue/OO1-148/tpi-c02-cpi-01食品與11餐廳旅館外食及住宿拆分證據)、[OO1-149](https://linear.app/001dev/issue/OO1-149/tpi-c03-cpi-04住宅能源及05家具家務租金水燃料口徑對帳)、[OO1-150](https://linear.app/001dev/issue/OO1-150/tpi-c04-cpi-06醫療保健與健保費確認價格指數涵蓋範圍)、[OO1-151](https://linear.app/001dev/issue/OO1-151/tpi-c05-cpi-07交通與08通訊拆分設備服務及通訊缺失)、[OO1-152](https://linear.app/001dev/issue/OO1-152/tpi-c06-cpi-02菸酒檳榔及12什項消費細分對照)、[OO1-153](https://linear.app/001dev/issue/OO1-153/tpi-c07-調查2020臺北市戶長年齡更細支出表公開微資料) |
| [OO1-102](https://linear.app/001dev/issue/OO1-102/ho600batch-9-c01-c03-60-筆研究級證據複驗與-c04-接續) | 價格籃／Batch 9 | HO600｜Batch 9 C01–C03 60 筆研究級證據複驗與 C04 接續 | — |
| [OO1-135](https://linear.app/001dev/issue/OO1-135/tpi-b01-建立-50-子分類22-空白子分類的缺口補證索引) | 價格籃／Batch 9 | 建立 50 子分類／22 空白子分類的缺口補證索引 | — |
| [OO1-136](https://linear.app/001dev/issue/OO1-136/tpi-b02-食品自煮基礎食品缺33包裝食品飲料缺17-的-exact-2020-搜尋) | 價格籃／Batch 9 | 食品：自煮基礎食品缺33、包裝食品飲料缺17 的 Exact 2020 搜尋 | — |
| [OO1-137](https://linear.app/001dev/issue/OO1-137/tpi-b03-衣著4-個零-exact-子分類與全領域65缺口回補) | 價格籃／Batch 9 | 衣著：4 個零 Exact 子分類與全領域65缺口回補 | — |
| [OO1-138](https://linear.app/001dev/issue/OO1-138/tpi-b04-住家5-個零-exact-子分類與80缺口回補) | 價格籃／Batch 9 | 住家：5 個零 Exact 子分類與80缺口回補 | — |
| [OO1-139](https://linear.app/001dev/issue/OO1-139/tpi-b05-交通6-個零-exact-子分類與68缺口回補) | 價格籃／Batch 9 | 交通：6 個零 Exact 子分類與68缺口回補 | — |
| [OO1-140](https://linear.app/001dev/issue/OO1-140/tpi-b06-日常個人衛生用品13及理美容11等剩餘62缺口) | 價格籃／Batch 9 | 日常個人：衛生用品13及理美容11等剩餘62缺口 | — |
| [OO1-143](https://linear.app/001dev/issue/OO1-143/tpi-b09-batch-9-c04-兩個-wip-候選的2020及現行規格補證) | 價格籃／Batch 9 | Batch 9 C04 兩個 WIP 候選的2020及現行規格補證 | — |
| [OO1-144](https://linear.app/001dev/issue/OO1-144/tpi-b10-batch-9-後續-checkpoints-至合理-75-100-筆研究級驗收) | 價格籃／Batch 9 | Batch 9 後續 Checkpoints 至合理 75–100 筆研究級驗收 | — |
| [OO1-145](https://linear.app/001dev/issue/OO1-145/tpi-b11-重新驗證-batch-9-品牌來源集中上限與20筆可比性-b) | 價格籃／Batch 9 | 重新驗證 Batch 9 品牌／來源集中上限與20筆可比性 B | — |
| [OO1-146](https://linear.app/001dev/issue/OO1-146/tpi-b12-維持-candidate-pool-價格變化盲選與跨批去重) | 價格籃／Batch 9 | 維持 Candidate_Pool 價格變化盲選與跨批去重 | — |
| [OO1-163](https://linear.app/001dev/issue/OO1-163/tpi-i04-dashboard-實機fail修復無障礙與安全回歸) | IUI Dashboard | Dashboard 實機FAIL修復、無障礙與安全回歸 | [OO1-161](https://linear.app/001dev/issue/OO1-161/tpi-i02-iui-dashboard-v0-mac-safari-四頁互動與csv匯出原生驗收)、[OO1-162](https://linear.app/001dev/issue/OO1-162/tpi-i03-iui-dashboard-v0-真正-iphone-safari-窄螢幕觸控驗收) |

## P2｜後續治理、維護與發布規劃

| 編號 | 工作線 | 待辦項目 | 前置阻擋 |
|---|---|---|---|
| [OO1-105](https://linear.app/001dev/issue/OO1-105/ho600basket-sealed-與指數解除-locked-的-600-概念驗收) | 正式指數發布 | HO600｜Basket SEALED 與指數解除 LOCKED 的 600 概念驗收 | [OO1-103](https://linear.app/001dev/issue/OO1-103/ho600181600-正式概念增量與工作簿匯出驗證程序)、[OO1-135](https://linear.app/001dev/issue/OO1-135/tpi-b01-建立-50-子分類22-空白子分類的缺口補證索引) |
| [OO1-134](https://linear.app/001dev/issue/OO1-134/tpi-g05-設計-lineargithub-todo-對帳與快照防漂移機制) | 安全／治理 | 設計 Linear↔GitHub TODO 對帳與快照防漂移機制 | — |
| [OO1-152](https://linear.app/001dev/issue/OO1-152/tpi-c06-cpi-02菸酒檳榔及12什項消費細分對照) | 臺北市 CPI | CPI 02菸酒檳榔及12什項消費細分對照 | — |
| [OO1-155](https://linear.app/001dev/issue/OO1-155/tpi-c09-臺北官方-cpi-資料版本異動月份與原始收據持續檢核) | 臺北市 CPI | 臺北官方 CPI 資料版本、異動月份與原始收據持續檢核 | — |
| [OO1-141](https://linear.app/001dev/issue/OO1-141/tpi-b07-教育補習語言線上學習兒童才藝等38缺口補證) | 價格籃／Batch 9 | 教育：補習語言、線上學習、兒童才藝等38缺口補證 | — |
| [OO1-142](https://linear.app/001dev/issue/OO1-142/tpi-b08-休閒展演票券等39缺口與超額類凍結管理) | 價格籃／Batch 9 | 休閒：展演票券等39缺口與超額類凍結管理 | — |
| [OO1-164](https://linear.app/001dev/issue/OO1-164/tpi-i05-iui-dashboard-靜態部署方式與公開資料授權決策) | IUI Dashboard | IUI Dashboard 靜態部署方式與公開資料授權決策 | [OO1-106](https://linear.app/001dev/issue/OO1-106/ho600public-倉庫公開範圍來源授權與敏感檔稽核)、[OO1-161](https://linear.app/001dev/issue/OO1-161/tpi-i02-iui-dashboard-v0-mac-safari-四頁互動與csv匯出原生驗收)、[OO1-162](https://linear.app/001dev/issue/OO1-162/tpi-i03-iui-dashboard-v0-真正-iphone-safari-窄螢幕觸控驗收) |
| [OO1-165](https://linear.app/001dev/issue/OO1-165/tpi-i06-dashboard-快照刷新來源-sha-與版本漂移警示無-actions) | IUI Dashboard | Dashboard 快照刷新、來源 SHA 與版本漂移警示（無 Actions） | — |
| [OO1-166](https://linear.app/001dev/issue/OO1-166/tpi-i07-在-iui-dashboard-新增唯讀-todolinear-工作線面板) | IUI Dashboard | 在 IUI Dashboard 新增唯讀 TODO／Linear 工作線面板 | [OO1-134](https://linear.app/001dev/issue/OO1-134/tpi-g05-設計-lineargithub-todo-對帳與快照防漂移機制) |

## 不可更改的專案邊界

1. **GitHub Actions 使用暫停**：任何 Issue 的建立或更新不得被當成恢復 Actions 的同意。G01/G02 只要求調查與提出有證據的修復方案，變更 main/workflow 須另獲許可。
2. **不改正式狀態**：`main`、七表正式 workbook、600 項指數與發布狀態只有完成正式可重現驗收且另獲核准才可以變更。研究及 Linear issue 本身不能自動加到 181。
3. **證據可靠性**：同 SKU／規格／地理／通路、2020 對 2026 normal/list/base 價、時點、來源雜湊與集中度必須保留；不得以促銷/會員價、跨年份替身或家庭代理虛構。
4. **人口／地理不混用**：臺北市戶長年齡 65+ 不等於退休人口，全國 WGT 來源仍 HOLD；無完整分類映射不得發布 age-head 全率。
5. **Public 與著作權**：當前 repo 為 Public；在任何新發布、部署或批次原始檔擴散前先核對使用權利與個資。
6. **待辦 != 完成**：本輪只建立／更新管理項，未宣稱 18 Python 測試或 Safari/iPhone 測試成功、未執行正式匯入、未啟用 Actions、未部署。

## 機器可讀清單

[HO600-TODO-2026-10-20.csv](./research/todo/HO600-TODO-2026-10-20.csv) 一列一 Issue，包含優先序、Group、Linear ID、依賴、驗收條件及來源連結。若要改變任務狀態／新增依賴，請以 Linear TPI-001 為準，再產生新版 GitHub 快照。每個 Issue 的詳細來源、驗收定義與安全界線以其 Linear 內容為準。

**下一個安全動作**：先處理 [OO1-130 Actions 停用風險](https://linear.app/001dev/issue/OO1-130/tpi-g01-github-actions-停用狀態與-main-自動觸發風險核實)、[OO1-131 歷史 Actions 紀錄](https://linear.app/001dev/issue/OO1-131/tpi-g02-調查-20261015-actions-push-紀錄與重啟風險) 與 [OO1-147 第09類 CPI 範圍](https://linear.app/001dev/issue/OO1-147/tpi-c01-核實第09類休閒文化與-cpi-娛樂費用的官方範圍)，同時可執行 IUI V0 原生驗收 [OO1-160](https://linear.app/001dev/issue/OO1-160/tpi-i01-iui-dashboard-v0-本機python-18項與node語法驗收)。這只是執行順序建議，並非授權改正式環境。
