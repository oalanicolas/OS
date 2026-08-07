# Inventario: MemPalace (refresh)

**Path:** `OS/mempalace/`  
**Date:** 2026-08-06  
**Confidence:** HIGH  
**Version:** 3.6.0

## Identity

| Field | Value |
|-------|-------|
| Source | https://github.com/MemPalace/mempalace |
| Stack | Python, Chroma default, pluggable backends, SQLite KG, MCP |
| License | MIT |
| Tagline | Local-first AI memory — **verbatim**, zero API on core path |

## Headline metrics

| Metric | Value | Source |
|--------|-------|--------|
| LongMemEval R@5 raw | **96.6%** | `benchmarks/BENCHMARKS.md` |
| Hybrid v4 + rerank | **100%** R@5 (optional LLM) | same |
| Policy | No summarize / no paraphrase | CONTRIBUTING / README |

## Backends (current tree)

`mempalace/backends/`: chroma, milvus, pgvector, qdrant, sqlite_exact (+ base/registry)

## Structure metaphor

Wings (people/projects) → rooms (topics) → drawers (verbatim content)

## Graph

Temporal entity-relationship graph with `valid_from` / `valid_to` (as-of queries)

## Local-first

**Strongest in pack** — core path no API keys; offline; data ownership explicit
