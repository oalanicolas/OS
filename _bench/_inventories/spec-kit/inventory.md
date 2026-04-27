# Inventário: spec-kit

**Path:** `OS/spec-kit/`
**Date:** 2026-04-19
**Extraction Method:** filesystem-scan + doc-scan
**Confidence:** HIGH

---

## Identity

| Field | Value |
|-------|-------|
| Slug | spec-kit |
| Source URL | https://github.com/github/spec-kit |
| Primary language | Python (CLI) + Markdown (templates) |
| Secondary languages | Bash, PowerShell |
| Stack | Typer, Rich, PyYAML, Hatchling |
| License | MIT |
| Tagline | "Build high-quality software faster — open-source toolkit for Spec-Driven Development where specifications become executable." |

## Key Metrics

| Metric | Value | Source |
|--------|-------|--------|
| LOC (py/ts/js/md) | 51,903 | `wc -l` |
| Files | 262 | filesystem scan |
| README length | 778 lines | `README.md` |
| SDD manifesto | 412 lines | `spec-driven.md` |
| Last commit | 2026-04-17 | `git log -1` |
| Tests | 13 pytest files | `tests/` |
| Python version | >=3.11 | `pyproject.toml` |

## Modules

| Module | Path | Type | Description |
|--------|------|------|-------------|
| specify_cli | `src/specify_cli/` | app | Python CLI that bootstraps SDD, integrates 12+ agents |
| templates | `templates/` | library | spec/plan/tasks/constitution/checklist templates |
| commands-templates | `templates/commands/` | library | 9 slash-command templates (specify, clarify, plan, tasks, implement, analyze, checklist, constitution, taskstoissues) |
| extensions | `extensions/` | library | Extension catalog + hooks mechanism |
| presets | `presets/` | library | Stack presets |
| scripts | `scripts/bash`, `scripts/powershell/` | library | Helper scripts |
| tests | `tests/` | library | Pytest covering CLI, extensions, presets, workflows |

## Entry Points

| Entry | Path | Command |
|-------|------|---------|
| CLI | `src/specify_cli/__init__.py` | `specify` |
| Bootstrap | — | `uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@vX.Y.Z` |
| Slash command | `templates/commands/specify.md` | `/speckit.specify` |
| Slash command | `templates/commands/plan.md` | `/speckit.plan` |
| Slash command | `templates/commands/tasks.md` | `/speckit.tasks` |
| Slash command | `templates/commands/implement.md` | `/speckit.implement` |
| Slash command | `templates/commands/analyze.md` | `/speckit.analyze` |

## Capabilities (observed)

### Core

| Capability | Evidence | Notes |
|------------|----------|-------|
| Executable spec format (US#, FR-###, SC-###, Edge Cases, Assumptions, Key Entities) | `OS/spec-kit/templates/spec-template.md` | Mandatory sections enforced by `/speckit.specify` |
| SDD manifesto | `OS/spec-kit/spec-driven.md` | 412 lines on "specifications as the lingua franca" |
| Spec → Plan → Tasks pipeline | `OS/spec-kit/templates/commands/{specify,plan,tasks}.md` | 3-stage generation with locked artefact names |
| Requirement IDs | `OS/spec-kit/templates/spec-template.md` | FR-### functional, SC-### success criteria, US# user stories |
| Consistency analyzer | `OS/spec-kit/templates/commands/analyze.md` | `/speckit.analyze` cross-validates spec/plan/tasks |
| Clarify loop (max 3 markers) | `OS/spec-kit/templates/commands/clarify.md` | [NEEDS CLARIFICATION] markers, interactive resolution |
| Quality checklist per spec | `OS/spec-kit/templates/checklist-template.md` | Auto-generated checklist validated each run |

### Governance / Integration

| Capability | Evidence | Notes |
|------------|----------|-------|
| Constitution file | `OS/spec-kit/templates/constitution-template.md` | Gates enforced in `plan.md` (Constitution Check) |
| tasks → GitHub issues | `OS/spec-kit/templates/commands/taskstoissues.md` | Export tasks to issue tracker |
| 12+ AI-agent harnesses | `OS/spec-kit/AGENTS.md`, `src/specify_cli/agents.py` | Copilot, Claude, Cursor, Gemini, Codex, Qwen, Windsurf, Trae, Kilo, CodeBuddy, Augment, opencode |

### Extensibility

| Capability | Evidence | Notes |
|------------|----------|-------|
| Extension hooks | `src/specify_cli/extensions.py`, `templates/commands/specify.md` | `.specify/extensions.yml` with before/after_specify, before/after_plan |
| Presets | `presets/`, `src/specify_cli/presets.py` | Stack packs applied at init |
| Air-gapped wheel assets | `pyproject.toml` | Templates/commands/scripts bundled in wheel |

## Tests / Quality Signals

| Signal | Value | Evidence |
|--------|-------|----------|
| Test framework | pytest | `tests/conftest.py`, `pyproject.toml` |
| Test files | 13 | `tests/*.py` |
| CI | GitHub Actions | `.github/workflows/` |
| Linting | markdownlint-cli2 | `.markdownlint-cli2.jsonc` |

## Unique Selling Points

- Canonical SDD methodology (spec-driven.md manifesto + concrete template set with FR/SC IDs)
- 12+ AI-agent harnesses from a single CLI
- Offline install via bundled wheel assets
- GitHub-native workflow (tasks→issues export)

## Limitations / Known Issues

- No automatic code→spec roundtripping; drift detection is explicit (`/speckit.analyze`), not continuous
- Tests in generated specs are optional by default — `tasks-template.md:11` states "only include them if explicitly requested"
- TDD is not enforced — it is the implementing agent's discipline

---

_Generated by os-bench inventory task | Template v1.0_
