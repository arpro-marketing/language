# Redirected internal links and the orphan page (approved)

Andrew, in the thread on 2026-11-19 at 1:33 PM ET: "fix the redirected internal links and the orphan page".

## Rules

- 209 links on 35 pages (from the logged-out fetch of all 77 sitemap pages at ~1:10 PM ET) send the visitor through a 301. Full list with anchor text and context: `redirected-links.json`.
- A link whose anchor is a city name and that points at an old `/locations/lead-generation-services-in-*/` page (143 links, all in "we serve ... in Nashville, Charlotte ..." or "Johnson City, TN · Kingsport, TN ..." lists): **remove the link, keep the city text exactly as it is**. All of them 301 to /services/lead-generation/, so ten identical links in a row add nothing.
- Every other link (66): **change only the href** to the final destination listed. Anchor text, classes and attributes stay. Use the absolute https URL with trailing slash.
- No visible word changes anywhere. Only `href` values and, for the city lists, the `<a>` tags around city names.
- Header, footer and menu templates: 3 of the links sit inside a header/footer/nav element on a page; fix them where they are stored.

## Orphan page

/best-contractor-marketing-agencies/ has no internal link from any sitemap page. Add one link without changing words, on /agency-consultant-or-fractional-cmo-contractor/, first paragraph that starts "A marketing agency executes marketing to produce leads." (inside `.s5-card`):
- NOW: `A <b>marketing agency</b> executes`
- NEW: `A <a href="https://andrewryanmarketing.com/best-contractor-marketing-agencies/"><b>marketing agency</b></a> executes`
- Only the first occurrence. It must look like the page's other in-text links (compare computed color and underline with the link "is it a sales or marketing problem?" on the same page); if it renders as plain text, add the same styling inline.

## How to save

One page at a time, record the revision, make only the listed changes, purge, fetch logged out with a cache-buster, confirm none of the listed old hrefs remain on that page and the visible text is unchanged. Log in ROLLBACK.txt. Stop on anything unexpected.

## Per page

### /services/painter-marketing/ (1)

| href now | anchor | action |
|---|---|---|
| `https://andrewryanmarketing.com/locations/` | View All Locations We Serve | point straight at /services/lead-generation/ |

### /services/medical-marketing/ (1)

| href now | anchor | action |
|---|---|---|
| `https://andrewryanmarketing.com/locations/` | View All Locations We Serve | point straight at /services/lead-generation/ |

### /services/cleaning-services-marketing/ (1)

| href now | anchor | action |
|---|---|---|
| `https://andrewryanmarketing.com/locations/` | View All Locations We Serve | point straight at /services/lead-generation/ |

### /services/marketing-for-pest-control-companies/ (1)

| href now | anchor | action |
|---|---|---|
| `https://andrewryanmarketing.com/locations/` | View All Locations We Serve | point straight at /services/lead-generation/ |

### /services/handyman-marketing/ (1)

| href now | anchor | action |
|---|---|---|
| `https://andrewryanmarketing.com/locations/` | View All Locations We Serve | point straight at /services/lead-generation/ |

### /services/marketing-for-plumbers/ (1)

| href now | anchor | action |
|---|---|---|
| `https://andrewryanmarketing.com/locations/` | View All Locations We Serve | point straight at /services/lead-generation/ |

### /sales-and-marketing-consulting-for-contractors/ (2)

| href now | anchor | action |
|---|---|---|
| `https://andrewryanmarketing.com/lead-to-booked-job/` | Sales Pipeline | point straight at /services/lead-to-booked-job/ |
| `https://andrewryanmarketing.com/sales-and-marketing-help-cost-for-contractors/` | What should a contractor pay for sales & marketing help? | point straight at /contractor-marketing-budget/ |

### /services/crm-email-and-automation/ (2)

| href now | anchor | action |
|---|---|---|
| `/lead-to-booked-job/` | Sales Pipeline | point straight at /services/lead-to-booked-job/ |
| `/lead-to-booked-job/` | → Contractor Sales Pipeline | point straight at /services/lead-to-booked-job/ |

### /services/lead-to-booked-job/ (1)

| href now | anchor | action |
|---|---|---|
| `/contact` | Book a Pipeline Diagnostic | point straight at /contact/ |

### /why-arent-my-leads-converting/ (1)

| href now | anchor | action |
|---|---|---|
| `https://andrewryanmarketing.com/lead-to-booked-job/` | Contractor Sales Pipeline Optimization | point straight at /services/lead-to-booked-job/ |

### /services/seo-bristol-tn/ (1)

| href now | anchor | action |
|---|---|---|
| `/locations/lead-generation-services-in-bristol-tn/` | Bristol lead generation | unlink (keep the city name) |

### /services/seo-kingsport-tn/ (1)

| href now | anchor | action |
|---|---|---|
| `/locations/lead-generation-services-in-kingsport-tn/` | Kingsport lead generation | unlink (keep the city name) |

### /services/marketing-for-landscaping-and-lawn-care/ (1)

| href now | anchor | action |
|---|---|---|
| `https://andrewryanmarketing.com/locations/` | View All Locations We Serve | point straight at /services/lead-generation/ |

### /services/fencing-company-marketing/ (1)

| href now | anchor | action |
|---|---|---|
| `/locations/` | Locations We Serve | point straight at /services/lead-generation/ |

### /services/flooring-company-marketing/ (1)

| href now | anchor | action |
|---|---|---|
| `/flooring-lead-generation/` | Flooring lead generation | point straight at /flooring-contractor-lead-generation/ |

### /services/seo-johnson-city-tn/ (1)

| href now | anchor | action |
|---|---|---|
| `/locations/lead-generation-services-in-johnson-city-tn/` | Johnson City lead generation | point straight at /services/lead-generation/ |

### /services/lead-generation/ (2)

| href now | anchor | action |
|---|---|---|
| `/services/reputation-management-johnson-city-tn/` | Reputation | point straight at /services/reputation-management-for-contractors/ |
| `/services/reputation-management-johnson-city-tn/` | reputation | point straight at /services/reputation-management-for-contractors/ |

### /services/window-and-door-marketing/seo/ (11)

| href now | anchor | action |
|---|---|---|
| `/locations/lead-generation-services-in-nashville-tn/` | Nashville | unlink (keep the city name) |
| `/locations/lead-generation-services-in-charlotte-nc/` | Charlotte | unlink (keep the city name) |
| `/locations/lead-generation-services-in-atlanta-ga/` | Atlanta | unlink (keep the city name) |
| `/locations/lead-generation-services-in-raleigh-nc/` | Raleigh | unlink (keep the city name) |
| `/locations/lead-generation-services-in-charleston-sc/` | Charleston | unlink (keep the city name) |
| `/locations/lead-generation-services-in-knoxville-tn/` | Knoxville | unlink (keep the city name) |
| `/locations/lead-generation-services-in-richmond-va/` | Richmond | unlink (keep the city name) |
| `/locations/lead-generation-services-in-huntsville-al/` | Huntsville | unlink (keep the city name) |
| `/locations/lead-generation-services-in-birmingham-al/` | Birmingham | unlink (keep the city name) |
| `/locations/lead-generation-services-in-virginia-beach-va/` | Virginia Beach | unlink (keep the city name) |
| `/locations/` | dozens of other Southeast markets | point straight at /services/lead-generation/ |

### /fence-contractor-advertising/ (12)

| href now | anchor | action |
|---|---|---|
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-johnson-city-tn/` | Johnson City, TN | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-kingsport-tn/` | Kingsport, TN | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-bristol-tn/` | Bristol, TN | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-knoxville-tn/` | Knoxville, TN | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-nashville-tn/` | Nashville, TN | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-chattanooga-tn/` | Chattanooga, TN | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-greenville-sc/` | Greenville, SC | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-richmond-va/` | Richmond, VA | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-charlotte-nc/` | Charlotte, NC | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-asheville-nc/` | Asheville, NC | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-raleigh-nc/` | Raleigh, NC | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-atlanta-ga/` | Atlanta, GA | unlink (keep the city name) |

### /seo-for-remodeling-contractors/ (17)

| href now | anchor | action |
|---|---|---|
| `https://andrewryanmarketing.com/locations/` | location pages | point straight at /services/lead-generation/ |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-nashville-tn/` | Nashville | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-charlotte-nc/` | Charlotte | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-atlanta-ga/` | Atlanta | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-raleigh-nc/` | Raleigh | unlink (keep the city name) |
| `https://andrewryanmarketing.com/local-seo-results/` | proven results | point straight at /case-studies/ |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-nashville-tn/` | Nashville | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-charlotte-nc/` | Charlotte | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-atlanta-ga/` | Atlanta | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-raleigh-nc/` | Raleigh | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-charleston-sc/` | Charleston | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-knoxville-tn/` | Knoxville | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-chattanooga-tn/` | Chattanooga | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-richmond-va/` | Richmond | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-huntsville-al/` | Huntsville | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-louisville-ky/` | Louisville | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/` | many other Southeast markets | point straight at /services/lead-generation/ |

### /ppc-for-remodeling-contractors/ (12)

| href now | anchor | action |
|---|---|---|
| `https://andrewryanmarketing.com/local-seo-results/` | proven results | point straight at /case-studies/ |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-nashville-tn/` | Nashville | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-charlotte-nc/` | Charlotte | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-atlanta-ga/` | Atlanta | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-raleigh-nc/` | Raleigh | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-charleston-sc/` | Charleston | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-knoxville-tn/` | Knoxville | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-lexington-ky/` | Lexington | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-asheville-nc/` | Asheville | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-greenville-sc/` | Greenville | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-virginia-beach-va/` | Virginia Beach | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/` | many other Southeast markets | point straight at /services/lead-generation/ |

### /seo-for-flooring-contractors/ (16)

| href now | anchor | action |
|---|---|---|
| `https://andrewryanmarketing.com/flooring-lead-generation/` | flooring lead generation | point straight at /flooring-contractor-lead-generation/ |
| `https://andrewryanmarketing.com/locations/` | service areas | point straight at /services/lead-generation/ |
| `/local-seo-results/` | flooring client case study | point straight at /case-studies/ |
| `/locations/lead-generation-services-in-nashville-tn/` | Nashville | unlink (keep the city name) |
| `/locations/lead-generation-services-in-charlotte-nc/` | Charlotte | unlink (keep the city name) |
| `/locations/lead-generation-services-in-atlanta-ga/` | Atlanta | unlink (keep the city name) |
| `/locations/lead-generation-services-in-raleigh-nc/` | Raleigh | unlink (keep the city name) |
| `/locations/lead-generation-services-in-charleston-sc/` | Charleston | unlink (keep the city name) |
| `/locations/lead-generation-services-in-knoxville-tn/` | Knoxville | unlink (keep the city name) |
| `/locations/lead-generation-services-in-huntsville-al/` | Huntsville | unlink (keep the city name) |
| `/locations/lead-generation-services-in-birmingham-al/` | Birmingham | unlink (keep the city name) |
| `/locations/lead-generation-services-in-greenville-sc/` | Greenville | unlink (keep the city name) |
| `/locations/lead-generation-services-in-memphis-tn/` | Memphis | unlink (keep the city name) |
| `/locations/` | many other Southeast markets | point straight at /services/lead-generation/ |
| `https://andrewryanmarketing.com/flooring-lead-generation/` | Flooring Lead Generation / How Flooring Contractors Get Leads | point straight at /flooring-contractor-lead-generation/ |
| `/local-seo-results/` | View our case studies | point straight at /case-studies/ |

### /flooring-contractor-lead-generation/ (14)

| href now | anchor | action |
|---|---|---|
| `https://andrewryanmarketing.com/local-seo-results` | local SEO Results | point straight at /case-studies/ |
| `/locations/lead-generation-services-in-nashville-tn/` | Nashville | unlink (keep the city name) |
| `/locations/lead-generation-services-in-charlotte-nc/` | Charlotte | unlink (keep the city name) |
| `/locations/lead-generation-services-in-atlanta-ga/` | Atlanta | unlink (keep the city name) |
| `/locations/lead-generation-services-in-raleigh-nc/` | Raleigh | unlink (keep the city name) |
| `/locations/lead-generation-services-in-charleston-sc/` | Charleston | unlink (keep the city name) |
| `/locations/lead-generation-services-in-knoxville-tn/` | Knoxville | unlink (keep the city name) |
| `/locations/lead-generation-services-in-chattanooga-tn/` | Chattanooga | unlink (keep the city name) |
| `/locations/lead-generation-services-in-asheville-nc/` | Asheville | unlink (keep the city name) |
| `/locations/lead-generation-services-in-richmond-va/` | Richmond | unlink (keep the city name) |
| `/locations/lead-generation-services-in-louisville-ky/` | Louisville | unlink (keep the city name) |
| `/locations/` | View all locations we serve | point straight at /services/lead-generation/ |
| `http://andrewryanmarketing.com/seo-for-flooring-contractors/` | SEO for Flooring Contractors: How to Rank #1 on Google in Your City | point straight at /seo-for-flooring-contractors/ |
| `/local-seo-results/` | View our case studies | point straight at /case-studies/ |

### /how-to-expand-a-contractor-business-into-a-new-market/ (1)

| href now | anchor | action |
|---|---|---|
| `/services/reputation-management-johnson-city-tn/` | Build reputation as a system → | point straight at /services/reputation-management-for-contractors/ |

### /marketing-for-fence-installers/ (13)

| href now | anchor | action |
|---|---|---|
| `https://andrewryanmarketing.com/services/marketing-for-contractors/` | contractor marketing | point straight at / |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-johnson-city-tn/` | Johnson City, TN | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-kingsport-tn/` | Kingsport, TN | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-bristol-tn/` | Bristol, TN | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-knoxville-tn/` | Knoxville, TN | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-nashville-tn/` | Nashville, TN | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-chattanooga-tn/` | Chattanooga, TN | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-greenville-sc/` | Greenville, SC | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-richmond-va/` | Richmond, VA | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-charlotte-nc/` | Charlotte, NC | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-asheville-nc/` | Asheville, NC | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-raleigh-nc/` | Raleigh, NC | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-atlanta-ga/` | Atlanta, GA | unlink (keep the city name) |

### /seo-for-fence-companies/ (13)

| href now | anchor | action |
|---|---|---|
| `https://andrewryanmarketing.com/marketing-for-fencing-contractors/` | marketing for fencing installers | point straight at /marketing-for-fence-installers/ |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-johnson-city-tn/` | Johnson City, TN | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-kingsport-tn/` | Kingsport, TN | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-bristol-tn/` | Bristol, TN | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-knoxville-tn/` | Knoxville, TN | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-nashville-tn/` | Nashville, TN | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-chattanooga-tn/` | Chattanooga, TN | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-greenville-sc/` | Greenville, SC | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-richmond-va/` | Richmond, VA | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-charlotte-nc/` | Charlotte, NC | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-asheville-nc/` | Asheville, NC | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-raleigh-nc/` | Raleigh, NC | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-atlanta-ga/` | Atlanta, GA | unlink (keep the city name) |

### /lead-generation-for-service-businesses/ (15)

| href now | anchor | action |
|---|---|---|
| `http://andrewryanmarketing.com` | Johnson City SEO company | point straight at / |
| `https://andrewryanmarketing.com/locations/` | locations we serve | point straight at /services/lead-generation/ |
| `https://andrewryanmarketing.com/services/window-door-siding-marketing/` | Window and Door marketing systems | point straight at /services/window-and-door-marketing/ |
| `/locations/lead-generation-services-in-nashville-tn/` | Nashville | unlink (keep the city name) |
| `/locations/lead-generation-services-in-charlotte-nc/` | Charlotte | unlink (keep the city name) |
| `/locations/lead-generation-services-in-atlanta-ga/` | Atlanta | unlink (keep the city name) |
| `/locations/lead-generation-services-in-raleigh-nc/` | Raleigh | unlink (keep the city name) |
| `/locations/lead-generation-services-in-memphis-tn/` | Memphis | unlink (keep the city name) |
| `/locations/lead-generation-services-in-chattanooga-tn/` | Chattanooga | unlink (keep the city name) |
| `/locations/lead-generation-services-in-richmond-va/` | Richmond | unlink (keep the city name) |
| `/locations/lead-generation-services-in-louisville-ky/` | Louisville | unlink (keep the city name) |
| `/locations/lead-generation-services-in-virginia-beach-va/` | Virginia Beach | unlink (keep the city name) |
| `/locations/lead-generation-services-in-rock-hill-sc/` | Rock Hill | unlink (keep the city name) |
| `/locations/` | many other cities across Tennessee, the Carolinas, Virginia, Georgia,  | point straight at /services/lead-generation/ |
| `/local-seo-results/` | View our case studies | point straight at /case-studies/ |

### /get-more-customers-johnson-city-tn/ (2)

| href now | anchor | action |
|---|---|---|
| `https://andrewryanmarketing.com/local-seo-results/` | Local SEO Results | point straight at /case-studies/ |
| `/local-seo-results/` | View our case studies | point straight at /case-studies/ |

### /get-more-leads-johnson-city-tn/ (1)

| href now | anchor | action |
|---|---|---|
| `/local-seo-results/` | View our case studies | point straight at /case-studies/ |

### /get-more-website-traffic-johnson-city-tn/ (3)

| href now | anchor | action |
|---|---|---|
| `http://andrewryanmarketing.com` | digital marketing in Johnson City TN | point straight at / |
| `https://andrewryanmarketing.com/services/email-marketing-services/` | Email marketing services in Johnson City | point straight at /services/crm-email-and-automation/ |
| `/local-seo-results/` | View our case studies | point straight at /case-studies/ |

### /remodeling-contractor-lead-generation/ (11)

| href now | anchor | action |
|---|---|---|
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-nashville-tn/` | Nashville | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-charlotte-nc/` | Charlotte | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-atlanta-ga/` | Atlanta | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-raleigh-nc/` | Raleigh | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-charleston-sc/` | Charleston | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-knoxville-tn/` | Knoxville | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-chattanooga-tn/` | Chattanooga | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-huntsville-al/` | Huntsville | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-louisville-ky/` | Louisville | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-richmond-va/` | Richmond | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/` | many other Southeast markets | point straight at /services/lead-generation/ |

### /local-contractor-seo-blueprint/ (17)

| href now | anchor | action |
|---|---|---|
| `http://andrewryanmarketing.com` | Andrew Ryan Marketing | point straight at / |
| `https://andrewryanmarketing.com/services/marketing-for-contractors/` | contractor marketing strategy | point straight at / |
| `http://andrewryanmarketing.com` | Johnson City | point straight at / |
| `https://andrewryanmarketing.com/locations/` | surrounding markets | point straight at /services/lead-generation/ |
| `https://andrewryanmarketing.com/local-seo-results/` | seen contractors gain traction | point straight at /case-studies/ |
| `/locations/lead-generation-services-in-nashville-tn/` | Nashville | unlink (keep the city name) |
| `/locations/lead-generation-services-in-charlotte-nc/` | Charlotte | unlink (keep the city name) |
| `/locations/lead-generation-services-in-atlanta-ga/` | Atlanta | unlink (keep the city name) |
| `/locations/lead-generation-services-in-raleigh-nc/` | Raleigh | unlink (keep the city name) |
| `/locations/lead-generation-services-in-charleston-sc/` | Charleston | unlink (keep the city name) |
| `/locations/lead-generation-services-in-chattanooga-tn/` | Chattanooga | unlink (keep the city name) |
| `/locations/lead-generation-services-in-richmond-va/` | Richmond | unlink (keep the city name) |
| `/locations/lead-generation-services-in-lexington-ky/` | Lexington | unlink (keep the city name) |
| `/locations/lead-generation-services-in-virginia-beach-va/` | Virginia Beach | unlink (keep the city name) |
| `/locations/lead-generation-services-in-asheville-nc/` | Asheville | unlink (keep the city name) |
| `/locations/` | dozens of other cities across the Southeast | point straight at /services/lead-generation/ |
| `/local-seo-results/` | View our case studies | point straight at /case-studies/ |

### /why-flooring-companies-struggle-online/ (13)

| href now | anchor | action |
|---|---|---|
| `https://andrewryanmarketing.com/flooring-lead-generation/` | flooring lead generation strategies | point straight at /flooring-contractor-lead-generation/ |
| `/locations/lead-generation-services-in-nashville-tn/` | Nashville | unlink (keep the city name) |
| `/locations/lead-generation-services-in-charlotte-nc/` | Charlotte | unlink (keep the city name) |
| `/locations/lead-generation-services-in-atlanta-ga/` | Atlanta | unlink (keep the city name) |
| `/locations/lead-generation-services-in-knoxville-tn/` | Knoxville | unlink (keep the city name) |
| `/locations/lead-generation-services-in-charleston-sc/` | Charleston | unlink (keep the city name) |
| `/locations/lead-generation-services-in-huntsville-al/` | Huntsville | unlink (keep the city name) |
| `/locations/lead-generation-services-in-birmingham-al/` | Birmingham | unlink (keep the city name) |
| `/locations/lead-generation-services-in-greenville-sc/` | Greenville | unlink (keep the city name) |
| `/locations/lead-generation-services-in-elizabethton-tn/` | Elizabethton | unlink (keep the city name) |
| `/locations/` | many other markets | point straight at /services/lead-generation/ |
| `https://andrewryanmarketing.com/flooring-lead-generation/` | Flooring Lead Generation / How Flooring Contractors Get Leads | point straight at /flooring-contractor-lead-generation/ |
| `/local-seo-results/` | View our case studies | point straight at /case-studies/ |

### /lead-generation-fence-contractors/ (14)

| href now | anchor | action |
|---|---|---|
| `https://andrewryanmarketing.com/services/marketing-for-contractors/` | contractor marketing | point straight at / |
| `https://andrewryanmarketing.com/marketing-for-fencing-contractors/` | marketing for fence installers | point straight at /marketing-for-fence-installers/ |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-johnson-city-tn/` | Johnson City, TN | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-kingsport-tn/` | Kingsport, TN | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-bristol-tn/` | Bristol, TN | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-knoxville-tn/` | Knoxville, TN | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-nashville-tn/` | Nashville, TN | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-chattanooga-tn/` | Chattanooga, TN | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-greenville-sc/` | Greenville, SC | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-richmond-va/` | Richmond, VA | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-charlotte-nc/` | Charlotte, NC | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-asheville-nc/` | Asheville, NC | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-raleigh-nc/` | Raleigh, NC | unlink (keep the city name) |
| `https://andrewryanmarketing.com/locations/lead-generation-services-in-atlanta-ga/` | Atlanta, GA | unlink (keep the city name) |

### /local-business-marketing/ (4)

| href now | anchor | action |
|---|---|---|
| `http://andrewryanmarketing.com` | marketing agency in Johnson City | point straight at / |
| `https://andrewryanmarketing.com/locations/` | location pages | point straight at /services/lead-generation/ |
| `https://andrewryanmarketing.com/local-seo-results/` | Local SEO Results | point straight at /case-studies/ |
| `/local-seo-results/` | View our case studies | point straight at /case-studies/ |
