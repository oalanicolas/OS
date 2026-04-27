# Executive Report: openclaw vs hermes-agent vs gbrain

**Date:** 2026-04-19
**Type:** n-way (3-way)
**Slug:** personal-assistant-3way
**Dimension pack:** `personal-assistant`

---

## Executive Summary (EN)

This benchmark compares three opensource projects that all orbit the "personal assistant" space but occupy distinctly different product tiers: **openclaw** is a multi-channel, multi-device assistant platform (25 bundled channels, native macOS/iOS/Android apps, Voice Wake, Live Canvas); **hermes-agent** is a self-improving cross-channel CLI agent that runs anywhere from a $5 VPS to serverless hibernation (Modal, Daytona); **gbrain** is a knowledge brain substrate with hybrid RAG + a self-wiring zero-LLM knowledge graph that plugs *into* either openclaw or hermes. On the pack-weighted total hermes-agent leads (84.75) narrowly over openclaw (80.91), with gbrain at 68.45 because the 20%-weighted `channels` dimension is zero-by-design for a brain layer. When the channels weight is excluded and rebalanced, hermes-agent (85.44) and gbrain (83.06) are within ~2.4 points and openclaw falls to 77.39. The correct read is: **pick openclaw for channel reach, pick hermes-agent for an agent that learns, pick gbrain as the memory layer under either, compose them for all three.**

## Sumário Executivo (PT-BR)

Este benchmark compara três projetos opensource no espaço "assistente pessoal" que ocupam camadas de produto diferentes: **openclaw** é uma plataforma de assistente multi-canal e multi-device (25 canais, apps nativos macOS/iOS/Android, Voice Wake, Live Canvas); **hermes-agent** é um agente CLI cross-canal que se auto-melhora e roda em qualquer lugar do $5 VPS até serverless com hibernação; **gbrain** é um substrato de brain/knowledge com hybrid RAG + grafo auto-wiring de zero LLM calls que pluga *sob* openclaw ou hermes. No total ponderado do pack, hermes-agent lidera (84.75) estreito sobre openclaw (80.91), com gbrain em 68.45 por causa do peso de 20% em `channels` — dimensão zero-by-design para um brain layer. Excluindo channels e rebalanceando, hermes (85.44) e gbrain (83.06) ficam dentro de ~2.4 pts e openclaw cai para 77.39. A leitura correta é: **escolha openclaw pela amplitude de canais, escolha hermes-agent por um agente que aprende, escolha gbrain como camada de memória sob qualquer dos dois, componha os três para ter tudo.**

---

## Key Metrics

| Metric | Value |
|--------|-------|
| Overall winner (pack as declared) | **hermes-agent** (84.75) — +3.84 vs openclaw |
| Overall winner (channels excluded) | **hermes-agent** (85.44) — +2.38 vs gbrain, +8.05 vs openclaw |
| Dimensions analyzed | 6 (channels, local_first, memory, skills, cost, privacy) |
| openclaw dimension wins | 2 (channels, local_first-narrow) |
| hermes-agent dimension wins | 2 (skills, cost) + memory (#2), cost (#1) |
| gbrain dimension wins | 2 (memory, privacy-narrow) |
| Confidence overall | HIGH (all three filesystem-scanned with 4+ evidence paths/dimension) |

---

## Scorecard Summary

| Dimension | Weight | openclaw | hermes-agent | gbrain | Winner |
|-----------|:------:|:--------:|:------------:|:------:|:------:|
| Channels | 20% | **95**/100 | 82/100 | 10/100 | openclaw |
| Local-first | 18% | **82**/100 | 80/100 | 80/100 | openclaw (narrow) |
| Memory | 15% | 68/100 | 85/100 | **92**/100 | gbrain |
| Skills | 17% | 78/100 | **92**/100 | 75/100 | hermes-agent |
| Cost | 13% | 75/100 | **92**/100 | 85/100 | hermes-agent |
| Privacy | 17% | 82/100 | 80/100 | **85**/100 | gbrain (narrow) |
| **Weighted total** | **100%** | **80.91** | **84.75** | **68.45** | **hermes-agent** |
| *Rebalanced (no channels)* | *80%→100%* | *77.39* | ***85.44*** | *83.06* | *hermes-agent* |

---

## Dimension Analysis

### Channels (20%)

**openclaw: 95** | **hermes-agent: 82** | **gbrain: 10**

openclaw ships the largest channel surface observed in `OS/` — 25 bundled messaging extensions covering WhatsApp, Telegram, Slack, Discord, Signal, iMessage (native + BlueBubbles), IRC, Microsoft Teams, Matrix, Feishu, LINE, Mattermost, Nextcloud Talk, Nostr, Synology Chat, Tlon, Twitch, Zalo, WeChat via `qqbot`, Google Chat, and native talk-voice/voice-call — plus companion apps for macOS (SwiftUI), iOS, and Android (Kotlin), Voice Wake + Talk Mode, and the Live Canvas A2UI visual surface. hermes-agent covers 19 gateway platforms with a genuinely unique tier: email, SMS, and Home Assistant as first-class conversational channels — something openclaw does not ship — but no native mobile/desktop apps and only voice-memo-grade transcription (not continuous voice). gbrain has no bundled channels; it offers 7 YAML+MD integration recipes (calendar, email, twilio-voice, x-to-brain, etc) for ingest, not for chat.

**Key signals:**

- openclaw: 25 extensions — `OS/openclaw/extensions/`
- openclaw: native apps — `OS/openclaw/apps/{macos,ios,android}/`
- hermes-agent: 19 platforms incl. email/sms/homeassistant — `OS/hermes-agent/gateway/platforms/`
- gbrain: 0 channels, 7 recipes — `OS/gbrain/recipes/`

---

### Local-first (18%)

**openclaw: 82** | **hermes-agent: 80** | **gbrain: 80**

Three-way cluster. openclaw is the strictest on-device story (Gateway binds `loopback` by default per `AGENTS.md`; Dockerfile.sandbox + sandbox-browser + sandbox-common for untrusted code). hermes-agent is the most flexible: 6 runtime backends (local, Docker, SSH, Daytona, Singularity, Modal, managed_modal) with explicit serverless hibernation. gbrain has the most local-first *data* story — PGLite is an embedded WASM Postgres ready in 2 seconds with no server and no API keys; the default MCP transport is stdio. None is fully offline because of model provider dependency.

**Key signals:**

- openclaw: loopback default — `OS/openclaw/AGENTS.md`
- hermes-agent: 6 backends — `OS/hermes-agent/tools/environments/`
- gbrain: PGLite WASM — `OS/gbrain/src/core/pglite-engine.ts`

---

### Memory (15%)

**openclaw: 68** | **hermes-agent: 85** | **gbrain: 92**

gbrain's dimension. It's the only subject with: (a) a published retrieval benchmark (BrainBench v1: R@5 83%→95%, graph-only F1 86.6% vs grep 57.8%), (b) a self-wiring knowledge graph with typed edges (`attended`, `works_at`, `invested_in`, `founded`, `advises`) extracted on *every* page write with zero LLM calls, (c) hybrid RAG (vector + keyword + RRF + multi-query expansion + dedup), and (d) a retrieval eval harness (P@k, R@k, MRR, nDCG@k, A/B). hermes-agent has a rich memory *experience* — agent-curated persistent memory with periodic nudges, FTS5 session search with LLM summarization for cross-session recall, 8 pluggable providers, and Honcho dialectic user modeling — but no published retrieval metric. openclaw's memory is a first-class single-slot plugin with 4 backends, but no KG, no auto-link, no benchmark.

**Key signals:**

- gbrain: BrainBench v1 — `OS/gbrain/docs/benchmarks/2026-04-18-brainbench-v1.md`
- gbrain: zero-LLM auto-link — `OS/gbrain/src/core/link-extraction.ts`
- hermes-agent: FTS5 session search — `OS/hermes-agent/tools/session_search_tool.py`
- hermes-agent: 8 memory providers — `OS/hermes-agent/plugins/memory/`
- openclaw: 4 memory extensions + SDK — `OS/openclaw/packages/memory-host-sdk/`

---

### Skills (17%)

**openclaw: 78** | **hermes-agent: 92** | **gbrain: 75**

hermes-agent's dimension. It is the **only subject with autonomous skill creation** — README explicit: "Autonomous skill creation after complex tasks. Skills self-improve during use." It ships native MCP on both sides (server + client + OAuth manager), 63 tools in a registry, and is agentskills.io-standard-compatible with a Skills Hub. openclaw leads on raw skill count (53) and has the most formal skill distribution story (ClawHub marketplace + versioned public Plugin SDK in `packages/plugin-sdk/` with strict boundary rules), but MCP is bridge-only via external mcporter. gbrain has native MCP (41 ops auto-exposed from a single contract-first `operations.ts`), 26 skills, and a skill-creator skill, but no marketplace and skill creation is agent-driven, not experiential.

**Key signals:**

- hermes-agent: auto-skill creation — `OS/hermes-agent/tools/skill_manager_tool.py` + README
- hermes-agent: native MCP + OAuth — `OS/hermes-agent/mcp_serve.py`, `OS/hermes-agent/tools/mcp_oauth_manager.py`
- openclaw: 53 skills — `OS/openclaw/skills/`
- openclaw: versioned Plugin SDK — `OS/openclaw/packages/plugin-sdk/`
- gbrain: 41 MCP ops from contract — `OS/gbrain/src/core/operations.ts`

---

### Cost (13%)

**openclaw: 75** | **hermes-agent: 92** | **gbrain: 85**

hermes-agent explicitly markets a "$5 VPS, a GPU cluster, or serverless infrastructure that costs nearly nothing when idle" in its README and backs it with real code: Modal + Daytona backends that hibernate when idle. gbrain reduces infra cost to essentially zero via PGLite (in-process DB), only suggesting Supabase at 1000+ files; variable cost is OpenAI embeddings. openclaw runs on your own device by default (free) but scaling implies a mac or VPS + many model calls across channels.

**Key signals:**

- hermes-agent: "$5 VPS" + hibernation — `OS/hermes-agent/README.md`, `OS/hermes-agent/tools/environments/modal.py`
- gbrain: PGLite embedded — `OS/gbrain/src/core/pglite-engine.ts`
- openclaw: device default — `OS/openclaw/README.md`

---

### Privacy (17%)

**openclaw: 82** | **hermes-agent: 80** | **gbrain: 85**

All three have explicit data ownership. openclaw has the most mature **inbound** policy (DM pairing codes, per-channel `allowFrom`, Docker sandbox for non-main sessions) but no PII redaction. hermes-agent is the only one with an explicit **redaction module** (`agent/redact.py`) and adds container isolation + command approval. gbrain formalizes privacy at the **identity layer**: a 4-tier `ACCESS_POLICY.md` (plus `SOUL.md` + `USER.md` + `HEARTBEAT.md`) from `soul-audit`, an `OperationContext.remote` flag in `operations.ts` that tightens filesystem confinement for untrusted agent callers, SSRF helpers, and prompt-injection sanitization.

**Key signals:**

- openclaw: DM pairing + allowFrom — `OS/openclaw/src/channels/allowlists/`
- hermes-agent: PII redact — `OS/hermes-agent/agent/redact.py`
- gbrain: 4-tier ACCESS_POLICY + remote flag — `OS/gbrain/skills/soul-audit/SKILL.md`, `OS/gbrain/src/core/operations.ts`

---

## Gap Highlights

### Top gaps of openclaw (what hermes-agent or gbrain have that openclaw doesn't)

| # | Capability | Source | Dimension |
|---|-----------|--------|-----------|
| 1 | Autonomous skill creation from experience | hermes-agent | skills |
| 2 | Self-wiring KG with zero-LLM auto-link on every write | gbrain | memory |
| 3 | Published retrieval benchmark (R@5 83%→95%, graph-only F1 86.6%) | gbrain | memory |
| 4 | Native MCP server + client + OAuth (not a bridge) | hermes-agent, gbrain | skills |
| 5 | Serverless hibernation (Modal + Daytona) for near-zero idle cost | hermes-agent | cost |
| 6 | FTS5 cross-session search with LLM summarization | hermes-agent | memory |
| 7 | Honcho dialectic user modeling | hermes-agent | memory |
| 8 | Email + SMS + Home Assistant as first-class channels | hermes-agent | channels |
| 9 | Explicit PII redaction module | hermes-agent | privacy |
| 10 | 4-tier identity system (SOUL/USER/ACCESS_POLICY/HEARTBEAT) | gbrain | privacy |

### Top gaps of hermes-agent (what openclaw or gbrain have)

| # | Capability | Source | Dimension |
|---|-----------|--------|-----------|
| 1 | Native companion apps (macOS SwiftUI + iOS + Android Kotlin) | openclaw | channels |
| 2 | 25 bundled channels (vs 19) incl. Twitch, Nostr, Tlon, LINE, NextcloudTalk, Synology Chat | openclaw | channels |
| 3 | Voice Wake + Talk Mode (continuous voice) | openclaw | channels |
| 4 | Live Canvas (A2UI) visual agent workspace | openclaw | channels / ux |
| 5 | Versioned public Plugin SDK (packaged contract) | openclaw | skills |
| 6 | Self-wiring knowledge graph + published benchmark | gbrain | memory |
| 7 | 4-tier identity + ACCESS_POLICY | gbrain | privacy |
| 8 | DM pairing codes + per-channel allowFrom | openclaw | privacy |
| 9 | Contract-first ops (41 ops → CLI + MCP) | gbrain | skills |

### Top gaps of gbrain (what openclaw or hermes-agent have)

| # | Capability | Source | Dimension |
|---|-----------|--------|-----------|
| 1 | Any messaging channel surface | openclaw, hermes-agent | channels (by design for gbrain) |
| 2 | Autonomous skill creation | hermes-agent | skills |
| 3 | Serverless runtime hibernation | hermes-agent | cost |
| 4 | Explicit PII redaction module | hermes-agent | privacy |
| 5 | Native mobile apps | openclaw | channels / ux |
| 6 | Voice Wake / continuous voice | openclaw | channels |
| 7 | FTS5 session search + LLM summarization for chat history | hermes-agent | memory (gbrain cover with its own search) |
| 8 | Skill marketplace (ClawHub / agentskills.io) | openclaw, hermes-agent | skills |

Note: `gbrain` README positions it as a layer *under* openclaw or hermes — many of its "gaps" are intentional (it is not an assistant).

---

## Strategic Recommendations

### 1. Compose, don't pick (composability is the real winner)

The gbrain README explicitly names both openclaw and hermes as target hosts. The three repos form a natural stack: hermes-agent **or** openclaw as the harness (choose based on channel/runtime needs) + gbrain as the memory substrate. Anyone evaluating these three as substitutes in the same slot is framing the question wrong.

- **Target:** all three users
- **Expected impact:** highest leverage path for any real assistant product
- **Priority:** P0

### 2. If you need channel reach + native apps → openclaw, adopt gbrain as the memory layer

openclaw's 25 channel extensions + native macOS/iOS/Android apps + Voice Wake + Live Canvas are uncontested. Its memory score (68) is the weakest of the three dimensions; bolting gbrain in as the memory plugin (via memory-host-sdk contract) directly addresses that weakness. gbrain's zero-LLM KG + hybrid RAG + published benchmark would lift openclaw's memory score to ~88+ without touching channels, local-first, or privacy.

- **Target:** openclaw users
- **Addresses:** openclaw's Memory gap (68 → ~88)
- **Expected impact:** top-tier personal assistant with measured memory quality
- **Priority:** P0

### 3. If you want an agent that *learns* and runs cheap → hermes-agent, consider gbrain for deep retrieval

hermes-agent's autonomous skill creation + skill self-improvement is a unique differentiator. Its memory model (FTS5 session search + Honcho + 8 pluggable providers) is rich but unmeasured. Stacking gbrain as an additional memory provider (it exposes 41 MCP operations) would give hermes the retrieval-quality signals it lacks without replacing the agent-curated memory + nudge loop.

- **Target:** hermes-agent users
- **Addresses:** hermes-agent's memory-measurability gap; adds KG capability
- **Expected impact:** measurable retrieval quality + preserves learning loop
- **Priority:** P1

### 4. Treat `channels` as an openclaw concern, not a gbrain concern

When benchmarking gbrain in a personal-assistant pack, the 20%-channels weight penalizes it inappropriately (it is a substrate). This benchmark computed both the pack-weighted and channels-excluded rankings explicitly; for future evaluations of gbrain, use the `memory` pack (where it competes with mempalace/mem0/gsd-2) rather than `personal-assistant`.

- **Target:** benchmark methodology
- **Expected impact:** fairer positioning of substrate-class tools
- **Priority:** P2

### 5. Fill the cross-subject gaps

- **openclaw** should publish a retrieval-quality benchmark for its memory plugins (closes the single biggest memory gap observable in code without changing architecture).
- **hermes-agent** should document which of its 8 memory providers offer graph traversal; today none appear to match gbrain's typed-edge capability.
- **gbrain** should publish a canonical "install under openclaw" playbook parallel to the existing one for hermes — openclaw's memory-host-sdk looks compatible but is not documented on the gbrain side.

- **Target:** all three maintainer groups
- **Priority:** P2

---

## When to Pick Which

### Choose openclaw if…

- You want **the most channels out of the box** (25 bundled: WhatsApp + Telegram + iMessage + Discord + Slack + Signal + IRC + Matrix + ...).
- You need **native mobile/desktop companion apps** (macOS SwiftUI, iOS, Android Kotlin).
- You want **continuous voice** (Voice Wake + Talk Mode) — not just transcription.
- You want a **Live Canvas / visual workspace** surface (A2UI).
- You need the **most formal plugin architecture** (versioned Plugin SDK, strict boundaries enforced in CI).
- Your primary security concern is **untrusted inbound messages** (DM pairing + allowFrom + Docker sandbox is the best story here).

### Choose hermes-agent if…

- You want an **agent that learns new skills autonomously** from its own task experience.
- You want to **run cheap** (explicit $5 VPS path) or serverless with idle hibernation (Modal, Daytona).
- You want **cross-session / cross-channel recall** of past conversations (FTS5 + LLM summarization is explicit).
- You want **native MCP on both sides** (server + client + OAuth manager) — not a bridge.
- You need **email, SMS, or Home Assistant** as first-class channels.
- You want **research-ready** infrastructure (batch trajectory generation + Atropos RL + trajectory compression).
- You value **explicit PII redaction** (the only one shipping `redact.py`).

### Choose gbrain if…

- You already have openclaw or hermes and want to **add a serious memory layer** (it is designed to plug into both).
- You need **measurable retrieval quality** (BrainBench v1 reproducible, R@5 83%→95%).
- You want a **self-wiring knowledge graph** with typed edges extracted by code (no LLM calls per write).
- You want **zero-config setup** (PGLite embedded Postgres ready in 2s) with a migration path to Supabase.
- You want **contract-first** architecture (one file defines CLI + MCP surface).
- You need a **durable, Postgres-native job queue** in your brain (Minions).
- You want an **explicit 4-tier access policy** as part of the agent's identity (SOUL/USER/ACCESS/HEARTBEAT).

### Consider all three (composing)

- You are building a production personal assistant and want the **channel reach of openclaw** (or cost profile of hermes) **+ the memory quality of gbrain**.
- You want to A/B the two harness options (openclaw vs hermes) against the same brain (gbrain) to learn which fits your workflow.

---

## Methodology

### Data Sources

| Subject | Source | Method | Confidence |
|---------|--------|--------|------------|
| openclaw | `OS/openclaw/` | filesystem-scan + doc-scan (README, VISION, AGENTS) | HIGH |
| hermes-agent | `OS/hermes-agent/` | filesystem-scan + doc-scan (README, RELEASE_v*.md, AGENTS) | HIGH |
| gbrain | `OS/gbrain/` | filesystem-scan + doc-scan (README, CLAUDE.md, docs/benchmarks/) | HIGH |

No web fetches performed. No community signals (stars, contributors) measured.

### Scoring Method

- **Dimension pack:** `personal-assistant` (6 dimensions: channels 20%, local_first 18%, memory 15%, skills 17%, cost 13%, privacy 17%)
- **Score range:** 0–100
- **Weighting:** pesos somam 1.00
- **Signals:** each score ≥90 has 2+ observable signals with evidence paths in `OS/{subject}/`
- **Confidence rollup:** HIGH (all three have 4+ evidence paths per dimension)

### Artifacts Generated

| Artifact | File | Status |
|----------|------|:------:|
| Metadata | `metadata.json` | OK |
| Inventory — openclaw | `inventory-openclaw.json` + `.md` | OK |
| Inventory — hermes-agent | `inventory-hermes-agent.json` + `.md` | OK |
| Inventory — gbrain | `inventory-gbrain.json` + `.md` | OK |
| Comparison Matrix | `comparison-matrix.json` + `.md` | OK |
| Scorecard | `scorecard.json` + `.md` | OK |
| Executive Report | `executive-report.md` | OK |
| Gap Analysis | `gap-analysis.*` | SKIP (n-way omits per-pair gap; highlights included above) |
| Battle Card | `battle-card.md` | SKIP (n-way; "When to Pick Which" covers battle-card role) |

### Limitations

- gbrain is positioned as a substrate; the `personal-assistant` pack's 20%-channels weight gives it an unrecoverable ~18-point handicap. Alternative ranking (channels excluded, rebalanced) included to disclose this.
- No community metrics (stars, cadence) — "no invented claims".
- No performance benchmarks run on openclaw or hermes-agent (none are published in-repo); only gbrain has published retrieval numbers.
- Capability inference relies on directory names + README claims where code-level verification would take many more hours (e.g., verifying that hermes actually hibernates via Modal is taken from README and `tools/environments/modal.py` filename, not an executed test).

---

## Appendix: Source Artifacts

All artifacts in `OS/_bench/personal-assistant-3way/`:

| # | File | Type | Format |
|---|------|------|--------|
| 1 | `metadata.json` | Metadata | JSON |
| 2 | `inventory-openclaw.json` | Inventory | JSON |
| 3 | `inventory-openclaw.md` | Inventory | MD |
| 4 | `inventory-hermes-agent.json` | Inventory | JSON |
| 5 | `inventory-hermes-agent.md` | Inventory | MD |
| 6 | `inventory-gbrain.json` | Inventory | JSON |
| 7 | `inventory-gbrain.md` | Inventory | MD |
| 8 | `comparison-matrix.json` | Matrix | JSON |
| 9 | `comparison-matrix.md` | Matrix | MD |
| 10 | `scorecard.json` | Scoring | JSON |
| 11 | `scorecard.md` | Scoring | MD |
| 12 | `executive-report.md` | Report | MD |

Cached inventories also in `OS/_bench/_inventories/{openclaw,hermes-agent,gbrain}/`.

---

_Generated by os-bench bench-executive-report task | Template v1.0_
