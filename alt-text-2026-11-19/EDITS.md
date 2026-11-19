# Alt text for the images that have none

STATUS: APPROVED, NOT YET LIVE. Andrew asked for this on 2026-11-19 at 12:01 PM ET:

> "now i see it looks like the images on our pages lack alt tags. we need to fix that. make them descriptive and keyword rich, but lean on being descriptive of what the image shows"

The wording below was posted to him in the thread at 12:18 PM ET.

## What the audit found

All 77 sitemap URLs were fetched logged out on 2026-11-19 and every `<img>` was read from the page code, then again from the rendered page in a browser.

- 487 `<img>` tags in the page code. None is missing the `alt` attribute. 176 have it empty.
- The 176 are 17 images: the logo in the header and footer of every page (152), six thumbnails that appear on two pages (12), six dimmed copies inside the Portfolio sliders (6), three blog images (3) and three pop-up slots (3).
- One more tag carries the alt text of a different image (the second image in the flooring post). It is fixed here too, because that alt does not describe what the image shows.
- The HVAC hub and its four spokes have no content images. The logo is their only image.

## Scope

Only `alt` attributes on the tags listed here, plus one `title` attribute on the tag that carried the wrong alt. No visible copy, no layout, no other attribute, no other page. The exact strings are in `alts.json` in this folder. Copy them from that file and never retype them.

## The changes

### 1. Logo: one field in the media library

Attachment 13184 (`2026/10/andrew-ryan-marketing-ar-mark-orange-160.webp`), field `_wp_attachment_image_alt`.

- NOW: empty
- NEW: `Andrew Ryan Marketing logo`

The header (Bricks element iyrj5g, template 13191) and the footer (element chha8k, template 13193) have no custom alt, so both print the library alt. Do not edit the templates. Both logos sit inside a link that already has `aria-label="Andrew Ryan Marketing home"`, so a screen reader still reads the link once. Purge the whole page cache after this one, because every page changes.

### 2. /portfolio/ (page 12875): twelve tags

Six thumbnails in the wall at the top (`nav.wall a.tile span.sh img`), each `alt=""` now:

| File (in `/wp-content/uploads/2026/09/`) | NEW alt |
|---|---|
| `lumitra-advisors-website-homepage-thumb.webp` | Lumitra Advisors manufacturing consultancy website homepage with the headline From Crisis to Confidence in 90 Days |
| `curl-up-and-dye-salon-website-homepage-thumb.webp` | Curl Up And Dye hair salon website homepage with five photos of client hair color above the headline The color you asked for. Finally. |
| `brandface-ceo-branding-services-page-thumb.webp` | BrandFace CEO Branding Services page with the headline Build the Identity Behind the Title and a strategy form |
| `executive-leadership-experts-website-homepage-thumb.webp` | Berke Gormley Leadership Advisors website homepage with the headline Executive Leadership Coaching and Consulting for High-Impact Leaders |
| `michael-carr-pendergrass-community-guide-thumb.webp` | Michael Carr and Associates real estate community guide for Pendergrass, Georgia, with a map of the town |
| `andrew-ryan-marketing-homepage-hero-thumb.webp` | Andrew Ryan Marketing homepage showing the 6-Gap Revenue Map beside the headline Contractor Marketing Agency. Get Chosen. Not just found. |

Six dimmed copies, one in each slider (`div.lens-mach > img.ghost`), each `alt=""` now. Each is the same file as the full image beside it (`img.lens-img`), which keeps its own alt. Change only the tag with `class="ghost"`:

| File | NEW alt |
|---|---|
| `lumitra-advisors-website-homepage.webp` | Lumitra Advisors homepage, dimmed, with numbered notes on what Google and AI read |
| `curl-up-and-dye-salon-website-homepage.webp` | Curl Up And Dye homepage, dimmed, with numbered notes on what Google and AI read |
| `brandface-ceo-branding-services-page.webp` | BrandFace CEO Branding Services page, dimmed, with numbered notes on what Google and AI read |
| `executive-leadership-experts-website-homepage.webp` | Berke Gormley Leadership Advisors homepage, dimmed, with numbered notes on what Google and AI read |
| `michael-carr-pendergrass-community-guide.webp` | Michael Carr and Associates Pendergrass community guide, dimmed, with numbered notes on what Google and AI read |
| `andrew-ryan-marketing-homepage-hero-2026-09-23.webp` | Andrew Ryan Marketing homepage, dimmed, with numbered notes on what Google and AI read |

### 3. /case-studies/ (page 5101): six tags

The same six thumbnails (`nav.t-wall a.t-tile span.t-sh img`), each `alt=""` now, with the same six alts as the Portfolio thumbnails above. This markup is inside a WPBakery raw HTML block, so decode the block, change the six attributes, encode it again and confirm the decoded block differs from the old one only in those six attributes.

### 4. /why-flooring-companies-struggle-online/ (post 9029): two tags

- `img.wp-image-9031` (`flooring-contractor-website-design-mistakes`), under the heading "1. Most Flooring Contractor Websites Are Built Like Brochures".
  - NOW: `alt=""`
  - NEW: `Example of a poorly designed flooring contractor website with slow loading, outdated design, and no contact form.`
- `img.wp-image-9032` (`flooring-contractor-seo-case-study-lead-growth`), under the heading "Case Study: How One Contractor Increased Leads by 180%".
  - NOW: `alt="Example of a poorly designed flooring contractor website with slow loading, outdated design, and no contact form."` and `title="Common Flooring Contractor Website Design Mistakes"`. Both belong to the first image.
  - NEW: `alt="Clipboard graphic titled Case Study: Flooring Company SEO Success, with a rising bar chart"` and the `title` attribute removed.
  - The image also shows "180% Increase in Traffic" and "3X More Leads". Those figures are left out of the alt on purpose: they are not one of the published results.

### 5. /lead-generation-fence-contractors/ (post 10925): one tag

`img.wp-image-10939` (`fencing-industry-market-data-2026`).

- NOW: `alt=""`
- NEW: `Infographic of fencing industry statistics: $9.8B U.S. fencing market size in 2024, 346,357 fence construction businesses, $4K to $12K average project value, and 76% of local searches leading to a call within 24 hours`

This string contains `$9` and `$4`. Use a literal string replace. A regex replacement would read them as group references and eat them.

### 6. /local-business-marketing/ (post 6218): one tag

`img.wp-image-6221` (`local-seo-company-results-in-2025-ranking-1-and-2-2`).

- NOW: `alt=""`
- NEW: `Google search results for get more calls johnson city tn, with Andrew Ryan Marketing pages ranked first and second`

### 7. Three pop-up slots: one tag each

These `<img>` tags have no `src` and sit inside a container that is `display:none` until a screenshot is opened. The scripts already copy the opened screenshot's alt into the slot (`im.alt=b.querySelector('img').alt` on the homepage, `lbImg.alt=im.alt` on the other two), so this only gives the slot a resting value.

- Homepage (2762): the one `<img>` inside `div.hp-lb`. The page prints it as `<img alt="">`.
- /ai-overview-proof/ (11947): the one `<img>` inside `div#apr-lb`. The page prints it as `<img alt="" />`.
- /services/generative-engine-optimization/ (12084): the one `<img>` inside `div#apr-lb`. The page prints it as `<img decoding="async" src="" alt="">`. Leave the empty `src` as it is.
- NEW on all three: `alt="Expanded screenshot"`

## How to save

One target at a time, in the order above. For each: record the revision (or the prior field value) for rollback, make only the listed attribute changes, save, purge the cache for that page, fetch the page logged out with a cache-buster, and confirm the new alt is in the page code before starting the next. If a tag does not match its NOW value, or anything else on a page would change, stop and report instead of saving.

Left alone on purpose: on /services/painter-marketing/ the page builder's gallery script adds a hidden, empty pop-up slot (`img.lb-image`) after load. It is not in the page code and the script fills it when a photo is opened.

## Checks after the saves (from the cloud, logged out, with a cache-buster)

1. On all 77 pages, no `<img>` in the page code has an empty alt.
2. Every tag in `alts.json` carries exactly its new alt, and the logo alt is in the header and footer of every page.
3. Compared with the copy fetched at 12:19 PM ET, nothing on any page differs except these alt attributes and the one removed title.
4. In a browser at 1440 wide: the same result on the rendered pages, no console error that was not there before, and each pop-up still opens and takes the opened screenshot's alt.

## Rollback

Set the field on attachment 13184 back to empty and restore the prior revision of pages 12875, 5101, 2762, 11947, 12084 and posts 9029, 10925, 6218.
