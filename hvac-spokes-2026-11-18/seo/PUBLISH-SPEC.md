# Publish spec: HVAC SEO spoke (Andrew 11-18 19:38Z: "ship the seo page plz")

Same method as the AI Visibility (13720) and PPC pages. Files here: body.html, extra.css (drop the @import line and body/footer font rule, as before), schema.json (Service + FAQPage only; Yoast supplies the single BreadcrumbList after today's bctitle fix), seo-mockup.html + jpgs (approved look).

- New page, parent 6515, slug seo → https://andrewryanmarketing.com/services/hvac-marketing/seo/
- Copy byte-for-byte from body.html. Bricks structure like the other two HVAC spokes (buttons as real button elements).
- SEO title (no suffix): HVAC SEO Services → Rank in Maps & Book More Jobs   (506px, 20px Arial canvas)
- Meta: HVAC SEO measured to sold jobs: Google Business Profile, reviews, a page for each service you sell and local links, not thin city pages.   (846px, 14px Arial)
- Yoast breadcrumb title: SEO
- WPCode: CSS + schema scoped to this URL. Allowlist 13228; template 13231 exclusion. Not in any menu. Hide Related Articles.
- Subnav: Marketing System → hub, AI Visibility → /services/hvac-marketing/ai-visibility/, Google Ads & LSAs → /services/hvac-marketing/ppc/, Call Handling → /services/hvac-marketing/call-handling/, SEO (current), Reviews → /services/reputation-management-for-contractors/, All Services → /services/.
- After it is live: on the AI Visibility, PPC and Call Handling pages change only the subnav "SEO" link target from /local-contractor-seo-blueprint/ to /services/hvac-marketing/seo/.

Verify logged out 1440 + 390: 200; one title = og:title; meta; 0 "<!-- /wp:"; 4 details = 4 summary; FAQ toggles; no page errors; JSON-LD parses; exactly one BreadcrumbList (Home › Services › HVAC Marketing › SEO); no horizontal scroll; table stacks on phone; in-body links 200 with no hop; canonical = new URL. Request indexing. Report page id, revisions, rollback, screenshots.
