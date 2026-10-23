# Warley Works — Approved UI Website v1

A responsive, static-first **prelaunch website** implementing the founder-approved Warley Works brand direction and UI reference (October 23, 2026).

## Project status

- **Status:** Visual implementation draft / founder review required.
- **Business model:** planned Chicago sole proprietorship; residential interior painting primary, limited handyman services secondary.
- **Source:** Existing `aicapitalventures/Warleyworks.com` repository.
- **Deployment:** Not configured or authorized by this change.
- **Bookings:** Not open; the estimate form is an interactive front-end **demo only**.
- **Business contact information, legal registration, license/insurance status, name/trademark clearance:** Must be verified before public operating claims.

## Brand tokens

| Token | Value |
| --- | --- |
| Deep navy | `#061c29` |
| Primary navy | `#0f2a3a` |
| Brass / gold | `#d4a15e` |
| Gold dark | `#bd8540` |
| Off-white | `#f7f5f1` |
| Ink | `#102c3b` |

The `assets/mark.svg` and `assets/logo-horizontal.svg` files in v1.1 are contour-traced directly from the **founder-supplied source artwork**, preserving the original letterforms and W/roof/window shape rather than substituting fonts or inventing a new symbol. They are derivative vector traces (not bit-for-bit source images). The authoritative original source PNG remains preserved separately in the founder asset kit. Source SHA-256: `6b3dc0440e7264edcabe51c22b6ef57dec26f24b6a81b7f65afbe56413036a70`. Acceptance requires Founder visual confirmation.

## Run locally

No build dependencies. From the project directory:

```bash
python3 -m http.server 8000
```

Open `http://localhost:8000`. Static hosting is possible later with GitHub Pages, Cloudflare Pages, or another approved host; none is enabled by this PR.

## v1.1 visual reconciliation

- The navbar and footer use `assets/logo-horizontal.svg`, built from traced paths of the supplied logo, avoiding the prior CSS-simulated wordmark.
- The favicon uses `assets/mark.svg`, traced from the approved W/roof symbol.
- The source-of-truth approval screenshot is inventoried in `docs/WW-WEB-V11-QA.md` with its checksum and validation limitations.
- The site still depends on remotely hosted illustrative photographs; verify image loading, licenses and fallbacks in browser testing before public release.
- A real desktop/mobile screenshot match has **not yet been signed off**.

## Working features

- Accessible skip link, mobile navigation with toggle / Escape close.
- Responsive hero, service cards, owner-focused section, staged portfolio, process steps, footer.
- Validated demo estimate form; does not transmit, persist, log or submit entered data.
- Reduced-motion support, keyboard focus treatment, alternative text for illustrative imagery.
- SVG favicon/mark and SVG social-card design.

## Image provenance and restrictions

Hero and service examples are remote illustrative photographs from Pexels or Unsplash, licensed by their respective providers. They **are not photographs of Warley Works jobs** and must never be labeled as such. Images may require user network connectivity. Validate each image URL and attribution/license status again before production release.

Pexels: https://www.pexels.com/legal-pages/license/
Unsplash: https://unsplash.com/license

### Forbidden claims until verified

Do not introduce invented testimonials, ratings, years in business, client counts, staff, portfolio results, licenses, insurance, certifications, contact addresses or completed contracts.

## Production gates

1. Founder visual acceptance.
2. Reconcile the original approved logo with web assets.
3. Confirm name/DBA, Chicago license and insurance readiness; obtain counsel or authoritative regulatory confirmation as appropriate.
4. Verify owner-authorized service scope, geographic coverage, pricing, contact email and phone.
5. Add secure estimate endpoint, anti-spam controls, retention/privacy disclosures, and successful end-to-end test.
6. Replace illustrative imagery with authentic project photographs when approved, retaining honest labels until then.
7. Validate mobile/tablet/desktop browsers, performance, accessibility and SEO.
8. Approve publication separately; no auto-deploy or public domain change in this PR.

## Planned next engineering iteration

- Add testable form backend with server-side validation and abuse controls.
- Add privacy/terms appropriate to actual deployed services and data processing.
- Implement test scripts and a staging preview before DNS or production launch.
