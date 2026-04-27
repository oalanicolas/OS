# Inventário: OpenClaw

**Path:** `OS/openclaw/`
**Date:** 2026-04-19
**Extraction Method:** filesystem-scan + doc-scan
**Confidence:** HIGH

---

## Identity

| Field | Value |
|-------|-------|
| Slug | openclaw |
| Source URL | https://github.com/openclaw/openclaw |
| Primary language | TypeScript |
| Secondary languages | Swift (macOS/iOS), Kotlin (Android), Python |
| Stack | Node.js >=22, pnpm workspaces, Bun (dev), Vitest, Oxlint, Oxfmt, Ink (TUI), Docker, SwiftUI, Gradle |
| License | MIT |
| Version | 2026.4.19-beta.2 |
| Tagline | Personal AI assistant you run on your own devices; multi-channel inbox plus local-first Gateway |

## Key Metrics

| Metric | Value | Source |
|--------|-------|--------|
| TS source files | 6,676 | filesystem scan `src/` (.ts/.tsx) |
| Bundled extensions | 113 | `extensions/` dir count |
| Bundled channel extensions | 25 | `extensions/{whatsapp,telegram,slack,discord,signal,imessage,bluebubbles,matrix,irc,msteams,feishu,line,mattermost,nextcloud-talk,nostr,synology-chat,tlon,twitch,zalo,zalouser,googlechat,qqbot,qa-matrix,talk-voice,voice-call}/` |
| Bundled skills | 53 | `skills/` dir count |
| README lines | 1,433 | `README.md` |
| Docs sections | 46 | `docs/` dir |
| Last commit | 2026-04-19 | `git log -1` |

## Modules / Top-level Structure

| Module | Path | Type | Description |
|--------|------|------|-------------|
| src | `src/` | app | Gateway core (channels, agents, commands, CLI, context-engine, canvas-host, cron, gateway protocol) |
| extensions | `extensions/` | package | 113 bundled plugins (channels, model providers, memory, voice, canvas, coding) |
| packages | `packages/` | package | plugin-sdk, memory-host-sdk, plugin-package-contract |
| apps | `apps/` | app | macOS, iOS, Android, shared companion apps |
| ui | `ui/` | app | Control UI (web) |
| skills | `skills/` | package | 53 bundled agent skills |
| docs | `docs/` | library | Mintlify docs (46 sections) |
| Swabble | `Swabble/` | app | Voice/audio helper component |

## Entry Points

| Entry | Path | Command |
|-------|------|---------|
| CLI | `src/cli/` + `openclaw.mjs` | `openclaw <cmd>` |
| Gateway | `src/gateway/` | `openclaw gateway run` |
| macOS app | `apps/macos/` | OpenClaw.app (menu bar, Voice Wake) |
| iOS node | `apps/ios/` | iOS companion (paired over Gateway WS) |
| Android node | `apps/android/` | Android companion |

## Capabilities (observed)

### Core Capabilities

| Capability | Evidence | Notes |
|------------|----------|-------|
| Multi-channel messaging (25 channels) | `extensions/whatsapp/`, `extensions/telegram/`, `extensions/slack/`, `extensions/discord/`, `extensions/signal/`, `extensions/imessage/`, `extensions/bluebubbles/`, `extensions/matrix/`, `extensions/irc/`, `extensions/msteams/`, `extensions/feishu/`, `extensions/line/`, `extensions/mattermost/`, `extensions/nextcloud-talk/`, `extensions/nostr/`, `extensions/synology-chat/`, `extensions/tlon/`, `extensions/twitch/`, `extensions/zalo/`, `extensions/zalouser/`, `extensions/googlechat/`, `extensions/qqbot/`, `extensions/qa-matrix/`, `extensions/talk-voice/`, `extensions/voice-call/` | Largest channel surface observed |
| Local-first Gateway | `src/gateway/`, `src/gateway/protocol/` | Loopback-bound by default, typed protocol |
| Native companion apps | `apps/macos/`, `apps/ios/`, `apps/android/`, `apps/shared/` | SwiftUI + Kotlin |
| Voice Wake + Talk Mode | `extensions/elevenlabs/`, `extensions/talk-voice/`, `extensions/voice-call/`, `Swabble/` | ElevenLabs + system TTS fallback per README |
| Live Canvas (A2UI) | `src/canvas-host/`, `src/canvas-host/a2ui/` | Agent-driven visual workspace |
| Cron service | `src/cron/service.jobs.test.ts`, `src/cron/schedule.test.ts`, `src/cron/store.test.ts` | Built-in scheduler |
| Multi-agent routing | `src/agents/`, `src/channels/` | Route inbound → isolated agents |
| Pluggable memory (4 backends) | `extensions/active-memory/`, `extensions/memory-core/`, `extensions/memory-lancedb/`, `extensions/memory-wiki/`, `packages/memory-host-sdk/` | Single-slot; multiple options incl. LanceDB |

### Optional/Extensibility Capabilities

| Capability | Evidence | Notes |
|------------|----------|-------|
| Skills system + ClawHub | `skills/` (53 dirs), `extensions/clawhub/` | Bundled + marketplace |
| Plugin SDK (versioned) | `packages/plugin-sdk/`, `src/plugin-sdk/`, `packages/plugin-package-contract/` | Public cross-package contract |
| MCP bridge via mcporter | `skills/mcporter/`, `VISION.md` | External, not first-class in core |
| Model provider plugins (30+) | `extensions/anthropic/`, `extensions/google/`, `extensions/deepseek/`, `extensions/groq/`, `extensions/fireworks/`, `extensions/huggingface/`, `extensions/kimi-coding/`, `extensions/codex/`, `extensions/amazon-bedrock/`, `extensions/cloudflare-ai-gateway/`, `extensions/copilot-proxy/` | Broad provider support |
| Docker sandboxing (non-main) | `Dockerfile.sandbox`, `Dockerfile.sandbox-browser`, `Dockerfile.sandbox-common`, `docker-compose.yml` | Per-session sandbox |
| DM pairing + allowlists | `src/channels/allowlists/`, `README.md` | Pairing codes for unknown senders |
| Remote (Tailscale, SSH) | `docs/` sections, `AGENTS.md` | Remote gateway control |

## Tests / Quality Signals

| Signal | Value | Evidence |
|--------|-------|----------|
| Test framework | Vitest | `vitest.config.ts` |
| Colocated tests | `*.test.ts` | Pattern per AGENTS.md |
| Linter | Oxlint + Oxfmt | `.oxlintrc.json`, `.oxfmtrc.jsonc` |
| Coverage threshold | 70% (lines/branches/functions/statements) | `AGENTS.md` |
| CI/CD | GitHub Actions | `.github/workflows/` |
| Pre-commit | installed via `prepare` script | `git-hooks/` |

## Documentation

| Type | Path | Status |
|------|------|--------|
| README | `README.md` | 1,433 lines |
| VISION | `VISION.md` | Present |
| SECURITY | `SECURITY.md` | 27 KB |
| CONTRIBUTING | `CONTRIBUTING.md` | Present |
| INCIDENT_RESPONSE | `INCIDENT_RESPONSE.md` | Present |
| Mintlify docs | `docs/` | 46 sections |
| Plugin docs | `docs/plugins/` | sdk-overview, manifest, architecture, channel, provider |
| Architecture doc | `docs/concepts/architecture.md` | Present |

## Extension Points

| Extension Type | Where | How to extend |
|----------------|-------|---------------|
| Plugins | `extensions/` + `packages/plugin-sdk/` | Bundled or npm-distributed; manifest + plugin-sdk contract |
| Channel plugins | `src/plugin-sdk/channel-contract.ts` | Typed channel contract; 25 bundled |
| Provider plugins | `src/plugin-sdk/provider-entry.ts` | Auto-enable hooks, SecretRef auth |
| Memory plugin | `packages/memory-host-sdk/` | Single-slot; one active at a time |
| Skills | `skills/` + ClawHub (clawhub.ai) | Bundled or marketplace |
| MCP | `skills/mcporter/` | External bridge |
| Hooks | `hooks.internal.entries` config | Inbound, pairing, onboarding events |

## Notable Design Decisions

- **Terminal-first setup by design** — evidence: `VISION.md` "OpenClaw is currently terminal-first by design."
- **Manifest-first control plane, runtime execution separate** — evidence: `AGENTS.md` "Keep runtime execution separate: actual provider/channel/tool execution should resolve through narrow targeted loaders."
- **Single-slot memory plugin** — evidence: `VISION.md` "Memory is a special plugin slot where only one memory plugin can be active at a time."
- **MCP via mcporter, not first-class** — evidence: `VISION.md` "we prefer this bridge model over building first-class MCP runtime into core."
- **Loopback-bound Gateway by default** — evidence: `AGENTS.md` restart command uses `--bind loopback`.

## Limitations / Known Issues

- No first-class MCP server in core (delegated to external `mcporter`) — `VISION.md`
- Terminal-first onboarding (no hidden convenience wrappers) — `VISION.md`
- Memory plugin is single-slot (one active backend) — `VISION.md`

## Unique Selling Points

- 25 bundled channel extensions — the widest observed here
- Native macOS/iOS/Android companion apps
- Live Canvas (A2UI) — agent-driven visual output
- Voice Wake + Talk Mode with ElevenLabs + TTS fallback
- Docker sandboxing for non-main sessions
- Strict, contract-enforced plugin/extension boundaries

---

## Extraction Notes

- Scanned directories: `src/`, `extensions/`, `packages/`, `apps/`, `skills/`, `docs/`
- Skipped: `node_modules`, `dist`, `.git`, `pnpm-lock.yaml`
- Data sources: filesystem 100%
- Tools used: `ls`, `find`, `grep`, README/VISION/AGENTS read

---

_Generated by os-bench inventory task | Template v1.0_
