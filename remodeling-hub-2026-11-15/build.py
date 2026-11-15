import re,json,html
b=open('body.part').read()
faq=re.findall(r'<details><summary>(.*?)</summary><div class="a">(.*?)</div></details>',b)
def clean(t): return html.unescape(re.sub('<[^>]+>','',t))
url="https://andrewryanmarketing.com/services/remodeling-contractor-marketing/"
g={"@context":"https://schema.org","@graph":[{"@type":"Service","@id":url+"#service","name":"Remodeling Contractor Marketing","serviceType":"Remodeling marketing agency","url":url,"description":"Remodeling contractor marketing measured to the booked project: local SEO, Google Business Profile, Google Ads, Local Services Ads, Meta ads, retargeting, direct mail, exclusive lead generation, websites and reviews, plus speed to lead, consult booking, confirmation and proposal follow-up for remodeling companies, tracked from the first inquiry to the signed project.","provider":{"@type":"Organization","@id":"https://andrewryanmarketing.com/#organization","name":"Andrew Ryan Marketing","url":"https://andrewryanmarketing.com/","telephone":"(423) 299-1718"},"areaServed":{"@type":"Country","name":"US"},"audience":{"@type":"BusinessAudience","audienceType":"Remodeling contractors, design-build firms, kitchen and bath remodelers"}},{"@type":"FAQPage","mainEntity":[{"@type":"Question","name":clean(q),"acceptedAnswer":{"@type":"Answer","text":clean(a)}} for q,a in faq]}]}
ld='<script type="application/ld+json">'+json.dumps(g,ensure_ascii=False)+'</script>\n'
out='<div class="rm">\n'+open('css.part').read()+open('extra.part').read()+b+ld+open('js.part').read()+open('tl.part').read()+'</div>\n'
open('rm-sections.html','w').write(out)
open('remodeling-hub-mockup.html','w').write(open('mockhead.part').read()+out)
print(len(faq),'faqs')
