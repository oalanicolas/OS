# Inventário: workflow (Vercel Workflow SDK)

**Path:** `OS/workflow/`
**Date:** 2026-04-19
**Extraction Method:** filesystem-scan + doc-scan
**Confidence:** HIGH

---

## Identity

| Field | Value |
|-------|-------|
| Slug | workflow |
| Source URL | https://github.com/vercel/workflow |
| Primary language | TypeScript |
| Secondary languages | JavaScript, Rust (SWC plugin) |
| Stack | pnpm workspace + Turborepo + Biome + Vitest + SWC + Next.js/Nitro/Nuxt/SvelteKit/Astro integrations |
| License | Apache-2.0 |
| Tagline | Durable functions framework for JavaScript/TypeScript. Persists progress as an event log and deterministically replays code to reconstruct state after cold starts, failures or scale events. |

## Key Metrics

| Metric | Value | Source |
|--------|-------|--------|
| LOC (ballpark, JS/TS only) | ~183,749 | `find + wc -l` over `.ts/.tsx/.js/.mjs` (excluding node_modules/dist) |
| Files | 1,730 | filesystem scan |
| Packages | 28 | `packages/` dir |
| Test files | 106 | `**/*.test.ts` |
| README length | 54 lines | `README.md` |
| Last commit | 2026-04-17 | `git log -1` (`5889d84`) |
| Docs site | workflow-sdk.dev | `docs/` app (Fumadocs / Next.js) |
| Core version | 5.0.0-beta.2 | `packages/core/package.json` |

## Modules / Top-level Structure

| Module | Path | Type | Description |
|--------|------|------|-------------|
| core | `packages/core` | package | `@workflow/core` — event-sourcing engine, VM, step/hook/sleep primitives |
| world | `packages/world` | package | Storage-backend interfaces (events, hooks, queue, runs, steps, waits) |
| world-local | `packages/world-local` | package | Filesystem backend for dev/tests |
| world-vercel | `packages/world-vercel` | package | Production backend on Vercel |
| world-postgres | `packages/world-postgres` | package | Postgres backend (Drizzle ORM) |
| world-testing | `packages/world-testing` | package | In-memory backend for tests |
| next | `packages/next` | package | Next.js integration (`@workflow/next`) |
| nitro / nuxt / sveltekit / astro / nest | `packages/{nitro,nuxt,sveltekit,astro,nest}` | package | Meta-framework integrations |
| cli | `packages/cli` | package | `@workflow/cli` — standalone mode |
| swc-plugin-workflow | `packages/swc-plugin-workflow` | package | Rust SWC plugin splitting `"use workflow"` / `"use step"` bundles |
| errors / serde / utils / types / ai / builders / web / web-shared / vite / rollup / vitest / typescript-plugin / tsconfig | `packages/*` | package | Shared utility + build integrations |
| workbench | `workbench/example`, `workbench/nextjs-turbopack` | app | Example/reference apps used for e2e |
| docs | `docs/` | app | Documentation site |

## External Dependencies (top 10)

| Package | Version | Purpose |
|---------|---------|---------|
| @aws-sdk/credential-provider-web-identity | 3.972.13 | AWS STS creds (Vercel backend) |
| @jridgewell/trace-mapping | 0.3.31 | Sourcemap tracing for replay errors |
| @standard-schema/spec | 1.0.0 | Schema standard |
| @vercel/functions | catalog | Vercel runtime helpers |
| debug | 4.4.3 | Debug logger |
| devalue | 5.6.3 | Structured serialization (event payloads) |
| nanoid | 5.1.6 | ID generation |
| seedrandom | 3.0.5 | Deterministic PRNG for replays |
| ulid | catalog | Monotonic event IDs |
| zod | catalog | Schema validation |

## Entry Points

| Entry | Path | Command |
|-------|------|---------|
| CLI | `packages/cli/src/base.ts` | `workflow` / `wf` |
| Main lib | `packages/core/src/index.ts` | `import { ... } from 'workflow'` |
| Next.js integration | `packages/next/` | `withWorkflow()` + `app/.well-known/workflow/v1/` |
| Compiler | `packages/swc-plugin-workflow/` | SWC/Turbopack/Webpack transform |

## Capabilities (observed)

### Core Capabilities

| Capability | Evidence | Notes |
|------------|----------|-------|
| Durable event-log execution | `OS/workflow/docs/content/docs/how-it-works/event-sourcing.mdx`, `OS/workflow/packages/core/src/events-consumer.ts` | Append-only event log; deterministic replay reconstructs state. |
| Directive-based split (`"use workflow"` / `"use step"`) | `OS/workflow/CLAUDE.md`, `OS/workflow/packages/swc-plugin-workflow/` | SWC plugin emits separate client/workflow/step bundles. |
| Sandboxed workflow VM | `OS/workflow/packages/core/src/vm/`, `OS/workflow/packages/core/src/workflow.ts` | Orchestrator runs inside `node:vm` for determinism. |
| Typed retry controls (`FatalError`, `RetryableError`) | `OS/workflow/docs/content/docs/foundations/errors-and-retries.mdx`, `OS/workflow/packages/errors/` | Default 3 retries; `maxRetries`, `retryAfter` (duration strings or ms), arbitrary backoff exponents. |
| Parallel composition via `Promise.all` / `Promise.race` | `OS/workflow/docs/content/docs/foundations/common-patterns.mdx` | No new API — native async primitives work durably. |
| Hooks (external suspension points) | `OS/workflow/packages/core/src/{create-hook,define-hook}.ts` | Workflows suspend on webhook/callback; resume deterministically. |
| Durable sleep | `OS/workflow/packages/core/src/sleep.ts` | Sleep events persist across cold starts. |
| Pluggable "worlds" (storage) | `OS/workflow/packages/world/src/interfaces.ts`, `OS/workflow/packages/world-{local,vercel,postgres,testing}/` | 4 backends; abstract interface. |
| Payload encryption at rest | `OS/workflow/packages/core/src/encryption.ts`, `OS/workflow/packages/world-vercel/src/encryption.ts` | CryptoKey-based. |

### Optional / Extensibility Capabilities

| Capability | Evidence | Notes |
|------------|----------|-------|
| OpenTelemetry tracing | `OS/workflow/packages/core/src/telemetry.ts`, `OS/workflow/packages/core/src/telemetry/semantic-conventions.ts` | `@opentelemetry/api` optional peer dep. |
| Framework integrations | `OS/workflow/packages/{next,nitro,nuxt,sveltekit,astro,nest}/` | 6 first-party integrations. |
| Standalone CLI | `OS/workflow/packages/cli/`, `OS/workflow/workbench/example/` | Run flows without a framework. |
| Observability hydration | `OS/workflow/packages/core/src/observability.ts` | `hydrateResourceIO` powers replay UI. |
| Benchmark harness | `OS/workflow/packages/core/e2e/bench.bench.ts` | `pnpm bench` for throughput runs. |

## Tests / Quality Signals

| Signal | Value | Evidence |
|--------|-------|----------|
| Test framework | Vitest | `root package.json` |
| Test file count | 106 | `**/*.test.ts` |
| Coverage config | `@vitest/coverage-v8` | root `package.json` |
| Linter / formatter | Biome | `biome.json` |
| CI | GitHub Actions | `.github/workflows/tests.yml` (referenced in CLAUDE.md) |
| E2E harness | Next.js turbopack + vitest | `packages/core/e2e/` |

## Documentation

| Type | Path | Status |
|------|------|--------|
| README | `README.md` | 54 lines — concise pointer to workflow-sdk.dev |
| AGENTS.md | `AGENTS.md` | exists |
| CLAUDE.md | `CLAUDE.md` | exists — detailed agent guide |
| Docs site | `docs/` | Full site under workflow-sdk.dev (fumadocs) |
| Foundations | `docs/content/docs/foundations/*.mdx` | workflows-and-steps, common-patterns, errors-and-retries, hooks, idempotency, serialization, starting-workflows, streaming |
| How-it-works | `docs/content/docs/how-it-works/*.mdx` | code-transform, encryption, event-sourcing, framework-integrations, understanding-directives |

## Configuration Surface

| File | Format | Purpose |
|------|--------|---------|
| `package.json` workspaces | JSON | pnpm workspace + turbo build graph |
| `turbo.json` | JSON | Turborepo pipeline |
| `biome.json` | JSON | Lint/format |
| `vitest.config.ts` | TS | Test config |
| `pnpm-workspace.yaml` | YAML | Workspace packages + dep catalogs |
| Per-framework configs | various | `next.config.*`, `nitro.config.*`, etc. in workbench apps |

## Extension Points

| Extension Type | Where | How to extend |
|----------------|-------|---------------|
| Storage backend | `packages/world/src/interfaces.ts` | Implement the `World` interface (see world-local/vercel/postgres for reference) |
| Framework adapter | `packages/{next,nuxt,nitro,sveltekit,astro,nest}` | Add new `@workflow/<framework>` package |
| Claude skills | `skills/{workflow,workflow-init,migrating-to-workflow-sdk}` | Agent-facing authoring guides |
| Compiler behavior | `packages/swc-plugin-workflow/` (Rust) + `packages/swc-plugin-workflow/spec.md` | Mutate SWC plugin, update spec.md in lockstep |

## Notable Design Decisions

- **Event sourcing as the foundation** — state is derived; nothing is stored in-place — evidence: `OS/workflow/docs/content/docs/how-it-works/event-sourcing.mdx`.
- **Directives over DSL** — workflows are plain async functions gated by `"use workflow"` / `"use step"` — evidence: `OS/workflow/CLAUDE.md`.
- **Determinism via sandbox** — workflow bodies run in `node:vm`; `seedrandom` + ULID give deterministic IDs — evidence: `OS/workflow/packages/core/src/workflow.ts`.
- **Dual-branch release model** — `main` for beta, `stable` for GA; changesets drive both — evidence: `OS/workflow/CLAUDE.md`.

## Limitations / Known Issues

- Workflow bodies don't have full Node.js access — can't use `fs`, `net`, etc. directly (must call `"use step"` helpers).
- Production-grade hosting path is Vercel (world-vercel); self-host via world-postgres exists but has less battle-testing.
- Current npm dist-tag is `beta` (5.0.0-beta.2); production users on `latest` still on 4.x.
- All workflow I/O must be `devalue`-serializable.

## Unique Selling Points

- Zero new DSL — idiomatic TypeScript async/await just works durably.
- Deterministic replay across crashes / cold starts / scale events.
- Multi-framework footprint (Next/Nitro/Nuxt/SvelteKit/Astro/Nest).
- Storage abstraction with 4 reference backends.

---

## Extraction Notes

- Scanned directories: packages/, docs/, workbench/, skills/, scripts/
- Skipped directories: node_modules/, dist/, .next/, .turbo/, .git/
- Data sources: filesystem (100%) + README + CLAUDE.md + docs/ content
- Tools used: filesystem scan + Grep + targeted Read of package.json + docs

---

_Generated by os-bench inventory task | Template v1.0_
