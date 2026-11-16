import re
b=open('body-03ac1f5.part').read()
def rep(o,n,s):
    assert s.count(o)==1,(o[:70],s.count(o)); return s.replace(o,n)
# live state: heading live 11-16 rev 13595
b=rep('Three ways to buy roofing marketing. Only one leaves you owning the engine.','Three ways to buy roofing marketing, and what each one counts as success.',b)
open('body-live.part','w').write(b)
r=b
r=rep('<h2>Most agencies report the first step. The roof is decided in the last three.</h2>','<h2 class="r2">From the first search to the finished roof. We work across the entire process.</h2>',r)
r=rep(' A marketing report that ends at the phone call sees none of that. We follow it to the signed job.</p>',' We follow the job from the first search through the signed contract and installation.</p>',r)
r=r.replace('<p class="lead">A homeowner buys a roof rarely','<p class="lead r2">A homeowner buys a roof rarely',1)
r=rep('<p class="lead">A marketing system with seven parts performs at the level of its weakest one. The <a href="/6-gap-revenue-map/">6-Gap Revenue Map™</a> shows which part is leaking most, and we start there, often on the calls you already get.</p>',
 '<p class="lead r2">More marketing won\'t fix a bottleneck elsewhere in the business. We identify what\'s limiting growth and fix that first, often starting with the calls and estimates you already have.</p>',r)
r=rep('<label for="rfCr">Your close rate today</label>','<label for="rfCr" class="r2">Estimates that become signed jobs</label>',r)
t=re.search(r'\n <div class="terms">.*?\n </div>',r,re.S).group(0)
r=r.replace(t,'',1)
r=rep('</table>\n <div class="notyet">','</table>'+t.replace('<div class="terms">','<div class="terms r2t">',1)+'\n <div class="notyet">',r)
open('body-r2.part','w').write(r)
print('ok')
