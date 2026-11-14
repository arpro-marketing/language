import re,json,html
b=open('body.part').read()
faq=re.findall(r'<details><summary>(.*?)</summary><div class="a">(.*?)</div></details>',b)
def clean(t): return html.unescape(re.sub('<[^>]+>','',t))
url="https://andrewryanmarketing.com/services/fencing-company-marketing/"
g={"@context":"https://schema.org","@graph":[{"@type":"Service","@id":url+"#service","name":"Fence Company Marketing","serviceType":"Fence company marketing agency","url":url,"description":"Fence company marketing measured to the sold install: local SEO, Google Business Profile, Google Ads, Local Services Ads, Meta ads, retargeting, direct mail, exclusive lead generation, websites and reviews, plus speed to lead, quote booking, confirmation and quote follow-up for fence contractors, tracked from the inquiry to the sold and installed job.","provider":{"@type":"Organization","@id":"https://andrewryanmarketing.com/#organization","name":"Andrew Ryan Marketing","url":"https://andrewryanmarketing.com/","telephone":"(423) 299-1718"},"areaServed":{"@type":"Country","name":"US"},"audience":{"@type":"BusinessAudience","audienceType":"Fence companies, fence installers and commercial fence contractors"}},{"@type":"FAQPage","mainEntity":[{"@type":"Question","name":clean(q),"acceptedAnswer":{"@type":"Answer","text":clean(a)}} for q,a in faq]}]}
ld='<script type="application/ld+json">'+json.dumps(g,ensure_ascii=False)+'</script>\n'
out='<div class="fh">\n'+open('css.part').read()+open('extra.part').read()+b+ld+open('js.part').read()+open('tl.part').read()+'</div>\n'
open('fh-sections.html','w').write(out)
open('fence-hub-mockup.html','w').write(open('mockhead.part').read()+out)
print(len(faq),'faqs')
