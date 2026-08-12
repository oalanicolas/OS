<div align="center">

# 🧰 cured-harness

<sub>🌐 <b>English</b> · <a href="README.pt-BR.md">Português</a></sub>

[![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)
[![Last Update](https://img.shields.io/badge/last%20update-April%202026-blue?style=flat-square)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](#contributing)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg?style=flat-square)](https://creativecommons.org/publicdomain/zero/1.0/)

<h3>Curated index of agent harnesses — frameworks, coding CLIs, memory layers, orchestration platforms and enterprise systems — used as study and benchmark references.</h3>

<a href="#-coding-agents--clis">Coding</a> · <a href="#-multi-agent-orchestration">Multi-agent</a> · <a href="#-memory--knowledge">Memory</a> · <a href="#-personal-assistants">Assistants</a> · <a href="#-spec-driven--methodology">Spec-driven</a> · <a href="#-self-improvement-loops">Self-improvement</a> · <a href="#️-workflow--durable-execution">Workflow</a> · <a href="#-protocol--infrastructure">Protocol</a> · <a href="#-evaluation--observability">Eval</a> · <a href="#-enterprise-platforms">Enterprise</a> · <a href="#-cross-agent-skills">Skills</a>

<sub>by **Alan Nicolas**</sub>

</div>

---

> **32 projects. 11 categories. Opinionated curation.** Contains no original code — all repos are forks/clones for analysis. See [Local mirror](#-local-mirror) to reproduce the bench.

---

## Contents

- [💻 Coding agents & CLIs](#-coding-agents--clis) — IDE-native, Terminal/CLI, Templates
- [🤝 Multi-agent orchestration](#-multi-agent-orchestration)
- [🧠 Memory & knowledge](#-memory--knowledge)
- [🦾 Personal assistants](#-personal-assistants)
- [📐 Spec-driven & methodology](#-spec-driven--methodology)
- [🧬 Self-improvement loops](#-self-improvement-loops)
- [⚙️ Workflow & durable execution](#️-workflow--durable-execution)
- [🔌 Protocol & infrastructure](#-protocol--infrastructure)
- [📊 Evaluation & observability](#-evaluation--observability)
- [🏢 Enterprise platforms](#-enterprise-platforms)
- [🧩 Cross-agent skills](#-cross-agent-skills)
- [🗒️ Patterns observed](#️-patterns-observed)
- [🛠 Local mirror](#-local-mirror)
- [🤝 Contributing](#contributing)
- [📄 License](#-license)

---

## 💻 Coding agents & CLIs

### Terminal / CLI

| Project | Stack | Differential |
|---------|-------|--------------|
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | TS + Ink + Bun | Snapshot (~512K LOC) of Anthropic's official CLI; canonical reference for terminal-UI coding agents. |
| [openai/codex](https://github.com/openai/codex) | TS + Rust | OpenAI's official CLI coding agent with IDE integrations and a focus on local automation. |
| [Aider-AI/aider](https://github.com/Aider-AI/aider) | Python | Most-used pair-programming CLI in open source; git-native with auto-commits per iteration. |
| [All-Hands-AI/OpenHands](https://github.com/All-Hands-AI/OpenHands) | Python | Most-starred autonomous agent on GitHub (formerly OpenDevin); standard SWE-bench benchmark. |

### Autonomous / Multi-role

| Project | Stack | Differential |
|---------|-------|--------------|
| [open-gsd/gsd-pi](https://github.com/open-gsd/gsd-pi) | TS (Pi SDK) | Living GSD: auto-milestones, worktree isolation, `.gsd/` memory, Agent Skills runtime. (gsd-2 is the archived snapshot.) |
| [garrytan/gstack](https://github.com/garrytan/gstack) | TS + Playwright | Personal software factory by YC's president; 24 specialized agents in a multi-role workflow. |
| [obra/superpowers](https://github.com/obra/superpowers) | TS (Claude Code plugin) | Pure red/green TDD with parallel subagents; reports a 94% PR rejection rate. |

### Templates / App-builders

| Project | Stack | Differential |
|---------|-------|--------------|
| [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | Next.js + shadcn | Pixel-perfect site cloning via parallel builder agents in the `/clone-website` command. |

---

## 🤝 Multi-agent orchestration

| Project | Stack | Differential |
|---------|-------|--------------|
| [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | TS | 12+ personas (PM, architect, UX…) with "Party Mode" running multiple in one session; agile applied to agents. |
| [crewAI-inc/crewAI](https://github.com/crewAI-inc/crewAI) | Python | Framework for collaborative role-playing agents with shared goals. |
| [microsoft/autogen](https://github.com/microsoft/autogen) | Python | Microsoft's multi-agent conversational framework; research baseline for message-based coordination. |
| [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | TS + React + Postgres | Manages agents like employees — org charts, budgets and goals. |
| [grandamenium/claude-remote-manager](https://github.com/grandamenium/claude-remote-manager) | Bash + TS | Claude Code 24/7 controlled via Telegram; persistent cron survives restart. |

---

## 🧠 Memory & knowledge

| Project | Stack | Differential |
|---------|-------|--------------|
| [mem0ai/mem0](https://github.com/mem0ai/mem0) | Python | Leading memory layer in 2025; native vector store and a simple API for LLM apps. |
| [milla-jovovich/mempalace](https://github.com/milla-jovovich/mempalace) | Python + Chroma | 96.6% R@5 with verbatim storage (no paraphrasing); local-first, no API keys. |
| [garrytan/gbrain](https://github.com/garrytan/gbrain) | TS + PGLite + pgvector | 95% recall@5; entity self-wiring without an LLM; 30-minute setup. |
| [MemoriLabs/Memori](https://github.com/MemoriLabs/Memori) | Python | LLM-agnostic, agent-native memory infrastructure; 81.95% on LoCoMo, SQL-backed. |

---

## 🦾 Personal assistants

| Project | Stack | Differential |
|---------|-------|--------------|
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | TS + SwiftUI + Kotlin | 20+ channels (WhatsApp, Telegram, iMessage…) running on-device. |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Python asyncio | Auto-creates skills; runs on a $5 VPS or serverless with hibernation; multi-model. |

---

## 📐 Spec-driven & methodology

| Project | Stack | Differential |
|---------|-------|--------------|
| [github/spec-kit](https://github.com/github/spec-kit) | Python + TS | Executable specs that generate implementation; GitHub's official methodology. |
| [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | TS | Solves "context rot" via spec discipline and meta-prompting; in use at Amazon, Google and Shopify. |

---

## 🧬 Self-improvement loops

Systems that iterate, mutate and optimize against a metric — descendants of `karpathy/autoresearch` and the "AI scientist" lineage. See also [`alvinreal/awesome-autoresearch`](https://github.com/alvinreal/awesome-autoresearch) for the full index.

| Project | Stack | Differential |
|---------|-------|--------------|
| [ShengranHu/ADAS](https://github.com/ShengranHu/ADAS) | Python | **Automated Design of Agentic Systems** (ICLR 2025); meta-agents that invent novel agent architectures by programming them in code. |
| [SakanaAI/AI-Scientist-v2](https://github.com/SakanaAI/AI-Scientist-v2) | Python | Workshop-level autonomous scientific discovery via agentic tree search; removes v1's template dependency and generalizes across domains. |
| [gepa-ai/gepa](https://github.com/gepa-ai/gepa) | Python | **GEPA (Genetic-Pareto)** — ICLR 2026 Oral; reflective prompt evolution that outperforms RL (GRPO); optimizes any textual parameter against any metric via natural-language reflection. |

---

## ⚙️ Workflow & durable execution

| Project | Stack | Differential |
|---------|-------|--------------|
| [vercel/workflow](https://github.com/vercel/workflow) | TS + Next.js + PG | Deterministic replay via event log; split VM + step runtime. |
| [github/gh-aw](https://github.com/github/gh-aw) | Go + Markdown | Agentic workflows written in natural language, executed sandboxed inside GitHub Actions. |

---

## 🔌 Protocol & infrastructure

| Project | Stack | Differential |
|---------|-------|--------------|
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | TS + Python | Official Model Context Protocol repo; 50+ reference servers. |

---

## 📊 Evaluation & observability

| Project | Stack | Differential |
|---------|-------|--------------|
| [langfuse/langfuse](https://github.com/langfuse/langfuse) | TS + Next.js | Most popular open-source observability for LLM apps; tracing, eval and prompt management. |

---

## 🏢 Enterprise platforms

| Project | Stack | Differential |
|---------|-------|--------------|
| [dataelement/Clawith](https://github.com/dataelement/Clawith) | TS | "OpenClaw for teams": digital employees with `soul.md` + `memory.md`, org chart and multi-tenant delegation. |
| [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | Multi-lang | Sub-ms policy enforcement covering 10/10 of the OWASP Agentic Top 10; runtime security. |
| [langgenius/dify](https://github.com/langgenius/dify) | Python + TS | Most popular low-code platform (129k+ stars); ready for teams and production. |

---

## 🧩 Cross-agent skills

| Project | Stack | Differential |
|---------|-------|--------------|
| [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | Skill (multi-agent) | Agent-agnostic skill (Claude Code, Cursor, Codex, OpenClaw, Hermes) that delivers ready-to-ship design — animations, clickable prototypes, slide decks, infographics — from a single prompt. |

---

## 🗒️ Patterns observed

Cross-cutting axis, grouping harnesses by recurring technique/architecture:

| Pattern | Projects | Note |
|---------|----------|------|
| **First-class memory** | gbrain, mempalace, gsd-pi, hermes-agent, mem0, memori-labs | Memory as a separate, measurable component — not a bolt-on. |
| **Spec-driven** | spec-kit, get-shit-done, superpowers | Pragmatic alternative to "vibe coding"; specs drive execution. |
| **Multi-persona / party-mode** | BMAD-METHOD, crewAI, autogen, paperclip, gstack | Coordination across multiple roles inside a single harness. |
| **Parallel subagents** | superpowers, ai-website-cloner-template, gstack | Task fan-out to specialized agents. |
| **Durable / replay** | vercel/workflow, gh-aw | Event-sourced; survives crashes; reproducible. |
| **Local-first** | mempalace, openclaw, gbrain, hermes-agent | No cloud dependency; on-device or self-hosted. |
| **Governance / policy** | agent-governance-toolkit, Clawith | Runtime security and agent org charts. |
| **24/7 persistent** | claude-remote-manager, hermes-agent, gsd-pi | Cron, hibernation, automatic resume. |
| **Self-improvement / autoresearch** | ADAS, AI-Scientist-v2, gepa, superpowers | A loop that measures, mutates and optimizes — code, prompts or architecture. |

---

## 🛠 Local mirror

To clone/update every project in parallel:

```bash
./update.sh
```

The script reads `repos.tsv`, clones whatever is missing and runs `pull --ff-only` on the rest.

Legend: `[+]` cloned · `[↑]` updated · `[=]` up-to-date · `[x]` error

---

## Contributing

PRs welcome. To add a harness:

1. Add an entry to `repos.tsv` in the form `name<TAB>url<TAB>branch`.
2. Add the row to the matching section's table in the README: `[owner/repo](url) | Stack | One-sentence description with the technical differential`.
3. If it represents a new recurring pattern, add it under **🗒️ Patterns observed**.

**Inclusion criterion**: the project must be a *harness* — something that orchestrates, executes, or gives memory/tools to an LLM. Pure model libraries (no agent loop) and generic infrastructure (raw vector DBs, etc.) are out of scope.

---

## 📄 License

This list is released under [CC0-1.0](https://creativecommons.org/publicdomain/zero/1.0/).
