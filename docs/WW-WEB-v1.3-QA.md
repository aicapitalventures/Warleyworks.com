# WARLEY WORKS — Website v1.3 Canonical Browser QA & Founder Gate
**Artifact:** WW-WEB-1.3-QA | **State:** TEST HARNESS COMMITTED; CANONICAL BROWSER RUN BLOCKED | **Authority:** Founder
**Date:** 2026-10-23 | **Cost:** $0 new infrastructure | **Branch:** `feature/approved-ui-website-v1` | **PR:** #1 (draft).
**Controlling source:** Founder-approved UI screenshot `image(20261023-184120).png`, immutable original `WARLEY WORKS LOGO.png`; v1.2 GitHub SHA `b019b132219934fb3b9cdb04950085716bc9e907`.
**Governance:** AICV Universal Lean Build Protocol™ v1.0, METADATA LAW™, MDL™, RAO LOOP™ v3.0.

## Verified this phase
- GitHub PR remained open, draft, unmerged and main retained SHA `cfb9ed24aa691454ac99cfaa88be3570f689de47` at phase inspection.
- Existing canonical site includes original-source-traced `assets/logo-horizontal.svg` and `assets/mark.svg`.
- Responsive breakpoints and demo-only form retained; no live lead delivery.
- `tests/browser_qa.py` added as a runnable LOCAL Chromium test. Source integrity and presence can be inspected on the review branch.
- Python test syntax was rehearsed locally on an equivalent script, **not** executed on the GitHub checkout.
- Existing standalone downloadable preview screenshots from v1.2 remain useful for visual orientation only; they cannot verify canonical branch fidelity.

## Blocker / correction of evidence scope
- Current local container lacks outbound GitHub network access; authentic `git clone` failed with `Could not resolve host: github.com` and a direct-IP attempt was blocked.
- GitHub connector can read and modify text files but cannot serve them through the local Playwright browser.
- A proposed GitHub-hosted browser-test workflow submission was blocked by the tool runtime. NO workflow was created or executed.
- Consequently, **do not record full canonical desktop/mobile rendering as passed**.
- The script must be run on a checkout of this exact branch using Codespaces/local terminal, or on a later separately authorized GitHub test runner.

## Exact local browser test — NOT a deployment
1. Open the GitHub repository on the feature branch, then use existing Codespaces environment or an approved local checkout. Inspect `git status --short --branch` and `git rev-parse HEAD` first.
2. Install temporary QA-only Playwright if absent. This does not modify package manifests:
   ```bash
   python3 -m pip install --user playwright==1.55.0
   python3 -m playwright install chromium
   ```
3. At the repository root, run:
   ```bash
   python3 tests/browser_qa.py
   node tests/smoke.mjs
   node tests/contrast.mjs
   ```
4. Inspect `qa-artifacts/results.json` and five `canonical-*.png` screenshots. Compare each screenshot manually to the approved founder design; separate expected trust-and-safety omissions from visual defects. Do not commit `qa-artifacts/` until its contents are screened; never commit real customer data.
5. Revalidate remote background photos, image-specific author/rights evidence, browser network responses, alt text, keyboard focus, readable text, and any console errors. Only then propose founder visual acceptance.

## QA/defect ledger
| Defect ID | Severity | Status | Evidence / remediation gate |
|---|---|---|---|
| WW13-01 | HIGH | BLOCKED | Canonical browser screenshots not captured. Run local test on repo checkout. |
| WW13-02 | HIGH | OPEN | Homepage hero/repair/refresh images rely on external URLs; per-image identity, availability and license records incomplete. |
| WW13-03 | HIGH | OPEN | Approved screenshot hero appears as polished renovated kitchen, GitHub hero uses unrelated external photo. Reconcile with an authorized locally stored image. |
| WW13-04 | MEDIUM | PARTIAL | Normal-text contrast token corrected v1.2; complete WCAG keyboard and screen-reader tests pending. |
| WW13-05 | MEDIUM | OPEN | Social sharing OG image points to relative SVG; absolute hosted raster preview pending deployment gate. |
| WW13-06 | HIGH | INTENTIONALLY DISABLED | Estimate demo does not deliver leads; secure form/privacy/back-end need separate phase. |
| WW13-07 | CRITICAL FOR PUBLIC RELEASE | HOLD | DBA/name, licensing, insurance, verified contact info and eligibility/operational readiness. |
| WW13-08 | LOW | DOCUMENTED | Standalone preview is not the canonical GitHub render. Keep provenance separate. |
| WW13-09 | MEDIUM | TEST HARNESS COMMITTED | Browser script exists, but actual run/report remains unverified until checkout execution. |

## Photo-source intelligence
- Pexels ID `6474471` is an identifiable photo by Tima Miroshnichenko of an interior wall being painted, listed as free on Pexels.
- Other current Pexels IDs `6264414`, `4792524` and the Unsplash CDN image ID have not been individually corroborated through accessible photographer/source pages.
- Pexels and Unsplash publish permissive general licenses for many commercial uses, but site-specific visual identity, releases, availability and individual provenance still require verification.
- Stock imagery is **never** to be described as actual Warley Works work.

## RAO LOOP™ v3.0 — Conservative finding
**Review:** Canonical website source preserved; v1.2 baseline verified.
**Analyze:** Real browser screenshot provenance remains the main bottleneck; downloaded preview does not substitute.
**Intelligence:** Official provider license terms reviewed; photographer-level evidence partial; GitHub Actions standard public runner is generally free, but CI action was blocked.
**Optimize:** Reusable local browser QA harness on same branch; test criteria include overflow, logo load, label association, internal anchors, demo form, JS and request method checks.
**Verify:** Script committed and source inspected; **actual canonical execution has not passed**.
**Execute:** Run the canonical checkout locally/Codespaces and attach results before adjudication.

**Provisional score:** 78/100 (carry-forward; no unsupported inflation). **Risk:** Moderate for internal drafting / High for public release. **Approval state:** CONTINUE ITERATION.
**Founder gate:** GO for local branch QA only. HOLD on visual acceptance, merge, deploy, domain/DNS, live intake and spending.

## METADATA LAW™
Owner/Authority: Founder. Current version: 1.3. Evidence: GitHub source, prior design uploads, separate standalone-preview report, this local test-harness commit. Cost impact: $0. Security lock: no real lead data. Next action: run QA against exact branch and review resulting screenshots before any approval.
