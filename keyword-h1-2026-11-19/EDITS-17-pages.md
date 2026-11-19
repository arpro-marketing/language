# Keyword H1s: the 17 pages (APPROVED)

Andrew, in the thread on 2026-11-19 at 1:23 PM ET: "Make the keyword H1 changes on the 17 pages in the table." The table is PROPOSAL-other-pages.md in this folder (the 17 pages in sections A and B).

## For each page, three edits plus one CSS block

1. Replace the eyebrow (EYEBROW NOW -> EYEBROW NEW). Where the eyebrow was a `<p>`, it becomes a `<div>` with the same classes plus `kw-ey`, because an H1 can't sit inside a `<p>`.
2. Change the old H1's opening tag (H1 NOW -> H2 NEW). Keep everything inside it exactly as it is.
3. Change that heading's closing `</h1>` (the first one after it) to `</h2>`.
4. Add the page's CSS file from `pages/` in a `<style>` block placed right AFTER the hero markup in the same code / raw HTML element (so it comes after the hero's own styles). Copy the file verbatim. For a native Bricks page (/services/crm-email-and-automation/), put it in the page's custom CSS, set the Heading element brxe-omgplf tag to h2 with class kw-q added, and make the Basic Text element brxe-u1c8d5 a div whose content is the EYEBROW NEW inner HTML.

NOW strings are as the live page prints them (fetched logged out 2026-11-19 ~1:10 PM ET). If the stored copy differs only in entity encoding (· vs &middot;) or whitespace, match the equivalent. Otherwise stop and report if any NOW string is not found exactly once. One page at a time: record the revision, save, purge that page, fetch it logged out with a cache-buster, confirm exactly one `<h1>` and that it is `h1.kw-eh` with the listed text, then the next page. Add the rows to ROLLBACK.txt. Do not touch any other page.

## What was tested

Each page was rendered from its live code with and without the change in Chromium at 1440, 768, 390 and 360 wide, and computed styles compared. On the 10 no-wording pages the big headline, its colored words, the eyebrow and the next three blocks are identical (font, size, weight, color, spacing, position), apart from a 1px width rounding on the Revenue Leak Finder eyebrow. On the 7 wording pages only the eyebrow's length changes; the headline styling is identical, and the content below shifts only by the eyebrow's extra line where it wraps.

## /revenue-breakpoint-diagnostic/

CSS: `pages/revenue-breakpoint-diagnostic.css`

EYEBROW NOW:
```html
<p class="eye">Revenue Breakpoint Diagnostic &middot; 7 questions &middot; 2 minutes</p>
```
EYEBROW NEW:
```html
<div class="eye kw-ey"><h1 class="kw-eh">Revenue Breakpoint Diagnostic</h1><span class="kw-ex"> &middot; 7 questions &middot; 2 minutes</span></div>
```
H1 NOW:
```html
<h1>
```
H2 NEW:
```html
<h2 class="kw-q">
```

## /6-gap-revenue-map/

CSS: `pages/6-gap-revenue-map.css`

EYEBROW NOW:
```html
<p class="eyebrow">The 6-Gap Revenue Map&trade;</p>
```
EYEBROW NEW:
```html
<div class="eyebrow kw-ey"><h1 class="kw-eh">The 6-Gap Revenue Map&trade;</h1></div>
```
H1 NOW:
```html
<h1>
```
H2 NEW:
```html
<h2 class="kw-q">
```

## /sales-and-marketing-consulting-for-contractors/

CSS: `pages/sales-and-marketing-consulting-for-contractors.css`

EYEBROW NOW:
```html
<p class="smc-eyebrow smc-rev">Sales &amp; Marketing Consulting for Contractors</p>
```
EYEBROW NEW:
```html
<div class="smc-eyebrow smc-rev kw-ey"><h1 class="kw-eh">Sales &amp; Marketing Consulting for Contractors</h1></div>
```
H1 NOW:
```html
<h1 class="smc-rev smc-d1">
```
H2 NEW:
```html
<h2 class="kw-q smc-rev smc-d1">
```

## /services/lead-to-booked-job/

CSS: `pages/services_lead-to-booked-job.css`

EYEBROW NOW:
```html
<p class="eyebrow">Contractor Sales Pipeline Optimization</p>
```
EYEBROW NEW:
```html
<div class="eyebrow kw-ey"><h1 class="kw-eh">Contractor Sales Pipeline Optimization</h1></div>
```
H1 NOW:
```html
<h1>
```
H2 NEW:
```html
<h2 class="kw-q">
```

## /services/reputation-management-for-contractors/

CSS: `pages/services_reputation-management-for-contractors.css`

EYEBROW NOW:
```html
<p class="eye rev">Reputation Management for Contractors</p>
```
EYEBROW NEW:
```html
<div class="eye rev kw-ey"><h1 class="kw-eh">Reputation Management for Contractors</h1></div>
```
H1 NOW:
```html
<h1 class="rev">
```
H2 NEW:
```html
<h2 class="kw-q rev">
```

## /revenue-leak-finder/

CSS: `pages/revenue-leak-finder.css`

EYEBROW NOW:
```html
<p class="eye">Revenue Leak Finder · free · no form, no email</p>
```
EYEBROW NEW:
```html
<div class="eye kw-ey"><h1 class="kw-eh">Revenue Leak Finder</h1><span class="kw-ex"> · free · no form, no email</span></div>
```
H1 NOW:
```html
<h1>
```
H2 NEW:
```html
<h2 class="kw-q">
```

## /about/

CSS: `pages/about.css`

EYEBROW NOW:
```html
<div class="eb">About Andrew Ryan Marketing</div>
```
EYEBROW NEW:
```html
<div class="eb kw-ey"><h1 class="kw-eh">About Andrew Ryan Marketing</h1></div>
```
H1 NOW:
```html
<h1>
```
H2 NEW:
```html
<h2 class="kw-q">
```

## /services/ppc-for-contractors/

CSS: `pages/services_ppc-for-contractors.css`

EYEBROW NOW:
```html
<p class="eye rev">PPC for Contractors</p>
```
EYEBROW NEW:
```html
<div class="eye rev kw-ey"><h1 class="kw-eh">PPC for Contractors</h1></div>
```
H1 NOW:
```html
<h1 class="rev">
```
H2 NEW:
```html
<h2 class="kw-q rev">
```

## /contractor-growth-marketing/

CSS: `pages/contractor-growth-marketing.css`

EYEBROW NOW:
```html
<p class="eyebrow" style="color:#a9b3c1">Growth Marketing for Established Contractors</p>
```
EYEBROW NEW:
```html
<div class="eyebrow kw-ey" style="color:#a9b3c1"><h1 class="kw-eh">Growth Marketing for Established Contractors</h1></div>
```
H1 NOW:
```html
<h1>
```
H2 NEW:
```html
<h2 class="kw-q">
```

## /services/crm-email-and-automation/

CSS: `pages/services_crm-email-and-automation.css`

EYEBROW NOW:
```html
<p id="brxe-u1c8d5" class="brxe-text-basic eyebrow">CRM, Email &amp; Automation for Contractors</p>
```
EYEBROW NEW:
```html
<div id="brxe-u1c8d5" class="brxe-text-basic eyebrow kw-ey"><h1 class="kw-eh">CRM, Email &amp; Automation for Contractors</h1></div>
```
H1 NOW:
```html
<h1 id="brxe-omgplf" class="brxe-heading sv-h1">
```
H2 NEW:
```html
<h2 id="brxe-omgplf" class="kw-q brxe-heading sv-h1">
```

## /attribution/

CSS: `pages/attribution.css`

EYEBROW NOW:
```html
<p class="aa-eyebrow">Better data. Better decisions.</p>
```
EYEBROW NEW:
```html
<div class="aa-eyebrow kw-ey"><h1 class="kw-eh">Marketing Attribution for Contractors</h1><span class="kw-ex">&nbsp;| Better data. Better decisions.</span></div>
```
H1 NOW:
```html
<h1>
```
H2 NEW:
```html
<h2 class="kw-q">
```

## /contractor-growth-stages/

CSS: `pages/contractor-growth-stages.css`

EYEBROW NOW:
```html
<p class="eye">From the next lead to the next market.</p>
```
EYEBROW NEW:
```html
<div class="eye kw-ey"><div class="kw-in"><h1 class="kw-eh">Contractor Growth Stages</h1><span class="kw-ex">&nbsp;| From the next lead to the next market.</span></div>
```
H1 NOW:
```html
<h1>
```
H2 NEW:
```html
<h2 class="kw-q">
```

## /pricing/

CSS: `pages/pricing.css`

EYEBROW NOW:
```html
<p class="eyebrow">Pricing</p>
```
EYEBROW NEW:
```html
<div class="eyebrow kw-ey"><h1 class="kw-eh">Contractor Marketing Pricing</h1></div>
```
H1 NOW:
```html
<h1>
```
H2 NEW:
```html
<h2 class="kw-q">
```

## /portfolio/

CSS: `pages/portfolio.css`

EYEBROW NOW:
```html
<p class="eyebrow">Website portfolio · 5&nbsp;client builds + our own&nbsp;site</p>
```
EYEBROW NEW:
```html
<div class="eyebrow kw-ey"><h1 class="kw-eh">Website Design Portfolio</h1><span class="kw-ex"> · 5&nbsp;client builds + our own&nbsp;site</span></div>
```
H1 NOW:
```html
<h1 id="pf-h1">
```
H2 NEW:
```html
<h2 class="kw-q" id="pf-h1">
```

## /services/generative-engine-optimization/

CSS: `pages/services_generative-engine-optimization.css`

EYEBROW NOW:
```html
<div class="eyebrow">The biggest budget no longer wins</div>
```
EYEBROW NEW:
```html
<div class="eyebrow kw-ey"><h1 class="kw-eh">Generative Engine Optimization Services</h1><span class="kw-ex">&nbsp;| The biggest budget no longer wins</span></div>
```
H1 NOW:
```html
<h1>
```
H2 NEW:
```html
<h2 class="kw-q">
```

## /case-studies/

CSS: `pages/case-studies.css`

EYEBROW NOW:
```html
<div class="eyebrow"><span class="live"></span> Live revenue-gap instrument</div>
```
EYEBROW NEW:
```html
<div class="eyebrow kw-ey"><span class="live"></span> <h1 class="kw-eh">Contractor Marketing Case Studies</h1></div>
```
H1 NOW:
```html
<h1>
```
H2 NEW:
```html
<h2 class="kw-q">
```

## /free-roi-calculator/

CSS: `pages/free-roi-calculator.css`

EYEBROW NOW:
```html
Free ROI Calculator
    </div>
```
EYEBROW NEW:
```html
<h1 class="kw-eh">Free Marketing ROI Calculator</h1>
    </div>
```
H1 NOW:
```html
<h1>
```
H2 NEW:
```html
<h2 class="kw-q">
```
