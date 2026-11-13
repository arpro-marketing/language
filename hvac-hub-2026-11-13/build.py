import re,json,html
b=open('body.part').read()
faq=re.findall(r'<details><summary>(.*?)</summary><div class="a">(.*?)</div></details>',b)
def clean(t): return html.unescape(re.sub('<[^>]+>','',t))
url="https://andrewryanmarketing.com/services/hvac-marketing/"
g={"@context":"https://schema.org","@graph":[{"@type":"Service","@id":url+"#service","name":"HVAC Marketing","serviceType":"HVAC marketing agency","url":url,"description":"HVAC marketing measured to the sold job: SEO, Google Maps, Google Ads, Local Services Ads, Meta ads, retargeting, direct mail, websites and reviews, plus speed to call, visit booking, appointment confirmation and estimate follow-up for established heating and cooling companies, tracked from the call to the installed system and its gross profit.","provider":{"@type":"Organization","@id":"https://andrewryanmarketing.com/#organization","name":"Andrew Ryan Marketing","url":"https://andrewryanmarketing.com/","telephone":"(423) 299-1718"},"areaServed":{"@type":"Country","name":"US"},"audience":{"@type":"BusinessAudience","audienceType":"HVAC companies and heating and cooling contractors"}},{"@type":"FAQPage","mainEntity":[{"@type":"Question","name":clean(q),"acceptedAnswer":{"@type":"Answer","text":clean(a)}} for q,a in faq]}]}
ld='<script type="application/ld+json">'+json.dumps(g,ensure_ascii=False)+'</script>\n'
out='<div class="hv">\n'+open('css.part').read()+b+ld+open('js.part').read()+open('tl.part').read()+'</div>\n'
open('hv-sections.html','w').write(out)
head=open('mockhead.part').read()
open('hvac-hub-mockup.html','w').write(head+out)
