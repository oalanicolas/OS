# Scorecard: coding-agents-8way

**Date:** 2026-04-19
**Dimension pack:** coding-agent (8 dimensões, soma = 1.00)
**Slug:** coding-agents-8way
**Overall Confidence:** HIGH

---

## Scoring Method

- Score range: 0–100 por dimensão
- Pesos do pack `coding-agent` (soma = 1.00): coding_depth 0.18, autonomy 0.15, context_mgmt 0.13, git_integration 0.10, tdd 0.10, multi_agent 0.12, extensibility 0.12, community 0.10
- Cada score deriva de signals observáveis documentados em `scorecard.json:signals_observed`
- Signal ausente → score rebaixado e confidence down
- Fonte: filesystem-scan de `OS/{subject}/` (README + manifest + top-level)

---

## Dimension Scores

| Dimension | Weight | claude-code-main | codex | aider | OpenHands | gsd-2 | gstack | superpowers | ai-website-cloner-template | Winner |
|-----------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Coding Depth | 18% | 88 | 82 | 85 | **92** | 84 | 70 | 72 | 55 | OpenHands |
| Autonomy | 15% | 72 | 70 | 55 | 85 | **93** | 70 | 88 | 75 | gsd-2 |
| Context Mgmt | 13% | 90 | 55 | 80 | 75 | **94** | 50 | 50 | 45 | gsd-2 |
| Git Integration | 10% | 88 | 65 | **92** | 80 | 85 | 82 | 78 | 70 | aider |
| TDD | 10% | 55 | 50 | 82 | 70 | 80 | 78 | **95** | 55 | superpowers |
| Multi-agent | 12% | **93** | 60 | 25 | 90 | 85 | 78 | 90 | 80 | claude-code-main |
| Extensibility | 12% | **96** | 75 | 60 | 88 | 90 | 85 | 80 | 62 | claude-code-main |
| Community | 10% | 85 | 88 | **95** | 90 | 68 | 62 | 80 | 45 | aider |

---

## Weighted Total & Ranking

| Rank | Subject | Weighted Total |
|:---:|-------|:---:|
| 1 | **gsd-2** | **85.59** |
| 2 | OpenHands | 84.42 |
| 3 | claude-code-main | 83.82 |
| 4 | superpowers | 78.36 |
| 5 | gstack | 71.36 |
| 6 | aider | 71.05 |
| 7 | codex | 68.91 |
| 8 | ai-website-cloner-template | 61.04 |

### Visual ASCII ranking

```
gsd-2                          ████████████████████████████████████████████  85.59
OpenHands                      ███████████████████████████████████████████   84.42
claude-code-main               ███████████████████████████████████████████   83.82
superpowers                    ████████████████████████████████████████      78.36
gstack                         █████████████████████████████████████         71.36
aider                          █████████████████████████████████████         71.05
codex                          ██████████████████████████████████            68.91
ai-website-cloner-template     ████████████████████████████████              61.04
                               0         20        40        60        80     100
```

---

## Dimension Analysis

### Coding Depth (18%)

Vencedor: **OpenHands (92)**. Publica SWE-bench 77.6 (`OS/OpenHands/README.md:11`) e tem 6 agents especializados em `openhands/agenthub/` (codeact, loc, browsing, visualbrowsing, readonly, dummy). claude-code-main vem perto (88) com 43 tools + 101 comandos + LSP, mas sem benchmark publicado no mirror. aider (85) compensa com 38 coders (`aider/coders/`) e 100+ linguagens via tree-sitter. gsd-2 (84) com pi-coding-agent + UOK. codex (82) com apply-patch + code-mode robustos mas sem benchmark in-repo. No fundo: gstack (70) e superpowers (72) dependem do host; ai-website-cloner-template (55) é template focado, não runtime genérico.

### Autonomy (15%)

Vencedor: **gsd-2 (93)**. 3 signals explícitos: auto-mode end-to-end (`README.md:14-23`), stuck-loop detection (#4414) e model fallback (#4373). superpowers (88) tem SDD que roda horas sem HITL (`skills/subagent-driven-development/`). OpenHands (85) via controller event-loop. claude-code-main (72) tem Plan mode mas bounded. aider (55) é single-turn focado — limitação explícita de design. codex (70) via cloud-tasks async.

### Context Mgmt (13%)

Vencedor: **gsd-2 (94)**. KG memory 5-phase + hybrid retrieval (keyword+semantic) + lifecycle explícito (`README.md:32-38`). claude-code-main (90) tem `/compact` + memdir + team-mem-sync (`src/memdir/`). aider (80) repomap é single-feature forte. OpenHands (75) tem memory/ module. codex (55) sem evidência explícita. gstack/superpowers (50) dependem do host.

### Git Integration (10%)

Vencedor: **aider (92)**. Auto-commit idiomático (`aider/repo.py`) + diff+undo + README.md:63-68 explicita que git é feature-chave. claude-code-main (88) com /commit + Enter/Exit WorktreeTool + Bash. gsd-2 (85) com branch isolation per milestone. gstack (82) com /ship + /land-and-deploy + CHANGELOG discipline. OpenHands (80) com resolver issue→PR. superpowers (78) com 2 skills git-especializadas. ai-website-cloner-template (70) com parallel worktree dispatch. codex (65) via SDK apenas.

### TDD (10%)

Vencedor: **superpowers (95)**. Skill dedicada (`skills/test-driven-development/`) + verification-before-completion + stance explícito "true red/green TDD, YAGNI, DRY" no README. aider (82) com auto-lint+auto-test após edit. gsd-2 (80) com verification gate. gstack (78) com own evals (LLM-judge + E2E 2-tier). OpenHands (70) com runtime testing genérico. claude-code-main (55) tem ferramentas mas sem skill TDD explícita. codex (50) e ai-website-cloner-template (55) fracos aqui.

### Multi-agent (12%)

Vencedor: **claude-code-main (93)**. 3 signals: AgentTool + coordinator + TeamCreateTool/Worktree. OpenHands (90) com AgentHub 6 + microagents. superpowers (90) com SDD + dispatching-parallel-agents. gsd-2 (85) com UOK reactive/parallel. ai-website-cloner-template (80) com orchestrator→builders padrão. gstack (78) com 23 role-skills. codex (60) só async. aider (25) é explicitamente single-agent.

### Extensibility (12%)

Vencedor: **claude-code-main (96)**. 4 eixos: Plugin + Skill + MCP + Hooks. gsd-2 (90) com workflow plugins + Extension API + own MCP server. OpenHands (88) com AgentHub + MCP (fastmcp) + skills + microagents. gstack (85) com 23 skills + multi-host (10 agents) + ACP/ClawHub. superpowers (80) com 14 skills + 6 platforms distribution + hooks. codex (75) com MCP server + SDK + hooks crate. ai-website-cloner-template (62) com skill + sync-agent-rules mas escopo domínio-único. aider (60) tem só coders pluggable.

### Community (10%)

Vencedor: **aider (95)**. 3 signals concretos: 5.7M PyPI installs + 15B tokens/week + OpenRouter Top 20 (README.md:28-37). OpenHands (90) com SWE-bench líder + arxiv paper + enterprise adopters citados. codex (88) como OpenAI oficial + 17 CI workflows + npm/Homebrew. claude-code-main (85) — é mirror mas é a tool Anthropic oficial. superpowers (80) distribuído no marketplace oficial Anthropic + 6 platforms. gsd-2 (68) e gstack (62) são projetos mais novos/nicho sem stars/installs publicados no README. ai-website-cloner-template (45) é pequeno (Discord + stars shield).

---

## Score Distribution by Subject

### claude-code-main
- Strongest: **Extensibility** (96) — Plugin+Skill+MCP+Hooks
- Weakest: **TDD** (55) — sem skill TDD explícita no repo
- Unweighted avg: 80.88
- Range: 55–96

### codex
- Strongest: **Community** (88) — OpenAI oficial + ecosystem
- Weakest: **TDD** (50)
- Unweighted avg: 68.12
- Range: 50–88

### aider
- Strongest: **Community** (95) — 5.7M installs
- Weakest: **Multi-agent** (25) — single-agent explícito
- Unweighted avg: 71.75
- Range: 25–95

### OpenHands
- Strongest: **Coding Depth** (92) — SWE-bench 77.6
- Weakest: **Git Integration** (80) — ainda alto
- Unweighted avg: 83.75
- Range: 70–92 (distribuição mais consistente)

### gsd-2
- Strongest: **Context Mgmt** (94) — KG memory
- Weakest: **Community** (68) — projeto novo
- Unweighted avg: 84.87 (maior média)
- Range: 68–94

### gstack
- Strongest: **Extensibility** (85) — 23 skills + multi-host
- Weakest: **Context Mgmt** (50) — depende do host
- Unweighted avg: 71.88
- Range: 50–85

### superpowers
- Strongest: **TDD** (95) — skill dedicada
- Weakest: **Context Mgmt** (50) — depende do host
- Unweighted avg: 76.62
- Range: 50–95

### ai-website-cloner-template
- Strongest: **Multi-agent** (80) — orchestrator→builders
- Weakest: **Community** (45) — pequeno
- Unweighted avg: 61.0
- Range: 45–80

### Competitive dimensions (|spread| < 20 entre top-3)

- **Coding Depth**: OpenHands(92) / claude-code-main(88) / aider(85) — 7 pontos
- **Git Integration**: aider(92) / claude-code-main(88) / gsd-2(85) — 7 pontos
- **Multi-agent**: claude-code-main(93) / OpenHands(90) / superpowers(90) — 3 pontos

---

## Profile Breakdown

Ranking muda conforme o perfil de uso. Abaixo 3 perfis com pesos reajustados.

### Solo Dev (autonomy + git + community first)

Pesos: autonomy 0.25, git 0.20, community 0.15, coding_depth 0.15, context 0.10, tdd 0.05, multi_agent 0.05, extensibility 0.05

| Rank | Subject | Score |
|:---:|-------|:---:|
| 1 | **gsd-2** | 85.20 |
| 2 | OpenHands | 84.45 |
| 3 | claude-code-main | 82.75 |
| 4 | superpowers | 78.65 |
| 5 | aider | 75.50 |

Solo dev ganha com gsd-2 auto-mode + stuck-loop (roda, sai, volta); OpenHands fica 2º pela maturidade de deploy; aider sobe pra 5º pela community forte.

### Equipe (multi-agent + TDD + extensibility first)

Pesos: multi_agent 0.20, tdd 0.18, extensibility 0.17, git 0.15, coding_depth 0.12, autonomy 0.08, context 0.05, community 0.05

| Rank | Subject | Score |
|:---:|-------|:---:|
| 1 | **gsd-2** | 85.07 |
| 2 | OpenHands | 83.65 |
| 3 | claude-code-main | 83.09 |
| 4 | superpowers | 82.58 |
| 5 | gstack | 75.99 |

Em equipe, superpowers sobe pro top-4 pelo TDD 95. gsd-2 continua no topo (UOK + 8 LLM providers + TDD 80). aider cai pra 6º por ser single-agent.

### Enterprise (extensibility + coding_depth + community first)

Pesos: extensibility 0.22, coding_depth 0.20, community 0.15, tdd 0.12, git 0.10, context 0.08, multi_agent 0.08, autonomy 0.05

| Rank | Subject | Score |
|:---:|-------|:---:|
| 1 | **claude-code-main** | 85.11 |
| 1 | **OpenHands** | 85.11 |
| 3 | gsd-2 | 83.87 |
| 4 | superpowers | 78.80 |
| 5 | aider | 74.64 |

Empate técnico no topo: claude-code-main (4-axis extensibility + 43 tools) e OpenHands (enterprise VPC + SWE-bench + arxiv + adopters enterprise). gsd-2 fica 3º. superpowers 4º.

---

## Confidence Disclosure

| Subject | Confidence | Reason |
|---------|-----------|--------|
| claude-code-main | HIGH | Mirror com src/ completo; 3+ signals por dimensão |
| codex | HIGH | Cargo workspace visível, mas sem runtime evidences pra autonomy/TDD |
| aider | HIGH | README detalhado + 80 arquivos .py claros |
| OpenHands | HIGH | README + pyproject + 484 py + 19 CI workflows + arxiv |
| gsd-2 | HIGH | README 855 linhas detalhadas + 1735 arquivos |
| gstack | HIGH | README 415 linhas + CLAUDE.md denso + 23 skills visíveis |
| superpowers | HIGH | 14 skills nomeadas + README + CLAUDE.md |
| ai-website-cloner-template | HIGH | README + AGENTS.md + INSPECTION_GUIDE completos |

### Sources

Filesystem scan + doc scan. Nenhum web fetch usado nesta run (profile=quick).

### Dimension Pack

| Pack | Version | Designed For |
|------|---------|-------------|
| coding-agent | 1.0 | Coding agents / CLI coding assistants |

### Scoring Transparency

Todo score ≥90 (OpenHands coding_depth, gsd-2 autonomy, gsd-2 context_mgmt, claude-code-main multi_agent, claude-code-main extensibility, superpowers tdd, aider git_integration, aider community, ai-website-cloner-template não atinge 90) tem 2+ signals com evidence path. Signals listados em `scorecard.json:dimensions[*].signals_observed`.

### Known Limitations

- Community dim é comparativa dentro do sample (READMEs variam no que expõem) — confidence MEDIUM nessa dim
- claude-code-main é mirror sem testes/CI — algumas capabilities inferidas do source, não executadas
- Profile=quick: sem code-level scan; signals vêm de README/manifest/ls top-level
- Scorecard não bebeu signals de web (PyPI downloads, GitHub stars não verificados em run time — usamos os números citados nos próprios READMEs)

---

_Generated by os-bench bench-score task | Template v1.0_
