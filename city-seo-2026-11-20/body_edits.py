import re
def R(old,new,count=1):
    global out
    n=out.count(old)
    assert n==count,(n,old[:80])
    out=out.replace(old,new)
def RX(pat,new):
    global out
    m=re.findall(pat,out,flags=re.S); assert len(m)==1,(len(m),pat[:80])
    out=re.sub(pat,(new if ('\\1' in new or '\\g<' in new) else (lambda _:new)),out,flags=re.S)

# --- 2. Junction: 4 paragraphs -> 2, board kept, board footer + bridge paragraph cut
RX(r'<p class="bsx-p" style="line-height:1.6;color:#dedede">A century later.*?the same three spots\.</p>',
 '<p class="bsx-p" style="line-height:1.6;color:#dedede">Customers still arrive through a junction. Today it runs through Google: the map pack, the top organic results, the AI answer and the reviews. Johnson City is the largest city in the Tri-Cities, with <b>74,943 people</b> (U.S. Census Bureau), so more searches meet here than anywhere else in the region, and more businesses compete for the same three&nbsp;spots.</p>')
RX(r'<div class="bsx-junc-foot".*?</div>\s*</div>\s*<p class="bsx-p" style="line-height:1.6;margin-top:18px;color:#cfcfcf">Every route.*?</p>','</div>')

# --- 3. Calculator: one-line intro, trailing 48% paragraph cut
RX(r'<p class="bsx-p bsx-lead" style="line-height:1.55">Four questions\. Your own numbers.*?worth to you\.</p>',
 '<p class="bsx-p bsx-lead" style="line-height:1.55">Four questions, using your own numbers. The top 3 results on Google get <b>68.7%</b> of the clicks (First Page Sage, 2025), so the distance between where you rank and the top 3 has a dollar&nbsp;value.</p>')
RX(r'<p class="bsx-src" style="line-height:1.5;margin-top:12px">One more number worth knowing.*?each one\.</p>','')

# --- 4. Proof: shorter intro + footer
R('Proof you can check — anonymized, specific, honestly labeled','Results you can check')
RX(r'(<p class="bsx-p bsx-lead" style="line-height:1.55;color:#e6e6e6">)Four real results.*?your outcome\.</p>',
 r'\g<0>'.replace(r'\g<0>','')+'<p class="bsx-p bsx-lead" style="line-height:1.55;color:#e6e6e6">Four clients in four different businesses, each labeled with what it measures and where the number comes&nbsp;from.</p>')
RX(r'<p class="bsx-pbfoot" style="line-height:1.6">.*?</p>','<p class="bsx-pbfoot" style="line-height:1.6">Ask on the call and we&rsquo;ll walk you through any of them, screen-shared.</p>')

# --- 5. Why us: one line per point; chain graphic, "most agencies" line and repeat button cut
R('Why us — and why you can check','How we work')
R('Every SEO company promises rankings. You&#39;re standing on our proof.','This is our home market, and this page competes in&nbsp;it.')
R('<div class="bsx-dk" style="line-height:1.4">You already ran the test</div>','<div class="bsx-dk" style="line-height:1.4">The same test you face</div>')
RX(r'<p style="line-height:1.6">There&#39;s a good chance you found this page.*?named after a depot\.</p>',
 '<p style="line-height:1.6">You may have found this page by searching <b>&ldquo;SEO company Johnson City.&rdquo;</b> It competes for that search against national agencies with Johnson City in a dropdown menu, the same way your business competes for&nbsp;yours.</p>')
RX(r'(Founder-led, from right here\.</h3><p class="bsx-p bsx-muted" style="line-height:1.6">).*?</p>',
 r'\1You work directly with Andrew, from an office in Johnson&nbsp;City.</p>')
RX(r'(Measured in booked jobs, not rankings\.</h3><p class="bsx-p bsx-muted" style="line-height:1.6">).*?</p>',
 r'\1We trace calls, form fills and booked revenue to their source, so you know what your marketing costs per&nbsp;job.</p>')
R('One client per trade — a policy you can test.','One client per trade.')
RX(r'(One client per trade\.</h3><p class="bsx-p bsx-muted" style="line-height:1.6">).*?</p>',
 r'\1If we already work with your trade in Johnson City, we tell you on the first call and don&#39;t take the&nbsp;work.</p>')
RX(r'(A system, not a bag of tactics\.</h3><p class="bsx-p bsx-muted" style="line-height:1.6">).*?</p>',
 r'\1Your site, Google Business Profile, reviews, citations, content and response speed work together, and the weakest one sets the pace. We find yours&nbsp;first.</p>')
RX(r'<div class="bsx-chain" aria-label.*?<div class="bsx-chain-cap".*?</div>','')
RX(r'<p style="line-height:1.4">Most agencies can&#39;t tell you your cost per booked job.*?</p>','')
RX(r'<div style="margin-top:24px"><a class="bsx-cta" href="#bsx-gap" style="line-height:1.3">Uncover My Revenue Gap →</a>\s*<div class="bsx-ctanote".*?</div></div>','')

# --- 6. Four moves: definition paragraph moved here from the hero; 1-2 sentences per step
RX(r'<p class="bsx-p bsx-muted" style="line-height:1.6">No 40-page audits.*?</p>',
 '<p class="bsx-p bsx-muted" style="line-height:1.6">An SEO company in Johnson City, TN gets your business into Google&#39;s top 3 results and the map pack for the services you sell, then turns those searches into calls, booked estimates and revenue you can trace. Rankings are how it starts; booked work is how it&#39;s&nbsp;measured.</p>')
steps={'Map the market — every route in':'Every search Johnson City customers use for your trade, who wins each one today, and where the openings are. You see the map before we touch&nbsp;anything.',
'Build the foundation that converts':'Pages built for the searches that book work, and a Google Business Profile with every category, service and photo filled&nbsp;in.',
'Build authority Google can verify':'A steady flow of fresh reviews, consistent business listings across the web, and content that answers what Johnson City customers&nbsp;ask.',
'Count what matters, monthly':'Every call and form traced to its source and tied to booked work. The report answers one question: what did marketing cost per job this&nbsp;month?'}
for k,v in steps.items():
    RX(r'('+re.escape(k)+r'</b><p style="line-height:1.55">).*?</p>', r'\g<1>'+v+'</p>')

# --- 7. FAQ: text unchanged (it feeds the FAQ schema); all closed; shorter heading
R('Johnson City SEO questions, answered like a neighbor — because we are one','Johnson City SEO questions,&nbsp;answered')
R('<details open="">\n        <summary style="line-height:1.45">How much does SEO cost in Johnson City, TN?','<details>\n        <summary style="line-height:1.45">How much does SEO cost in Johnson City, TN?')

# --- 8. Close: shorter heading + one line; duplicate conflict line cut; buttons match the hubs
R('The region&#39;s biggest market has the same three spots as everywhere else. Somebody holds them — it might as well be you.','Somebody holds the top three spots in Johnson City. It might as well be&nbsp;you.')
RX(r'(<p class="bsx-p bsx-muted" style="line-height:1.6;max-width:56ch;margin:0 auto 8px;color:#cfcfcf">)Every month those spots.*?call with Andrew\.</p>',
 r'\1Find out where you stand in a 20-minute call with&nbsp;Andrew.</p>')
RX(r'<p style="color:#e6e6e6;margin:0 auto 20px;font-size:14px;line-height:1.5">Before we take you on.*?</p>','<div style="height:12px"></div>')
RX(r'<a class="bsx-cta" href="#bsx-gap" style="background:var\(--bx-orange\);line-height:1.3">Uncover My Revenue Gap →</a>\s*<div class="bsx-ctanote" style="line-height:1.5">60 seconds · no form, no email, no sales call</div>\s*<p style="margin:14px auto 0;font-size:13.5px;line-height:1.5"><a href="(https://calendly[^"]*cta-2)"[^>]*>Already know your gap\?.*?</a></p>',
 '<a class="bsx-cta" href="https://calendly.com/andrew-andrewryanmarketing/gap-review?utm_source=arm-site&amp;utm_medium=cta&amp;utm_campaign=seo-johnson-city-tn&amp;utm_content=cta-2" target="_blank" rel="noopener" style="background:var(--bx-orange);line-height:1.3">Book a 20-minute call →</a>\n    <p style="margin:14px auto 0;font-size:13.5px;line-height:1.5"><a href="#bsx-gap" style="color:#FF8A5C;font-weight:bold;text-decoration:underline">Or run the 60-second Revenue Gap check →</a></p>')

# --- chip bar label: drop "Local"
R('<span class="arml-t" style="line-height:1.4">Local SEO <span class="arml-r">·</span> Tri-Cities</span>','<span class="arml-t" style="line-height:1.4">SEO <span class="arml-r">·</span> Tri-Cities</span>')
R('<div class="bsx-grid2">','<div class="bsx-grid2" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,420px),1fr))">')
