# Homepage final polish — Nov 4, 2026 (preview only, nothing live)

## What changed
1. **Founder H2:** "Our founder built a sales department from scratch. Then made it run without him." (Andrew's wording). Body: "built the Business Development Center (BDC) from nothing: the processes, the follow-up systems, and the tracking from first lead to sold deal." Stats and the "Not a client result" attribution are unchanged.
2. **Transition into founder section:** no copy added. The eyebrow "Why we measure to the booked job" and the line "That's the work we do for contractors" already bridge from the scenarios to the record.
3. **Consequence table (≤820px):** still stacked by scenario, and now keeps the orange-tinted "So you" box on mobile. Labels went from 11px to 12px. No horizontal scroll.
4. **$144,000:** "closing one more percentage point of your 60 shown appointments a month … $20,000 average job." Math line: "60 shown appointments × 1 point = 0.6 more sold jobs a month, or 7.2 a year. 7.2 × $20,000 = $144,000 a year in booked revenue, before costs. Illustrative, not a client result." Checked: 60 × 0.01 = 0.6; × 12 = 7.2; × 20,000 = 144,000.
5. **Hero:** no wording changes. On phones the "Already know where it's leaking? Talk to Andrew directly →" line was split into cramped columns by the site's flex style; it now reads as one line. Hero side padding now lines up with the sections at 768/390/360. The 360px hero overflow is fixed.
6. **Close CTAs:** "Book the 20-minute Gap Review" → Calendly gap-review (utm_content=home-close). Hero "Talk to Andrew directly" → Calendly (home-hero). "Get my gaps on video" → see open item. Button text fits better at ≤400px.
7. **Spacing:** section side padding is 40px on tablet/desktop (it was 20px, which looked flush at 1024/768). Link rows no longer break mid-name ("CRM & / Automation").
8. **Links:** all 24 internal links return 200 except /local-seo-results/, which 301s to /case-studies/. It now links to /case-studies/ directly.

## QA (Playwright, fresh logged-out loads of live page + mock transform)
1440 / 1024 / 768 / 390 / 360: no horizontal overflow at any width. Small text appears only in uppercase eyebrows and labels (12–13px). Title, meta description, canonical, the H1 element and JSON-LD come from the live page untouched.

## Open items before production
- **Video CTA destination (blocker):** the live video request (seven questions + website/email, video in 48h) exists only inside the homepage 6-Gap Map block, which this design removes. /6-gap-revenue-map/ has no request form. The mock points the button at /6-gap-revenue-map/. The form needs a home before launch.
- Existing site header at 360px wraps the Menu button to a second line (not part of this page; same on live).
