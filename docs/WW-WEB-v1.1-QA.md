# WW-WEB-v1.1 — Design Fidelity & QA Evidence
**Status:** IMPLEMENTED SOURCE CHANGES / BROWSER QA OPEN — FOUNDER REVIEW REQUIRED
**Date:** 2026-10-23
**Source baseline:** GitHub PR #1 (draft), branch `feature/approved-ui-website-v1`, parent `ed0e15af16e444944da9d7848a07a605c55dd1ec`.
**Review authority:** Founder. **Cost impact:** $0 new infrastructure.
**Protocol:** AICV Universal Lean Build Protocol™ v1.0; METADATA LAW™; RAO LOOP™ v3.0.

## Controlling sources
1. Original founder-uploaded logo `WARLEY WORKS LOGO.png` (389 × 244); SHA-256 `6b3dc0440e7264edcabe51c22b6ef57dec26f24b6a81b7f65afbe56413036a70`. Original preserved in founder's downloadable kit; not rewritten.
2. Founder-approved desktop/mobile website mockup `image(20261023-184120).png` (1448 × 1086); SHA-256 `7900998f967caf9a1e849f1ce3fdfa508440202c856f3853aaa5d624193be78b`.
3. Draft PR #1, current website code in the approved repository.
4. Master Warley Works handoff: painting-first sole-proprietor business, modest $100–$300 prelaunch capital, future property maintenance vision.

## v1.1 changes executed
- Replaced simulated wordmark in header and footer with `assets/logo-horizontal.svg`, a vector contour trace *derived directly from the founder's artwork*; no substitute letterforms.
- Replaced `assets/mark.svg` with original-symbol-derived contour paths for the favicon. Shape remains from original source; antialias and tracing may cause tiny edge differences.
- Unified responsive CSS dimensions for logo at desktop, tablet and mobile widths.
- Added minimal source provenance and v1.1 QA documentation. No business claims, backend, deployment, purchase, DNS, advertisements or production contact integration.

## Functional / static QA (verified via GitHub source inspection)
| Requirement | Evidence and status |
|---|---|
| Two source-derived logo placements | Header and footer reference `assets/logo-horizontal.svg` — PASS (static) |
| Favicon artwork | `assets/mark.svg` derived from uploaded source — PASS (asset check) |
| Mobile breakpoint strategy | 860px, 640px, and 360px responsive rules present — PASS (static) |
| Keyboard/navigation code | Toggle, Escape close, click close and aria-expanded in JS — PASS (static) |
| Estimate demo | Form validates browser fields, prevents submission, no network calls — PASS (static) |
| Unsupported public claims | No licensed/insured, client testimonials or five-star assertions in site copy — PASS (static) |
| Authentic portfolio | No false completed project claims; illustrative placeholder disclosed — PASS (static) |
| Privacy | Demo does not persist or send submitted information — PASS (static inspection) |
| DNS / public release | Unchanged and not authorized — PASS (workflow boundary) |
| Desktop screenshot parity | Actual rendered site screenshot versus founder reference — NOT YET TESTED |
| Mobile screenshot parity | Actual rendered site screenshot versus founder reference — NOT YET TESTED |
| Third-party hero / service images | Browser load, current license and replacement policy — NOT YET VERIFIED |
| SEO/social preview | Relative SVG og:image requires public absolute URL and PNG/JPG — BLOCKED UNTIL DEPLOYMENT PLAN |
| Formal accessibility | Keyboard/browser test and automated audit — NOT YET TESTED |
| Production form | Secure endpoint, captcha/abuse controls, privacy/retention — OUT OF SCOPE |

No browser screenshot or production image-load test is represented here as completed.

## Browser QA runbook (Codespaces/local only; no public hosting)
Run a local static server in a checked-out branch. Capture and archive screenshots at 320, 375, 768, 1024, and 1440px widths. Compare header mark, hero hierarchy, section spacing, service cards, estimate form, footer and responsive navigation against the approved reference. Test mobile menu open/close (including Escape), keyboard focus order, valid/invalid form states, console exceptions, horizontal overflow, image failures and reduced-motion preference. Use demo-only fictional form data; never enter private customer data. Do not activate public GitHub Pages in this stage.

## RAO LOOP™ v3.0
- **Review:** Strong prelaunch page sections already present; logo was originally a reconstructed approximation.
- **Analyze:** Main visual discrepancies: header wordmark fidelity and unverified external photography; no browser screenshots of deployed/staged page.
- **Intelligence:** Exact logo and approved mockup recovered and checksummed; third-party image rights, browser rendering and compliance clearance remain outstanding.
- **Optimize:** Source-traced logo treatment, responsive logo sizing, traceable audit evidence, no unsupported trust badges.
- **Verify:** Source-level checks pass; browser fidelity and full accessibility remain open.
- **Execute:** Remain on draft PR pending measured local browser QA, cosmetic adjustments, and Founder review.

### RAO v3.0 provisional scorecard (out of 100)
| Dimension | Score |
|---|---:|
| Clarity | 9 |
| Purpose alignment | 9 |
| Strategic value | 8 |
| Market/user value | 8 |
| Feasibility | 9 |
| Monetization potential | 7 |
| Risk control | 7 |
| Scalability | 8 |
| Differentiation | 7 |
| Execution readiness | 6 |
| **Total** | **78 / 100** |

**Classification:** Continue Iteration (score below 80). **Risk:** Moderate for private visual review; high for public release until compliance, form delivery, real photos and browser testing are resolved. **Approval:** Not eligible for Official Approval Lock™. Score is a provisional editorial assessment, not evidence of completed visual testing.

## Priority/defect ledger
| ID | Severity | Finding | Remediation / gate |
|---|---|---|---|
| FID-01 | Resolved-in-source | Initial SVG was not based on exact uploaded geometry | Source-derived trace in both placements; final founder comparison required |
| FID-02 | High | Remote hero imagery differs from mockup and is not browser-verified | Replace with reviewed, properly licensed/local photographic asset and re-test |
| FID-03 | High | No real desktop/mobile screenshot tests | Local browser QA on representative widths |
| FID-04 | High | Estimate intake disabled and no authorized contact exists | Secure intake project gated separately |
| FID-05 | Moderate | Social OG asset is relative SVG | Approved PNG/JPG and absolute production URL at deployment gate |
| FID-06 | Moderate | Formal keyboard/a11y audit not completed | Browser a11y review and remediation |
| FID-07 | Critical for public launch | Business licensing, insurance, contact, DBA/trademark and service capability status unverified | Explicit business activation and public-release gates |

## Founder Review Gate
**GO:** Continue on draft branch with local browser fidelity testing and approved image replacement.
**HOLD:** Merge, live publication, deployment, live lead collection, DNS changes, business/license claims, or paid services.

**METADATA LAW™**
Project: Warley Works; Artifact: WW-WEB-v1.1-QA; Authority: Founder; Stage: Build Room visual refinement; Status: CONDITIONAL SOURCE IMPLEMENTATION / VALIDATION INCOMPLETE; Risk: MODERATE-INTERNAL / HIGH-PUBLIC; Priority: HIGH; Next: rendered QA; Do not: merge, publish or spend.