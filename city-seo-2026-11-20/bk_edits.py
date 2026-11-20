import re,json,sys
def mk(city):
    C='Bristol' if city=='bristol' else 'Kingsport'
    ops=[]
    def RX(p,n): ops.append(['RX',p,n])
    # story section
    if city=='bristol':
        RX(r'<p class="bsx-p" style="line-height:1.6;color:#dedede">A homeowner out by the Speedway.*?</p>\s*<p class="bsx-p" style="line-height:1.6;color:#dedede">Engineering visibility.*?</p>\s*<p class="bsx-p" style="line-height:1.6;color:#dedede">And Bristol isn.*?</p>',
           '<p class="bsx-p" style="line-height:1.6;color:#dedede">A homeowner out by the Speedway searches <i>&ldquo;roofing company bristol tn.&rdquo;</i> Three blocks north of State Street, the same search ends in <i>&ldquo;va.&rdquo;</i> Same market, two result pages, and Google picks the map pack on each side. Your website and Google Business Profile need to speak to both Bristols while staying anchored where your business&nbsp;sits.</p>')
        RX(r'<p class="bsx-p" style="line-height:1.6;margin-top:18px;color:#cfcfcf">In a market this size.*?</p>','')
    else:
        RX(r'<p class="bsx-p" style="line-height:1.6;color:#dedede">Here.{1,8}s why that matters.*?</p>\s*<p class="bsx-p" style="line-height:1.6;color:#dedede">That.{1,8}s the whole difference.*?</p>\s*<p class="bsx-p" style="line-height:1.6;color:#dedede">And the demand is real.*?</p>',
           '<p class="bsx-p" style="line-height:1.6;color:#dedede">Rankings are built the same way: you map the demand, draw the plan and build to it, and the calls arrive the way traffic arrives on a well-laid street. Broad Street&rsquo;s downtown is drawing people back, and Sullivan and Hawkins counties send searches into Google every day. The open question is whose name comes up&nbsp;first.</p>')
        RX(r'<p class="bsx-p" style="line-height:1.6;margin-top:18px;color:#cfcfcf">In a market Kingsport.*?</p>','')
    # calculator
    RX(r'<p class="bsx-p bsx-lead" style="line-height:1.55">Four questions\. Your own numbers.*?</p>',
       '<p class="bsx-p bsx-lead" style="line-height:1.55">Four questions, using your own numbers. The top 3 results on Google get <b>68.7%</b> of the clicks (First Page Sage, 2025), so the distance between where you rank and the top 3 has a dollar&nbsp;value.</p>')
    RX(r'<p class="bsx-src" style="line-height:1.5;margin-top:12px">One more number worth knowing.*?</p>','')
    # why us
    RX(r'<div class="bsx-eyebrow" style="line-height:1.5">Why us .{1,12} why it.{1,8}s obvious</div>','<div class="bsx-eyebrow" style="line-height:1.5">How we work</div>')
    RX(r'Most SEO pages could be about any city\. You just read one that couldn.{1,8}t\.',f'This page is written for {C}, and so is the&nbsp;work.')
    if city=='bristol':
        dare='Search <b>&ldquo;SEO company Bristol TN&rdquo;</b> and count how many results could have any city&rsquo;s name pasted in. This page knows which side of State Street the Speedway sits on, and the work for your business is just as&nbsp;specific.'
    else:
        dare='Search <b>&ldquo;SEO company Kingsport TN&rdquo;</b> and count how many results could have any city&rsquo;s name pasted in. This page knows Kingsport was drawn from a master plan in 1917, and the work for your business is just as&nbsp;specific.'
    RX(r'(<div class="bsx-dk" style="line-height:1.4">Try it yourself</div>\s*<p style="line-height:1.6">).*?</p>',r'$1'+dare+'</p>')
    RX(r'(Founder-led, \d+ minutes away\.</h3><p class="bsx-p bsx-muted" style="line-height:1.6">).*?</p>',r'$1You work directly with Andrew, from an office in Johnson&nbsp;City.</p>')
    RX(r'(Measured in booked jobs, not rankings\.</h3><p class="bsx-p bsx-muted" style="line-height:1.6">).*?</p>',r'$1We trace calls, form fills and booked revenue to their source, so you know what your marketing costs per&nbsp;job.</p>')
    RX(r'One client per trade .{1,12} a policy you can test\.','One client per trade.')
    RX(r'(One client per trade\.</h3><p class="bsx-p bsx-muted" style="line-height:1.6">).*?</p>',r'$1If we already work with your trade in '+C+', we tell you on the first call and don&#39;t take the&nbsp;work.</p>')
    RX(r'(A system, not a bag of tactics\.</h3><p class="bsx-p bsx-muted" style="line-height:1.6">).*?</p>',r'$1Your site, Google Business Profile, reviews, citations, content and response speed work together, and the weakest one sets the pace. We find yours&nbsp;first.</p>')
    RX(r'<div class="bsx-grid2">','<div class="bsx-grid2" style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,420px),1fr))">')
    RX(r'<div class="bsx-chain" aria-label.*?<div class="bsx-chain-cap".*?</div>','')
    RX(r'(<div class="bsx-proof">.*?<p style="line-height:1.6;margin-top:10px">).*?</p>',r'$1A Tennessee contractor&rsquo;s average map-pack position, tracked in BrightLocal: <b>5.4 &rarr; 2.5</b>. Ask about it on the call and we&rsquo;ll walk you through what&nbsp;happened.</p>')
    RX(r'<p style="line-height:1.4">Most agencies can.{1,8}t tell you your cost per booked job.*?</p>','')
    RX(r'<div style="margin-top:24px"><a class="bsx-cta" href="#bsx-gap" style="line-height:1.3">Uncover My Revenue Gap →</a>\s*<div class="bsx-ctanote".*?</div></div>','')
    # four moves
    if city=='bristol':
        dab=r'<div class="bsx-dab" style="line-height:1.55">An SEO company in Bristol.*?</div>'
        intro='An SEO company in Bristol, TN gets your business into Google&rsquo;s top 3 results and the map pack for the services you sell, on both sides of the state line, then turns those searches into calls, booked estimates and revenue you can trace. Rankings are how it starts; booked work is how it&rsquo;s&nbsp;measured.'
    else:
        intro='An SEO company in Kingsport, TN gets your business into Google&rsquo;s top 3 results and the map pack for the services you sell, then turns those searches into calls, booked estimates and revenue you can trace. Rankings are how it starts; booked work is how it&rsquo;s&nbsp;measured.'
    RX(r'(<p class="bsx-p bsx-muted" style="line-height:1.6">)No 40-page audits.*?</p>',r'$1'+intro+'</p>')
    steps={'Build the foundation that converts':('Pages built for the searches that book work on both Bristol result pages, and a Google Business Profile with every category, service and photo filled&nbsp;in.' if city=='bristol' else 'Pages built for the searches that book work in Kingsport, and a Google Business Profile with every category, service and photo filled&nbsp;in.'),
      'Build authority Google can verify':('A steady flow of fresh reviews, consistent business listings across the web, and content that answers what Bristol customers ask on either side of State&nbsp;Street.' if city=='bristol' else 'A steady flow of fresh reviews, consistent business listings across the web, and content that answers what Kingsport customers ask before they&nbsp;call.'),
      'Count what matters, monthly':('Every call and form traced to its source and tied to booked work. The report answers one question: what did marketing cost per job this month, across both&nbsp;Bristols?' if city=='bristol' else 'Every call and form traced to its source and tied to booked work. The report answers one question: what did marketing cost per job this&nbsp;month?')}
    for k,v in steps.items():
        RX('('+re.escape(k).replace('\\ ',' ')+r'</b><p style="line-height:1.55">).*?</p>',r'$1'+v+'</p>')
    # FAQ
    RX(C+r' SEO questions, answered like a neighbor .{1,12} not a brochure',C+' SEO questions,&nbsp;answered')
    RX(r'<details open(?:="")?>','<details>')
    # close
    pclose='Find out which side of State Street you&rsquo;re invisible on in a 20-minute call with&nbsp;Andrew.' if city=='bristol' else 'Find out where you stand in a 20-minute call with&nbsp;Andrew.'
    RX(r'(<p class="bsx-p bsx-muted" style="line-height:1.6;max-width:56ch;margin:0 auto 8px;color:#cfcfcf">)Every month those spots.*?</p>',r'$1'+pclose+'</p>')
    RX(r'<p style="color:#e6e6e6;margin:0 auto 20px;font-size:14px;line-height:1.5">Before we take you on.*?</p>','<div style="height:12px"></div>')
    camp='seo-bristol-tn' if city=='bristol' else 'seo-kingsport-tn'
    RX(r'<a class="bsx-cta" href="#bsx-gap" style="background:var\(--bx-orange\);line-height:1.3">Uncover My Revenue Gap →</a>\s*<div class="bsx-ctanote" style="line-height:1.5">60 seconds · no form, no email, no sales call</div>\s*<p style="margin:14px auto 0;font-size:13.5px;line-height:1.5"><a href="https://calendly[^"]*"[^>]*>Already know your gap\?.*?</a></p>',
       f'<a class="bsx-cta" href="https://calendly.com/andrew-andrewryanmarketing/gap-review?utm_source=arm-site&amp;utm_medium=cta&amp;utm_campaign={camp}&amp;utm_content=cta-2" target="_blank" rel="noopener" style="background:var(--bx-orange);line-height:1.3">Book a 20-minute call →</a>\n    <p style="margin:14px auto 0;font-size:13.5px;line-height:1.5"><a href="#bsx-gap" style="color:#FF8A5C;font-weight:bold;text-decoration:underline">Or run the 60-second Revenue Gap check →</a></p>')
    RX(r'<span class="arml-t" style="line-height:1.4">Local SEO <span class="arml-r">·</span> Tri-Cities</span>','<span class="arml-t" style="line-height:1.4">SEO <span class="arml-r">·</span> Tri-Cities</span>')
    eb='SEO for contractors &middot; Bristol, TN &amp; VA' if city=='bristol' else 'SEO for contractors &middot; Kingsport, TN'
    pid='11771' if city=='bristol' else '11788'
    hero=open('hero.html').read().replace('SEO for contractors &middot; Johnson City, TN',eb).replace('SEO Company in Johnson City, TN',f'SEO Company in {C}, TN').replace('jc-seo-hero',f'{city}-seo-hero').replace('kw-hw-5398',f'kw-hw-{pid}')
    style=open('rf-hero-style.html').read().replace('5398',pid)
    return {'ops':ops,'hero':style+hero,'start':'<section class="bsx-hero"'}
for c in ['bristol','kingsport']:
    json.dump(mk(c),open(f'{c}-edits.json','w'))
