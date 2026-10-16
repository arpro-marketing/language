# W&D ship list — approved by Andrew 2026-10-16 17:03Z ("ship them all")

Approved items: A1, A2, A3, B1, B2, B3, B4, B5 exactly as below. Nothing else.
Back up each page's content.raw before saving. Verify each page logged out at 1440 and 390 after saving. Restore that page's backup if any check fails.

## Hub — /services/window-and-door-marketing/ (page 7107)

A1. Insert `wd-three-ways.html` (this folder) as ONE new top-level row directly after the row that contains `<section class="arm-tfs" id="two-funnels-wd"`:
`[vc_row][vc_column][vc_raw_html]<encoded block>[/vc_raw_html][/vc_column][/vc_row]`
Encode like the page's other raw_html blocks (URL-encoded, then base64). Pre-check: page contains zero `id="three-ways-wd"`.
Verify: one #three-ways-wd between #two-funnels-wd and #system; three cards; one "Uncover Your Revenue Gap" button under the cards scrolls to #wddiag; card 01 scrolls to #system; no sideways scroll at 390.

A2. In the block containing `id="two-funnels-wd"`, delete the one paragraph `<p class="arm-tfs__note">…</p>` (starts "Nobody buys replacement windows off a website"). Keep everything else in that block.

A3. In "The seven parts" section (`id="system"`), make the FIRST `.layer` render open on page load, in the same state a click produces (its `button.hd` aria-expanded="true" plus whatever open class the section's script toggles). Other rows stay closed. Verify the first row is open on load at 1440 and 390 and still toggles closed on click.

## Blog posts (site-wide)

B1. Add this CSS to the site's existing site-wide CSS snippet (the same place other site-wide fixes live), or a new site-wide snippet if none fits:
```
@media (max-width:991px){ body.single-post #content-wrapper{ padding-top:28px !important; } }
```
Verify on /window-and-door-lead-generation/ at 390: H1 top is below the fixed header (header ~70px). Desktop 1440 unchanged.

## Lead gen post — /window-and-door-lead-generation/ (post 9488)

B2. Under the H2 "Window & Door Lead Generation by Market", replace the paragraph that starts "Window and door replacement is driven by housing age" (the one with the 9 city links + "many other Southeast cities") with:
```
<p>Window and door replacement is driven by housing age, climate and energy costs. Markets with older housing stock and hard weather see the most demand, and every one of them is some window company’s next market. We build lead generation for window and door companies nationwide, and before you open a new town we <a href="/contractor-growth-marketing/">model the cost per installed job there</a>.</p>
```
H2 unchanged.

B5. Directly after the "What this page covers" box, insert:
```
<p style="margin:24px 0 8px;"><a href="/services/window-and-door-marketing/#wddiag" style="display:inline-block;background:#EF662F;color:#fff;text-decoration:none;font-weight:700;font-size:17px;line-height:1.3;padding:16px 30px;border-radius:8px;">Uncover Your Revenue Gap →</a></p>
```

## All three W&D spokes — lead gen (9488), /seo-for-window-and-door-companies/, /ppc-for-window-and-door-companies/

B3. Change the link text "Window and Door Contractor Marketing: The Complete Guide" to "Window & Door Contractor Marketing Agency: The Full System". Same href.

B4. In the `.arm-related-grid` image-card grid: delete the card titled "Window and Door Contractor Marketing — Build Predictable Growth" (it duplicates the hub card), and retitle the card "Marketing for Window & Door Companies to Get More Customers" to "Window & Door Contractor Marketing Agency". Same href and image.
If the grid is not in the post content (theme or a shared snippet), report where it lives before changing it.
