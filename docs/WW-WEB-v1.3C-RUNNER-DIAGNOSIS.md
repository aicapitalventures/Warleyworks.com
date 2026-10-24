# WARLEY WORKS — Website v1.3C: Runner Failure Diagnostic & Canonical QA Evidence Gate

**Record ID:** WW-WEB-V1.3C-DIAG-001  
**Version:** 1.0 — October 23, 2026 (Founder local date)  
**Classification:** Public-repository internal development evidence (no customer secrets)  
**Status:** VERIFIED PRE-STEP JOB FAILURES / ROOT CAUSE NOT ESTABLISHED / CANONICAL BROWSER QA BLOCKED  
**Decision authority:** WW-GOV-LOVE-001 v1.0 delegated technical authority, subject to Founder release and spending holds  
**Repository:** `aicapitalventures/Warleyworks.com` (public)  
**Working branch:** `feature/approved-ui-website-v1`  
**Pull request:** #1 (draft, unmerged at preflight)  
**Starting branch commit:** `a155851c960e604b0482602f5ca079c2070134bf`  
**Base `main` SHA:** `cfb9ed24aa691454ac99cfaa88be3570f689de47`  
**Governing sources:** Original Founder Warley Works logo, Founder-approved mockup, AICV Universal Lean Build Protocol™ v1.0, RAO LOOP™ v3.0, and existing v1.3B closeout.  
**Cost:** No new paid services, runner tiers, infrastructure or recurring costs authorized.

## 1. Actual GitHub Actions evidence

These values were fetched through the connected GitHub API; times are UTC.

| Field | Run #1 | Run #2 |
|---|---|---|
| Run ID | 40042652354 | 40042890084 |
| URL | https://github.com/aicapitalventures/Warleyworks.com/actions/runs/40042652354 | https://github.com/aicapitalventures/Warleyworks.com/actions/runs/40042890084 |
| Job ID | 120717067157 | 120717814099 |
| Commit SHA | `f3f676b430432101eab1a9deff03949c1fdb04b5` | `266eb05f0ffe211f8c6d1fa11dc6a3f8baf9bb89` |
| Runner label (workflow source) | `ubuntu-24.04` | `ubuntu-latest` |
| Status/conclusion | completed / failure | completed / failure |
| Job started UTC | 2026-10-23 23:59:21 | 2026-10-24 00:01:56 |
| Job completed UTC | 2026-10-23 23:59:23 | 2026-10-24 00:01:58 |
| `runner_id` | 0 | 0 |
| `runner_name` | blank | blank |
| `steps` | [] | [] |
| QA screenshots/artifacts | none | none |

The workflow file itself was accepted as a registered Actions run on the feature branch. In both runs the recorded job finished with zero executed steps. GitHub job-log retrieval was attempted previously but returned `404 BlobNotFound` (no usable logs).

## 2. Diagnostic conclusion and limits

**VERIFIED:** Both failures occurred before any recorded job step ran; no canonical Chromium test executed, and no screenshots or test assertions were produced.

**INFERRED, NOT PROVEN:** The empty runner assignment and zero-step jobs are consistent with a failure before runner execution (scheduling, preflight, initialization, or other platform/repository-level issue).

**UNKNOWN:** Exact causal explanation and specific corrective action. This evidence does **not** establish an account billing block, runner shortage, security restriction, permissions defect, or YAML issue.

**Tool-access boundary:** The installed GitHub connector permits run/job details but disallows fetching Actions settings and check-run annotations through its generic fetch endpoint. No changes were made to repository/account settings or to billing. Two runner-label variants have already produced the same failure, so speculative runner-label changes are stopped.

Official GitHub Actions troubleshooting and the community discussion of identical `runner_id=0`, empty-steps, `BlobNotFound` signatures justify inspecting run-level annotations and account-side runner diagnostics, but are not themselves evidence of this account's root cause.

## 3. Minimum owner-side evidence needed to close the failure

Read-only; do **not** change settings until a specific failure reason is visible.

1. Open the most recent [failed run](https://github.com/aicapitalventures/Warleyworks.com/actions/runs/40042890084) on GitHub while signed into the repository-owner account. Expand the **validate** job or top-level error banner. Capture the exact red error text and any annotations.
2. Open **Settings → Actions → General** for the Warley Works repository. Record the visible action-enablement and workflow-permission status; do not change anything yet.
3. Open **Settings → Actions → Runners** if present. Note whether standard GitHub-hosted runners are available/allowed. Do not create a self-hosted runner or select a premium tier.
4. If no repository-visible cause is displayed, prepare a GitHub Support request citing both run and job IDs, `runner_id=0`, blank runner name, zero steps, two standard runner labels and absent logs. Do not assert an unverified cause in the support request.

## 4. Canonical browser QA fallback, without publication

The already committed `tests/browser_qa.py`, `tests/smoke.mjs`, `tests/contrast.mjs` and existing [v1.3 runbook](WW-WEB-v1.3-QA.md) are the controlled fallback. Use an **already available, authorized local checkout or existing Codespaces environment**. Execute the canonical branch without a public endpoint. Capture screenshots at 320, 375, 768, 1024 and 1440 px, plus:
- Explicit browser Console and network failures, especially remote CSS background images;
- Full-form invalid and fictional-valid demonstrations; no customer data;
- Menu open/close, Escape behavior, focus and keyboard navigation;
- Horizontal overflow, missing labels and missing anchor targets;
- Formal screenshot comparison with the approved mockup and original brand treatment;
- Individual photographer/source and licensing records for all retained photography.

Do not reuse screenshots of the separately packaged standalone preview as canonical-site verification.

## 5. Defect status / decision ledger

| ID | Priority | Decision and current evidence |
|---|---|---|
| WW13C-01 | P0 validation | **BLOCKED:** GitHub Actions two pre-step failures; root-cause evidence unavailable through connector |
| WW13C-02 | P0 validation | **OPEN:** Canonical site screenshots and actual Chromium results missing |
| WW13C-03 | P1 brand | **OPEN:** Approved kitchen hero versus current remote site hero remains to be visually reconciled |
| WW13C-04 | P1 asset | **OPEN:** Photo URL availability, attribution and individual-image provenance incomplete |
| WW13C-05 | P1 accessibility | **OPEN:** Canonical keyboard, screen-reader and complete accessibility verification |
| WW13C-06 | P0 public release | **HOLD:** Compliance, verified contact, production form and privacy controls not cleared |
| WW13C-07 | P2 engineering | **PRESERVED:** Original traced SVG source checks and v1.2 contrast token (no regression asserted) |

**Authority decision:** GO for read-only diagnostics and local QA on an authorized no-cost environment. HOLD for further speculative CI configuration changes, Founder visual-acceptance lock, merge, staging/public deployment, DNS, payments, live lead intake and spending.

## 6. RAO LOOP™ v3.0

- **Review:** Current source and release constraints remain valid.
- **Analyze:** Both CI jobs failed before test execution with matching runner assignment symptoms.
- **Intelligence:** API job metadata established precisely; account settings and check annotations inaccessible.
- **Optimize:** Preserve actionable diagnostic evidence and stop unsupported configuration guessing.
- **Verify:** Failed runs and zero-step job records verified; no false browser test pass.
- **Execute:** Obtain explicit UI annotation/error evidence; then fix a verified cause or execute canonical tests in an existing authorized local environment.

**Score:** Carried-forward provisional **78/100 — Continue Iteration**, not re-scored. Official Approval Lock™ requires at least 90/100 plus the RAO v3.0 risk and execution gates; neither threshold nor readiness is established here.  
**Risk:** Moderate for isolated development, high for public release; unresolved compliance items may be critical within public-release scope.  
**Final GO/HOLD:** GO for read-only diagnostics/local QA; HOLD for launch and approval.

## MDL™ / METADATA LAW™

**Project:** Warley Works | **Artifact:** WW-WEB-V1.3C-DIAG-001 | **Version:** 1.0 | **Reasoning:** High | **Authority:** WW-GOV-LOVE-001, bounded technical delegation | **Source:** API readback of two Actions jobs and original Founder sources | **Cost impact:** $0 new infrastructure | **Immutable lock:** original logo, approved UI, repository history and explicit release prohibitions | **Open gate:** owner-visible GitHub Actions error/annotation or canonical checkout browser evidence | **Next action:** diagnose the exact failed-job banner and run authentic page tests without public deployment.
