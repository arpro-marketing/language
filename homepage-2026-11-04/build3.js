const {chromium}=require('playwright');
const fs=require('fs');
async function build(p){
await p.goto('https://andrewryanmarketing.com/',{waitUntil:'domcontentloaded',timeout:60000});
for(let i=0;i<8;i++){const t=await p.title();if(!/One moment/.test(t))break;await p.waitForTimeout(4000);}
for(let t=0;t<4;t++){const ok=await p.waitForSelector('#wpb-content-root',{timeout:20000}).then(()=>1).catch(()=>0);if(ok)break;await p.waitForTimeout(5000);await p.goto('https://andrewryanmarketing.com/?r='+t,{waitUntil:'domcontentloaded',timeout:60000});}
await p.waitForTimeout(2500);
await p.evaluate(()=>{
 const root=document.querySelector('#wpb-content-root');
 const rows=[...root.children];
 const R=i=>rows[i];
 // ---- HERO
 const panel=document.querySelector('.rge-panel');
 const calc=document.querySelector('.armx-s.armx-calc');
 const h1=panel.querySelector('h1');
 const talk=panel.querySelector('.adc-hero-wrap');
 const eyebrow=panel.querySelector('.rge-eyebrow');
 const sub=panel.querySelector('p.sub');
 const lead=panel.querySelector('p.rge-lead');
 panel.innerHTML='';
 panel.style.cssText='max-width:780px;margin:0 auto;text-align:left;';
 h1.style.cssText='font-size:clamp(15px,1.5vw,18px)!important;line-height:1.35!important;letter-spacing:0!important;margin:0 0 26px!important;font-weight:700!important;color:#fff!important;';
 h1.innerHTML='<span style="color:#ef662f;text-transform:uppercase;letter-spacing:1.5px;font-size:.85em;display:block;margin-bottom:4px">Contractor Marketing Agency.</span>Get Chosen. Not just found.';
 panel.appendChild(h1);
 const q=document.createElement('div');
 q.innerHTML=`
 <p style="font-family:'Plus Jakarta Sans',sans-serif;font-weight:800;color:#fff;font-size:clamp(34px,4.6vw,58px);line-height:1.06;letter-spacing:-1.2px;margin:0 0 16px">Do you feel disconnected from your marketing?</p>
 <p style="font-family:'Plus Jakarta Sans',sans-serif;font-weight:700;color:#ef662f;font-size:clamp(22px,2.5vw,32px);line-height:1.2;letter-spacing:-.4px;margin:0 0 44px">Do you spend money and wonder if it's really working?</p>
 <div style="font-family:'DM Sans',sans-serif;color:#c9ccd3;font-size:clamp(17px,1.45vw,20px);line-height:1.6;max-width:760px">
 <p style="margin:0 0 22px;font-size:clamp(19px,1.7vw,24px);line-height:1.45"><b class="hx-lab" style="color:#fff;font-weight:800;font-size:1.2em;font-family:'Plus Jakarta Sans',sans-serif">The problem is:</b> your business and most agencies <b style="color:#fff;font-weight:700">don't share the same goals.</b></p>
 </div>
 <div class="hx-split">
  <p><span class="hx-k">The agency is focused on</span><b style="color:#fff">sending you leads.</b></p>
  <div class="hx-gap" aria-hidden="true"><svg viewBox="0 0 64 96" width="56" height="84"><path d="M6 2 C6 34 28 40 28 48 C28 56 6 62 6 94" fill="none" stroke="rgba(255,255,255,.28)" stroke-width="1.2"/><path d="M58 2 C58 34 36 40 36 48 C36 56 58 62 58 94" fill="none" stroke="rgba(255,255,255,.28)" stroke-width="1.2"/><line x1="28" y1="48" x2="36" y2="48" stroke="#ef662f" stroke-width="1.6"/></svg></div>
  <p><span class="hx-k">But you're focused on</span><b style="color:#ef662f;white-space:nowrap">booking jobs.</b></p>
 </div>
 <div style="font-family:'DM Sans',sans-serif;color:#c9ccd3;font-size:clamp(17px,1.45vw,20px);line-height:1.6;max-width:760px">
 <p style="margin:0 0 22px">That difference is what we call the gap — and it's the unspoken source of that disconnected feeling.</p>
 <p style="margin:0 0 34px;color:#fff;font-weight:700;font-size:clamp(19px,1.7vw,24px);line-height:1.45"><b class="hx-lab" style="color:#fff;font-weight:800;font-size:1.2em;font-family:'Plus Jakarta Sans',sans-serif">The solution:</b> work with an agency that shares your goals and focuses on booked jobs, rather than just leads.</p>
 </div>
 <a href="#start" style="display:inline-block;background:#ef662f;color:#fff;font-family:'Plus Jakarta Sans',sans-serif;font-weight:700;font-size:16px;padding:16px 28px;border-radius:8px;text-decoration:none;margin:0 0 18px">Get my gaps on video →</a>
 <style>
 .hx-split{display:grid;grid-template-columns:max-content auto max-content;justify-content:start;align-items:center;margin:6px 0 30px;max-width:820px;border-top:1px solid rgba(255,255,255,.14);border-bottom:1px solid rgba(255,255,255,.14)}
 .hx-split p{margin:0;padding:24px 0;font-family:'Plus Jakarta Sans',sans-serif;font-size:clamp(22px,2.2vw,30px);line-height:1.2;font-weight:800;letter-spacing:-.4px}
 .hx-split p:last-child{padding-left:0}
 .hx-gap{display:flex;flex-direction:column;align-items:center;padding:12px 40px;text-align:center}
 .hx-gap svg{display:block;margin-bottom:6px}
 .hx-gl{font-family:'Plus Jakarta Sans',sans-serif;font-size:11px;font-weight:700;letter-spacing:2px;text-transform:uppercase;color:#ef662f;white-space:nowrap}
 .hx-gs{font-family:'DM Sans',sans-serif;font-size:11px;color:#8b909a;white-space:nowrap;margin-top:2px}
 .hx-k{display:block;font-family:'DM Sans',sans-serif;font-size:15px;font-weight:500;letter-spacing:0;color:#9ca3af;margin-bottom:6px}
 @media(max-width:600px){.adc-hero-link{display:block!important;line-height:1.55}.adc-hero-link b,.adc-hero-link .a{display:inline!important}}
 @media(max-width:700px){.hx-split{grid-template-columns:1fr}.hx-split p{padding:16px 0}.hx-split p:last-child{padding-left:0}.hx-gap{flex-direction:row;flex-wrap:wrap;justify-content:center;padding:4px 0;gap:0 10px}.hx-gap svg{transform:rotate(90deg);width:28px;height:42px;margin:0}.hx-gs{margin:0}}
 </style>`;
 panel.appendChild(q);
 panel.appendChild(talk);
 calc.remove();
 const rge=document.getElementById('rge');const hr=rge.closest('.vc_row');if(hr){hr.style.setProperty('width','100%','important');hr.style.setProperty('left','0','important');hr.style.setProperty('margin-left','0','important');hr.style.setProperty('margin-right','0','important');}
 if(innerWidth<700) rge.style.setProperty('padding','56px 20px 44px','important'); else rge.style.setProperty('padding','96px 40px 80px','important');
 document.querySelector('.rge-in').style.cssText='display:block;max-width:1180px;margin:0 auto;padding:0;';panel.style.minWidth='0';

 const argW=document.querySelector('#argmRoot').parentElement;
 const sec=window.__SECTIONS;
 rows.forEach((r,i)=>{if(i>1)r.remove()});
 const wrap=document.createElement('div');wrap.innerHTML=sec;root.appendChild(wrap);
 const fold=document.createElement('div');fold.id='vr';fold.style.cssText='display:none;margin:8px 0 32px';fold.appendChild(argW);document.querySelector('#start .two').after(fold);
 const openFold=e=>{if(e)e.preventDefault();fold.style.display='block';const m=document.getElementById('argmModeSelf');if(m)m.click();setTimeout(()=>fold.scrollIntoView({behavior:'auto',block:'start'}),50);};
 window.__openFold=openFold;
 const cl=[...fold.querySelectorAll('a,button')].find(e=>/Close the map/.test(e.textContent));if(cl){cl.style.cssText='display:inline-block;background:none;border:0;color:#9ca3af;font:600 14px "DM Sans",sans-serif;cursor:pointer;padding:10px 0;margin-top:12px';cl.addEventListener('click',e=>{e.preventDefault();fold.style.display='none';document.querySelector('#start .two').scrollIntoView({block:'start'})});}
 document.querySelectorAll('#start a.btn[href="/6-gap-revenue-map/"], #rge a[href="#start"]').forEach(a=>{a.setAttribute('href','#vr');a.setAttribute('aria-controls','vr');a.addEventListener('click',openFold)});
 talk.querySelector('a').setAttribute('href','https://calendly.com/andrew-andrewryanmarketing/gap-review?utm_source=arm-site&utm_medium=cta&utm_campaign=site&utm_content=home-hero');
});
}
(async()=>{const b=await chromium.launch();
const VPS=(process.env.VPS||'1440:desktop:900|1024:t1024:768|768:t768:1024|390:phone:844|360:p360:780').split('|').map(g=>g.split(',').map(x=>{const [w,n,h]=x.split(':');return [+w,n,+h]}));
let first=true;
for(const grp of VPS){
 if(!first) await new Promise(r=>setTimeout(r,30000)); first=false;
 const p=await b.newPage({viewport:{width:grp[0][0],height:grp[0][2]},deviceScaleFactor:grp[0][0]>=700?1:2});
 await p.addInitScript({content:'window.__SECTIONS='+JSON.stringify(fs.readFileSync("mock3/sections.html","utf8"))});await build(p);
 for(const [w,n,vh] of grp){
 await p.setViewportSize({width:w,height:vh});await p.waitForTimeout(800);
 await p.evaluate(()=>{const rge=document.getElementById('rge');if(innerWidth<700){rge.style.setProperty('padding','56px 20px 44px','important');document.querySelector('.rge-in').style.padding='0';} else rge.style.setProperty('padding','96px 40px 80px','important');const h=document.querySelector('header,#brx-header');if(h)h.style.visibility='visible'});
 await p.evaluate(()=>{document.querySelectorAll('*').forEach(e=>{const cs=getComputedStyle(e);if(cs.position==='fixed'&&!e.closest('header')&&e.getBoundingClientRect().height<200)e.style.display='none'})});
 await p.evaluate(()=>{[...document.querySelectorAll('body *')].filter(e=>e.children.length===0&&/Message Andrew/.test(e.textContent)).forEach(e=>{let a=e;while(a&&a!==document.body){const ps=getComputedStyle(a).position;if(ps==='fixed'||ps==='sticky'){a.style.setProperty('display','none','important');break;}a=a.parentElement}})});
 await p.waitForTimeout(1500);await p.addStyleTag({content:'direct-line{display:none!important}'});await p.evaluate(()=>scrollTo(0,0));await p.waitForTimeout(1200);
 await p.screenshot({path:`mock3/home-mock-${n}-first-screen.png`});
 const qa=await p.evaluate(()=>{const W=innerWidth;const over=[...document.querySelectorAll('body *')].filter(e=>{const r=e.getBoundingClientRect();return r.width>0&&r.right>W+1&&getComputedStyle(e).position!=='fixed'}).slice(0,8).map(e=>e.tagName+'.'+String(e.className).slice(0,30)+' '+e.textContent.trim().slice(0,30));
 const nh=document.querySelector('.nh');const small=[...document.querySelectorAll('.nh *, #rge *')].filter(e=>e.children.length===0&&e.textContent.trim()&&parseFloat(getComputedStyle(e).fontSize)<14).map(e=>e.textContent.trim().slice(0,30)+':'+getComputedStyle(e).fontSize).slice(0,10);
 const taps=[...document.querySelectorAll('.nh a, #rge a')].filter(a=>{const r=a.getBoundingClientRect();return r.width&&r.height<24}).map(a=>a.textContent.trim().slice(0,25)+':'+Math.round(a.getBoundingClientRect().height)).slice(0,12);
 return {sw:document.documentElement.scrollWidth,W,over,small,taps}});
 qa.align=await p.evaluate(()=>({hero:Math.round(document.querySelector('#rge p').getBoundingClientRect().left),sec:Math.round(document.querySelector('.nh .in').getBoundingClientRect().left)}));
 fs.writeFileSync(`mock3/qa-${n}.json`,JSON.stringify(qa,null,1));
 const H=await p.evaluate(()=>document.documentElement.scrollHeight);
 const files=[];let k=0;
 for(let y=0;y<H;y+=vh){await p.evaluate(y=>scrollTo(0,y),y);await p.waitForTimeout(900);
   if(k===1){await p.evaluate(()=>{const h=document.querySelector('header,#brx-header');if(h)h.style.visibility='hidden'});await p.waitForTimeout(200);}
   const f=`mock3/frame-${n}-${String(k).padStart(2,'0')}.png`;await p.screenshot({path:f});files.push([f,Math.min(vh,H-y)]);k++;}
 fs.writeFileSync(`mock3/frames-${n}.json`,JSON.stringify(files));
 if(n==='desktop'||n==='phone'){await p.evaluate(()=>{const h=document.querySelector('header,#brx-header');if(h)h.style.visibility='visible';document.querySelector('#start a.btn').click()});await p.waitForTimeout(2500);
  const fy=await p.evaluate(()=>document.getElementById('vr').getBoundingClientRect().top+scrollY-(innerWidth<700?140:200));
  const fh=await p.evaluate(()=>document.getElementById('vr').getBoundingClientRect().height);
  const of=[];let j=0;for(let y=fy;y<fy+fh+260;y+=vh){await p.evaluate(y=>scrollTo(0,y),y);await p.waitForTimeout(900);const f=`mock3/open-${n}-${j}.png`;await p.screenshot({path:f});of.push(f);j++;if(j>5)break;}
  fs.writeFileSync(`mock3/open-${n}.json`,JSON.stringify(of));}
}
 await p.close();}
await b.close();})();
