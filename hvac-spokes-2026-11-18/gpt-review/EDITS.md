# HVAC spokes: edits from the outside (GPT) review, 2026-11-18

STATUS: PROPOSED. Waiting for Andrew's yes. Nothing here is live. Save only when his own message names it.
This file is the single agreed wording. It replaces any earlier draft of these edits.

Copy changes only. No layout, class or style change. One new Bricks text element pair on the PPC page (edit 1c).
Pages: PPC 13726, AI Visibility 13720, Call Handling 13733, SEO 13745. Schema snippet touched: WPCode 13722 (AI page FAQ text, edit 3b).

## Why (checked 2026-11-18 on Google's own pages)

- blog.google, 20 Aug 2025, "Google Verified makes it easier to find trusted local businesses advertising on Google": "Google Verified will replace other LSA badges and programs", naming Google Guaranteed, Google Screened, License Verified by Google and the Money Back Guarantee, "Starting in October".
- Google Ads Help, answer 17213585, "Local Services Ads transition to Performance Max campaigns with pay-per-lead goals":
  - "August 2026: The first phase of the migration begins for select home and storefront service advertisers in the United States (including plumbing, HVAC, electrical, appliance repair, house cleaning, lawn care, roofing, pest control, and moving)."
  - "Late 2026: The migration expands to broader advertiser groups, including service-area businesses without physical storefronts and accounts with custom bidding or booking configurations."
  - "Your ads in Performance Max campaigns with pay-per-lead goals will continue to show exclusively on Google Search and Google Maps in the same ad positions as before"
  - "You still only pay for valid leads (such as phone calls and messages) rather than ad clicks."
  - "Manual bidding (such as setting a maximum cost-per-lead) is no longer supported in Google Ads."
  - "previous performance reports won't carry over to Google Ads."
  - "standard Performance Max campaigns serve across all Google ad networks, including YouTube, Gmail, and the Google Display Network."
- The 40% gross margin is the same example figure the HVAC hub calculator already uses (page 6515: "Gross margin 40%").
- Site-wide, the Gap Review is described as "20 minutes on a shared screen with your own numbers in front of you" (/6-gap-revenue-map/). The closes below now match that.

## PPC page (13726) /services/hvac-marketing/ppc/

### 1a. Badge name (intro paragraph)
FIND:    with the Google Guaranteed or Google Screened badge
REPLACE: with the Google Verified badge

### 1b. Comparison table, third column name
Column header cell: `Performance Max` becomes `Standard Performance&nbsp;Max` (non-breaking space between Performance and Max so the header breaks after "Standard").
The four phone labels `data-l="Performance Max"` become `data-l="Standard Performance Max"`.
The H2 above the table stays "Local Services Ads, search ads and Performance Max".

### 1c. Two new short paragraphs under the table
Insert as two text elements (tag p, same class as its neighbour) directly ABOVE the existing paragraph that starts "Local Services Ads lean heavily on your review count". That paragraph stays unchanged.

Paragraph 1:
One change to know about: Google is moving Local Services Ads into Google Ads, and its timeline puts HVAC in the first phase, which began in August 2026. After the move, your LSAs appear there as a Performance Max campaign with a pay-per-lead goal. That isn’t the standard Performance Max in the table above. It still runs only on Search and Maps, and you still pay per lead.

Paragraph 2:
If your account hasn’t moved yet, save your LSA reports first, because they don’t carry over. Once it has, check the bidding, because you can no longer set a maximum cost per lead.

### 2a. Call-type table, System replacement row
FIND:    One sale can pay for a month of ads.
REPLACE: At a 40% gross margin, one sale leaves about $3,000 in gross profit to cover what the ads cost.

### 2b. Worked example paragraph
FIND:    on almost the same spend.
REPLACE: on almost the same spend, or about $9,000 more in gross profit at a 40% margin.
(The next sentence, "That’s an illustration of the math, not a client result.", stays.)

### 4a. Closing paragraph
FIND:    In a free 20-minute Gap Review, we look at your search terms, your landing pages and what your ad calls actually sold, so you can see your cost per sold job by call type and where the spend is leaking.
REPLACE: In a free 20-minute Gap Review, we go through your ad account with you on a shared screen: the search terms you’re paying for, the pages they land on and where the spend is most likely leaking. Bring last month’s calls and sold jobs if you have them, and we’ll work out your cost per sold job by call type.

## AI Visibility page (13720) /services/hvac-marketing/ai-visibility/

### 3a. Step 04, "We connect it to the phone." (the bold lead-in stays)
FIND:    A recommendation only pays if the call that follows gets booked and the estimate gets sold, so we track AI-sourced calls the same way we track every other source, through to the <a href="/services/lead-to-booked-job/">booked job</a>.
REPLACE (version A, the default): A recommendation only pays if the call that follows gets booked and the estimate gets sold. A click from ChatGPT or Perplexity arrives with its source attached, so we can follow it through to the <a href="/services/lead-to-booked-job/">booked job</a>. Many homeowners read your name in an answer and then search for you or call directly, which leaves no trail, so we add a “how did you find us?” question to your call intake and forms and report the two counts separately.

Version B (use ONLY if Andrew says the intake question is not how he works): same first two sentences, then: Many homeowners read your name in an answer and then search for you or call directly, which leaves no trail, so we report the calls we can trace and say plainly what that number leaves out.

### 3b. Last FAQ answer ("How long does it take to start showing up in AI answers?")
FIND:    alongside the calls and jobs that came from it.
REPLACE: alongside the calls and jobs we can trace to it.
This sentence appears twice in the page source: once in the visible FAQ and once in the FAQPage JSON-LD (WPCode 13722). Change both so the schema text still matches the page word for word.

## Call Handling page (13733) /services/hvac-marketing/call-handling/

### 4b. Closing paragraph
FIND:    what happened to last month’s replacement estimates, so you can see where the sold jobs are slipping and what to fix first.
REPLACE: what happened to last month’s replacement estimates, using the numbers you have on hand, so you can see where sold jobs are most likely slipping and what to fix first.

## SEO page (13745) /services/hvac-marketing/seo/

### 4c. Closing paragraph
FIND:    In a free 20-minute Gap Review, we look at where you show up in Maps and search for the services you want to sell, how you compare with the companies above you, and what those rankings are bringing in, so you can see what to fix first.
REPLACE: In a free 20-minute Gap Review, we look at where you show up in Maps and search for the services you want to sell and how you compare with the companies above you. If you can open your Google Business Profile or Search Console numbers on the call, we also look at what those rankings are bringing in, so you can see what to fix first.

## Not changed
- AI Visibility closing paragraph (it only promises what can be run from outside).
- Titles, metas, H1s, H2s, buttons, sub-nav, FAQ questions.
- No other page. The LSA guide and the general PPC page do not mention the Performance Max move yet; that is a separate proposal.

## Checks after saving (each page, logged out, 1440 and 390)
1. Old strings gone: "Google Guaranteed", "Google Screened", "One sale can pay for a month of ads", "track AI-sourced calls the same way", "that came from it", "what your ad calls actually sold" each appear 0 times in the rendered page.
2. New strings present once each ("we can trace to it" twice on the AI page: body and JSON-LD).
3. PPC table: desktop header reads "Standard Performance Max"; on phone all four card labels read "STANDARD PERFORMANCE MAX"; table still stacks into cards at 390; no horizontal scroll.
4. PPC: two new paragraphs sit between the table and the "lean heavily" sentence, with the same type size and spacing as that sentence.
5. Both JSON-LD blocks on each page still parse; AI page FAQPage answer text equals the visible answer.
6. details count equals summary count; zero "<!-- /wp:" markers; no console errors.
7. Record revision ids before and after for all four pages and WPCode 13722 in a rollback note.
