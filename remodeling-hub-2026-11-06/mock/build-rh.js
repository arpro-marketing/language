const {chromium}=require('playwright');
const fs=require('fs');
const U='https://andrewryanmarketing.com/services/remodeling-contractor-marketing/';
const OUT=process.env.OUT||'remo/out';fs.mkdirSync(OUT,{recursive:true});
async function build(p){
 await p.goto(U,{waitUntil:'domcontentloaded',timeout:60000});
 for(let i=0;i<10;i++){const t=await p.title();if(!/One moment/.test(t))break;await p.waitForTimeout(5000);}
 for(let t=0;t<4;t++){const ok=await p.waitForSelector('#wpb-content-root',{timeout:20000}).then(()=>1).catch(()=>0);if(ok)break;await p.waitForTimeout(8000);await p.goto(U+'?r='+t,{waitUntil:'domcontentloaded',timeout:60000});}
 await p.waitForTimeout(2000);
 await p.evaluate(()=>{
  const root=document.querySelector('#wpb-content-root');
  [...root.children].forEach(c=>c.remove());
  const w=document.createElement('div');w.innerHTML=window.__SECTIONS;root.appendChild(w);
  // run inline scripts injected via innerHTML
  w.querySelectorAll('script:not([type="application/ld+json"])').forEach(s=>{const n=document.createElement('script');n.textContent=s.textContent;s.replaceWith(n)});
  const m=root.closest('main');if(m){m.style.padding='0';m.style.margin='0'}
  document.querySelectorAll('direct-line').forEach(e=>e.remove());
  setInterval(()=>{document.querySelectorAll('direct-line,[class*=direct-line],[id*=direct-line]').forEach(e=>e.remove());[...document.querySelectorAll('body *')].filter(e=>e.shadowRoot&&/Message Andrew/.test(e.shadowRoot.textContent||'')).forEach(e=>e.remove());[...document.querySelectorAll('body *')].filter(e=>e.children.length===0&&/Message Andrew/.test(e.textContent)).forEach(e=>{let a=e;while(a&&a!==document.body){const ps=getComputedStyle(a).position;if(ps==='fixed'||ps==='sticky'){a.style.setProperty('display','none','important');break;}a=a.parentElement}})},150);
 });
 await p.addStyleTag({content:'direct-line{display:none!important} #wpb-content-root{padding:0!important}'});
}
(async()=>{const b=await chromium.launch();
const VPS=(process.env.VPS||'1440:desktop:900|1024:t1024:768|768:t768:1024|390:phone:844|360:p360:780').split('|').map(x=>{const [w,n,h]=x.split(':');return [+w,n,+h]});
let first=true;
for(const [w,n,vh] of VPS){
 if(!first) await new Promise(r=>setTimeout(r,20000)); first=false;
 const p=await b.newPage({viewport:{width:w,height:vh},deviceScaleFactor:w>=700?1:2});
 let SEC=fs.readFileSync('remo/rh-sections.html','utf8');if(process.env.H1B)SEC=SEC.replace('<h1>Remodeling Contractor Marketing <span class="o">Measured to the Booked Project</span></h1>','<h1>A Remodeling Marketing Agency <span class="o">Measured to the Booked Project</span></h1>');await p.addInitScript({content:'window.__SECTIONS='+JSON.stringify(SEC)});
 let ok=false;for(let a=0;a<4;a++){try{await build(p);ok=true;break}catch(e){console.log('retry',a,String(e).slice(0,80));await new Promise(r=>setTimeout(r,120000));}} if(!ok){await p.close();continue;}
 await p.evaluate(()=>{document.querySelectorAll('*').forEach(e=>{const cs=getComputedStyle(e);if(cs.position==='fixed'&&!e.closest('header')&&e.getBoundingClientRect().height<200)e.style.display='none'})});
 await p.evaluate(()=>{[...document.querySelectorAll('body *')].filter(e=>e.children.length===0&&/Message Andrew/.test(e.textContent)).forEach(e=>{let a=e;while(a&&a!==document.body){const ps=getComputedStyle(a).position;if(ps==='fixed'||ps==='sticky'){a.style.setProperty('display','none','important');break;}a=a.parentElement}})});await p.waitForTimeout(1200);await p.evaluate(()=>scrollTo(0,0));await p.waitForTimeout(800);
 await p.screenshot({path:`${OUT}/rh-${n}-first-screen.png`});
 if(process.env.FIRST){await p.close();continue;}
 const qa=await p.evaluate(()=>{const W=innerWidth;
  const over=[...document.querySelectorAll('.rh *')].filter(e=>{const r=e.getBoundingClientRect();return r.width>0&&r.right>W+1}).slice(0,8).map(e=>e.tagName+'.'+String(e.className).slice(0,30)+' '+e.textContent.trim().slice(0,30));
  const small=[...document.querySelectorAll('.rh *')].filter(e=>e.children.length===0&&e.textContent.trim()&&parseFloat(getComputedStyle(e).fontSize)<13).map(e=>e.textContent.trim().slice(0,30)+':'+getComputedStyle(e).fontSize).slice(0,10);
  const taps=[...document.querySelectorAll('.rh a, .rh summary')].filter(a=>{const r=a.getBoundingClientRect();return r.width&&r.height<24}).map(a=>a.textContent.trim().slice(0,25)+':'+Math.round(a.getBoundingClientRect().height)).slice(0,12);
  const secs=[...document.querySelectorAll('.rh section')].map(s=>({id:s.id,bg:getComputedStyle(s).backgroundColor,h:Math.round(s.getBoundingClientRect().height)}));
  const adj=[];for(let i=1;i<secs.length;i++)if(secs[i].bg===secs[i-1].bg)adj.push(secs[i-1].id+'|'+secs[i].id);
  const txt=document.querySelector('.rh').innerText;const words=txt.split(/\s+/).filter(Boolean).length;
  const c=(re)=>(txt.match(re)||[]).length;
  const per=(x)=>Math.round(x/words*1000*10)/10;
  const hs=[...document.querySelectorAll('.rh h1,.rh h2,.rh h3')].map(h=>h.textContent.trim());
  const hRem=hs.filter(h=>/remodel/i.test(h)).length;
  const h2=[...document.querySelectorAll('.rh h2')].map(h=>h.textContent.trim());const h2Rem=h2.filter(h=>/remodel/i.test(h)).length;
  const links=[...document.querySelectorAll('.rh a[href]')].map(a=>a.getAttribute('href'));
  const hash=links.filter(h=>h==='#');
  return {sw:document.documentElement.scrollWidth,W,over,small,taps,adj,words,vocab:{remodel:per(c(/remodel/gi)),marketing:per(c(/marketing/gi)),lead:per(c(/\blead/gi)),inquir:per(c(/inquir/gi)),booked:per(c(/booked/gi))},headings:hs.length,hRem,h2:h2.length,h2Rem,links:links.length,hashLinks:hash.length,h1s:document.querySelectorAll('h1').length}});
 fs.writeFileSync(`${OUT}/qa-${n}.json`,JSON.stringify(qa,null,1));
 const H=await p.evaluate(()=>document.documentElement.scrollHeight);
 const files=[];let k=0;
 for(let y=0;y<H;y+=vh){await p.evaluate(y=>scrollTo(0,y),y);await p.waitForTimeout(500);await p.evaluate(()=>{[...document.querySelectorAll('body *')].filter(e=>e.children.length===0&&/Message Andrew/.test(e.textContent)).forEach(e=>{let a=e;while(a&&a!==document.body){const ps=getComputedStyle(a).position;if(ps==='fixed'||ps==='sticky'){a.style.setProperty('display','none','important');break;}a=a.parentElement}})});
   if(k===1){await p.evaluate(()=>{const h=document.querySelector('header,#brx-header');if(h)h.style.visibility='hidden'});await p.waitForTimeout(150);}
   const f=`${OUT}/frame-${n}-${String(k).padStart(2,'0')}.png`;await p.screenshot({path:f});files.push([f,Math.min(vh,H-y)]);k++;}
 fs.writeFileSync(`${OUT}/frames-${n}.json`,JSON.stringify(files));
 if(n==='desktop'||n==='phone'){await p.evaluate(()=>{document.getElementById('calc').open=true;document.querySelectorAll('.rh .faq details').forEach((d,i)=>{if(i<2)d.open=true});});await p.evaluate(()=>{const y=document.getElementById('calc').getBoundingClientRect().top+scrollY-120;scrollTo(0,y)});await p.waitForTimeout(900);await p.screenshot({path:`${OUT}/rh-${n}-calc-open.png`});
  await p.evaluate(()=>{const y=document.getElementById('faq').getBoundingClientRect().top+scrollY-80;scrollTo(0,y)});await p.waitForTimeout(900);await p.screenshot({path:`${OUT}/rh-${n}-faq-open.png`});}
 await p.close();}
await b.close();})();
