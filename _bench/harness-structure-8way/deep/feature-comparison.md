# Deep: feature comparison (harness-structure-8way)

Companion to `comparison-matrix.md`. Depth on the five atoms that actually move complex work.

## 1. Discovery surface

| Mechanism | Who | Always-on cost | Failure mode |
|---|---|---|---|
| SessionStart body inject | superpowers | 1 skill body | If hook missing, pack is inert |
| Generated preamble + router | gstack | large | Rot; host listing + preamble |
| XML `<available_skills>` | gsd-pi | name+desc | Truncation if too many user skills |
| Persona menu | BMAD | activation facts | User must invoke Winston |
| Heartbeat → skill | paperclip | issue payload | CEO that ICs anyway |
| Compact index + slash | hermes | ≤60c × N | Invoke still optional |
| Catalog + caps + `$refs` | openclaw | 18k max | Silent drop if you ignore the warning |
| Slash commands | spec-kit | command file on invoke | Invisible to SKILL.md-only hosts |

## 2. Who thinks independently

- **Fresh child, constructed prompt:** superpowers, gsd-pi (default `context: fresh`).
- **Independent voice, shared artifact:** gstack dual-voice; BMAD `subagent`/`agent-team`.
- **Separate process + adapter:** paperclip.
- **Same mind, many labels:** BMAD `session` party; cheap and correlated.

## 3. Where truth lives

| SoT | Who |
|---|---|
| Plan + ledger | superpowers |
| Design doc + ~/.gstack/projects | gstack |
| `.gsd/` checkboxes | gsd-pi |
| PRD / arch / stories | BMAD |
| Issue tree | paperclip |
| `.hermes/plans` + memory plugins | hermes |
| MEMORY.md vs daily | openclaw / clawd |
| spec.md / plan.md / tasks.md | spec-kit |

Chat is never the SoT in anyone who scores 80+ on handoff.

## 4. What a “plugin” is allowed to add

```
superpowers   skills + one hook
gstack        generated skills + host rewrite + daemon
gsd-pi         extension manifest + MCP
BMAD          customize.toml + more skills
paperclip     UI + API routes + adapters + catalogs
hermes        kinded plugin.yaml + MCP + skill bundles
openclaw      providers, channels, tools, hooks, HTTP, skills, MCP, exclusive slots
spec-kit      namespaced commands + lifecycle hooks + catalogs
```

Core tool schemas should stay narrow (hermes AGENTS.md). Every core tool is paid every turn.

## 5. Composition styles

| Style | Example | Load cost |
|---|---|---|
| Named REQUIRED SUB-SKILL | superpowers | 0 until invoked |
| Read sibling SKILL.md, skip preamble | gstack autoplan | 4 bodies, sequential |
| YAML bundle = N bodies | hermes | N bodies in one slash |
| `$a $b` refs (max 8) | openclaw | model must Read each |
| TEAM requiredSkills | paperclip | catalog + persona |
| Workflow YAML + gate | spec-kit | command-sized |
| Router skill that only points | hermes **forbids** | wasted hop |
