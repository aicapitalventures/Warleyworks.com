# WW-WEB-v1.2 — Rendered Fidelity Verification & Production Asset Reconciliation
**Report status:** PARTIALLY VERIFIED; FULL REPOSITORY BROWSER QA BLOCKED; FOUNDER REVIEW REQUIRED.
**Date:** 2026-10-23. **Operating protocol:** AICV Universal Lean Build Protocol™ v1.0; METADATA LAW™; RAO LOOP™ v3.0.
**Repository:** `aicapitalventures/Warleyworks.com`.
**Working branch:** `feature/approved-ui-website-v1`, PR #1 (draft).
**Authoritative starting SHA:** `8f83e7e7ff50b9dc433ac9aa7931e735eb2e9a44`.
**Authorized scope:** visual-fidelity assessment, accessibility defects, static QA and evidence; no production release, paid infrastructure, lead collection, merge or DNS changes.

## Source integrity
- Founder-uploaded original logo: `WARLEY WORKS LOGO.png` (389x244), SHA-256 `6b3dc0440e7264edcabe51c22b6ef57dec26f24b6a81b7f65afbe56413036a70`.
- Founder-approved website design reference: `image(20261023-184120).png` (1448x1086), SHA-256 `7900998f967caf9a1e849f1ce3fdfa508440202c856f3853aaa5d624193be78b`.
- Local interactive preview: `Warley_Works_Preview/index.html`, SHA-256 `4a6bd3fa2ef685574b99d43458ce547a378f1a967fcccf13260413ea21093351`.
- **Important distinction:** the local preview was created separately and is NOT a byte-for-byte rendering of this GitHub branch. Its browser results must not be attributed to the repository page.

## Verification matrix
| Category | Result | Evidence/limitation |
|---|---|---|
| GitHub baseline | PASS | Draft PR #1 head and main independently read through authenticated GitHub connector |
| Canonical logo vector in GitHub | PASS (source) | `assets/logo-horizontal.svg` and `assets/mark.svg` derived from original artwork |
| Brand colors | PASS (source) | Navy/brass/ivory preserved |
| Light-background gold small-text contrast | DEFECT FOUND; PATCH PREPARED | Previous `#bd8540` on `#faf9f7` ≈3.03:1; v1.2 uses `#8f601f` ≈5.17:1 for selected small labels |
| Primary brass on navy | PASS (calculation) | `#d4a15e` on `#061c29` ≈7.51:1 |
| Text on brass button | PASS (calculation) | Navy on brass ≈6.41:1 |
| Actual GitHub page screenshots | BLOCKED / NOT TESTED | Local browser cannot fetch GitHub and GitHub text connector does not provide a browser-serving site |
| Packaged interactive preview at 1440, 1024, 768, 375, 320 px | PASS (preview only) | Real headless Chromium `set_content` rendering; 0 horizontal overflow, 0 page JavaScript errors, 0 broken in-page `img` elements |
| Preview mobile menu at 768, 375, 320 px | PASS (preview only) | Hamburger opened and Escape closed |
| Preview valid demo form at 1440, 375 px | PASS (preview only) | Explicit preview confirmation, no external requests |
| Preview invalid form | PASS native validation (preview only) | Native browser invalid state blocks submission; separate inline error message not visible |
| Production GitHub estimate form | PASS (static only) | JS prevents default and has no fetch/transport; full browser interaction not run |
| External remote service photos in GitHub CSS | UNVERIFIED | Pexels/Unsplash asset URLs, image delivery, attribution for each ID not validated due network restriction |
| Stock/photo licensing rules | VERIFIED GENERIC LICENSE ONLY | Official Pexels and Unsplash license pages permit certain commercial uses. Individual photo provenance must still be reconciled. No images presented as Warley Works projects |
| Open Graph social card | HOLD | Relative SVG is not robust for social crawlers; create production PNG and absolute image URL when deployment is approved |
| Accessibility | CONDITIONAL | Static WCAG contrast remediation made; full keyboard audit, screen reader testing and automated a11y scan of canonical site remain open |
| Security/lead capture | PASS SCOPE LIMIT | No live intake/delivery enabled, no personal data submitted to backend; full production privacy and anti-spam remain future-phase |
| Release control | PASS | No merge, deploy, DNS changes or paid infrastructure authorized |

## Screen-by-screen design reconciliation
- **Navigation:** existing navy header, gold CTA and founder-source-traced wordmark fit the direction; canonical actual rendering remains untested.
- **Hero:** correct hierarchy, headline and painting-first messaging; source CSS relies on third-party photographs rather than a vetted, local version of the approved hero kitchen image.
- **Services:** painting primary and handyman secondary; no unsupported exterior-painting or extensive maintenance claims.
- **Portfolio/reviews:** mockup included stock before/after and invented five-star review; canonical site deliberately excludes false completed jobs, ratings and customer identities. This difference is a REQUIRED integrity improvement, not a defect.
- **Estimate:** preview-only; final live form requires a separate secure intake Build Room and business activation authorization.
- **Mobile:** preview fits 320–375 px; canonical responsive CSS includes 360/640/860 breakpoints but must be rendered independently.

## Defect & remediation register
| ID | Priority | Status | Detail and release condition |
|---|---|---|---|
| WW-12-01 | HIGH | PATCHED SOURCE | Gold small text did not meet WCAG AA on cream; separate dark accessible text token `#8f601f` adopted; visual recheck pending |
| WW-12-02 | HIGH | OPEN | Canonical GitHub page not browser-tested; run real headless Chromium on checkout/localhost in Codespaces |
| WW-12-03 | HIGH | OPEN | Remote image delivery and individual-source provenance not confirmed; use approved local image assets and archive licenses before public release |
| WW-12-04 | MEDIUM | OPEN | Relative SVG OG card not ready for production social sharing |
| WW-12-05 | HIGH | INTENTIONALLY DISABLED | Live estimate handling, privacy terms and anti-spam deferred pending founder authorization |
| WW-12-06 | HIGH (PUBLIC) | OPEN | Business name/DBA, Chicago licensing, insurance and real contact/channel not cleared |
| WW-12-07 | MEDIUM | OPEN | Screen-reader and keyboard user-journey QA of the canonical site not completed |
| WW-12-08 | LOW | ACCEPTED | Preview uses a slightly different layout from canonical GitHub page. Keep separate and label honestly |

## RAO LOOP™ v3.0 outcome
**Review:** approved visual direction maintained; source and local preview checked separately.
**Analyze:** canonical screenshot access is the central evidence gap. Small-text contrast was a concrete in-scope defect.
**Intelligence:** exact source SHA-256 established; official stock-provider general licenses checked; photo-specific evidence absent.
**Optimize:** accessibility text-color variant without modifying the identity palette; update QA decision and defects.
**Verify:** preview Chromium at five sizes passed; CSS contrast math passes; canonical full rendered/browser checks remain **NOT VERIFIED**.
**Execute:** preserve Draft PR #1 and perform canonical checkout/browser QA as the next bounded validation step.

**Provisional RAO assessment:** 78/100 (carry-forward conservative value, not an inflated approval). **Approval state:** Continue Iteration. **Risk:** Moderate for internal review; high for public launch. Official Approval Lock™ cannot be recorded while material verification and compliance gaps remain.

## Canonical-site local browser QA (next gate)
In a clean Codespaces checkout of this branch, serve from the repository root using `python3 -m http.server 8000`, then navigate locally and capture viewport screenshots at 320, 375, 768, 1024 and 1440 px. Check console, network, alt labels, focus order, overflow, mobile menu, invalid/valid demo requests, broken backgrounds, responsive cards, and color contrast. Check generated screenshot against original founder reference, without inventing portfolio or customer proof. No GitHub Pages, DNS or production deployment is required.

## Founder decision
**GO:** In-branch internal QA/remediation and evidence capture only.
**HOLD:** Merge, public staging publication, production, DNS, paid infrastructure or live customer intake.

**METADATA LAW™:** Project WARLEY WORKS; Artifact WW-WEB-v1.2; Evidence classes SOURCE / LOCAL PREVIEW / EXTERNAL POLICY; Authority Founder; Priority High; Cost $0; Risk High for public release; Next action canonical rendered QA; Prohibited actions merge, publish, spend, fabricate proof.