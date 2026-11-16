import re,json,html
import sys
b=open(sys.argv[1]).read()
suf=sys.argv[2]
faq=re.findall(r'<details><summary>(.*?)</summary><div class="a">(.*?)</div></details>',b)
def clean(t): return html.unescape(re.sub('<[^>]+>','',t))
url="https://andrewryanmarketing.com/services/window-and-door-marketing/"
g={"@context":"https://schema.org","@graph":[{"@type":"Service","@id":url+"#service","name":"Window and Door Contractor Marketing","serviceType":"Window and door marketing agency","url":url,"description":"Window and door contractor marketing measured to the signed install: local SEO, Google Business Profile, Google Ads, Local Services Ads, Meta ads, retargeting, direct mail, exclusive lead generation, websites and reviews, plus speed to lead, estimate booking, confirmation and estimate follow-up for replacement window and door companies, tracked from the inquiry to the signed and installed job.","provider":{"@type":"Organization","@id":"https://andrewryanmarketing.com/#organization","name":"Andrew Ryan Marketing","url":"https://andrewryanmarketing.com/","telephone":"(423) 299-1718"},"areaServed":{"@type":"Country","name":"US"},"audience":{"@type":"BusinessAudience","audienceType":"Window and door contractors, replacement window companies and door installers"}},{"@type":"FAQPage","mainEntity":[{"@type":"Question","name":clean(q),"acceptedAnswer":{"@type":"Answer","text":clean(a)}} for q,a in faq]}]}
ld='<script type="application/ld+json">'+json.dumps(g,ensure_ascii=False)+'</script>\n'
out='<div class="wd">\n'+open('css.part').read()+open('extra.part').read()+b+ld+open('js.part').read()+open('tl.part').read()+'</div>\n'
open('wd-sections-'+suf+'.html','w').write(out)
open('wd-mock-'+suf+'.html','w').write(open('mockhead.part').read()+out)
print(len(faq),'faqs')
