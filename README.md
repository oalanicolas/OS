# OS — Opensource Benchmarks

Coleção de 28 projetos opensource usados como referência/benchmark para estudo de **AI agents**: frameworks de orquestração, coding agents, sistemas de memória, assistentes pessoais, MCP, workflows, observability e **enterprise agent platforms**.

Não contém código próprio — todos são forks/clones para análise.

## Projetos

| # | Projeto | Tags | Stack | Diferencial |
|---|---------|------|-------|-------------|
| 1 | [BMAD-METHOD](./BMAD-METHOD) | `multi-agent` `agile` `orchestration` | TS | Party Mode: múltiplas personas em uma sessão; 12+ agentes (PM, arquiteto, UX…) |
| 2 | [ai-website-cloner-template](./ai-website-cloner-template) | `website-clone` `coding-agent` `claude-code` | Next.js + shadcn | Clonagem pixel-perfect via builder agents paralelos em `/clone-website` |
| 3 | [claude-code-main](./claude-code-main) | `cli` `coding-agent` `terminal-ui` | TS + Ink + Bun | Snapshot (~512K LOC) do CLI oficial da Anthropic (source leak) |
| 4 | [claude-remote-manager](./claude-remote-manager) | `remote-control` `persistence` `telegram` | Bash + TS | Claude Code 24/7 controlado por Telegram; cron sobrevive restart |
| 5 | [codex](./codex) | `coding-agent` `cli` `openai` | TS + Rust | CLI coding agent oficial da OpenAI com integrações IDE |
| 6 | [crewAI](./crewAI) | `multi-agent` `framework` `python` | Python | Agentes role-playing colaborativos com objetivos compartilhados |
| 7 | [gbrain](./gbrain) | `memory` `rag` `knowledge-graph` | TS + PGLite + pgvector | 95% recall@5; self-wiring entity links sem LLM; setup em 30min |
| 8 | [get-shit-done](./get-shit-done) | `spec-driven` `meta-prompting` `context-engineering` | TS | Resolve "context rot" via spec discipline (usado em Amazon/Google/Shopify) |
| 9 | [gh-aw](./gh-aw) | `github-actions` `agentic-workflows` `governance` | Go + markdown | Workflows em linguagem natural executados safe em GH Actions |
| 10 | [gsd-2](./gsd-2) | `coding-agent` `automation` `memory` | TS (Pi SDK) | Auto-milestones sem humano; RTK comprime shell output |
| 11 | [gstack](./gstack) | `coding-agent` `workflow` `multi-role` | TS + Playwright | Software factory pessoal do pres. da YC; 24 agentes especializados |
| 12 | [hermes-agent](./hermes-agent) | `personal-assistant` `learning-loop` `multi-model` | Python asyncio | Auto-cria skills; roda em VPS de $5 ou serverless com hibernação |
| 13 | [mempalace](./mempalace) | `memory` `rag` `local-first` | Python + Chroma | 96.6% R@5 com storage verbatim (sem paráfrase); zero API keys |
| 14 | [openclaw](./openclaw) | `personal-assistant` `multi-channel` `local-first` | TS + SwiftUI + Kotlin | 20+ canais (WhatsApp, Telegram, iMessage…) rodando on-device |
| 15 | [paperclip](./paperclip) | `multi-agent` `orchestration` `governance` | TS + React + Postgres | Gerencia agentes como empregados: org charts, budgets, goals |
| 16 | [spec-kit](./spec-kit) | `spec-driven` `github` `tooling` | Python + TS | Specs executáveis que geram implementação; metodologia oficial do GitHub |
| 17 | [superpowers](./superpowers) | `coding-agent` `tdd` `subagent-driven` | TS (Claude Code plugin) | TDD red/green puro; subagents paralelos; 94% PR rejection rate |
| 18 | [workflow](./workflow) | `durable-functions` `event-sourcing` `serverless` | TS + Next.js + PG | Replay determinístico via event log; split VM + step runtime |
| 19 | [OpenHands](./OpenHands) | `autonomous-agent` `swe-bench` `coding-agent` | Python | Autonomous agent mais estrelado do GitHub (ex-OpenDevin) |
| 20 | [aider](./aider) | `coding-cli` `pair-programming` `git-native` | Python | Pair programming CLI mais usado no OS; commits automáticos |
| 21 | [autogen](./autogen) | `multi-agent` `conversational` `microsoft` | Python | Framework multi-agente conversacional da Microsoft |
| 22 | [mem0](./mem0) | `memory` `layer` `vector-store` | Python | Memory layer líder; cresceu explosivamente em 2025 |
| 23 | [mcp-servers](./mcp-servers) | `mcp` `protocol` `reference` | TS + Python | Repo oficial do Model Context Protocol; 50+ servers de referência |
| 24 | [langfuse](./langfuse) | `observability` `eval` `tracing` | TS + Next.js | Observability OS mais popular pra aplicações LLM |
| 25 | [Clawith](./Clawith) | `enterprise-platform` `multi-tenant` `digital-employees` | TS | "OpenClaw for Teams": agentes com `soul.md`+`memory.md`+org chart+delegation |
| 26 | [agent-governance-toolkit](./agent-governance-toolkit) | `governance` `runtime-security` `owasp-agentic` | Multi-lang | Microsoft: policy enforcement sub-ms, cobre 10/10 OWASP Agentic Top 10 |
| 27 | [memori-labs](./memori-labs) | `memory` `agent-native` `llm-agnostic` | Python | Memory infrastructure, 81.95% LoCoMo, SQL-backed |
| 28 | [dify](./dify) | `enterprise-platform` `low-code` `visual` | Python + TS | Plataforma low-code mais popular (129k stars), teams + production |

## Categorias

### Por função
- **Coding agents**: `claude-code-main`, `codex`, `aider`, `OpenHands`, `ai-website-cloner-template`, `gsd-2`, `gstack`, `superpowers`
- **Multi-agent orchestration**: `BMAD-METHOD`, `crewAI`, `autogen`, `paperclip`, `claude-remote-manager`, `gh-aw`
- **Personal assistants**: `openclaw`, `hermes-agent`, `gbrain`
- **Memory / knowledge**: `mem0`, `mempalace`, `gbrain`, `gsd-2`, `hermes-agent`
- **Spec-driven / methodology**: `spec-kit`, `get-shit-done`, `superpowers`
- **Workflow infra**: `workflow`, `gh-aw`
- **Protocol / MCP**: `mcp-servers`
- **Eval / observability**: `langfuse`
- **Enterprise platforms**: `Clawith`, `dify`, `agent-governance-toolkit`
- **Memory infrastructure**: `memori-labs` (adicional a mem0/mempalace/gbrain)

### Por origem
- **Big tech / fundações**: codex (OpenAI), spec-kit/gh-aw (GitHub), workflow (Vercel), claude-code (Anthropic), autogen (Microsoft), hermes (NousResearch), mcp-servers (Anthropic/MCP)
- **YC / founders**: gstack/gbrain (Garry Tan), superpowers (Obra)
- **Comunidade**: BMAD-METHOD, crewAI, aider, OpenHands, mem0, langfuse, openclaw, mempalace, paperclip, gsd-build/*

### Por maturidade / local-first
- **Local-first**: `mempalace`, `openclaw`, `gbrain`, `hermes-agent`
- **Cloud-native**: `workflow`, `paperclip`, `gh-aw`
- **Híbrido**: `claude-remote-manager`, `gstack`, `gsd-2`

## Observações

- **Memória é first-class em 4 projetos** (gbrain, mempalace, gsd-2, hermes)
- **Spec-driven está em ascensão** (spec-kit, get-shit-done, superpowers) — alternativa a "vibe coding"
- **8 de 18 projetos** centram em coordenação multi-agente
- **GitHub e Vercel** já têm frameworks de agente em produção (gh-aw, workflow)

## Manutenção

Em uma máquina nova (ou pra atualizar tudo de uma vez):

```bash
./update.sh
```

O script lê `repos.tsv`, clona o que está faltando e dá `pull --ff-only` no que já existe. Tudo em paralelo.

Legenda: `[+]` clonado · `[↑]` atualizado · `[=]` up-to-date · `[x]` erro
