# Keyword H1s: homepage

STATUS: approved, not yet live. Andrew asked for this in the thread on 2026-11-19 at 1:00 PM ET:

> "no i think keeping the smaller eyebrow as; 'contractor marketing agency | seo, google ads & growth' would work fine while making 'contractor marketing agency' the h1"

and, from the plan he pasted and agreed to: "the larger 'Do you feel disconnected from your marketing?' becomes the H2 while retaining its current visual styling ... preserves the existing desktop and mobile styling and verifies that the homepage has only one H1."

Other pages are NOT in this file and are not approved. They come as a separate proposal.

## Page

Homepage, page 2762. Only the hero markup below and one CSS block. Nothing else on the page changes.

## Change 1: hero markup (inside `div.hp-hero div.hp-wrap`)

NOW (exactly as the page prints it, fetched logged out 2026-11-19 1:05 PM ET):

```html
<div class="hp-eyebrow" style="text-wrap:balance">SEO, Google Ads &amp; Growth Systems for Contractors</div>
<h1>Do you feel <em>disconnected</em> from your marketing?</h1>
```

NEW:

```html
<div class="hp-eyebrow" style="text-wrap:balance"><h1 class="hp-eh1">Contractor Marketing Agency</h1><span class="hp-eyx">&nbsp;| SEO, Google Ads &amp; Growth</span></div>
<h2 class="hp-q">Do you feel <em>disconnected</em> from your marketing?</h2>
```

The `&nbsp;` before the bar is deliberate: on phones the eyebrow wraps to two lines (it does today too), and this keeps the bar at the end of line one instead of starting line two. The eyebrow stays uppercase through its existing CSS; type the words in the case shown.

If the stored markup has whitespace or line breaks between these tags, keep them; only the tags, classes and eyebrow text change. If the NOW text is not found exactly once, stop and report.

## Change 2: CSS (append to the same style block the hero rules live in, i.e. next to `.hp-hero h1{color:#fff!important}`)

Copy from `homepage.css` in this folder:

```css
.home .hp-hero .hp-eyebrow h1.hp-eh1{display:inline;margin:0!important;padding:0;font:inherit;font-family:inherit!important;letter-spacing:inherit;line-height:inherit;text-transform:inherit;color:inherit!important;text-wrap:inherit}
.hp-hero h2.hp-q{font-family:"Plus Jakarta Sans",sans-serif;font-weight:800;color:#fff;font-size:clamp(36px,5vw,60px);line-height:1.05;letter-spacing:-1.4px;margin-bottom:18px}
.hp-hero h2.hp-q em{font-style:normal;color:#EF662F}
@media (max-width:600px){.hp-hero h2.hp-q{margin-bottom:12px}}
```

Why each rule: the page has an unscoped `h1{font-size:clamp(36px,5vw,60px);color:#EF662F;...}` rule, `.home h1{font-family:Plus Jakarta Sans !important}` and `.hp-hero h1{color:#fff!important}`. The first CSS line stops all three from touching the eyebrow H1. The other three lines give the H2 exactly what the old H1 got from those rules. Do not remove the old h1 rules.

## Tested before saving (cloud, simulated on the live page code)

Rendered the live homepage code with and without the change in Chromium at 1440x900 and 390x844 and compared computed styles. Identical for the eyebrow, the big headline (font family, size, weight, line height, letter spacing, color, margins, box position and size), the orange word, the subhead and the hero button. The eyebrow H1 renders in DM Sans like the rest of the eyebrow. Exactly one H1 on the page.

## How to save

Record the current revision for rollback, make the two changes, save, purge the homepage cache, fetch the homepage logged out with a cache-buster and confirm: one `<h1>` in the page, its text is "Contractor Marketing Agency", the `h2.hp-q` is present, and the old eyebrow text is gone. Report the new revision number.

## Rollback

Restore the revision recorded before the save.
