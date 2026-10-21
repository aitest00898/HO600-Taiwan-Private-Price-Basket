/* Optional *real browser* smoke: append ?smoke=1 to dashboard/index.html.
 * Runs against the real current DOM on file:// or local HTTP. No network.
 * Never modifies stored project data and intercepts the test CSV download.
 */
(function () {
  "use strict";
  const messages=[];
  const wait=(ms=100)=>new Promise(resolve=>setTimeout(resolve,ms));
  const text=()=>document.getElementById("app-content")?.innerText||"";
  const node=(selector)=>document.querySelector(selector);
  function assertion(name,condition,detail="") {
    messages.push({name,passed:!!condition,detail});
  }
  function click(selector) {
    const el=node(selector);
    if(!el)throw Error("Control not found: "+selector);
    el.click();
    return wait();
  }
  function change(selector,value) {
    const el=node(selector);
    if(!el)throw Error("Select not found: "+selector);
    el.value=value;
    el.dispatchEvent(new Event("change",{bubbles:true}));
    return wait();
  }
  function display() {
    let host=document.getElementById("ho600-smoke-results");
    if(!host){
      host=document.createElement("aside");
      host.id="ho600-smoke-results";
      host.setAttribute("role","status");
      host.style.cssText="position:fixed;z-index:99999;right:12px;bottom:12px;width:min(440px,calc(100vw - 24px));max-height:52vh;overflow:auto;background:#fff;color:#162e34;border:2px solid #377d70;border-radius:12px;box-shadow:0 8px 40px #1c3b4d45;padding:12px;font:13px/1.5 -apple-system,BlinkMacSystemFont,sans-serif";
      document.body.appendChild(host);
    }
    const passed=messages.filter(x=>x.passed).length,failed=messages.length-passed;
    host.replaceChildren();
    const h=document.createElement("h2");
    h.style.cssText="font-size:15px;margin:0 0 8px";
    h.textContent="HO600 實際瀏覽器驗收 · "+passed+"/"+messages.length+" "+(failed?"FAIL":"PASS");
    host.appendChild(h);
    const p=document.createElement("p");
    p.style.cssText="font-size:11px;color:#617780;margin:0 0 8px";
    p.textContent="僅測目前瀏覽器／視窗；不等於另一台 Mac、Safari 或實體 iPhone 驗收。";
    host.appendChild(p);
    const ul=document.createElement("ul");
    ul.style.cssText="padding-left:18px;margin:4px 0 8px";
    for(const m of messages){
      const li=document.createElement("li");
      li.style.color=m.passed?"#276c57":"#ae362b";
      li.textContent=(m.passed?"PASS · ":"FAIL · ")+m.name+(m.detail?" — "+m.detail:"");
      ul.appendChild(li);
    }
    host.appendChild(ul);
    const close=document.createElement("button");close.type="button";close.textContent="關閉測試面板";
    close.style.cssText="background:#185b51;color:white;border:0;border-radius:7px;padding:7px 11px";
    close.addEventListener("click",()=>host.remove());host.appendChild(close);
    window.HO600_BROWSER_SMOKE_RESULT={passed,failed,total:messages.length,cases:messages.map(m=>({...m})),viewport:{w:innerWidth,h:innerHeight},userAgent:navigator.userAgent};
    const detail=document.createElement("details");
    detail.style.cssText="margin-top:8px;font-size:11px";
    const summary=document.createElement("summary");
    summary.textContent="展開可複製的驗收 JSON（含瀏覽器與視窗資訊）";
    detail.appendChild(summary);
    const output=document.createElement("textarea");
    output.readOnly=true;
    output.value=JSON.stringify(window.HO600_BROWSER_SMOKE_RESULT,null,2);
    output.style.cssText="display:block;width:100%;height:110px;max-width:100%;font-size:10px;margin-top:7px";
    output.addEventListener("focus",()=>output.select());
    detail.appendChild(output);
    host.appendChild(detail);
    console.info("HO600_BROWSER_SMOKE_RESULT",JSON.stringify(window.HO600_BROWSER_SMOKE_RESULT));
  }

  async function run() {
    for(let i=0;i<45&&!node(".kpi-grid");i++)await wait(100);
    try {
      assertion("首頁正常渲染",!!node(".kpi-grid")&&text().includes("181 / 600"));
      assertion("首頁正式 419 缺口",text().includes("419"));
      assertion("首頁沒有完整年齡通膨率",text().includes("0 / 7"));
      if (innerWidth <= 760) {
        await click("#menuToggle");
        assertion("手機選單可觸控開啟",node("#sidebar")?.classList.contains("open") && node("#menuToggle")?.getAttribute("aria-expanded")==="true");
        await click("#mobileBackdrop");
        assertion("點擊遮罩關閉手機選單",!node("#sidebar")?.classList.contains("open") && node("#menuToggle")?.getAttribute("aria-expanded")==="false");
      } else {
        assertion("行動選單遮罩元件已建立",!!node("#mobileBackdrop"));
      }

      await click('[data-tab="basket"]');
      assertion("價格籃分頁可切換",node("#pageTitle")?.textContent==="價格籃與研究配額");
      assertion("七個正式領域都有進度條",document.querySelectorAll("#app-content .bar-line").length>=7);
      assertion("研究 C04 不視為正式完成",text().includes("C04")&&text().includes("WIP"));

      await click('[data-tab="cohorts"]');
      assertion("臺北市 CPI 分頁可切換",node("#pageTitle")?.textContent==="戶長年齡與 CPI");
      assertion("保守排除 09 為預設",node('[data-mode="strict"]')?.getAttribute("aria-pressed")==="true");
      assertion("保守 65+ A 覆蓋率 2.54%",text().includes("2.54%"));
      assertion("保守 65+ A 部分貢獻 +0.0447 pp",text().includes("+0.0447 pp"));
      assertion("完整年齡率仍 HOLD",text().includes("HOLD")&&text().includes("0 / 7"));

      await click('[data-mode="provisional"]');
      assertion("暫定含 09 切換有效",node('[data-mode="provisional"]')?.getAttribute("aria-pressed")==="true");
      assertion("暫定 65+ A 為 7.57%、+1.9018 pp",text().includes("7.57%")&&text().includes("+1.9018 pp"));

      await click('[data-period="B"]');
      assertion("期間 B 可切換",node('[data-period="B"]')?.getAttribute("aria-pressed")==="true"&&text().includes("2020 全年 → 2025 全年"));
      assertion("暫定 65+ B 為 +1.7103 pp",text().includes("+1.7103 pp"));

      await change("#ageSelect","45～54歲");
      assertion("年齡組切換可用",node("#ageSelect")?.value==="45～54歲");
      assertion("暫定 45–54 B 為 +2.3734 pp",text().includes("+2.3734 pp"));

      await change("#statusSelect","SPLIT_REQUIRED");
      assertion("需拆分類別篩選為八筆",document.querySelectorAll("#app-content table tbody tr").length===8);

      await click('[data-period="A"]');
      await click('[data-mode="strict"]');
      await change("#ageSelect","65歲及以上");
      let exportedBlob=null,downloadPrevented=false,originalURL=URL.createObjectURL,
          originalClick=HTMLAnchorElement.prototype.click;
      try {
        URL.createObjectURL=function (blob) {exportedBlob=blob;return originalURL.call(URL,blob)};
        HTMLAnchorElement.prototype.click=function () {
          if(this.download?.startsWith("ho600_")){downloadPrevented=true;return;}
          return originalClick.call(this);
        };
        await click("#exportBtn");
      } finally {
        URL.createObjectURL=originalURL;
        HTMLAnchorElement.prototype.click=originalClick;
      }
      assertion("CSV 匯出按鈕實際運作且測試下載被攔截",downloadPrevented&&exportedBlob instanceof Blob);
      if(exportedBlob){
        const csv=await exportedBlob.text();
        assertion("匯出檔反映 A 與 strict 模式",csv.includes('"A"')&&csv.includes('"strict"'));
        assertion("匯出檔明確 HOLD 非完整通膨率",csv.includes("HOLD_NOT_A_FULL_RATE")&&!csv.includes("full_inflation_rate"));
        assertion("匯出檔包含七個年齡組",csv.trim().split(/\r?\n/).length===8);
      } else {
        assertion("CSV 內容可讀",false,"Blob not captured");
      }

      await click('[data-tab="evidence"]');
      assertion("證據分頁載入",node("#pageTitle")?.textContent==="證據與驗收");
      assertion("至少七筆來源與 SHA 追溯",document.querySelectorAll(".source-record").length>=7);
      assertion("GitHub Actions 標記暫停",text().includes("PAUSED"));
      assertion("正式指數依然 LOCKED",text().includes("LOCKED"));

      await click('[data-tab="tasks"]');
      assertion("Linear TODO 第五頁可切換",node("#pageTitle")?.textContent==="專案 TODO");
      assertion("42張快照預設僅顯示40張未結任務",document.querySelectorAll("#app-content table tbody tr").length===40);
      assertion("Linear狀態為39 Todo 1進行中 2已完成",text().includes("39")&&text().includes("2"));
      await change("#taskPriority","P0");
      assertion("P0 篩選只保留未完成任務",document.querySelectorAll("#app-content table tbody tr").length===5);
      await change("#taskStatus","ALL");
      assertion("P0 全部含結案共6張",document.querySelectorAll("#app-content table tbody tr").length===6);
      await change("#taskGroup","IUI Dashboard");
      assertion("IUI P0 共三張真機驗收任務",document.querySelectorAll("#app-content table tbody tr").length===3);
      assertion("依賴狀態可見",text().includes("未結前置"));
      await change("#taskStatus","OPEN");
      assertion("IUI P0 三張仍未完成",document.querySelectorAll("#app-content table tbody tr").length===3);

      const pageWidth=document.documentElement.scrollWidth;
      if(innerWidth<=500){
        assertion("手機寬度下無全頁橫向溢出",pageWidth<=innerWidth+2,"scrollWidth="+pageWidth+", innerWidth="+innerWidth);
      }else{
        assertion("瀏覽器 viewport 有效",innerWidth>500,"手機寬度請在 Safari 響應式模式另測");
      }
    } catch(error) {
      assertion("測試流程沒有未處理例外",false,String(error&&error.stack||error).slice(0,400));
    }
    display();
  }

  if(document.readyState==="loading")document.addEventListener("DOMContentLoaded",run,{once:true});
  else run();
})();
