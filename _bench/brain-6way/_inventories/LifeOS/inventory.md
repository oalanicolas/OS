# Inventario: LifeOS (Daniel Miessler)

**Path:** `OS/LifeOS/`  
**Date:** 2026-08-06  
**Confidence:** HIGH  
**Version tip:** commit `27c94f9` (2026-08-05); distribution ~v7.x (Cortex/Hermes wave)

## Identity

| Field | Value |
|-------|-------|
| Source | https://github.com/danielmiessler/LifeOS |
| Site | https://ourlifeos.ai · docs.ourlifeos.ai |
| Author | Daniel Miessler — blog danielmiessler.com |
| Former name | PAI (Personal AI Infrastructure) |
| License | MIT |
| Stack | TypeScript + Bun; skill-pack install into Claude Code (or other harness) |
| Tagline | AI-powered **Life Operating System** — Current State → Ideal State |

## What it is (product job)

**Not a standalone memory SDK.** LifeOS is a **personal OS layer on top of an agent harness**:
- TELOS / Algorithm (hill-climb current→ideal)
- **Cortex** (memory product name)
- **Pulse** daemon (dashboard, voice TTS, cron, hooks, wiki API)
- Skills library + autonomic reviewer
- Digital Assistant (DA) identity + principal identity

## Cortex (memory)

| Item | Evidence |
|------|----------|
| Storage | Markdown tree `~/.claude/LIFEOS/MEMORY/` — **no intermediate vector DB** |
| Hot layer | `PRINCIPAL_MEMORY.md` / `DA_MEMORY.md` — always loaded, set-overwrite cap |
| Knowledge archive | `KNOWLEDGE/{People,Companies,Ideas,Research}/` |
| Retrieval | **BM25** + LLM compression (`MemoryRetriever.ts`); graph separate (`MemoryGraph.ts` / graphology) |
| Graph | tags + wikilinks + related; Louvain / PageRank via graphology |
| Autonomic loop | reviewer emits typed items (memory/idea/knowledge/proposal); proposals on Pulse |
| Health | MemoryHealthCheck 22 checks; hook health gate |
| Verbatim? | Mixed — hot-layer declarative facts; knowledge as structured MD notes, not LongMemEval-style raw chat |

Source: `LifeOS/install/LIFEOS/DOCUMENTATION/Memory/MemorySystem.md`

## Pulse (runtime / voice)

| Item | Evidence |
|------|----------|
| Daemon | port 31337, launchd `com.lifeos.pulse` |
| Voice | ElevenLabs TTS notifications; Siri bridge module; voice personality on DA interview |
| Dashboard | Observatory UI (memory, algorithm, atlas, doctor…) |
| Cron | scheduled jobs from PULSE.toml |

Source: `DOCUMENTATION/Pulse/PulseSystem.md`

## Local-first stance

- All knowledge as **local files** under config root  
- Runtime depends on **cloud LLM harness** (Claude Code path primary)  
- No Qdrant/Pinecone zoo; embeddings not first-class  

## Install

```
Read https://ourlifeos.ai/install and install LifeOS for me.
```

Or `curl -fsSL https://ourlifeos.ai/install.sh | bash` (Claude Code macOS/Linux).

## Benchmarks

- **No** public LongMemEval / LoCoMo / BrainBench in-repo  
- Strength is operational (hooks, health gates, doctor) not published recall leaderboards  

## Related

- Fabric (same author): https://github.com/danielmiessler/fabric — prompt patterns, complementary  
