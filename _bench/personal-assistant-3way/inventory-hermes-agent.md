# Inventário: Hermes Agent

**Path:** `OS/hermes-agent/`
**Date:** 2026-04-19
**Extraction Method:** filesystem-scan + doc-scan
**Confidence:** HIGH

---

## Identity

| Field | Value |
|-------|-------|
| Slug | hermes-agent |
| Source URL | https://github.com/NousResearch/hermes-agent |
| Primary language | Python (3.11) |
| Secondary languages | TypeScript (minor), Shell |
| Stack | Python 3.11, uv/pip, asyncio, SQLite (FTS5), Honcho, Modal, Daytona, Singularity, Docker, pytest |
| License | MIT |
| Tagline | Self-improving AI agent with built-in learning loop; skill creation, agent-curated memory, cross-channel CLI |

## Key Metrics

| Metric | Value | Source |
|--------|-------|--------|
| Python files | 981 | filesystem scan |
| Gateway platforms | 19 | `gateway/platforms/` |
| Tools | 63 | `tools/` dir |
| Bundled skill categories | 25 | `skills/` |
| Optional skill categories | 15+ | `optional-skills/` |
| Memory plugins | 8 | `plugins/memory/` |
| `run_agent.py` LOC | 12,218 | `wc -l` |
| `cli.py` LOC | 10,577 | `wc -l` |
| README lines | 186 | `README.md` |
| Last commit | 2026-04-19 | `git log -1` |

## Modules / Top-level Structure

| Module | Path | Type | Description |
|--------|------|------|-------------|
| agent | `agent/` | app | Agent loop, context engine, prompt builder, memory manager, model adapters |
| gateway | `gateway/` | service | 19 platform adapters (Telegram, Discord, Slack, WhatsApp, Signal, Matrix, Email, SMS, Home Assistant, Wecom, Feishu, etc) |
| hermes_cli | `hermes_cli/` | app | CLI commands (auth, setup wizard, doctor, gateway, plugins, profiles) |
| tools | `tools/` | package | 63 tools (browser, code-exec, delegate, cron, memory, skills, MCP, session-search, mixture-of-agents) |
| tools/environments | `tools/environments/` | package | Local, Docker, SSH, Daytona, Singularity, Modal, managed_modal |
| skills | `skills/` | package | 25 bundled skill categories |
| optional-skills | `optional-skills/` | package | 15+ opt-in skill categories |
| plugins/memory | `plugins/memory/` | package | 8 memory backends |
| plugins/context_engine | `plugins/context_engine/` | package | Pluggable context engine |
| cron | `cron/` | service | Built-in cron scheduler |
| acp_adapter / acp_registry | `acp_adapter/` `acp_registry/` | library | Agent Client Protocol adapter + registry |
| web / website | `web/` `website/` | app | Web interfaces |
| run_agent.py | `run_agent.py` | app | Main agent loop (12,218 LOC) |
| cli.py | `cli.py` | app | CLI root (10,577 LOC) |
| mcp_serve.py | `mcp_serve.py` | service | MCP server (867 LOC) |
| batch_runner.py | `batch_runner.py` | app | Batch trajectory generation (RL) |
| trajectory_compressor.py | `trajectory_compressor.py` | library | RL trajectory compression |
| tinker-atropos | `tinker-atropos/` | library | RL environment submodule |

## Entry Points

| Entry | Path | Command |
|-------|------|---------|
| CLI | `hermes` shell + `cli.py` | `hermes` |
| Agent main loop | `run_agent.py` | `python run_agent.py` |
| Gateway | `gateway/run.py` | `hermes gateway start` |
| MCP server | `mcp_serve.py` | `hermes mcp serve` |
| Batch / RL | `batch_runner.py`, `mini_swe_runner.py`, `rl_cli.py` | `python batch_runner.py` |

## Capabilities (observed)

### Core Capabilities

| Capability | Evidence | Notes |
|------------|----------|-------|
| Messaging gateway (19 platforms) | `gateway/platforms/{telegram,discord,slack,whatsapp,signal,matrix,email,sms,homeassistant,feishu,wecom,weixin,qqbot,mattermost,bluebubbles,dingtalk,webhook}.py` | Includes Home Assistant + SMS |
| Self-improving skill loop | `tools/skill_manager_tool.py`, `tools/skills_tool.py`, `tools/skills_sync.py`, `tools/skills_hub.py` | Auto skill creation; agentskills.io compatible |
| Agent-curated memory + nudges | `agent/memory_manager.py`, `agent/memory_provider.py`, `tools/memory_tool.py` | Periodic nudges; Honcho dialectic modeling |
| FTS5 session search + summarization | `tools/session_search_tool.py` | Cross-session recall per README |
| Pluggable memory (8 providers) | `plugins/memory/{byterover,hindsight,holographic,honcho,mem0,openviking,retaindb,supermemory}/plugin.yaml` | Manifest-driven |
| Pluggable context engine | `plugins/context_engine/`, `agent/context_engine.py`, `agent/context_compressor.py`, `agent/context_references.py` | Compression + reference tracking |
| Six terminal backends (incl. serverless) | `tools/environments/{local,docker,base,daytona,singularity,modal,managed_modal}.py` | Daytona+Modal offer hibernation |
| Subagent delegation + mixture-of-agents | `tools/delegate_tool.py`, `tools/mixture_of_agents_tool.py` | Parallel workstreams |
| MCP server + client + OAuth | `mcp_serve.py`, `tools/mcp_tool.py`, `tools/mcp_oauth.py`, `tools/mcp_oauth_manager.py` | Native MCP both sides |
| Cron + automations | `cron/jobs.py`, `cron/scheduler.py`, `tools/cronjob_tools.py` | Delivery to any messaging platform |
| Multi-provider LLM | `agent/anthropic_adapter.py`, `agent/bedrock_adapter.py`, `agent/gemini_{cloudcode,native}_adapter.py`, `tools/openrouter_client.py`, `hermes_cli/nous_subscription.py`, `hermes_cli/providers.py` | Switch with `hermes model`; 200+ via OpenRouter |

### Optional/Extensibility Capabilities

| Capability | Evidence | Notes |
|------------|----------|-------|
| Toolsets system | `toolsets.py`, `toolset_distributions.py` | Organize tools into named sets |
| Trajectory compression + RL | `trajectory_compressor.py`, `batch_runner.py`, `mini_swe_runner.py`, `rl_cli.py`, `tinker-atropos/`, `tools/rl_training_tool.py` | Training pipelines |
| 25 bundled + 15 opt-in skills | `skills/`, `optional-skills/` | agentskills.io compatible |
| OpenClaw migration | `hermes_cli/claw.py` | `hermes claw migrate` — settings, memory, skills, API keys |
| Voice memo transcription + TTS | `tools/neutts_synth.py`, `tools/neutts_samples/` | Voice memo path per README |
| ACP (Agent Client Protocol) | `acp_adapter/`, `acp_registry/`, `docs/acp-setup.md` | ACP support |
| TUI gateway + ui-tui | `tui_gateway/`, `ui-tui/` | Terminal UI surface |

## Tests / Quality Signals

| Signal | Value | Evidence |
|--------|-------|----------|
| Test framework | pytest | `tests/` |
| E2E tests | Yes | per README Contributing |
| CI/CD | GitHub Actions | `.github/workflows/` |

## Documentation

| Type | Path | Status |
|------|------|--------|
| README | `README.md` | 186 lines |
| AGENTS | `AGENTS.md` | 25 KB |
| Docs (hosted) | hermes-agent.nousresearch.com/docs | External hosted |
| Release notes | `RELEASE_v0.2.0.md`..`RELEASE_v0.10.0.md` | Present |
| Architecture doc | `docs/` + hosted | Yes |

## Extension Points

| Extension Type | Where | How to extend |
|----------------|-------|---------------|
| Memory plugins | `plugins/memory/` | `plugin.yaml` manifest per provider |
| Context engine plugin | `plugins/context_engine/` | Pluggable context engine |
| Tools | `tools/registry.py` | Register in registry |
| Skills | `skills/` + `optional-skills/` + Skills Hub | agentskills.io |
| MCP | `mcp_serve.py` + `tools/mcp_tool.py` | Server + client |
| ACP | `acp_adapter/` | Agent Client Protocol |
| Environments | `tools/environments/base.py` | Pluggable terminal backends |

## Notable Design Decisions

- **Self-improving / closed learning loop** — evidence: `README.md` "Agent-curated memory with periodic nudges. Autonomous skill creation after complex tasks. Skills self-improve during use."
- **Serverless + hibernation friendly** — evidence: `tools/environments/modal.py` + `managed_modal.py` + `daytona.py`; README "your agent's environment hibernates when idle and wakes on demand, costing nearly nothing between sessions."
- **Not tied to laptop** — evidence: README "Six terminal backends — local, Docker, SSH, Daytona, Singularity, and Modal."
- **Research-ready** — evidence: `batch_runner.py`, `trajectory_compressor.py`, `tinker-atropos/`, `tools/rl_training_tool.py`.
- **OpenClaw migration path** — evidence: `hermes_cli/claw.py` + README migrate section.

## Limitations / Known Issues

- Native Windows not supported (WSL2 required) — `README.md`
- Termux install uses curated `.[termux]` extra (voice deps incompatible) — `README.md`
- No native mobile companion apps (vs openclaw) — observed (no `apps/` dir)

## Unique Selling Points

- Self-improving agent: autonomous skill creation + skills improve during use
- Built-in learning loop with curated memory + nudges
- Six terminal backends; serverless hibernation (Daytona, Modal)
- FTS5 session search + LLM summarization for cross-session recall
- Honcho dialectic user modeling
- Batch trajectory generation + Atropos RL + trajectory compression
- Runs on $5 VPS or GPU cluster
- agentskills.io open-standard compatible

---

## Extraction Notes

- Scanned: `agent/`, `gateway/`, `hermes_cli/`, `tools/`, `skills/`, `optional-skills/`, `plugins/`, `environments/`
- Skipped: `venv/`, `.git`, `uv.lock`, `package-lock.json`
- Data sources: filesystem 100%
- Tools used: `ls`, `find`, `grep`, README/AGENTS read

---

_Generated by os-bench inventory task | Template v1.0_
