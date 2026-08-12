# Inventory: hermes-agent

**Generated:** 2026-08-12T18:00:00Z  
**Path:** `OS/hermes-agent/`  
**Stack:** Python agent core, desktop/TUI/web apps, plugin.yaml  
**License:** MIT  
**Confidence:** HIGH  
**Extraction:** filesystem-scan

> Self-improving personal/coding agent with a cataloged skill library, skill bundles, and kinded plugins.

## Metrics

- Files: 8752 · SKILL.md count: 194 · README lines: 264
- Last commit: `2026-08-12T20:19:26+05:30`
- Source: https://github.com/NousResearch/hermes-agent

## Capabilities

- **Hardline skill authoring** (core): ≤60-char description, platforms, tests, docs generator; bundled vs optional tier. — `OS/hermes-agent/skills/software-development/hermes-agent-skill-authoring/SKILL.md`
- **Skill index + skill_view** (core): Compact index always; full body via skill_view or slash; YAML bundles load N skills. — `OS/hermes-agent/agent/skill_utils.py`, `OS/hermes-agent/agent/skill_bundles.py`
- **Kinded plugins** (extensibility): plugin.yaml under memory/, model-providers/, platforms/, context_engine/… — `OS/hermes-agent/plugins/`
- **Micro-compaction** (core): Compacts agent narration; never compact user messages. Prompt-cache stability is sacred. — `OS/hermes-agent/docs/micro-compaction.md`
- **Project context caps** (core): First-match .hermes.md → AGENTS.md → CLAUDE.md, 20k cap. — `OS/hermes-agent/skills/autonomous-ai-agents/hermes-agent/references/project-context-files.md`
- **No router skills** (governance): A skill whose only job is pointing at siblings is rejected. — `OS/hermes-agent/skills/software-development/hermes-agent-skill-authoring/SKILL.md`

## Extension points

- Plugins: plugin.yaml kinds + $HERMES_HOME/plugins (`plugins/`)
- Hooks: gateway builtin_hooks + cron
- MCP: client=True server=True

## USPs

- Largest in-repo skill library with a real validator/review bar
- Skill bundles as first-class composition
- User text is never compacted

## Limitations

- Squad model is delegate_task, not a persistent org — `OS/hermes-agent/agent/`
- Description 60-char hardline trades trigger richness for listing budget — `OS/hermes-agent/skills/software-development/hermes-agent-skill-authoring/SKILL.md`

