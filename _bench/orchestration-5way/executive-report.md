# Executive Report: orchestration-5way

**Date:** 2026-04-19
**Type:** n-way (5 subjects)
**Slug:** orchestration-5way
**Dimension pack:** orchestration (8 dimensões, pesos somam 1.00)

---

## Executive Summary

Este benchmark compara cinco frameworks de orquestração multi-agente que resolvem o mesmo problema — coordenar múltiplos agentes — através de **unidades mentais fundamentalmente diferentes**: `BMAD-METHOD` (pipeline agile numerada), `crewAI` (role-playing crew cooperativa), `autogen` (conversacional multi-agent com runtime distribuído), `paperclip` (company-sim com org-chart, budgets e governança) e `claude-remote-manager` (remote-persistence via launchd+tmux+Telegram). No score ponderado, **paperclip (79.62)** e **autogen (79.14)** ficam em empate técnico no topo (delta 0.48 pt), mas por razões opostas: paperclip lidera via profundidade operacional (state mgmt + observabilidade + deployment) e autogen via profundidade técnica (topologias formais + runtime distribuído + paralelismo). crewAI (67.54) fica no meio com um perfil balanceado, enquanto BMAD (50.70) e CRM (48.58) fecham — não por serem piores, mas porque são otimizados para nichos específicos (skill-driven pipeline; persistência 24/7 via Telegram) que o pack orchestration padrão sub-representa. **Recomendação high-level:** a escolha entre os cinco não é "qual vence" — é "qual paradigma encaixa no seu caso de uso".

---

## Key Metrics

| Metric | Value |
|--------|-------|
| Overall Winner | paperclip (79.62/100) — delta 0.48 vs autogen (empate técnico) |
| Dimensions analyzed | 8 |
| paperclip wins | 3 de 8 (State, Obs, Deployment) |
| autogen wins | 2 de 8 (Topology, Parallelism) |
| crewAI wins | 1 (Delegation) |
| BMAD wins | 1 (DSL) |
| CRM wins | 1 (Failure Recovery) |
| Ties | 0 |
| Confidence overall | HIGH |

---

## Scorecard Summary

| Dimension | Weight | BMAD | crewAI | autogen | paperclip | CRM | Winner |
|-----------|:------:|:----:|:------:|:-------:|:---------:|:---:|:------:|
| Topology | 15% | 70 | 72 | **92** | 68 | 25 | autogen |
| Delegation | 15% | 75 | **85** | 82 | 80 | 45 | crewAI |
| State Mgmt | 12% | 20 | 78 | 82 | **92** | 55 | paperclip |
| Parallelism | 12% | 72 | 58 | **88** | 78 | 55 | autogen |
| Failure Recovery | 13% | 15 | 45 | 62 | 68 | **82** | CRM |
| Observability | 12% | 12 | 70 | 85 | **90** | 40 | paperclip |
| DSL | 11% | **82** | 72 | 58 | 78 | 42 | BMAD |
| Deployment | 10% | 55 | 55 | 80 | **88** | 48 | paperclip |
| **Weighted total** | **100%** | **50.70** | **67.54** | **79.14** | **79.62** | **48.58** | **paperclip** |

---

## Paradigmatic Positioning

Antes das dimensões, a leitura mais útil é por paradigma. Cada subject resolve orquestração através de uma **unidade mental distinta**, e é essa unidade que determina adequação a cada caso.

| Subject | Paradigma | Unidade | Quando brilha |
|---------|-----------|---------|---------------|
| BMAD-METHOD | Agile pipeline | Skill + fase numerada | SDLC estruturado (análise→plan→dev), workflows editoriais |
| crewAI | Role-playing crew | Agent com role/goal/backstory | Cooperação humana-like, tarefas criativas com personas |
| autogen | Conversacional + distribuído | Agent em group chat com topologias formais | Research/experimentação técnica, escala horizontal gRPC |
| paperclip | Company simulation | Company (org-chart + budgets + goals) | Empresas autônomas, governance cross-runtime, ops mobile |
| claude-remote-manager | Remote persistence | Agent-dir 24/7 + Telegram + A2A bus | Agents que não podem morrer, controle mobile fora da máquina |

---

## Dimension Analysis

### Topology (15% weight)

**Scores:** autogen 92 · crewAI 72 · BMAD 70 · paperclip 68 · CRM 25

autogen é disparadamente o mais rico em topologias formais — 4 implementações distintas (`_round_robin_group_chat.py`, `_selector_group_chat.py`, `_swarm_group_chat.py`, `_magentic_one/`) mais graph DAG via `_graph/`, além do orquestrador Magentic-One. BMAD-METHOD codifica pipeline agile numerada nas 4 fases (`src/bmm-skills/{1-analysis,2-plan-workflows,3-solutioning,4-implementation}/`) e adiciona Party Mode (roundtable de subagents reais). crewAI oferece sequential/hierarchical em `Process` enum + Flow graph. paperclip tem a única topologia hierarchical **programática** (org-chart DB-backed com roles CEO/CTO/Engineer) — conceitualmente única, mas não cobre as outras topologias. claude-remote-manager não orquestra — agents são dirs independentes conectados só pelo msg bus.

**Key signals:**
- autogen: `python/packages/autogen-agentchat/src/autogen_agentchat/teams/_group_chat/` (4 topologias + graph)
- BMAD: `src/bmm-skills/` (pipeline) + `src/core-skills/bmad-party-mode/SKILL.md`
- paperclip: `server/src/services/company-member-roles.ts` + `routes/org-chart-svg.ts`

### Delegation Model (15%)

**Scores:** crewAI 85 · autogen 82 · paperclip 80 · BMAD 75 · CRM 45

crewAI lidera porque combina role-based (role/goal/backstory em `src/crewai/agent.py`) com LLM-driven routing via `manager_llm` e Planner automático que decompõe tasks antes da execução. autogen segue próximo via `SelectorGroupChat` (LLM escolhe próximo speaker), `_handoff.py` primitive e type subscriptions por tópico. paperclip é único com delegação **cross-runtime** — 7 adapters (claude-local, codex-local, cursor-local, gemini-local, openclaw-gateway, opencode-local, pi-local) permitem orquestrar agents de provedores diferentes na mesma "empresa". BMAD tem 12+ roles formalizados como skills mas delegação é editorial (documentada em MD). CRM tem só `send-message <to>` manual.

**Key signals:**
- crewAI: `src/crewai/utilities/planning_handler.py`, `src/crewai/agent.py`
- paperclip: `packages/adapters/` (7 runtimes)
- autogen: `teams/_group_chat/_selector_group_chat.py`, `base/_handoff.py`

### State Mgmt (12%)

**Scores:** paperclip 92 · autogen 82 · crewAI 78 · CRM 55 · BMAD 20

paperclip domina com Postgres embutido via Drizzle ORM (`packages/db/` + `patches/embedded-postgres@18.1.0-beta.16.patch`), execution workspaces com git worktrees isolados por agent/task (`services/execution-workspaces.ts`), WS realtime para shared state (`realtime/live-events-ws.ts`) e heartbeat run summaries como checkpoints (`services/heartbeat-run-summary.ts`). autogen oferece save_state/load_state explícitos em agents e teams (`autogen-agentchat/.../state/`) e memory protocol plugável com backends Redis/mem0/Chroma em ext. crewAI tem multi-tier memory typed (short/long/entity/user). CRM é durable via filesystem inbox mas rudimentar. BMAD não tem runtime próprio — estado fica no IDE host.

### Parallelism (12%)

**Scores:** autogen 88 · paperclip 78 · BMAD 72 · crewAI 58 · CRM 55

autogen é o único com runtime distribuído formal — gRPC multi-worker via `autogen-ext/src/autogen_ext/runtimes/grpc/` + protos `agent_worker.proto` e `cloudevent.proto` — capacidade de escalar horizontal de verdade. paperclip paraleliza via N execution workspaces isolados. BMAD via Party Mode spawna subagents paralelos reais através do Agent tool. crewAI sofre GIL + sync-by-default (async_execution parcial). CRM paraleliza via N tmux sessions independentes mas sem fan-out coordenado.

### Failure Recovery (13%)

**Scores:** CRM 82 · paperclip 68 · autogen 62 · crewAI 45 · BMAD 15

**claude-remote-manager domina disparado** — é o único do conjunto com semântica **at-least-once** explícita no bus A2A: mensagens vão para inflight, são ACK'das no reply, e redelivery automático em 5 min se não houver ACK (`core/bus/check-inbox.sh`). Combinado com launchd watchdog (`core/scripts/generate-launchd.sh`), crash-alert (`core/scripts/crash-alert.sh`) e soft-reset a cada 71h (`core/bus/self-restart.sh`), CRM é o único framework que genuinamente não perde trabalho em crash. paperclip segundo via approval retry flows + cron service retries + dev-runner-worktree resilient. autogen oferece gRPC worker resilience mas sem DLQ formal. crewAI apenas retries de LLM call via litellm. BMAD sem recovery (fica no IDE).

**Key signals CRM:**
- `core/bus/check-inbox.sh` (inflight → redelivery)
- `core/scripts/generate-launchd.sh` (watchdog OS-level)
- `core/bus/self-restart.sh` (71h reset)
- `core/scripts/crash-alert.sh` (Telegram notify)

### Observability (12%)

**Scores:** paperclip 90 · autogen 85 · crewAI 70 · CRM 40 · BMAD 12

paperclip é o único com **cost tracking de nível empresa** — services dedicados para `costs.ts`, `budgets.ts`, `finance.ts` — além de React dashboard com WS realtime mobile (`ui/` + `realtime/live-events-ws.ts`), heartbeat summaries, activity log e promptfoo evals no CI. autogen segundo com OTel core tracing (`autogen-core/.../_telemetry/`) + AutoGen Studio UI + agbench harness. crewAI delega observabilidade via OTel wiring (`src/crewai/telemetry/`) + usage metrics. CRM usa Telegram como UI improvisado e arquivos de log per-agent. BMAD não tem nada embutido.

### DSL (11%)

**Scores:** BMAD 82 · paperclip 78 · crewAI 72 · autogen 58 · CRM 42

**BMAD lidera** — é o único com DSL YAML + MD + skill validator determinístico no CI (`tools/validate-skills.js`). A combinação de frontmatter tipado + MD + schema enforcement cria uma camada de governança editorial que nenhum outro subject tem. paperclip segundo com routines declarativas + company portability JSON serializável + org-chart SVG editor. crewAI via Flow decorators + visualizer HTML + YAML scaffolding da CLI. autogen é code-first em Python (Studio cobre via GUI no-code mas sem DSL declarativa). CRM tem config.json + CLAUDE.md persona — mínimo funcional.

### Deployment (10%)

**Scores:** paperclip 88 · autogen 80 · BMAD 55 · crewAI 55 · CRM 48

paperclip é o mais "production-ready" — Dockerfile root + docker/ dir + embedded Postgres zero-config + MCP server distribuível via `npx -y @paperclipai/mcp-server` + monorepo pnpm com hot-reload. autogen via pip + Studio Dockerfile + gRPC distributed runtime. BMAD/crewAI são library-style (apenas one-command install). CRM tem bootstrap.sh curl-one-liner excelente mas macOS-only é limitação dura (depende de launchd).

---

## Strategic Recommendations

### 1. Use paperclip se seu caso de uso é "empresa autônoma de agentes heterogêneos"

A abstração company-sim + governance (budgets, costs, approvals) + 7 adapters para runtimes diferentes torna paperclip o único framework projetado para coordenar agents de **diferentes stacks** (Claude, Codex, Cursor, Gemini, OpenClaw) sob uma mesma organização. Se você precisa audit log, cost tracking e dashboard mobile desde o dia 1, é ele.

- **Target:** teams que operam múltiplos agents de provedores diferentes
- **Addresses:** State Mgmt + Observability + Delegation cross-runtime
- **Expected impact:** single control plane para empresa autônoma heterogênea
- **Priority:** P0

### 2. Use autogen se seu caso é "research/experimentação técnica com topologias formais + escala"

autogen entrega topologias formais (round-robin, selector LLM-driven, swarm, magentic, graph) e o único runtime gRPC distribuído do conjunto. Apesar do **maintenance mode**, é a referência técnica para quem precisa experimentar diferentes configurações de topologia ou escalar horizontal.

- **Target:** research labs, experimentação cross-topology, workloads multi-worker
- **Addresses:** Topology + Parallelism + Paridade .NET
- **Caveat:** **maintenance mode** — sem novas features; considerar MS Agent Framework para projetos novos
- **Priority:** P1 (com olhar para migração futura)

### 3. Use crewAI se seu caso é "abstração role-playing humana para tarefas cooperativas"

A metáfora "crew" (time com role/goal/backstory) é a mais intuitiva para quem vem de workflows humanos. Planner automático + multi-tier memory + Flow DSL cobrem bem coordenação cooperativa.

- **Target:** product teams que mapeiam agents a papéis humanos (marketer, analyst, writer)
- **Addresses:** Delegation + memory typed
- **Priority:** P1

### 4. Use BMAD-METHOD como **camada editorial** sobre qualquer coding agent

BMAD não é runtime — é pacote de skills. Use como metodologia agile dentro do Claude Code/Cursor quando o workflow é SDLC estruturado (analysis → plan → architecture → dev → QA). Pode coexistir com os outros (usar BMAD para descrever skills, rodar no Claude Code, orquestrar via paperclip ou CRM).

- **Target:** SDLC estruturado dentro de IDE-based coding agents
- **Addresses:** DSL + metodologia
- **Priority:** P2 (complementar)

### 5. Use claude-remote-manager para agents que **não podem morrer** + controle mobile

Se o requisito é "agent 24/7 com controle via Telegram" (ex: ops, monitoring, trading, content-growth autônomo), CRM é insubstituível — nenhum outro no conjunto tem launchd + tmux + at-least-once A2A + Telegram approvals. macOS-only, porém.

- **Target:** agents persistentes remotos controlados pelo celular
- **Addresses:** Failure Recovery (disparado)
- **Caveat:** macOS-only (launchd)
- **Priority:** P1 para o caso de uso específico

### 6. Combinações produtivas

- **paperclip + claude-remote-manager:** paperclip orquestra companies; CRM fornece o substrato de agent persistente 24/7 via Telegram
- **paperclip + BMAD:** BMAD fornece skills/DSL; paperclip fornece control plane e governance
- **autogen + paperclip:** autogen como runtime distribuído gRPC; paperclip como control plane governado
- **crewAI + BMAD:** crewAI estrutura cooperação; BMAD fornece skills agile validadas

---

## When to Pick Which

### Choose BMAD-METHOD if…

- Seu workflow é SDLC estruturado (analysis → plan → architect → dev → QA)
- Você usa Claude Code/Cursor e quer skills validadas como layer editorial
- Valoriza DSL tipada + schema enforcement no CI
- Precisa de roundtable multi-agent (Party Mode) para perspectivas cruzadas

### Choose crewAI if…

- A metáfora role-playing (role/goal/backstory) encaixa no mental model do time
- Precisa de multi-tier memory typed (short/long/entity/user) embutido
- Quer LLM-driven planning automático
- OTel-first backend externo é OK (não precisa de dashboard próprio)
- Stack Python é requisito

### Choose autogen if…

- Precisa de múltiplas topologias formais (round-robin, selector, swarm, graph)
- Escala horizontal via gRPC multi-worker é requisito
- Paridade .NET + Python é necessária
- AutoGen Studio no-code serve como GUI para stakeholders
- **Você aceita o risco de maintenance mode** (ou está disposto a migrar para MS Agent Framework)

### Choose paperclip if…

- Você quer operar "zero-human companies" (agents autônomos em org-chart)
- Orquestra agents de **provedores heterogêneos** (Claude + Codex + Cursor + OpenClaw)
- Cost tracking + budgets + approvals são requisitos (governance enterprise)
- Mobile-first (dashboard + mobile notifications) é prioridade
- Auto-hosting Docker com DB embutido é preferível a SaaS

### Choose claude-remote-manager if…

- Seus agents **não podem morrer** (crash = retomar do último ACK)
- Controle remoto via Telegram é o UX primário
- Você está em macOS (launchd é requisito hard)
- A2A at-least-once entre agents é importante
- Setup deve ser zero-serviço (bash + tmux only)

### Consider combining if…

- Você precisa de skills estruturadas BMAD DENTRO de uma company paperclip com fallback CRM persistente
- Autogen gRPC como runtime distribuído, paperclip como control plane
- Qualquer framework + MCP: paperclip MCP server + crewAI client, por exemplo

---

## Methodology

### Data Sources

| Subject | Source | Method | Confidence |
|---------|--------|--------|------------|
| BMAD-METHOD | `OS/BMAD-METHOD/` | filesystem-scan + doc-scan | HIGH |
| crewAI | `OS/crewAI/` | filesystem-scan + doc-scan | HIGH |
| autogen | `OS/autogen/` | filesystem-scan + doc-scan | HIGH |
| paperclip | `OS/paperclip/` | filesystem-scan + doc-scan | HIGH |
| claude-remote-manager | `OS/claude-remote-manager/` | filesystem-scan + doc-scan | HIGH |

### Scoring Method

- **Dimension pack:** orchestration v1.0 (8 dimensões)
- **Weights sum:** 1.00 (verificado)
- **Score range:** 0–100 por dimensão
- **Evidence requirement:** score ≥90 precisa de 2+ signals observáveis com evidence path; aplicado em todos os 90+ scores
- **Confidence rollup:** HIGH (todos os subjects com 9+ capabilities observadas com evidence)
- **Nenhum claim inventado** — cada signal aponta arquivo concreto em `OS/{subject}/`

### Artifacts Generated

| Artifact | File | Status |
|----------|------|:------:|
| Metadata | `metadata.json` | OK |
| Inventory BMAD | `_inventories/BMAD-METHOD/inventory.{json,md}` | OK |
| Inventory crewAI | `_inventories/crewAI/inventory.{json,md}` | OK |
| Inventory autogen | `_inventories/autogen/inventory.{json,md}` | OK |
| Inventory paperclip | `_inventories/paperclip/inventory.{json,md}` | OK |
| Inventory CRM | `_inventories/claude-remote-manager/inventory.{json,md}` | OK |
| Comparison Matrix | `comparison-matrix.{json,md}` | OK |
| Scorecard | `scorecard.{json,md}` | OK |
| Executive Report | `executive-report.md` | OK |
| Gap Analysis | `gap-analysis.{json,md}` | SKIP (nway design) |
| Battle Card | `battle-card.md` | SKIP (nway design) |

### Limitations

- BMAD pontua baixo em dimensões runtime (State/Recovery/Obs) por design — é library de skills, não runtime. Para o nicho "pipeline agile editorial", o valor real está acima do weighted total.
- autogen está em **maintenance mode** (README banner). Scores refletem capability atual, não roadmap. Projetos novos devem avaliar Microsoft Agent Framework como sucessor.
- crewAI snapshot local é de 2024-12-22 — versão atual upstream pode ter evoluído.
- claude-remote-manager é macOS-only (launchd) — penaliza Deployment cross-platform.
- Pesos do pack são fixos. Para caso de uso específico (ex: priorizar persistência 24/7 ou topology formal), reponderar as dimensões produz ranking diferente.
- GitHub stars/contributors não foram coletados (local-first); para dados de comunidade, consultar `README.md` badges de cada repo.

---

## Appendix: Source Artifacts

Todos os artefatos em `OS/_bench/orchestration-5way/`:

| # | File | Type | Format |
|---|------|------|--------|
| 1 | `metadata.json` | Metadata | JSON |
| 2 | `_inventories/BMAD-METHOD/inventory.json` | Inventory | JSON |
| 3 | `_inventories/BMAD-METHOD/inventory.md` | Inventory | MD |
| 4 | `_inventories/crewAI/inventory.json` | Inventory | JSON |
| 5 | `_inventories/crewAI/inventory.md` | Inventory | MD |
| 6 | `_inventories/autogen/inventory.json` | Inventory | JSON |
| 7 | `_inventories/autogen/inventory.md` | Inventory | MD |
| 8 | `_inventories/paperclip/inventory.json` | Inventory | JSON |
| 9 | `_inventories/paperclip/inventory.md` | Inventory | MD |
| 10 | `_inventories/claude-remote-manager/inventory.json` | Inventory | JSON |
| 11 | `_inventories/claude-remote-manager/inventory.md` | Inventory | MD |
| 12 | `comparison-matrix.json` | Matrix | JSON |
| 13 | `comparison-matrix.md` | Matrix | MD |
| 14 | `scorecard.json` | Scoring | JSON |
| 15 | `scorecard.md` | Scoring | MD |
| 16 | `executive-report.md` | Report | MD |

---

_Generated by os-bench bench-executive-report task | Template v1.0_
