# Inventário: claude-remote-manager

**Path:** `OS/claude-remote-manager/`
**Date:** 2026-04-19
**Extraction Method:** filesystem-scan + doc-scan
**Confidence:** HIGH

---

## Identity

| Field | Value |
|-------|-------|
| Slug | claude-remote-manager |
| Source URL | https://github.com/grandamenium/claude-remote-manager |
| Primary language | Bash |
| Secondary languages | Markdown |
| Stack | Bash, tmux, launchd (macOS), jq, Telegram Bot API, Claude Code CLI |
| License | unknown |
| Tagline | Persistent 24/7 Claude Code agents controlled from Telegram — persistência (launchd+tmux), hooks de permissão, A2A bus, cron scheduling. |

## Key Metrics

| Metric | Value | Source |
|--------|-------|--------|
| LOC (.sh) | 3.691 | `wc -l` |
| Files | 60 | filesystem scan |
| Top-level dirs | core, agents | `ls` |
| README length | ~200 linhas | `README.md` |
| Last commit | 2026-04-06 | `git log -1` |

## Modules / Top-level Structure

| Module | Path | Type | Descrição |
|--------|------|------|-----------|
| core/bus | `core/bus/` | library | Message bus: Telegram I/O, inbox A2A, hooks |
| core/scripts | `core/scripts/` | library | agent-wrapper, fast-checker, generate-launchd, crash-alert |
| core/skills | `core/skills/` | library | Skills transversais (comms, cron-management) |
| agents/agent-template | `agents/agent-template/` | library | Template CLAUDE.md + config.json + skills |
| agents/aiox-master | `agents/aiox-master/` | app | Agent exemplo master |
| agents/frank | `agents/frank/` | app | Agent exemplo |
| agents/content-growth | `agents/content-growth/` | app | Agent exemplo |
| agents/marketing-dev | `agents/marketing-dev/` | app | Agent exemplo |
| agents/revenue-dev | `agents/revenue-dev/` | app | Agent exemplo |

## External Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| tmux | brew | Sessões persistentes terminal |
| jq | brew | Parse JSON Telegram callbacks |
| curl | system | HTTP client Telegram |
| Claude Code CLI | external | Execução do agent |
| launchd | macOS | Auto-restart + persistência |
| Telegram Bot API | external | Control plane humano |

## Entry Points

| Entry | Path | Command |
|-------|------|---------|
| Bootstrap | `bootstrap.sh` | `bash <(curl ... bootstrap.sh)` |
| Install | `install.sh` | `./install.sh` |
| Setup | `setup.sh` | `./setup.sh` |
| Wrapper daemon | `core/scripts/agent-wrapper.sh` | Invocado por launchd |
| Fast-checker daemon | `core/scripts/fast-checker.sh` | Invocado por agent-wrapper |

## Capabilities

### Core

| Capability | Evidence | Notes |
|------------|----------|-------|
| Persistent 24/7 session | `core/scripts/agent-wrapper.sh`, `generate-launchd.sh`, `bus/self-restart.sh` | launchd + tmux + auto-restart + 71h soft-reset |
| Telegram control plane | `core/bus/{send-telegram,check-telegram,send-voice}.sh` | Mensagens, callbacks, voz |
| Permission/Plan/Ask hooks | `core/bus/{hook-permission-telegram,hook-planmode-telegram,hook-ask-telegram}.sh`, `send-ask-question.sh` | Hooks do Claude Code → Telegram com Approve/Deny |
| Fast-checker daemon | `core/scripts/fast-checker.sh` | Poll Telegram+inbox → tmux send-keys; singleton mkdir-lock |
| Agent-to-agent message bus | `core/bus/{send-message,check-inbox,ack-inbox}.sh` | Inbox + priorities + inflight + redelivery 5min |
| Scheduled tasks (cron loops) | `core/skills/cron-management/`, `agents/agent-template/CLAUDE.md` | `/loop` dentro do agent + config.json |
| Multi-agent template | `agents/agent-template/`, `aiox-master/`, `frank/`, `content-growth/`, `marketing-dev/`, `revenue-dev/` | 1 template + 5 exemplos |
| Crash alerts | `core/scripts/crash-alert.sh` | Notifica Telegram em crash |
| Voice support | `core/bus/send-voice.sh` | Voice msgs |
| Instance ID isolation | `core/bus/send-message.sh` (CRM_INSTANCE_ID) | Múltiplas instalações em `~/.claude-remote/{id}` |

## Tests / Quality Signals

| Signal | Value | Evidence |
|--------|-------|----------|
| Test framework | none | — |
| Test file count | 0 | find |
| Linter | none | — |
| CI/CD | none | ausência de `.github/workflows` |

## Documentation

| Type | Path | Status |
|------|------|--------|
| README | `README.md` | rico, ~200 linhas |
| CONTRIBUTING | `CONTRIBUTING.md` | presente |
| Agent docs | `agents/*/CLAUDE.md` | per-agent |

## Extension Points

| Type | Where | How |
|------|-------|-----|
| Agents | `agents/<name>/` | dir isolado com CLAUDE.md + config.json + skills/ |
| Hooks | `core/bus/hook-*.sh` | Claude Code hooks |
| Skills | `agents/*/skills/`, `core/skills/` | Skills per-agent e globais |

## Notable Design Decisions

- **Zero-servidor** — tudo em bash+tmux+launchd na máquina host — evidência: `bootstrap.sh` + `core/scripts/`
- **At-least-once A2A** — inbox com ACK + redelivery 5min — evidência: `core/bus/send-message.sh` + `check-inbox.sh`
- **Singleton daemon** — `mkdir $LOCKDIR` atômico como lock (POSIX portable) — evidência: `core/scripts/fast-checker.sh`
- **Agent = diretório** — cada agent é um dir autocontido com CLAUDE.md + skills — evidência: `agents/*/`

## Limitations

- macOS-only (depende de launchd) — sem Linux/Windows
- Sem UI além de Telegram/terminal
- Sem CI, sem testes automatizados
- Stateless em disco fora do inbox — sem checkpoint rich
- Paralelismo = N tmux sessions independentes (sem fan-out coordenado)

## USPs

- **Persistência 24/7 real**: launchd + tmux + auto-restart + 71h soft-reset — agent nunca morre
- **Remote-first via Telegram**: approvals, plan, perguntas e voz no celular
- **A2A at-least-once**: inbox durável com ACK + redelivery
- **Zero servidor**: rodando inteiro em bash + tmux na máquina host
- **Agent = dir**: cada agent autocontido, config por-agent simples

---

_Generated by os-bench inventory task | Template v1.0_
