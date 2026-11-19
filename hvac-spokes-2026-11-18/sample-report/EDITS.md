# HVAC SEO page: example sold-jobs report in step 06

STATUS: LIVE since 2026-11-19 12:05 PM ET. Saved on Andrew's message of 12:02 PM ET: "put the example report and the new sentence in SEO step 06". As-built notes are at the end.

## Scope

One element on one page: the SEO page (13745), /services/hvac-marketing/seo/, step 06 of "How we do SEO for HVAC companies" (element #brxe-hzefla). This is item 5.5 of the review of 2026-11-18, which was left out of the final pass so it could have its own preview and its own yes.

Andrew, 2026-11-18 5:32 PM ET: "I favor your suggestion to show a small, explicitly labeled sample report with source, spend, calls, booked jobs, sold jobs, revenue, and cost per sold job. This makes your differentiator tangible."

Revised 2026-11-19 after Andrew read the first version (11:55 AM ET) and asked for the fall-off from booked jobs to sold jobs to be closer to usual: the Booked jobs column changed from 40, 38 and 37 to 36, 35 and 34. No other figure changed.

Nothing else on the page changes. Step 06 is not part of the FAQ, so the schema snippet (13747) is not touched. No other page changes.

Mockups: `example-report-desktop.png` and `example-report-phone.png` in this folder.

## Word count

The SEO page has 1,115 words now and 1,153 after (+38). The step's sentence gets 8 words shorter (41 to 33). The table adds 46 short entries: a 7-word label, 12 words of column names, 9 words of row names and 18 figures.

## The edit

### Element #brxe-hzefla (step 06)

NOW (live text, logged-out fetch of 2026-11-19 00:17Z). If the element doesn't match this exactly, stop and report instead of editing.
```html
<strong>We measure SEO by sold jobs.</strong> Rankings and traffic are early signs. The report that matters shows the calls that came from Maps and organic search and what they sold, from the numbers in your field software, alongside what you spent.
```
NEW text:
```html
<strong>We measure SEO by sold jobs.</strong> Rankings and traffic are early signs. The report that matters follows each source from the call to the sold job, using the numbers in your field software.
```
The sentence that listed the report's contents in words is replaced by one that introduces the table, because the table now shows those contents.

Then the table, inside the same step card, directly under the sentence:
```html
<div class="hv-rep">
<span class="hv-k">Illustrative one-month example, not a client result</span>
<table class="hv-report" role="table" aria-label="Illustrative example of a one-month sold-jobs report by source">
<thead role="rowgroup"><tr role="row"><th role="columnheader" scope="col">Source</th><th role="columnheader" scope="col">Spend</th><th role="columnheader" scope="col">Calls</th><th role="columnheader" scope="col">Booked jobs</th><th role="columnheader" scope="col">Sold jobs</th><th role="columnheader" scope="col">Revenue</th><th role="columnheader" scope="col">Cost per sold job</th></tr></thead>
<tbody role="rowgroup">
<tr role="row"><th role="rowheader" scope="row">SEO <small>Maps and organic</small></th><td role="cell">$2,500</td><td role="cell">58</td><td role="cell">36</td><td role="cell">28</td><td role="cell">$31,250</td><td role="cell">$89</td></tr>
<tr role="row"><th role="rowheader" scope="row">Search ads</th><td role="cell">$4,800</td><td role="cell">60</td><td role="cell">35</td><td role="cell">25</td><td role="cell">$44,500</td><td role="cell">$192</td></tr>
<tr role="row"><th role="rowheader" scope="row">Local Services Ads</th><td role="cell">$2,800</td><td role="cell">56</td><td role="cell">34</td><td role="cell">27</td><td role="cell">$23,750</td><td role="cell">$104</td></tr>
</tbody>
</table>
</div>
```
The rendered step must be the sentence followed by `div.hv-rep`, both inside the step's own `li`, so the table sits in the grey card under the 06. Use whatever Bricks mechanics give that result. If the table can't sit inside the step's own card, stop and report instead of placing it somewhere else.

The `role` attributes stay. On phones the CSS turns the table on its side with `display:grid` and `display:contents`, and the roles keep it a table for screen readers.

### CSS, added to WPCode 13748
```css
.hv-rep{margin:16px 0 4px}
.hv-rep .hv-k{display:block;font-size:13px;font-weight:700;color:#666;margin:0 0 8px;text-wrap:balance}
.hv-report{width:100%;border-collapse:collapse;background:#fff;font-family:"DM Sans",ui-sans-serif,system-ui,sans-serif;font-size:15px;line-height:1.35;color:#333;font-variant-numeric:tabular-nums;border:1px solid #E0E0E0}
.hv-report th,.hv-report td{padding:12px 14px;text-align:right;vertical-align:middle;border-bottom:1px solid #E0E0E0;white-space:nowrap}
.hv-report thead th{background:#333;color:#fff;font-weight:600;font-size:14px;line-height:1.3;white-space:normal;vertical-align:bottom}
.hv-report th:first-child{text-align:left}
.hv-report tbody th{font-weight:700;white-space:normal}
.hv-report tbody th small{display:block;font-size:13px;font-weight:400;color:#666}
.hv-report tbody tr:last-child th,.hv-report tbody tr:last-child td{border-bottom:0}
.hv-report td:last-child{background:#FDF0EB;font-weight:700}
@media (max-width:767px){
 .hv-rep{margin-left:-40px}
 .hv-report{display:grid;grid-template-columns:minmax(0,1.1fr) repeat(3,minmax(0,1fr));grid-template-rows:repeat(7,auto);grid-auto-flow:column;font-size:15px}
 .hv-report thead,.hv-report tbody,.hv-report tr{display:contents}
 .hv-report th,.hv-report td{display:flex;align-items:center;justify-content:flex-end;padding:10px 6px;white-space:normal;text-align:right;border-bottom:1px solid #E0E0E0}
 .hv-report thead th{background:#fff;color:#333;font-size:13px;font-weight:600;line-height:1.3;justify-content:flex-start;text-align:left}
 .hv-report thead th:first-child{background:#333;color:#fff}
 .hv-report tbody th,.hv-report tbody th:first-child{background:#333;color:#fff;font-size:13px;line-height:1.25;flex-direction:column;align-items:stretch;justify-content:flex-end;text-align:right}
 .hv-report tbody th small{color:#E0E0E0;font-size:12px}
 .hv-report thead th:last-child{background:#FDF0EB;font-weight:700}
 .hv-report tbody tr:last-child th,.hv-report tbody tr:last-child td{border-bottom:1px solid #E0E0E0}
 .hv-report thead th:last-child,.hv-report tbody tr td:last-child,.hv-report tbody tr:last-child td:last-child{border-bottom:0}
}
@media (max-width:379px){
 .hv-report{font-size:14px}
}
@media (max-width:339px){
 .hv-report{grid-template-columns:repeat(4,minmax(0,1fr));font-size:13px}
 .hv-report th,.hv-report td{padding:9px 4px}
 .hv-report thead th,.hv-report tbody th,.hv-report tbody th:first-child{font-size:12px}
 .hv-report tbody th small{font-size:11px}
}
```
The look follows the table already on this page (`.hv-table`): white on the grey card, a #333 header, #E0E0E0 rules and the #FDF0EB tint on the last column. The label uses the style of the result card's label under it (`.hv-result .hv-k`).

On phones (767px and under, the same breakpoint the step cards use) the table turns on its side: the three sources run across the top and the seven measures run down, so the three figures for each measure sit side by side with no sideways scroll. `.hv-rep{margin-left:-40px}` pulls the table out under the step number, which leaves 18px on both sides of the card.

## Where the numbers come from

Every figure is an example, and the label says so. They are built to agree with what the HVAC pages already say:
- Prices are the Google Ads page's example prices: $350 a repair and $7,500 a system.
- Search ads is that page's second account: 60 leads at $80 = $4,800, and 5 replacements + 20 repairs = 25 sold jobs and $44,500.
- Local Services Ads uses that page's other price per lead: 56 leads at $50 = $2,800, and 2 replacements + 25 repairs = 27 sold jobs and $23,750.
- SEO: $2,500 is the top of the range the hub gives for focused SEO work ("$1,500–2,500 a month"), and 3 replacements + 25 repairs = 28 sold jobs and $31,250.
- Booked jobs (36, 35 and 34) are worked out from each row's own job mix, using two published rates: repair calls close at 85% or better, and replacement estimates close at a little over 40%.
  - SEO: 29 repair calls sell 25 repairs, and 7 estimates sell 3 systems. 36 booked, 28 sold (78%).
  - Search ads: 23 repair calls sell 20 repairs, and 12 estimates sell 5 systems. 35 booked, 25 sold (71%).
  - Local Services Ads: 29 repair calls sell 25 repairs, and 5 estimates sell 2 systems. 34 booked, 27 sold (79%).
  - Sources, read 2026-11-19: ServiceTitan's contractor playbook lists "Closed calls ≥ 85%" as the benchmark for an HVAC service technician (a target, not a measured average). ACHR News, Feb 10 2026, on a survey of more than 1,000 contractors by ACCA and Farmington Consulting Group: "Contractors are closing 43% of their install jobs", 45% in residential. The hub's own example uses 40%.
  - Calls to booked comes out at 62%, 58% and 61%. ServiceTitan's data from more than 3,000 shops (June 2022) put HVAC at 38% of calls booked and shops with 25 or more techs at 59%.
- Cost per sold job is spend ÷ sold jobs, rounded to the dollar: 2,500 ÷ 28 = 89, 4,800 ÷ 25 = 192, 2,800 ÷ 27 = 104.
- The SEO row has the lowest cost per sold job because the page already says so in words: "For an established company, it’s usually the channel that brings cost per sold job down over time."

## Checks after the save (logged out, with a cache-buster)

1. Step 06 reads exactly as NEW, and the label reads exactly "Illustrative one-month example, not a client result".
2. The table has the seven column names in this order and three rows with exactly these figures.
3. At 1440 wide: the table sits inside the step card, 24px from the card's right edge, with the column names on one line.
4. At 390 and 360 wide: the table is turned on its side, there is no sideways scroll, no figure touches its neighbour, and the table sits 18px from both edges of the card.
5. No other element on the page changed, and the page count is 1,153 words.
6. No console error on load.

Checked on a copy of the live page in a browser before this file was written: 1440, 1280, 1024, 820, 768, 430, 412, 390, 375, 360 and 320 wide, with no sideways scroll and no clipped or touching cell at any of them.

## Rollback

The page's version before the save. One element and one CSS block, so putting back the NOW text and removing the `.hv-rep` and `.hv-report` rules also undoes it.

## As built (2026-11-19)

- Saved at 12:05 PM ET from commit 75095db, the version with Booked jobs at 36, 35 and 34.
- Page 13745: the text setting of the step's own element (#brxe-hzefla, a Basic Text `li`) now holds the NEW sentence followed by `div.hv-rep`. No element was added, so the page still has 117 elements. Revision 13765 before, 13776 after.
- WPCode 13748: the CSS above was added at the end under the comment `/* sample report 2026-11-19 */`. The snippet went from 4,589 to 7,117 characters. The schema snippet (13747) was not touched.
- Checked from the cloud, logged out with a cache-buster:
  - `verify/check.py` against the copy fetched at 11:38 AM ET: 29 of 29. Only #brxe-hzefla changed, the markup equals this spec, every role and scope attribute survived the save, the other CSS is unchanged, and the page went from 1,115 to 1,153 words.
  - `verify/live.js` in a browser at 1440, 390 and 360 wide: 54 of 54. No sideways scroll, nothing above the step moved, everything below it moved by the same amount (219px on desktop, about 355 to 360px on phones), the table sits 24px from the card's right edge on desktop and 18px from both edges on phones, and there is no new console error.
- Re-read from a copy fetched at 12:19 PM ET: the label, the three rows and the sentence match this spec.
- Rollback on the PC: `hvac-spokes-2026-11-18\sample-report\ROLLBACK.txt` (page revision 13765 and the prior code of snippet 13748).

