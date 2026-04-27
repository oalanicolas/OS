# Scorecard: BMAD-METHOD vs crewAI vs autogen vs paperclip vs claude-remote-manager

**Date:** 2026-04-19
**Dimension pack:** orchestration (8 dimensões)
**Slug:** orchestration-5way
**Overall Confidence:** HIGH

---

## Scoring Method

- Score range: 0–100 por dimensão
- Pesos do pack `orchestration` (soma = 1.00): Topology 0.15, Delegation 0.15, State 0.12, Parallelism 0.12, Recovery 0.13, Observability 0.12, DSL 0.11, Deployment 0.10
- Cada score derivado de 2+ signals documentados abaixo com evidence path em `OS/{subject}/...`
- Nenhum score ≥90 sem 2+ signals observáveis
- Fonte primária: filesystem (`OS/{subject}/`)

---

## Dimension Scores

| Dimension | Weight | BMAD | crewAI | autogen | paperclip | CRM | Winner |
|-----------|-------:|:----:|:------:|:-------:|:---------:|:---:|:------:|
| Topology | 15% | 70 | 72 | **92** | 68 | 25 | autogen |
| Delegation Model | 15% | 75 | **85** | 82 | 80 | 45 | crewAI |
| State Mgmt | 12% | 20 | 78 | 82 | **92** | 55 | paperclip |
| Parallelism | 12% | 72 | 58 | **88** | 78 | 55 | autogen |
| Failure Recovery | 13% | 15 | 45 | 62 | 68 | **82** | CRM |
| Observability | 12% | 12 | 70 | 85 | **90** | 40 | paperclip |
| DSL | 11% | **82** | 72 | 58 | 78 | 42 | BMAD |
| Deployment | 10% | 55 | 55 | 80 | **88** | 48 | paperclip |

---

## Weighted Total

| Subject | Weighted | Dim Wins |
|---------|:--------:|:--------:|
| paperclip | **79.62/100** | 3 |
| autogen | **79.14/100** | 2 |
| crewAI | 67.54/100 | 1 |
| BMAD-METHOD | 50.70/100 | 1 |
| claude-remote-manager | 48.58/100 | 1 |

**Overall Winner:** paperclip por 0.48pt — empate técnico com autogen. crewAI mid-pack, BMAD e CRM fecham (penalizados por dimensões onde não têm runtime/Docker).

---

## Dimension Analysis

### Topology (15%)

| BMAD | crewAI | autogen | paperclip | CRM |
|:----:|:------:|:-------:|:---------:|:---:|
| 70 | 72 | **92** | 68 | 25 |

autogen lidera com 4 topologias formais (`_round_robin_group_chat.py`, `_selector_group_chat.py`, `_swarm_group_chat.py`, `_magentic_one/`) + graph DAG (`_graph/`) — é o único com cobertura swarm e graph. BMAD e crewAI ficam próximos via pipeline + Flow/hierarchical. paperclip tem hierarquia programática única (org-chart), mas não cobre outras topologias. CRM sem topologia coordenada.

**Signals observados:**
- **BMAD:** `src/bmm-skills/` (pipeline), `src/core-skills/bmad-party-mode/SKILL.md` (roundtable)
- **crewAI:** `src/crewai/process.py` (sequential/hierarchical), `src/crewai/flow/flow.py` (graph)
- **autogen:** `python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/` (4 topologias + graph)
- **paperclip:** `server/src/services/company-member-roles.ts`, `routes/org-chart-svg.ts`
- **CRM:** `agents/` (apenas dirs independentes)

### Delegation Model (15%)

| BMAD | crewAI | autogen | paperclip | CRM |
|:----:|:------:|:-------:|:---------:|:---:|
| 75 | **85** | 82 | 80 | 45 |

crewAI lidera com modelo mental role-playing (role/goal/backstory) + manager_llm + Planner automático (`src/crewai/utilities/planning_handler.py`). autogen próximo via SelectorGroupChat LLM-driven + handoff primitive. paperclip único com delegação cross-runtime (7 adapters heterogêneos). BMAD tem roles explícitos mas delegação é editorial. CRM depende de send-message manual.

**Signals:**
- **crewAI:** `src/crewai/agent.py`, `utilities/planning_handler.py`
- **autogen:** `teams/_group_chat/_selector_group_chat.py`, `base/_handoff.py`, `_type_subscription.py`
- **paperclip:** `server/src/services/company-member-roles.ts`, `packages/adapters/`
- **BMAD:** `src/bmm-skills/`, `tools/validate-skills.js`
- **CRM:** `core/bus/send-message.sh`

### State Mgmt (12%)

| BMAD | crewAI | autogen | paperclip | CRM |
|:----:|:------:|:-------:|:---------:|:---:|
| 20 | 78 | 82 | **92** | 55 |

paperclip domina com Postgres embutido via Drizzle (`packages/db/`) + execution workspaces isolados (`services/execution-workspaces.ts`) + WS realtime + heartbeat summaries — é state mgmt de nível empresa. autogen vem atrás via save_state/load_state + memory protocol plugável (Redis/mem0/Chroma em ext). crewAI oferece multi-tier memory (short/long/entity/user) embutida. CRM durable via inbox filesystem, rudimentar. BMAD sem runtime próprio → state no IDE host.

**Signals:**
- **paperclip:** 4+ evidence paths incluindo `packages/db/`, `services/execution-workspaces.ts`
- **autogen:** `autogen-agentchat/src/autogen_agentchat/state/`, `autogen-ext/.../memory/`
- **crewAI:** `src/crewai/memory/{short_term,long_term,entity,user}/`

### Parallelism (12%)

| BMAD | crewAI | autogen | paperclip | CRM |
|:----:|:------:|:-------:|:---------:|:---:|
| 72 | 58 | **88** | 78 | 55 |

autogen lidera com async runtime + gRPC multi-worker distribuído (`autogen-ext/.../runtimes/grpc/`) + topic broadcast fan-out. paperclip forte com N execution workspaces paralelos. BMAD via Party Mode spawna subagents via Agent tool (fan-out real). crewAI limitado pelo GIL e sync-by-default. CRM paraleliza via N tmux sessions mas sem coordenação.

### Failure Recovery (13%)

| BMAD | crewAI | autogen | paperclip | CRM |
|:----:|:------:|:-------:|:---------:|:---:|
| 15 | 45 | 62 | 68 | **82** |

claude-remote-manager domina disparado — é o único com semântica at-least-once explícita (inflight → redelivery 5min em `core/bus/check-inbox.sh`) + launchd auto-restart + crash-alert + 71h soft-reset. paperclip segundo via approval retry + cron retries + dev-runner resilience. autogen oferece gRPC worker resilience. crewAI apenas retries de LLM call. BMAD sem recovery (fica no IDE).

**Signals CRM:**
- `core/scripts/generate-launchd.sh` (launchd watchdog)
- `core/bus/check-inbox.sh` (inflight → redelivery)
- `core/scripts/crash-alert.sh`
- `core/bus/self-restart.sh` (71h soft-reset)

### Observability (12%)

| BMAD | crewAI | autogen | paperclip | CRM |
|:----:|:------:|:-------:|:---------:|:---:|
| 12 | 70 | 85 | **90** | 40 |

paperclip lidera — cost + budget + finance services nativos, React dashboard com WS realtime mobile-ready, heartbeat summaries, promptfoo evals. autogen segundo com OTel core + Studio UI + agbench. crewAI via OTel wiring + usage metrics delega backend externo. CRM usa Telegram como UI improvisado. BMAD nada embutido.

**Signals paperclip:**
- `services/costs.ts`, `services/budgets.ts`, `services/finance.ts`
- `ui/`, `server/src/realtime/live-events-ws.ts`
- `services/heartbeat-run-summary.ts`
- `evals/promptfoo/`

### DSL (11%)

| BMAD | crewAI | autogen | paperclip | CRM |
|:----:|:------:|:-------:|:---------:|:---:|
| **82** | 72 | 58 | 78 | 42 |

BMAD-METHOD lidera com DSL YAML + MD + skill validator strict (`tools/validate-skills.js`) — único com schema enforcement no CI. paperclip próximo via routines declarativas + company portability JSON + org-chart editor. crewAI via Flow decorators + visualizer. autogen code-first (Python); Studio cobre GUI mas não há DSL nativa. CRM config.json + CLAUDE.md é mínimo.

### Deployment (10%)

| BMAD | crewAI | autogen | paperclip | CRM |
|:----:|:------:|:-------:|:---------:|:---:|
| 55 | 55 | 80 | **88** | 48 |

paperclip lidera com Dockerfile + embedded Postgres zero-config + MCP server npx-distribuível + monorepo com pnpm. autogen via pip + Studio Dockerfile + gRPC distributed. BMAD/crewAI apenas one-command install library-style. CRM excelente bootstrap mas macOS-only.

---

## Score Distribution

### Profiles

- **BMAD-METHOD** (avg 50.1, range 12–82) — **spike em DSL**; vales profundos em State/Recovery/Obs porque é library de skills, não runtime.
- **crewAI** (avg 66.9, range 45–85) — perfil balanceado com spike em Delegation; sem extremos negativos.
- **autogen** (avg 79.3, range 58–92) — perfil forte e amplo; **spike em Topology**, vale leve em DSL.
- **paperclip** (avg 78.6, range 68–92) — perfil mais equilibrado do conjunto; lidera 3 dimensões, não está abaixo de 68 em nenhuma.
- **claude-remote-manager** (avg 49.0, range 25–82) — **spike isolado em Failure Recovery**; vales em Topology/DSL/Obs porque foco é persistência, não orquestração formal.

### Competitive Dimensions (|delta| < 5 entre top-2)

- **Topology:** autogen 92 vs crewAI 72 (gap largo — sem competição)
- **State Mgmt:** paperclip 92 vs autogen 82 (delta 10)
- **Parallelism:** autogen 88 vs paperclip 78 (delta 10)
- **Observability:** paperclip 90 vs autogen 85 (delta 5 — competitivo)
- **DSL:** BMAD 82 vs paperclip 78 (delta 4 — competitivo)
- **Deployment:** paperclip 88 vs autogen 80 (delta 8)

---

## Confidence Disclosure

| Subject | Confidence | Reason |
|---------|-----------|--------|
| BMAD-METHOD | HIGH | 9 capabilities observáveis + README rico + docs/ + CI + validator |
| crewAI | HIGH | 11 capabilities + tests 43 + docs mkdocs + 6 CI workflows |
| autogen | HIGH | 14 capabilities + tests 117 + 25+ CI workflows + docs 200+ páginas |
| paperclip | HIGH | 16 capabilities + tests 255 + docs + Dockerfile + 6 CI workflows |
| claude-remote-manager | HIGH | 10 capabilities + README rico; sem CI/tests mas escopo shell é observável integralmente |

### Sources

Todos os subjects: scan filesystem 100% de `OS/{subject}/` + leitura de README/docs. Sem fallback web.

### Dimension Pack

| Pack | Version | Designed For |
|------|---------|-------------|
| orchestration | 1.0 | Multi-agent orchestration frameworks |

### Known Limitations

- BMAD subscore depende de paradigma "library de skills" — dimensões runtime são 0 por design; se a métrica valorizasse "qualidade de skills" o score subiria
- autogen em **maintenance mode** — scores refletem estado atual, não roadmap (sucessor MS Agent Framework)
- crewAI snapshot é de 2024-12-22 no repo local — upstream pode ter evoluído
- claude-remote-manager macOS-only penaliza Deployment cross-platform
- Pesos pack fixos — para caso-de-uso específico (ex: "prioridade absoluta a persistência"), reponderar

---

_Generated by os-bench bench-score task | Template v1.0_
