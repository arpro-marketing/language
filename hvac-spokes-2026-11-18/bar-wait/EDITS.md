# HVAC spoke pages: the "Message Andrew" bar waits for the hero button on phones

STATUS: PROPOSED. Nothing here is live. Save only when Andrew's own message names it.

## What changes

On phones, on the four HVAC spoke pages, the "Message Andrew" bar stays hidden until the hero button and the line under it are clear of it. Then it shows exactly where and how it shows today. If the reader scrolls back to the top, it waits again.

Nothing changes on a phone screen tall enough that the bar doesn't touch the hero button row, and nothing changes on tablets or desktop. No wording changes, so the word counts stay as they are.

The bar never waits once the chat has been opened, or when a conversation is already under way, so this rule never hides a chat in progress.

Mockup: `bar-before-after.png` in this folder (AI Visibility and Google Ads on a 390 by 664 screen: now, with the change, and with the change after a short scroll).

## Why

On a phone the bar is fixed to the bottom of the screen: 58 pixels tall, 14 pixels up, almost the full width. On short phone screens that is where the hero button row sits before any scrolling. Measured on the live pages:

- 390 by 664: the bar covers 38 of the hero button's 51 pixels on AI Visibility, and the line under the button ("Free · 20 minutes · a call with Andrew") on Google Ads, Call Handling and SEO. That line went live in the final pass on 2026-11-18.
- 375 by 635: it covers most of the hero button on Google Ads (46 of 51 pixels) and SEO (36), and part of it on Call Handling (21).
- 360 by 640: it covers the whole hero button on Call Handling and 42 of its 51 pixels on SEO.

390 by 664 and 393 by 659 are the sizes standard iPhones have reported in Safari with its bars showing, and 375 by 635 the older 375-wide ones. The exact size depends on the phone and the iOS version, so read these as "short phone screens", not as a list of models.

This is the "phone Message Andrew box covers hero button" item that was already on the known list, measured on these four pages.

## Pages

AI Visibility (13720), Google Ads (13726), Call Handling (13733) and SEO (13745). No other page changes. The hub, the homepage and the other trade pages keep today's behavior.

## The code

One new WPCode snippet (HTML, footer), limited to the same four pages as the sub-nav script (13762). It is its own snippet so that switching it off is the whole rollback. If it can't be limited to those four pages, stop and report instead of loading it more widely.

```html
<script>
/* Phones: the 'Message Andrew' button waits until the hero button and the line under it are clear of it, then shows as usual. A hidden marker, placed the way the widget places its button (58px tall, 14px above the bottom of the screen), gives the button's top edge, so the rule follows whatever the browser's own toolbars do. 4px of air. It never waits once the chat has been opened or a conversation is under way. Same switch as the 30 Oct form/footer rule, with its own class. Rollback: delete this block. */
(function(){var st=document.createElement('style');st.textContent='html.arm-dl-wait direct-line,html.arm-dl-wait [data-dl-fallback]{opacity:0!important;visibility:hidden!important;pointer-events:none!important}';document.head.appendChild(st);var mq=window.matchMedia('(max-width:640px)'),R=document.documentElement,q=0,used=0,hk=0,ob=0,m=document.createElement('div');m.setAttribute('aria-hidden','true');m.setAttribute('data-dl-mark','1');m.style.cssText='position:fixed;left:0;bottom:14px;width:1px;height:58px;margin:0;padding:0;border:0;transform:none;visibility:hidden;pointer-events:none';function chat(){var F=window.FounderLine;if(!F)return;try{if(!hk&&F.on){hk=1;F.on('open',function(){used=1;upd()})}if(F.state&&F.state().started)used=1}catch(e){}}function upd(){q=0;chat();var w=false,B=document.body;if(B&&!ob&&window.MutationObserver){ob=1;new MutationObserver(upd).observe(B,{childList:true})}if(!used&&mq.matches){var b=document.querySelector('.spoke-hero .hero-ctas');if(b){if(B&&!m.parentNode)B.appendChild(m);var r=b.getBoundingClientRect(),t=m.parentNode?m.getBoundingClientRect().top:window.innerHeight-72;w=r.height>0&&r.bottom>t-4}}R.classList.toggle('arm-dl-wait',w)}function sch(){if(!q){q=1;setTimeout(upd,80)}}document.addEventListener('click',function(e){var t=e.target;if(t&&t.closest&&t.closest('direct-line,[data-dl-fallback]')){used=1;upd()}},true);window.addEventListener('scroll',sch,{passive:true});window.addEventListener('resize',sch);window.addEventListener('load',upd);window.addEventListener('pageshow',upd);document.addEventListener('DOMContentLoaded',upd);upd();setTimeout(upd,1500);setTimeout(upd,4000)})();
</script>
```

How it works:

- A class on `<html>` (`arm-dl-wait`) switches on a stylesheet rule that hides the widget. This is the same method as the 30 Oct form and footer rule (`arm-dl-hide`), with its own class, so the two rules don't touch each other. The widget's own visibility guard only watches the widget's own attributes, so a class on `<html>` doesn't trip it.
- The rule applies on screens up to 640 wide, which is where the widget itself switches to the full-width bar.
- The widget sits in a closed shadow root, so the page can't measure the bar directly. The script adds a hidden one-pixel marker that is placed the way the widget places its bar (fixed, 58 pixels tall, 14 pixels above the bottom). Wherever the browser puts the bar, it puts the marker, so the marker's top edge is the bar's top edge. That holds whatever a phone's own toolbars do.
- The class is on while the bottom edge of `.spoke-hero .hero-ctas` is lower than 4 pixels above the marker's top edge.
- It is checked again on scroll and on resize (at most once every 80 milliseconds), when the page has loaded or is shown again from the back button, when something is added to `<body>` (the widget arriving), and 1.5 and 4 seconds after the script runs.
- The widget's open chat panel lives in the same element as the bar, and a conversation that is already under way opens its panel by itself when a page loads. So the rule stops for the rest of the page view as soon as the chat opens (the widget's own "open" event, or any tap inside the widget) or when `FounderLine.state().started` is true.
- It covers the backup button (`[data-dl-fallback]`) as well, which shows when the chat server can't be reached.

## Tested

2026-11-18, on copies of the live pages with the snippet added before `</body>`, logged out, in a phone-size Chromium window with a phone user agent and touch. Each cell is a fresh page load.

Now, at first view:

| Screen | AI Visibility | Google Ads | Call Handling | SEO |
|---|---|---|---|---|
| 390 by 664 | bar over 38 of the button's 51px | bar over the line under the button | bar over the line under the button | bar over the line under the button |
| 393 by 659 | button cut off by the screen edge, bar over 33px of it | bar over the line under the button | bar over the line under the button | bar over the line under the button |
| 402 by 681 | bar over the whole button | bar touching the button row | bar over part of the line under the button | bar touching the button row |
| 375 by 635 | button cut off by the screen edge, bar over 9px of it | bar over 46 of the button's 51px | bar over 21 of the button's 51px and the line under it | bar over 36 of the button's 51px and part of the line under it |
| 414 by 715 | clear | clear | clear | clear |
| 375 by 548 | button below the screen | button below the screen | button cut off by the screen edge | button below the screen |
| 360 by 640 | button below the screen | button cut off by the screen edge, bar over 5px of it | bar over the whole button | bar over 42 of the button's 51px |
| 320 by 454 | button below the screen | button below the screen | button below the screen | button below the screen |
| 390 by 745 | clear | clear | clear | clear |
| 430 by 739 | clear | clear | clear | clear |
| 412 by 780 | clear | clear | clear | clear |
| 700 by 900 | clear | clear | clear | clear |
| 768 by 1024 | clear | clear | clear | clear |
| 1440 by 900 | clear | clear | clear | clear |

With the change, pixels of scrolling before the bar shows:

| Screen | AI Visibility | Google Ads | Call Handling | SEO |
|---|---|---|---|---|
| 390 by 664 | 80 | 24 | 32 | 24 |
| 393 by 659 | 88 | 32 | 40 | 32 |
| 402 by 681 | 64 | 8 | 16 | 8 |
| 375 by 635 | 112 | 88 | 64 | 80 |
| 414 by 715 | no change | no change | no change | no change |
| 375 by 548 | 192 | 176 | 152 | 160 |
| 360 by 640 | 136 | 144 | 96 | 104 |
| 320 by 454 | 408 | 360 | 368 | 352 |
| 390 by 745 | no change | no change | no change | no change |
| 430 by 739 | no change | no change | no change | no change |
| 412 by 780 | no change | no change | no change | no change |
| 700 by 900 | no change | no change | no change | no change |
| 768 by 1024 | no change | no change | no change | no change |
| 1440 by 900 | no change | no change | no change | no change |

On every one of these 112 loads (14 screen sizes, four pages, with and without the snippet): no page errors and no sideways scroll. On every load with the snippet: the hero row is in the same place as on the live page, the bar is never over the hero row at any scroll position on the way down, the bar changes state at most once on the way down, it is showing at 2,400 pixels down, and the first-view state is back after scrolling to the top. Wherever the bar was showing in the first view on a phone-width screen, the marker's top edge was within a pixel of the bar's top edge (16 of 16 loads). On all 44 phone-width loads of the live pages the bar's top edge was 72 pixels above the bottom of the screen, which is what the marker assumes.

Also tested on Google Ads at 390 by 664:

- With the real widget and the snippet in place, the chat was opened by tapping the bar 200 pixels down, and nothing was typed. The panel stayed on screen after scrolling back to the top. After it was closed, the bar no longer waited.
- With a stand-in widget, so that no call reached the chat server: a conversation already under way never waits; a chat that opens by itself stops the wait within a fraction of a second; a widget that arrives six seconds late with a conversation under way shows at once, with no scrolling; with no chat activity the bar keeps waiting.
- With the chat server blocked, the backup button waits and shows the same way as the bar.

## After saving, check

Logged out, with a cache-buster, at the rendering layer:

1. The source of each of the four pages contains `arm-dl-wait`. The hub and one window and door spoke do not.
2. At 390 by 664 on each page, the first view has no bar and the hero button and the line under it are fully visible. Scrolling down, the bar appears at about these positions (give or take 8 pixels): AI Visibility 80, Google Ads 24, Call Handling 32, SEO 24. It is showing at 2,400 pixels down, and it is hidden again back at the top.
3. At 412 by 780, 768 by 1024 and 1440 by 900 the bar is in the first view exactly where it is now (708 to 765, 942 to 999 and 818 to 875 pixels from the top).
4. After scrolling a little, tap the bar to open the chat and type nothing. Scroll back to the top. The chat stays on screen.
5. No console errors and no sideways scroll.
6. The 30 Oct rule still works: on a phone-size screen the bar is hidden while the footer is on screen.

The same test files are in the project files under `hvac-spokes-2026-11-18/bar-wait/verify/`. Run against the live pages after the save, the results must match the second table above.

## Rollback

Switch the snippet off and clear the page cache. Nothing else is touched.

## Not in this change

- The other pages with the same overlap (the hub, the homepage, the other trade pages). Their hero button rows have different class names, so each needs its name added to the selector and its own test.
- Screens between 641 and 767 wide, where the widget is a box in the bottom right corner instead of a bar.
- The closing button row at the bottom of each page.
- The 30 Oct rule itself. Seen during this test: on a phone-size screen it also hides an open chat while the footer is on screen, and brings it back when the footer leaves the screen. Left as it is.
- If the chat is ever set to open by itself for first-time visitors, test this rule again. Today it opens by itself only for a conversation that is already under way.

## Limits of the test

A phone-size Chromium window is not an iPhone. Safari's own toolbars, which grow and shrink the screen as the reader scrolls and which changed again in recent iOS versions, are not reproduced here, and no Safari engine was available for this test. The marker is there so that the rule doesn't depend on any of that, but the last check after saving is still a look on a real iPhone.
