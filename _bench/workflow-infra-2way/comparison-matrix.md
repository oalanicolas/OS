# Comparison Matrix: workflow vs gh-aw

**Date:** 2026-04-19
**Comparison type:** pair
**Dimension pack:** workflow-infra (v1.0)
**Slug:** workflow-infra-2way

---

## Sources

| Subject | Path | Web source | Confidence |
|---------|------|------------|------------|
| workflow (Vercel Workflow SDK) | `OS/workflow/` | https://github.com/vercel/workflow, https://workflow-sdk.dev | HIGH |
| gh-aw (GitHub Agentic Workflows) | `OS/gh-aw/` | https://github.com/github/gh-aw, https://github.github.com/gh-aw | HIGH |

## Method

The matrix was built from the clonadas copies in `OS/` using filesystem scan + doc-scan. For each feature we read: (1) the README/CLAUDE.md at the root, (2) package/go manifests (`packages/*/package.json`, `go.mod`), (3) docs site content (`OS/workflow/docs/content/docs/**` and `OS/gh-aw/docs/src/content/docs/**`), (4) source code landmarks (runtime, retry, event-log, sandbox, safe-outputs). No web-only claims were admitted unless backed by an in-repo path. Equivalence labels follow the skeleton (Forte 5/5, Parcial 3/5, Sem_Equiv 1/5) and are driven by how the same underlying durable-workflow concern (durability, retries, replay, fan-out, lock-in) is actually addressed by each subject — not by a shallow feature-name match.

---

## Inventory Summary

| Metric | workflow | gh-aw | Delta |
|--------|----------|-------|-------|
| LOC (ballpark) | ~183,749 (JS/TS) | ~526,558 (Go+JS) | gh-aw ~2.9x |
| Files | 1,730 | 4,044 | gh-aw +2,314 |
| Primary language | TypeScript | Go | — |
| License | Apache-2.0 | MIT | — |
| Test files | 106 | 1,050 | gh-aw +944 |
| Last commit | 2026-04-17 | 2026-04-19 | — |
| Version | `@workflow/core` 5.0.0-beta.2 | v0.40.1 (pre-1.0) | — |
| Docs stack | Fumadocs (Next.js) | Astro + Starlight | — |
| Top-level packages / modules | 28 packages | 17+ pkgs + 272 workflows | — |

---

## Feature Matrix

### Category: Paradigm

| Item | workflow | gh-aw | Equivalence | Delta |
|------|----------|-------|:-----------:|-------|
| Execution model | Durable JS functions with event-sourced replay (`node:vm` sandbox + SWC-split step bundles) | Markdown with YAML frontmatter compiled to GitHub Actions `.lock.yml`; agent interprets the NL body | Sem_Equiv | Entirely different paradigms: typed durable code vs declarative NL DSL compiled to CI jobs. |
| Primary runtime | Node.js on Vercel / self-host (Postgres/local FS) | GitHub Actions runners (hosted or self-hosted) | Sem_Equiv | Runtime substrates share almost no assumptions. |
| Author surface | TS/JS source files with `"use workflow"` / `"use step"` directives | Markdown + YAML frontmatter; body is a natural-language prompt | Sem_Equiv | Code vs prose DSL. |

### Category: Durability

| Item | workflow | gh-aw | Equivalence | Delta |
|------|----------|-------|:-----------:|-------|
| Step persistence | Every step input/output persisted to event log via `events-consumer.ts` + `world` backends | Persistence = Actions-level job logs + artifacts; no per-LLM-turn event log | Sem_Equiv | workflow has a first-class durable step abstraction; gh-aw inherits Actions semantics. |
| Crash recovery | Deterministic replay reconstructs state after cold start / scale event (see `docs/how-it-works/event-sourcing.mdx`) | Replay = re-run the whole `workflow_run` | Sem_Equiv | workflow recovers mid-function; gh-aw recovers by restarting the whole job. |
| Exactly-once side effects | Steps memoized by event log; authors warned to keep bodies idempotent (`foundations/idempotency.mdx`) | No framework-level memoization; `safe-outputs` handler has per-output dedupe for writes | Parcial | Both lean on user idempotency; workflow structurally memoizes successful steps. |

### Category: Retry semantics

| Item | workflow | gh-aw | Equivalence | Delta |
|------|----------|-------|:-----------:|-------|
| Default retries | 3 retries per step by default; `fn.maxRetries = N` override (`docs/foundations/errors-and-retries.mdx`) | Inherits Actions `continue-on-error`/retry-action patterns; per-engine `max-turns` / `max-continuations` for agent loops | Sem_Equiv | workflow has typed retry primitives; gh-aw delegates to Actions. |
| Typed error opt-outs | `FatalError` (stop retrying) / `RetryableError` (custom `retryAfter`, exponential backoff) — `packages/errors` | No equivalent error taxonomy | Sem_Equiv | workflow-only. |
| Backoff / jitter | Arbitrary schedule: `retryAfter: (attempt ** 2) * 1000`; duration strings ("1m", "30s") | Delegated to Actions retry tooling | Sem_Equiv | workflow exposes programmable backoff; gh-aw uses external patterns. |

### Category: Event log & debugging

| Item | workflow | gh-aw | Equivalence | Delta |
|------|----------|-------|:-----------:|-------|
| Append-only event log | Yes — core engine + per-world backend | No — Actions job logs only | Sem_Equiv | workflow-only. |
| Deterministic replay | First-class; `seedrandom` + ULID ensure determinism | N/A — runs are independent | Sem_Equiv | workflow-only. |
| Observability UI | `observability.ts hydrateResourceIO` powers step-aware replay inspector | GitHub Actions run UI + `gh aw logs` | Parcial | Both have UIs; shapes differ. |
| Audit trail | Event log doubles as audit trail | GitHub Actions audit + commit history of `.lock.yml` + `gh aw audit` | Parcial | Different shapes; both credible. |

### Category: Parallelism

| Item | workflow | gh-aw | Equivalence | Delta |
|------|----------|-------|:-----------:|-------|
| Fan-out primitive | `Promise.all` on step invocations — all persisted durably | `matrix:` strategy inherited from Actions; `engine.concurrency` caps | Parcial | workflow parallelizes inside one function; gh-aw parallelizes at the job level. |
| Race / timeout | `Promise.race` + durable `sleep()` | `timeout-minutes` + `stop-after` triggers | Parcial | Conceptually similar outcomes via different mechanisms. |
| Concurrency limits | Not framework-level; world backends can throttle | Dual concurrency: per-workflow (keyed by issue/PR/branch) + per-engine `gh-aw-{engine-id}` | Sem_Equiv | gh-aw ships richer out-of-the-box controls. |

### Category: Language support & DSL

| Item | workflow | gh-aw | Equivalence | Delta |
|------|----------|-------|:-----------:|-------|
| Languages | JavaScript / TypeScript only | Markdown DSL; prompts can invoke any language via shell/tools; native CLI is Go | Sem_Equiv | gh-aw is polyglot at the tool surface; workflow is JS-only. |
| DSL richness | None — idiomatic TS (directives only) | Rich YAML frontmatter: triggers, permissions, tools, engines, sandbox, safe-outputs, concurrency | Sem_Equiv | gh-aw has a large DSL; workflow deliberately has none. |
| Framework integrations | Next.js, Nitro, Nuxt, SvelteKit, Astro, NestJS (6 packages) | N/A (runs on Actions) | Sem_Equiv | workflow-only category. |
| IDE support | TypeScript plugin package + types | WASM compiler for editor integration; JSON-schema-backed frontmatter | **Forte** | Both invest in editor integration along their DSL grain. |

### Category: Cloud lock-in / portability

| Item | workflow | gh-aw | Equivalence | Delta |
|------|----------|-------|:-----------:|-------|
| Managed hosting | First-class on Vercel (`world-vercel`); other worlds less battle-tested | Runs on GitHub.com, GHES, self-hosted runners | Sem_Equiv | workflow leans Vercel; gh-aw leans GitHub — GitHub Actions is more widely self-hosted today. |
| Self-host option | `@workflow/world-postgres` (Drizzle) + `@workflow/world-local` | GitHub Actions self-hosted runners | Parcial | Both self-hostable with trade-offs. |
| Portable artifact | npm packages; portable JS source | Standard GitHub Actions YAML (`.lock.yml`) | Parcial | Different artifacts; both portable within their ecosystems. |
| Vendor-neutral backend | World abstraction allows new backends | Bound to GitHub Actions semantics; companion firewall/gateway are GitHub-owned | Parcial | workflow abstracts storage; gh-aw assumes Actions. |

### Category: Safety / Governance

| Item | workflow | gh-aw | Equivalence | Delta |
|------|----------|-------|:-----------:|-------|
| Sandboxing | Workflow body runs in `node:vm` (determinism, not security) | AWF firewall (default), MCP Gateway, lockdown mode, tool allow-lists | Sem_Equiv | gh-aw explicitly targets adversarial safety; workflow's sandbox targets determinism. |
| Approval gates | Hooks can implement HITL manually | `on.manual-approval` via GitHub Environments; skip-roles/skip-bots | Parcial | Both possible; gh-aw first-class. |
| Output validation | Author-provided (zod/return types) | Every write side effect goes through validated `safe-outputs` handler | Sem_Equiv | gh-aw enforces at write time by design. |
| Secret redaction | Not built-in | Built-in regex redactor for GitHub/Azure/Google/AWS/OpenAI/Anthropic | Sem_Equiv | gh-aw-only. |
| Supply-chain hardening | `pnpm.overrides` pins (rfc6902, devalue) | SHA-pinned Actions via `pkg/actionpins` + gosec + embedded actionlint | Parcial | Both invest; gh-aw is more automated. |

### Category: Ecosystem & community

| Item | workflow | gh-aw | Equivalence | Delta |
|------|----------|-------|:-----------:|-------|
| Sample workflows | `workbench/example`, `workbench/nextjs-turbopack` | 272 `.md` workflows in `.github/workflows/` (smoke + agentics) | Sem_Equiv | gh-aw ships vastly more example surface. |
| Community contributions | Vercel team + OSS contributors (list in README) | 100+ named community contributors auto-tracked in README | Sem_Equiv | gh-aw has more visible traction today. |
| Skills for agent authoring | 3 skills (workflow, workflow-init, migrating-to-workflow-sdk) | 22 skills (authoring, debugging, safe-outputs, etc.) | Parcial | Both offer skill packs; gh-aw has richer coverage. |

---

## Equivalence Summary

| Level | Count | Percentage |
|-------|-------|-----------|
| Forte (strong equivalent, 5/5) | 1 | 3% |
| Parcial (partial equivalent, 3/5) | 10 | 33% |
| Sem_Equiv (no equivalent, 1/5) | 19 | 64% |
| **Total items compared** | **30** | 100% |

The very low Forte count reflects how divergent these paradigms are: the only direct "both do the same thing with comparable depth" item is IDE tooling. Everything else is either paradigm-incompatible or covered by structurally different mechanisms.

---

## workflow-Only Capabilities

Capabilities present in workflow without counterpart in gh-aw:

| # | Capability | Category | Description | Evidence path |
|---|-----------|----------|-------------|---------------|
| 1 | Event-sourced durable execution | Durability | Every step/hook/sleep persisted to append-only event log, with deterministic replay | `OS/workflow/docs/content/docs/how-it-works/event-sourcing.mdx`, `OS/workflow/packages/core/src/events-consumer.ts` |
| 2 | Directive-based bundle split | Core | SWC plugin splits `"use workflow"` / `"use step"` into distinct runtime bundles | `OS/workflow/CLAUDE.md`, `OS/workflow/packages/swc-plugin-workflow/` |
| 3 | Typed retry primitives (`FatalError`, `RetryableError`) | Retry | Default 3 retries + arbitrary backoff via `retryAfter` on RetryableError | `OS/workflow/docs/content/docs/foundations/errors-and-retries.mdx`, `OS/workflow/packages/errors/` |
| 4 | Pluggable "world" storage abstraction | Portability | Reference implementations for local FS, Postgres (Drizzle), Vercel, in-memory | `OS/workflow/packages/world/src/interfaces.ts`, `OS/workflow/packages/world-{local,vercel,postgres,testing}/` |
| 5 | Meta-framework integrations | Integration | Next.js, Nitro, Nuxt, SvelteKit, Astro, NestJS native adapters | `OS/workflow/packages/{next,nitro,nuxt,sveltekit,astro,nest}/` |
| 6 | Durable `sleep()` primitive | Parallelism | Timer survives restarts; part of event log | `OS/workflow/packages/core/src/sleep.ts`, `OS/workflow/packages/core/src/workflow/sleep.ts` |

**Total:** 6

## gh-aw-Only Capabilities

Capabilities present in gh-aw without counterpart in workflow:

| # | Capability | Category | Description | Evidence path |
|---|-----------|----------|-------------|---------------|
| 1 | Markdown-as-DSL agentic workflows | Core | 272 ready-to-use NL workflows; agent interprets body with permissions sandbox | `OS/gh-aw/.github/workflows/`, `OS/gh-aw/docs/src/content/docs/introduction/how-they-work.mdx` |
| 2 | Multi-engine agent support | Core | Copilot / Claude / Codex / Gemini / Crush with per-engine feature matrix | `OS/gh-aw/docs/src/content/docs/reference/engines.md` |
| 3 | Safe-outputs handler | Governance | Read-only default; writes flow through validated handler (comment/PR/issue/label/milestone/autofix/push) | `OS/gh-aw/pkg/workflow/safe_outputs_validation.go`, `OS/gh-aw/docs/src/content/docs/reference/safe-outputs.md` |
| 4 | AWF agent firewall | Governance | Default `sandbox.agent: awf` provides domain-based network egress control + activity logging | `OS/gh-aw/docs/src/content/docs/reference/sandbox.md`, companion repo `gh-aw-firewall` |
| 5 | MCP Gateway | Governance | Unified HTTP gateway for all MCP calls with centralized auth (`gh-aw-mcpg`) | `OS/gh-aw/docs/src/content/docs/reference/mcp-gateway.md` |
| 6 | `on.manual-approval` via Environments | Governance | Human approval gates piggyback on GitHub Environments protection rules | `OS/gh-aw/docs/src/content/docs/reference/frontmatter.md` |
| 7 | SHA-pinned Actions + actionlint + gosec on compile | Governance | Supply-chain hardening built into compile | `OS/gh-aw/pkg/actionpins/`, `OS/gh-aw/pkg/workflow/action_pins.go`, `OS/gh-aw/pkg/workflow/action_sha_checker.go` |
| 8 | Secret redaction in logs | Governance | Built-in regex redactor for major cloud/AI tokens | `OS/gh-aw/CHANGELOG.md` (redact_secrets.cjs) |
| 9 | Dual concurrency control | Parallelism | Per-workflow (issue/PR/branch-keyed) + per-engine (`gh-aw-{engine-id}`) groups | `OS/gh-aw/docs/src/content/docs/reference/concurrency.md` |

**Total:** 9

---

## Partial Equivalences (Notable Deltas)

Items marked `Parcial` where the delta matters:

| Item | workflow detail | gh-aw detail | Stronger | Delta |
|------|-----------------|--------------|----------|-------|
| Exactly-once side effects | Structural memoization of successful steps | User-side guarantee + safe-outputs dedupe for writes | workflow | workflow removes a class of bugs by construction. |
| Observability UI | Step/event-aware replay inspector | Job/step view of Actions + `gh aw logs` | workflow | workflow has deeper per-step introspection. |
| Audit trail | Event log is the audit trail | `.lock.yml` commits + GH audit + `gh aw audit` | gh-aw | gh-aw integrates with existing enterprise audit surface. |
| Fan-out primitive | `Promise.all` durably persisted | Actions `matrix:` per job | workflow | workflow persists each parallel branch; matrix relies on Actions job state. |
| Race / timeout | `Promise.race` + durable sleep | `timeout-minutes` + `stop-after` | = | Comparable in outcome. |
| Self-host option | `world-postgres` + `world-local` | Actions self-hosted runners | gh-aw | Far larger existing self-host base for Actions runners. |
| Portable artifact | npm JS packages | `.lock.yml` (standard Actions YAML) | = | Both are portable within their ecosystem. |
| Vendor-neutral backend | World abstraction | Actions-bound | workflow | workflow's storage is swappable in a way gh-aw's runtime isn't. |
| Approval gates | DIY via hooks | `on.manual-approval` + Environments | gh-aw | Built-in, auditable. |
| Supply-chain hardening | `pnpm.overrides` pins | SHA-pinned Actions + gosec + actionlint | gh-aw | Much more automated. |
| Skills for agent authoring | 3 skills | 22 skills | gh-aw | More coverage. |

---

## Objective Reading

### workflow Strengths

workflow is the only side of this pair that solves durability *inside* user code: event-sourced replay, typed retry primitives, durable `sleep()`, and `Promise.all`-parallelism that all survive cold starts (`OS/workflow/docs/content/docs/how-it-works/event-sourcing.mdx`, `OS/workflow/docs/content/docs/foundations/errors-and-retries.mdx`). It ships six first-party meta-framework integrations (Next/Nitro/Nuxt/SvelteKit/Astro/Nest) and a pluggable `world` abstraction with local-FS, Postgres and Vercel backends (`OS/workflow/packages/world/src/interfaces.ts`). For JS/TS teams building long-running agents or multi-step business flows that must recover mid-task, workflow is the correct abstraction. Its compiler-level directive split (`"use workflow"` / `"use step"`) keeps the authoring surface zero-DSL while giving the runtime enough structure to replay.

### gh-aw Strengths

gh-aw is designed for *safe* agentic automation on code-hosting infrastructure the organization already runs. Its defaults are all about guardrails: read-only by default, AWF firewall sandbox, `safe-outputs` handler for every write, SHA-pinned Actions, secret redaction in logs, and `on.manual-approval` gates via GitHub Environments (`OS/gh-aw/README.md` Guardrails section, `OS/gh-aw/pkg/workflow/safe_outputs_validation.go`). Because workflows compile to standard GitHub Actions `.lock.yml`, the runtime is whatever GitHub Actions already provides (GitHub.com, GHES, self-hosted runners) with a massive existing self-host footprint. The multi-engine matrix (Copilot/Claude/Codex/Gemini/Crush) and markdown-native DSL make workflows diff-able, shareable and installable via `gh aw add owner/repo/path@ref`. 272 sample workflows + 22 authoring skills + a 100+ contributor community give it remarkable ecosystem density for a pre-1.0 project.

### Key Differentiators

- **workflow** owns: event log, deterministic replay, typed retries, durable sleep, framework integrations, storage abstraction.
- **gh-aw** owns: markdown DSL + multi-engine, safe-outputs, AWF sandbox, MCP Gateway, SHA pinning, secret redaction, approval gates via Environments, dual concurrency control.

### Areas of Parity

- IDE/editor support (TS plugin ↔ WASM compiler + JSON schema).
- Observability (step-aware inspector ↔ Actions UI + `gh aw logs`), each excellent in its native mode.
- Self-host (Postgres world ↔ self-hosted runners), both real but operationally different.

---

## Method Disclosure

- **Comparison date:** 2026-04-19
- **Dimension pack:** workflow-infra v1.0
- **Items compared:** 30
- **Dimensions used:** 6 (Durability, Retry semantics, Event log, Parallelism, Language support, Cloud lock-in)
- **Equivalence criteria:**
  - Forte ≥90% match in functionality and depth
  - Parcial 60–89% match
  - Sem_Equiv <60% match
- **Data sources:**
  - workflow: filesystem scan of `OS/workflow/` + https://github.com/vercel/workflow + https://workflow-sdk.dev
  - gh-aw: filesystem scan of `OS/gh-aw/` + https://github.com/github/gh-aw + https://github.github.com/gh-aw

---

_Generated by os-bench bench-matrix task | Template v1.0_
