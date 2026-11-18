# Publish spec: HVAC Call Handling & Estimate Follow-Up spoke (Andrew 11-18 19:32Z: "ship the call handling and estimate spoke")

Same method as the AI Visibility (13720) and PPC pages. Files here: body.html, extra.css (drop the @import line and body/footer font rule, as before), schema.json (Service + FAQPage only; Yoast supplies the single BreadcrumbList after today's bctitle fix), call-handling-mockup.html + jpgs (approved look).

- New page, parent 6515, slug call-handling → https://andrewryanmarketing.com/services/hvac-marketing/call-handling/
- Copy byte-for-byte from body.html. Bricks structure like the other two HVAC spokes (buttons as real button elements).
- SEO title (no suffix): HVAC Call Handling & Estimate Follow-Up → Sold Jobs   (495px, 20px Arial canvas)
- Meta: HVAC call handling and estimate follow-up: answer every call, book the visit, present options and follow up while homeowners decide.   (828px, 14px Arial)
- Yoast breadcrumb title: Call Handling
- WPCode: CSS + schema scoped to this URL. Allowlist 13228; template 13231 exclusion. Not in any menu. Hide Related Articles.
- Subnav: Marketing System → hub, AI Visibility → /services/hvac-marketing/ai-visibility/, Google Ads & LSAs → /services/hvac-marketing/ppc/, Call Handling (current), SEO → /local-contractor-seo-blueprint/, Reviews → /services/reputation-management-for-contractors/, All Services → /services/.
- After it is live: on the AI Visibility and PPC pages change only the subnav "Call Handling" link target from /services/lead-to-booked-job/ to /services/hvac-marketing/call-handling/.

Verify logged out 1440 + 390: 200; one title = og:title; meta; 0 "<!-- /wp:"; 4 details = 4 summary; FAQ toggles; no page errors; JSON-LD parses; exactly one BreadcrumbList (Home › Services › HVAC Marketing › Call Handling); no horizontal scroll; table stacks on phone; record tiles 2x2 on phone; in-body links 200 with no hop; canonical = new URL. Request indexing. Report page id, revisions, rollback, screenshots.
