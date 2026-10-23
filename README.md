# Warley Works — Branded Website v1.0 (Prelaunch)

![Warley Works — Painting, Handyman, Property](assets/github-readme-banner.svg)

Founder-approved navy, warm gold and white website design adapted from the supplied brand concept boards.

## Site architecture

- `index.html` — responsive marketing homepage, service descriptions, illustrative gallery, process, about, draft estimate form.
- `privacy.html` — honest prelaunch privacy and website notice.
- `styles.css` — responsive design system, accessible keyboard navigation and reduced-motion support.
- `main.js` — mobile navigation, section links, estimate validation and prelaunch copy-to-clipboard workflow.
- `site-config.js` — production feature flags; **inquiry endpoint is intentionally disabled**.
- `assets/` — logos in editable SVG + transparent PNG, favicon sizes, service illustrations, background, banners, social-share graphic and colors.
- `docs/` — launch gates and QA checklist.

## Preview locally

No dependencies, database, or build process are required. From the site directory:

```bash
python3 -m http.server 8080
```

Open `http://localhost:8080`.

## Before live customer traffic

1. Verify trade-name availability, register the assumed name and satisfy all applicable Chicago licensing/insurance requirements.
2. Verify the proprietor's public contact details. None have been invented in this build.
3. Provision a secure, abuse-protected endpoint to receive inquiries, with server-side validation, spam controls, authentication if relevant, rate limiting, privacy and retention policies, and delivery monitoring.
4. Test the endpoint before setting `site-config.js` `activeForCustomers: true` and its approved HTTPS `estimateEndpoint`. The current form only **copies a draft**, and sends nothing.
5. Replace illustration-only gallery content with permission-approved genuine projects. Never publish fake testimonials, trust badges, metrics or license claims.
6. Complete production privacy notice, verify SEO information, remove `noindex,nofollow`, adjust `robots.txt`, and verify canonical domain.
7. Run cross-browser tests and a final accessibility pass.
8. Deploy only after separate launch approval; no live hosting is provisioned here.

## Brand

Source-of-truth design reference: founder-supplied Warley Works logo and approved concept boards. Some graphic assets are **reconstructed editable derivatives** rather than exact manufacturer-grade vector tracings of the source artwork. Proof all assets against approved master before printed collateral.

## Status

**Draft implementation, founder review required.** Business contact, legal and operational activation remain outstanding. The site does not represent active services, customer reviews, licensing or insurance.
## GitHub media note
This review branch includes editable SVG illustrations where the connector cannot transfer the finished local WebP/PNG asset library. The full, original approved-concept raster asset kit is included in the downloadable package supplied in chat; these SVG illustrations are intentionally provisional. Do not publish the branch as production.
