# Trade hubs and homepage: the "Message Andrew" bar waits for the hero's main button on phones

STATUS: PROPOSED on 2026-11-19. Not approved and not live. Do not save any part of this until Andrew's own message asks for it.

This is the follow-on to `hvac-spokes-2026-11-18/bar-wait/EDITS.md`, which has been live on the four HVAC spoke pages since 2026-11-19 12:45 PM ET as WPCode snippet 13785. That file explains the method in full. This one applies the same method to eight more pages.

## What changes

On phones, on the homepage and the seven trade hubs, the "Message Andrew" bar stays hidden until the hero's main button ("Let's talk about your marketing →") is clear of it. Then it shows exactly where and how it shows today. If the reader scrolls back to the top, it waits again.

Nothing changes on a phone screen tall enough that the bar doesn't touch that button, and nothing changes on tablets or desktop. No wording changes, so the word counts stay as they are.

The bar never waits once the chat has been opened, or when a conversation is already under way, so this rule never hides a chat in progress.

Mockup: `hubs-before-after-390x664.png` in this folder (the roofing hub and the HVAC hub on a 390 by 664 screen: now, with the change, and with the change after a short scroll).

## Why

On a phone the bar is fixed to the bottom of the screen: 58 pixels tall, 14 pixels up, almost the full width. On short phone screens that is where the hero's main button sits. Measured on the live pages on 2026-11-19, before any scrolling:

- 390 by 664: the bar covers the whole button on the roofing and electrician hubs. On the HVAC and flooring hubs the bar covers the top 25 pixels of the button and the screen edge cuts off the bottom, so 14 pixels of it show. The fencing hub is the same with 14 pixels covered. On the remodeling and window and door hubs only the top edge of the button is on screen (4 and 12 pixels), and the button passes under the bar as the reader scrolls.
- 402 by 681: the bar covers the whole button on the fencing hub, 47 of its 51 pixels on the window and door hub, 43 on the HVAC and flooring hubs, and 19 on the roofing and electrician hubs.
- 390 by 745: the bar covers 36 of the button's 50 pixels on the remodeling hub and 28 on the window and door hub.
- Homepage: the button is clear at 390 wide and wider. At 375 by 635 the bar covers 6 of its 53 pixels, and at 360 by 640 it covers 50 of them.

Across the eleven phone-size screens tested, the bar is on the main button before any scrolling on 29 of the 88 page-and-size pairs. On another 32 the button starts below the bar or below the screen and passes under the bar on the way up.

390 by 664 and 393 by 659 are the sizes standard iPhones have reported in Safari with its bars showing, and 375 by 635 the older 375-wide ones. The exact size depends on the phone and the iOS version, so read these as "short phone screens", not as a list of models.

## Pages

| Page | Address | Page ID |
|---|---|---|
| Homepage | `/` | 2762 |
| Roofing hub | `/services/roofing-marketing/` | 6525 |
| Electrician hub | `/services/marketing-for-electricians/` | 6597 |
| HVAC hub | `/services/hvac-marketing/` | 6515 |
| Flooring hub | `/services/flooring-company-marketing/` | 7131 |
| Fencing hub | `/services/fencing-company-marketing/` | 7150 |
| Remodeling hub | `/services/remodeling-contractor-marketing/` | 7071 |
| Window and door hub | `/services/window-and-door-marketing/` | 7107 |

No other page changes. The four HVAC spoke pages keep snippet 13785 exactly as it is.

## The code

One new WPCode snippet (HTML, footer), limited to these eight pages by its own page rules. It is separate from 13785 so that each can be switched off by itself, and so that nothing about the four spoke pages changes.

Three conditions on the page rules:

1. The snippet loads on these eight pages and on no other page. The homepage rule has to match the homepage only. A rule written as "the address contains `/`" would match every page.
2. Each rule has to hold when the address carries a query string, because ad clicks arrive with one.
3. This snippet and 13785 are never on the same page. Both switch the same class on `<html>`, so two of them on one page would work against each other. The eight pages above and the four spoke pages don't overlap.

If the snippet can't be limited to exactly these eight pages, stop and report instead of loading it more widely.

```html
<script>
/* Phones: the 'Message Andrew' button waits until the hero's main button is clear of it, then shows as usual. A hidden marker, placed the way the widget places its button (58px tall, 14px above the bottom of the screen), gives the button's top edge, so the rule follows whatever the browser's own toolbars do. 4px of air. It never waits once the chat has been opened or a conversation is under way. Same switch as the 30 Oct form/footer rule, with its own class. Rollback: delete this block. */
(function(){var st=document.createElement('style');st.textContent='html.arm-dl-wait direct-line,html.arm-dl-wait [data-dl-fallback]{opacity:0!important;visibility:hidden!important;pointer-events:none!important}';document.head.appendChild(st);var mq=window.matchMedia('(max-width:640px)'),R=document.documentElement,q=0,used=0,hk=0,ob=0,m=document.createElement('div');m.setAttribute('aria-hidden','true');m.setAttribute('data-dl-mark','1');m.style.cssText='position:fixed;left:0;bottom:14px;width:1px;height:58px;margin:0;padding:0;border:0;transform:none;visibility:hidden;pointer-events:none';function chat(){var F=window.FounderLine;if(!F)return;try{if(!hk&&F.on){hk=1;F.on('open',function(){used=1;upd()})}if(F.state&&F.state().started)used=1}catch(e){}}function upd(){q=0;chat();var w=false,B=document.body;if(B&&!ob&&window.MutationObserver){ob=1;new MutationObserver(upd).observe(B,{childList:true})}if(!used&&mq.matches){var b=document.querySelector('section.hero.dark a.btn,.hp-hero a.hp-btn');if(b){if(B&&!m.parentNode)B.appendChild(m);var r=b.getBoundingClientRect(),t=m.parentNode?m.getBoundingClientRect().top:window.innerHeight-72;w=r.height>0&&r.bottom>t-4}}R.classList.toggle('arm-dl-wait',w)}function sch(){if(!q){q=1;setTimeout(upd,80)}}document.addEventListener('click',function(e){var t=e.target;if(t&&t.closest&&t.closest('direct-line,[data-dl-fallback]')){used=1;upd()}},true);window.addEventListener('scroll',sch,{passive:true});window.addEventListener('resize',sch);window.addEventListener('load',upd);window.addEventListener('pageshow',upd);document.addEventListener('DOMContentLoaded',upd);upd();setTimeout(upd,1500);setTimeout(upd,4000)})();
</script>
```

The block is 2,183 characters, from `<script>` to `</script>`. Copy it from this file and never retype it. It is the block in 13785 with two differences: the opening comment, and the element it watches.

- 13785 watches `.spoke-hero .hero-ctas`, which is the spoke pages' button together with the line under it.
- This one watches `section.hero.dark a.btn,.hp-hero a.hp-btn`, which is the main button alone. The first half matches the seven hubs, which share one hero layout, and the second half matches the homepage. On each of the eight pages the selector matches exactly one element, and its text is "Let's talk about your marketing →".

Everything else works as described under "How it works" in the spoke file: the class on `<html>`, the 640-pixel limit, the hidden marker that stands in for the bar, the 4 pixels of air, the times it is checked again, the chat guard, and the backup button.

### Why the main button alone

Under the main button each of these heroes has two more lines: a link to the free video review, and the Google rating. This rule does not watch them. Once the bar shows, it sits on the video-review link, as it does today on phones where the main button is already clear.

Watching all three would keep the bar out of the first view on nearly every phone, the homepage included. On 2026-11-17 Andrew said to keep the "Message Andrew" box on the homepage hero. Watching the main button alone keeps the box in the homepage's first view at 390 wide and wider, and takes it away only where it covers the main button.

To watch the lines under the button as well, the selector would end at the rating line instead (`section.hero.dark a.rating,.hp-hero a.hp-rating`). That version has not been tested and is not part of this change.

## Tested

2026-11-19, 1:12 to 1:32 PM ET, on copies of the live pages with the snippet added before `</body>`, logged out, in a phone-size Chromium window with a phone user agent and touch. Each cell is a fresh page load.

Now, at first view:

| Screen | Homepage | Roofing | Electrician | HVAC | Flooring | Fencing | Remodeling | Window and door |
|---|---|---|---|---|---|---|---|---|
| 390 by 664 | clear | bar over the whole button | bar over the whole button | button cut off by the screen edge, bar over 25px of the 39px showing | button cut off by the screen edge, bar over 25px of the 39px showing | button cut off by the screen edge, bar over 14px of the 28px showing | button cut off by the screen edge, bar not on it | button cut off by the screen edge, bar not on it |
| 393 by 659 | clear | bar over 44 of the button's 50px | bar over 44 of the button's 50px | button cut off by the screen edge, bar over 20px of the 34px showing | button cut off by the screen edge, bar over 20px of the 34px showing | button cut off by the screen edge, bar over 9px of the 23px showing | button below the screen | button cut off by the screen edge, bar not on it |
| 402 by 681 | clear | bar over 19 of the button's 51px | bar over 19 of the button's 51px | bar over 43 of the button's 51px | bar over 43 of the button's 51px | bar over the whole button | button cut off by the screen edge, bar over 29px of the 43px showing | bar over 47 of the button's 51px |
| 375 by 635 | bar over 6 of the button's 53px | button cut off by the screen edge, bar over 20px of the 34px showing | button cut off by the screen edge, bar not on it | button cut off by the screen edge, bar not on it | button cut off by the screen edge, bar not on it | button below the screen | button below the screen | button below the screen |
| 414 by 715 | clear | clear | clear | clear | clear | bar over 21 of the button's 51px | bar over 9 of the button's 51px | bar over 13 of the button's 51px |
| 375 by 548 | button cut off by the screen edge, bar over 17px of the 31px showing | button below the screen | button below the screen | button below the screen | button below the screen | button below the screen | button below the screen | button below the screen |
| 360 by 640 | bar over 50 of the button's 53px | button cut off by the screen edge, bar not on it | button below the screen | button below the screen | button below the screen | button below the screen | button below the screen | button below the screen |
| 320 by 454 | button below the screen | button below the screen | button below the screen | button below the screen | button below the screen | button below the screen | button below the screen | button below the screen |
| 390 by 745 | clear | clear | clear | bar over 1 of the button's 50px | bar over 1 of the button's 50px | bar over 12 of the button's 50px | bar over 36 of the button's 50px | bar over 28 of the button's 50px |
| 430 by 739 | clear | clear | clear | clear | clear | clear | clear | clear |
| 412 by 780 | clear | clear | clear | clear | clear | clear | clear | clear |
| 700 by 900 | clear | clear | clear | clear | clear | clear | clear | clear |
| 768 by 1024 | clear | clear | clear | clear | clear | clear | clear | clear |
| 1440 by 900 | clear | clear | clear | clear | clear | clear | clear | clear |

"Clear" means the bar is not on the main button. It can still be on the lines under it.

With the change, pixels of scrolling before the bar shows:

| Screen | Homepage | Roofing | Electrician | HVAC | Flooring | Fencing | Remodeling | Window and door |
|---|---|---|---|---|---|---|---|---|
| 390 by 664 | no change | 64 | 64 | 88 | 88 | 104 | 128 | 120 |
| 393 by 659 | no change | 72 | 72 | 96 | 96 | 104 | 128 | 120 |
| 402 by 681 | no change | 24 | 24 | 48 | 48 | 64 | 88 | 56 |
| 375 by 635 | 16 | 96 | 120 | 120 | 120 | 128 | 152 | 144 |
| 414 by 715 | no change | no change | no change | no change | no change | 32 | 16 | 24 |
| 375 by 548 | 104 | 184 | 208 | 208 | 208 | 216 | 240 | 232 |
| 360 by 640 | 72 | 128 | 152 | 152 | 152 | 160 | 224 | 176 |
| 320 by 454 | 328 | 440 | 384 | 352 | 384 | 384 | 440 | 432 |
| 390 by 745 | no change | no change | no change | 8 | 8 | 24 | 48 | 40 |
| 430 by 739 | no change | no change | no change | no change | no change | no change | no change | no change |
| 412 by 780 | no change | no change | no change | no change | no change | no change | no change | no change |
| 700 by 900 | no change | no change | no change | no change | no change | no change | no change | no change |
| 768 by 1024 | no change | no change | no change | no change | no change | no change | no change | no change |
| 1440 by 900 | no change | no change | no change | no change | no change | no change | no change | no change |

The bar waits on 61 of the 88 phone-size pairs: the 29 where it is on the button at first view, and the 32 where the button would pass under it on the way up.

On every one of these 224 loads (14 screen sizes, eight pages, with and without the snippet): no page errors, no console errors and no sideways scroll. On every load with the snippet:

- the hero is in the same place as on the live page;
- the selector matches one element, the main button;
- the bar is never over the main button, at first view or at any scroll position on the way down;
- the bar changes state at most once on the way down, at the scroll position the geometry gives (the button's bottom edge against the marker's top edge less 4 pixels, to the next 8-pixel step);
- 2,400 pixels down the bar is showing where it shows on the live page;
- the first-view state is back after scrolling to the top;
- where the bar does not wait, it is exactly where it is on the live page.

On all 88 phone-size loads of the live pages the bar's top edge was 72 pixels above the bottom of the screen, and on all 88 loads with the snippet the marker's top edge was within a pixel of it. On all 24 loads at 700 wide and wider the rule did nothing: no marker, no wait, and the box where it is today.

Also tested with the snippet added, at 390 by 664 on the roofing and HVAC hubs and at 360 by 640 on the homepage. Nothing was typed at any point.

- With the real widget: the bar was tapped 200 pixels down and the chat opened. Back at the top the chat stayed on screen. While the footer was on screen the 30 Oct rule hid it, as it does today. After the chat was closed, the bar no longer waited.
- With a stand-in widget, so that no call reached the chat server: with no chat activity the bar keeps waiting; a conversation already under way never waits; a chat that opens by itself stops the wait right away; a conversation flag that turns on with no event is picked up by the next check, at the latest the one 4 seconds after the script starts.

## After saving, check

Logged out, with a cache-buster, at the rendering layer. The test files are in the project files under `bar-wait-hubs-2026-11-19/verify/`.

1. Page code, all 77 sitemap addresses: `arm-dl-wait` is in the code of twelve pages, which are these eight and the four HVAC spokes, and of no other page. On each of the eight, the script block is this file's block character for character (2,183 characters), printed once, after the footer. On each of the four spokes the block is still 13785's own.
2. Each of the eight pages carries the block when fetched with no query string and when fetched with one.
3. Every page against its copy from before the save: each of the eight gained this one block and nothing else on it changed, and no other page changed.
4. Browser, the eight pages at the fourteen screen sizes (`test4.js` in `live` mode, compared by `cmp-live4.py`): 112 of 112 rows equal `expected-with-the-change.json`. Run before the save, the same comparison reports all 88 phone-size rows as different, which is the proof that it can tell the two states apart.
5. At 412 by 780, 768 by 1024 and 1440 by 900 the bar is in the first view exactly where it is now (708 to 765, 942 to 999 and 818 to 875 pixels from the top).
6. Chat, on two hubs and the homepage, with nothing typed: after scrolling a little, tap the bar to open the chat, then scroll back to the top. The chat stays on screen.
7. The four HVAC spokes still give the rows in `hvac-spokes-2026-11-18/bar-wait/verify/expected-with-the-change.json`.
8. No console errors and no sideways scroll on any of the twelve pages.

The 360 by 640 and 320 by 454 rows were measured with today's site header, which breaks onto two rows on screens 361 wide and narrower and pushes each page down 36 pixels. If the header fix in `site-header-narrow-phones-2026-11-18/` goes live, the bar will show 36 pixels sooner on those two rows, and they should be measured again.

## Rollback

Switch the new snippet off and clear the page cache. Nothing else is touched. 13785 stays on.

## Not in this change

- The lines under the main button: the video-review link and the Google rating. Before any scrolling today, the bar is on part of one or both of them on 30 of the 88 phone-size pairs. On the homepage at 390 by 664 it covers the rating line and half of the video-review link. That stays as it is. See "Why the main button alone".
- Other pages. A read-only look at the first view of all 77 sitemap addresses at one screen size, 390 by 664, on 2026-11-19 from 1:38 to 1:43 PM ET (`verify/survey-390x664-summary.txt`):
  - The bar shows and is on no link, button or field at 48 of the 77 addresses. Three of those are the remodeling hub, the window and door hub and `/remodeling-marketing-systems/`, which redirects to the remodeling hub. On them the button starts just below the bar.
  - The bar is hidden at first view on 10 pages: the four HVAC spokes (13785), and six pages with a form in the first view (the 30 Oct rule).
  - The bar is on a link or a button on 19 pages: the homepage and five of the hubs, which are covered above, and 13 others.
  - On eight of those 13 it is on a hero button. `/services/` ("See the services ↓", 41 of the 49 pixels showing), `/industries/` ("Talk to Andrew", 32 of 47), `/services/generative-engine-optimization/` ("Get Your Free AI Visibility Check", 29 of 43), `/services/crm-email-and-automation/` ("See Where Your Pipeline Leaks →", 11 of 25), `/services/lead-to-booked-job/` ("Book a Pipeline Diagnostic", 5 of 19), and the three city SEO pages ("Uncover My Revenue Gap →", 8 to 15 of 50).
  - On the other five it is on a text link or a tab: `/services/lead-generation/` and `/cost-per-booked-job/` ("Prefer email, phone, or text? Contact Andrew"), `/best-contractor-marketing-agencies/`, `/local-business-marketing/`, and the tab row on `/free-roi-calculator/`.
  - Each of these pages has its own hero layout, so each needs its own selector and its own test. They were measured at one screen size only.
- The window and door spokes. Their SEO page uses the spoke layout and is not covered by 13785.
- Screens between 641 and 767 wide, where the widget is a box in the bottom right corner instead of a bar.
- The 30 Oct rule itself, and snippet 13785.

## Limits of the test

A phone-size Chromium window is not an iPhone. Safari's own toolbars, which grow and shrink the screen as the reader scrolls, are not reproduced here, and no Safari engine was available for this test. The marker is there so that the rule doesn't depend on any of that. The same rule has been live on the four HVAC spokes since 12:45 PM ET on 2026-11-19, and it has not yet been looked at on a real iPhone.
