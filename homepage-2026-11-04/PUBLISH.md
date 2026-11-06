# Publish the new homepage (approved by Andrew 2026-11-04 17:50Z: "push it live, its good to go")

Source of truth: `build3.js` (the hero rewrite plus the row removal, run against the live page) and `sections.html` (the five new sections). The approved mock = live homepage + exactly this transform.

## Steps (PC session, ARM Local)
1. Back up the homepage. Note the current revision ID as a rollback point in `site-rebuild-sample\fixes\fixes-log.txt`.
2. Hero (row 0, `#rge .rge-panel`): replace the panel contents with the hero markup from `build3.js` (`q.innerHTML`, plus the H1 lockup text and the existing `.adc-hero-wrap` "Talk to Andrew directly" link pointing to Calendly with utm_content=home-hero). Remove the hero calculator (`.armx-s.armx-calc`). Keep the real `<h1>` element. Hero side padding: 96px 40px 80px on desktop, 56px 20px 44px under 700px. `.rge-in` padding 0. Also include the mobile fix for `.adc-hero-link` (display:block, with `b` and `.a` inline under 600px).
3. Remove content rows 2 and up. Keep row 1 and the `#argmRoot` wrapper (the 6-Gap tool, its seven questions and the video request form, including `#argmData`). Move that wrapper into a new `<div id="vr" style="display:none">` placed right after `#start .two`.
4. Add `sections.html` as one Raw HTML row after row 1.
5. Small inline script: the hero "Get my gaps on video" button and the `#start` video button get `href="#vr"`. On click: show `#vr`, click `#argmModeSelf` (the "Score my business" mode), and scroll to `#vr`. "Close the map" hides `#vr` again. The "Book the 20-minute Gap Review" button goes to Calendly gap-review with utm_content=home-close.
6. Don't touch the title, meta description, canonical, H1 text or JSON-LD.

## Verify (logged out, live page in a real browser, 1440 and 390)
- Hero copy, the gap divider and the matching "The problem is:" / "The solution:" labels render. No calculator.
- Exactly 5 `.nh` sections. No leftover old rows, orphaned shortcodes or white gaps.
- The video button opens the seven questions. Answering all seven unlocks the website/email form. Do NOT submit a test unless Andrew says so.
- The Calendly buttons open gap-review.
- No horizontal overflow at 390 or 360.
- If any check fails: restore the backup revision and report.

## 2026-11-06 polish pass (Andrew: "buttons and cards need hover effects")
Append the whole of `polish.html` (one <style id="nh-polish"> + one <script id="nh-polish-js">) to the END of the homepage Raw HTML block that holds the `.nh` sections. No copy changes. If `#nh-polish` already exists, replace it (never duplicate).
The script has no `&&` (WordPress encodes it and kills inline scripts). After saving, check that the served HTML still has no `&#038;&#038;` inside it.
Verify logged out at 1440: hovering a scenario card lifts it 4px with an orange border; hovering a close option lifts it 5px with an orange glow; the buttons lift 2px and brighten; 12 arrows sit in `<span class="arrow">` and slide on hover; there are no page errors. At 390: no layout change and no overflow.
