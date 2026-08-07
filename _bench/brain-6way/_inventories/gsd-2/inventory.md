# Inventario: GSD-2 memory layer (refresh)

**Path:** `OS/gsd-2/`  
**Date:** 2026-08-06  
**Confidence:** HIGH  
**Note:** Memory is a **side feature** of a coding agent — not a standalone memory product.

## Memory surface

| Item | Evidence |
|------|----------|
| Tools | `capture_thought`, `memory_query` — `src/resources/extensions/gsd/tools/memory-tools.ts` |
| Categories (enum 6) | architecture, convention, gotcha, preference, environment, pattern |
| Storage | SQLite + FTS5 (`db-memory-fts-schema.ts`) |
| Embeddings | `memory-embeddings.ts` (optional via model discovery) |
| Relations | `memory-relations.ts` |
| Consolidation | `memory-consolidation-scanner.ts`, doctor warnings |

## Why low scores

- No published LongMemEval/LoCoMo/BrainBench
- No hybrid RAG product surface
- Schema rigid (6 categories)
- Designed for project tribal knowledge inside GSD workflows only
