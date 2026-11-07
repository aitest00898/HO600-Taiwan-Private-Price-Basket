# HO600｜Exact-first 執行流程（2026-11-07）

## 固定邊界

此流程只改**研究排序和證據審核順序**，不放寬既有 Exact-2020 ↔ Exact-2026 Gate，不變更樣本配額、不使用政府價格或 CPI 權重、不建立新通膨總指數。正式權威仍是 main/workbook + canonical/status.json。

本輪主分支錨點：bb90962fb76943c3cce27c9cd937e9120bebcf5e；正式 **199/600**，缺口 **401**，Candidate Pool **434**，Evidence **1,600**，Basket **NOT SEALED**、Index **LOCKED**。研究分支的輸出不增加正式數字。

## 為什麼調整

Batch 9 C01–C08 固定研究級 160 個配對；正式只從中獨立審核、納入 18 個。原研究預審 2 READY / 30 NEEDS_EVIDENCE / 1 HOLD / 127 RESEARCH_ONLY；定向複核後 18 READY。不能把 18/160 視為同質研究樣本的真實統計轉換率，但有必要將正式可比條件提早檢驗。

2026-11-07 從 main 重新讀取：195 個 RESEARCHABLE-CURRENT-ONLY，其中 156 個仍落在正缺額子類（另有其他狀態的候選）。正式 Quota_Control 當前列出 **50 個子類配額列、18 個零 Exact 子類**；早期「50 子分類／22 空白」的 22 是歷史快照，不能取代本次配額檔。

## 立即可操作的並行工作

1. **既有候選優先：** 用 scripts/triage_exact_backfill.py 只讀 main 的 Candidate_Pool、Quota_Control，產生不含任何年度價格／漲幅的研究順位清單；排序優先零 Exact 子類與結構性缺額。這只是待核對清單，不能依排序直接准入。
2. **歷史證據工作：** 每一個選定概念先確立 2020 同期、具日期、可讀的民間正常／牌價來源；若沒有，保留 HOLD / SOURCE_LEAD 而不大規模搜尋新 2026 SKU。政府來源可作 identity 背景但不能提供 HO600 核心價格。
3. **現行對照工作：** 只在有 2020 可核對價後，核對 2026 同一經濟概念、規格／配方／條碼 lineage、地理／通路與價格語意；折扣、第二件優惠、會員有效價及不同平台 markup 不得混成正常價。現行網頁讀到價格不等於歷史配對合格。
4. **互不依賴工作可並行：** 食品自煮、包裝食品、居家、衣著、交通與日常用品採用不同研究帳本；同品牌／同來源／同產品家族仍須在候選正式審核時合併檢查上限。禁止同時改同一個正式 CSV/工作簿。
5. **持續正式交付：** 遇到 5–20 筆真正證據完整的 Exact 候選即可形成**待正式驗收的小包**，不以先完成 75–100 筆研究配對為入庫前置；原始 75–100 只是大研究批次的參考規模。按既有匯出→重匯入→七表對帳→驗證→核准→合併流程准入。不得自行宣稱資料已入正式庫。
6. **停滯處理：** 對同一來源在沒有新增可檢驗假說時，兩次無新證據即停止同條件重試；記錄精確缺口及可替代官方或民間商家來源，轉到其他獨立候選。不要因資料難找而生成無關治理任務。

## 正式證據決策（每個候選必查）

| Check | Pass / Hold |
|---|---|
| 2020 定年 | 同期 2020 可直接核對的售價，不以 2019、2021 或回顧報導推定 |
| 價格口徑 | 正常／牌價／基價，有明確來源，不用促銷或 2020 資料缺價的條碼表 |
| 2026 定年 | 2026 真實可查的同等售價，非未標明有效時間的二次轉述 |
| 可比性 | 相同商品／經濟概念、規格、服務時長、通路／地理；差異需明示且具足夠直接證據 |
| 配額及去重 | 對 main 既存 Candidate Pool、品牌／來源／家族／企業集團集中規則核對，禁止價格漲幅導向挑選 |
| 狀態 | 所有通過後只能寫 READY_FOR_FORMAL_REVIEW；正式准入仍需獨立 workbook 驗收 |

2020 身分線索（例如全聯活動的條碼／印花清單）若沒有正常售價，一律不得變成 Exact-2020。2024 報導追溯過往價格也不等於 2020 當期直接可驗售價。

## 使用及檢查

Run on the same canonical checkout, without network or GitHub Actions:

    python3 scripts/triage_exact_backfill.py --repo-root . --limit 30
    python3 -m unittest discover -s tests -p "test_triage_exact_backfill.py" -v
    python3 scripts/validate_repo.py

The queue is written to stdout, not to main Candidate_Pool. A stored output snapshot is in research/batch-10/2026-11-07-price-blind-backfill-queue.csv; an evidence/probe register (which can contain prices, **separate from candidate selection**) is in research/batch-10/2026-11-07-source-probes.csv. No new CI workflow.

## Measure actual throughput

- 正式新增 Exact 數量／來源 QA 完成的正式候選數（分母必須相同口徑）。
- 由零 Exact 轉為有 Exact 的子分類數。
- 每批有實際 2020 正常價與 2026 可比來源、能進入正式驗收的概念數。
- 對已證偽／無新增線索重複搜尋的耗時及終止原因。

Dashboard、臺北市 CPI 年齡代理、全國權重與公開指數繼續各自研究或暫緩，**不得成為補歷史價或形成小型正式待審包的無關前置**。

GitHub Actions 保持全域停用；正式 main、原工作簿、Index 和既有研究固定 160 ledger 不在本次更新範圍。
