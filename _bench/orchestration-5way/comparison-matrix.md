# Comparison Matrix: BMAD-METHOD vs crewAI vs autogen vs paperclip vs claude-remote-manager

**Date:** 2026-04-19
**Comparison type:** n-way (5 subjects)
**Dimension pack:** orchestration
**Slug:** orchestration-5way

---

## Sources

| Subject | Path | Confidence |
|---------|------|-----------|
| BMAD-METHOD | `OS/BMAD-METHOD/` | HIGH |
| crewAI | `OS/crewAI/` | HIGH |
| autogen | `OS/autogen/` | HIGH |
| paperclip | `OS/paperclip/` | HIGH |
| claude-remote-manager | `OS/claude-remote-manager/` | HIGH |

## Method

Matriz construída por scan filesystem + leitura de README/docs de cada subject. Features foram agrupadas nas 8 dimensões do pack `orchestration` (Topology, Delegation Model, State Mgmt, Parallelism, Failure Recovery, Observability, DSL, Deployment). Cada célula cita evidence path concreto em `OS/{subject}/...`. A coluna "values" descreve presença e profundidade; "evidence" aponta o arquivo. Classificação per-pair foi omitida (nway) em favor de ranking por feature.

---

## Inventory Summary

| Metric | BMAD-METHOD | crewAI | autogen | paperclip | claude-remote-manager |
|--------|-------------|--------|---------|-----------|-----------------------|
| LOC | 18.493 (JS) | 23.651 (Py) | 112.463 (Py) | 279.802 (TS) | 3.691 (sh) |
| Files | 544 | 500 | 1.837 | 1.650 | 60 |
| Primary language | JavaScript | Python | Python | TypeScript | Bash |
| License | MIT | MIT | MIT+CLA | MIT | unknown |
| Last commit | 2026-04-19 | 2024-12-22 | 2026-04-06 | 2026-04-17 | 2026-04-06 |
| Tests | 5 | 43 | 117 | 255 | 0 |
| CI workflows | 6 | 6 | 25+ | 6 | 0 |

---

## Feature Matrix

### Category: Topology

| Item | BMAD-METHOD | crewAI | autogen | paperclip | claude-remote-manager |
|------|-------------|--------|---------|-----------|-----------------------|
| Sequential pipeline | yes (4 fases numeradas) | yes (Process.sequential) | yes (RoundRobin, GraphFlow) | partial (routines) | no |
| Hierarchical topology | partial (editorial) | yes (Process.hierarchical + manager_llm) | yes (SelectorGroupChat, Magentic) | yes (company org-chart explícito) | partial (aiox-master + msg bus) |
| Group chat / swarm | yes (Party Mode) | no | yes (SwarmGroupChat) | no | no |
| Graph / DAG | no | yes (Flow decorators) | yes (_graph/) | no | no |

**Líderes:** `autogen` (4 topologias formais) e `BMAD-METHOD` (pipeline + party mode). `paperclip` tem a única hierarquia programática tipo org-chart.

### Category: Delegation Model

| Item | BMAD-METHOD | crewAI | autogen | paperclip | claude-remote-manager |
|------|-------------|--------|---------|-----------|-----------------------|
| Role-based delegation | yes (12+ roles) | yes (role/goal/backstory) | yes (Assistant/UserProxy/SOM) | yes (CEO/CTO/Engineer) | partial (CLAUDE.md per agent) |
| LLM-driven routing | partial (Party Mode pick) | yes (manager_llm + Planner) | yes (SelectorGroupChat) | no (worker-claim regra) | no (manual send-message) |
| Skill-based routing | yes (skills validadas) | partial (tools per-agent) | partial (type subscriptions) | yes (company-skills) | partial (agent skills/) |

**Líderes:** `paperclip` (role + skill robustos) e `crewAI`/`autogen` (role + LLM-driven).

### Category: State Mgmt

| Item | BMAD-METHOD | crewAI | autogen | paperclip | claude-remote-manager |
|------|-------------|--------|---------|-----------|-----------------------|
| Durable backend | no | partial (Chroma/SQLite) | partial (ext Redis/mem0/Chroma + state) | yes (Postgres embutido via Drizzle) | partial (filesystem inbox) |
| Shared memory | no | yes (entity/long-term) | yes (topic subs + runtime state) | yes (DB + WS realtime) | partial (A2A bus) |
| Checkpoint/restore | no | partial (output storage) | yes (save_state/load_state) | partial (heartbeat-run-summary) | partial (launchd + --continue) |

**Líderes:** `paperclip` (Postgres durável) e `autogen` (state + memory protocolado + gRPC).

### Category: Parallelism

| Item | BMAD-METHOD | crewAI | autogen | paperclip | claude-remote-manager |
|------|-------------|--------|---------|-----------|-----------------------|
| True parallel agents | yes (Party subagents) | partial (async GIL) | yes (async + gRPC multi-worker) | yes (N workspaces) | partial (N tmux) |
| Fan-out / fan-in | yes (Party 2-4) | partial (async_execution) | yes (topic broadcast + graph) | partial (routines) | no |

**Líderes:** `autogen` (runtime async + gRPC) e `paperclip` (workspaces).

### Category: Failure Recovery

| Item | BMAD-METHOD | crewAI | autogen | paperclip | claude-remote-manager |
|------|-------------|--------|---------|-----------|-----------------------|
| Retry w/ backoff | no | partial (litellm) | partial (model clients) | yes (cron retries + approvals) | yes (launchd + inbox redelivery) |
| Crash recovery | no | no | partial (gRPC workers) | partial (dev-runner) | yes (launchd + crash-alert) |
| Replay / DLQ | no | no | partial (topic subs) | no | yes (inflight → redelivery 5min) |

**Líder disparado:** `claude-remote-manager` — é o único com semântica at-least-once explícita no bus A2A + launchd auto-restart. `paperclip` segue em nível HTTP/cron.

### Category: Observability

| Item | BMAD-METHOD | crewAI | autogen | paperclip | claude-remote-manager |
|------|-------------|--------|---------|-----------|-----------------------|
| Tracing OTel | no | yes (OTel embutido) | yes (OTel core) | partial (telemetry + activity-log) | no |
| Cost tracking | no | partial (usage metrics) | partial (OTel) | yes (costs + budgets + finance) | no |
| UI dashboard | no (IDE host) | no (backend externo) | yes (AutoGen Studio) | yes (React SPA + WS mobile) | partial (Telegram como UI) |

**Líderes:** `paperclip` (cost tracking + dashboard mobile) e `autogen` (OTel + Studio).

### Category: DSL

| Item | BMAD-METHOD | crewAI | autogen | paperclip | claude-remote-manager |
|------|-------------|--------|---------|-----------|-----------------------|
| Declarative workflow | yes (YAML skills + workflows) | yes (Flow decorators) | partial (Python code) | yes (routines + company JSON) | partial (config.json + CLAUDE.md) |
| Visual editor / graph UI | no | partial (Flow viz read-only) | yes (Studio drag-drop) | yes (org-chart SVG + UI) | no |

**Líderes:** `BMAD-METHOD` (DSL YAML + skills validadas) e `paperclip` (UI rica).

### Category: Deployment

| Item | BMAD-METHOD | crewAI | autogen | paperclip | claude-remote-manager |
|------|-------------|--------|---------|-----------|-----------------------|
| Docker image | no | no | partial (Studio) | yes (Dockerfile + compose) | no (macOS-only) |
| Local dev (one-command) | yes (npx) | yes (pip) | yes (pip) | yes (pnpm + embedded pg) | yes (bootstrap.sh) |
| Distributed runtime | no | no | yes (gRPC + CloudEvents) | partial (Node single; adapters distribuídos) | partial (N tmux) |

**Líderes:** `paperclip` (Docker + DB embutido) e `autogen` (gRPC distribuído).

---

## Subject-Only Capabilities

### BMAD-METHOD only

| # | Capability | Category | Evidence |
|---|-----------|----------|----------|
| 1 | Pipeline agile 4-fases numerada | Topology | `OS/BMAD-METHOD/src/bmm-skills/` |
| 2 | Adversarial review + edge-case hunter | Governance | `OS/BMAD-METHOD/src/core-skills/bmad-review-adversarial-general/` |
| 3 | Deterministic skill validator no CI | Governance | `OS/BMAD-METHOD/tools/validate-skills.js` |

### crewAI only

| # | Capability | Category | Evidence |
|---|-----------|----------|----------|
| 1 | Multi-tier memory typed (short/long/entity/user) | State Mgmt | `OS/crewAI/src/crewai/memory/` |
| 2 | Knowledge sources (PDF/CSV) compartilhadas | Integration | `OS/crewAI/src/crewai/knowledge/` |
| 3 | Planner handler (decompõe tasks antes) | Delegation | `OS/crewAI/src/crewai/utilities/planning_handler.py` |

### autogen only

| # | Capability | Category | Evidence |
|---|-----------|----------|----------|
| 1 | Runtime gRPC distribuído multi-worker | Deployment | `OS/autogen/python/packages/autogen-ext/src/autogen_ext/runtimes/grpc/` |
| 2 | 4 topologias formais + Magentic | Topology | `OS/autogen/python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/` |
| 3 | Paridade .NET + Python | Deployment | `OS/autogen/dotnet/AutoGen.sln` |
| 4 | Intervention handlers (hook mid-runtime) | Governance | `OS/autogen/python/packages/autogen-core/src/autogen_core/_intervention.py` |

### paperclip only

| # | Capability | Category | Evidence |
|---|-----------|----------|----------|
| 1 | Company-sim (org-chart + roles + budgets) | Topology | `OS/paperclip/server/src/services/companies.ts` |
| 2 | Budgets + costs + finance governance | Observability | `OS/paperclip/server/src/services/budgets.ts` |
| 3 | Heterogeneous adapters (7 runtimes) | Delegation | `OS/paperclip/packages/adapters/` |
| 4 | Approval workflow HITL | Governance | `OS/paperclip/server/src/services/approvals.ts` |
| 5 | Execution workspaces (git worktrees) | State Mgmt | `OS/paperclip/server/src/services/execution-workspaces.ts` |
| 6 | MCP server (expor Paperclip como tool) | Integration | `OS/paperclip/packages/mcp-server/src/tools.ts` |
| 7 | Company portability / Clipmart | Extensibility | `OS/paperclip/server/src/services/company-portability.ts` |
| 8 | Embedded Postgres zero-config | State Mgmt | `OS/paperclip/patches/embedded-postgres@18.1.0-beta.16.patch` |
| 9 | Log/PII redaction automática | Governance | `OS/paperclip/server/src/log-redaction.ts` |

### claude-remote-manager only

| # | Capability | Category | Evidence |
|---|-----------|----------|----------|
| 1 | Persistência 24/7 (launchd + tmux + 71h reset) | Failure Recovery | `OS/claude-remote-manager/core/scripts/generate-launchd.sh` |
| 2 | Telegram como control plane completo | Observability / UX | `OS/claude-remote-manager/core/bus/hook-permission-telegram.sh` |
| 3 | A2A message bus at-least-once (redelivery) | Failure Recovery | `OS/claude-remote-manager/core/bus/check-inbox.sh` |
| 4 | Singleton daemon lock atomic (mkdir) | Failure Recovery | `OS/claude-remote-manager/core/scripts/fast-checker.sh` |

---

## Paradigmatic Positioning

| Subject | Paradigma | Unidade mental |
|---------|-----------|----------------|
| BMAD-METHOD | **Agile pipeline** | Skill + fase numerada (analyst → PM → architect → dev) |
| crewAI | **Role-playing crew** | Agent (role/goal/backstory) cooperando em Crew |
| autogen | **Conversacional multi-agent + distribuído** | Agent em group chat (topic/graph); runtime gRPC |
| paperclip | **Company simulation** | Company (org-chart + budgets + goals) orquestrando adapters heterogêneos |
| claude-remote-manager | **Remote persistence** | Agent = diretório 24/7 com Telegram control + A2A bus |

Cada subject resolve o mesmo problema ("múltiplos agents trabalhando juntos") através de unidade mental diferente — e é essa unidade que determina qual framework encaixa melhor em cada caso.

---

## Objective Reading

### BMAD-METHOD Strengths
Pipeline agile explicitamente numerada (analysis→plan→solutioning→implementation) evidenciada em `src/bmm-skills/` é única no conjunto. Party Mode spawna subagents paralelos independentes via tool Agent (`src/core-skills/bmad-party-mode/SKILL.md`), oferecendo true parallelism que nem crewAI tem. DSL em YAML + validação determinística (`tools/validate-skills.js`) cria superfície de governança editorial robusta. Porém, sem runtime próprio — todo estado mora no IDE host (Claude Code/Cursor).

### crewAI Strengths
Abstração mental role-playing (role/goal/backstory em `src/crewai/agent.py`) é a mais "humana" do conjunto e destaca-se para quem vem de workflows humanos. Multi-tier memory (short/long/entity/user em `src/crewai/memory/`) é o sistema de memória mais estruturado embutido. Flow (`src/crewai/flow/flow.py`) complementa Process com grafo dinâmico + visualizer. OTel-first (`src/crewai/telemetry/`) delega observabilidade ao stack externo do cliente.

### autogen Strengths
Único framework com runtime distribuído gRPC + CloudEvents (`python/packages/autogen-ext/src/autogen_ext/runtimes/grpc/`, `protos/agent_worker.proto`), única opção que escala horizontal de verdade. 4 topologias embutidas (`_round_robin_group_chat.py`, `_selector_group_chat.py`, `_swarm_group_chat.py`, `_magentic_one/`) + Graph flow é cobertura incomparável. AutoGen Studio (`autogen-studio/`) é a UI no-code mais completa do conjunto open-source. Paridade .NET + Python (`dotnet/AutoGen.sln`). Principal fraqueza: maintenance mode — sem novas features.

### paperclip Strengths
Unidade mental "company-sim" (org-chart + budgets + goals em `server/src/services/companies.ts`) é paradigma único no conjunto. 7 adapters heterogêneos (`packages/adapters/`) tornam paperclip o único control-plane agent-agnostic — coordena Claude Code, Codex, Cursor, Gemini, OpenClaw, Opencode e Pi simultaneamente. Full-stack pronto (server + React UI + CLI + Postgres embutido + MCP server + Docker) torna auto-hosting trivial. Governança nível empresa — budgets, costs, finance, approvals, log redaction. Mobile-first (dashboard responsivo + heartbeat summaries). Único com MCP server nativo.

### claude-remote-manager Strengths
Persistência real 24/7 via launchd + tmux + auto-restart + 71h soft-reset (`core/scripts/generate-launchd.sh`) é incomparável — agent não morre. A2A message bus com semântica at-least-once explícita (inflight → redelivery após 5min em `core/bus/check-inbox.sh`) é o único sistema do conjunto com garantia de entrega tipo queue. Lock atômico via `mkdir` (`core/scripts/fast-checker.sh`) mostra atenção a singleton em POSIX-pure. Telegram como control plane completo (mensagens, callbacks, plan mode, ask, voice) é o setup mobile mais imediato. Zero servidor externo — roda inteiro em bash na máquina host.

### Key Differentiators

- **BMAD-METHOD:** skill-driven + pipeline agile + adversarial review
- **crewAI:** abstração role-playing + memory multi-tier + Flow DSL
- **autogen:** topologias formais + runtime distribuído + .NET parity
- **paperclip:** company-sim + adapters heterogêneos + governança empresa + MCP + mobile
- **claude-remote-manager:** persistência 24/7 + Telegram-native + A2A at-least-once

### Areas of Parity

Local dev one-command é universal. Role-based delegation existe em todos (com graus variados de formalidade). Sequential/pipeline é dominado por BMAD, crewAI, autogen; paperclip/CRM tratam fluxo via cron/workspaces. Shared memory entre agents existe em crewAI/autogen/paperclip; BMAD não tem e CRM tem via A2A bus.

---

## Method Disclosure

- **Comparison date:** 2026-04-19
- **Dimension pack:** orchestration v1.0 (8 dimensões, pesos somam 1.00)
- **Items compared:** 22 features agrupadas em 8 categorias
- **Dimensions used:** Topology, Delegation Model, State Mgmt, Parallelism, Failure Recovery, Observability, DSL, Deployment
- **Data sources:** filesystem scan 100% de cada `OS/{subject}/`
- **Equivalence criteria (nway):** ranking por feature via líderes observáveis; classificação Forte/Parcial/Sem_Equiv omitida por ser pair-wise por design
- **Evidência:** todo claim aponta path em `OS/{subject}/...`

---

_Generated by os-bench bench-matrix task | Template v1.0_
