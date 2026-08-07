# Inventario: GBrain (refresh)

**Path:** `OS/gbrain/`  
**Date:** 2026-08-06  
**Confidence:** HIGH  
**Version:** 0.42.73.2

## Identity

| Field | Value |
|-------|-------|
| Source | https://github.com/garrytan/gbrain |
| Stack | Bun/TS, PGLite or Postgres+pgvector, MCP, Minions queue |
| License | MIT |
| Tagline | Search gives pages; GBrain gives the **answer** (synthesis + gap analysis + graph) |

## Headline metrics (in-repo)

| Metric | Value | Source |
|--------|-------|--------|
| BrainBench P@5 / R@5 | 49.1% / **97.9%** | `README.md` (graph on; +31.4 P@5 vs graph-off) |
| Production scale (author) | 146k pages, 24k people, 5k companies | README |
| Engines | PGLite default + Postgres/Supabase | README / `src/core/engine.ts` |

## Capabilities (delta since memory-4way / v0.33)

| Capability | Evidence |
|------------|----------|
| Company brain / multi-tenant | README company-brain; auth slug-prefix write fence v0.42.72 |
| Provider-agnostic AI gateway | `src/core/ai/gateway.ts`, embedding migration v0.42.67 |
| Life Chronicle bi-temporal | v0.42.56 feat(chronicle) |
| Typed-edge relational retrieval | v0.42.34 |
| skillopt / skillpacks | v0.42.1, v0.42.47 |
| Content-quality gate on sync | v0.42.8 |
| Doctor cause-ranked + remediate | v0.42.16+ |
| Self-upgrade + GitHub Releases | v0.42.12 / v0.42.71 |

## Persistence

- Primary: `compiled_truth` (synthesized) + raw in JSONB
- Graph edges on every write (zero-LLM heuristics)
- Not verbatim-first

## Local-first

- PGLite zero-server works; embeddings/rerank usually need API keys
- Full offline path incomplete vs mempalace
