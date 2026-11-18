# Publish spec: HVAC AI Visibility spoke (Andrew 11-18 19:11Z: "looks good, ship it")

Files (this folder): body.html (page content, built on the W&D SEO spoke classes), extra.css (scoped styles; the @import DM Sans line and the body/footer font rules are mockup-only, drop them if the live theme already loads DM Sans), schema.json, ai-visibility-mockup.html + jpgs (approved look).

- New WordPress PAGE, parent = 6515 (HVAC hub), slug ai-visibility → https://andrewryanmarketing.com/services/hvac-marketing/ai-visibility/
- Build in Bricks to match the approved mockup exactly (same pattern as /services/window-and-door-marketing/seo/: spoke-hero with breadcrumb, H1, byline, spoke-lead, spoke-sub, button; subnav bar; bands). Copy is byte-for-byte from body.html. No copy changes.
- SEO title (Yoast, no suffix): AI Visibility for HVAC → Who ChatGPT Recommends   (475px, 20px Arial canvas)
- Meta description: About 6 in 10 HVAC companies AI named weren’t in Google’s top results. See what ChatGPT and Google AI look for, from our 2026 study.   (857px, 14px Arial)
- Share title = SEO title (no custom Yoast share title). Yoast schema page type: WebPage; add schema.json as one JSON-LD block (BreadcrumbList with the hub as parent, Service, FAQPage = the 5 visible FAQs exactly).
- Gotchas (trade-spoke-build-gotchas): add the URL to the Bricks path allowlist on page 13228; exclude it from template 13231 page frame if it is Bricks-built; no .postid CSS; no Redirection duplicates; not in any menu; hide "Related Articles".
- Subnav label "HVAC": Marketing System → /services/hvac-marketing/, AI Visibility (current), Google Ads & LSAs → /services/ppc-for-contractors/, Call Handling → /services/lead-to-booked-job/, SEO → /local-contractor-seo-blueprint/, Reviews → /services/reputation-management-for-contractors/, All Services → /services/.
- Close button → https://calendly.com/andrew-andrewryanmarketing/gap-review?utm_source=arm-site&utm_medium=cta&utm_campaign=site&utm_content=hvac-ai-close

Verify logged out at 1440 and 390 (full-page screenshots, look strip by strip): one <title> and one og:title matching; meta shows; zero "<!-- /wp:" markers; 5 <details> = 5 <summary>; FAQ opens/closes; no console page errors; JSON-LD parses; no horizontal scroll at 390; comparison table stacks into cards on phone; all in-body links return 200 with no 301 hop; canonical is the new URL.
Do NOT touch the hub (6515) or any other page in this step. Request indexing in GSC (/u/2) after it checks out.
Report: page id, revision, screenshots, any check that failed.
