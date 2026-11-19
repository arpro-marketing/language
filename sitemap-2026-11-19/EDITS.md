# Sitemap clean-up (approved)

Andrew, in the thread on 2026-11-19 at 1:30 PM ET: "okay great then lets improve the sitemap and make sure its perfect".

## Audit (cloud, logged out, 2026-11-19 ~1:35 PM ET)

- sitemap_index.xml lists page-sitemap.xml (57 URLs) and post-sitemap.xml (20 URLs). robots.txt points to it. /sitemap.xml and /wp-sitemap.xml 301 to it.
- 76 of 77 URLs return 200, have a self canonical and no noindex. All 145 image URLs in the sitemap return 200.
- 1 URL is wrong: /remodeling-marketing-systems/ (post 10478) returns 301 (Redirection plugin) to /services/remodeling-contractor-marketing/.
- Every published page and post missing from the sitemap is either a 301'd location page or noindex (lead-generation-sunset8-31). Nothing indexable is missing.
- llms.txt (the sitemap for AI crawlers) lists 4 URLs that now 301.

## Change 1: take /remodeling-marketing-systems/ out of the sitemap

Post 10478. In Yoast, set "Allow search engines to show this post in search results" to No (meta `_yoast_wpseo_meta-robots-noindex` = 1). Do not unpublish or trash it, and do not touch the Redirection rule: the 301 must keep working. Yoast drops noindexed posts from post-sitemap.xml.

Check: post-sitemap.xml no longer lists it (19 URLs), and /remodeling-marketing-systems/ still 301s to /services/remodeling-contractor-marketing/.

Rollback: set the field back to empty.

## Change 2: llms.txt, URLs only

| Line now | Becomes |
|---|---|
| `https://andrewryanmarketing.com/seo-for-window-and-door-companies/` | `https://andrewryanmarketing.com/services/window-and-door-marketing/seo/` |
| `https://andrewryanmarketing.com/window-and-door-lead-generation/` | `https://andrewryanmarketing.com/services/window-and-door-marketing/lead-generation/` |
| `https://andrewryanmarketing.com/ppc-for-window-and-door-companies/` | `https://andrewryanmarketing.com/services/window-and-door-marketing/ppc/` |
| the whole line `- [Remodeling Marketing Systems](https://andrewryanmarketing.com/remodeling-marketing-systems/): ...` | removed (the remodeling hub is already listed two lines above it, and the old URL 301s to that hub) |

Each target is exactly where the old URL redirects today. No description text changes. Keep a copy of the current llms.txt for rollback.

Check: every URL in llms.txt returns 200.
