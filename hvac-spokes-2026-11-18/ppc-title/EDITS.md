# HVAC Google Ads page: "PPC" in the title

STATUS: PROPOSED 2026-11-19. Not live. It waits for Andrew's yes (asked in the thread on 2026-11-19 at 11:17 AM ET). Do not save anything from this file until his own message approves it.

## Why

The page's planned first term is "hvac ppc services". Today "PPC" is in the page's web address, one section heading, the sentence under it and one outbound link. It is not in the title or the main heading, and no link on the site points to the page with the word.

## Edit 1: SEO title, page 13726 (/services/hvac-marketing/ppc/)

NOW:
HVAC Google Ads & LSAs → Bid on Installs, Not Clicks

NEW:
HVAC PPC & Google Ads → Bid on Installs, Not Clicks

- Width in 20px Arial: 493px now, 486px new. The limit we work to is 510px.
- Where: the Yoast SEO title field of page 13726. No custom social title. The share title must follow the SEO title, as on every page.
- Do not change: the H1, the meta description, the slug, the breadcrumb label, the sub-nav label, the structured data or any body text.

## Edit 2: hub 6515, services card 01 link text

NOW (inside `div#svp1.tp`):
`<a class="tl" href="/services/hvac-marketing/ppc/">Google Ads <span class="ar">→</span></a>`

NEW:
`<a class="tl" href="/services/hvac-marketing/ppc/">HVAC PPC <span class="ar">→</span></a>`

- Only the two words change. It matches card 02's `HVAC SEO →`.
- The hub's other two links to the page ("Google Ads" and "Local Services Ads" in the first-funnel box) stay as they are.

## Before saving

Stop and report if either NOW does not match the live page. Note the version of each page before the save, for rollback.

## Checks after the save

Run logged out against a fresh copy of each page.

- /services/hvac-marketing/ppc/: `<title>` and `og:title` both equal NEW, and the WebPage name in the structured data equals NEW. The H1, description, canonical, FAQ structured data and word count are unchanged. Nothing else differs from the copy taken before the save.
- /services/hvac-marketing/: the card 01 link reads `HVAC PPC →` at 1440, 390 and 360 wide, with no wrap inside the link. Nothing else differs from the copy taken before the save, and the word count is unchanged.

## Second choice

Only if Andrew picks it instead: `HVAC PPC Services → Google Ads & LSAs, No Markup` (500px). Edit 2 is the same.
