# Comparison Matrix: coding-agents-8way

**Date:** 2026-04-19
**Comparison type:** nway (8 subjects)
**Dimension pack:** coding-agent
**Slug:** coding-agents-8way

---

## Sources

| Subject | Path | Web source | Confidence |
|---------|------|------------|------------|
| claude-code-main | `OS/claude-code-main/` | mirror (.map leak) | HIGH |
| codex | `OS/codex/` | github.com/openai/codex | HIGH |
| aider | `OS/aider/` | github.com/Aider-AI/aider | HIGH |
| OpenHands | `OS/OpenHands/` | github.com/OpenHands/OpenHands | HIGH |
| gsd-2 | `OS/gsd-2/` | github.com/gsd-build/GSD-2 | HIGH |
| gstack | `OS/gstack/` | github.com/garrytan/gstack | HIGH |
| superpowers | `OS/superpowers/` | github.com/obra/superpowers | HIGH |
| ai-website-cloner-template | `OS/ai-website-cloner-template/` | github.com/JCodesMore/ai-website-cloner-template | HIGH |

## Method

Profile = quick. Leu README, manifest (package.json / pyproject.toml / Cargo.toml) e ls de top-level pra cada um dos 8 subjects. Usou o pack `coding-agent` como grid de categorias (8 dimensões). Para nway, classificação Forte/Parcial/Sem_Equiv não se aplica cell-a-cell — ao invés, cada feature lista "leaders" (subjects com capability observada + evidence path).

---

## Inventory Summary

| Metric | claude-code-main | codex | aider | OpenHands | gsd-2 | gstack | superpowers | ai-website-cloner-template |
|--------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| LOC (ballpark) | ~512k | ~400k | ~60k | ~200k | ~250k | ~40k | ~20k | ~3k |
| Files (src) | 1884 | 1493 | 80 | 484 | 1735 | 250 | 45 | 4 |
| Primary lang | TS/TSX | Rust | Python | Python | TS | TS | Markdown | TS |
| License | (mirror) | Apache-2.0 | Apache-2.0 | MIT (+SA ent) | MIT | MIT | see LICENSE | MIT |
| Last commit | n/a (not-git) | 2026-04-08 | 2026-04-19 | 2026-04-19 | 2026-04-19 | 2026-04-19 | 2026-04-16 | 2026-03-30 |
| CI workflows | 0 (mirror) | 17 | 9 | 19 | 11 | 5 | 0 | 0 |
| README lines | 280 | 60 | 180 | 153 | 855 | 415 | 198 | 155 |

---

## Feature Matrix

### Category: Coding Depth

| Feature | claude-code-main | codex | aider | OpenHands | gsd-2 | gstack | superpowers | ai-website-cloner-template | Leaders |
|---|---|---|---|---|---|---|---|---|---|
| Multi-file edits / refactor | yes (FileEdit/Write + Agent) | yes (apply-patch + code-mode) | yes (38 coders) | yes (codeact + loc_agent) | yes (pi-coding-agent + UOK) | via host | via host (SDD) | via host (parallel worktree) | claude-code-main, aider, codex, OpenHands |
| Benchmark published | no (mirror) | no in-repo | 5.7M PyPI, 15B tok/wk, Singularity 88% | SWE-bench 77.6 (badge) | internal evals | own evals LLM-judge+E2E | no | no | OpenHands, aider |
| Language coverage | generic (Bash+LSP) | generic (agnóstico) | 100+ (tree-sitter) | generic + Python-first | generic | generic | generic | TS/React-only | aider |

### Category: Autonomy

| Feature | claude-code-main | codex | aider | OpenHands | gsd-2 | gstack | superpowers | ai-website-cloner-template | Leaders |
|---|---|---|---|---|---|---|---|---|---|
| Long-horizon auto-mode | Plan mode + Agent bounded | SDK + cloud-tasks | single-turn focused | controller event-loop | **auto-mode end-to-end** | autoplan → /ship | **SDD horas** | multi-phase pipeline | gsd-2, superpowers, OpenHands |
| Stuck-loop / self-correction | — | — | linter+tests re-run | event retry | **stuck-loop detection #4414 + model fallback #4373** | /investigate skill | systematic-debugging skill | visual diff QA | gsd-2 |

### Category: Context Mgmt

| Feature | claude-code-main | codex | aider | OpenHands | gsd-2 | gstack | superpowers | ai-website-cloner-template | Leaders |
|---|---|---|---|---|---|---|---|---|---|
| Context compression | **/compact + services/compact** | implícito | **repomap** | controller+memory | context save/restore + /scan | via host | via host | via host | claude-code-main, aider, gsd-2 |
| Persistent memory | **memdir + team-mem-sync** | none | session-only | `memory/` module | **KG memory (5 phases)** | via host | via host | docs/research artifacts | gsd-2, claude-code-main |

### Category: Git Integration

| Feature | claude-code-main | codex | aider | OpenHands | gsd-2 | gstack | superpowers | ai-website-cloner-template | Leaders |
|---|---|---|---|---|---|---|---|---|---|
| Auto-commit | /commit | via SDK | **auto com messages** | via resolver | per milestone | /ship + /land-and-deploy | finishing-branch skill | via host | aider, claude-code-main, gstack |
| Worktree support | **Enter/Exit WorktreeTool** | — | no | — | worktree routing | via host | **using-git-worktrees skill** | **parallel worktree dispatch** | claude-code-main, superpowers, ai-website-cloner-template |
| PR creation | /pr_comments + Bash | via SDK | no explícito | **resolver issue→PR** | auto-mode fecha PR | **/ship + /land-and-deploy** | requesting-code-review | via host | OpenHands, gstack |

### Category: TDD

| Feature | claude-code-main | codex | aider | OpenHands | gsd-2 | gstack | superpowers | ai-website-cloner-template | Leaders |
|---|---|---|---|---|---|---|---|---|---|
| TDD red-green enforcement | tools disponíveis, sem skill | — | **auto-lint+auto-test after edit** | runtime tooling | verification gate | own eval infrastructure | **TDD skill (red/green)** | QA visual diff | superpowers, aider |
| Verification before completion | hooks/toolPermission | — | re-run tests | event verify | **verification gate mandatory** | **/qa + /canary + /cso** | **verification-before-completion skill** | visual diff phase | superpowers, gstack, gsd-2 |

### Category: Multi-agent

| Feature | claude-code-main | codex | aider | OpenHands | gsd-2 | gstack | superpowers | ai-website-cloner-template | Leaders |
|---|---|---|---|---|---|---|---|---|---|
| Sub-agent orchestration | **AgentTool + coordinator + Team** | via SDK async | single-agent | **AgentHub 6 + microagents** | **UOK reactive/parallel** | /autoplan dispatches | **SDD + dispatch-parallel skills** | orchestrator → builder agents | claude-code-main, OpenHands, superpowers |
| Parallel execution | **TeamCreate + worktree** | Rust async | no | async sandbox | **UOK parallel scheduling** | via host worktrees | **dispatching-parallel-agents** | **parallel builders per section** | claude-code-main, gsd-2, superpowers, ai-website-cloner-template |

### Category: Extensibility

| Feature | claude-code-main | codex | aider | OpenHands | gsd-2 | gstack | superpowers | ai-website-cloner-template | Leaders |
|---|---|---|---|---|---|---|---|---|---|
| Plugin / skill system | **Skill + Plugin systems** | SDK-based | coders pluggable (38) | AgentHub + microagents + skills | **workflow plugins + Extension API** | **23+ skills + gen-skill-docs** | 14 skills + hooks + agents | /clone-website skill + sync | claude-code-main, gstack, gsd-2 |
| MCP support | **MCP client + OAuth** | **MCP server crate** | — | **fastmcp client+server** | **own mcp-server package** | — | — (zero-dep) | Chrome MCP client (host-provided) | claude-code-main, OpenHands, gsd-2, codex |
| Hooks / lifecycle | **hooks/ (permission+lifecycle)** | **codex-hooks crate** | — | events bus | pre-commit + DB-write hooks | — | session-start hooks | — | claude-code-main, codex |

### Category: Community

| Feature | claude-code-main | codex | aider | OpenHands | gsd-2 | gstack | superpowers | ai-website-cloner-template | Leaders |
|---|---|---|---|---|---|---|---|---|---|
| Community signals | mirror de tool Anthropic oficial (ecosystem) | OpenAI official | **5.7M PyPI, 15B tok/wk, OpenRouter Top 20** | SWE-bench leader + arxiv paper + Slack | npm + Discord | MIT free + YC voice | Anthropic marketplace + 6 platforms | small; Discord + GitHub | aider, claude-code-main, codex, OpenHands, superpowers |

---

## Equivalence Summary (N-way)

Em n-way não se aplica Forte/Parcial/Sem_Equiv cell-a-cell. Abaixo, o "leader count" por subject — quantas vezes aparece como líder em alguma feature (16 features totais):

| Subject | Leader mentions | % das features |
|---------|:---:|:---:|
| claude-code-main | 7 | 44% |
| aider | 7 | 44% |
| OpenHands | 6 | 38% |
| gsd-2 | 8 | 50% |
| superpowers | 6 | 38% |
| gstack | 3 | 19% |
| codex | 3 | 19% |
| ai-website-cloner-template | 2 | 13% |

---

## Subject-Only Capabilities

### claude-code-main-Only
- Team tools (create/delete teams de agents) — `src/tools/TeamCreateTool`
- IDE Bridge bidirecional (VS Code, JetBrains) — `src/bridge/`
- Memdir team-mem-sync — `src/memdir/teamMemPaths.ts`
- 101 slash commands + 43 tools (maior surface area) — `src/commands/`, `src/tools/`

### codex-Only
- Rust-native runtime (único) — `codex-rs/Cargo.toml`
- ChatGPT Plan auth (Plus/Pro/Team/Edu/Enterprise) — `codex-rs/chatgpt/`
- Cloud tasks bridge (integra Codex Web) — `codex-rs/cloud-tasks/`
- Bazel + Nix build reprodutível — `BUILD.bazel`, `flake.nix`
- TS + Python SDK oficial — `sdk/`

### aider-Only
- Repomap (mapeamento codebase completo) — `aider/repomap.py`
- 100+ linguagens via tree-sitter — `aider/queries/`
- Voice-to-code — `aider/voice.py`
- Copy/paste web-chat mode — `aider/copypaste.py`
- 5.7M PyPI installs documentados — `README.md:30`

### OpenHands-Only
- SWE-bench 77.6 badge publicado — `README.md:11`
- Browsing + visualbrowsing agents (Playwright) — `openhands/agenthub/browsing_agent/`, `visualbrowsing_agent/`
- Docker + K8s runtime sandbox — `openhands/runtime/`, `kind/`
- Enterprise source-available + VPC — `enterprise/`
- Tech report arxiv — `README.md:14`
- Integrations Slack/Jira/Linear — `openhands/integrations/`

### gsd-2-Only
- Auto-mode end-to-end (1 comando, volta com PR) — `README.md:14-23`
- KG memory 5-fase + hybrid retrieval — `README.md:32-38`
- Stuck-loop detection + model fallback — `README.md:66-69`
- Remote control Telegram/Slack/Discord — `README.md:51`
- Self-healing .gsd + stale OAuth recovery — `README.md:70-71`
- UOK (Unified Orchestration Kernel) — `gsd-orchestrator/`
- 8+ provedores de LLM nativos — `package.json deps`

### gstack-Only
- CSO (OWASP Top 10 + STRIDE) skill — `cso/`
- Multi-host config (10 AI agents) — `hosts/`, `README.md:113-119`
- Own Playwright browser CLI — `browse/src/commands.ts`
- Evals 2-tier diff-based (gate+periodic) — `test/`
- Slop-scan integration — `slop-scan.config.json`
- Team mode auto-update — `README.md:53-64`
- ACP/OpenClaw + ClawHub marketplace — `openclaw/`

### superpowers-Only
- Distribuição no Claude marketplace oficial Anthropic — `README.md:32-40`
- 94% PR rejection rate (curadoria) — `CLAUDE.md`
- Zero-dependency design — `CLAUDE.md`
- session-start hooks auto-inject — `hooks/hooks.json`

### ai-website-cloner-template-Only
- Escopo domínio-específico (clone de sites) — `README.md`
- 5-phase inspection guide (visual → component → layout → stack → docs) — `docs/research/INSPECTION_GUIDE.md`
- Stack Next.js 16 + React 19 + Tailwind v4 pronto — `package.json`

---

## Partial Equivalences (Notable Deltas)

**MCP support**: claude-code-main e OpenHands têm client completo; codex e gsd-2 focam em server. Aider, gstack e superpowers não têm. ai-website-cloner-template usa Chrome MCP via host.

**Multi-agent**: claude-code-main, OpenHands e superpowers têm modelos robustos (coordinator/AgentHub/SDD); gsd-2 tem UOK parallel; aider é single-agent puro.

**Persistent memory**: gsd-2 (KG 5-fase) e claude-code-main (memdir + team sync) lideram; OpenHands tem módulo memory genérico; aider é session-only.

**Auto-mode long-horizon**: gsd-2 é explicitamente end-to-end; superpowers vai horas via SDD; OpenHands via controller event-loop; claude-code-main tem Plan mode (bounded); aider é single-turn.

---

## Objective Reading

### claude-code-main
Mais largo surface area do benchmark: 43 tools + 101 commands + Skills + Plugins + MCP + Hooks + Bridge IDE + memdir + Team tools. Evidência: `src/tools/`, `src/commands/`, `src/plugins/`, `src/skills/`, `src/bridge/`, `src/memdir/`. Limitação: é mirror sem testes/CI.

### codex
Único em Rust nativo — performance + binário distribuível. Integra Codex Web (cloud-tasks), ChatGPT Plan auth e SDK TS+Python oficial. Evidência: `codex-rs/`, `codex-rs/chatgpt/`, `sdk/`. Limitação: README minimalista e extensão via SDK, sem skills/plugins.

### aider
Diferencial é repomap + 100+ linguagens + git auto-commit idiomático. Ecosistema massivo: 5.7M installs PyPI. Evidência: `aider/repomap.py`, `aider/queries/`, `aider/repo.py`. Limitação: single-agent, sem MCP/plugins/skills.

### OpenHands
Deploy ladder completo (SDK → CLI → GUI → Cloud → Enterprise) + SWE-bench 77.6 + docker/k8s sandbox + tech report arxiv. Browser agents nativos. Evidência: `openhands/agenthub/`, `enterprise/`, `README.md:11,14`. Limitação: setup pesado, enterprise source-available pago.

### gsd-2
Auto-mode end-to-end + KG memory + stuck-loop + model fallback + remote control multi-canal + UOK. Maturidade operacional (self-healing, single-writer DB, DB-authoritative milestone). Evidência: `README.md:14-85`, `gsd-orchestrator/`. Limitação: setup polyglot pesado, README denso.

### gstack
Virtual engineering team de 23 specialists (CEO/eng/design/QA/CSO/release). Multi-host (10 agents). CSO+OWASP+STRIDE único. Own browser CLI + evals 2-tier. Evidência: `README.md:51,113-119`, `cso/`, `browse/`. Limitação: skill-oriented, sem MCP nativo.

### superpowers
Metodologia pura em skills — SDD + TDD red/green + systematic-debugging + worktrees. Distribuído no marketplace oficial Anthropic. Zero-dep. Evidência: `skills/subagent-driven-development/`, `skills/test-driven-development/`, `README.md:32-40`. Limitação: precisa de host.

### ai-website-cloner-template
Único escopo domínio-específico. Multi-phase pipeline (recon→foundation→specs→parallel build→assembly) + 5-phase inspection guide + 13 agents. Evidência: `README.md:72-82`, `docs/research/INSPECTION_GUIDE.md`. Limitação: é template, não runtime; sem tests/CI.

### Key Differentiators

- **claude-code-main**: maior surface de tools/commands + Team + Bridge
- **codex**: Rust nativo + ChatGPT auth + Cloud tasks
- **aider**: repomap + 100+ langs + voice + copy/paste web
- **OpenHands**: SWE-bench 77.6 + docker/k8s + enterprise VPC
- **gsd-2**: auto-mode + KG memory + remote control + self-healing
- **gstack**: 23-skill team + multi-host + CSO + slop-scan
- **superpowers**: SDD + TDD real + Anthropic marketplace
- **ai-website-cloner-template**: single-purpose web-clone pipeline

### Areas of Parity

- Multi-file edits (todos cobrem, via mecanismos diferentes)
- Git commit/integration (todos têm — só aider+claude+gstack destacam)
- Parallel execution (claude/gsd-2/superpowers/ai-website-cloner-template convergem via worktrees)

---

## Method Disclosure

- **Comparison date:** 2026-04-19
- **Dimension pack:** coding-agent v1.0 (8 dimensões)
- **Items compared:** 16 features across 8 categories
- **Subjects:** 8
- **Data sources:** filesystem-scan de `OS/{subject}/` (README, package.json/pyproject.toml/Cargo.toml, top-level ls, CLAUDE.md quando presente)

---

_Generated by os-bench bench-matrix task | Template v1.0_
