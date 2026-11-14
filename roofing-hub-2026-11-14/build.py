import re,json,html
b=open('body.part').read()
faq=re.findall(r'<details><summary>(.*?)</summary><div class="a">(.*?)</div></details>',b)
def clean(t): return html.unescape(re.sub('<[^>]+>','',t))
url="https://andrewryanmarketing.com/services/roofing-marketing/"
g={"@context":"https://schema.org","@graph":[{"@type":"Service","@id":url+"#service","name":"Roofing Contractor Marketing","serviceType":"Roofing marketing agency","url":url,"description":"Roofing contractor marketing measured to the signed roof: local SEO, Google Business Profile, Google Ads, Local Services Ads, Meta ads, retargeting, direct mail, exclusive lead generation, websites and reviews, plus speed to lead, inspection booking, confirmation and estimate follow-up for roofing companies, tracked from the call to the signed and installed roof.","provider":{"@type":"Organization","@id":"https://andrewryanmarketing.com/#organization","name":"Andrew Ryan Marketing","url":"https://andrewryanmarketing.com/","telephone":"(423) 299-1718"},"areaServed":{"@type":"Country","name":"US"},"audience":{"@type":"BusinessAudience","audienceType":"Roofing contractors, residential roofing companies and storm restoration roofers"}},{"@type":"FAQPage","mainEntity":[{"@type":"Question","name":clean(q),"acceptedAnswer":{"@type":"Answer","text":clean(a)}} for q,a in faq]}]}
ld='<script type="application/ld+json">'+json.dumps(g,ensure_ascii=False)+'</script>\n'
out='<div class="rf">\n'+open('css.part').read()+open('extra.part').read()+b+ld+open('js.part').read()+open('tl.part').read()+'</div>\n'
open('rf-sections.html','w').write(out)
open('roofing-hub-mockup.html','w').write(open('mockhead.part').read()+out)
print(len(faq),'faqs')
