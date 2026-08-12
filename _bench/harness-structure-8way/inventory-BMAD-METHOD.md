# Inventory: BMAD-METHOD

**Generated:** 2026-08-12T18:00:00Z  
**Path:** `OS/BMAD-METHOD/`  
**Stack:** Node installer, uv/Python skill scripts, IDE skill trees  
**License:** MIT  
**Confidence:** HIGH  
**Extraction:** filesystem-scan

> Agile AI-driven development: named personas + numbered phase skills turn an idea into working software without dropping the thinking.

## Metrics

- Files: 596 · SKILL.md count: 58 · README lines: 94
- Last commit: `2026-08-11T16:51:20-07:00`
- Source: https://github.com/bmad-code-org/BMAD-METHOD

## Capabilities

- **Named persona skills** (core): Winston/John/Amelia etc. with 3-layer TOML merge and a menu that dispatches other skills. — `OS/BMAD-METHOD/src/bmm-skills/agents/bmad-agent-architect/SKILL.md`, `OS/BMAD-METHOD/src/bmm-skills/agents/bmad-agent-architect/customize.toml`
- **Party Mode** (core): session/auto/subagent/agent-team roundtables; memlog is dynamics not transcript. — `OS/BMAD-METHOD/src/core-skills/bmad-party-mode/SKILL.md`
- **Numbered agile pipeline** (core): Analysis → PRD/UX/SPEC → architecture/epics → build/review, each as a skill with steps/. — `OS/BMAD-METHOD/src/bmm-skills/plan/`, `OS/BMAD-METHOD/src/bmm-skills/ship/`
- **Skill validator** (governance): Deterministic CI validator for skill frontmatter and structure. — `OS/BMAD-METHOD/tools/validate-skills.js`
- **Persistent facts + project-context** (core): file: globs and literal facts loaded on persona activation. — `OS/BMAD-METHOD/src/bmm-skills/agents/bmad-agent-architect/customize.toml`
- **Customization layers** (extensibility): skill default → team toml → user toml. — `OS/BMAD-METHOD/src/bmm-skills/agents/bmad-agent-architect/SKILL.md`

## Extension points

- Plugins: customize.toml + install into IDE skill trees (`src/`)
- Hooks: activation_steps_prepend/append
- MCP: client=False server=False

## USPs

- Personas you talk to, not agent-3
- YAML+MD skill DSL with a validator
- Party Mode is for disagreement, not consensus

## Limitations

- No own runtime state backend — lives in the host IDE — `OS/BMAD-METHOD/README.md`
- No token budgets, no plugin marketplace — `OS/BMAD-METHOD/src/core-skills/`

