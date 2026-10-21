# About page: remove orange spine lines (2026-10-21)

Andrew's ask: "on the about page i'd like you to remove the orange spine lines which are connecting the different sections."

## Change (one line, scoped to About only)

Target: WPCode snippet 12539 "ARM — Section Spine (signature head + tail)" (HTML, Site Wide Footer).

1. Back up the full current snippet code to `ARM Local\backups\wpcode-12539-before-2026-10-21.html`.
2. Inside `<style id="arm-spine-css">`, immediately BEFORE the line
   `/* retire the two hand-built predecessors (router tail-in, 6-Gap plug) */`
   insert exactly this line:

```
/* 2026-10-21 Andrew: no spine lines on About (page 11236) */ body.page-id-11236 .arm-spine__head,body.page-id-11236 .arm-spine__tail{display:none!important}
```

3. Assert: the anchor line occurs exactly once; the code grows by exactly the inserted line; nothing else changes.
4. WPCode save note: call the CodeMirror `cm.save()` before clicking Update, or the form posts the old code.
5. Purge cache for /about/ (`/?armpurge=/about/`).

Nothing else changes: page content, section padding/spacing and every other page's spine marks stay as they are.

## Verify (live page load)

- https://andrewryanmarketing.com/about/ at 1440 and 390 width, logged out: count `.arm-spine__head, .arm-spine__tail` with height > 0 and display != none. Expect 0. Page height unchanged (about 13,829px desktop / 24,840px phone).
- Homepage: `.arm-ws` still shows its head and tail (spine still works elsewhere).

Rollback: delete the inserted line.
