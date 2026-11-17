import pathlib
H = pathlib.Path(__file__).parent
fonts = (H/'../../about/fonts.css').read_text()
ROWS = [
 ("“We’re not getting enough leads.”","Increase ad spend.","New leads wait hours for a callback. They’re booking with competitors.","Help your team respond in minutes before spending more."),
 ("“Our campaigns are performing well.”","Raise the budget.","Estimates go out, but too few become sold jobs.","Improve estimate follow‑up before buying more leads."),
 ("“Let’s push harder before the season.”","Buy more demand.","Your crews are already booked out for weeks.","Shift your budget toward higher‑value jobs until capacity opens&nbsp;up."),
]
CHECK = '<svg viewBox="0 0 20 20" width="18" height="18" aria-hidden="true"><circle cx="10" cy="10" r="10" fill="#EF662F"/><path d="M5.5 10.3l3 3 6-6.3" fill="none" stroke="#fff" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'

def current(i,r):
    a,b,c,d=r
    return f'<div class="c0"><div class="p"><div class="l">The report says</div><div class="q">{a}</div><div class="l">So you</div><div class="t">{b}</div><div class="l">What’s really happening</div><div class="b">{c}</div></div><div class="fx"><div class="l o">The fix</div><div class="t2">{d}</div></div></div>'

def opt1(i,r):  # numbered timeline inside card
    a,b,c,d=r
    return f'''<div class="c1"><div class="hd"><span class="n">0{i+1}</span><span class="hl">What the report says</span></div><div class="qq">{a}</div>
<ol class="tl"><li><span class="l">So you</span><span class="t">{b}</span></li><li class="re"><span class="l">What’s really happening</span><span class="b">{c}</span></li><li class="fx"><span class="l o">The fix</span><span class="t2">{d}</span></li></ol></div>'''

def opt2(i,r):  # three bands: assumption grey / reality white / fix tint
    a,b,c,d=r
    return f'''<div class="c2"><div class="ba"><div class="l">The report says</div><div class="q">{a}</div><div class="so"><span class="l">So you</span> <s>{b}</s></div></div>
<div class="bb"><div class="l">What’s really happening</div><div class="b">{c}</div></div>
<div class="bc">{CHECK}<div><div class="l o">The fix</div><div class="t2">{d}</div></div></div></div>'''

def opt3(i,r):  # dark quote header, then reality + fix
    a,b,c,d=r
    return f'''<div class="c3"><div class="dk"><div class="l lo">Report 0{i+1}</div><div class="q">{a}</div><div class="so">So you: {b}</div></div>
<div class="bd"><div class="row"><span class="tag">Reality</span><div class="b">{c}</div></div><div class="row fx"><span class="tag o">Fix</span><div class="t2">{d}</div></div></div></div>'''

CSS = r"""
*{box-sizing:border-box}body{margin:0;background:#F8F8F8;font-family:'DM Sans',sans-serif;color:#333}
.top{max-width:1640px;margin:0 auto;padding:28px 24px 8px}.top h1{font:800 26px 'Plus Jakarta Sans';margin:0 0 6px}.top p{color:#666;margin:0;font-size:15px;line-height:1.5;max-width:760px}
.cols{display:flex;gap:28px;flex-wrap:wrap;justify-content:center;padding:20px 16px 48px}
.ph{width:390px;max-width:100%}.ph h2{font:800 17px 'Plus Jakarta Sans';margin:0 0 4px}.ph .why{font-size:14px;color:#666;line-height:1.45;margin:0 0 12px;min-height:3em}
.fr{background:#fff;border:1px solid #E0E0E0;border-radius:22px;padding:16px;display:flex;flex-direction:column;gap:14px}
.l{font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#666}.o{color:#EF662F}
.q{font:600 19px/1.3 'Plus Jakarta Sans';color:#333;margin:4px 0 14px}.t,.t2{font-size:16px;line-height:1.45;color:#333}.b{font-weight:700;font-size:16px;line-height:1.45;color:#333}
[class^=c]{transition:transform .2s,box-shadow .2s,border-color .2s}
/* current */
.c0{border:1px solid #EF662F;border-radius:14px;overflow:hidden}.c0 .p{padding:18px}.c0 .p .l{margin-top:10px}.c0 .p .l:first-child{margin-top:0}.c0 .t{margin:4px 0 0;color:#666}.c0 .b{margin-top:4px}
.c0 .fx{border-top:3px solid #EF662F;background:#F8F8F8;padding:14px 18px}.c0 .t2{margin-top:4px}
/* opt1 timeline */
.c1{border:1px solid #E0E0E0;border-radius:16px;padding:18px;background:#fff;box-shadow:0 10px 24px -18px rgba(51,51,51,.45)}
.c1 .hd{display:flex;align-items:center;gap:10px}.c1 .n{font:800 13px 'Plus Jakarta Sans';color:#fff;background:#333;border-radius:8px;padding:4px 8px}.c1 .hl{font-size:11px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#666}
.c1 .qq{font:700 20px/1.3 'Plus Jakarta Sans';margin:12px 0 16px}
.c1 .tl{list-style:none;margin:0;padding:0 0 0 22px;position:relative}
.c1 .tl:before{content:"";position:absolute;left:6px;top:6px;bottom:22px;width:2px;background:#E0E0E0}
.c1 li{position:relative;padding-bottom:14px}.c1 li:last-child{padding-bottom:0}
.c1 li:before{content:"";position:absolute;left:-21px;top:4px;width:12px;height:12px;border-radius:50%;background:#fff;border:2px solid #666}
.c1 li.re:before{border-color:#333;background:#333}
.c1 li.fx{background:#FDF0EB;border-radius:10px;padding:12px 14px;margin-left:-8px}.c1 li.fx:before{left:-13px;top:16px;border-color:#EF662F;background:#EF662F}
.c1 li span{display:block}.c1 .l{margin-bottom:3px}.c1 .t{color:#666}
/* opt2 bands */
.c2{border:1px solid #E0E0E0;border-radius:16px;overflow:hidden;background:#fff;box-shadow:0 10px 24px -18px rgba(51,51,51,.45)}
.c2 .ba{background:#F8F8F8;padding:18px 18px 14px;border-bottom:1px solid #E0E0E0}.c2 .q{margin:4px 0 10px;color:#666}
.c2 .so{font-size:15px;color:#666}.c2 .so s{text-decoration-color:#EF662F;text-decoration-thickness:2px}
.c2 .bb{padding:16px 18px}.c2 .bb .b{margin-top:4px;font-size:17px}
.c2 .bc{display:flex;gap:12px;align-items:flex-start;background:#FDF0EB;border-top:2px solid #EF662F;padding:14px 18px}.c2 .bc svg{flex:none;margin-top:2px}.c2 .t2{margin-top:3px}
/* opt3 dark header */
.c3{border-radius:16px;overflow:hidden;background:#fff;border:1px solid #E0E0E0;box-shadow:0 10px 24px -18px rgba(51,51,51,.45)}
.c3 .dk{background:#14161C;color:#fff;padding:18px}.c3 .lo{color:#EF662F}.c3 .q{color:#fff;margin:6px 0 8px}.c3 .so{font-size:14px;color:rgba(255,255,255,.65)}
.c3 .bd{padding:6px 18px 18px}.c3 .row{display:grid;grid-template-columns:62px 1fr;gap:10px;align-items:start;padding:12px 0;border-bottom:1px solid #E0E0E0}.c3 .row:last-child{border-bottom:0;padding-bottom:0}
.c3 .tag{font-size:11px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:#666;border:1px solid #E0E0E0;border-radius:999px;padding:3px 0;text-align:center;margin-top:2px}
.c3 .tag.o{color:#fff;background:#EF662F;border-color:#EF662F}.c3 .fx .t2{color:#333;font-weight:600}
@media (hover:hover){.c1:hover,.c2:hover,.c3:hover{transform:translateY(-3px);border-color:#EF662F;box-shadow:0 12px 28px rgba(239,102,47,.14)}}
@media (prefers-reduced-motion:reduce){[class^=c]{transition:none}}
"""
cols = [
 ("Now (live)", "Orange outline, label stack, orange line before the fix.", current),
 ("Option 1: Numbered path", "The quote is the card’s title. A thin line walks from decision to reality to fix, and the fix lands in an orange-tinted box.", opt1),
 ("Option 2: Three bands", "Grey band for what the report says, white for what’s really happening, tinted band with a check for the fix. The wrong move is struck through.", opt2),
 ("Option 3: Dark header", "The report’s quote sits in a dark header like the hero. Below, two labeled rows: Reality and Fix.", opt3),
]
body = '<div class="top"><h1>Report-says cards on phones: three options</h1><p>Same copy in every option. Each column shows the three homepage cards at real phone width (390px). On desktop these cards stay as they are.</p></div><div class="cols">'
for t,w,f in cols:
    body += f'<div class="ph"><h2>{t}</h2><p class="why">{w}</p><div class="fr">' + ''.join(f(i,r) for i,r in enumerate(ROWS)) + '</div></div>'
body += '</div>'
(H/'gap-options.html').write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Report card options</title><style>{fonts}{CSS}</style></head><body>{body}</body></html>')
