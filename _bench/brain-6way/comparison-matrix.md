# Comparison Matrix: brain-6way

**Date:** 2026-08-06 · **Pack:** memory + product framing

---

## Product job (o que cada um *é*)

| Subject | Job-to-be-done | Unit of knowledge |
|---------|----------------|-------------------|
| **LifeOS** | Rodar a **vida/trabalho** com um DA que conhece TELOS e sobe o hill | markdown files + hot memory cards |
| **gbrain** | **Responder** com síntese + gaps sobre um corpus de páginas/entidades | pages + graph edges (Postgres) |
| **mempalace** | **Lembrar verbatim** e buscar offline | drawers (exact text) |
| **mem0** | Embutir **memory layer** em qualquer app multi-provider | extracted facts + vectors |
| **memori-labs** | Lembrar o que o **agente fez** (tools/outcomes) | SQL entity facts |
| **gsd-2** | Memória tribal **dentro** do coding agent GSD | 6 categorias enum |

---

## Architecture snapshot

| | LifeOS | gbrain | mempalace | mem0 | memori |
|--|--------|--------|-----------|------|--------|
| Runtime | Claude Code + Pulse daemon | CLI/MCP + Minions + dream | CLI/MCP | SDK/API | SDK/plugin |
| Storage | MD tree local | PGLite/Postgres | Chroma + SQLite KG | 24 vector stores | multi SQL |
| Search | BM25 (+ graph tool) | hybrid vector+BM25+graph | vector + hybrid | vector multi-backend | FAISS+BM25 |
| Graph | graphology over MD | zero-LLM edges + multi-hop | temporal KG | optional Neo4j etc. | KG tables |
| Voice | **Pulse TTS + Siri + DA voice** | agent-voice / Twilio | no first-class | no | no |
| Dashboard | **Pulse Observatory** | admin embed | no | Platform hosted | Cloud console |
| Life goals / TELOS | **first-class** | no | no | no | no |
| Published recall bench | no | BrainBench custom | LongMemEval | LoCoMo+LME+BEAM | LoCoMo |

---

## Feature classes (LifeOS-centric)

| Capability | LifeOS | gbrain | mempalace | mem0 | memori |
|------------|:------:|:------:|:---------:|:----:|:------:|
| Verbatim storage policy | Parcial | Parcial | **Forte** | Sem | Parcial |
| Industry recall leaderboard | Sem | Parcial | **Forte** | **Forte** | Forte |
| Entity knowledge (people/co) | **Forte** | **Forte** | Parcial | Parcial | Parcial |
| Synthesis / gap analysis | Parcial (DA) | **Forte** (`think`) | Sem | Sem | Parcial |
| Autonomic memory loop | **Forte** | dream/enrich | Sem | graph recon | capture |
| Life OS / goals / TELOS | **Forte** | Sem | Sem | Sem | Sem |
| Voice runtime | **Forte** | Forte | Sem | Sem | Sem |
| Multi vector-store SDK | Sem | Sem | Parcial | **Forte** | Sem |
| Zero-API offline core | Parcial | Sem | **Forte** | Sem | Parcial |
| Coding-agent side memory only | Sem | Sem | Sem | Sem | Sem (gsd-2 yes) |

---

## When LifeOS wins the room

- Você quer **um sistema de vida**, não um store de embeddings  
- DA com identidade, TELOS, Algorithm, dashboard, voz  
- Markdown/files como SoT (git-friendly, legível)  
- Já vive em Claude Code (ou aceita harness forte)

## When LifeOS loses the room

- Precisa **R@5 SOTA** / LongMemEval  
- Precisa **offline zero LLM**  
- Precisa **SDK multi-tenant multi-Qdrant**  
- Precisa só “coloque mem0 no meu chatbot” em 10 linhas  

---

## Stacks sensatos (compose)

| Stack | Papéis |
|-------|--------|
| **LifeOS alone** | full personal OS |
| **LifeOS + mempalace** | life OS + cold verbatim archive |
| **LifeOS + gbrain** | life OS + institutional knowledge synthesis (pesado; overlapping people/companies) |
| **gbrain + memori** | knowledge + agent-action (sem life TELOS) |
| **mem0 + app** | product memory layer only |
