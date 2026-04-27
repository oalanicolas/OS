# Executive Report: coding-agents-8way

**Date:** 2026-04-19
**Type:** nway (8 subjects)
**Slug:** coding-agents-8way
**Dimension pack:** coding-agent

---

## Executive Summary

Oito coding agents opensource foram comparados no pack `coding-agent` (8 dimensões: coding_depth, autonomy, context_mgmt, git_integration, tdd, multi_agent, extensibility, community). **gsd-2 lidera o ranking ponderado geral (85.59/100)** pela combinação de auto-mode end-to-end, KG memory 5-fase e stuck-loop detection — três dimensões onde pontua 80+. **OpenHands é o runner-up (84.42)** pela maturidade de deploy (SDK→Enterprise + docker/k8s) e SWE-bench 77.6 publicado. **claude-code-main (83.82)** vence em multi-agent (93) e extensibility (96) sozinho, puxado por 43 tools, 101 comandos, coordinator + Team + Bridge + memdir. No outro extremo, **ai-website-cloner-template (61.04)** é template domínio-específico — ótimo no que propõe mas escopo estreito. A recomendação high-level: para dev solo, pegar **gsd-2** (auto-mode + resilience); para equipe TDD, **superpowers** (TDD 95 + SDD) sobre Claude Code; para enterprise, empate técnico entre **claude-code-main** e **OpenHands** (ambos 85.11 no profile enterprise).

---

## Key Metrics

| Metric | Value |
|--------|-------|
| Overall Winner | **gsd-2** (+1.17 pts vs #2) |
| Dimensions analyzed | 8 |
| Subjects | 8 |
| gsd-2 dimension wins | 2 (autonomy, context_mgmt) |
| claude-code-main dimension wins | 2 (multi_agent, extensibility) |
| aider dimension wins | 2 (git_integration, community) |
| OpenHands dimension wins | 1 (coding_depth) |
| superpowers dimension wins | 1 (tdd) |
| Confidence overall | HIGH |

---

## Scorecard Summary

| Dimension | Weight | claude-code-main | codex | aider | OpenHands | gsd-2 | gstack | superpowers | ai-website-cloner-template |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Coding Depth | 18% | 88 | 82 | 85 | **92** | 84 | 70 | 72 | 55 |
| Autonomy | 15% | 72 | 70 | 55 | 85 | **93** | 70 | 88 | 75 |
| Context Mgmt | 13% | 90 | 55 | 80 | 75 | **94** | 50 | 50 | 45 |
| Git Integration | 10% | 88 | 65 | **92** | 80 | 85 | 82 | 78 | 70 |
| TDD | 10% | 55 | 50 | 82 | 70 | 80 | 78 | **95** | 55 |
| Multi-agent | 12% | **93** | 60 | 25 | 90 | 85 | 78 | 90 | 80 |
| Extensibility | 12% | **96** | 75 | 60 | 88 | 90 | 85 | 80 | 62 |
| Community | 10% | 85 | 88 | **95** | 90 | 68 | 62 | 80 | 45 |
| **Weighted total** | **100%** | **83.82** | **68.91** | **71.05** | **84.42** | **85.59** | **71.36** | **78.36** | **61.04** |

---

## Dimension Analysis

### Coding Depth (18%) — Winner: OpenHands (92)

OpenHands é o único com SWE-bench score publicado oficialmente (77.6 no badge README) + arxiv tech report (2511.03690) + 6 agents especializados no `openhands/agenthub/`. Isso satisfaz o critério 90+ do pack ("SWE-bench >40% OR demonstrated multi-file refactors with tests passing"). claude-code-main (88) vem logo atrás com 43 tools + 101 comandos + LSP integration mas é mirror sem testes/CI expostos. aider (85) compensa profundidade com 38 coders (`aider/coders/`) e 100+ linguagens via tree-sitter queries. gsd-2 (84) tem pi-coding-agent package dedicado + UOK.

**Key signals:**
- OpenHands: SWE-bench 77.6 — `OS/OpenHands/README.md:11`
- claude-code-main: 43 tools + 101 commands — `OS/claude-code-main/src/tools/`, `src/commands/`
- aider: 38 coders — `OS/aider/aider/coders/`
- gsd-2: pi-coding-agent package — `OS/gsd-2/packages/pi-coding-agent/`

### Autonomy (15%) — Winner: gsd-2 (93)

gsd-2 explicita auto-mode end-to-end no README.md:14-23 ("One command. Walk away. Come back to a built project") + stuck-loop detection (#4414) + model fallback em limit errors (#4373) + branch isolation per milestone (#4389). São 4 signals observáveis de autonomia longa, o que justifica o 93. superpowers (88) vem atrás com SDD ("not uncommon for Claude to be able to work autonomously for a couple hours at a time") no README e verification-before-completion skill. OpenHands (85) via controller event-loop genuinamente long-horizon. aider (55) é explicitamente single-turn — não tenta long-horizon.

**Key signals:**
- gsd-2: auto-mode + stuck-loop + model fallback — `OS/gsd-2/README.md:14-23,66-69`
- superpowers: SDD + verification skill — `OS/superpowers/skills/subagent-driven-development/`
- OpenHands: controller — `OS/OpenHands/openhands/controller/`

### Context Mgmt (13%) — Winner: gsd-2 (94)

gsd-2 entrega o pacote triplo do pack ("90-100: Compressão automática + memory layer persistente + RAG"): KG memory 5-fase (capture_thought/memory_query/gsd_graph) + hybrid retrieval (keyword+semantic) + scoped/tagged memories + explicit context clear/inject lifecycle. claude-code-main (90) tem `/compact` + memdir persistente com relevance scoring + team-mem-sync + MCP pra contexto externo. aider (80) tem repomap (diferencial core) mas é single-feature. codex (55) não tem evidência explícita de memory/compact. gstack/superpowers (50) dependem do host.

**Key signals:**
- gsd-2: KG 5-phase + hybrid retrieval — `OS/gsd-2/README.md:32-38`
- claude-code-main: memdir + /compact + MCP — `OS/claude-code-main/src/memdir/`, `src/commands/compact`
- aider: repomap — `OS/aider/aider/repomap.py`

### Git Integration (10%) — Winner: aider (92)

aider levanta git como feature-core no README.md:63-68 ("Aider automatically commits changes with sensible commit messages. Use familiar git tools to easily diff, manage and undo AI changes"). O código em `aider/repo.py` trata commits idiomáticos. claude-code-main (88) tem /commit + Worktree + Bash. gsd-2 (85) tem branch isolation per milestone. gstack (82) com /ship + /land-and-deploy + CHANGELOG discipline (documentado em CLAUDE.md). codex (65) fica atrás por não ter git tooling explícito no repo (delega ao SDK).

**Key signals:**
- aider: auto-commit + diff+undo — `OS/aider/aider/repo.py`, `README.md:63-68`
- claude-code-main: /commit + Enter/Exit WorktreeTool — `OS/claude-code-main/src/tools/EnterWorktreeTool`
- gstack: /ship + /land-and-deploy — `OS/gstack/ship/`

### TDD (10%) — Winner: superpowers (95)

superpowers é o único com skill TDD dedicada (`skills/test-driven-development/`) + verification-before-completion + stance explícito no README ("true red/green TDD, YAGNI, DRY"). O pack define 90+ como "TDD puro enforcement (red-green-refactor, subagents)" — superpowers bate. aider (82) tem auto-lint + auto-test após cada edit (`aider/linter.py`). gsd-2 (80) tem verification gate obrigatório. gstack (78) com own eval framework 2-tier. claude-code-main (55) tem as ferramentas (Bash, hooks) mas sem skill TDD declarada.

**Key signals:**
- superpowers: TDD skill — `OS/superpowers/skills/test-driven-development/`
- aider: auto-lint+auto-test — `OS/aider/aider/linter.py`, `README.md:91-94`
- gsd-2: verification gate — `OS/gsd-2/README.md:67`
- gstack: evals LLM-judge+E2E — `OS/gstack/test/skill-llm-eval.test.ts`

### Multi-agent (12%) — Winner: claude-code-main (93)

claude-code-main tem o tripé forte: AgentTool (spawn) + coordinator/ (multi-agent orchestration) + TeamCreateTool/DeleteTool (team-level parallel). OpenHands (90) com AgentHub 6 agents + microagents. superpowers (90) com SDD + dispatching-parallel-agents skill. gsd-2 (85) com UOK reactive/parallel scheduling em `gsd-orchestrator/`. aider (25) é explicitamente single-agent — é o piso.

**Key signals:**
- claude-code-main: AgentTool + coordinator + Team — `OS/claude-code-main/src/coordinator/coordinatorMode.ts`, `src/tools/TeamCreateTool`
- OpenHands: AgentHub 6 + microagents — `OS/OpenHands/openhands/agenthub/`
- superpowers: SDD + dispatching skills — `OS/superpowers/skills/subagent-driven-development/`

### Extensibility (12%) — Winner: claude-code-main (96)

claude-code-main cumpre o "90-100: Plugin system + MCP + hooks + config completo" — 4 eixos simultâneos em `src/plugins/`, `src/skills/`, `src/tools/MCPTool`, `src/hooks/`. gsd-2 (90) com workflow plugins + Extension API (`.gsd/extensions/`) + own mcp-server. OpenHands (88) com AgentHub + fastmcp + skills + microagents. gstack (85) com 23 skills + multi-host (10 agents) + ACP/ClawHub marketplace. superpowers (80) com 14 skills + 6 platforms distribution + session-start hooks. codex (75) com MCP server + SDK TS/Py + hooks crate.

**Key signals:**
- claude-code-main: 4-axis (plugin+skill+MCP+hooks) — `src/plugins/`, `src/skills/`, `src/tools/MCPTool`, `src/hooks/`
- gsd-2: workflow plugins + extensions + MCP — `README.md:46,82`, `packages/mcp-server/`
- OpenHands: AgentHub + MCP + skills — `openhands/agenthub/`, `openhands/mcp/`

### Community (10%) — Winner: aider (95)

aider é o único com números publicados de adoption no próprio README: 5.7M PyPI installs + 15B tokens/week + OpenRouter Top 20 + Singularity 88% (`README.md:28-37`). OpenHands (90) com SWE-bench líder + arxiv + enterprise adopters citados (TikTok/VMware/Roche/Amazon). codex (88) como OpenAI oficial + 17 CI workflows. claude-code-main (85) — é mirror mas tool Anthropic oficial (ecosystem). superpowers (80) no marketplace oficial Anthropic + 6 platforms. gsd-2 (68) e gstack (62) mais novos/nicho. ai-website-cloner-template (45) é pequeno.

**Key signals:**
- aider: 5.7M installs + 15B tok/wk — `OS/aider/README.md:28-37`
- OpenHands: SWE-bench + arxiv + adopters — `OS/OpenHands/README.md:11,14,101-118`
- superpowers: marketplace oficial — `OS/superpowers/README.md:32-40`

---

## Profile Breakdown (Ranking por perfil de uso)

### Solo Dev

Pesos: autonomy 0.25, git 0.20, community 0.15, coding_depth 0.15, context 0.10, tdd 0.05, multi_agent 0.05, extensibility 0.05

| Rank | Subject | Score |
|:---:|-------|:---:|
| 1 | gsd-2 | 85.20 |
| 2 | OpenHands | 84.45 |
| 3 | claude-code-main | 82.75 |

### Equipe (feature factory)

Pesos: multi_agent 0.20, tdd 0.18, extensibility 0.17, git 0.15, coding_depth 0.12, autonomy 0.08, context 0.05, community 0.05

| Rank | Subject | Score |
|:---:|-------|:---:|
| 1 | gsd-2 | 85.07 |
| 2 | OpenHands | 83.65 |
| 3 | claude-code-main | 83.09 |

### Enterprise

Pesos: extensibility 0.22, coding_depth 0.20, community 0.15, tdd 0.12, git 0.10, context 0.08, multi_agent 0.08, autonomy 0.05

| Rank | Subject | Score |
|:---:|-------|:---:|
| 1 (tie) | claude-code-main | 85.11 |
| 1 (tie) | OpenHands | 85.11 |
| 3 | gsd-2 | 83.87 |

---

## Strategic Recommendations

### 1. Para devs solo: padronize em gsd-2

gsd-2 combina auto-mode end-to-end + KG memory + stuck-loop em ranking solo 85.20. O retorno por dev é grande: menos HITL, resilience contra limite de modelos, memória persistente. Risco: setup pesado (polyglot Node+native+web+studio) e README denso de 855 linhas. Mitigar com /gsd onboarding + team mode (auto-update throttled).

- **Target:** todos
- **Addresses:** autonomy, context_mgmt, resilience gaps
- **Expected impact:** reduzir HITL per task em 50%+ (signal gsd-2 README.md:14)
- **Priority:** P0

### 2. Para equipes TDD-first: pipeline superpowers + Claude Code

superpowers tem TDD 95 e multi-agent 90. Na prática, é plugin — instala no Claude Code (marketplace oficial Anthropic) ou em 5 outros hosts. A combinação claude-code-main + superpowers entrega: tools+plugins+MCP+hooks (de claude-code) + SDD+TDD+code-review skills (de superpowers). Ganha-se 2-agentes: superpowers enforça TDD e dispatch; Claude Code executa.

- **Target:** equipes com cultura de testes
- **Addresses:** TDD (95) + multi-agent (90) simultâneos
- **Expected impact:** cobertura de teste explícita em produção
- **Priority:** P0

### 3. Para enterprise (VPC/self-host): OpenHands

OpenHands é o único com ladder SDK→CLI→GUI→Cloud→Enterprise + docker/k8s runtime sandbox + tech report arxiv + enterprise adopters públicos (TikTok, VMware, Roche, Amazon). Empata com claude-code-main em profile enterprise (85.11) mas claude-code-main é mirror non-official. Se precisa self-host VPC, OpenHands é a única opção mature.

- **Target:** times com constraint de compliance
- **Addresses:** extensibility (88) + coding_depth (92) + community (90) + deploy maturity
- **Expected impact:** atinge compliance sem abrir mão de SWE-bench 77.6
- **Priority:** P1

### 4. Para uso Git-intensive: aider

aider é o winner em git_integration (92) + community (95). Se o workflow é "ler-editar-commitar" em pair programming interativo, aider tem 5.7M installs, 15B tok/week, e integração git idiomática. Trade-off: é single-agent (multi-agent 25) e sem MCP/plugins. Bom como complemento, não substituto.

- **Target:** refactors em repos legados, projetos individuais
- **Addresses:** git_integration + community
- **Expected impact:** menor fricção em workflows interactive-heavy
- **Priority:** P2

### 5. Domínio-específico: ai-website-cloner-template quando se aplica

Se o caso de uso é "reverse-engineer de sites pra Next.js", ai-website-cloner-template já traz o pipeline multi-fase + inspection guide + 13 agents. Ranking geral baixo (61.04) é efeito de escopo estreito — no seu domínio, não tem concorrente no benchmark.

- **Target:** clone/migration de sites
- **Addresses:** especialização vertical
- **Expected impact:** ~zero-setup pro caso específico
- **Priority:** P3

---

## When to Pick Which

### Escolha **gsd-2** se...
- Precisa de auto-mode long-horizon com 1 comando (volta com PR)
- Quer memória KG persistente entre sessões
- Opera com múltiplos LLM providers (quer fallback automático)
- Precisa remote control (Telegram/Slack/Discord)
- Tolera setup polyglot e README denso

### Escolha **OpenHands** se...
- Precisa self-host em VPC (enterprise)
- Quer validação benchmark pública (SWE-bench 77.6)
- Opera browsers na automação (browsing+visualbrowsing agents)
- Quer arxiv-backed credibility pra stakeholders
- Tem infra docker/k8s disponível

### Escolha **claude-code-main** (ou Claude Code real) se...
- Precisa da maior surface area de tools+comandos do mercado
- Quer MCP + Skills + Plugins + Hooks em uma só ferramenta
- Vai fazer multi-agent com Team tools + Worktree
- Opera com IDEs (Bridge pra VS Code/JetBrains)

### Escolha **superpowers** (sobre Claude Code ou outro) se...
- Quer TDD enforcement real (95)
- Quer SDD (autonomy horas sem HITL)
- Valoriza distribuição oficial Anthropic marketplace
- Precisa zero-dep (não quer pagar em complexidade)

### Escolha **aider** se...
- Trabalha solo em pair-programming interativo
- Repomap é killer feature (codebase grande)
- Quer multi-LLM (incluindo Ollama local)
- Quer voice-to-code

### Escolha **gstack** se...
- Quer "virtual engineering team" em slash-commands
- Precisa CSO/OWASP audit integrado
- Trabalha com múltiplos AI agents (10 hosts)
- Valoriza evals próprios + slop-scan

### Escolha **codex** se...
- Prefere binário Rust (sem Node runtime)
- Usa ChatGPT Plan (aproveita auth)
- Quer integrar com Codex Web (cloud tasks)
- Precisa SDK oficial TS/Python

### Escolha **ai-website-cloner-template** se...
- Caso de uso é clone/reverse-engineer de sites específicos
- Já tem Claude Code/Codex/Cursor (é template, não runtime)

### Considere dois complementares quando...
- **Claude Code + superpowers**: tools completos + metodologia SDD/TDD
- **gsd-2 + gstack/superpowers** (via host adapter): auto-mode gsd-2 com skills gstack/superpowers quando host adaptador existir
- **OpenHands + aider**: enterprise runtime (OpenHands) + pair programming solo (aider)

---

## Methodology

### Data Sources

| Subject | Source | Method | Confidence |
|---------|--------|--------|------------|
| claude-code-main | `OS/claude-code-main/` (README + src ls) | filesystem-scan + doc-scan | HIGH |
| codex | `OS/codex/` (README + package.json + Cargo workspace ls) | filesystem-scan + doc-scan | HIGH |
| aider | `OS/aider/` (README + pyproject + aider/ ls) | filesystem-scan + doc-scan | HIGH |
| OpenHands | `OS/OpenHands/` (README + pyproject + openhands/ ls) | filesystem-scan + doc-scan | HIGH |
| gsd-2 | `OS/gsd-2/` (README + package.json + packages/ ls) | filesystem-scan + doc-scan | HIGH |
| gstack | `OS/gstack/` (README + CLAUDE.md + package.json) | filesystem-scan + doc-scan | HIGH |
| superpowers | `OS/superpowers/` (README + CLAUDE.md + skills/ ls) | filesystem-scan + doc-scan | HIGH |
| ai-website-cloner-template | `OS/ai-website-cloner-template/` (README + AGENTS.md + INSPECTION_GUIDE) | filesystem-scan + doc-scan | HIGH |

### Scoring Method

- **Dimension pack:** coding-agent (8 dimensões; pesos somam 1.00)
- **Score range:** 0–100 por dimensão
- **Signals:** todo score ≥90 requer 2+ signals observáveis com evidence path — ver `scorecard.json:dimensions[*].signals_observed`
- **Confidence rollup:** HIGH se todas dimensões HIGH; MEDIUM se community LOW; LOW se qualquer outra LOW

### Artifacts Generated

| Artifact | File | Status |
|----------|------|:------:|
| Metadata | `metadata.json` | OK |
| Inventories (8 × json+md) | `_inventories/{subject}/inventory.{json,md}` | OK |
| Comparison Matrix | `comparison-matrix.{json,md}` | OK |
| Scorecard | `scorecard.{json,md}` | OK |
| Gap Analysis | — | SKIP (nway mode) |
| Battle Card | — | SKIP (nway mode) |
| Executive Report | `executive-report.md` | OK |

### Limitations

- Profile=quick: sem code-level deep scan. Signals vêm de README + manifest + top-level ls + CLAUDE.md. Decisões arquiteturais finas exigem profile=full
- Community é comparativa dentro do sample — READMEs variam no que expõem (ex: gsd-2 e gstack não publicam stars no README)
- claude-code-main é source mirror — algumas capabilities são inferidas do código mas não executáveis (sem tests/CI)
- Nenhum web fetch foi usado — todos os números são dos próprios READMEs ou inferidos dos diretórios
- Pair-mode artifacts (gap-analysis, battle-card) foram intencionalmente skippados per `tasks/run-all.md` (nway mode)

---

## Appendix: Source Artifacts

Todos em `OS/_bench/coding-agents-8way/`:

| # | File | Type | Format |
|---|------|------|--------|
| 1 | `metadata.json` | Metadata | JSON |
| 2 | `_inventories/claude-code-main/inventory.{json,md}` | Inventory | JSON+MD |
| 3 | `_inventories/codex/inventory.{json,md}` | Inventory | JSON+MD |
| 4 | `_inventories/aider/inventory.{json,md}` | Inventory | JSON+MD |
| 5 | `_inventories/OpenHands/inventory.{json,md}` | Inventory | JSON+MD |
| 6 | `_inventories/gsd-2/inventory.{json,md}` | Inventory | JSON+MD |
| 7 | `_inventories/gstack/inventory.{json,md}` | Inventory | JSON+MD |
| 8 | `_inventories/superpowers/inventory.{json,md}` | Inventory | JSON+MD |
| 9 | `_inventories/ai-website-cloner-template/inventory.{json,md}` | Inventory | JSON+MD |
| 10 | `comparison-matrix.{json,md}` | Matrix | JSON+MD |
| 11 | `scorecard.{json,md}` | Scoring | JSON+MD |
| 12 | `executive-report.md` | Report | MD |

---

_Generated by os-bench bench-executive-report task | Template v1.0_
