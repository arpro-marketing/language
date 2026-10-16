# Electrician hub v2: WPBakery blocks (page order)

Spec: /mnt/project-files/elec-research-2026-10-16/electrician-hub-v2-draft.md. Source blocks: ../wd-blocks/bNN.html (live window and door hub).
Each eNN.html is the inner HTML of one Raw HTML element, one per row. Row settings as on the window and door hub: every row after the hero is "Stretch row and content (no padding)", row margin-top -35px, Raw HTML element margin-bottom -20px. The hero row sets its own geometry (-20px desktop, -30px at 991px and below, via .vc_row:has(...)).

| File | Spec section | From | Notes |
|---|---|---|---|
| e00.html | 1 Hero + 2 Hero tool | b00 | H1 eyebrow "Electrician Marketing Agency"; button to #eldiag. Tool: kicker, 3 job chips, sliders 79/1600/35.6 (ranges 10-400, $300-$25,000, 5-80%), teaser and result both from value(), opened line, fine print. Lift slider, "How this is calculated" and "That's how much..." line dropped (not in spec). |
| e01.html | shared CSS | b01 | .arm-wd renamed .arm-el; otherwise unchanged. |
| e02.html | 3 Operator stat bar | b02 | Unchanged except class rename. |
| e03.html | 4 Direct answer | b03 | |
| e04.html | 5 Sub-nav | b04 | Electrician: Marketing System (current) · Lead to Booked Job · New Markets · Reviews · All Services. |
| e05.html | 6 Four numbers | b05 | |
| e06.html | 6 CTA line | b06 | data-scroll="eldiag". |
| e07.html | 7 Job mix (new) | b05 card classes | id="job-mix"; six cards, no commercial card. |
| e08.html | 8 6-Gap band | b07 | Eyebrow/H2/sub per spec; "a composite window & door company" became "a composite company"; instrument numbers and labels unchanged. ids sixgap-el / eldiag. |
| e09-row.html | 8 (diagnostic) | W&D row vc_custom_wd8 | NOT a Raw HTML block: the shared 6-Gap Revenue Map text-block row copied from the live window and door page (holds #argmRoot). In WPBakery, copy that row from the W&D page and place it directly under e08. Included here so the preview's "Open the 6-Gap Revenue Map" works. |
| e10.html | 9 Three ways | b09 | 01 to #job-mix, 02 /services/lead-to-booked-job/, 03 /contractor-growth-marketing/. |
| e11.html | 10 Capacity (new) | b03 .dab card in a .wash section | "Not yet." bold. |
| e12.html | 11 Seven parts | b10 | Part 1 open on load. Spec has no in-body links, so the W&D links are gone. |
| e13.html | 12 Cost meter | b11 (rebuilt) | CPL $39, booked 43.4%, sold 35.6%; job toggle Service call $351 / Panel upgrade $1,600 / Standby generator $5,157. |
| e14.html | 12 Button | b12 | Strip with the button only (spec gives no CTA line here). |
| e15.html | 13 Spend by stage | b13 | Four tabs + Timing + question. |
| e16.html | 14 Proof | b14 | Gregg Murray review removed; two anonymized results. |
| e17.html | 15 Comparison | b15 | "One electrical company per market..." approved, marker dropped. |
| e18.html | 16 Who it's built for | b16 | Links /contractor-growth-marketing/ and /services/seo-johnson-city-tn/ (W&D href). |
| e19.html | 17 FAQ (8) | b17 | |
| e20.html | 18 Final CTA | b18 | Spec copy only (book link, contact link, north line and forward links dropped). |
| e21.html | page JS | b19 | __armElInit; reveal, accordions, meter, stage tabs, data-scroll="eldiag". ASCII-only, no && operators. |
| e22.html | schema | b20 | Service + BreadcrumbList + FAQPage (8, text identical to the visible FAQ). No Article/HowTo/DefinedTerm. |
| e23.html | count-up | b21 | Unchanged logic. |

Not used: b08 (two funnels, not in spec).
