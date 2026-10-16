# Ship spec: electrician hub v2 (page 6597, /services/marketing-for-electricians/)

Approved by Andrew on 2026-10-16: commercial out; one company per market applies; "build it for now". Ship only after Andrew types a line naming this change.

1. Back up page 6597 content.raw, the Yoast title and meta, and note the current revision id.
2. Replace the page content with one row per file, in MANIFEST.md order (e00 to e23). Each eNN.html goes into its own Raw HTML element in its own row, except e09-row.html: copy that 6-Gap Revenue Map row exactly as it exists on the window and door page (page 7107) and place it directly under e08.
3. Row settings as on page 7107: rows after the hero are "Stretch row and content (no padding)", row margin-top -35px, Raw HTML element margin-bottom -20px. If REST saves can't regenerate vc_custom CSS, put the geometry in block CSS via .vc_row:has(...), as done for the window and door blocks.
4. Remove every v1 row: old hero, image rows, v1 FAQ, "Why Electricians Choose", the 800+ keywords bar, the services list, "What we do differently", the industries grid, the Locations section, and the v1 form. Keep the slug.
5. Yoast title: Electrician Marketing Agency → Measured to the Booked Job
   Yoast meta: Electrician marketing for contractors who sell panels, generators and rewires. See what one more sale in ten estimates is worth to you →
   Remove any old FAQPage/Service schema from Yoast or elsewhere on the page so only e22's graph remains (no duplicate FAQPage).
6. Purge cache. Verify logged out with ?v= at 1440 and 390: one h1 ("Electrician Marketing Agency"); hero tool shows $151,680 on load and teaser equals result; chips give $488,884 and $711,000; meter defaults $90/26%, $252/16%, $252/5%; accordion part 1 open; FAQ, stage tabs and the 6-Gap open/close work; no horizontal scroll at 390; no "window"/"door" text; no orphaned shortcodes; no console errors; rendered <title> measures under 600px.
7. Roll back from the backup if any check fails.

Previews: /mnt/project-files/elec-research-2026-10-16/preview/ (cloud project files).

## Meter fix (2026-10-16, after v2 went live)
Replace only the cost meter block (the raw HTML block holding `id="elmeter"`) with the current e13.html. Nothing else on the page changes.
- Removes the theme's inner up/down arrows (Formstone) so each input has one −/+ pair.
- Removes the theme `.row` clearfix pseudo-elements that took the first grid cell, so the three inputs sit in one row (one column under 620px).
- Estimates sold stays fully visible; on Service call it shows "Not used for service calls: booked is sold." under the box.
Verify logged out at 1440 and 390: one −/+ pair per input, three inputs in one row at 1440, defaults $90/26%, panel $252/16%, generator $252/5%, no sideways scroll.
