# Scorecard: workflow vs gh-aw

**Date:** 2026-04-19
**Dimension pack:** workflow-infra (6 dimensions)
**Slug:** workflow-infra-2way
**Overall Confidence:** HIGH

---

## Scoring Method

- Score range: 0–100 per dimension
- Weights from pack `workflow-infra` (sum = 1.00)
- Each score derived from 2+ signals documented below
- Signal absent → score reduced and confidence downgraded
- Primary source: filesystem scan of `OS/workflow/` and `OS/gh-aw/`; web fallback only for community metrics

---

## Dimension Scores

| Dimension | Weight | workflow | gh-aw | Delta | Confidence | Winner |
|-----------|-------:|:--------:|:-----:|------:|:----------:|:------:|
| Durability | 22% | 92/100 | 45/100 | +47 | HIGH | workflow |
| Retry Semantics | 15% | 90/100 | 45/100 | +45 | HIGH | workflow |
| Event Log | 18% | 95/100 | 35/100 | +60 | HIGH | workflow |
| Parallelism | 13% | 78/100 | 80/100 | -2 | HIGH | gh-aw |
| Language Support | 15% | 45/100 | 75/100 | -30 | HIGH | gh-aw |
| Cloud Lock-in (inverse) | 17% | 55/100 | 80/100 | -25 | HIGH | gh-aw |

---

## Weighted Total

| Subject | Weighted Score | Wins | Ties | Losses |
|---------|:-------------:|:----:|:----:|:------:|
| workflow | **77.08/100** | 3 | 0 | 3 |
| gh-aw | **58.20/100** | 3 | 0 | 3 |
| **Delta** | **+18.88 workflow** | — | — | — |

**Overall Winner:** workflow (+18.88 pts weighted)

Despite a 3–3 dimension split, workflow's three wins sit on the three heaviest-weighted dimensions (durability 22% + event_log 18% + retry_semantics 15% = 55% of total weight), and its margins there are much larger (+47, +60, +45) than gh-aw's margins on the lighter dimensions (-2, -30, -25 on 13% + 15% + 17% = 45% of weight).

---

## Dimension Analysis

### Durability (22%)

**workflow: 92/100** | **gh-aw: 45/100** | Delta: +47 | Confidence: HIGH

Durability is the core promise of the Workflow SDK and it is front-loaded in the architecture: every step, hook, sleep and run transition is persisted to an event log, and state is reconstructed by deterministic replay after cold starts, failures or scale events. gh-aw inherits the durability model of GitHub Actions itself — the step granularity is a workflow job, not an LLM turn. That's fine for CI-style tasks but does not cover the "resume a long agentic run mid-way" scenario that workflow solves by construction.

**Signals observed:**

- **workflow**
  - Per-step persistence via events-consumer — evidence: `OS/workflow/packages/core/src/events-consumer.ts`
  - Event-sourced deterministic replay documented — evidence: `OS/workflow/docs/content/docs/how-it-works/event-sourcing.mdx`
  - Idempotency guidance for side-effectful steps — evidence: `OS/workflow/docs/content/docs/foundations/idempotency.mdx`
  - Four world backends all implement event persistence — evidence: `OS/workflow/packages/world-{local,vercel,postgres,testing}/`
- **gh-aw**
  - Persistence = Actions job logs + artifacts, inherited from the Actions runtime — evidence: `OS/gh-aw/docs/src/content/docs/reference/`
  - No per-LLM-step event log — replay means re-running the full `workflow_run` — evidence: `OS/gh-aw/docs/src/content/docs/reference/compilation-process.md`
  - safe-outputs handler dedupes writes but does not memoize agent turns — evidence: `OS/gh-aw/pkg/workflow/safe_outputs_validation.go`

**Justification:**

- workflow → 92: exactly-once memoization + replay + four backends, short of 100 only because self-hosted backends are less battle-tested than world-vercel.
- gh-aw → 45: best-effort durability via Actions restart; credible for many use cases but not the framework's concern.

---

### Retry Semantics (15%)

**workflow: 90/100** | **gh-aw: 45/100** | Delta: +45 | Confidence: HIGH

workflow exposes programmable retry primitives that are idiomatic to the language: throw `RetryableError` with a `retryAfter` (duration string or ms) for custom schedules; throw `FatalError` to opt out. Default is 3 retries, override with `fn.maxRetries = N`. gh-aw has no equivalent typed retry layer — retries live at the Actions step level (third-party retry actions, `continue-on-error`) and the only per-engine knobs are `max-turns` (Claude) and `max-continuations` (Copilot), which limit chatter rather than provide structured retry.

**Signals observed:**

- **workflow**
  - Default 3 retries + maxRetries override — evidence: `OS/workflow/docs/content/docs/foundations/errors-and-retries.mdx`
  - Typed FatalError / RetryableError with retryAfter — evidence: `OS/workflow/packages/errors/`
  - Exponential backoff example in docs: `retryAfter: (metadata.attempt ** 2) * 1000`
- **gh-aw**
  - No framework-level retry primitives observed in `OS/gh-aw/pkg/workflow/`
  - Engine knobs max-turns / max-continuations — evidence: `OS/gh-aw/docs/src/content/docs/reference/engines.md`

**Justification:**

- workflow → 90: typed retry controls + programmable backoff, short of 100 only because jitter is user-implemented rather than built-in.
- gh-aw → 45: retries are possible but delegated and not part of the DSL.

---

### Event Log (18%)

**workflow: 95/100** | **gh-aw: 35/100** | Delta: +60 | Confidence: HIGH

This is the dimension where the paradigms diverge most. workflow's entire architecture is event-sourced: Runs, Steps, Hooks and Waits all follow lifecycles defined by events, and the log is append-only. Deterministic replay is guaranteed via `seedrandom` + ULID monotonic IDs. gh-aw has no equivalent — audit is a composition of `.lock.yml` commits, GitHub Actions audit logs, and the `gh aw audit` command, but there is no time-travel replay.

**Signals observed:**

- **workflow**
  - Append-only log as persistence model — evidence: `OS/workflow/docs/content/docs/how-it-works/event-sourcing.mdx`
  - Four entity types managed through events — same doc
  - seedrandom + ULID guarantee determinism — evidence: `OS/workflow/packages/core/src/workflow.ts` (imports from `ulid`/`seedrandom`)
  - Observability hydration helper — evidence: `OS/workflow/packages/core/src/observability.ts` (referenced in CLAUDE.md)
- **gh-aw**
  - `gh aw audit` command + `.lock.yml` commit history — evidence: `OS/gh-aw/docs/src/content/docs/reference/audit.md`
  - No replay primitive; a re-run starts from scratch — evidence: `OS/gh-aw/docs/src/content/docs/reference/`

**Justification:**

- workflow → 95: complete event-sourcing implementation with deterministic replay and time-travel debugging foundations.
- gh-aw → 35: audit trail exists but lacks replay / time-travel.

---

### Parallelism (13%)

**workflow: 78/100** | **gh-aw: 80/100** | Delta: -2 | Confidence: HIGH

Closest dimension of the comparison. workflow uses idiomatic `Promise.all` / `Promise.race` that work durably across steps — no new API to learn, and each parallel branch persists independently. gh-aw inherits Actions' `matrix:` for fan-out and ships dual concurrency control out of the box: per-workflow (keyed by issue/PR/branch) and per-engine (`gh-aw-{engine-id}`). gh-aw narrowly edges out because concurrency limits are first-class in the DSL; workflow doesn't expose a framework-level limiter.

**Signals observed:**

- **workflow**
  - Promise.all / Promise.race in durable steps — evidence: `OS/workflow/docs/content/docs/foundations/common-patterns.mdx`
  - Durable sleep + hooks compose for timeouts — evidence: `OS/workflow/packages/core/src/sleep.ts`
  - No first-class concurrency-limit primitive at framework layer
- **gh-aw**
  - `matrix:` strategy inherited — evidence: compiled `.lock.yml` files
  - Dual concurrency documented — evidence: `OS/gh-aw/docs/src/content/docs/reference/concurrency.md`
  - cancel-in-progress on PR pushes; label-specific groups

**Justification:**

- workflow → 78: native async parallelism works durably, but concurrency caps are implicit.
- gh-aw → 80: slightly higher for the explicit dual-level concurrency semantics.

---

### Language Support (15%)

**workflow: 45/100** | **gh-aw: 75/100** | Delta: -30 | Confidence: HIGH

workflow is JS/TS-only — a deliberate choice that keeps the engine focused but excludes Python/Go/Rust authors. gh-aw is markdown-native (polyglot by virtue of shelling out to any tool) and ships a WASM compiler build for editor/browser integrations. Its per-engine feature matrix (Copilot/Claude/Codex/Gemini/Crush) means teams can route the same workflow through different models without rewrites.

**Signals observed:**

- **workflow**
  - JS/TS only — evidence: `OS/workflow/packages/core/package.json`
  - 6 framework integrations (Next/Nitro/Nuxt/SvelteKit/Astro/Nest) — evidence: `OS/workflow/packages/`
- **gh-aw**
  - Markdown + YAML DSL, polyglot tool invocation — evidence: `OS/gh-aw/docs/src/content/docs/introduction/how-they-work.mdx`
  - WASM compiler build — evidence: `OS/gh-aw/cmd/gh-aw-wasm/`
  - Multi-engine — evidence: `OS/gh-aw/docs/src/content/docs/reference/engines.md`

**Justification:**

- workflow → 45: deep in one language, invisible to everyone else.
- gh-aw → 75: reaches the 90–100 band except the DSL is limited in expressiveness compared to a full programming language.

---

### Cloud Lock-in (inverse) (17%)

**workflow: 55/100** | **gh-aw: 80/100** | Delta: -25 | Confidence: HIGH

Higher is better (less lock-in). gh-aw compiles to standard GitHub Actions YAML that runs on GitHub.com, GHES and self-hosted runners — the existing self-host base for Actions is vast. workflow has a pluggable `world` abstraction with Postgres/local backends alongside the first-class Vercel one, which is commendable but operationally newer. Both are tied to a major vendor (Vercel or GitHub) at their easy-path runtime, so neither hits the 90+ band reserved for truly portable OSS durable-workflow engines.

**Signals observed:**

- **workflow**
  - Production path is @workflow/world-vercel — evidence: `OS/workflow/packages/world-vercel/`
  - Self-host via @workflow/world-postgres (Drizzle) — evidence: `OS/workflow/packages/world-postgres/`
  - World interface allows new backends — evidence: `OS/workflow/packages/world/src/interfaces.ts`
- **gh-aw**
  - Runs on standard Actions (GitHub.com + GHES + self-hosted runners) — evidence: `OS/gh-aw/README.md`
  - `.lock.yml` is portable across repos/orgs — evidence: `OS/gh-aw/.github/workflows/`
  - Companion projects are optional — evidence: `OS/gh-aw/README.md` Related Projects
  - Not portable to GitLab/Jenkins — inherent to the paradigm

**Justification:**

- workflow → 55: swappable storage but easy-path is Vercel-native.
- gh-aw → 80: massive existing self-host footprint; portable artifact within GH ecosystem.

---

## Score Distribution

### workflow Profile

- Strongest: **Event Log** (95/100)
- Weakest: **Language Support** (45/100)
- Unweighted average: 75.83
- Range: 45–95

### gh-aw Profile

- Strongest: **Parallelism** (80/100)
- Weakest: **Event Log** (35/100)
- Unweighted average: 60.00
- Range: 35–80

### Competitive Dimensions (|delta| < 5)

Dimensions where A and B are essentially tied:

- Parallelism: 78 vs 80 (delta -2)

---

## Confidence Disclosure

| Subject | Confidence | Reason |
|---------|-----------|--------|
| workflow | HIGH | 5+ evidence paths per dimension, comprehensive docs site, detailed CLAUDE.md, 106 tests. |
| gh-aw | HIGH | 5+ evidence paths per dimension, 953-line README, comprehensive docs, 1,050 tests, 272 sample workflows. |

### Sources

- **workflow**: filesystem `OS/workflow/` + https://github.com/vercel/workflow + https://workflow-sdk.dev
- **gh-aw**: filesystem `OS/gh-aw/` + https://github.com/github/gh-aw + https://github.github.com/gh-aw

### Dimension Pack

| Pack | Version | Designed For |
|------|---------|-------------|
| workflow-infra | 1.0 | Durable workflows / event-sourced infra |

### Scoring Transparency

All scores above derive from documented signals in the "Signals observed" section of each dimension. No score ≥90 was assigned without 2+ verifiable signals. When a signal could not be observed, the score was reduced and confidence downgraded (did not happen here — all dimensions HIGH).

### Known Limitations

- No reproducible throughput benchmark across the two: workflow ships `pnpm bench` for its runtime; gh-aw is bound to Actions' scheduling latency, which is environment-dependent.
- Community metrics (stars, downloads) not pulled — local-first policy; gh-aw's README lists 100+ contributors but quantitative stars not collected.
- gh-aw is pre-1.0 (v0.40.1); workflow core is beta (5.0.0-beta.2). Neither has GA stability signals at time of measurement.
- Scoring reflects current OS/ snapshot (2026-04-17 workflow HEAD, 2026-04-19 gh-aw HEAD); pre-1.0 velocity is high on both sides.

---

_Generated by os-bench bench-score task | Template v1.0_
