import re
b=open('body-a030af6.part').read()
def rep(o,n,s):
    assert s.count(o)==1,(o[:70],s.count(o)); return s.replace(o,n)
# ---- live rev 13573 equivalent ----
b=re.sub(r'<p class="sub">.*?</p>','<p class="sub"><span class="ln">A smarter way to grow your business.</span></p>',b,count=1,flags=re.S)
b=re.sub(r'<p class="sol">.*?</p>','<p class="sol"><span>We find what\'s working and fix what&nbsp;isn\'t.</span></p>',b,count=1,flags=re.S)
b=re.sub(r'<p class="dab">.*?</p>','<p class="dab">Our HVAC marketing services bring your business to homeowners and commercial buyers looking for a professional HVAC company. As an HVAC marketing agency, we connect your first funnel&#8288;—creating demand&#8288;—with your second funnel&#8288;—turning that demand into&nbsp;sold&nbsp;jobs.</p>\n <p class="dab">Then, using your company\'s own data, we measure which marketing produces sold jobs, identify where opportunities are lost, and improve what delivers the greatest return.</p>',b,count=1,flags=re.S)
b=rep('<div class="sv-dcard mkt">','<div class="sv-col"><p class="sv-fn">First funnel</p>\n   <div class="sv-dcard mkt">',b)
b=rep('<div class="sv-dcard team">','<div class="sv-col"><p class="sv-fn">Second funnel</p>\n   <div class="sv-dcard team">',b)
# close the sv-col wrappers after each card
def close_after(cls,s):
    i=s.find('<div class="sv-dcard '+cls+'">'); depth=0; j=i
    for m in re.finditer(r'<div\b|</div>',s[i:]):
        depth+=1 if m.group(0)=='<div' else -1
        if depth==0: j=i+m.end(); break
    return s[:j]+'</div>'+s[j:]
b=close_after('mkt',b); b=close_after('team',b)
b=rep('<p class="eb">Our track record</p>','<p class="eb">The experience behind the work</p>',b)
open('body-live.part','w').write(b)
# ---- round 1 ----
r=b
def it(x,last=False): return '<span class="it">'+x+('' if last else '<span class="sep" aria-hidden="true"> · </span>')+'</span>'
def grp(rows): return '<ul class="sv-dlist sv-dgroups r2">'+''.join('<li>'+' '.join(it(x,i==len(rw)-1) for i,x in enumerate(rw))+'</li>' for rw in rows)+'</ul>'
lists=re.findall(r'<ul class="sv-dlist">(.*?)</ul>',r)
items=[dict((re.sub('<[^>]+>','',li),li) for li in re.findall(r'<li>(.*?)</li>',l)) for l in lists]
f,s2=items; print(list(f),list(s2))
r=r.replace('<ul class="sv-dlist">'+lists[0]+'</ul>',grp([[f['SEO'],f['Google Maps'],f['AI Visibility']],[f['Google Ads'],f['Local Services Ads'],f['Meta ads'],f['Retargeting']],[f['Websites'],f['Direct mail']]]))
r=r.replace('<ul class="sv-dlist">'+lists[1]+'</ul>',grp([[s2['Speed to call'],s2['Visit booking']],[s2['Appointment confirmation'],s2['Estimate-to-sale']],[s2['Estimate follow-up'],s2['CRM']]]))
r=rep('<div class="stats','<p class="stat-src r2">Andrew\'s own dealership record · 27&nbsp;months · not a client result</p>\n <div class="stats',r)
r=rep('Three ways HVAC companies buy marketing. Only one leaves you owning the engine.','Three ways to buy HVAC marketing, and what each one counts as success.',r)
r=re.sub(r'(<caption)([^>]*>)Three ways',lambda m:m.group(1)+(' class="r2"' if 'class' not in m.group(2) else '')+m.group(2)+'Three ways',r,count=1)
secs=re.findall(r'<section.*?</section>',r,re.S); ids=[re.search(r'id="(\w+)"',x).group(1) for x in secs]; d=dict(zip(ids,secs))
d['system']=d['system'].replace('class="soft" id="system"','class="light" id="system"',1)
order=['top','system','math','worth','leaks','services','proof','engagement','faq','start']
mid=r[r.find(secs[0]):r.rfind(secs[-1])+len(secs[-1])]; head=r[:r.find(secs[0])]; tail=r[r.rfind(secs[-1])+len(secs[-1]):]
for x in secs: mid=mid.replace(x,'@@'+re.search(r'id="(\w+)"',x).group(1)+'@@',1)
slots=re.findall(r'@@(\w+)@@',mid)
for slot,new in zip(slots,order): mid=mid.replace('@@'+slot+'@@','##'+new+'##',1)
for k in order: mid=mid.replace('##'+k+'##',d[k])
r=head+mid+tail
# ---- round 2 ----
r=rep('<h2>Where HVAC companies lose growth</h2>','<h2 class="r2">From the first search to the finished install. We work across the entire process.</h2>',r)
r=rep('<p class="lead">Every HVAC job moves through four stages, and revenue can leak at any of them. Most HVAC marketing reports stop at the call. We follow it to the installed system.</p>','<p class="lead r2">Every HVAC job moves through four stages, and revenue can leak at any of them. We follow the job from the first search through the signed contract and installation.</p>',r)
r=rep("There's no fixed order: we start where the return is largest, often on the calls you already get.</p>","More marketing won't fix a bottleneck elsewhere in the business. We identify what's limiting growth and fix that first, often starting with the calls and estimates you already have.</p>",r)
r=r.replace('<p class="lead">As a full-service HVAC','<p class="lead r2">As a full-service HVAC',1)
t=re.search(r'\n <div class="terms">.*?\n </div>',r,re.S).group(0)
assert t.count('<div')==t.count('</div>')
r=r.replace(t,'',1)
r=rep('</table>\n <div class="price">','</table>'+t.replace('<div class="terms">','<div class="terms r2t">',1)+'\n <div class="price">',r)
r=rep('<p class="eb">Why generic marketing fails this trade</p>','<p class="eb r2">Where the job is won or lost</p>',r)
open('body-r2.part','w').write(r)
print('ok')
