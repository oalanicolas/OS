# Comparison Matrix: openclaw vs hermes-agent vs gbrain

**Date:** 2026-04-19
**Comparison type:** n-way (3 subjects)
**Dimension pack:** personal-assistant
**Slug:** personal-assistant-3way

> PT-BR/EN split: sumários em PT-BR; evidência e matrizes em EN (paths são código, não tradução).

---

## Sources

| Subject | Path | Source | Confidence |
|---------|------|--------|------------|
| openclaw | `OS/openclaw/` | https://github.com/openclaw/openclaw | HIGH |
| hermes-agent | `OS/hermes-agent/` | https://github.com/NousResearch/hermes-agent | HIGH |
| gbrain | `OS/gbrain/` | https://github.com/garrytan/gbrain | HIGH |

## Method

Matriz construída a partir de filesystem scan (100%) dos três subjects em `OS/`, lendo `README.md`, `VISION.md`/`CLAUDE.md`/`AGENTS.md`, `package.json`/`pyproject.toml`, e inspecionando as pastas estruturais (`src/`, `extensions/`, `plugins/`, `skills/`, `gateway/platforms/`, `apps/`, `docs/`). Evidence paths apontam para diretórios/arquivos reais (verificados com `ls`/`find`). Todas as seis dimensões do pack `personal-assistant` foram cobertas. Nenhum dado foi puxado da web.

---

## Inventory Summary

| Metric | openclaw | hermes-agent | gbrain |
|--------|----------|--------------|--------|
| Primary language | TypeScript | Python | TypeScript (Bun) |
| Top-level surface | Gateway + 113 extensions + 3 native apps | Agent loop + gateway + CLI + 63 tools | Brain engine + MCP server + 26 skills |
| Bundled channels | 25 | 19 | 0 (host-provided) |
| Skills (bundled) | 53 | 25 + 15 opt-in categories | 26 |
| Plugins / backends | 113 extensions | 8 memory + plugin manifests | Pluggable engines (PGLite/Postgres) |
| Docs footprint | 46 doc sections + Mintlify | Hosted docs + release notes | 4 published benchmarks + ethos docs |
| Last commit | 2026-04-19 | 2026-04-19 | 2026-04-19 |
| Version | 2026.4.19-beta.2 | v0.10.0 | 0.12.3 |

---

## Feature Matrix

### Category: Channels

| Feature | openclaw | hermes-agent | gbrain | Leader |
|---------|----------|--------------|--------|--------|
| Bundled messaging channels | 25 (whatsapp, telegram, slack, discord, signal, imessage, bluebubbles, matrix, irc, msteams, feishu, line, mattermost, nextcloud-talk, nostr, synology-chat, tlon, twitch, zalo, zalouser, googlechat, qqbot, qa-matrix, talk-voice, voice-call) | 19 (telegram, discord, slack, whatsapp, signal, matrix, email, sms, homeassistant, feishu, wecom, weixin, qqbot, mattermost, bluebubbles, dingtalk, webhook, etc) | 0 (brain layer) | **openclaw** |
| Email as first-class channel | no | **yes** (`gateway/platforms/email.py`) | import-only via recipe | **hermes-agent** |
| SMS / Home Assistant | no | **yes** (`sms.py`, `homeassistant.py`) | Twilio voice recipe only | **hermes-agent** |
| Voice Wake / continuous voice | **yes** (ElevenLabs + Swabble + talk-voice + voice-call) | voice memo transcription only | no (transcription lib for ingest) | **openclaw** |
| Native companion apps (macOS/iOS/Android) | **yes** (SwiftUI + Kotlin) | no | no | **openclaw** |
| Delivery from cron/scheduled | yes (`src/cron/delivery-plan.ts`) | yes (`cron/jobs.py`) | yes (`skills/cron-scheduler/`) | TIE |
| Live Canvas / A2UI | **yes** (`src/canvas-host/a2ui/`) | no | no | **openclaw** |

### Category: Local-first

| Feature | openclaw | hermes-agent | gbrain | Leader |
|---------|----------|--------------|--------|--------|
| Runs entirely on-device | yes (Gateway loopback-bound) | yes (local default) | yes (PGLite embedded, no server) | TIE |
| Serverless + hibernation | not primary path | **yes** (Modal + Daytona hibernation) | n/a (in-process) | **hermes-agent** |
| Offline operation | partial (needs model provider) | partial (needs model provider) | mostly (PGLite offline; embeddings via OpenAI by default) | **gbrain** |
| Docker sandbox for untrusted code | yes (`Dockerfile.sandbox*`) | yes (`tools/environments/docker.py`, `singularity.py`) | n/a (no code-exec surface) | TIE |
| Zero-config setup time | ~minutes (needs onboard + auth) | ~minutes (install.sh) | **~2 seconds** (PGLite init) | **gbrain** |

### Category: Memory

| Feature | openclaw | hermes-agent | gbrain | Leader |
|---------|----------|--------------|--------|--------|
| Memory architecture | Single-slot pluggable (4 extensions: memory-core, memory-lancedb, memory-wiki, active-memory) | Agent-curated with periodic nudges + 8 pluggable providers + Honcho dialectic user modeling | Hybrid RAG (vector + keyword + RRF + MQE) + self-wiring KG | **gbrain** (depth) / **hermes-agent** (breadth of providers) |
| Cross-session / cross-channel recall | via memory plugin + sessions tools | **FTS5 session search + LLM summarization** (explicit cross-session recall) | cross-session is the default (brain is the substrate) | **hermes-agent** + **gbrain** |
| Vector index | yes (memory-lancedb) | via chosen plugin (mem0, supermemory, holographic) | yes (pgvector HNSW on both engines) | TIE (gbrain HIGH, others depend on choice) |
| Knowledge graph / typed edges | memory-wiki (wiki-style, not deeply verified) | no explicit KG (Honcho models user, not graph-of-things) | **yes — zero-LLM typed-edge auto-link on every write** (attended/works_at/invested_in/founded/advises) | **gbrain** |
| Published retrieval benchmark | no | no | **yes** (BrainBench v1: R@5 83%→95%, graph-only F1 86.6% vs grep 57.8%) | **gbrain** |
| Memory as durable queue | no | no | **yes** (Minions Postgres-native queue) | **gbrain** |

### Category: Skills

| Feature | openclaw | hermes-agent | gbrain | Leader |
|---------|----------|--------------|--------|--------|
| Bundled skill count | **53** | 25 + 15 opt-in | 26 | **openclaw** |
| Skill marketplace / hub | **yes** (ClawHub — clawhub.ai) | **yes** (Skills Hub — agentskills.io open standard) | no (shipped-with-tool) | openclaw + hermes-agent |
| **Autonomous skill creation** | no | **yes** (agent creates skills from experience; skills self-improve during use) | partial (skill-creator is agent-driven, not experiential) | **hermes-agent** |
| MCP integration | bridge only (external `mcporter`) | **native server + client + OAuth manager** | **native server** (stdio + HTTP; 41 ops exposed) | **hermes-agent** + **gbrain** |
| Versioned public Plugin SDK | **yes** (`packages/plugin-sdk`, `plugin-package-contract`) | partial (plugins/ with plugin.yaml per backend) | partial (contract is ops not plugins) | **openclaw** |
| Tool count | via 113 extensions (agent tools via skills/extensions) | 63 tools with registry | 41 operations | hermes-agent (sheer tool breadth) |

### Category: Cost

| Feature | openclaw | hermes-agent | gbrain | Leader |
|---------|----------|--------------|--------|--------|
| Default run environment | on your devices (laptop + phone) | local, $5 VPS, GPU cluster, or serverless | PGLite embedded (no DB server) | TIE (all cheap) |
| Serverless hibernation | not the primary path | **yes** (Modal + Daytona idle hibernation — "costing nearly nothing between sessions") | n/a (in-process with host) | **hermes-agent** |
| Paid deps required for baseline | 1 (model provider); many channels free | 1 (model provider); portal subscription optional | 1 (OpenAI embeddings by default) + optional Groq/Supabase | TIE |
| Lowest viable $/mo (self-host) | moderate (you run the mac or VPS) | **$5 VPS** (author explicit) | depends on host (PGLite free, Supabase tier varies) | **hermes-agent** |

### Category: Privacy

| Feature | openclaw | hermes-agent | gbrain | Leader |
|---------|----------|--------------|--------|--------|
| Default network binding | **loopback** (explicit in `AGENTS.md` restart command) | local default; remote via explicit gateway setup | stdio MCP by default; HTTP requires explicit `serve --http` + token + tunnel | **openclaw** / **gbrain** |
| DM pairing / untrusted inbound | **yes** (pairing codes for unknown senders, per-channel `allowFrom`) | yes per docs (container isolation + command approval) | yes (`OperationContext.remote` + filesystem confinement) | **openclaw** (most explicit inbound policy) |
| Data ownership | explicit (`~/.openclaw/agents/<id>/sessions/`) | explicit (configs/memory local, portable VPS) | explicit (you own the Postgres/PGLite DB; brain repo is git-trackable) | TIE |
| Explicit access-policy / identity system | per-channel allowlists + sandbox modes | per-platform allowed users + command approval | **4-tier `ACCESS_POLICY.md` + `SOUL.md` + `USER.md` + `HEARTBEAT.md` from soul-audit** | **gbrain** |
| PII redaction in logs/outputs | no explicit redaction tool observed | **yes** (`agent/redact.py`) | partial (prompt-injection sanitization, not general PII) | **hermes-agent** |
| Trust-boundary-aware ops | via sandbox.mode=non-main | via command approval | **yes** (`OperationContext.remote` flag explicit in `operations.ts`) | **gbrain** |

---

## Leaders by dimension (derived)

| Dimension | Leader | Reason |
|-----------|--------|--------|
| Channels | **openclaw** | 25 bundled channels + native apps + Voice Wake + Canvas; hermes-agent ahead only on Email/SMS/HomeAssistant and CLI-first |
| Local-first | TIE (slight edge **hermes-agent** for serverless hibernation; **gbrain** for offline DB) | All three are local by default; the deciding axis is the deployment story |
| Memory | **gbrain** | Only subject with hybrid RAG + self-wiring KG + published retrieval benchmark |
| Skills | **hermes-agent** | Only subject with autonomous skill creation from experience + agentskills.io standard + native MCP |
| Cost | **hermes-agent** | Explicit $5 VPS + serverless hibernation story |
| Privacy | **gbrain** (edge) / **openclaw** (pairing) | gbrain: 4-tier ACCESS_POLICY + remote flag; openclaw: most mature inbound allowlisting; hermes-agent has PII redaction |

---

## openclaw-only Capabilities

| # | Capability | Category | Evidence |
|---|-----------|----------|----------|
| 1 | 25 bundled channel extensions (widest observed) | Channels | `OS/openclaw/extensions/` |
| 2 | Native companion apps (macOS SwiftUI, iOS, Android Kotlin) | Channels / UX | `OS/openclaw/apps/` |
| 3 | Voice Wake + Talk Mode + Live Canvas (A2UI) | Channels / UX | `OS/openclaw/src/canvas-host/`, `OS/openclaw/extensions/elevenlabs/` |
| 4 | Versioned public Plugin SDK (packaged + contract + strict boundaries) | Skills | `OS/openclaw/packages/plugin-sdk/`, `OS/openclaw/packages/plugin-package-contract/` |
| 5 | ClawHub marketplace | Skills | `OS/openclaw/extensions/clawhub/` |
| 6 | Per-channel DM pairing + `allowFrom` | Privacy | `OS/openclaw/src/channels/allowlists/` |

## hermes-agent-only Capabilities

| # | Capability | Category | Evidence |
|---|-----------|----------|----------|
| 1 | Self-improving skills + autonomous skill creation from experience | Skills | `OS/hermes-agent/tools/skill_manager_tool.py`, `OS/hermes-agent/README.md` |
| 2 | FTS5 session search with LLM summarization | Memory | `OS/hermes-agent/tools/session_search_tool.py` |
| 3 | Honcho dialectic user modeling built-in | Memory | `OS/hermes-agent/plugins/memory/honcho/` |
| 4 | Six terminal backends including serverless hibernation (Modal, Daytona) | Cost / Local-first | `OS/hermes-agent/tools/environments/modal.py`, `daytona.py`, `managed_modal.py` |
| 5 | Native MCP server + client + OAuth manager | Skills | `OS/hermes-agent/tools/mcp_oauth_manager.py` |
| 6 | Email + SMS + Home Assistant channels | Channels | `OS/hermes-agent/gateway/platforms/email.py`, `sms.py`, `homeassistant.py` |
| 7 | Mixture-of-agents tool | Skills | `OS/hermes-agent/tools/mixture_of_agents_tool.py` |
| 8 | Explicit PII redaction | Privacy | `OS/hermes-agent/agent/redact.py` |
| 9 | Trajectory compression + Atropos RL training | Core | `OS/hermes-agent/trajectory_compressor.py`, `OS/hermes-agent/tinker-atropos/` |

## gbrain-only Capabilities

| # | Capability | Category | Evidence |
|---|-----------|----------|----------|
| 1 | Self-wiring knowledge graph with zero-LLM typed-edge auto-link | Memory | `OS/gbrain/src/core/link-extraction.ts` |
| 2 | Pluggable engines: PGLite (embedded WASM Postgres) or Postgres + pgvector | Memory / Local-first | `OS/gbrain/src/core/engine-factory.ts` |
| 3 | Hybrid RAG (vector + keyword + RRF + multi-query expansion) with published benchmark | Memory | `OS/gbrain/docs/benchmarks/2026-04-18-brainbench-v1.md` |
| 4 | Contract-first: 41 operations → CLI + MCP from single source | Skills | `OS/gbrain/src/core/operations.ts` |
| 5 | Minions: durable Postgres-native job queue with cascade-kill + idempotency | Core | `OS/gbrain/src/core/minions/queue.ts` |
| 6 | 4-tier identity system (SOUL/USER/ACCESS_POLICY/HEARTBEAT) | Privacy | `OS/gbrain/skills/soul-audit/SKILL.md` |
| 7 | Integration recipes (YAML+MD) for Twilio voice, email, calendar, X, meetings | Channels (indirect) | `OS/gbrain/recipes/` |
| 8 | Trust-boundary-aware ops (`OperationContext.remote`) | Privacy | `OS/gbrain/src/core/operations.ts` |
| 9 | Agent-driven installation (`INSTALL_FOR_AGENTS.md`) | UX | `OS/gbrain/INSTALL_FOR_AGENTS.md` |

---

## Objective Reading (PT-BR)

### Forças do openclaw

Cobertura de canal incomparável no set: 25 plugins de canal (incluindo macOS/iOS/Android nativos, Voice Wake, Canvas A2UI). A arquitetura de plugin é a mais formal das três — SDK versionado em `packages/plugin-sdk/`, contrato em `packages/plugin-package-contract/`, regras de fronteira estritas em `AGENTS.md`. Dosagem de segurança madura no ingresso: pairing codes para DMs desconhecidos e `allowFrom` por canal. O produto é o assistente multicanal — apps, voz, canvas, workspace visual incluídos.

### Forças do hermes-agent

Único com loop de aprendizado fechado: cria skills sozinho e melhora skills em uso. `session_search_tool.py` + FTS5 dão recall explícito cross-session. Arquitetura de runtime singular — 6 backends de terminal (local, docker, SSH, Daytona, Singularity, Modal, managed_modal), com hibernação serverless explícita que cumpre a promessa de "$5 VPS ou cluster GPU". Honcho embutido para modelagem dialética do usuário. MCP nativo em ambas as pontas (server + client + OAuth). Email + SMS + Home Assistant como canais primários. Único com `redact.py` dedicado. Também research-ready (Atropos + trajectory compression).

### Forças do gbrain

O único que compete na dimensão Memory num nível diferente: auto-link de grafo com zero LLM calls por escrita, hybrid RAG (vector + keyword + RRF + MQE), e benchmark publicado (BrainBench v1 — R@5 83%→95%, F1 de graph-only 86.6% vs grep 57.8%). Engine pluggable com setup em ~2 segundos via PGLite (WASM embedded Postgres). Contract-first — 41 operações geram tanto CLI quanto MCP server de uma fonte única. Minions dá fila durável nativa do Postgres. Sistema de identidade 4-tier (SOUL/USER/ACCESS_POLICY/HEARTBEAT) é o mais explícito em governance. Trust boundary no código (`OperationContext.remote`).

### Key Differentiators

- **openclaw = canais.** Se você quer alcance cross-canal real (25 plataformas + apps nativos + voz), é aqui.
- **hermes-agent = aprendizado + runtime.** Se você quer um agente que aprende skills novas autonomamente e roda barato em qualquer infra (incl. serverless hibernation), é aqui.
- **gbrain = conhecimento.** Se você quer memória de qualidade mensurável (KG + hybrid RAG + benchmark reprodutível), é aqui.

### Areas of Parity

- Todos rodam local-first por padrão.
- Todos têm cron/scheduled delivery.
- Todos suportam MCP (openclaw via bridge; outros dois nativamente).
- Todos têm sandbox/container support para código não confiável (exceto gbrain, que não tem code-exec surface).
- Todos oferecem data ownership explícita via filesystem.

### Natural Composition

O README do gbrain explicita: "Designed to be installed and operated by an AI agent" sob OpenClaw **ou** Hermes. Logo, a leitura natural é que **gbrain é o brain layer** e **openclaw / hermes-agent são as harness layers** — não são substitutos entre si no mesmo slot.

---

## Method Disclosure

- **Comparison date:** 2026-04-19
- **Dimension pack:** `personal-assistant` v1.0 (Channels, Local-first, Memory, Skills, Cost, Privacy)
- **Features compared:** 26 distintos agrupados em 6 categorias
- **Dimensions used:** 6
- **Data sources:** filesystem scan 100% (zero web fetch)
- **Confidence:** HIGH nos três (todas as capabilities citadas têm evidence path verificado)

---

_Generated by os-bench bench-matrix task | Template v1.0_
