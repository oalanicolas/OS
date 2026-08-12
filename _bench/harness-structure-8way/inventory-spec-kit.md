# Inventory: spec-kit

**Generated:** 2026-08-12T18:00:00Z  
**Path:** `OS/spec-kit/`  
**Stack:** specify CLI, presets, extensions, workflows  
**License:** MIT  
**Confidence:** HIGH  
**Extraction:** filesystem-scan

> Specification-driven development: specs are the source of truth; commands + YAML workflows + gates generate the plan and the code.

## Metrics

- Files: 539 · SKILL.md count: 1 · README lines: 384
- Last commit: `2026-08-12T11:36:12-05:00`
- Source: https://github.com/github/spec-kit

## Capabilities

- **SDD command spine** (core): specify → plan → tasks → implement as markdown commands, not SKILL.md. — `OS/spec-kit/spec-driven.md`, `OS/spec-kit/templates/commands/specify.md`
- **YAML workflow + gates** (core): Steps can be commands or type: gate (approve/reject) with persisted state. — `OS/spec-kit/workflows/speckit/workflow.yml`, `OS/spec-kit/workflows/README.md`
- **Extension system** (extensibility): extension.yml adds namespaced speckit.<ext>.<cmd> commands, hooks, catalogs. — `OS/spec-kit/extensions/EXTENSION-DEVELOPMENT-GUIDE.md`
- **Agent-context overlay** (integration): Opt-in managed AGENTS.md/CLAUDE.md block — routing, not the encyclopedia. — `OS/spec-kit/extensions/agent-context/`
- **Presets and bundles** (extensibility): Role stacks compose extensions+presets; community catalog is discovery-only. — `OS/spec-kit/presets/`, `OS/spec-kit/docs/community/bundles.md`
- **Spec persistence models** (core): Declares flow-back / flow-forward / living-spec instead of silent drift. — `OS/spec-kit/docs/concepts/spec-persistence.md`

## Extension points

- Plugins: extension.yml + catalogs (`extensions/`)
- Hooks: after_specify/plan/tasks/implement
- MCP: client=False server=False

## USPs

- Specs invert power: code serves the spec
- First-class workflow gates
- Contrast case: structure without Agent Skills

## Limitations

- Almost no SKILL.md surface (1 file); discovery is slash commands — `OS/spec-kit/templates/commands/`
- No personas, org-chart, or skill bootstrap — `OS/spec-kit/spec-driven.md`

