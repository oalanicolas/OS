# Comparison Matrix: mempalace vs gbrain

**Date:** 2026-08-06 · **Pack:** memory · **Type:** pair

---

## Identity

| | mempalace | gbrain |
|--|-----------|--------|
| Version | 3.6.0 | 0.42.73.2 |
| Language | Python | TypeScript (Bun) |
| License | MIT | MIT |
| Core product? | YES — local memory palace | YES — personal/company knowledge brain |
| Default store | Chroma + SQLite KG | PGLite / Postgres + pgvector |
| MCP | **36 tools** | **30+ tools** (stdio + HTTP OAuth) |
| Install | `uv tool install mempalace` | agent-install ~30 min / bun from GitHub |
| Last tip | 2026-07-17 | 2026-08-05 |

## Job-to-be-done

| | mempalace | gbrain |
|--|-----------|--------|
| Primary job | **Remember exactly what was said** | **Answer what you need to know** |
| Output of query | ranked verbatim drawers / sessions | synthesized prose + citations + **gap analysis** |
| Overnight work | optional hybrid rerank | dream cycle, enrich, extract, doctor, 66 crons (author) |
| Multi-user | personal palace + hooks | **company brain** + OAuth write fences |

## Feature classes

| Capability | mempalace | gbrain | Class |
|------------|:---------:|:------:|-------|
| Verbatim storage policy | **Forte** | Parcial (raw backup) | A-only strength |
| Industry LongMemEval published | **Forte** | Sem_Equiv | A-only |
| Zero API core path | **Forte** | Sem_Equiv | A-only |
| Temporal KG as-of queries | **Forte** | Parcial (Chronicle) | A stronger temporal |
| Claude Code session mine/hooks | **Forte** | Parcial | A stronger agent-session |
| Synthesis `think` + gap analysis | Sem_Equiv | **Forte** | B-only |
| Zero-LLM graph auto-wiring | Parcial | **Forte** | B stronger |
| Durable job queue (Minions) | Sem_Equiv | **Forte** | B-only |
| Company multi-tenant isolation | Sem_Equiv | **Forte** | B-only |
| Dream/enrich/doctor loop | Sem_Equiv | **Forte** | B-only |
| Hybrid vector+keyword search | Forte | Forte | Empate |
| MCP for coding agents | Forte (36) | Forte (30+) | Empate |
| Schema packs / BYO shape | Parcial (wings/rooms) | **Forte** | B stronger |
| Multi embedding providers | Parcial | **Forte** (gateway) | B stronger |
| Pluggable vector backends | **Forte** (5) | Parcial (pgvector focus) | A stronger surface |
| Production scale claim | benchmarks 500q | 146k pages author prod | B scale story |

## Architecture contrast

```
mempalace                          gbrain
─────────                          ──────
drawer (verbatim text)             page (compiled_truth + raw)
  → wing / room layout               → slug taxonomy + schema packs
  → Chroma embed (default)           → pgvector HNSW
  → optional hybrid rerank           → hybrid RRF + graph signals
  → temporal KG (explicit triples)   → auto edges on every write
  → return snippets                  → think → answer + gaps
  → no overnight daemon required     → dream / minions / autopilot
```
