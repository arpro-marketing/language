# HVAC spokes: final edit pass, 2026-11-18

STATUS: COMPLETE. Live on the four spokes and the hub since 2026-11-18, about 6:40 PM ET (Andrew, 6:27 PM ET: "yes ship it"). Part 6 items 6.5 to 6.9 and item 2.8 went live under the same approval on 2026-11-19, about 10:40 AM ET. See "As built" below.
This file is the single agreed wording for the pass. It replaces any earlier draft of these edits, and where it differs from the review document, this file wins.

## As built (2026-11-18)

Saved from this file as it stood at commit 9e2282c. Checked afterwards on the live pages, logged out, at 1440, 390 and 360 wide: all 54 element edits match NEW word for word, the new elements N-1 to N-5 are in place, and no element outside this file changed.

Versions, before (the rollback) and after:

| Page | Before | After |
|---|---|---|
| Google Ads & LSAs (13726) | 13759 | 13761 |
| AI Visibility (13720) | 13755 | 13763 |
| Call Handling (13733) | 13757 | 13764 |
| SEO (13745) | 13760 | 13765 |
| HVAC hub (6515) | 13754 | 13766 |

Where the build differs from the suggestions in this file. None of these change wording:
- N-1 closing note: `.cta-box.brxe-div p` was overriding `.cta-note` (the note rendered white at 17px), so the rule in use is `.cta-box .cta-note.cta-note` at 14px in the muted color, with a 13px size under 380px wide.
- N-3 Call Handling record label: wraps evenly on phones.
- 2.3 phone sub-nav: the scroll script is its own WPCode snippet (13762).
- 2.6 breadcrumb tap height: the padding rule made the breadcrumb row 12px taller and pushed the whole page down by that much. A correction sits directly after it in the four CSS snippets (13724, 13729, 13736, 13748): `.crumbs.brxe-div{margin-top:-6px;margin-bottom:16px}`. With it the H1 and the hero button sit where they did before the pass (H1 top 156 at 390 wide and 200 at 1440 wide on all four pages) and the links are 25px tall.

Saved on 2026-11-19, about 10:40 AM ET, under the same approval as the rest of the pass:

| Item | Page | Before | After |
|---|---|---|---|
| 6.5 | /services/ppc-for-contractors/ (5642) | 13705 | 13767, then 13773 for the link style |
| 6.6 | /local-services-ads-for-contractors/ | 13530 | 13768 |
| 6.7 | /local-contractor-seo-blueprint/ | 13696 | 13769 |
| 6.8 | /answer-gap-index/ (12925) | 13302 | 13771, then 13774 for the link style |
| 6.9 | /services/ | 13502 | 13770 |

- Item 2.8, llms.txt: a new `## HVAC Marketing` section after the fencing section holds the five lines below (hub and four spokes), and the old single HVAC line is gone from "Other Contractor Industries". No other line changed.
- Link style, about 11:03 AM ET: the new "HVAC" links on /services/ppc-for-contractors/ and /answer-gap-index/ rendered like the plain text around them. The first now carries `class="tx"` like that page's other in-text links (orange, bold). The second carries `style="border-bottom:1px solid #EF662F"` like that page's "see Method" link, set inline because the page's Bricks CSS file is not rebuilt by an API save. The blueprint's new link was left as it is, because it matches the unstyled in-text links around it.
- Checked from the cloud, logged out with a fresh copy forced: 18 of 18 text and link checks; each of the five pages in a browser at 1440, 390 and 360 wide with no errors, no sideways scroll and every new link clickable; nothing else on the five pages changed against the copies of the night before (only the page-modified date in the structured data); the two restyled links re-read in a browser at 1440 and 390.
- Rollback for these six saves is in `final-pass\ROLLBACK.txt` on the PC.

Known after the save, to be proposed on its own: on a 390 by 664 phone screen the "Message Andrew" bar covers the note under the hero button at first view on Google Ads, Call Handling and SEO. Screens of 390 by 745 and taller, and desktop, are clear.

Rich Results Test after the save (smartphone): 3 valid items, 0 errors and 0 warnings on each of the four spokes.

## Scope

Source: the review and fix list of 2026-11-18 (Parts 1 to 9), the outside (GPT) read of it, and Andrew's answers of 2026-11-18 (5:32, 5:59 and 6:04 PM ET).

Updated 2026-11-18 6:30 PM ET, after Andrew read the three new pieces of wording:
- AI step 02 lists wording (AI-19): he agreed.
- Call Handling paragraph (CAL-2): stays exactly as written here. He asked what a comfort advisor is, then said to keep the term. Do not replace it and do not add an explanation of it.
- Google Ads example (PPC-6): he asked for a graph beside it. The graph is N-5 below, and its mockup was sent to him at 6:19 PM ET. PPC-6 loses its last sentence because the graph's label carries it. If Andrew says to keep that sentence, put it back at the end of PPC-6 and shorten the graph's label to `Illustrative example`.

IN this pass:
- Part 1, items 1.1 to 1.16 (facts and wording). Item 1.11 is redone: the ad example now counts repairs and replacements for both accounts at one gross margin.
- Part 2, items 2.1 to 2.6 and 2.8 (display bugs, llms.txt). No copy changes.
- Part 4, items 4.1 to 4.9 (ideas picked up from the simulated reads; each also rests on the hub's own wording, a rule of Andrew's or a source).
- Part 5, only what Andrew answered or approved: who makes the follow-up calls (5.3, Call Handling), how a company gets onto the lists AI cites (5.4, AI page), and the two extras in 5.6 (one company per market on all four closes, the founder-led line on Google Ads).
- The graph under the Google Ads example (N-5), which Andrew asked for on 2026-11-18 at 5:59 PM ET.
- Part 6, items 6.1 to 6.9 (links).

NOT in this pass. Do not change these:
- 5.1 SEO hero question. It stays: "When someone near you searches “AC repair near me,” is your company in the three names Google shows?"
- 5.2 SEO timeline FAQ. It stays as it is, and the SEO schema snippet (13747) is not touched.
- 5.3 the two unconfirmed process lines (SEO step 01 profile check, AI step 02 "never scripted or paid for").
- 5.5 the example sold-jobs report. It comes as its own preview and its own yes.
- 5.6 the third extra (a booking link at the end of the AI findings).
- 2.7 share images. Part 9 (other pages).
- Page structure, section order, headings, hero questions, button labels (except the AI hero button in 1.16) and every line listed under "Lines to protect" at the end of this file.

Each element below is given in full. Replace the element's whole text with NEW. NOW is the live text on 2026-11-18 22:35Z (logged-out fetch), so if an element doesn't match NOW exactly, stop and report instead of editing.

## Word count

| Page | Words now | Change | After |
|---|---|---|---|
| AI Visibility | 1,530 | +32 | 1,562 |
| Google Ads & LSAs | 1,372 | +47 | 1,419 |
| Call Handling | 1,015 | +63 | 1,078 |
| SEO | 1,022 | +86 | 1,108 |

## Google Ads & LSAs page (13726) /services/hvac-marketing/ppc/

### PPC-1. Element #brxe-k91qel (items 4.7, 4.4)
NOW:
```html
PPC for an HVAC company usually means two Google products. Local Services Ads sit at the very top of the page with the Google Verified badge, and you pay for each lead. Search ads sit just below them, and you pay for each click. Both are part of our <a href="/services/hvac-marketing/">HVAC contractor marketing</a>, and we measure both the same way: by the jobs they sell and the gross profit those jobs leave, not by the number of calls.
```
NEW:
```html
PPC for an HVAC company usually means two Google products: Local Services Ads, where you pay for each lead, and search ads, where you pay for each click. Both are part of our <a href="/services/hvac-marketing/">HVAC contractor marketing</a>, and we measure both the same way: <strong>by the jobs they sell and the gross profit those jobs leave, not by the number of calls</strong>.
```

### PPC-2. Element #brxe-zeh430 (items 1.16, 4.2, 4.7)
NOW:
```html
Paid search is the fastest channel an HVAC company has. A well-built campaign can ring the phone in its first week. It’s also the easiest to waste, because Google will happily spend a budget on whatever converts cheapest unless the account is told what a good call is actually worth.
```
NEW:
```html
Paid search is the fastest channel you have. A well-built campaign can ring the phone in its first week, which makes search ads the first channel to open in a new service area.
```

### PPC-3. Element #brxe-wxu2a2 (items 1.10, 4.4)
NOW:
```html
Around $350 a visit (Angi)
```
NEW:
```html
Around <strong>$350</strong> a visit (Angi, 2026)
```

### PPC-4. Element #brxe-g3ahmk (items 4.4)
NOW:
```html
Around $7,500 a system (Angi, 2026)
```
NEW:
```html
Around <strong>$7,500</strong> a system (Angi, 2026)
```

### PPC-5. Element #brxe-5605cp (items 1.5, 4.7)
NOW:
```html
Fewer searches and costlier clicks, and a longer path through a comfort visit and an estimate. At a 40% gross margin, one sale leaves about $3,000 in gross profit to cover what the ads cost.
```
NEW:
```html
Fewer searches, a higher cost per lead, and a longer path through a comfort visit and an estimate.
```

### PPC-6. Element #brxe-1wf1r9 (items 1.11 (redone), 4.7, graph N-5)
NOW:
```html
Here is why this matters. Say one account produces 100 leads a month at $50 each, mostly repairs, and sells two replacements. Another produces 60 leads at $80 each, aimed at replacement searches, and sells five. The first looks cheaper per lead. At $7,500 a system, the second brings in about $22,500 more in replacement revenue on almost the same spend, or about $9,000 more in gross profit at a 40% margin. That’s an illustration of the math, not a client result.
```
NEW:
```html
Say one account produces 100 leads a month at $50 each, mostly repair calls, and they turn into 60 repair visits and two replacements. Another produces 60 leads at $80 each, aimed at replacement searches, and they turn into 20 repair visits and five replacements. The first looks cheaper per lead. At $350 a repair, $7,500 a system and a 40% gross margin on both, the first leaves about $14,400 in gross profit and the second about $17,800, on almost the same spend.
```

### PPC-7. Element #brxe-adf3c4 (items 4.7)
NOW:
```html
The very top of the results, with the badge and your reviews
```
NEW:
```html
The very top of the results, with the Google Verified badge and your reviews
```

### PPC-8. Element #brxe-ndmz7y (items 1.10)
NOW:
```html
One change to know about: Google is moving Local Services Ads into Google Ads, and its timeline puts HVAC in the first phase, which began in August 2026. After the move, your LSAs appear there as a Performance Max campaign with a pay-per-lead goal. That isn’t the standard Performance Max in the table above. It still runs only on Search and Maps, and you still pay per lead.
```
NEW:
```html
One change to know about: <a href="https://support.google.com/google-ads/answer/17213585">Google is moving Local Services Ads into Google Ads</a>, and its timeline puts HVAC in the first phase, which began in August 2026. After the move, your LSAs appear there as a Performance Max campaign with a pay-per-lead goal. That isn’t the standard Performance Max in the table above. It still runs only on Search and Maps, and you still pay per lead.
```

### PPC-9. Element #brxe-gzmxdu (items 6.3)
NOW:
```html
Local Services Ads lean heavily on your review count, your rating and how fast you answer, so they reward the same work as your <a href="/services/reputation-management-for-contractors/">reviews</a> and your <a href="/services/lead-to-booked-job/">call handling</a>.
```
NEW:
```html
Local Services Ads lean heavily on your review count, your rating and how fast you answer, so they reward the same work as your <a href="/services/reputation-management-for-contractors/">reviews</a> and your <a href="/services/hvac-marketing/call-handling/">call handling</a>.
```

### PPC-10. Element #brxe-3yi8q7 (items 1.7, 1.9)
NOW:
```html
<strong>We send sold-job revenue back to Google.</strong> When your field software records the sale, that revenue goes back to the ad click that started it. ServiceTitan can do this with its Google Ads revenue import, and other systems can do it through offline conversion uploads. Google then learns which searches end in a $7,500 replacement instead of a $99 tune-up. Very few contractors have this in place: a scan of 1,000 contractor websites reported by Contracting Business in August 2026 found a Google Ads conversion tag on only 14% of them.
```
NEW:
```html
<strong>We send sold-job revenue back to Google.</strong> When your field software records the sale, that revenue goes back to the ad click that started it. ServiceTitan does it through Ads Optimizer, part of its Marketing Pro package with Ads, and other systems can do it through offline conversion uploads. Google then learns which searches end in a $7,500 replacement instead of a $99 tune-up. Most contractors aren’t close to this: a scan of 1,000 contractor websites reported by Contracting Business in August 2026 found even a basic Google Ads conversion tag on only 14% of them.
```

### PPC-11. Element #brxe-cdgfef (items 5.6)
NOW:
```html
You own the ad account, and we don’t mark up your ad spend. Our full approach to paid search for contractors is on our <a href="/services/ppc-for-contractors/">PPC for contractors</a> page.
```
NEW:
```html
You own the ad account, and we don’t mark up your ad spend. Andrew runs the strategy and the weekly decisions on every account himself. Our full approach to paid search for contractors is on our <a href="/services/ppc-for-contractors/">PPC for contractors</a> page.
```

### PPC-12. Element #brxe-cvcyee (items 1.6 (schema))
NOW:
```html
It depends on your market, your season and which calls you go after. Clicks for replacement searches cost more than repair clicks, and big metros cost more in July than smaller towns do in April. The number that matters is your cost per sold job by call type, because a cheap lead that never sells is the most expensive one you buy.
```
NEW:
```html
What you pay Google depends on your market, your season and which calls you go after. What you pay us is a flat fee by tier, never a percentage of your ad spend, and the tiers are on our <a href="/pricing/">pricing page</a>. The number that matters is your cost per sold job by call type, because a cheap lead that never sells is the most expensive one you buy.
```

### PPC-13. Element #brxe-6klc77 (items 1.8 (schema))
NOW:
```html
Yes. ServiceTitan has a built-in Google Ads revenue import that ties completed-job revenue to the original ad click, and other field software can send the same information through offline conversion uploads. Once that data is flowing, Google can bid toward sold jobs and their value instead of raw lead counts.
```
NEW:
```html
Yes. ServiceTitan does it through Ads Optimizer, part of its Marketing Pro package with Ads, which ties completed-job revenue to the original ad click, and other field software can send the same information through offline conversion uploads. Once that data is flowing, Google can bid toward sold jobs and their value instead of raw lead counts.
```

### PPC-14. Element #brxe-lnoftc (items 5.6, 4.1)
NOW:
```html
In a free 20-minute Gap Review, we go through your ad account with you on a shared screen: the search terms you’re paying for, the pages they land on and where the spend is most likely leaking. Bring last month’s calls and sold jobs if you have them, and we’ll work out your cost per sold job by call type.
```
NEW:
```html
In a free 20-minute Gap Review, we go through your ad account with you on a shared screen: the search terms you’re paying for, the pages they land on and where the spend is most likely leaking. Bring last month’s calls and sold jobs if you have them, and we’ll work out your cost per sold job by call type. One HVAC company per market. Tiers and exit terms are on our <a href="/pricing/">pricing page</a>.
```

### New text on this page
- 4.1 note under the hero button: `Free · 20 minutes · a call with Andrew`
- 4.1 note under the closing button: `Free · 20 minutes · a call with Andrew`
- N-5 graph: label: `Illustrative example, not a client result`
- N-5 graph: title: `Gross profit from about $5,000 in ad spend`
- N-5 graph: first bar, name: `$50 per lead`
- N-5 graph: first bar, detail: `100 leads: 2 replacements, 60 repairs`
- N-5 graph: first bar, value: `$14,400`
- N-5 graph: second bar, name: `$80 per lead`
- N-5 graph: second bar, detail: `60 leads: 5 replacements, 20 repairs`
- N-5 graph: second bar, value: `$17,800`
- N-5 graph: key: `Replacements`
- N-5 graph: key: `Repairs`

## AI Visibility page (13720) /services/hvac-marketing/ai-visibility/

### AI-1. Element #brxe-h4hprz (items 1.12)
NOW:
```html
More homeowners now ask ChatGPT, Perplexity or Google’s AI Mode who to call before they ever scroll the map. We’ve asked that question hundreds of times a month since September, and the HVAC answers don’t follow Google’s rankings the way most owners expect.
```
NEW:
```html
More homeowners now ask ChatGPT, Perplexity or Google’s AI Mode who to call before they ever scroll the map. We’ve asked that question 60 times a month since September, and the answers don’t follow Google’s rankings the way most owners expect.
```

### AI-2. Element #brxe-sey07n (items 1.16)
NOW:
```html
See the HVAC findings
```
NEW:
```html
See the findings
```

### AI-3. Element #brxe-rucffo (items 4.9, 4.4)
NOW:
```html
AI visibility is whether your company gets named when a homeowner asks an AI assistant for a recommendation, and what the assistant says about you when it does. It’s one part of our <a href="/services/hvac-marketing/">HVAC marketing agency</a> work, and we judge it the same way as everything else we run: by whether it ends in sold jobs, not by how often your name appears.
```
NEW:
```html
AI visibility is whether your company gets named when a homeowner asks an AI assistant for a recommendation, and what the assistant says about you when it does. It’s one part of our work as an <a href="/services/hvac-marketing/">HVAC marketing agency</a>, and we judge it the same way as everything else we run: <strong>by whether it ends in sold jobs, not by how often your name appears</strong>.
```

### AI-4. Element #brxe-zwxnkr (items 4.7)
NOW:
```html
It overlaps with local SEO, but it isn’t the same thing. Google’s map pack ranks companies by distance, relevance and prominence. ChatGPT, Perplexity and Google’s AI answers read your reviews, the lists and articles that mention you, and your own website, and then write a short answer. In our research they often land on different companies than the map does.
```
NEW:
```html
It overlaps with local SEO, but it isn’t the same thing. ChatGPT, Perplexity and Google’s AI answers read your reviews, the lists and articles that mention you, and your own website, and then write a short answer. In our research they often land on different companies than the map does.
```

### AI-5. Element #brxe-vsuea5 (items 4.5)
NOW:
```html
Usually Google’s
```
NEW:
```html
8 in 10
```

### AI-6. Element #brxe-ua60kk (items 4.5)
NOW:
```html
The company AI named first was usually one Google already showed. The rest of the list is where AI reached past Google.
```
NEW:
```html
of AI’s first picks were companies Google already showed. The rest of the list is where AI reached past Google.
```

### AI-7. Element #brxe-m9l90p (items 4.5)
NOW:
```html
Not in Google’s results: 7 of 55 first picks in September · 11 of 46 in October
```
NEW:
```html
48 of 55 first picks in September · 35 of 46 in October
```

### AI-8. Element #brxe-r2kiw4 (items 4.5)
NOW:
```html
Local names
```
NEW:
```html
19 in 20
```

### AI-9. Element #brxe-6bdk7c (items 4.5)
NOW:
```html
Almost every HVAC company AI named was a locally branded company. National franchise names were a small fraction of the mentions.
```
NEW:
```html
of the mentions went to locally branded companies. National franchise names were a small fraction.
```

### AI-10. Element #brxe-81w77a (items 4.5)
NOW:
```html
7 of 205 HVAC mentions in October · 13 of 267 in September
```
NEW:
```html
198 of 205 HVAC mentions in October · 254 of 267 in September
```

### AI-11. Element #brxe-k3sm6n (items 4.7)
NOW:
```html
ChatGPT started citing HVAC companies’ own websites. In September it cited none of them; in October it did for 11 of its picks.
```
NEW:
```html
ChatGPT started citing HVAC companies’ own websites.
```

### AI-12. Element #brxe-wlnxpw (items 4.4)
NOW:
```html
Reaches farther. The companies AI named that Google didn’t sat a median 6.8 miles from the search point, against 1.7 miles.
```
NEW:
```html
Reaches farther. The companies AI named that Google didn’t sat a median <strong>6.8 miles</strong> from the search point, against 1.7 miles.
```

### AI-13. Element #brxe-4a1iqj (items 4.4)
NOW:
```html
Among companies Google already showed, the ones AI named had more reviews (median 106 against 64) and more recent ones. Star rating made no difference.
```
NEW:
```html
Among companies Google already showed, the ones AI named had more reviews (median <strong>106 against 64</strong>) and more recent ones. Star rating made no difference.
```

### AI-14. Element #brxe-s1ok5p (items 4.4)
NOW:
```html
Named companies had more websites linking to them, and 39% of the sites ChatGPT cited were “best of” and ranking lists.
```
NEW:
```html
Named companies had more websites linking to them, and <strong>39%</strong> of the sites ChatGPT cited were “best of” and ranking lists.
```

### AI-15. Element #brxe-mqb7hn (items 4.4)
NOW:
```html
ChatGPT cited the business’s own site for 27% of its picks in October, up from 7% in September.
```
NEW:
```html
ChatGPT cited the business’s own site for <strong>27%</strong> of its picks in October, up from 7% in September.
```

### AI-16. Element #brxe-o7jpih (items 4.4)
NOW:
```html
The same engine often repeats its first pick, but ChatGPT, Perplexity and AI Mode agreed on the first business only 3.6% of the time.
```
NEW:
```html
The same engine often repeats its first pick, but ChatGPT, Perplexity and AI Mode agreed on the first business only <strong>3.6%</strong> of the time.
```

### AI-17. Element #brxe-r32qqu (items 4.6)
NOW:
```html
A homeowner whose air conditioning quits in July isn’t looking for a list of twenty contractors. When they ask an AI assistant, they get three to five names and a sentence about each. If your company is one of them, you’re in a very short conversation. If it isn’t, that homeowner never calls.
```
NEW:
```html
In BrightLocal’s 2026 survey, 45% of consumers said they use AI tools for local business recommendations, up from 6% a year earlier. A homeowner whose air conditioning quits in July isn’t looking for a list of twenty contractors. When they ask an AI assistant, they get three to five names and a sentence about each.
```

### AI-18. Element #brxe-j90z7h (items 4.6)
NOW:
```html
The value depends on which calls those are. A repair visit averages around $350, and a full system replacement around $7,500 (Angi, 2026). One extra replacement a month from AI answers is about $90,000 a year in revenue at that average, before margin. That’s an illustration of the math, not a client result, and it only holds if the call gets answered, the visit gets booked and the estimate gets followed up.
```
NEW:
```html
What a recommendation is worth depends on which calls it brings. Nationally, a repair visit averages around $350, and a full system replacement around $7,500 (Angi, 2026). One extra replacement a month from AI answers is about $90,000 a year in revenue at that average, before margin. That’s an illustration of the math, not a client result, and it only holds if the call gets answered, the visit gets booked and the estimate gets followed up.
```

### AI-19. Element #brxe-rpojxj (items 5.4 (Andrew's answer))
NOW:
```html
<strong>We build the evidence the engines read.</strong> That starts with a steady flow of recent Google reviews that mention the work and the area, and it continues with getting your company onto the local lists and articles the answers already cite. Our <a href="/services/reputation-management-for-contractors/">review and reputation work</a> covers the first part.
```
NEW:
```html
<strong>We build the evidence the engines read.</strong> That starts with a steady flow of recent Google reviews that mention the work and the area, which our <a href="/services/reputation-management-for-contractors/">review and reputation work</a> covers. Then we take the lists and articles the answers cite for your city and ask the publishers to include you where you belong, with your reviews and record behind the request. They decide, and we never pay for a spot dressed up as an editorial pick.
```

### AI-20. Element #brxe-ievyed (items 6.1)
NOW:
```html
<strong>We make your website easy to cite.</strong> Clear pages for replacements, heat pumps, ductless systems and maintenance plans, each with plain answers to what homeowners ask, give an engine a reason to cite your own site instead of a directory. This is the same work that helps your <a href="/local-contractor-seo-blueprint/">local SEO</a>.
```
NEW:
```html
<strong>We make your website easy to cite.</strong> Clear pages for replacements, heat pumps, ductless systems and maintenance plans, each with plain answers to what homeowners ask, give an engine a reason to cite your own site instead of a directory. This is the same work that helps your <a href="/services/hvac-marketing/seo/">local SEO</a>.
```

### AI-21. Element #brxe-tvfj5n (items 6.2)
NOW:
```html
<strong>We connect it to the phone.</strong> A recommendation only pays if the call that follows gets booked and the estimate gets sold. A click from ChatGPT or Perplexity arrives with its source attached, so we can follow it through to the <a href="/services/lead-to-booked-job/">booked job</a>. Many homeowners read your name in an answer and then search for you or call directly, which leaves no trail, so we add a “how did you find us?” question to your call intake and forms and report the two counts separately.
```
NEW:
```html
<strong>We connect it to the phone.</strong> A recommendation only pays if <a href="/services/hvac-marketing/call-handling/">the call that follows gets booked</a> and the estimate gets sold. A click from ChatGPT or Perplexity arrives with its source attached, so we can follow it through to the <a href="/services/lead-to-booked-job/">booked job</a>. Many homeowners read your name in an answer and then search for you or call directly, which leaves no trail, so we add a “how did you find us?” question to your call intake and forms and report the two counts separately.
```

### AI-22. Element #brxe-b7emy6 (items 1.13 (schema))
NOW:
```html
In the local answers we tested, they mostly didn’t. When we asked for the best HVAC company in a city, nearly every company named was a locally branded company, and national franchise names made up only 3 to 5% of mentions. National studies that mix in brand and software questions show franchises doing better, so it depends on what the homeowner asks.
```
NEW:
```html
In the local answers we tested, they mostly didn’t. When we asked for the best HVAC company in a city, nearly every company named was a locally branded company, and national franchise names made up only 3 to 5% of mentions. 5W’s national HVAC index, which asks questions with no city in them, mostly returns equipment makers, franchise networks and software companies, so it depends on what the homeowner asks.
```

### AI-23. Element #brxe-wlm4wm (items 4.2, 5.6, 4.1)
NOW:
```html
In a free 20-minute Gap Review, we run the homeowner’s question for your city across the AI engines, show you who gets named and which sites the answers lean on, and talk through where your company fits.
```
NEW:
```html
In a free 20-minute Gap Review, we run the homeowner’s question for your city, or for a market you’re moving into, across the AI engines, show you who gets named and which sites the answers lean on, and talk through where your company fits. One HVAC company per market. Tiers and exit terms are on our <a href="/pricing/">pricing page</a>.
```

### New text on this page
- 4.1 note under the closing button: `Free · 20 minutes · a call with Andrew`

## Call Handling page (13733) /services/hvac-marketing/call-handling/

### CAL-1. Element #brxe-eikqnm (items 4.4)
NOW:
```html
Call handling is everything between the phone ringing and a technician or comfort advisor arriving at the house: answering, booking, confirming. Estimate follow-up is everything between the replacement quote and the homeowner’s decision. Together they make up what we call the second funnel, and they’re part of our <a href="/services/hvac-marketing/">marketing for HVAC companies</a> because marketing that stops at the call leaves most of the result to chance.
```
NEW:
```html
Call handling is everything between the phone ringing and a technician or comfort advisor arriving at the house: answering, booking, confirming. Estimate follow-up is everything between the replacement quote and the homeowner’s decision. Together they make up what we call the second funnel, and they’re part of our <a href="/services/hvac-marketing/">marketing for HVAC companies</a> because <strong>marketing that stops at the call leaves most of the result to chance</strong>.
```

### CAL-2. Element #brxe-82h1ka (items 5.3 (Andrew's answer; replaces the two 4.7 cuts))
NOW:
```html
We work alongside your CSRs, dispatchers and comfort advisors. We don’t replace your team or your call center. We help them see where the jobs are slipping and give them a simple, repeatable way to keep more of them.
```
NEW:
```html
We work alongside your CSRs, dispatchers and comfort advisors. They run the phones and the follow-up, and we improve the system they work in. If you don’t have that team yet, we help you build one you own.
```

### CAL-3. Element #brxe-ta7fwk (items 4.2)
NOW:
```html
None of this needs more leads. A replacement recovered from last month’s open estimates is a job you already paid to create.
```
NEW:
```html
None of this needs more leads. A replacement recovered from last month’s open estimates is a job you already paid to create. It’s also worth fixing before you add a location, because more calls only multiply what happens to them now.
```

### CAL-4. Element #brxe-1xm7ks (items 1.15)
NOW:
```html
Before he started Andrew Ryan Marketing, Andrew built and ran a dealership’s business development center from scratch: the phones, the follow-up and the appointments that turned into sales. This is his own sales-floor record from that work, not a client result.
```
NEW:
```html
Before he started Andrew Ryan Marketing, Andrew built and ran a dealership’s business development center from scratch: the phones, the follow-up and the appointments that turned into sales.
```

### CAL-5. Element #brxe-zfadj5 (items 4.9)
NOW:
```html
<strong>We make the replacement easier to say yes to.</strong> Clear options at the comfort visit, financing presented as part of the conversation rather than as an afterthought, and a written estimate that leaves the house the same day.
```
NEW:
```html
<strong>We make the replacement easier to say yes to.</strong> Clear options at the comfort visit, financing presented as part of the conversation rather than as an afterthought, and a written estimate in the homeowner’s hands the same day.
```

### CAL-6. Element #brxe-p0g2ft (items 4.3, 4.4)
NOW:
```html
Then we tie it back to the marketing. Once you can see which calls booked and which estimates sold, your <a href="/services/hvac-marketing/ppc/">Google Ads and LSAs</a> can be judged by sold jobs instead of leads.
```
NEW:
```html
Then we tie it back to the marketing, using the numbers in your field software. Once you can see which calls booked and which estimates sold, your <a href="/services/hvac-marketing/ppc/">Google Ads and LSAs</a> can be <strong>judged by sold jobs instead of leads</strong>.
```

### CAL-7. Element #brxe-v1fqi3 (items 1.14 (schema))
NOW:
```html
Hard for about ten days, then lightly. Most homeowners who are going to buy decide within a short window after the visit. A focused push of calls and texts in that window wins more jobs than months of reminders, and it costs your team far less time.
```
NEW:
```html
Hard for about ten days, then lightly. That window comes from Andrew’s own sales record, not an HVAC study: a quote that stayed silent for two weeks almost never came back. Your own closed estimates will show whether yours runs longer.
```

### CAL-8. Element #brxe-663t84 (items 4.7 (schema))
NOW:
```html
Because that’s where the result of the marketing is decided. If half the calls never become a visit, doubling your ad spend mostly doubles the waste. Fixing the second funnel first means every dollar of marketing after that works harder.
```
NEW:
```html
Because that’s where the result of the marketing is decided. If half the calls never become a visit, doubling your ad spend mostly doubles the waste.
```

### CAL-9. Element #brxe-5586n9 (items 4.8, 5.6, 4.1)
NOW:
```html
In a free 20-minute Gap Review, we walk through how your calls get answered and booked and what happened to last month’s replacement estimates, using the numbers you have on hand, so you can see where sold jobs are most likely slipping and what to fix first.
```
NEW:
```html
In a free 20-minute Gap Review, we walk through how your calls get answered and booked and what happened to last month’s replacement estimates, so you can see where sold jobs are most likely slipping and what to fix first. Bring last month’s call count and open estimates if you have them. One HVAC company per market. Tiers and exit terms are on our <a href="/pricing/">pricing page</a>.
```

### New text on this page
- 1.15 label above the four tiles: `Andrew’s own dealership record · not a client result`
- 1.15 line under the four tiles: `The method is what travels: a big-ticket purchase, a phone inquiry, a booked appointment, financing, follow-up and competitors quoting the same buyer. A comfort visit is a sales appointment too.`
- 4.1 note under the hero button: `Free · 20 minutes · a call with Andrew`
- 4.1 note under the closing button: `Free · 20 minutes · a call with Andrew`

## SEO page (13745) /services/hvac-marketing/seo/

### SEO-1. Element #brxe-p3a5tu (items 1.3)
NOW:
```html
Most HVAC calls from Google come from two places: the map with three companies on it, and the pages below it. They rank for different reasons, and an HVAC company needs a plan for each.
```
NEW:
```html
The HVAC calls you don’t pay Google for come from two places: the map with three companies on it, and the pages below it. They rank for different reasons, and you need a plan for each.
```

### SEO-2. Element #brxe-tsatu7 (items 4.9, 4.4)
NOW:
```html
HVAC SEO is the work that gets your company found on Google without paying for each click: in the map results for “furnace repair near me” and in the organic results for searches like “heat pump installation [your city].” It’s one channel inside our <a href="/services/hvac-marketing/">HVAC marketing agency</a> work, and like the rest, we judge it by the calls it produces and the jobs those calls sell.
```
NEW:
```html
HVAC SEO is the work that gets your company found on Google without paying for each click: in the map results for “furnace repair near me” and in the organic results for searches like “heat pump installation [your city].” It’s one channel in our work as an <a href="/services/hvac-marketing/">HVAC marketing agency</a>, and like the rest, <strong>we judge it by the calls it produces and the jobs those calls sell</strong>.
```

### SEO-3. Element #brxe-1qx090 (items 1.4, 1.16)
NOW:
```html
SEO is slower than ads, but it keeps working when you stop paying. For an established HVAC company, it’s usually the channel that brings cost per sold job down over time.
```
NEW:
```html
SEO is slower than ads, but its calls don’t stop when the ad budget does. For an established company, it’s usually the channel that brings cost per sold job down over time.
```

### SEO-4. Element #brxe-oahnr1 (items 4.2)
NOW:
```html
Distance is the one thing you can’t change in the map, which is why a company a few miles outside the center of town has to win on reviews and relevance. Our <a href="/services/hvac-marketing/ai-visibility/">AI visibility research</a> found the same signals, reviews and mentions on other sites, line up with being named by ChatGPT and Google’s AI answers.
```
NEW:
```html
Distance is the one thing you can’t change in the map, which is why a company a few miles outside the center of town has to win on reviews and relevance. It’s also why a second location starts from zero: a new address has no reviews and no history. Our <a href="/services/hvac-marketing/ai-visibility/">AI visibility research</a> found the same signals, reviews and mentions on other sites, line up with being named by ChatGPT and Google’s AI answers.
```

### SEO-5. Element #brxe-o5djej (items 1.2)
NOW:
```html
<strong>We build a small number of real local pages, not hundreds of thin ones.</strong> Google’s spam policies call mass-produced, near-identical “[service] in [town]” pages scaled content abuse. We build pages for the towns that matter most to you, with real jobs, photos and local detail like utility rebates, and we’ll tell you if a past agency built pages that are now a risk.
```
NEW:
```html
<strong>We build a small number of real local pages, not hundreds of thin ones.</strong> Google’s spam policies treat mass-produced, near-identical “[service] in [town]” pages as doorway abuse or scaled content abuse. We build pages for the towns that matter most to you, with real jobs, photos and local detail like utility rebates, and we’ll tell you if a past agency built pages that are now a risk.
```

### SEO-6. Element #brxe-hzefla (items 4.3)
NOW:
```html
<strong>We measure SEO by sold jobs.</strong> Rankings and traffic are early signs. The report that matters shows the calls that came from Maps and organic search and what they sold, alongside what you spent.
```
NEW:
```html
<strong>We measure SEO by sold jobs.</strong> Rankings and traffic are early signs. The report that matters shows the calls that came from Maps and organic search and what they sold, from the numbers in your field software, alongside what you spent.
```

### SEO-7. Element #brxe-knbv80 (items 1.1)
NOW:
```html
The same approach is working outside HVAC: for a Tennessee plumbing company, it moved the average Google Maps position from 5.4 to 2.5. The full method for contractors is in our <a href="/local-contractor-seo-blueprint/">local contractor SEO blueprint</a>, and the calls SEO brings in are only worth what your <a href="/services/hvac-marketing/call-handling/">call handling</a> turns into booked visits.
```
NEW:
```html
The full method for contractors is in our <a href="/local-contractor-seo-blueprint/">local contractor SEO blueprint</a>, and the calls SEO brings in are only worth what your <a href="/services/hvac-marketing/call-handling/">call handling</a> turns into booked visits.
```

### SEO-8. Element #brxe-oyuvjt (items 5.6, 4.1)
NOW:
```html
In a free 20-minute Gap Review, we look at where you show up in Maps and search for the services you want to sell and how you compare with the companies above you. If you can open your Google Business Profile or Search Console numbers on the call, we also look at what those rankings are bringing in, so you can see what to fix first.
```
NEW:
```html
In a free 20-minute Gap Review, we look at where you show up in Maps and search for the services you want to sell and how you compare with the companies above you. If you can open your Google Business Profile or Search Console numbers on the call, we also look at what those rankings are bringing in, so you can see what to fix first. One HVAC company per market. Tiers and exit terms are on our <a href="/pricing/">pricing page</a>.
```

### New text on this page
- 1.1 result card: label: `Client result · plumbing, not HVAC`
- 1.1 result card: figure: `5.4 → 2.5`
- 1.1 result card: line: `Tennessee Plumbing, Johnson City: average Google Maps rank for “plumbers johnson city tn,” April 3 to April 6, 2026, after profile work like step 01 (BrightLocal).`
- 1.1 result card: quote: `“The phone started ringing more — that’s what matters.” Tim S., Owner`
- 1.1 result card: link: `See the case study →`
- 4.1 note under the hero button: `Free · 20 minutes · a call with Andrew`
- 4.1 note under the closing button: `Free · 20 minutes · a call with Andrew`

## New elements: where they go and how they look

No new sections. Four small pieces of text and one graph are new elements. The CSS below is a suggestion that follows the styles already on these pages (WPCode CSS 13724, 13729, 13736, 13748). Adjust the mechanics as Bricks needs, and keep the look.

### N-1. Note under the booking buttons (4.1)
Text: `Free · 20 minutes · a call with Andrew`
Where: inside each `.hero-ctas` wrapper, as the element right after the button, on its own line.
- Google Ads, Call Handling and SEO: under the hero button and under the closing button (two per page).
- AI Visibility: under the closing button only. Its hero button jumps to the findings, so it gets no note.
```css
.cta-note{flex-basis:100%;margin:2px 0 0;font:600 14px/1.4 "DM Sans",ui-sans-serif,system-ui,sans-serif;color:var(--on-ink-muted)}
```
Both spots are on dark bands (`--ink` #222 and `--ink-3` #2a2a2a), and `--on-ink-muted` #bdbdbd is the color the hero paragraph already uses there.

### N-2. Link inside the dark closing box (4.1)
The closing paragraphs now end with a link to /pricing/. No link has sat in that box before, so it needs a style:
```css
.cta-box p a{color:var(--on-ink);font-weight:600;text-decoration:underline;text-underline-offset:3px}
```

### N-3. Call Handling record tiles (1.15)
Above the four tiles (`.hv-record`, #brxe-7vemxe), a label: `Andrew’s own dealership record · not a client result`
Under the four tiles, one line: `The method is what travels: a big-ticket purchase, a phone inquiry, a booked appointment, financing, follow-up and competitors quoting the same buyer. A comfort visit is a sales appointment too.`
Both come word for word from the hub's own record block (minus "27 months", which is already a tile here). The paragraph above (#brxe-1xm7ks) loses its last sentence, as given in CH-4.
```css
.hv-record-label{margin:24px 0 0;font:700 14px/1.4 "DM Sans",ui-sans-serif,system-ui,sans-serif;color:#333}
.hv-record-label+.hv-record{margin-top:10px}
.hv-record+.hv-note{margin-top:14px;max-width:680px}
```
The line under the tiles can reuse the existing `.hv-note` class (15px, #666).

### N-4. SEO result card (1.1)
Where: directly above paragraph #brxe-knbv80 (which loses its first sentence, see SEO-7), in the same container, so it sits under the six steps.
Build it as one `.hv-stat` card (the class the AI page's four findings cards use: white, 1px #E0E0E0 border, 4px orange left bar), max-width 680px:
- Label (small, #666, above the figure): `Client result · plumbing, not HVAC`
- Figure (`.hv-num`): `5.4 → 2.5`
- Line (p): `Tennessee Plumbing, Johnson City: average Google Maps rank for “plumbers johnson city tn,” April 3 to April 6, 2026, after profile work like step 01 (BrightLocal).`
- Quote (p): `“The phone started ringing more — that’s what matters.”` followed by `Tim S., Owner` in #666
- Link: `See the case study →` to `/case-studies/`
```css
.hv-result{max-width:680px;margin:24px 0}
.hv-result .hv-k{display:block;font-size:13px;font-weight:700;color:#666;margin-bottom:6px}
.hv-result .hv-who{color:#666}
```
Every figure, date, the search and the quote are on /case-studies/ today (fetched 2026-11-18 21:44Z). The dash inside the quote is the client's own wording as published, so it stays.

### N-5. Google Ads: graph under the lead-cost example (Andrew's request, 2026-11-18 5:59 PM ET)
Where: directly after the `.prose` div that holds paragraph #brxe-1wf1r9 (div #brxe-reop9u), inside the same container, in the section "Not every HVAC call is worth the same". It is the last thing in that section. Mockups: `graph-google-ads-desktop.png` and `graph-google-ads-phone.png` in the project files folder for this pass.

What it shows: the two accounts from the paragraph as two bars of gross profit, each split into replacements (orange, first) and repairs (gray). Both bars share one scale, with $17,800 as the full width, and each total sits at the end of its bar. The second total is orange because it is the larger one, the way the hub's example table marks its best row.

Every number is the paragraph's own:
- $50 per lead: 100 leads × $50 = $5,000 spent. 2 replacements × $7,500 × 40% = $6,000. 60 repairs × $350 × 40% = $8,400. Total $14,400.
- $80 per lead: 60 leads × $80 = $4,800 spent. 5 replacements × $7,500 × 40% = $15,000. 20 repairs × $350 × 40% = $2,800. Total $17,800.
- Bar lengths: the first bar is 14,400 ÷ 17,800 = 0.809 of the second.

HTML (one Bricks code element, or the same structure built from Bricks elements; keep the classes, the two `role="img"` labels and the four `title` tooltips):
```html
<figure class="hv-fig">
<figcaption><span class="hv-k">Illustrative example, not a client result</span><strong class="hv-fig-t">Gross profit from about $5,000 in ad spend</strong></figcaption>
<div class="hv-fig-row hv-fig-row--1">
<p class="hv-fig-l"><strong>$50 per lead</strong><span>100 leads: 2 replacements, 60 repairs</span></p>
<div class="hv-fig-b" role="img" aria-label="At $50 per lead, 100 leads became 2 replacements and 60 repairs. Gross profit $14,400: $6,000 from replacements and $8,400 from repairs."><span class="hv-bar"><span class="hv-seg hv-seg--repl" title="2 replacements × $7,500 × 40% = $6,000"></span><span class="hv-seg hv-seg--rep" title="60 repairs × $350 × 40% = $8,400"></span></span><span class="hv-fig-v"><span class="u">$</span>14,400</span></div>
</div>
<div class="hv-fig-row hv-fig-row--2">
<p class="hv-fig-l"><strong>$80 per lead</strong><span>60 leads: 5 replacements, 20 repairs</span></p>
<div class="hv-fig-b" role="img" aria-label="At $80 per lead, 60 leads became 5 replacements and 20 repairs. Gross profit $17,800: $15,000 from replacements and $2,800 from repairs."><span class="hv-bar"><span class="hv-seg hv-seg--repl" title="5 replacements × $7,500 × 40% = $15,000"></span><span class="hv-seg hv-seg--rep" title="20 repairs × $350 × 40% = $2,800"></span></span><span class="hv-fig-v"><span class="u">$</span>17,800</span></div>
</div>
<p class="hv-fig-leg"><span><i class="hv-sw hv-seg--repl"></i>Replacements</span><span><i class="hv-sw hv-seg--rep"></i>Repairs</span></p>
</figure>
```
CSS, added to WPCode 13729:
```css
#brx-content .hv-fig{max-width:680px;margin:24px 0 0;padding:24px 26px 22px;background:#fff;border:1px solid #E0E0E0;border-radius:10px;font-family:"DM Sans",ui-sans-serif,system-ui,sans-serif;color:#333}
.hv-fig figcaption{display:block;margin:0 0 20px;text-align:left}
.hv-fig .hv-k{display:block;font-size:13px;font-weight:700;color:#666;margin:0 0 6px}
.hv-fig-t{display:block;font-family:"Plus Jakarta Sans",ui-sans-serif,system-ui,sans-serif;font-size:20px;font-weight:800;line-height:1.25;letter-spacing:-.01em;color:#333;text-wrap:balance}
.hv-fig-row+.hv-fig-row{margin-top:20px}
.hv-fig-l{margin:0 0 8px;font-size:15px;line-height:1.4;color:#666;display:flex;flex-wrap:wrap;align-items:baseline;gap:2px 10px}
.hv-fig-l strong{font-size:17px;font-weight:700;color:#333}
.hv-fig-b{display:flex;align-items:center;gap:12px;--val:104px}
.hv-fig-b .hv-bar{display:flex;gap:2px;height:16px;flex:0 0 auto;width:calc((100% - var(--val) - 12px)*var(--r))}
.hv-fig-row--1 .hv-bar{--r:.809}
.hv-fig-row--2 .hv-bar{--r:1}
.hv-seg{display:block;flex:1 1 0;min-width:2px;height:100%;transition:filter .15s ease-out}
.hv-seg:hover{filter:brightness(1.12)}
.hv-seg--repl{background:#EF662F}
.hv-seg--rep{background:#666}
.hv-fig-row--1 .hv-seg--repl{flex-grow:6000}
.hv-fig-row--1 .hv-seg--rep{flex-grow:8400}
.hv-fig-row--2 .hv-seg--repl{flex-grow:15000}
.hv-fig-row--2 .hv-seg--rep{flex-grow:2800}
.hv-bar .hv-seg:last-child{border-radius:0 4px 4px 0}
.hv-fig-v{flex:0 0 auto;font-family:"Plus Jakarta Sans",ui-sans-serif,system-ui,sans-serif;font-size:24px;font-weight:800;line-height:1;letter-spacing:-.02em;color:#333;white-space:nowrap}
.hv-fig-row--2 .hv-fig-v{color:#EF662F}
.hv-fig-v .u{font-family:Arial,Helvetica,sans-serif;font-size:.55em;font-weight:700;opacity:.7;vertical-align:.55em;margin-right:1px;letter-spacing:0}
.hv-fig-leg{margin:18px 0 0;display:flex;flex-wrap:wrap;gap:6px 20px;font-size:14px;line-height:1.4;color:#666}
.hv-fig-leg span{display:inline-flex;align-items:center;gap:7px}
.hv-sw{display:inline-block;width:12px;height:12px;border-radius:2px}
@media (max-width:640px){#brx-content .hv-fig{padding:20px 18px 18px}.hv-fig-t{font-size:19px}.hv-fig-v{font-size:22px}.hv-fig-b{--val:96px}}
@media (prefers-reduced-motion:reduce){.hv-seg{transition:none}}
```
Notes:
- No script and no animation. The bars are plain boxes sized by the CSS, so the graph looks the same with JavaScript off and in a full-page screenshot.
- The two colors are brand colors: #EF662F and #666666. Checked with a palette validator on white: the pair stays apart for color-blind readers (13.2, against a floor of 8) and both clear 3 to 1 against the card.
- The label reuses the wording of the hub's own example label ("Illustrative example, not client results.").
- Checked in a browser on a copy of the live page at 1440, 390 and 360 wide: no sideways scroll, nothing outside the card, bar lengths 413 and 510 px on desktop and 165 and 204 px at 390.

## Part 2: display bugs (no copy changes)

- 2.1 SEO, last FAQ: the link "Google Ads and LSAs" (in #brxe-9jpect) has no link style. 2.2 AI and Call Handling step cards: four links are orange with no underline (about 3.2 to 1 on white). One rule fixes both, on all four pages:
```css
#faq details p a,.hv-steps a,.hv-stat a{color:var(--orange-ink);font-weight:600;text-decoration:underline;text-underline-offset:3px}
```
  It replaces the current `.hv-steps a,.hv-stat a{color:#EF662F}`. `--orange-ink` is #b84a0e, the body link color already used in `.prose a`.
- 2.3 Google Ads, Call Handling and SEO, on a phone: the sub-nav opens with the current page out of view. Scroll the bar, never the page:
```html
<script>(function(){var w=document.querySelector('.subnav-in'),a=w&&w.querySelector('a[aria-current]');if(!a)return;function c(){var r=a.getBoundingClientRect(),q=w.getBoundingClientRect();w.scrollLeft+=(r.left-q.left)-(q.width-r.width)/2}c();window.addEventListener('load',c)})();</script>
```
  HVAC spokes only in this pass. Do not use scrollIntoView, which would move the page.
- 2.4 "follow-up" breaks across two lines in two Call Handling headings and one hub card. Wrap the word so it can't break, and leave the characters alone (a different hyphen character could change how the heading matches a search):
  - #brxe-tzs7tc: `What call handling and estimate <span class="nw">follow-up</span> mean for an HVAC company`
  - #brxe-kk62mr: `HVAC call handling and <span class="nw">follow-up</span>: common questions` (keep the existing `<strong>` wrapper)
  - Hub 6515, service card 06 title: `Estimate <span class="nw">follow-up</span> and estimate-to-sale`
```css
.nw{white-space:nowrap}
```
- 2.5 All four pages: the sub-nav's current link outputs `aria-current="page page"`. Set it so it outputs `page` once.
- 2.6 All four pages: breadcrumb links are 13px tall. Bring the tap height to at least 24px:
```css
.crumbs a,.crumbs span{display:inline-block;padding:6px 0}
```
- 2.8 llms.txt: replace the single line that starts `- [HVAC Marketing](https://andrewryanmarketing.com/services/hvac-marketing/):` with these five, under a new `## HVAC Marketing` heading if the file's layout allows, otherwise in place:
```
- [HVAC Marketing, Hub](https://andrewryanmarketing.com/services/hvac-marketing/): Marketing for heating and cooling companies, measured by sold jobs rather than leads, from search and ads through call handling and estimate follow-up.
- [AI Visibility for HVAC Companies](https://andrewryanmarketing.com/services/hvac-marketing/ai-visibility/): Which HVAC companies ChatGPT, Perplexity and Google's AI answers name, from the Answer Gap Index HVAC data for September and October 2026.
- [HVAC Google Ads and Local Services Ads](https://andrewryanmarketing.com/services/hvac-marketing/ppc/): Separate campaigns for repair, replacement and maintenance calls, sold-job revenue sent back to Google, and the move of Local Services Ads into Google Ads.
- [HVAC Call Handling and Estimate Follow-Up](https://andrewryanmarketing.com/services/hvac-marketing/call-handling/): Where jobs are lost between the phone ringing and the replacement decision, and how we work with CSRs and comfort advisors.
- [HVAC SEO Services](https://andrewryanmarketing.com/services/hvac-marketing/seo/): Google Maps and organic search for HVAC companies, covering the Google Business Profile, reviews, service pages, local pages and links.
```
  Leave every other line of llms.txt alone in this pass. If the file is generated by a plugin and can't be edited line by line, skip 2.8 and report.

## FAQ schema (keep the hidden FAQ text word for word with the page)

Five FAQ answers change. Each answer's plain text (no link markup) goes into the FAQPage JSON-LD of that page:
- Google Ads, WPCode 13728: "How much do Google Ads cost for an HVAC company?" (PPC-12) and "Can Google Ads use the revenue in ServiceTitan or Housecall Pro?" (PPC-13).
- AI Visibility, WPCode 13722: "Can national franchises crowd a local HVAC company out of AI answers?" (AI-22).
- Call Handling, WPCode 13735: "How long should an HVAC company follow up on a replacement estimate?" (CAL-7) and "Why would a marketing company work on call handling?" (CAL-8).
- SEO, WPCode 13747: no change.

## Part 6: links on other pages

| # | Page | Find (visible text) | Change |
|---|---|---|---|
| 6.4 | HVAC hub 6515, service 02 | the link text `Local SEO for contractors →` (it already points to /services/hvac-marketing/seo/) | Text becomes `HVAC SEO →`. Keep the arrow span and the href. |
| 6.5 | /services/ppc-for-contractors/ | "…fencing, flooring, roofing, HVAC, electrical, and plumbing contractors anywhere a job is worth a few thousand dollars or more…" | Link the word `HVAC` to `/services/hvac-marketing/ppc/`. |
| 6.6 | /local-services-ads-for-contractors/ | the cost table row `HVAC` · `$51` | Link the word `HVAC` in that row to `/services/hvac-marketing/ppc/`. |
| 6.7 | /local-contractor-seo-blueprint/ | the paragraph that starts "Recurring service trades (HVAC, plumbing, electrical, cleaning)" | Add one sentence at the end of that paragraph: `The HVAC version of this plan is on our <a href="/services/hvac-marketing/seo/">HVAC SEO services</a> page.` |
| 6.8 | /answer-gap-index/ | "Home: roofer, plumber, HVAC, electrician." | Link the word `HVAC` to `/services/hvac-marketing/ai-visibility/`. |
| 6.9 | /services/ | the "Built for your trade" line, where "HVAC, roofing, electricians, plumbers and more" is plain text | Link `HVAC` to `/services/hvac-marketing/`, `roofing` to `/services/roofing-marketing/`, `electricians` to `/services/marketing-for-electricians/`, `plumbers` to `/services/marketing-for-plumbers/`. Same link style as the four trade links already in that line. |

6.1, 6.2 and 6.3 are inside the element edits above (AI-20, AI-21, PPC-9). All four target URLs for 6.9 are in page-sitemap.xml today.
Pages built in WPBakery with nested rows are changed by hand in the editor, one page at a time, each checked on the live page before the next.

## Basis for each item

Andrew's rule (2026-11-18): the simulated buyer reads are a source of ideas and do not decide what ships. So each item is tagged by what it stands on.

| Items | Stands on |
|---|---|
| 1.1, 1.2, 1.5, 1.7, 1.8, 1.9, 1.10, 1.12, 1.13 | A fact checked at its source on 2026-11-18 |
| 1.3, 1.16 | A fact (ads and LSAs also bring calls) and Andrew's rule on a third trade name in one section |
| 1.4 | The page's own step 02 (reviews slip without upkeep) |
| 1.6 | The click-cost claim had no support; the fee wording is from /services/ppc-for-contractors/ |
| 1.11 | GPT's caution: both sides of the comparison now use the same basis |
| 1.14 | An unsupported claim, replaced with what the estimate follow-up page already says |
| 1.15 | Andrew's rule that the dealership record never reads as a client result; wording from the hub |
| 2.1 to 2.8 | Display bugs seen on the live pages at 1440 and 390 |
| 4.1 | Idea from the reads. The hub already says all three things, and GPT agrees |
| 4.2 | Andrew's champion definition (the owner who is expanding). The reads only showed where it was missing |
| 4.3 | Idea from the reads. The hub already says where the numbers come from |
| 4.4, 4.5, 4.8 | Ideas from the reads only |
| 4.6 | Idea from the reads, with a source (BrightLocal, 2026) |
| 4.7 | Cuts that pay for the additions, under Andrew's rule that pages don't grow |
| 4.9 | Wording fixes |
| 5.3, 5.4, 5.6 | Andrew's answers and approval of 2026-11-18 |
| N-5 graph | Andrew's request of 2026-11-18 ("add a graph along with it as a visual reference to make it easier to understand") |
| 6.1 to 6.9 | Links |

## Lines to protect (unchanged in this pass)

- "That’s an illustration of the math, not a client result." It stays on the AI page. On the Google Ads page it moves into the graph's label ("Illustrative example, not a client result"), directly under the example, unless Andrew asks to keep the sentence as well.
- "read the percentages as a direction, not a precise rate", and the counts under every number on the AI page
- "Schema markup, homepage length and directory listings made no difference in the study."
- "it only holds if the call gets answered, the visit gets booked and the estimate gets followed up"
- "We don’t promise a timeline." on the AI page
- "not hundreds of thin ones", and the flat "No." on town pages
- "You own the ad account, and we don’t mark up your ad spend."
- "save your LSA reports first, because they don’t carry over"
- "we’ll work out your cost per sold job by call type" and "on a shared screen"
- The Call Handling table, above all "“How much is a new unit?” gets a price range instead of a visit"
- "None of this needs more leads."
- The three hero questions: "whose name comes back?", "buying tune-ups while your install crews have open days" and "calls you paid for last July"

## After the save: checks on the live pages (logged out, 1440 and 390 wide)

1. Every NEW string above is on its page, and each of these is gone: "hundreds of times a month", "Usually Google’s", "Local names", "costlier clicks", "built-in Google Ads revenue import", "Very few contractors have this in place", "Here is why this matters", "Most homeowners who are going to buy decide", "We don’t replace your team or your call center" in the Call Handling definition (it stays in the FAQ answer "No. We work with the people you have."), "it keeps working when you stop paying", "calls scaled content abuse", "The same approach is working outside HVAC".
2. The FAQ JSON-LD on Google Ads, AI Visibility and Call Handling matches the visible answers word for word. Rich Results still shows Service and FAQ with 0 errors.
3. The note sits under each button it belongs to, on one line at 390, and the "Message Andrew" box doesn't cover it.
4. On a phone, the sub-nav of Google Ads, Call Handling and SEO opens with the current page in view, and the page itself hasn't scrolled.
5. `aria-current="page"` appears once per sub-nav. Breadcrumb links are at least 24px tall.
6. Step-card and FAQ links are underlined in the darker orange. The pricing link in each closing box is readable on the dark background.
7. No heading leaves a single word on its last line at either width. No sideways scroll at 390.
8. The nine links in Part 6 resolve (200) and point where the table says.
9. Google Ads graph (N-5): it sits right under the example paragraph, the paragraph no longer ends with "That’s an illustration of the math, not a client result.", and the graph's label reads "Illustrative example, not a client result". The first bar is about 0.81 the length of the second, each total sits at the end of its bar, nothing leaves the card, and there is no sideways scroll at 390 or 360.
Report each check with how it was verified. Keep the previous revision id of every page touched as the rollback.
