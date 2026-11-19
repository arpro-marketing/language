# Site header: logo and Menu button on one row on narrow phones

STATUS: PROPOSED. Nothing here is live. Save only when Andrew's own message names it.

## What changes

On phones 361 pixels wide and narrower, the logo and the Menu button sit on one row, the way they already do on wider phones. The header goes back to 69 pixels tall, and the page under it starts 36 pixels higher. No wording changes. Nothing changes at 362 pixels and wider.

Mockup: `header-before-after.png` in this folder (the homepage and the HVAC Google Ads page at 360 wide, now and with the change, and the open menu).

## Why

The header row needs 362 pixels: 20 of margin, 224 for the logo and name, a 20 gap, 78 for the Menu button, and 20 of margin. On a narrower screen the Menu button drops to a second row. The header grows from 69 to 105 pixels, the logo loses its space at the top, and the whole page starts 36 pixels lower.

Measured on the live site on 2026-11-18, logged out, on the homepage, the HVAC hub, the HVAC Google Ads page, About, Pricing, Contact, Case Studies and Insights. All eight wrap at 360 wide. The homepage's logo block is 2 pixels narrower than the others, so it wraps from 360 down and the other seven from 361 down.

360 wide is a common phone size. StatCounter's "Mobile Screen Resolution Stats in United States Of America - October 2026" lists 360x780 fourth, at 4.58%, and that is only one of the 360-wide sizes (read 2026-11-18 at https://gs.statcounter.com/screen-resolution-stats/mobile/united-states-of-america). The site's own analytics will show the real share for its visitors.

This is the shared header, so it is on every page.

## The code

One rule. It belongs with the header's other phone rules, in the custom CSS of the Bricks header template. That looks like template 13191: its stylesheet (`/wp-content/uploads/bricks/css/post-13191.min.css`) carries the phone menu rules and ends with the two `.nav.nav.brxe-div` gap rules. Confirm that before saving. If the header's rules are edited somewhere else, put the rule there and say so in the report.

```css
/* Narrow phones: keep the logo and the Menu button on one row. The row needs 362px. These two gaps give back 10px, and nowrap covers anything narrower. Rollback: delete this rule. */
@media (max-width:361px){#brx-header .hdr-in{flex-wrap:nowrap;gap:12px}#brx-header .logo{gap:10px}}
```

How it works:

- `flex-wrap:nowrap` keeps the Menu button on the logo's row at any width.
- The gap between the logo and the button goes from 20 to 12 pixels, and the gap between the mark and the name from 12 to 10. That gives back 10 pixels, so the name stays on one line from 352 wide up. The side margins stay at 20.
- Below 352 wide the name takes two lines ("Andrew Ryan" over "Marketing") inside the same 69-pixel header.
- `#brx-header` in front makes the rule win over the existing `.hdr-in.brxe-container` and `.logo.brxe-div` rules wherever it loads.

## Tested

2026-11-18, logged out, in a phone-size Chromium window with an Android phone user agent and touch. Each of the eight pages was loaded fresh as it is, and again as a copy with the rule added before `</head>`, then measured at sixteen widths.

| Width | Header height now | With the change | Name |
|---|---|---|---|
| 280 | 105 | 69 | two lines |
| 320 | 105 | 69 | two lines |
| 344 | 105 | 69 | two lines |
| 352 | 105 | 69 | one line |
| 353 | 105 | 69 | one line |
| 360 | 105 | 69 | one line |
| 361 | 105 (homepage 69) | 69 | one line |
| 362, 375, 390, 412, 768, 900, 901, 1024, 1440 | 69 | no change | no change |

On all eight pages, live and copy: no page errors and no sideways scroll at any width.

With the change, at every width that wraps today: the header is 69 pixels tall, the Menu button is on the logo's row with its usual 20-pixel margin and at least 12 pixels from the logo, the logo sits inside the header, and the page heading starts exactly 36 pixels higher.

At 362 and wider every measured value is identical to the live page: header height, logo and button position, lines in the name, menu and button visibility, and heading position.

At 320, 360 and 375 wide the menu was opened and closed on every page, live and copy. It opens directly under the header, shows all 28 links and closes again.

## After saving, check

Logged out, with a cache-buster, at the rendering layer:

1. At 360 wide on the homepage, the HVAC hub, one HVAC spoke and About, the header is 69 pixels tall and the Menu button is on the right of the logo's row.
2. At 362, 375, 390 and 1440 wide the header is exactly as it was.
3. At 360 wide the menu opens under the header, lists every link and closes.
4. No console errors and no sideways scroll.

The test files are in the project files under `site-header-narrow-phones-2026-11-18/verify/`. After the save, `hdrtest.js` in `live` mode must give the same numbers as `ht-fix.txt` (`hdrsame.py` compares them).

## Rollback

Delete the rule and clear the page cache. Nothing else is touched.

## Not in this change

- At 901 wide, the narrowest width that shows the desktop menu, the name takes two lines today. Left as it is.
- The "Message Andrew" bar proposal in `hvac-spokes-2026-11-18/bar-wait/`. Its numbers for 360 by 640 and 320 by 454 were measured with today's header. Once this change is live, pages on those screens start 36 pixels higher, so those two rows have to be measured again before that proposal's check.

## Limits of the test

A phone-size Chromium window is not a phone. The rule is plain CSS that every current phone browser supports, but one look at a 360-wide Android phone after the save is still the last check.
