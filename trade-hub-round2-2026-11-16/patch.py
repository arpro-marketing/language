import re,sys
b=open('body-422fbf7.part').read()
def rep(old,new,s,cnt=1):
    assert s.count(old)==cnt,(old[:60],s.count(old)); return s.replace(old,new)
# ---- bring to live rev 13596 ----
b=rep('<p class="sub"><span class="ln">You win jobs at the kitchen table.</span> <span class="ln">Your marketing should be measured there too.</span></p>','<p class="sub"><span class="ln">A smarter way to grow your business.</span></p>',b)
b=rep('<p class="sol"><span>Recognized by local homeowners.</span><span>Trust that turns estimates into&nbsp;contracts.</span><span>Every step measured. Every job accounted&nbsp;for.</span></p>','<p class="sol"><span>We find what\'s working and fix what isn\'t.</span></p>',b)
old=re.search(r'<p class="dab">.*?</p>',b,re.S).group(0)
b=b.replace(old,'<p class="dab">Our window and door marketing services bring your business to homeowners and builders looking for new windows and doors. As a window and door marketing agency, we connect your first funnel&#8288;—creating demand&#8288;—with your second funnel&#8288;—turning that demand into sold jobs.</p>\n <p class="dab">Then, using your company\'s own data, we measure which marketing produces sold jobs, identify where opportunities are lost, and improve what delivers the greatest return.</p>')
def it(x,last=False): return '<span class="it">'+x+('' if last else '<span class="sep" aria-hidden="true"> · </span>')+'</span>'
def grp(rows): return '<ul class="sv-dlist sv-dgroups">'+''.join('<li>'+' '.join(it(x,i==len(r)-1) for i,x in enumerate(r))+'</li>' for r in rows)+'</ul>'
lists=re.findall(r'<ul class="sv-dlist">(.*?)</ul>',b)
items=[dict((re.sub('<[^>]+>','',li),li) for li in re.findall(r'<li>(.*?)</li>',l)) for l in lists]
f=items[0]; s=items[1]
b=b.replace('<ul class="sv-dlist">'+lists[0]+'</ul>',grp([[f['SEO'],f['Google Maps'],f['Reviews']],[f['Google Ads'],f['Local Services Ads'],f['Meta ads'],f['Retargeting']],[f['Websites'],f['Exclusive leads'],f['Direct mail']]]))
b=b.replace('<ul class="sv-dlist">'+lists[1]+'</ul>',grp([[s['Speed to lead'],s['Estimate booking']],[s['Appointment confirmation'],s['Kitchen-table close']],[s['Estimate follow-up'],s['CRM']]]))
b=rep('<p class="eb">Why trust us with your marketing</p>','<p class="eb">The experience behind the work</p>',b)
b=rep('<div class="stats','<p class="stat-src">Andrew\'s own dealership record · 27 months · not a client result</p>\n <div class="stats',b)
b=re.sub(r'(value="7348"></div>\n)(   </div>)',lambda m:m.group(1)+'    <p class="preset-src">Starting rates come from Andrew\'s own dealership record, not a client result. Replace them with your numbers.</p>\n'+m.group(2),b,count=1)
assert 'preset-src' in b,'calc line'
b=rep('Three ways to buy window and door marketing. Only one leaves you owning the engine.','Three ways to buy window and door marketing, and what each one counts as success.',b)
# section order + grounds
secs=re.findall(r'<section.*?</section>',b,re.S); ids=[re.search(r'id="(\w+)"',x).group(1) for x in secs]; d=dict(zip(ids,secs))
d['system']=d['system'].replace('class="soft" id="system"','class="light" id="system"',1)
d['services']=d['services'].replace('class="light" id="services"','class="soft" id="services"',1)
order=['top','system','math','leaks','services','proof','engagement','faq','start']
head=b[:b.find(secs[0])]; tail=b[b.rfind(secs[-1])+len(secs[-1]):]
mid=b[b.find(secs[0]):b.rfind(secs[-1])+len(secs[-1])]
for x in secs: mid=mid.replace(x,'@@'+re.search(r'id="(\w+)"',x).group(1)+'@@',1)
slots=re.findall(r'@@(\w+)@@',mid)
for slot,new in zip(slots,order): mid=mid.replace('@@'+slot+'@@','##'+new+'##',1)
for k in order: mid=mid.replace('##'+k+'##',d[k])
b=head+mid+tail
open('body-live.part','w').write(b)
# ---- round 2 ----
r=b
M=lambda x:'<span class="r2m" aria-hidden="true">R2</span>'
r=rep('<h2>Most agencies report the first step. The job is decided in the last three.</h2>\n <p class="lead">A homeowner replaces windows once every 15 to 40 years, compares several companies, and decides at the kitchen table. A marketing report that ends at the form fill sees none of that. We follow it to the signed install.</p>',
 '<h2 class="r2">Four steps decide every window and door job. We work on all four.</h2>\n <p class="lead r2">A homeowner replaces windows once every 15 to 40 years, compares several companies, and decides at the kitchen table. We follow each job through all four steps, from the first search to the signed install.</p>',r)
r=rep('<p class="lead">A marketing system with seven parts performs at the level of its weakest one. The <a href="/6-gap-revenue-map/">6-Gap Revenue Map™</a> shows which part is leaking most, and we start there, often on the inquiries you already have.</p>',
 '<p class="lead r2">A marketing system with seven parts performs at the level of its weakest one. We find the part that\'s leaking most and start there, often with the inquiries you already have.</p>',r)
t=re.search(r'\n <div class="terms">.*?\n </div>',r,re.S).group(0)
assert t.count('<div')==t.count('</div>'),'terms block unbalanced'
r=r.replace(t,'',1)
r=rep('</table>\n <div class="notyet">','</table>'+t.replace('<div class="terms">','<div class="terms r2t">',1)+'\n <div class="notyet">',r)
open('body-r2.part','w').write(r)
print('ok')
