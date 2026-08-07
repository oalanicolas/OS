# Executive Report: memory-5way

**Date:** 2026-08-06  
**Type:** nway  
**Slug:** memory-5way  
**Dimension pack:** memory  
**Supersedes:** `memory-4way` (2026-04-19)

---

## Executive summary

Cinco camadas de memória para agentes, no tip atual dos clones em `OS/`:

| Rank | Subject | Score | Papel |
|-----:|---------|------:|-------|
| 1 | **mempalace** | **84.23** | Memória **verbatim local-first** — baseline de fidelidade |
| 2 | **gbrain** | **78.56** | **Knowledge brain** com síntese + graph zero-LLM + dream cycle |
| 3 | **mem0** | **77.54** | **SDK universal** multi-vector-store / multi-embedder |
| 4 | **memori-labs** | **76.43** | Memória do que o agente **faz** (tools/outcomes) + SQL BYODB |
| 5 | **gsd-2** | **52.94** | Side-feature de coding agent — não compete como produto |

**Mudança vs memory-4way:** gbrain sobe ~2.7 pts (gateway multi-provider, company brain, retrieval/graph wave v0.34–0.42) e **passa mem0** no total ponderado. memori-labs entra no ranking logo atrás de mem0 — produto distinto (agent-action / LoCoMo token-efficient), não clone de mem0.

A decisão entre os quatro líderes depende do eixo:

1. **Fidelidade + offline** → mempalace  
2. **Síntese + graph de entidades + cron noturno** → gbrain  
3. **Plugar em qualquer stack de vetores** → mem0  
4. **Lembrar execução do agente (OpenClaw/Hermes)** → memori-labs  

---

## Scorecard (resumo)

| Dimension | W | gbrain | mempalace | mem0 | memori | gsd-2 |
|-----------|--:|:------:|:---------:|:----:|:------:|:-----:|
| Recall | 22% | 80 | **93** | 92 | 85 | 38 |
| Write lat. | 10% | **82** | 65 | 80 | 76 | 55 |
| Read lat. | 12% | **80** | 75 | 74 | 76 | 60 |
| Persistence | 12% | 82 | **95** | 72 | 78 | 65 |
| Schema flex. | 10% | 78 | 80 | 86 | **88** | 55 |
| Local-first | 13% | 58 | **95** | 40 | 55 | 60 |
| Vector | 11% | 78 | 72 | **98** | 70 | 48 |
| Graph | 10% | **94** | 86 | 72 | 80 | 55 |
| **Total** | | **78.56** | **84.23** | **77.54** | **76.43** | **52.94** |

---

## Dimension highlights

### Recall
- **mempalace** lidera em recall de *retrieval* (LongMemEval R@5 96.6% sem LLM).  
- **mem0** lidera em *suite* de industry benches (LoCoMo + LongMemEval + BEAM).  
- **memori** publica **87% LoCoMo com 721 tokens** — trade-off accuracy vs custo de contexto.  
- **gbrain** R@5 97.9% em corpus próprio; comparabilidade limitada.

### Graph (onde gbrain vence)
Auto-wiring **sem LLM** em cada write + `graph-query` multi-hop + retrieval relacional tipado + Life Chronicle bi-temporal. mempalace temporal KG é o runner-up; memori tem tabelas KG no Rust core; mem0 terceiriza graph store.

### Vector (onde mem0 vence)
~24 vector stores e ~11 embedders no tree. gbrain melhorou (gateway multi-provider) mas continua centrado em pgvector. mempalace agora tem 5 backends. memori usa FAISS+SQL, não zoo de stores.

### Schema (onde memori vence)
BYODB: SQLite, Postgres, MySQL, TiDB, Oracle, OceanBase, MongoDB, Cockroach + adapters SQLAlchemy/Django. Entity attribution multi-user. Ganha flexibilidade de *infra* em cima de mem0 (que ganha em *metadata de memória*).

### Local-first (onde mempalace vence de lavada)
Único com path core **zero API / offline / zero telemetry**. Os outros quatro assumem LLM ou cloud em algum grau.

---

## Strategic recommendations

### 1. Default local / auditável → **mempalace**
Use quando a memória precisa ser auditável palavra-por-palavra e rodar offline.  
**P0** se privacidade e fidelidade forem non-negotiable.

### 2. Company / personal knowledge brain → **gbrain**
Use para people/companies/deals, síntese com gap analysis, dream cycle, MCP no coding agent, multi-tenant company brain.  
**P0** se o workload é entity-graph heavy (o caso Garry/OpenClaw/Hermes production brain).

### 3. Product memory layer multi-stack → **mem0**
Use quando o time já tem Qdrant/Pinecone/etc. e quer SDK Python+TS + platform.  
**P0** para SaaS multi-tenant genérico.

### 4. Agent execution memory → **memori-labs**
Use para capturar tool calls, decisions, outcomes; plugin OpenClaw / provider Hermes; recall com budget de tokens baixo.  
**P1** complementar a gbrain/mempalace (não substitui knowledge vault).

### 5. gsd-2
Só se já vive no GSD coding agent. Não escolher como memory system standalone.

### 6. Combinações sensatas
| Stack | Papel |
|-------|--------|
| **gbrain + memori** | knowledge vault + agent-action log (OpenClaw/Hermes) |
| **mempalace + mem0** | verbatim local core + cloud multi-tenant edge |
| **gbrain + mem0** | raro — overlapping; prefira um como SoT |

---

## GBrain delta (por que subiu no ranking)

Desde o memory-4way / tip v0.33 → **v0.42.73.2** (~683 commits):

1. Company brain + auth write fences (multi-tenant real)  
2. AI gateway multi-provider + embedding migration path  
3. Retrieval cathedral / typed-edge relational / contextual / autocut  
4. Life Chronicle bi-temporal  
5. skillopt + skillpacks + doctor remediations  
6. Content-quality gates + sync resumable  

Isso move gbrain de “RAG+graph promissor” para “daemon de memória institucional” — o que explica a ultrapassagem de mem0 no pack `memory` (pesos valorizam graph e latência de write/read, onde gbrain pontua).

---

## Caveats

1. **Métricas não comensuráveis 1:1** — R@5 retrieval ≠ QA accuracy. Scores ajustam, mas cross-bench perfeito é impossível sem re-run unificado.  
2. **memory-4way permanece** em `OS/_bench/memory-4way/` como snapshot histórico.  
3. Battle-card / gap-analysis **não** gerados (n-way core = matrix + scorecard + executive). Pedir `*bench-pair gbrain memori-labs` se quiser battle-card focado.

---

## Artefatos

```
OS/_bench/memory-5way/
├── metadata.json
├── comparison-matrix.{md,json}
├── scorecard.{md,json}
├── executive-report.md
└── _inventories/{gbrain,mempalace,mem0,memori-labs,gsd-2}/inventory.md
```
