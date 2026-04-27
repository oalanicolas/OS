# Inventário: get-shit-done

**Path:** `OS/get-shit-done/`
**Date:** 2026-04-19
**Extraction Method:** filesystem-scan + doc-scan
**Confidence:** HIGH

---

## Identity

| Field | Value |
|-------|-------|
| Slug | get-shit-done |
| Source URL | https://github.com/gsd-build/get-shit-done |
| Primary language | JavaScript/TypeScript |
| Secondary languages | Markdown, Bash |
| Stack | Node.js, Vitest, TS SDK, Claude Code + 13 other harnesses |
| License | MIT |
| Tagline | "Light-weight and powerful meta-prompting, context engineering and spec-driven development system — solves context rot." |

## Key Metrics

| Metric | Value | Source |
|--------|-------|--------|
| LOC (py/ts/js/md) | 146,206 | `wc -l` |
| Files | 808 | filesystem scan |
| README length | 928 lines | `README.md` |
| CHANGELOG | 126 KB | `CHANGELOG.md` |
| Last commit | 2026-04-19 | `git log -1` |
| Tests | 213+ vitest files | `tests/` |
| npm version | 1.37.1 | `package.json` |

## Modules

| Module | Path | Type | Description |
|--------|------|------|-------------|
| commands | `commands/gsd/` | library | 100+ slash commands |
| agents | `agents/` | library | 32 specialised subagents |
| hooks | `hooks/` | library | 12 runtime hooks |
| workflows | `get-shit-done/workflows/` | library | Workflow definitions backing command files |
| templates | `get-shit-done/templates/` | library | 40+ artefact templates (spec, requirements, phase-prompt, UI-SPEC, AI-SPEC, SECURITY, UAT, VALIDATION, ...) |
| references | `get-shit-done/references/` | library | 50+ reference docs (thinking-models, gates, TDD, context-budget, ...) |
| sdk | `sdk/` | package | TypeScript SDK |
| bin/install.js | `bin/install.js` | app | Installer across 14 runtimes |

## Entry Points

| Entry | Path | Command |
|-------|------|---------|
| Installer | `bin/install.js` | `npx get-shit-done-cc@latest` |
| Spec phase | `commands/gsd/spec-phase.md` | `/gsd-spec-phase <N>` |
| Discuss phase | `commands/gsd/discuss-phase.md` | `/gsd-discuss-phase <N>` |
| Plan phase | `commands/gsd/plan-phase.md` | `/gsd-plan-phase <N>` |
| Execute phase | `commands/gsd/execute-phase.md` | `/gsd-execute-phase <N>` |
| Verify | `commands/gsd/verify-work.md` | `/gsd-verify-work` |
| Autonomous | `commands/gsd/autonomous.md` | `/gsd-autonomous [--auto|--to N|--interactive]` |
| Brownfield | `commands/gsd/map-codebase.md` | `/gsd-map-codebase` |

## Capabilities (observed)

### Core

| Capability | Evidence | Notes |
|------------|----------|-------|
| Ambiguity-scored Socratic spec phase | `OS/get-shit-done/get-shit-done/workflows/spec-phase.md` | 4-dim weighted score (Goal 35% / Boundary 25% / Constraint 20% / Acceptance 20%) with gate ≤0.20 |
| Falsifiable requirements | `OS/get-shit-done/get-shit-done/templates/spec.md` | Current / Target / Acceptance per requirement |
| Spec → Discuss → Plan → Execute → Verify pipeline | `commands/gsd/{spec,discuss,plan,execute,verify}-*.md` | 5-stage pipeline with locked upstream artefacts |
| 32 subagents | `agents/` | Planner, Executor, Verifier, Debugger, Code-fixer, Code-reviewer, 5x Researcher, Security-auditor, Eval-auditor/planner, Nyquist-auditor, UI agents, Doc agents, etc. |
| Autonomous mode with checkpoints | `commands/gsd/autonomous.md` | `--auto --to N --interactive` |
| Vitest suite (213+ files) | `tests/`, `vitest.config.ts` | Agent frontmatter, architecture-counts, atomic writes, anti-pattern enforcement, ai-evals, ... |

### Governance

| Capability | Evidence | Notes |
|------------|----------|-------|
| Context rot mitigation | `OS/get-shit-done/hooks/gsd-context-monitor.js`, `docs/context-monitor.md` | Active context-window monitoring + thinning |
| Nyquist auditor | `OS/get-shit-done/agents/gsd-nyquist-auditor.md` | Dedicated subagent for context-compression quality |
| Schema drift detection | `OS/get-shit-done/docs/FEATURES.md:79,1440` | Gate blocks execute if ORM changes missing migrations |
| STATE.md filesystem drift detection | `OS/get-shit-done/docs/FEATURES.md:1635-1650` | REQ-STATE-01: `state validate` + Sync from disk |
| Scope reduction detection | `OS/get-shit-done/docs/FEATURES.md` | Flags silent requirement drops between SPEC and plan |
| Security enforcement gate | `agents/gsd-security-auditor.md`, `get-shit-done/templates/SECURITY.md` | Anchors verification to threat model |
| Agent size-budget enforcement | `tests/agent-size-budget.test.cjs` | XL/Large/Default limits enforced in CI |

### Integration

| Capability | Evidence | Notes |
|------------|----------|-------|
| Multi-runtime installer (14+) | `bin/install.js`, `docs/CLI-TOOLS.md` | Claude Code, OpenCode, Codex, Gemini CLI, Cursor, Windsurf, Kilo, Copilot, Antigravity, Augment, Trae, Qwen, Cline, CodeBuddy |
| Cross-AI peer review / execution delegation | `docs/FEATURES.md`, `commands/gsd/code-review.md` | Multiple AI providers can review/execute |
| TypeScript SDK | `sdk/` | Programmatic primitives |
| Brownfield codebase map | `commands/gsd/map-codebase.md`, `commands/gsd/scan.md` | Seed planning context from existing repo |

### UX / Governance continued

| Capability | Evidence | Notes |
|------------|----------|-------|
| Response language i18n | `docs/FEATURES.md#83-response-language-config` | User-facing text localised while code/paths stay English |
| UI design contract | `commands/gsd/ui-phase.md`, `templates/UI-SPEC.md` | UI-SPEC artefact with UI auditor/checker/researcher agents |
| AI integration phase | `commands/gsd/ai-integration-phase.md`, `templates/AI-SPEC.md` | AI-SPEC + eval planner/auditor |
| Spike / sketch exploration | `commands/gsd/{spike,sketch,spike-wrap-up,sketch-wrap-up}.md` | 2–5 experiments or 2–3 interactive HTML mockups |
| Extract learnings | `commands/gsd/extract_learnings.md` | Global learnings store across sessions |

## Tests / Quality Signals

| Signal | Value | Evidence |
|--------|-------|----------|
| Test framework | vitest | `vitest.config.ts` |
| Test files | 213+ | `tests/` |
| CI | GitHub Actions | `.github/workflows/` |
| Hooks | 12 | `hooks/` |
| Commands | ~100 | `commands/gsd/` |
| Agents | 32 | `agents/` |
| References | 50+ | `get-shit-done/references/` |

## Unique Selling Points

- Solves "context rot" explicitly via context-monitor hook + Nyquist auditor
- Meta-prompting with XML-formatted prompts + 32 subagents + state management
- Falsifiable requirements with ambiguity-scoring gate (4 weighted dimensions)
- Two drift-detection layers (schema drift + STATE.md drift)
- 14+ coding harnesses from a single npm package

## Limitations

- No executable-spec → test generation; acceptance criteria are pass/fail checkboxes, not auto-generated failing tests
- Installer-driven copy model (not a native plugin in the host runtime)
- Spec format is GSD-specific; not aligned with spec-kit's FR-###/SC-### IDs

---

_Generated by os-bench inventory task | Template v1.0_
