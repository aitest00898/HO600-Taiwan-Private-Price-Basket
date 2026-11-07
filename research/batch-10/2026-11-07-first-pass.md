# Batch 10｜首次 Exact-first 探索收據（2026-11-07）

本研究採用 main commit bb90962fb76943c3cce27c9cd937e9120bebcf5e 的正式 Candidate Pool、Quota Control，**沒有修改官方數字**。研究分支與 main 隔離，GitHub Actions 未使用。

## 結果

- 434 個正式候選，其中 195 個是 RESEARCHABLE-CURRENT-ONLY。
- 156 個既有現價候選在仍有缺口的子類中；此數字只是可研究母體，不是 156 個準備准入。
- 當前正式配額表包含 **50 子分類、18 個零 Exact 子分類**。若把表尾的 7 個領域匯總當成子類，會誤算為 57。
- 使用 price-blind 程式選出 30 個研究優先候選，不將任何價格／漲跌／通膨率放入選擇清單。完整 CSV 同資料夾。
- 第一次查閱 5 個既有民生概念的現價頁面與歷史線索：**0 筆 Exact 可准入；5 筆 HOLD**。沒有 2020 同通路、正常價的直接證據，不使用其他年度或促銷價補齊。

## 查核的五項

| 候選 | 現價網頁觀察 | 歷史問題 | 判定 |
|---|---|---|---|
| LEG-EC-315 台鹽高級碘鹽 1kg | [PXGO 17元](https://shop.pxgo.com.tw/hourArrive/goods/253620-51220002-4711271000014) | [2024 年新聞](https://ec.ltn.com.tw/article/breakingnews/4776816) 回述調價前 15 元，但不是 2020 同商店當期正常價證據；2026頁面現價口徑亦待核 | HOLD |
| LEG-EC-313 可果美蕃茄醬 500g | [PXGO 72元](https://shop.pxgo.com.tw/hourArrive/goods/352009-09010242-4710134023276) | 沒找到 2020 當期全聯正常價；現在的全聯其他線上頁另稱 72 元「特價」 | HOLD |
| LEG-EC-349 金蘭特級醬油 1000ml | [PXGO 82元](https://shop.pxgo.com.tw/hourArrive/goods/237901-20133956-4710012129069) | [PXBOX](https://pxbox.es.pxmart.com.tw/product/177711) 將 82 元標成特價，標示原價 89 元；2020 正常價缺失 | HOLD |
| LEG-EC-309 乖乖五香 52g | [PXGO 活動價目 24元](https://shop.pxgo.com.tw/hourArrive/activity/334) | 活動頁的 24 元不保證是正常價，且缺 2020 當期相同規格及通路正常價 | HOLD |
| LEG-EC-342 義美小泡芙巧克力 65g | [PXGO 33元](https://shop.pxgo.com.tw/hourArrive/goods/242266-20467304-4710126021006) | 尚無 2020 當期相同通路正常價與歷史 SKU 證明 | HOLD |

詳細機器可讀記錄：[2026-11-07-source-probes.csv](2026-11-07-source-probes.csv)。

此處的 2026 網頁數字是查核時顯示的**候選線索**，未取得可永久讀回的原始頁面 SHA 收據，也未對它們判定無條件一般牌價。正式 2026 Evidence 仍以 canonical 的來源及其既有證據為準；本輪並未重寫任何正式 Evidence。

## 下一批搜尋決策

優先對 30 筆候選查找 2020 日期、商家及正常價；先查是否已有 2020 同 SKU、同通路原始價目，再確認 2026 正價及配方／條碼。不再對缺 2020 的上述五項重複追問同一網頁（除非有新的原始證據線索）。在獨立子類可並行搜尋；第一批真正滿足原 Gate 的 5–20 筆才進入正式包驗收。

正式主分支維持 199/600、剩餘 401；Basket NOT SEALED、Index LOCKED。研究不代表 formally admitted 或可產出全台體感通膨率。
