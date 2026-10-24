# WW-WEB-v1.3D — Runner Root-Cause Review, Canonical QA Fallback & Decision Closeout

**Version:** v1.0 | **Status:** FOUNDER REVIEW — QA BLOCKED / ROOT CAUSE UNVERIFIED  
**Date:** 2026-10-23 (Founder local date)  
**Authority:** LOVE v1.0, bounded technical delegation under WW-GOV-LOVE-001  
**Repo / PR:** `aicapitalventures/Warleyworks.com`, Draft PR #1, `feature/approved-ui-website-v1`  
**Controlling sources:** Original Founder logo (389×244 PNG), approved website screenshot (1448×1086 PNG), AICV Universal Lean Build Protocol™ v1.0, RAO LOOP™ v3.0, v1.3C diagnostic.  
**Cost:** $0 additional infrastructure/commitments.  
**Release:** HOLD — do not merge, deploy, publish, alter DNS, activate intake, or incur costs.

## A. Runner root-cause evaluation — no invented attribution

The user requested remediation using the GitHub Actions error annotation for run 40042890084. **No annotation text was supplied in the user message** and the installed GitHub connector does not expose this check-run annotation or the repository's Actions account-setting page.

**Verified by authenticated GitHub job/run API:**

| Signal | First attempt | Second attempt |
|---|---|---|
| Run | [40042652354](https://github.com/aicapitalventures/Warleyworks.com/actions/runs/40042652354) | [40042890084](https://github.com/aicapitalventures/Warleyworks.com/actions/runs/40042890084) |
| Job | 120717067157 | 120717814099 |
| Runner workflow label | ubuntu-24.04 | ubuntu-latest |
| Runner assigned | `runner_id: 0`, empty name | `runner_id: 0`, empty name |
| Recorded steps | [] | [] |
| Result | Failure | Failure |
| Duration | ~2 sec | ~2 sec |
| Artifact screenshots | None | None |

The observed cause level is a **pre-step failure**; the **precise underlying cause is not established**. Similar community reports are not account-specific evidence. The connector returned `BlobNotFound` for job logs, and fetching Actions permissions/check-run annotations was disallowed. No billing, runner or permission diagnosis has been invented, and no third speculative runner configuration has been applied.

**Required owner-side evidence:** Read the failed run's red banner and job annotations. If needed, inspect repository Settings → Actions → General and runner availability **read-only**. If the UI offers no explanation, escalate with both run/job IDs to GitHub Support.

## B. Remediation within verified control

The canonical branch now includes a fallback browser script `tests/inline_browser_qa.py` that reads **actual checkout file bytes** from `index.html`, `styles.css`, `script.js` and all three committed SVGs, captures source SHA-256 hashes, and uses Playwright `set_content()` to render an in-memory document where local `file://` and `localhost` browsing is blocked.

The fallback is reversible, free, requires an authorized checkout and an existing Playwright installation, and **does not** publish, upload, deploy or send form data. It captures five screenshots (320, 375, 768, 1024, 1440px), CSS layout checks, logo render, named form demo tests, menu interactions and JS errors. It logs failed external requests. It must be treated as **source-derived in-memory browser QA**, not as an HTTP deployment test; remote photo availability/licensing and full WCAG review still require separate checks.

The new `.gitignore` excludes `qa-artifacts/`, virtual environments and Python cache files from accidental source commits.

**Actual test execution:** The test script was committed and source-inspected; it **has not run against the canonical checkout in this environment**, because the container cannot reach GitHub and the GitHub-hosted job fails before steps start. No screenshots have been fabricated, and this source change is not claimed to pass its own test suite.

### Controlled execution commands (existing authorized no-cost checkout)

```bash
git status --short --branch
git rev-parse HEAD
python3 tests/inline_browser_qa.py
node tests/smoke.mjs
node tests/contrast.mjs
```

If Playwright is absent, use an already authorized Python/Playwright environment or obtain explicit approval before any potentially billable new infrastructure. Archive the generated `qa-artifacts/in-memory/` screenshots and report separately from canonical HTTP-browser evidence.

## C. Source-based verification, not a browser PASS

GitHub connector readbacks of `index.html`, `styles.css`, `script.js`, logo SVGs, and the new fallback script confirm:
- Existing v1.2 files remain unchanged, including founder-traced logo symbols, navy/brass/ivory theme, and small-text contrast fix.
- **No duplicate HTML IDs** and **no missing fragment-link targets** from source parsing.
- Canonical homepage headline remains **Reliable Work. Lasting Value.**
- The estimate form is explicitly demo-only, `event.preventDefault()` is present, and JavaScript does not invoke `fetch`, `XMLHttpRequest` or `sendBeacon`.
- Responsive media-query breakpoints at 360, 640 and 860 px are retained.
- Seven external photo URL references remain in CSS and have **not been verified as successfully loaded** in the canonical browser. Photo-specific license/provenance remains open.

These observations are **static source checks only**. Mobile behavior, visual parity, browser accessibility and image delivery remain open.

## D. Defect / decision ledger

| ID | Priority | Decision | State |
|---|---|---|---|
| WW13D-01 | P0 | Require exact Actions annotation or owner-visible run error to assign root cause | BLOCKED, NOT A CODE FIX |
| WW13D-02 | P0 | Validate exact checkout in Chromium via no-publication fallback | TEST SCRIPT COMMITTED, RUN PENDING |
| WW13D-03 | P1 | Compare genuine 320/375/768/1024/1440 screenshots with Founder approved reference | OPEN |
| WW13D-04 | P1 | Validate and localize legally usable real or properly labeled stock imagery | OPEN |
| WW13D-05 | P1 | Check tab order, focus, screen-reader semantics and responsive touch targets | OPEN |
| WW13D-06 | P0 public | License/insurance/DBA, verified contact, secure intake and privacy | HARD HOLD |
| WW13D-07 | P2 hygiene | Keep local QA output out of Git history | COMPLETED IN `.gitignore` |
| WW13D-08 | P0 governance | Keep Draft PR, original source history and cost/release holds | VERIFIED |

## E. RAO LOOP™ v3.0

**Review:** Source and two failed Actions runs inspected.  
**Analyze:** Pre-step runner failure is established; root cause isn't.  
**Intelligence:** Authenticated API lacks the error annotation; no account-specific setting can be inferred.  
**Optimize:** Added source-derived, zero-publication browser fallback and test output hygiene; no speculative runner setting edits.  
**Verify:** New files exist on branch; source checks passed. Full browser execution and visual fidelity **NOT VERIFIED**.  
**Execute:** Obtain GitHub Actions annotation or run the fallback in an existing authorized checkout. Evaluate real screenshot evidence before acceptance.

**Score:** Retain historical provisional **78/100** under the ten-category rubric, **Continue Iteration** (70–79), not an Official Approval Lock™. This is not a newly validated score.

**Decision:** **GO** for read-only runner diagnostics, zero-cost branch testing, reversible in-scope fixes. **HOLD** for visual acceptance, PR merge, public staging/production, DNS, live data and spending.

## MDL™ / METADATA LAW™
Project: WARLEY WORKS. Artifact: WW-WEB-v1.3D-QA. Version: 1.0. Authority: WW-GOV-LOVE-001. Source: authenticated GitHub run/job/readbacks, Founder assets, official RAO rubric. Status: PARTIAL VALIDATION — BLOCKER OPEN. Risk: MODERATE internal / HIGH public release. Infrastructure cost: $0. Next: owner-visible Actions error/annotation **or** execute existing-checkout in-memory QA; preserve all release and financial locks.

## F. Post-commit verification — third CI attempt

The commit adding `tests/inline_browser_qa.py` triggered a third GitHub Actions run automatically through the existing `tests/**` workflow path filter. **Run [40052254819](https://github.com/aicapitalventures/Warleyworks.com/actions/runs/40052254819)**, job `120747266388`, completed with `failure`, `runner_id=0`, empty runner name, zero job steps, no screenshot artifacts, and approximately three seconds between job start and completion. This reproduces the pre-step symptom for the **third** time; it still does **not** prove a specific underlying root cause. No further speculative runner/permissions/billing mutation is authorized by this evidence. The release and validation HOLD remains unchanged.
