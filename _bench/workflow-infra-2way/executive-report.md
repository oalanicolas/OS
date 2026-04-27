# Executive Report: workflow vs gh-aw

**Date:** 2026-04-19
**Type:** pair
**Slug:** workflow-infra-2way
**Dimension pack:** workflow-infra (v1.0)

---

## Executive Summary

Vercel Workflow SDK (`workflow`) and GitHub Agentic Workflows (`gh-aw`) share a surface-level similarity — both orchestrate multi-step async work including AI tasks — but they sit on opposite sides of a paradigm divide. workflow is a *durable-function runtime*: workflows are TypeScript async functions whose progress is persisted as an event log and deterministically replayed across cold starts, failures and scale events. gh-aw is an *agentic CI compiler*: markdown files with YAML frontmatter compile to standard GitHub Actions `.lock.yml` workflows that run with safety rails (read-only default, AWF firewall, `safe-outputs` handler, SHA-pinned actions, secret redaction, approval gates via GitHub Environments). Weighted against the `workflow-infra` pack (durability 22% + event_log 18% + retries 15% + parallelism 13% + language 15% + lock-in 17%), workflow scores 77.08 and gh-aw scores 58.20 — a +18.88-pt lead for workflow driven almost entirely by the three durability-adjacent dimensions. On governance (not scored by this pack) gh-aw is clearly ahead, and the gap analysis identifies several low-complexity wins workflow could absorb from it.

---

## Key Metrics

| Metric | Value |
|--------|-------|
| Overall Winner | workflow (+18.88 pts weighted) |
| Dimensions analyzed | 6 |
| workflow wins | 3 of 6 (durability, retry_semantics, event_log) |
| gh-aw wins | 3 of 6 (parallelism, language_support, cloud_lock_in) |
| Ties | 0 |
| Gaps workflow | 9 (0 P0, 2 P1, 4 P2, 3 P3) |
| Gaps gh-aw | 8 (2 P0, 2 P1, 3 P2, 1 P3) |
| Confidence overall | HIGH |

---

## Scorecard Summary

| Dimension | Weight | workflow | gh-aw | Delta | Winner |
|-----------|:------:|:--------:|:-----:|------:|:------:|
| Durability | 22% | 92/100 | 45/100 | +47 | workflow |
| Retry Semantics | 15% | 90/100 | 45/100 | +45 | workflow |
| Event Log | 18% | 95/100 | 35/100 | +60 | workflow |
| Parallelism | 13% | 78/100 | 80/100 | -2 | gh-aw |
| Language Support | 15% | 45/100 | 75/100 | -30 | gh-aw |
| Cloud Lock-in (inverse) | 17% | 55/100 | 80/100 | -25 | gh-aw |
| **Weighted total** | **100%** | **77.08/100** | **58.20/100** | **+18.88** | **workflow** |

---

## Dimension Analysis

### Durability (22%)

**workflow: 92/100** | **gh-aw: 45/100** | Delta: +47

workflow persists every step, hook, sleep and run transition to an event log; state is reconstructed by deterministic replay. gh-aw inherits GitHub Actions' coarser-grained durability — a retry means re-running the whole `workflow_run`, and there is no per-LLM-turn memoization. For long agentic flows that must survive cold starts mid-task, only workflow provides structural durability.

**Key signals:**
- workflow: per-step persistence via `events-consumer.ts` — `OS/workflow/packages/core/src/events-consumer.ts`
- workflow: event-sourcing doc — `OS/workflow/docs/content/docs/how-it-works/event-sourcing.mdx`
- gh-aw: Actions-level persistence; `safe-outputs` dedupes writes but not agent turns — `OS/gh-aw/pkg/workflow/safe_outputs_validation.go`

**Gaps in this dimension:** GAP-B-001 (durable step persistence, P0), GAP-B-004 (durable sleep, P2), GAP-B-008 (exactly-once memoization, P1).

---

### Retry Semantics (15%)

**workflow: 90/100** | **gh-aw: 45/100** | Delta: +45

workflow ships `FatalError` / `RetryableError` with programmable `retryAfter` (duration strings or ms) and default-3-retries. gh-aw has no equivalent typed retry layer; retries live at the Actions step level (third-party retry actions, `continue-on-error`) and the per-engine knobs `max-turns` / `max-continuations` limit chatter rather than provide structured retry.

**Key signals:**
- workflow: typed errors + retryAfter — `OS/workflow/docs/content/docs/foundations/errors-and-retries.mdx`, `OS/workflow/packages/errors/`
- gh-aw: engine knobs documented — `OS/gh-aw/docs/src/content/docs/reference/engines.md`

**Gaps in this dimension:** GAP-B-003 (typed retry controls, P1).

---

### Event Log (18%)

**workflow: 95/100** | **gh-aw: 35/100** | Delta: +60

This is the dimension where the paradigms diverge most. workflow's architecture is fully event-sourced, with lifecycles for Runs/Steps/Hooks/Waits driven by events and determinism guaranteed via `seedrandom` + ULID monotonic IDs. gh-aw's audit story is a composition of `.lock.yml` commit history + GitHub Actions audit + `gh aw audit` — there is no replay.

**Key signals:**
- workflow: event-sourcing as persistence model — `OS/workflow/docs/content/docs/how-it-works/event-sourcing.mdx`
- workflow: `hydrateResourceIO` observability helper — `OS/workflow/packages/core/src/observability.ts`
- gh-aw: `gh aw audit` documented — `OS/gh-aw/docs/src/content/docs/reference/audit.md`

**Gaps in this dimension:** GAP-B-002 (deterministic replay, P0), GAP-B-007 (step-level observability, P2).

---

### Parallelism (13%)

**workflow: 78/100** | **gh-aw: 80/100** | Delta: -2

Closest dimension. workflow uses native `Promise.all` / `Promise.race` that work durably; gh-aw inherits Actions `matrix:` and ships dual concurrency control (per-workflow keyed by issue/PR/branch + per-engine `gh-aw-{engine-id}`). gh-aw narrowly edges out because the concurrency limits are first-class; workflow doesn't expose an equivalent knob.

**Key signals:**
- workflow: Promise.all in steps — `OS/workflow/docs/content/docs/foundations/common-patterns.mdx`
- gh-aw: dual concurrency groups — `OS/gh-aw/docs/src/content/docs/reference/concurrency.md`

**Gaps in this dimension:** GAP-A-007 (dual-level concurrency for workflow, P3).

---

### Language Support (15%)

**workflow: 45/100** | **gh-aw: 75/100** | Delta: -30

workflow is JS/TS-only — deliberate, but excludes everyone else. gh-aw is markdown-native (polyglot at tool surface) with a WASM compiler build for editor integrations and a per-engine feature matrix (Copilot/Claude/Codex/Gemini/Crush).

**Key signals:**
- workflow: JS/TS manifest — `OS/workflow/packages/core/package.json`
- gh-aw: engines doc — `OS/gh-aw/docs/src/content/docs/reference/engines.md`
- gh-aw: WASM build — `OS/gh-aw/cmd/gh-aw-wasm/`

**Gaps in this dimension:** GAP-A-001 (markdown DSL, P2), GAP-A-002 (multi-engine, P2), GAP-A-008 (sample library, P3), GAP-B-006 (framework integrations, P3).

---

### Cloud Lock-in (inverse) (17%)

**workflow: 55/100** | **gh-aw: 80/100** | Delta: -25

Higher is better. gh-aw compiles to standard GitHub Actions YAML running on GitHub.com, GHES or self-hosted runners — a vast existing self-host footprint. workflow has a pluggable `world` abstraction but the easy-path production backend is Vercel.

**Key signals:**
- workflow: `world-vercel` as production path — `OS/workflow/packages/world-vercel/`
- workflow: self-host via `world-postgres` — `OS/workflow/packages/world-postgres/`
- gh-aw: standard Actions runtime — `OS/gh-aw/README.md`

**Gaps in this dimension:** GAP-A-003 (safe-outputs, P1), GAP-A-004 (AWF sandbox, P2), GAP-A-005 (secret redaction, P1), GAP-A-006 (approval gates, P2), GAP-A-009 (SHA pinning, P3), GAP-B-005 (pluggable storage, P2).

---

## Gap Highlights

### Top gaps de workflow (o que gh-aw tem)

| # | Capability | Impact | Complexity | Priority | Dimension |
|---|-----------|:------:|:----------:|:--------:|-----------|
| 1 | Safe-outputs handler for validated writes | HIGH | MED | P1 | cloud_lock_in |
| 2 | Secret redaction in logs | MED | LOW | P1 | cloud_lock_in |
| 3 | Multi-engine agent support | MED | MED | P2 | language_support |
| 4 | Built-in agent sandbox (AWF firewall) | MED | HIGH | P2 | cloud_lock_in |
| 5 | First-class approval gates (`on.manual-approval`) | MED | LOW | P2 | cloud_lock_in |

**Total:** 9

### Top gaps de gh-aw (o que workflow tem)

| # | Capability | Impact | Complexity | Priority | Dimension |
|---|-----------|:------:|:----------:|:--------:|-----------|
| 1 | Durable step persistence | HIGH | HIGH | P0 | durability |
| 2 | Event-sourced deterministic replay | HIGH | HIGH | P0 | event_log |
| 3 | Typed retry controls (FatalError/RetryableError) | HIGH | MED | P1 | retry_semantics |
| 4 | Exactly-once side-effect memoization | MED | HIGH | P1 | durability |
| 5 | Durable sleep primitive | MED | MED | P2 | durability |

**Total:** 8

---

## Strategic Recommendations

### 1. Use both — they compose, they don't compete

For an enterprise adopting AI-assisted delivery end-to-end, the right answer is both: gh-aw for safe, auditable, markdown-authored agentic CI on GitHub; workflow for durable execution of long-running or multi-step agentic flows the CI triggers. gh-aw's `safe-outputs` validates what comes back to the repo; workflow's event log handles resume-after-failure inside long tasks.

- **Target:** both
- **Addresses:** paradigm split exposed by the scorecard
- **Expected impact:** avoids forcing one tool to do the other's job
- **Priority:** P1

### 2. Absorb gh-aw's governance primitives into workflow (low-hanging fruit)

Secret redaction (GAP-A-005), a safe-outputs-style validated-write layer (GAP-A-003) and a standard approval-gate primitive (GAP-A-006) are all low-to-medium complexity and close the three P1/P2 governance gaps in workflow. Doing so raises workflow's cloud_lock_in dimension from 55 towards 75+.

- **Target:** workflow
- **Addresses:** GAP-A-003, GAP-A-005, GAP-A-006
- **Expected impact:** +15–20 pts in cloud_lock_in
- **Priority:** P1

### 3. For gh-aw, document the "delegate durable sub-runs" pattern rather than rebuild durability

gh-aw's P0 gaps (durable persistence, deterministic replay) are paradigm-mismatched — rebuilding event sourcing inside Actions would destroy what makes gh-aw valuable. A better response is a documented pattern: a gh-aw workflow triggers a durable engine (workflow, Temporal, Inngest) for sub-tasks that must survive cold starts, then collects results via `safe-outputs`. Clarifies positioning without scope creep.

- **Target:** gh-aw
- **Addresses:** GAP-B-001, GAP-B-002 (via documentation, not code)
- **Expected impact:** narrows addressable surface cleanly
- **Priority:** P0

### 4. Introduce a typed retry convention in gh-aw agent outputs

Borrowing from workflow's `RetryableError`, define a JSON sentinel agents can emit (e.g., `{"__retry__": {"after": "30s"}}`) that the safe-outputs handler interprets as "schedule a re-trigger". Keeps agent ergonomics while running on Actions.

- **Target:** gh-aw
- **Addresses:** GAP-B-003
- **Expected impact:** +15 pts in retry_semantics
- **Priority:** P1

### 5. Extend safe-outputs into a full idempotency story (gh-aw)

Adopt a stable idempotency-key convention across agent turns so re-runs don't re-comment or re-PR. Builds on existing safe-outputs dedupe.

- **Target:** gh-aw
- **Addresses:** GAP-B-008
- **Expected impact:** +5 pts in durability
- **Priority:** P1

---

## When to Pick Which

### Choose workflow if…

- You're writing long-running or multi-step async logic in a JavaScript / TypeScript codebase.
- You need deterministic replay or "resume mid-task after a cold start" semantics.
- You want programmable retry controls (typed errors, custom backoff) baked into the language surface.
- You're already on Vercel or willing to run `@workflow/world-postgres` self-hosted.
- You're building AI agents that must survive scale events and concurrent executions.

### Choose gh-aw if…

- You want AI-driven automation of repo-centric tasks (triage, PR review, docs upkeep) that runs on GitHub Actions.
- Safety is paramount: read-only defaults, validated writes, firewall egress control, SHA-pinned actions, approval gates, secret redaction.
- Your team prefers markdown-native authoring and multi-engine routing (Copilot/Claude/Codex/Gemini).
- You want workflows that are diff-able as prose and installable via a `gh aw add` marketplace.
- You don't need durable resume-after-crash semantics at the LLM-step level.

### Consider both (complementary) if…

- You're standing up an end-to-end AI engineering platform: gh-aw handles CI-layer agentic automation with safety rails; workflow handles durable sub-tasks triggered from gh-aw and reports back through safe-outputs.
- You have Node.js apps that need durable workflow execution *and* repo-level agentic safety rails.

---

## Methodology

### Data Sources

| Subject | Source | Method | Confidence |
|---------|--------|--------|------------|
| workflow | `OS/workflow/` + https://github.com/vercel/workflow + https://workflow-sdk.dev | filesystem-scan + doc-scan | HIGH |
| gh-aw | `OS/gh-aw/` + https://github.com/github/gh-aw + https://github.github.com/gh-aw | filesystem-scan + doc-scan | HIGH |

### Scoring Method

- **Dimension pack:** workflow-infra (6 dimensions)
- **Score range:** 0–100
- **Weighting:** pack weights sum to 1.00 (durability 22% + retry 15% + event_log 18% + parallelism 13% + language 15% + lock-in 17%)
- **Signals:** each score ≥90 required 2+ observable signals
- **Confidence rollup:** all dimensions HIGH → overall HIGH

### Artifacts Generated

| Artifact | File | Status |
|----------|------|:------:|
| Metadata | `metadata.json` | OK |
| Inventory workflow | `inventory-workflow.json` | OK |
| Inventory workflow (MD) | `inventory-workflow.md` | OK |
| Inventory gh-aw | `inventory-gh-aw.json` | OK |
| Inventory gh-aw (MD) | `inventory-gh-aw.md` | OK |
| Comparison Matrix | `comparison-matrix.json` | OK |
| Comparison Matrix (MD) | `comparison-matrix.md` | OK |
| Scorecard | `scorecard.json` | OK |
| Scorecard (MD) | `scorecard.md` | OK |
| Gap Analysis | `gap-analysis.json` | OK |
| Gap Analysis (MD) | `gap-analysis.md` | OK |
| Battle Card | `battle-card.md` | OK |
| Executive Report | `executive-report.md` | OK |

### Limitations

- Community metrics (GitHub stars, download counts) not collected — local-first policy of the skill; gh-aw's README lists 100+ contributors but no quantitative GitHub traction metric was pulled.
- No reproducible cross-tool throughput benchmark: workflow ships `pnpm bench` for its runtime, gh-aw runs on Actions infrastructure whose latency depends on the runner pool.
- Both are pre-stable (workflow beta 5.0.0-beta.2; gh-aw pre-1.0 v0.40.1). Rapid velocity means scores could shift within weeks.
- Scoring is scoped to the `workflow-infra` pack; a governance-oriented pack would tilt materially toward gh-aw.

---

## Appendix: Source Artifacts

All artifacts in `OS/_bench/workflow-infra-2way/`:

| # | File | Type | Format |
|---|------|------|--------|
| 1 | `metadata.json` | Metadata | JSON |
| 2 | `inventory-workflow.json` | Inventory | JSON |
| 3 | `inventory-workflow.md` | Inventory | MD |
| 4 | `inventory-gh-aw.json` | Inventory | JSON |
| 5 | `inventory-gh-aw.md` | Inventory | MD |
| 6 | `comparison-matrix.json` | Matrix | JSON |
| 7 | `comparison-matrix.md` | Matrix | MD |
| 8 | `scorecard.json` | Scoring | JSON |
| 9 | `scorecard.md` | Scoring | MD |
| 10 | `gap-analysis.json` | Gaps | JSON |
| 11 | `gap-analysis.md` | Gaps | MD |
| 12 | `battle-card.md` | Battle card | MD |
| 13 | `executive-report.md` | Report | MD |

---

_Generated by os-bench bench-executive-report task | Template v1.0_
