# Inventário: superpowers

**Path:** `OS/superpowers/`
**Date:** 2026-04-19
**Extraction Method:** filesystem-scan + doc-scan
**Confidence:** HIGH

---

## Identity

| Field | Value |
|-------|-------|
| Slug | superpowers |
| Source URL | https://github.com/obra/superpowers |
| Primary language | Markdown (skills) + JS (hooks/plugin glue) |
| Secondary languages | Bash |
| Stack | Claude Code + OpenCode + Codex + Cursor + Gemini + Copilot plugins |
| License | MIT |
| Tagline | "Complete software-development methodology for coding agents — TDD red/green enforcement, YAGNI, DRY, subagent-driven execution, skills auto-trigger." |

## Key Metrics

| Metric | Value | Source |
|--------|-------|--------|
| LOC (md/js/sh) | 21,078 | `wc -l` |
| Files | 142 | filesystem scan |
| README length | 198 lines | `README.md` |
| Release notes | 58 KB | `RELEASE-NOTES.md` |
| Last commit | 2026-04-16 | `git log -1` |
| Plugin version | 5.0.7 | `.claude-plugin/plugin.json` |
| Runtime deps | 0 | `package.json` (zero-dep design) |

## Modules

| Module | Path | Type | Description |
|--------|------|------|-------------|
| skills | `skills/` | library | 14 composable skills that auto-trigger |
| commands | `commands/` | library | 3 slash commands (brainstorm, write-plan, execute-plan) |
| agents | `agents/` | library | code-reviewer agent |
| hooks | `hooks/` | library | session-start hook + hooks.json |
| .claude-plugin | `.claude-plugin/` | config | Claude Code plugin manifest + marketplace |
| .opencode | `.opencode/plugins/superpowers.js` | config | OpenCode plugin (package main) |
| .codex, .cursor-plugin | `.codex/`, `.cursor-plugin/` | config | Codex + Cursor plugin packaging |
| tests | `tests/` | library | Per-harness test dirs (claude-code, opencode, skill-triggering, subagent-driven-dev, etc.) |

## Entry Points

| Entry | Path | Command |
|-------|------|---------|
| Plugin install | `.claude-plugin/plugin.json` | `/plugin install superpowers@claude-plugins-official` |
| OpenCode plugin | `.opencode/plugins/superpowers.js` | OpenCode autoload |
| Slash command | `commands/brainstorm.md` | `/brainstorm` |
| Slash command | `commands/write-plan.md` | `/write-plan` |
| Slash command | `commands/execute-plan.md` | `/execute-plan` |

## Capabilities (observed)

### Core — TDD as the Iron Law

| Capability | Evidence | Notes |
|------------|----------|-------|
| Red/Green/Refactor enforcement | `OS/superpowers/skills/test-driven-development/SKILL.md` | "NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST"; "Write code before the test? Delete it. Start over." |
| Testing anti-patterns reference | `OS/superpowers/skills/test-driven-development/testing-anti-patterns.md` | Mock-only tests, test-only methods, mocking without understanding deps |
| Skill auto-triggering | `OS/superpowers/hooks/session-start/`, `skills/using-superpowers/` | Skills trigger automatically from session-start hook; user doesn't invoke manually |

### Core — Workflow skills

| Capability | Evidence | Notes |
|------------|----------|-------|
| Brainstorming (Socratic design) | `skills/brainstorming/`, `commands/brainstorm.md` | Teases spec from conversation; presents design in chunks |
| Writing plans (bite-sized tasks) | `skills/writing-plans/SKILL.md` | 2–5 min tasks, exact file paths, complete code, verification steps; "No placeholders" rule |
| Subagent-driven development | `skills/subagent-driven-development/SKILL.md` + `implementer-prompt.md` + `spec-reviewer-prompt.md` + `code-quality-reviewer-prompt.md` | Fresh subagent per task; spec-compliance review THEN code-quality review |
| Executing plans (batched) | `skills/executing-plans/` | Alternative for parallel sessions with checkpoints |
| Git worktrees | `skills/using-git-worktrees/` | Mandatory isolated workspace before implementation |
| Dispatching parallel agents | `skills/dispatching-parallel-agents/` | Concurrent subagent workflows |
| Systematic debugging | `skills/systematic-debugging/` | 4-phase root cause process |
| Verification before completion | `skills/verification-before-completion/` | Blocks "done" claim without verification |
| Requesting / receiving code review | `skills/requesting-code-review/`, `skills/receiving-code-review/`, `agents/code-reviewer.md` | Pre-review checklist + feedback loop |
| Finishing a dev branch | `skills/finishing-a-development-branch/` | Merge/PR/keep/discard workflow |

### Extensibility / Governance

| Capability | Evidence | Notes |
|------------|----------|-------|
| Writing skills (meta) | `skills/writing-skills/` | Create new skills with testing methodology |
| Zero-dependency design | `OS/superpowers/CLAUDE.md`, `package.json` | "Superpowers is a zero-dependency plugin by design"; 3rd-party deps rejected |
| Cross-harness plugin packaging | `.claude-plugin/`, `.opencode/`, `.codex/`, `.cursor-plugin/`, `gemini-extension.json` | 6 harnesses from one repo |

## Tests / Quality Signals

| Signal | Value | Evidence |
|--------|-------|----------|
| Test categories | 6 dirs | `tests/brainstorm-server`, `claude-code`, `explicit-skill-requests`, `opencode`, `skill-triggering`, `subagent-driven-dev` |
| CI | GitHub Actions | `.github/workflows/` |
| Plugin marketplace | Anthropic official | README (`/plugin install superpowers@claude-plugins-official`) |

## Unique Selling Points

- TDD enforced as Iron Law (delete code written before tests)
- Skills auto-trigger — user doesn't remember to invoke
- Subagent-driven with two-stage review (spec compliance → code quality)
- Zero runtime dependencies
- Available in Claude Code's official Anthropic marketplace

## Limitations

- No structured executable spec — spec is a design doc from brainstorming dialogue, not a typed artefact with IDs
- No drift detection / roundtripping — no skill tracks spec↔code divergence after plan execution
- Narrow command surface (3 slash commands) — relies on auto-triggering
- Strict PR policy: 94% PR rejection rate; contributor guidelines in CLAUDE.md

---

_Generated by os-bench inventory task | Template v1.0_
