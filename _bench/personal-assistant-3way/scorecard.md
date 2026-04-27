# Scorecard: openclaw vs hermes-agent vs gbrain

**Date:** 2026-04-19
**Dimension pack:** `personal-assistant` (6 dimensões)
**Slug:** personal-assistant-3way
**Overall Confidence:** HIGH

> **Nota importante / Important note:** gbrain positions itself as a brain-layer substrate, not a standalone personal assistant (README: "Designed to be installed and operated by an AI agent"). Its Channels score is low by design. An alternative ranking with channels excluded is provided below.

---

## Scoring Method

- Score range: 0–100 por dimensão
- Pesos do pack `personal-assistant` (soma = 1.00): channels 0.20, local_first 0.18, memory 0.15, skills 0.17, cost 0.13, privacy 0.17
- Cada score derivado de signals documentados (ver abaixo)
- Signal ausente → score reduzido; 90+ requer 2+ signals com evidence path
- Fonte: filesystem scan 100% de `OS/{openclaw,hermes-agent,gbrain}/`

---

## Dimension Scores

| Dimension | Weight | openclaw | hermes-agent | gbrain | Confidence | Leader |
|-----------|-------:|:-------:|:------------:|:------:|:----------:|:------:|
| Channels | 20% | **95**/100 | 82/100 | 10/100 | HIGH | openclaw |
| Local-first | 18% | **82**/100 | 80/100 | 80/100 | HIGH | openclaw (narrow) |
| Memory | 15% | 68/100 | 85/100 | **92**/100 | HIGH | gbrain |
| Skills | 17% | 78/100 | **92**/100 | 75/100 | HIGH | hermes-agent |
| Cost | 13% | 75/100 | **92**/100 | 85/100 | HIGH | hermes-agent |
| Privacy | 17% | 82/100 | 80/100 | **85**/100 | HIGH | gbrain (narrow) |

---

## Weighted Total

| Subject | Weighted Score | Strongest dims | Weakest dim |
|---------|:-------------:|----------------|-------------|
| openclaw | **80.91**/100 | Channels (95), Local-first (82), Privacy (82) | Memory (68) |
| hermes-agent | **84.75**/100 | Skills (92), Cost (92), Memory (85) | Privacy (80), Local-first (80) |
| gbrain | **68.45**/100 | Memory (92), Privacy (85), Cost (85) | Channels (10) |

**Overall Winner (pack as declared):** **hermes-agent** (84.75) — +3.84 vs openclaw (80.91), +16.30 vs gbrain (68.45).

**Overall Winner (channels excluded, rebalanced):** **hermes-agent** (85.44) — with gbrain rising to 83.06 and openclaw falling to 77.39.

---

## Dimension Analysis

### Channels (20%)

**openclaw: 95/100** | **hermes-agent: 82/100** | **gbrain: 10/100** | Confidence: HIGH

openclaw has 25 bundled channel extensions (including native macOS SwiftUI + iOS + Android Kotlin companion apps, Voice Wake, Talk Mode, and the Live Canvas A2UI surface) — that is the widest channel coverage observed in this set. hermes-agent covers 19 platforms via `gateway/platforms/` with a real differentiator on the long tail: email, SMS, and Home Assistant as first-class conversational channels — something openclaw does not ship. gbrain by design has no channels; it exposes 7 YAML+MD integration recipes (calendar, email, twilio-voice, x-to-brain, etc) for ingest, not for conversation.

**Signals observed:**

- **openclaw**
  - bundled channel extensions: 25 — evidence: `OS/openclaw/extensions/{whatsapp,telegram,slack,discord,signal,imessage,bluebubbles,matrix,irc,msteams,...}`
  - native companion apps: macOS + iOS + Android — evidence: `OS/openclaw/apps/`
  - voice: Voice Wake + Talk Mode + ElevenLabs — evidence: `OS/openclaw/extensions/elevenlabs/, OS/openclaw/Swabble/`
  - Live Canvas (A2UI): `OS/openclaw/src/canvas-host/a2ui/`
- **hermes-agent**
  - gateway platforms: 19 — evidence: `OS/hermes-agent/gateway/platforms/`
  - email / SMS / HomeAssistant (unique): `OS/hermes-agent/gateway/platforms/{email,sms,homeassistant}.py`
  - voice memo transcription (not continuous): `OS/hermes-agent/tools/neutts_synth.py`
- **gbrain**
  - 0 bundled channels: README explicit
  - 7 integration recipes (import-only): `OS/gbrain/recipes/`

**Justificativa:**
- openclaw → 95: top-band; 4 independent signals.
- hermes-agent → 82: strong second; Email/SMS/HomeAssistant is a differentiator worth +5 but no native apps and no continuous voice caps it under 90.
- gbrain → 10: by design.

---

### Local-first (18%)

**openclaw: 82/100** | **hermes-agent: 80/100** | **gbrain: 80/100** | Confidence: HIGH

All three are genuinely local-first but for different reasons. openclaw binds the Gateway to loopback by default (`AGENTS.md` restart command uses `--bind loopback`) and ships Docker sandbox images for non-main sessions. hermes-agent has 6 runtime backends (local, Docker, SSH, Daytona, Singularity, Modal, managed_modal) — the "run it where you want" story is the most flexible, and the serverless hibernation path via Modal/Daytona is unique in this set. gbrain has the most local-first *data* story — PGLite (embedded Postgres 17 via WASM) is ready in 2 seconds with no server and no API keys; the default MCP transport is stdio (no network). None of the three is 100% offline because all rely on a model provider for LLM calls.

**Signals observed:**

- **openclaw**: loopback default (`AGENTS.md`), Dockerfile.sandbox + sandbox-browser + sandbox-common, on-device product per README
- **hermes-agent**: 6 backends in `tools/environments/`, serverless hibernation (`modal.py`, `managed_modal.py`, `daytona.py`), explicit "$5 VPS or GPU cluster" in README
- **gbrain**: PGLite WASM Postgres (`src/core/pglite-engine.ts`), 2-second init, stdio MCP default (`src/mcp/server.ts`)

**Justificativa:**
- openclaw → 82: clearest "strictly on-device" story.
- hermes-agent → 80: embraces cloud VMs/serverless explicitly, trades "strictly local" for deployment flexibility.
- gbrain → 80: most local-first DB layer, but runs under a host platform so its local-first-ness depends partly on the host's posture.

---

### Memory (15%)

**openclaw: 68/100** | **hermes-agent: 85/100** | **gbrain: 92/100** | Confidence: HIGH

This is gbrain's dimension. It is the only subject with a published retrieval benchmark (BrainBench v1: R@5 jumps 83%→95%, graph-only F1 86.6% vs grep 57.8%), a self-wiring knowledge graph with typed edges (`attended`, `works_at`, `invested_in`, `founded`, `advises`) extracted from every write with zero LLM calls, and a hybrid RAG stack (vector + keyword + RRF + multi-query expansion + dedup) sitting on pgvector HNSW. hermes-agent has a rich memory *experience*: agent-curated memory with periodic nudges, FTS5 session search with LLM summarization for cross-session recall, 8 pluggable memory providers, and Honcho dialectic user modeling built in — but no single measured benchmark. openclaw's memory is a first-class single-slot plugin with 4 backends (`memory-core`, `memory-lancedb`, `memory-wiki`, `active-memory`), but there is no KG, no auto-link, and no published retrieval metric.

**Signals observed:**

- **openclaw**: 4 memory extensions + `packages/memory-host-sdk/`, single-slot constraint (`VISION.md`), sessions tools per README — no benchmark, no KG
- **hermes-agent**: agent-curated memory + nudges (`agent/memory_manager.py`), FTS5 session search + LLM summarization (`tools/session_search_tool.py`), Honcho dialectic modeling (`plugins/memory/honcho/`), 8 pluggable providers
- **gbrain**: hybrid RAG (`src/core/search/`), zero-LLM typed-edge KG (`src/core/link-extraction.ts`), published benchmark (`docs/benchmarks/2026-04-18-brainbench-v1.md`), pgvector HNSW on both engines, retrieval eval harness (`src/core/search/eval.ts`)

**Justificativa:**
- openclaw → 68: pluggable and extensible but not differentiated on depth.
- hermes-agent → 85: richest memory *experience*, upper-60-89 band.
- gbrain → 92: only subject with measured retrieval quality + KG; clears 90+ bar with 4 signals.

---

### Skills (17%)

**openclaw: 78/100** | **hermes-agent: 92/100** | **gbrain: 75/100** | Confidence: HIGH

This is hermes-agent's dimension. It is the only subject with *autonomous skill creation* — the README is explicit: "Autonomous skill creation after complex tasks. Skills self-improve during use." It ships with native MCP on both sides (server + client + OAuth manager), 63 tools in a registry, 25 bundled skills + 15+ opt-in categories, and is compatible with the agentskills.io open standard (Skills Hub). openclaw has the largest raw skill count (53) and the most formal skill distribution story (ClawHub marketplace + versioned public Plugin SDK in `packages/plugin-sdk/` + strict extension boundary rules), but MCP is bridge-only via external mcporter and skills are authored manually. gbrain has native MCP (41 operations auto-exposed from a contract-first `operations.ts`), 26 skills, and a skill-creator skill, but no marketplace and no autonomous skill creation.

**Signals observed:**

- **openclaw**: 53 bundled skills, ClawHub marketplace, versioned Plugin SDK + plugin-package-contract, MCP bridge via mcporter (not first-class)
- **hermes-agent**: 25 core + 15 opt-in skill categories, Skills Hub (agentskills.io), autonomous skill creation + skill self-improvement (`tools/skill_manager_tool.py`, README), native MCP (server + client + OAuth), 63 tools
- **gbrain**: 26 skills + RESOLVER.md, native MCP server (stdio + HTTP, 41 ops), contract-first `src/core/operations.ts` (1137 LOC), skill-creator with conformance tests

**Justificativa:**
- openclaw → 78: broad surface but MCP-bridge-only and no auto-skill creation.
- hermes-agent → 92: autonomous skill loop + native MCP + marketplace + 63 tools = 5 independent signals, top band.
- gbrain → 75: native MCP and contract-first design are strong, but no marketplace and skill-creator is agent-driven, not experiential.

---

### Cost (13%)

**openclaw: 75/100** | **hermes-agent: 92/100** | **gbrain: 85/100** | Confidence: HIGH

hermes-agent explicitly markets a "$5 VPS, a GPU cluster, or serverless infrastructure that costs nearly nothing when idle" story — and backs it with actual code: Modal + Daytona backends that hibernate when idle. gbrain reduces infra cost to essentially zero for small brains via PGLite (embedded Postgres in-process, no server), only suggesting Supabase beyond 1000 files; the variable cost is OpenAI embeddings. openclaw runs on your own device as the primary path (zero infra) but the product implies a mac plus optional VPS for remote access plus many model calls across channels.

**Signals observed:**

- **openclaw**: your-device default, fly.toml + render.yaml available but not primary
- **hermes-agent**: "$5 VPS" explicit in README, Modal/Daytona hibernation (`tools/environments/modal.py`, `managed_modal.py`), portal subscription optional
- **gbrain**: PGLite embedded (zero infra cost), tiered scaling suggests Supabase only at 1000+ files, OpenAI embeddings as default paid dep

**Justificativa:**
- openclaw → 75: free on your device, but scale implies more ongoing cost.
- hermes-agent → 92: explicit cheap-VPS/hibernation pairs with the 90+ band definition ("<$5/mo or serverless with hibernation").
- gbrain → 85: PGLite is free, embeddings bill per page, no hibernation story of its own.

---

### Privacy (17%)

**openclaw: 82/100** | **hermes-agent: 80/100** | **gbrain: 85/100** | Confidence: HIGH

All three have explicit data ownership and some form of untrusted-input handling. openclaw has the most mature inbound-policy story: DM pairing codes, per-channel `allowFrom`, Docker sandboxing for non-main sessions — but no explicit PII redaction tool. hermes-agent is the only one with an explicit redaction module (`agent/redact.py`) and adds container isolation + command approval; its inbound-policy story is less formalized than openclaw's. gbrain formalizes privacy at the identity layer: a 4-tier `ACCESS_POLICY.md` (plus `SOUL.md` + `USER.md` + `HEARTBEAT.md`) generated by `soul-audit`, an `OperationContext.remote` flag in `operations.ts` that tightens filesystem confinement when an agent (untrusted) calls ops, SSRF helpers with internal-URL detection, and prompt-injection sanitization for the LLM channel.

**Signals observed:**

- **openclaw**: loopback default, DM pairing + allowFrom (`src/channels/allowlists/`), Dockerfile.sandbox*, data ownership (`~/.openclaw/agents/<id>/sessions/`)
- **hermes-agent**: explicit PII redaction (`agent/redact.py`), command approval + container isolation (docs), singularity + docker environments
- **gbrain**: 4-tier ACCESS_POLICY (`skills/soul-audit/SKILL.md`), `OperationContext.remote` (`src/core/operations.ts`), SSRF helpers (`src/commands/integrations.ts`: `isInternalUrl`, `parseOctet`, `hostnameToOctets`, `isPrivateIpv4`), query sanitization (`src/core/search/expansion.ts`: `sanitizeQueryForPrompt`)

**Justificativa:**
- openclaw → 82: best-of-set inbound policy, weaker on outbound PII controls.
- hermes-agent → 80: only one with an explicit redact module, less formal inbound story.
- gbrain → 85: most formal identity + trust-boundary layer, narrow edge; doesn't clear 90 because no published audit log / zero-telemetry claim.

---

## Score Distribution

### openclaw Profile

- Strongest: **Channels (95)**, Local-first (82), Privacy (82)
- Weakest: **Memory (68)**
- Unweighted average: 80.0
- Range: 68 – 95

### hermes-agent Profile

- Strongest: **Skills (92)**, **Cost (92)**, Memory (85)
- Weakest: Privacy (80), Local-first (80)
- Unweighted average: 85.2
- Range: 80 – 92

### gbrain Profile

- Strongest: **Memory (92)**, Privacy (85), Cost (85)
- Weakest: **Channels (10)** (by design)
- Unweighted average (without channels): 83.4
- Range: 10 – 92

### Competitive Dimensions (|delta| < 5 across at least 2 subjects)

- **Local-first**: openclaw 82, hermes 80, gbrain 80 — essentially tied
- **Privacy**: openclaw 82, hermes 80, gbrain 85 — 5-point spread

---

## Alternative Ranking — Channels Excluded

For the fair reading where gbrain is assessed as a brain-layer substrate (not an assistant), we exclude the `channels` weight (0.20) and rebalance the remaining five dimensions to sum to 1.00:

| Subject | Rebalanced Weighted Score |
|---------|:-------------------------:|
| **hermes-agent** | **85.44**/100 |
| **gbrain** | **83.06**/100 |
| openclaw | 77.39/100 |

In this framing, **gbrain closes the gap to hermes-agent within ~2.4 points**, and openclaw falls to third. This is the reading the three repos suggest when you take gbrain's stated position at face value.

---

## Confidence Disclosure

| Subject | Confidence | Reason |
|---------|-----------|--------|
| openclaw | HIGH | Filesystem scan with 4+ evidence paths per dimension; version + README + VISION + AGENTS consistent |
| hermes-agent | HIGH | Filesystem scan with 4+ evidence paths per dimension; README explicit on learning loop, backends, MCP |
| gbrain | HIGH | Filesystem scan + CLAUDE.md deep architecture doc + published benchmarks with reproducible harness |

### Sources

- **openclaw**: `OS/openclaw/` filesystem only (no web)
- **hermes-agent**: `OS/hermes-agent/` filesystem only (no web)
- **gbrain**: `OS/gbrain/` filesystem only (no web)

### Dimension Pack

| Pack | Version | Designed For |
|------|---------|--------------|
| `personal-assistant` | 1.0 | Multi-channel personal assistants |

### Scoring Transparency

All scores above derive from signals documented in the "Signals observed" lists. No score ≥90 was assigned with fewer than 2+ verifiable signals (evidence paths cited). When a signal could not be observed, the score was reduced and/or confidence rebaixada.

### Known Limitations

- gbrain's channels score (10) is low by design — the pack was chosen per user request; `gbrain` would normally be benchmarked under the `memory` pack (where it would compete with `mempalace`, `mem0`).
- Community signals (GitHub stars, contributor count, release cadence) were **not** measured — no web fetch performed, consistent with "no invented claims".
- No performance measurement (read/write latency, throughput) was run.
- Multi-query expansion, RRF, and KG traversal depth for gbrain are described from code structure + README, not load-tested here.

---

_Generated by os-bench bench-score task | Template v1.0_
