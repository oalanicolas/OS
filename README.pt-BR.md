<div align="center">

# 🧰 cured-harness

<sub>🌐 <a href="README.md">English</a> · <b>Português</b></sub>

[![Awesome](https://awesome.re/badge-flat2.svg)](https://awesome.re)
[![Last Update](https://img.shields.io/badge/última%20atualização-Setembro%202026-blue?style=flat-square)]()
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](#contribuindo)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0_1.0-lightgrey.svg?style=flat-square)](https://creativecommons.org/publicdomain/zero/1.0/)

<h3>Índice curado de agent harnesses — frameworks, CLIs de coding, memória, orquestração e plataformas enterprise — usados como referência e benchmark de estudo.</h3>

<a href="#-coding-agents--clis">Coding</a> · <a href="#-orquestração-multi-agente">Multi-agente</a> · <a href="#-memória--conhecimento">Memória</a> · <a href="#-assistentes-pessoais">Assistentes</a> · <a href="#-spec-driven--metodologia">Spec-driven</a> · <a href="#-self-improvement-loops">Self-improvement</a> · <a href="#️-workflow--execução-durável">Workflow</a> · <a href="#-protocolo--infraestrutura">Protocolo</a> · <a href="#-avaliação--observabilidade">Eval</a> · <a href="#-plataformas-enterprise">Enterprise</a> · <a href="#-skills-cross-agent">Skills</a>

<sub>by **Alan Nicolas**</sub>

</div>

---

> **33 projetos. 11 categorias. Curadoria opinativa.** Não contém código próprio — todos os repos são forks/clones para análise. Veja [Espelho local](#-espelho-local) para reproduzir o bench.

---

## Conteúdo

- [💻 Coding agents & CLIs](#-coding-agents--clis) — IDE-native, Terminal/CLI, Templates
- [🤝 Orquestração multi-agente](#-orquestração-multi-agente)
- [🧠 Memória & conhecimento](#-memória--conhecimento)
- [🦾 Assistentes pessoais](#-assistentes-pessoais)
- [📐 Spec-driven & metodologia](#-spec-driven--metodologia)
- [🧬 Self-improvement loops](#-self-improvement-loops)
- [⚙️ Workflow & execução durável](#️-workflow--execução-durável)
- [🔌 Protocolo & infraestrutura](#-protocolo--infraestrutura)
- [📊 Avaliação & observabilidade](#-avaliação--observabilidade)
- [🏢 Plataformas enterprise](#-plataformas-enterprise)
- [🧩 Skills cross-agent](#-skills-cross-agent)
- [🗒️ Padrões observados](#️-padrões-observados)
- [🛠 Espelho local](#-espelho-local)
- [🤝 Contribuindo](#contribuindo)
- [📄 Licença](#-licença)

---

## 💻 Coding agents & CLIs

### Terminal / CLI

| Projeto | Stack | Diferencial |
|---------|-------|-------------|
| [anthropics/claude-code](https://github.com/anthropics/claude-code) | TS + Ink + Bun | Snapshot (~512K LOC) do CLI oficial da Anthropic; referência canônica de terminal-UI para coding agents. |
| [openai/codex](https://github.com/openai/codex) | TS + Rust | CLI coding agent oficial da OpenAI, com integrações IDE e foco em automação local. |
| [Aider-AI/aider](https://github.com/Aider-AI/aider) | Python | Pair programming CLI mais usado no open source; git-native e commits automáticos por iteração. |
| [All-Hands-AI/OpenHands](https://github.com/All-Hands-AI/OpenHands) | Python | Agente autônomo mais estrelado do GitHub (ex-OpenDevin); benchmark padrão em SWE-bench. |

### Autonomous / Multi-role

| Projeto | Stack | Diferencial |
|---------|-------|-------------|
| [open-gsd/gsd-pi](https://github.com/open-gsd/gsd-pi) | TS (Pi SDK) | GSD vivo: auto-milestones, worktrees, memória em `.gsd/`, runtime Agent Skills. (gsd-2 é o snapshot arquivado.) |
| [garrytan/gstack](https://github.com/garrytan/gstack) | TS + Playwright | Software factory pessoal do presidente da YC; 24 agentes especializados em workflow multi-role. |
| [obra/superpowers](https://github.com/obra/superpowers) | TS (Claude Code plugin) | TDD red/green puro com subagents paralelos; reporta 94% de PR rejection rate. |

### Templates / App-builders

| Projeto | Stack | Diferencial |
|---------|-------|-------------|
| [JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template) | Next.js + shadcn | Clonagem pixel-perfect via builder agents paralelos no comando `/clone-website`. |

---

## 🤝 Orquestração multi-agente

| Projeto | Stack | Diferencial |
|---------|-------|-------------|
| [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) | TS | 12+ personas (PM, arquiteto, UX…) com "Party Mode" para múltiplas em uma sessão; ágil aplicado a agentes. |
| [crewAI-inc/crewAI](https://github.com/crewAI-inc/crewAI) | Python | Framework para agentes role-playing colaborativos com objetivos compartilhados. |
| [microsoft/autogen](https://github.com/microsoft/autogen) | Python | Framework multi-agente conversacional da Microsoft; padrão de pesquisa em coordenação por mensagens. |
| [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | TS + React + Postgres | Gerencia agentes como empregados — org charts, budgets e goals. |
| [grandamenium/claude-remote-manager](https://github.com/grandamenium/claude-remote-manager) | Bash + TS | Claude Code 24/7 controlado por Telegram; cron persistente sobrevive restart. |

---

## 🧠 Memória & conhecimento

| Projeto | Stack | Diferencial |
|---------|-------|-------------|
| [mem0ai/mem0](https://github.com/mem0ai/mem0) | Python | Memory layer líder em 2025; vector store nativo e API simples para LLM apps. |
| [milla-jovovich/mempalace](https://github.com/milla-jovovich/mempalace) | Python + Chroma | 96.6% R@5 com storage verbatim (sem paráfrase); local-first e sem API keys. |
| [garrytan/gbrain](https://github.com/garrytan/gbrain) | TS + PGLite + pgvector | 95.32% LongMemEval recall_all@5 com Voyage rerank (hybrid-only 93.19%; expansion@k=5 é 54.89%); self-wiring de entidades sem LLM. |
| [MemoriLabs/Memori](https://github.com/MemoriLabs/Memori) | Python | Memory infrastructure agent-native LLM-agnóstica; 81.95% no LoCoMo, backing em SQL. |

---

## 🦾 Assistentes pessoais

| Projeto | Stack | Diferencial |
|---------|-------|-------------|
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | TS + SwiftUI + Kotlin | 20+ canais (WhatsApp, Telegram, iMessage…) rodando on-device. |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Python asyncio | Auto-cria skills; roda em VPS de $5 ou serverless com hibernação; multi-model. |
| [danielmiessler/LifeOS](https://github.com/danielmiessler/LifeOS) | Skills + hooks | Life OS pessoal: TELOS/ISA como spec viva, dashboard Pulse, releases com receipts (claim ≠ done). |

---

## 📐 Spec-driven & metodologia

| Projeto | Stack | Diferencial |
|---------|-------|-------------|
| [github/spec-kit](https://github.com/github/spec-kit) | Python + TS | Specs executáveis que geram implementação; metodologia oficial do GitHub. |
| [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | TS | Resolve "context rot" via spec discipline e meta-prompting; em uso na Amazon, Google e Shopify. |

---

## 🧬 Self-improvement loops

Sistemas que iteram, mutam e otimizam contra uma métrica — descendentes do `karpathy/autoresearch` e da linhagem de "AI scientist". Veja também [`alvinreal/awesome-autoresearch`](https://github.com/alvinreal/awesome-autoresearch) para o índice completo.

| Projeto | Stack | Diferencial |
|---------|-------|-------------|
| [ShengranHu/ADAS](https://github.com/ShengranHu/ADAS) | Python | **Automated Design of Agentic Systems** (ICLR 2025); meta-agentes que inventam novas arquiteturas de agente programando-as em código. |
| [SakanaAI/AI-Scientist-v2](https://github.com/SakanaAI/AI-Scientist-v2) | Python | Descoberta científica autônoma em nível de workshop via agentic tree search; remove a dependência de template do v1 e generaliza entre domínios. |
| [gepa-ai/gepa](https://github.com/gepa-ai/gepa) | Python | **GEPA (Genetic-Pareto)** — ICLR 2026 Oral; evolução reflexiva de prompts que supera RL (GRPO); otimiza qualquer parâmetro textual contra qualquer métrica via reflexão em linguagem natural. |

---

## ⚙️ Workflow & execução durável

| Projeto | Stack | Diferencial |
|---------|-------|-------------|
| [vercel/workflow](https://github.com/vercel/workflow) | TS + Next.js + PG | Replay determinístico via event log; split VM + step runtime. |
| [github/gh-aw](https://github.com/github/gh-aw) | Go + Markdown | Agentic workflows escritos em linguagem natural, executados sandboxed em GH Actions. |

---

## 🔌 Protocolo & infraestrutura

| Projeto | Stack | Diferencial |
|---------|-------|-------------|
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | TS + Python | Repo oficial do Model Context Protocol; 50+ servers de referência. |

---

## 📊 Avaliação & observabilidade

| Projeto | Stack | Diferencial |
|---------|-------|-------------|
| [langfuse/langfuse](https://github.com/langfuse/langfuse) | TS + Next.js | Observability OS mais popular para apps LLM; tracing, eval e prompt management. |

---

## 🏢 Plataformas enterprise

| Projeto | Stack | Diferencial |
|---------|-------|-------------|
| [dataelement/Clawith](https://github.com/dataelement/Clawith) | TS | "OpenClaw para times": digital employees com `soul.md` + `memory.md`, org chart e delegation multi-tenant. |
| [microsoft/agent-governance-toolkit](https://github.com/microsoft/agent-governance-toolkit) | Multi-lang | Policy enforcement sub-ms cobrindo 10/10 do OWASP Agentic Top 10; runtime security. |
| [langgenius/dify](https://github.com/langgenius/dify) | Python + TS | Plataforma low-code mais popular (129k+ stars); pronta para teams e production. |

---

## 🧩 Skills cross-agent

| Projeto | Stack | Diferencial |
|---------|-------|-------------|
| [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | Skill (multi-agent) | Skill agent-agnóstica (Claude Code, Cursor, Codex, OpenClaw, Hermes) que entrega design pronto — animações, protótipos clicáveis, PPT, infográficos — a partir de um prompt. |

---

## 🗒️ Padrões observados

Eixo cruzado, agrupando harnesses por técnica/arquitetura recorrente:

| Padrão | Projetos | Observação |
|--------|----------|------------|
| **Memória first-class** | gbrain, mempalace, gsd-pi, hermes-agent, mem0, memori-labs, LifeOS | Memória como componente separado e medível, não bolt-on. |
| **Spec-driven** | spec-kit, get-shit-done, superpowers | Alternativa pragmática a "vibe coding"; specs guiam execução. |
| **Multi-persona / party-mode** | BMAD-METHOD, crewAI, autogen, paperclip, gstack | Coordenação entre múltiplos roles em um harness. |
| **Subagents paralelos** | superpowers, ai-website-cloner-template, gstack | Fan-out de tarefas para agentes especializados. |
| **Durable / replay** | vercel/workflow, gh-aw | Event-sourced; sobrevive a crash; reproduzível. |
| **Local-first** | mempalace, openclaw, gbrain, hermes-agent, LifeOS | Sem dependência de cloud; on-device ou self-hosted. |
| **Governance / policy** | agent-governance-toolkit, Clawith | Runtime security e org chart de agentes. |
| **24/7 persistente** | claude-remote-manager, hermes-agent, gsd-pi | Cron, hibernação, retomada automática. |
| **Self-improvement / autoresearch** | ADAS, AI-Scientist-v2, gepa, superpowers | Loop que mede, muta e otimiza — código, prompts ou arquitetura. |

---

## 🛠 Espelho local

Para clonar/atualizar todos os projetos em paralelo:

```bash
./update.sh
```

O script lê `repos.tsv`, clona o que falta e dá `pull --ff-only` no resto. Linhas com `#` são ignoradas (`next-level-outreach` está 404 desde 2026-08-23; o clone local foi preservado).

Legenda: `[+]` clonado · `[↑]` atualizado · `[=]` up-to-date · `[x]` erro

Notas do último sync: [`_bench/_research/os-update-convergence-2026-09-05.md`](_bench/_research/os-update-convergence-2026-09-05.md).

---

## Contribuindo

PRs são bem-vindos. Para adicionar um harness:

1. Adicione a entrada em `repos.tsv` no formato `name<TAB>url<TAB>branch`.
2. Adicione a linha na tabela da seção correspondente do README, com `[owner/repo](url) | Stack | Descrição em uma frase com diferencial técnico`.
3. Se for um padrão novo recorrente, adicione em **🗒️ Padrões observados**.

**Critério de inclusão**: o projeto precisa ser um *harness* — algo que orquestra, executa, dá memória ou ferramentas a um LLM. Bibliotecas-modelo (sem loop de agente) e infraestrutura genérica (vector DB puro, etc.) ficam de fora.

---

## 📄 Licença

Esta lista é distribuída sob [CC0-1.0](https://creativecommons.org/publicdomain/zero/1.0/).
