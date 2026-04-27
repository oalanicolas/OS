# Gap Analysis: workflow vs gh-aw

**Date:** 2026-04-19
**Dimension pack:** workflow-infra
**Slug:** workflow-infra-2way
**Source artifacts:** `comparison-matrix.json`, `scorecard.json`, `inventory-workflow.json`, `inventory-gh-aw.json`

---

## Executive Summary

Most of the gaps on both sides are paradigm-driven rather than oversights: workflow can't "adopt" gh-aw's GitHub Actions runtime model, and gh-aw can't "adopt" workflow's durable-event-sourced core without changing what it is. That said, there are concrete items each side could absorb. For workflow, the highest-leverage items are governance primitives it does not yet ship: a safe-outputs-style write handler (P1), built-in secret redaction in logs (P1), first-class approval gates (P2). For gh-aw, the highest-leverage items are durability primitives absent by construction: step-level persistence (P0), deterministic replay (P0), typed retry controls (P1). Most gh-aw gaps are scored P0/P1 but classified as HIGH complexity because they would require changes to the runtime model — gh-aw's practical response is to delegate to workflow-class engines for durable sub-runs rather than rebuild durability inside Actions.

| Direction | Total gaps | HIGH | MED | LOW | P0 | P1 | P2 | P3 |
|-----------|:---------:|:----:|:---:|:---:|:--:|:--:|:--:|:--:|
| Gaps de workflow (o que gh-aw tem e workflow não) | 9 | 1 | 5 | 3 | 0 | 2 | 4 | 3 |
| Gaps de gh-aw (o que workflow tem e gh-aw não) | 8 | 3 | 4 | 1 | 2 | 2 | 3 | 1 |

---

## Gaps de workflow

O que gh-aw tem que workflow não tem (ou tem parcialmente):

### Missing Capabilities (Sem_Equiv)

| ID | Capability | Dimension | Impact | Complexity | Priority | Description |
|----|-----------|-----------|:------:|:----------:|:--------:|-------------|
| GAP-A-001 | Markdown-as-DSL agentic DSL | language_support | MED | HIGH | P2 | Let non-JS authors write workflows in NL markdown. |
| GAP-A-002 | Multi-engine agent support | language_support | MED | MED | P2 | First-class engine routing across Copilot/Claude/Codex/Gemini. |
| GAP-A-003 | Safe-outputs handler for validated writes | cloud_lock_in | HIGH | MED | P1 | Schema-validated write side-effect handler (comment/PR/issue). |
| GAP-A-004 | Built-in agent sandbox (AWF firewall) | cloud_lock_in | MED | HIGH | P2 | Domain-based network egress controls by default. |
| GAP-A-005 | Secret redaction in logs | cloud_lock_in | MED | LOW | P1 | Regex redactor for GitHub/Azure/Google/AWS/OpenAI/Anthropic tokens. |
| GAP-A-007 | Dual-level concurrency control | parallelism | LOW | MED | P3 | Per-workflow + per-engine concurrency groups. |

### Partial Gaps (gh-aw Stronger)

| ID | Capability | What workflow has | What workflow lacks | Impact | Priority |
|----|-----------|-------------------|---------------------|:------:|:--------:|
| GAP-A-006 | First-class approval gates | Hooks (HITL possible via custom wiring) | `on.manual-approval` equivalent backed by a native gate | MED | P2 |
| GAP-A-008 | Sample workflow library | workbench/example, workbench/nextjs-turbopack + cookbook docs | Breadth of 272 shipped workflows | LOW | P3 |
| GAP-A-009 | SHA-pinned supply chain verification | pnpm.overrides for select deps | Automated pin-and-verify at compile | LOW | P3 |

### Gap Detail

#### GAP-A-001: Markdown-as-DSL agentic DSL

- **Type:** Missing
- **Dimension:** language_support
- **Impact:** MED — opens workflow to non-JS authors
- **Complexity:** HIGH — new parser + compiler layer, a second authoring surface in parallel with the JS directive model
- **Priority:** P2
- **Evidence (gh-aw has):** `OS/gh-aw/docs/src/content/docs/introduction/how-they-work.mdx`
- **Target (where to add in workflow):** would be an entirely new packages/markdown-dsl + agent loop

#### GAP-A-002: Multi-engine agent support

- **Type:** Missing
- **Dimension:** language_support
- **Impact:** MED — gives workflow reach into the agent-tooling market
- **Complexity:** MED — `packages/ai` is the natural landing spot
- **Priority:** P2
- **Evidence (gh-aw has):** `OS/gh-aw/docs/src/content/docs/reference/engines.md`
- **Target (where to add in workflow):** `OS/workflow/packages/ai/`

#### GAP-A-003: Safe-outputs handler for validated writes

- **Type:** Missing
- **Dimension:** cloud_lock_in
- **Impact:** HIGH — structural safety for production agent flows
- **Complexity:** MED — a new runtime module validating output schemas before side effects commit
- **Priority:** P1
- **Evidence (gh-aw has):** `OS/gh-aw/pkg/workflow/safe_outputs_validation.go`, `OS/gh-aw/docs/src/content/docs/reference/safe-outputs.md`
- **Target (where to add in workflow):** new `OS/workflow/packages/core/src/safe-outputs/` (or new package `@workflow/safe-outputs`)

#### GAP-A-004: Built-in agent sandbox (AWF firewall)

- **Type:** Missing
- **Dimension:** cloud_lock_in
- **Impact:** MED — workflow's `node:vm` targets determinism, not adversarial isolation
- **Complexity:** HIGH — requires egress control, likely outside the JS layer
- **Priority:** P2
- **Evidence (gh-aw has):** `OS/gh-aw/docs/src/content/docs/reference/sandbox.md`, companion `gh-aw-firewall` repo
- **Target (where to add in workflow):** around `OS/workflow/packages/core/src/vm/` + an optional proxy-based egress controller

#### GAP-A-005: Secret redaction in logs

- **Type:** Missing
- **Dimension:** cloud_lock_in
- **Impact:** MED — defense in depth for credential leaks
- **Complexity:** LOW — a logger middleware with stock regex patterns
- **Priority:** P1
- **Evidence (gh-aw has):** `OS/gh-aw/CHANGELOG.md` (redact_secrets.cjs patterns)
- **Target (where to add in workflow):** `OS/workflow/packages/core/src/logger.ts` middleware

#### GAP-A-006: First-class approval gates

- **Type:** Partial
- **Dimension:** cloud_lock_in
- **Impact:** MED
- **Complexity:** LOW — a hook convention + CLI helper
- **Priority:** P2
- **Evidence (gh-aw has):** `OS/gh-aw/docs/src/content/docs/reference/frontmatter.md` (`on.manual-approval`)
- **Target:** convention layer on top of `OS/workflow/packages/core/src/workflow/hook.ts`
- **What workflow has:** hooks (can implement HITL manually)
- **What's missing:** a standard "approval gate" primitive with audit trail integration

#### GAP-A-007: Dual-level concurrency control

- **Type:** Missing
- **Dimension:** parallelism
- **Impact:** LOW — world backends can throttle already
- **Complexity:** MED
- **Priority:** P3
- **Evidence (gh-aw has):** `OS/gh-aw/docs/src/content/docs/reference/concurrency.md`
- **Target:** `OS/workflow/packages/core/src/runtime/` + world queue layer

#### GAP-A-008: Sample workflow library (breadth)

- **Type:** Partial
- **Dimension:** language_support
- **Impact:** LOW — content/marketing, not code
- **Complexity:** LOW
- **Priority:** P3
- **Evidence (gh-aw has):** 272 sample workflows in `OS/gh-aw/.github/workflows/`
- **Target:** grow `OS/workflow/workbench/` + cookbook docs

#### GAP-A-009: SHA-pinned supply chain verification

- **Type:** Partial
- **Dimension:** cloud_lock_in
- **Impact:** LOW
- **Complexity:** MED
- **Priority:** P3
- **Evidence (gh-aw has):** `OS/gh-aw/pkg/actionpins/`, `OS/gh-aw/pkg/workflow/action_sha_checker.go`
- **Target:** optional compile-time dep-lockfile validator

---

## Gaps de gh-aw

O que workflow tem que gh-aw não tem (ou tem parcialmente):

### Missing Capabilities (Sem_Equiv)

| ID | Capability | Dimension | Impact | Complexity | Priority | Description |
|----|-----------|-----------|:------:|:----------:|:--------:|-------------|
| GAP-B-001 | Durable step persistence | durability | HIGH | HIGH | P0 | Per-step input/output persistence so workflows survive cold starts. |
| GAP-B-002 | Event-sourced deterministic replay | event_log | HIGH | HIGH | P0 | Append-only log + seedrandom/ULID for replay. |
| GAP-B-003 | Typed retry controls | retry_semantics | HIGH | MED | P1 | FatalError / RetryableError + programmable backoff. |
| GAP-B-004 | Durable sleep | durability | MED | MED | P2 | Timer survives process restarts. |
| GAP-B-005 | Pluggable storage worlds | cloud_lock_in | MED | HIGH | P2 | Abstract storage backend interface. |
| GAP-B-006 | Framework integrations (Next/Nitro/etc.) | language_support | LOW | HIGH | P3 | First-party adapters for JS meta-frameworks. |

### Partial Gaps (workflow Stronger)

| ID | Capability | What gh-aw has | What gh-aw lacks | Impact | Priority |
|----|-----------|----------------|------------------|:------:|:--------:|
| GAP-B-007 | Step-level observability | Actions UI + `gh aw logs` | Event-aware step inspector | MED | P2 |
| GAP-B-008 | Exactly-once side-effect memoization | safe-outputs dedupes writes | Structural memoization of all successful steps | MED | P1 |

### Gap Detail

#### GAP-B-001: Durable step persistence

- **Type:** Missing
- **Dimension:** durability
- **Impact:** HIGH — long agentic runs currently can't resume mid-way
- **Complexity:** HIGH — would require a new persistence layer outside Actions
- **Priority:** P0
- **Evidence (workflow has):** `OS/workflow/packages/core/src/events-consumer.ts`, `OS/workflow/docs/content/docs/how-it-works/event-sourcing.mdx`
- **Target:** outside the standard scope; pragmatic answer is to delegate to workflow (or Temporal/Inngest) for the durable sub-run

#### GAP-B-002: Event-sourced deterministic replay

- **Type:** Missing
- **Dimension:** event_log
- **Impact:** HIGH
- **Complexity:** HIGH
- **Priority:** P0
- **Evidence (workflow has):** `OS/workflow/docs/content/docs/how-it-works/event-sourcing.mdx`, `OS/workflow/packages/core/src/workflow.ts`
- **Target:** paradigm mismatch — gh-aw's practical replacement is immutable `.lock.yml` + `gh aw audit`

#### GAP-B-003: Typed retry controls

- **Type:** Missing
- **Dimension:** retry_semantics
- **Impact:** HIGH
- **Complexity:** MED
- **Priority:** P1
- **Evidence (workflow has):** `OS/workflow/docs/content/docs/foundations/errors-and-retries.mdx`, `OS/workflow/packages/errors/`
- **Target:** `OS/gh-aw/pkg/workflow/` — introduce a typed error convention agents can emit and the runtime can interpret

#### GAP-B-004: Durable sleep

- **Type:** Missing
- **Dimension:** durability
- **Impact:** MED
- **Complexity:** MED
- **Priority:** P2
- **Evidence (workflow has):** `OS/workflow/packages/core/src/sleep.ts`
- **Target:** use scheduled re-trigger (`on: schedule`) as a substitute — not exactly equivalent

#### GAP-B-005: Pluggable storage worlds

- **Type:** Missing
- **Dimension:** cloud_lock_in
- **Impact:** MED
- **Complexity:** HIGH
- **Priority:** P2
- **Evidence (workflow has):** `OS/workflow/packages/world/src/interfaces.ts`
- **Target:** scope mismatch with Actions' state model

#### GAP-B-006: Framework integrations

- **Type:** Missing
- **Dimension:** language_support
- **Impact:** LOW — gh-aw doesn't target Node.js frameworks
- **Complexity:** HIGH
- **Priority:** P3
- **Evidence (workflow has):** `OS/workflow/packages/{next,nitro,nuxt,sveltekit,astro,nest}/`
- **Target:** N/A — intentional scope difference

#### GAP-B-007: Step-level observability

- **Type:** Partial
- **Dimension:** event_log
- **Impact:** MED
- **Complexity:** HIGH
- **Priority:** P2
- **Evidence (workflow has):** `OS/workflow/packages/core/src/observability.ts`
- **Target:** would need a runtime state store in gh-aw — paradigm mismatch

#### GAP-B-008: Exactly-once side-effect memoization

- **Type:** Partial
- **Dimension:** durability
- **Impact:** MED
- **Complexity:** HIGH
- **Priority:** P1
- **Evidence (workflow has):** `OS/workflow/docs/content/docs/foundations/idempotency.mdx`, `OS/workflow/packages/core/src/events-consumer.ts`
- **Target:** `OS/gh-aw/pkg/workflow/safe_outputs_validation.go` already dedupes writes; expanding to agent-turn memoization requires durability work from GAP-B-001

---

## Classification Matrix

### By Impact

| Impact | Gaps de workflow | Gaps de gh-aw |
|--------|:----------------:|:-------------:|
| HIGH | 1 | 3 |
| MED | 5 | 4 |
| LOW | 3 | 1 |

### By Complexity

| Complexity | Gaps de workflow | Gaps de gh-aw |
|------------|:----------------:|:-------------:|
| LOW | 3 | 0 |
| MED | 4 | 3 |
| HIGH | 2 | 5 |

### By Priority

| Priority | Gaps de workflow | Gaps de gh-aw |
|----------|:----------------:|:-------------:|
| P0 (crítico) | 0 | 2 |
| P1 (alto) | 2 | 2 |
| P2 (médio) | 4 | 3 |
| P3 (baixo) | 3 | 1 |

### Impact x Complexity Heatmap

```
              LOW complexity    MED complexity    HIGH complexity
HIGH impact   —                 GAP-B-003         GAP-B-001, GAP-B-002
                                GAP-A-003
MED impact    GAP-A-005         GAP-A-002, -007   GAP-A-001, -004
              GAP-A-006         GAP-B-004         GAP-B-005, -007, -008
LOW impact    GAP-A-008         GAP-A-009         GAP-B-006
```

---

## Most Affected Dimensions

### Para workflow

| Dimension | Gap count | Highest priority |
|-----------|:---------:|:----------------:|
| cloud_lock_in | 5 | P1 |
| language_support | 3 | P2 |
| parallelism | 1 | P3 |

### Para gh-aw

| Dimension | Gap count | Highest priority |
|-----------|:---------:|:----------------:|
| durability | 3 | P0 |
| event_log | 2 | P0 |
| retry_semantics | 1 | P1 |
| cloud_lock_in | 1 | P2 |
| language_support | 1 | P3 |

---

## Action Items

Gaps P0 and P1 worth immediate attention:

| # | Action | Target | Closes gap | Dimension | Expected impact | Priority |
|---|--------|--------|-----------|-----------|-----------------|:--------:|
| 1 | Add a `safe-outputs`-style handler for validated writes | workflow | GAP-A-003 | cloud_lock_in | +10 pts | P1 |
| 2 | Ship built-in secret redaction middleware on the logger | workflow | GAP-A-005 | cloud_lock_in | +8 pts | P1 |
| 3 | Document a "delegate to durable engine" pattern for agentic workflows | gh-aw | GAP-B-001, GAP-B-002 | durability/event_log | — (documentation; avoids scope creep) | P0 |
| 4 | Introduce a typed retry convention agents can emit | gh-aw | GAP-B-003 | retry_semantics | +15 pts | P1 |
| 5 | Expand safe-outputs dedupe into a broader idempotency story | gh-aw | GAP-B-008 | durability | +5 pts | P1 |

### Action Detail

#### 1. Add a safe-outputs handler for validated writes (workflow)

- **Target:** workflow
- **Closes gap:** GAP-A-003
- **Description:** Introduce `@workflow/safe-outputs` (or a module in core) that requires every side-effecting step writer to declare an output schema; enforce at step boundary before commit.
- **Expected score improvement:** +10 in cloud_lock_in
- **Dependencies:** none
- **Source to copy/adapt:** `OS/gh-aw/pkg/workflow/safe_outputs_validation.go`, `OS/gh-aw/pkg/workflow/safe_outputs_validation_config.go`

#### 2. Built-in secret redaction on the logger (workflow)

- **Target:** workflow
- **Closes gap:** GAP-A-005
- **Description:** Add a middleware to the existing logger (`packages/core/src/logger.ts`) applying regex patterns for GitHub/Azure/Google/AWS/OpenAI/Anthropic tokens. Opt-in via config but on-by-default for Vercel world.
- **Expected score improvement:** +8 in cloud_lock_in
- **Dependencies:** none
- **Source to copy/adapt:** patterns referenced in `OS/gh-aw/CHANGELOG.md` under redact_secrets.cjs

#### 3. Document "delegate durable sub-runs to an engine" (gh-aw)

- **Target:** gh-aw
- **Closes gaps:** GAP-B-001, GAP-B-002
- **Description:** Instead of absorbing durability primitives, publish a canonical pattern: the gh-aw workflow invokes a durable engine (e.g., Temporal/Inngest/Vercel Workflow) for sub-tasks that must survive cold starts; the workflow itself handles triggering + safe-outputs.
- **Expected improvement:** avoids scope creep; clarifies positioning
- **Dependencies:** none

#### 4. Typed retry convention (gh-aw)

- **Target:** gh-aw
- **Closes gap:** GAP-B-003
- **Description:** Define an agent-emitted JSON sentinel (e.g., `{__retry__: {after: "30s"}}`) that the handler recognizes and schedules a re-trigger with back-off. Keeps agent-side ergonomics while running on Actions.
- **Expected score improvement:** +15 in retry_semantics
- **Dependencies:** agent-output schema update

#### 5. Broader idempotency story around safe-outputs (gh-aw)

- **Target:** gh-aw
- **Closes gap:** GAP-B-008
- **Description:** Extend safe-outputs dedupe to include a stable idempotency-key convention across agent turns so re-runs don't re-comment/re-PR.
- **Expected score improvement:** +5 in durability
- **Dependencies:** GAP-B-003 (retry) to capture `attempt` number

---

## Methodology

- **Gap identification:** from `comparison-matrix.json` classes (Forte/Parcial/Sem_Equiv)
- **Impact:** derived from pack weights + score delta in scorecard.json
- **Complexity:**
  - LOW: 1–3 files, <1 day
  - MED: 4–15 files or module integration, 1–3 days
  - HIGH: architectural / multi-module, >3 days
- **Priority matrix:** impact x complexity (see heatmap above)
- **Confidence:** HIGH

---

_Generated by os-bench bench-gap task | Template v1.0_
