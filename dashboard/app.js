/* HO600 IUI V0 — read-only. No network calls, cookies, storage or writes.
 * Static, reviewed snapshot is provided by ./snapshot.js. There is no auth/token.
 */
(function () {
  "use strict";
  const D = window.HO600_SNAPSHOT;
  const app = document.getElementById("app-content");
  const title = document.getElementById("pageTitle");
  const subtitle = document.getElementById("pageSubtitle");
  const crumb = document.getElementById("breadcrumb");
  const headings = {
    overview: ["研究全貌", "從正式價格籃到研究驗收：只顯示可追溯的已確認進度。", "總覽"],
    basket: ["價格籃與研究配額", "正式主線和 Batch 9 研究分流；配額依保留歷史樣本政策。", "價格籃"],
    cohorts: ["戶長年齡與 CPI", "臺北市 2020 支出結構與 CPI 局部對照，不是完整族群通膨率。", "年齡與 CPI"],
    evidence: ["證據與驗收", "逐項查看提交、原始來源與不能跨越的正式發布門檻。", "證據"]
  };
  const state = {tab: "overview", period: "A", mode: "strict", age: "65歲及以上", status: "ALL"};
  const nf = new Intl.NumberFormat("zh-TW");
  const fmt = (n, digits = 1) => Number(n).toLocaleString("zh-TW", {minimumFractionDigits:digits, maximumFractionDigits:digits});
  const esc = (value) => String(value == null ? "" : value).replace(/[&<>"']/g, c => ({'&':'&amp;', '<':'&lt;', '>':'&gt;', '"':'&quot;', "'":'&#39;'}[c]));
  const attr = esc;
  const clamp = (x, low, high) => Math.min(high, Math.max(low, Number(x) || 0));
  const link = (url, label, cls = "panel-link") => '<a class="' + cls + '" href="' + attr(url) + '" target="_blank" rel="noopener noreferrer">' + esc(label) + ' ↗</a>';
  const pill = (v, label) => '<span class="pill ' + v + '">' + esc(label) + '</span>';
  const card = (label, val, foot, tone = "") => '<div class="kpi"><div class="kpi-top"><span>' + esc(label) + '</span><span class="kpi-icon">↗</span></div><div class="kpi-number ' + tone + '">' + esc(val) + '</div><div class="kpi-caption">' + esc(foot) + '</div></div>';
  const panel = (name, desc, content, foot = "", action = "") => '<article class="panel"><header class="panel-header"><div><h2 class="panel-title">' + esc(name) + '</h2>' + (desc ? '<p class="panel-desc">' + esc(desc) + '</p>' : '') + '</div>' + action + '</header>' + content + (foot ? '<div class="panel-footer">' + foot + '</div>' : '') + '</article>';
  const pct = (n, digits = 1) => fmt(n, digits) + "%";
  const sourceURL = D?.links?.repository || "#";
  let toastTimer = 0;

  function verify() {
    if (!D || D.schemaVersion !== "1.0.0") throw Error("Snapshot is missing or incompatible.");
    const c = D.canonical, co = D.cohort;
    if (c.basketSealed || c.indexStatus !== "LOCKED" || c.accepted + c.remaining !== c.target) throw Error("Formal basket release invariant violated.");
    const v = c.quota.reduce((acc, e) => {acc.accepted += e.accepted; acc.needed += e.needed; acc.target += e.target; return acc;}, {accepted:0,needed:0,target:0});
    if (c.quota.length !== 7 || v.accepted !== c.accepted || v.needed !== c.remaining || v.target !== c.target) throw Error("Official quota mismatch.");
    if (co.age.length !== 7 || co.crosswalk.length !== 12 || co.fullCohortRatesReleased !== 0) throw Error("Cohort publication invariant violated.");
    if (co.crosswalk.filter(x => x.status === "PROVISIONAL").length !== 1) throw Error("Missing provisional class 09 caveat.");
    for (const x of co.age) {
      for (const period of ["A","B"]) {
        if (!x.periods[period] || !Number.isFinite(x.periods[period].coverage) || x.periods[period].coverage >= 95) throw Error("Age CPI rate cannot be released.");
      }
    }
  }

  function quotaBars(rows) {
    return rows.map(x => {
      const p = clamp(x.accepted / x.target * 100, 0, 100);
      return '<div class="bar-line"><div class="bar-label"><strong>' + esc(x.domain) + '</strong><span class="values">' +
        nf.format(x.accepted) + ' / ' + nf.format(x.target) + '</span></div><div class="track" role="img" aria-label="' +
        attr(x.domain + " 正式 " + x.accepted + "，缺口 " + x.needed) + '"><div class="track-fill" style="width:' + p + '%"></div><div class="track-rest"></div></div><div class="bar-sub"><span>' +
        esc(pct(p)) + ' 已達成</span><span>缺口 ' + nf.format(x.needed) + '</span></div></div>';
    }).join("");
  }
  function stageRows() {
    return D.research.checkpoints.map(x => '<div class="milestone ' + (x.status === "WIP" ? "wip" : "") +
      '"><div class="milestone-tag">' + esc(x.id) + '</div><div class="milestone-body"><strong>' +
      (x.status === "PASS" ? esc(x.accepted + " 筆研究級驗收") : "尚未形成正式 Checkpoint") +
      '</strong><small>' + (x.status === "PASS" ? "Research PASS · 未納入 main" : esc(x.provisional + " provisional · " + x.hold + " HOLD")) +
      '</small></div>' + link(x.url, "來源") + '</div>').join("");
  }
  function overview() {
    const C = D.canonical, R = D.research, T = D.cohort;
    const progress = C.accepted / C.target * 100;
    const largest = [...C.quota].sort((a,b) => b.needed - a.needed).slice(0,4);
    const kpis = '<div class="kpi-grid">' +
      card("正式 Exact 概念", C.accepted + " / " + C.target, "main · Batch " + C.batch, "teal") +
      card("尚待完成的正式概念", nf.format(C.remaining), "正式配額缺口，不含候選", "") +
      card("Batch 9 研究 PASS", "60", "C01–C03 各 20，尚未正式匯入", "") +
      card("可發布完整年齡通膨", "0 / 7", "七組皆 HOLD；不發布完整率", "warn") + '</div>';
    const donut = '<div class="progress-layout"><div class="ring" style="--progress:' + progress.toFixed(6) +
      '%" role="img" aria-label="正式價格概念完成率 '+pct(progress,2)+'"><div class="ring-info"><strong>' + fmt(progress,2) + '%</strong><small>正式完成率</small></div></div><div class="ring-copy"><strong>' +
      C.accepted + ' 已有歷史價格對</strong><p>目標 ' + C.target + ' 項經濟概念<br>候選 ' +
      C.candidates + ' 筆／證據 ' + nf.format(C.evidence) + ' 筆</p><div class="tiny-stat"><i class="dot"></i>' +
      C.accepted + ' 正式預審 Exact</div><div class="tiny-stat"><i class="dot pale"></i>' + C.remaining +
      ' 個缺口</div></div></div>';
    const priorities = largest.map((x,i) => '<div class="insight-item"><div class="insight-index">' +
      String(i+1).padStart(2,"0") + '</div><div><b>' + esc(x.domain) + ' · 尚缺 ' + x.needed +
      ' 項</b><p>目前 ' + x.accepted + ' / ' + x.target + '；依正式配額優先補足。</p></div></div>').join("");
    const stat = '<div class="metric-strip"><div><strong>48 / 48</strong><small>臺北 CPI 分類月份完整</small></div><div><strong>84</strong><small>2020 年戶長年齡權重格數</small></div><div><strong>2 + 1</strong><small>穩健對照 + 暫定第 09 類</small></div><div><strong>0 / 7</strong><small>完整族群通膨率</small></div></div>';
    return kpis + '<div class="dashboard-grid">' + panel("600 項價格籃進度","正式主線獨立計算，不累加 Batch 9",donut,
      pill("warning","Index LOCKED") + '　Basket NOT SEALED',
      link(D.links.canonicalStatus,"主線來源")) +
      panel("優先補足的領域","按最終目標缺口由大到小",'<div class="insight-list">' + priorities + '</div>') +
      panel("七大領域配額","正式已取得 / 各領域目標",quotaBars(C.quota),
      '<div class="legend"><span><i class="teal"></i>正式 Exact</span><span><i class="gray"></i>未完成</span></div>') +
      panel("Batch 9 研究進度","研究級驗收不等於正式納入",stageRows()) +
      '<div class="full">' + panel("臺北市年齡代理研究","已完成資料取得；價目分類對照仍不足以發布完整率",stat +
      '<div class="big-note"><b>未發布原因</b>　食品、住宅與醫療等必要支出仍無足夠 CPI 對照。第 09 類休閒文化暫定映射影響很大，預設顯示排除版本。</div>',
      '',link(D.links.study,"查看分類風險")) + '</div></div>';
  }
  function basket() {
    const C = D.canonical;
    const table = '<div class="data-table-scroll"><table class="data-table"><thead><tr><th>領域</th><th class="num">正式 Exact</th><th class="num">尚缺</th><th class="num">最終配額</th><th class="num">完成率</th></tr></thead><tbody>' +
      C.quota.map(x => '<tr><td><strong>' + esc(x.domain) + '</strong></td><td class="num">' +
      x.accepted + '</td><td class="num">' + x.needed + '</td><td class="num">' +
      x.target + '</td><td class="num">' + pct(x.accepted/x.target*100,1) + '</td></tr>').join("") +
      '</tbody></table></div>';
    const checks = '<div class="state-list"><div class="state-row"><div><div class="state-label">Canonical Workbook</div><div class="state-sub">永久七張表 · 完整匯入／匯出驗證後方可變更</div></div>' + pill("good","7 張") + '</div>' +
      '<div class="state-row"><div><div class="state-label">Batch 8 驗證紀錄</div><div class="state-sub">data/Validation_Release.csv</div></div>' + pill("good",C.validationPass+"/"+C.validationChecks+" PASS") + '</div>' +
      '<div class="state-row"><div><div class="state-label">候選價格盲選</div><div class="state-sub">選擇候選時不可使用 2020／2026 漲跌資訊</div></div>' + pill("good","維持") + '</div>' +
      '<div class="state-row"><div><div class="state-label">Index_Calc</div><div class="state-sub">Basket 尚未滿 600 且未封存</div></div>' + pill("warning","LOCKED") + '</div></div>';
    return '<div class="kpi-grid">' +
      card("正式來源", "main", "Batch " + C.batch + " · 唯一權威") +
      card("正式完成率",pct(C.accepted/C.target*100,2),nf.format(C.accepted)+" / "+C.target,"teal")+
      card("尚缺項目",nf.format(C.remaining),"以 Legacy-preserving 配額衡量")+
      card("候選研究紀錄",nf.format(C.candidates),"非正式 Exact")+'</div><div class="dashboard-grid">' +
      panel("領域完成分布","配額來自 main / Quota_Control.csv",quotaBars(C.quota),"舊有超額領域保留，不直接刪除已取得的歷史證據。",link(D.links.quota,"配額來源")) +
      panel("Checkpoint 追蹤","C01–C03 研究級 PASS · C04 WIP",stageRows(),'<div class="big-note">研究中的 60 筆不應與 main 181 筆相加成「241 筆正式完成」。</div>') +
      '<div class="full">' + panel("正式配額明細","目前七大領域可追溯分母",table,"完成率＝main 已預審 Exact ÷ final legacy-preserving target。") + '</div>' +
      panel("驗收與安全邊界","不啟用 GitHub Actions",checks,"研究 branch 運作不改寫正式工作簿。") +
      panel("下一個實作決策","對準尚缺的經濟概念",
      '<div class="insight-list"><div class="insight-item"><div class="insight-index">01</div><div><b>繼續 Batch 9 C04</b><p>優先現有 current-only 候選的 Exact-2020 證據。</p></div></div><div class="insight-item"><div class="insight-index">02</div><div><b>保留來源等級</b><p>核對 SKU、常態價格、日期與通路，不以特價或推算價格補缺口。</p></div></div><div class="insight-item"><div class="insight-index">03</div><div><b>正式發布門檻</b><p>須完成 600 項及完整匯出／匯入／七表驗收後再解鎖。</p></div></div></div>',
      '',link(D.links.researchHandoff,"研究交接"))+'</div>';
  }

  function ageBars(rows, key, max, exploratory) {
    return '<div class="age-bars">' + rows.map(x => {
      const val = x.periods[state.period][key];
      const width = clamp(val/max*100, 0, 100);
      return '<div class="age-line"><div class="age-name">' + esc(x.group) + '</div><div class="age-track' +
        (exploratory?" exploratory":"") + '" role="img" aria-label="' + attr(x.group + " 覆蓋率 " + pct(val,2)) +
        '"><div class="age-fill" style="width:' + width.toFixed(4) + '%"></div></div><div class="age-val">' + pct(val,2) +
        '</div></div>';
    }).join("") + '</div>';
  }
  function contributionBars(rows, period, key, max) {
    return '<div class="age-bars">' + rows.map(x => {
      const v=x.periods[period][key];
      const w=clamp(v/max*100,0,100);
      return '<div class="age-line"><div class="age-name">' + esc(x.group) + '</div><div class="age-track ' +
        (key==="partial"?"exploratory":"") + '" role="img" aria-label="' + attr(x.group+" 部分貢獻 "+fmt(v,3)+" 百分點") +
        '"><div class="age-fill" style="width:' + w.toFixed(4) + '%"></div></div><div class="age-val">' + fmt(v,3) +
        '</div></div>';
    }).join("") + '</div>';
  }
  function controls() {
    return '<div class="controls"><span class="control-label">比較期間</span><div class="segmented" role="group" aria-label="CPI 比較期間">' +
      ["A","B"].map(p => '<button class="seg-btn" data-period="'+p+'" aria-pressed="'+(p===state.period)+'">'+(p==="A"?"2020→2026":"2020→2025")+'</button>').join("") +
      '</div><span class="control-label">分類假設</span><div class="segmented" role="group" aria-label="分類對照假設">' +
      '<button class="seg-btn" data-mode="strict" aria-pressed="'+(state.mode==="strict")+'">保守：排除 09</button>' +
      '<button class="seg-btn" data-mode="provisional" aria-pressed="'+(state.mode==="provisional")+'">暫定：納入 09</button>' +
      '</div></div>';
  }
  function cohort() {
    const T=D.cohort, rows=T.age, p=state.period, strict=state.mode==="strict";
    const k=strict?"strictCoverage":"coverage", v=strict?"strictPartial":"partial";
    const chosen=rows.find(x=>x.group===state.age)||rows[rows.length-1];
    const covs=rows.map(x=>x.periods[p][k]), min=Math.min(...covs), max=Math.max(...covs);
    const desc='<div class="mini-banner"><strong>固定研究期間：</strong>'+esc(T.periods[p])+'。已發布的是「部分貢獻」，非完整率；'+(strict?"預設排除第 09 類休閒文化的暫定 CPI 對照。":"目前使用包含第 09 類的探索性對照；不可視為分類完成。")+'</div>';
    const selects='<div class="controls"><label class="control-label" for="ageSelect">檢視年齡</label><select class="select" id="ageSelect">'+rows.map(x=>'<option value="'+attr(x.group)+'" '+(x.group===chosen.group?"selected":"")+'>'+esc(x.group)+'</option>').join("")+'</select></div>';
    const ageHead='<div class="age-compare"><div><div class="age-detail-num">'+pct(chosen.housingHealthShare,2)+'</div><div class="age-detail-desc">住宅 + 醫療，2020 年家庭支出占比</div></div><div><div class="age-detail-num">'+nf.format(chosen.annualSpend)+'<small> 元／年</small></div><div class="age-detail-desc">該戶長年齡組平均每戶消費總額</div></div></div>';
    const split='<div class="bar-line"><div class="bar-label"><strong>住宅能源</strong><span class="values">'+pct(chosen.housingShare,2)+'</span></div><div class="track"><div class="track-fill" style="width:'+clamp(chosen.housingShare,0,100)+'%"></div></div></div><div class="bar-line"><div class="bar-label"><strong>醫療保健</strong><span class="values">'+pct(chosen.healthShare,2)+'</span></div><div class="track alt"><div class="track-fill" style="width:'+clamp(chosen.healthShare,0,100)+'%"></div></div></div>';
    const conval=chosen.periods[p];
    const warn='<div class="big-note"><b>發布門檻未通過</b>　每組至少需 95% 加權涵蓋，且食品、住宅、醫療必須完整對應。目前即使包含暫定 09 類也只有 7.57–15.26%；不能將未映射權重重新歸一化。</div>';
    const coverage=ageBars(rows,k,20,!strict);
    const cont=contributionBars(rows,p,v,3,!strict);
    const statusText={"MAPPED":"已對應","PROVISIONAL":"範圍待複核","SPLIT_REQUIRED":"需拆分","UNMAPPED":"無對應"};
    const statusStyle={"MAPPED":"good","PROVISIONAL":"warning","SPLIT_REQUIRED":"neutral","UNMAPPED":"danger"};
    const cw=T.crosswalk.filter(x=>state.status==="ALL"||x.status===state.status);
    const crossTable='<div class="table-filter"><div class="secondary-text">2020 官方 12 大類 · 暫定不等於最終認證</div><div class="controls"><label class="control-label" for="statusSelect">狀態</label><select id="statusSelect" class="select"><option value="ALL">全部 12 類</option>'+Object.entries(statusText).map(([key,name])=>'<option value="'+key+'" '+(state.status===key?"selected":"")+'>'+name+'</option>').join("")+'</select></div></div><div class="data-table-scroll"><table class="data-table"><thead><tr><th>代碼</th><th>家庭支出類別</th><th>官方 CPI 對照</th><th>驗收狀態</th></tr></thead><tbody>'+cw.map(x=>'<tr><td class="mono">'+esc(x.code)+'</td><td><strong>'+esc(x.label)+'</strong></td><td class="secondary-text">'+esc(x.cpi||"尚無")+'</td><td>'+pill(statusStyle[x.status],statusText[x.status])+'</td></tr>').join("")+'</tbody></table></div>';
    return '<div class="kpi-grid">' +
      card("2020 年戶長年齡代理","7 組",T.weightCells+" 格支出權重已對帳","teal")+
      card("官方 CPI 分類月資料","48 / 48",T.cpiMonthlyRows.toLocaleString("zh-TW")+" 筆 · 截至 "+T.cpiThrough) +
      card("已確認全域對照","2 / 12","另 1 類休閒文化為暫定") +
      card("完整年齡通膨率","HOLD","0 / 7 達成發布條件","warn") +
      '</div><div class="full mini-banner" style="margin-bottom:15px"><strong>地理／人口：</strong>臺北市經濟戶長年齡代理，不是全國、不代表受僱或真正退休家庭。</div>'+
      '<div class="panel" style="margin-bottom:15px">'+controls()+'<div style="margin-top:13px">'+desc+'</div></div>'+
      '<div class="dashboard-grid">'+
      panel("七組加權 CPI 覆蓋率",strict?"僅衣著＋教育兩類（保守）":"衣著＋教育＋第 09 類（待複核）",coverage,'圖上滿刻度是 20%，並非正式 95% 門檻。覆蓋率 ' +pct(min,2)+'–'+pct(max,2)+'；完整率 7/7 HOLD。')+
      panel("已對應類別對總預算的部分貢獻","單位為百分點（pp）；不是完整族群通膨率",cont,
      '本圖滿刻度為 3 pp，僅顯示已對應項目。'+ (strict?"第 09 類已排除。":"第 09 類映射尚未確認。"))+
      panel("2020 年家庭支出結構","年齡組可切換，支出金額是每戶年平均",selects+'<div style="margin-top:16px">'+ageHead+split+'</div>',
      '公布大類與細項四捨五入可能相差少量元；65+ 戶長不等於退休。',link(D.links.originalAge,"家庭調查原始 CSV"))+
      panel("該組局部分析","以 2020 年原始支出占比，不重新歸一化",
      '<div class="metric-strip"><div><strong>'+pct(conval[k],2)+'</strong><small>已覆蓋權重</small></div><div><strong>+'+fmt(conval[v],4)+' pp</strong><small>部分貢獻（非通膨率）</small></div><div><strong>'+pct(100-conval[k],2)+'</strong><small>未覆蓋份額</small></div></div>'+
      '<div class="big-note">'+(strict?'第 09 類已排除。':'第 09 類含有大量套裝旅遊及其他非服務支出，CPI 娛樂費用對照仍待來源核實。')+'</div>',
      '原始官方全體 CPI ' +p+ ' 期間變化為 '+pct(T.generalCpi[p],4)+'，僅作不同人口／權重的背景參考；不可與這裡的部分貢獻等同比較。')+
      '<div class="full">'+panel("CPI 與 12 類家庭支出 crosswalk","2 已對應 · 1 暫定 · 8 需拆分 · 1 未對應",crossTable,"類別 01 食品、04 住宅、06 醫療仍未完整對應。"+link(D.links.crosswalk,"核對檔"))+'</div>'+
      '<div class="full">'+warn+'</div></div>';
  }

  function evidence() {
    const C = D.canonical, T=D.cohort;
    const status = '<div class="state-list">'+[
      ["Canonical main", "正式價目唯一來源",pill("good",C.accepted+"/"+C.target)],
      ["Batch 9 C01–C03","研究級 PASS，尚未正式匯入",pill("neutral","60 RESEARCH")],
      ["2020 臺北市戶長支出","來源 CSV／PDF 大類對帳",pill("good",T.officialAgeCsvPdfParentChecks)],
      ["臺北市 CPI 原始檔","48 類完整月資料，2021＝100",pill("good","16,560 筆")],
      ["第 09 類價格對照","休閒文化包含套裝旅遊等細項",pill("warning","PROVISIONAL")],
      ["全國 WORK／RETIRE","正式權重與完整分類未具備",pill("danger","HOLD")],
      ["正式籃子指數", "Basket 未封存",pill("warning","LOCKED")],
      ["GitHub Actions","依使用者決策暫停；本版不觸發",pill("neutral","PAUSED")],
    ].map(x=>'<div class="state-row"><div><div class="state-label">'+esc(x[0])+'</div><div class="state-sub">'+esc(x[1])+'</div></div>'+x[2]+'</div>').join("")+'</div>';
    const names={"status":"正式狀態","quota":"七大領域配額","validation":"正式驗收紀錄","age":"2020 戶長支出結構","cpi":"CPI 計算驗收摘要","sensitivity":"第 09 類排除敏感度","crosswalk":"12 類 CPI 對照"};
    const sources=D.sources.map(x=>'<div class="source-record"><div><strong>'+esc(names[x.name]||x.name)+'</strong><div class="small-code">blob '+esc(x.blobSha.slice(0,16))+'…　·　'+esc(x.ref)+'</div></div>'+link(x.link,"查看")+'</div>').join("");
    const risks='<div class="insight-list">'+[
      ["資料權威分隔", "main 是唯一正式來源。研究分支 60 筆不等於正式新增 60 項。"],
      ["分類跨資料源對照", "CPI 原始時序完整，但家庭支出與 CPI 口徑未完成；不能只憑名稱自動配對。"],
      ["人口與地理", "臺北市戶長 65 歲以上，不是全國退休戶。"],
      ["GitHub 可見性", "倉庫目前為 PUBLIC。此靜態面板只引用公開來源，不含金鑰或個人資料。"],
      ["Actions 安全", "本 Dashboard 不需要 workflow、CI 或部署。main 仍存有 push 觸發設定，尚未改動。"]
    ].map((x,i)=>'<div class="insight-item"><div class="insight-index">'+String(i+1).padStart(2,"0")+'</div><div><b>'+esc(x[0])+'</b><p>'+esc(x[1])+'</p></div></div>').join("")+'</div>';
    return '<div class="kpi-grid">'+card("正式驗收紀錄",C.validationPass+" / "+C.validationChecks,"main / Validation_Release.csv","teal")+
      card("來源數量",D.sources.length.toString(),"快照引用的已讀取檔案數")+
      card("月 CPI 指數",nf.format(T.cpiMonthlyRows),"48 類，1998 至 2026/09")+
      card("全國族群發布","HOLD","WORK／RETIRE 0/2，不能推估","warn")+
      '</div><div class="dashboard-grid">'+
      panel("研究與發布 Gate","無法越權升級正式狀態",status,"任何來源被替換時必須重建快照及重新驗證。")+
      panel("驗收風險清單","需持續保留的限制",risks) +
      '<div class="full">'+panel("資料來源與版本","固定 SHA／提交，點選可查看 GitHub 檔案",'<div class="source-list">'+sources+'</div>',
      '<div class="line-note">主線 commit：<span class="mono">'+esc(D.identity.canonicalCommit)+'</span>　　研究 commit：<span class="mono">'+esc(D.identity.researchCommit)+'</span></div>')+'</div>'+
      '<div class="full">'+panel("治理邊界","唯讀 V0，不包含可寫入、排程或啟動 Actions 的功能",
      '<div class="rule-summary"><div class="rule-box"><b>'+esc(D.identity.authoritativeBranch)+'</b><span>正式來源分支</span></div><div class="rule-box"><b>未部署</b><span>本次僅建立靜態程式</span></div><div class="rule-box"><b>0</b><span>憑證、連接器、網路呼叫</span></div></div>',
      '這份快照不會自動更新。重新產生資料與重新驗證後，才能更新頁面。',link(D.links.researchHandoff,"最新研究交接"))+'</div></div>';
  }

  function showToast(message) {
    const e=document.getElementById("toast");
    if (!e) return;
    e.textContent=message; e.classList.add("show");
    clearTimeout(toastTimer);
    toastTimer=setTimeout(()=>e.classList.remove("show"),2800);
  }
  function csvRows() {
    let head,rows,basename;
    if(state.tab==="cohorts"){
      head=["year","age_head","window","mapping_mode","coverage_pct","partial_contribution_pp","uncovered_pct","full_rate_status"];
      rows=D.cohort.age.map(x=>{const t=x.periods[state.period],k=state.mode==="strict"?"strictCoverage":"coverage",v=state.mode==="strict"?"strictPartial":"partial";return [2020,x.group,state.period,state.mode,t[k],t[v],100-t[k],"HOLD_NOT_A_FULL_RATE"]});
      basename="ho600_taipei_age_head_partial";
    }else if(state.tab==="evidence"){
      head=["name","branch","blob_sha","source_url"];rows=D.sources.map(s=>[s.name,s.ref,s.blobSha,s.link]);basename="ho600_evidence";
    }else if(state.tab==="overview"){
      head=["domain","canonical_exact","remaining","final_target","completed_pct"];
      rows=D.canonical.quota.map(x=>[x.domain,x.accepted,x.needed,x.target,(x.accepted/x.target*100).toFixed(4)]);basename="ho600_overview";
    }else{
      head=["domain","canonical_exact","remaining","final_target","original_target","completed_pct"];
      rows=D.canonical.quota.map(x=>[x.domain,x.accepted,x.needed,x.target,x.originalTarget,(x.accepted/x.target*100).toFixed(4)]);basename="ho600_quota";
    }
    return {head,rows,basename};
  }
  function exportCSV() {
    const {head,rows,basename}=csvRows();
    const wrap=s=>'"'+String(s ?? "").replace(/"/g,'""')+'"';
    const content="\uFEFF"+[head.map(wrap).join(","),...rows.map(r=>r.map(wrap).join(","))].join("\r\n")+"\r\n";
    const blob=new Blob([content],{type:"text/csv;charset=utf-8"});
    const url=URL.createObjectURL(blob),a=document.createElement("a");
    a.href=url;a.download=basename+"_"+D.snapshotDate+".csv";a.style.display="none";
    document.body.appendChild(a);a.click();a.remove();setTimeout(()=>URL.revokeObjectURL(url),1200);
    showToast("已匯出目前分頁資料 · "+rows.length+" 筆");
  }
  function closeNav(){
    document.getElementById("sidebar").classList.remove("open");
    document.getElementById("workspace").classList.remove("menu-open");
    document.getElementById("menuToggle").setAttribute("aria-expanded","false");
  }
  function tabFromHash(){const match=(window.location.hash||"").replace(/^#/,"");return Object.prototype.hasOwnProperty.call(headings,match)?match:"overview"}
  function switchTab(tab) {
    if(!headings[tab]) tab="overview";
    state.tab=tab;
    const header=headings[tab];title.textContent=header[0];subtitle.textContent=header[1];crumb.textContent=header[2];
    document.querySelectorAll("[data-tab]").forEach(e=>{
      const selected=e.dataset.tab===tab;e.classList.toggle("active",selected);
      if(selected) e.setAttribute("aria-current","page");else e.removeAttribute("aria-current");
    });
    app.innerHTML = (tab==="overview"?overview():tab==="basket"?basket():tab==="cohorts"?cohort():evidence());
    document.getElementById("exportBtn").setAttribute("title",tab==="cohorts"?"匯出所選假設與期間的局部貢獻":"匯出目前分頁資料");
    closeNav();
  }
  function init(){
    try{verify();}catch(error){app.innerHTML='<div class="callout-error"><b>Dashboard 驗證失敗；已停止顯示數值。</b><p>'+esc(error.message)+'</p></div>';return}
    document.getElementById("snapshotDate").textContent="快照 "+D.snapshotDate;
    document.getElementById("githubLink").href=D.links.repository;
    document.getElementById("footerSource").href=D.links.canonicalStatus;
    document.getElementById("indexPill").textContent="INDEX "+D.canonical.indexStatus;
    switchTab(tabFromHash());
    document.querySelectorAll("[data-tab]").forEach(e=>e.addEventListener("click",()=>{
      const tab=e.dataset.tab;state.tab=tab;
      if(location.hash!=="#"+tab)location.hash=tab;else{switchTab(tab);window.scrollTo({top:0,behavior:"smooth"})}
    }));
    document.getElementById("menuToggle").addEventListener("click",()=>{
      const el=document.getElementById("sidebar"),opened=el.classList.toggle("open");
      document.getElementById("workspace").classList.toggle("menu-open",opened);
      document.getElementById("menuToggle").setAttribute("aria-expanded",String(opened));
    });
    document.getElementById("mobileBackdrop").addEventListener("click",closeNav);
    document.addEventListener("keydown",e=>{if(e.key==="Escape")closeNav()});
    app.addEventListener("click",e=>{
      const period=e.target.closest("[data-period]");
      if(period){state.period=period.dataset.period;switchTab("cohorts");return;}
      const mode=e.target.closest("[data-mode]");
      if(mode){state.mode=mode.dataset.mode;switchTab("cohorts");return;}
    });
    app.addEventListener("change",e=>{
      if(e.target.id==="ageSelect"){state.age=e.target.value;switchTab("cohorts");}
      else if(e.target.id==="statusSelect"){state.status=e.target.value;switchTab("cohorts");}
    });
    document.getElementById("exportBtn").addEventListener("click",exportCSV);
    window.addEventListener("hashchange",()=>{switchTab(tabFromHash());window.scrollTo({top:0,behavior:"auto"})});
  }
  if(document.readyState==="loading"){document.addEventListener("DOMContentLoaded",init,{once:true});}else init();
})();
