# Inventário: BMAD-METHOD

**Path:** `OS/BMAD-METHOD/`
**Date:** 2026-04-19
**Extraction Method:** filesystem-scan + doc-scan
**Confidence:** HIGH

---

## Identity

| Field | Value |
|-------|-------|
| Slug | BMAD-METHOD |
| Source URL | https://github.com/bmad-code-org/BMAD-METHOD |
| Primary language | JavaScript |
| Secondary languages | Markdown, YAML |
| Stack | Node.js >=20, bmad-cli (commander/clack), Astro docs site, Python >=3.10 opcional |
| License | MIT |
| Tagline | Breakthrough Method of Agile AI-driven Development — pipeline agentic escalável (analyst → PM → architect → dev → QA). |

## Key Metrics

| Metric | Value | Source |
|--------|-------|--------|
| LOC (JS/TS) | 18.493 | `wc -l` |
| Files | 544 | filesystem scan |
| Top-level dirs | 5 | filesystem scan |
| README length | ~200 linhas | `README.md` |
| Docs pages | ~50+ | `docs/` |
| Last commit | 2026-04-19 | `git log -1` |
| GitHub stars | n/d local (public repo, stars visíveis em npm/github badges no README) | npm badge |

## Modules / Top-level Structure

| Module | Path | Type | Descrição |
|--------|------|------|-----------|
| bmm-skills | `src/bmm-skills/` | library | Pipeline agile — 4 fases numeradas |
| core-skills | `src/core-skills/` | library | Skills transversais (party-mode, brainstorm, review, help) |
| installer | `tools/installer/bmad-cli.js` | app | CLI `npx bmad-method install` |
| website | `website/` | app | Docs site Astro/Starlight |
| test | `test/` | library | Testes de instalação e refs |

## External Dependencies (top 10)

| Package | Version | Purpose |
|---------|---------|---------|
| @clack/prompts | ^1.0.0 | Prompts interativos no installer |
| commander | ^14.0.0 | CLI arg parsing |
| glob | ^11.0.3 | File globs na instalação |
| js-yaml | ^4.1.0 | Parse de skills/workflows YAML |
| yaml | ^2.7.0 | YAML writer |
| chalk | ^4.1.2 | Terminal colors |
| semver | ^7.6.3 | Versionamento de módulos |
| xml2js | ^0.6.2 | Parse de prompts XML |
| csv-parse | ^6.1.0 | Skill manifests CSV |
| @kayvan/markdown-tree-parser | ^1.6.1 | Parse de docs |

## Entry Points

| Entry | Path | Command |
|-------|------|---------|
| CLI | `tools/installer/bmad-cli.js` | `npx bmad-method install` |
| npm bin | `package.json#bin` | `bmad` / `bmad-method` |

## Capabilities (observed)

### Core

| Capability | Evidence | Notes |
|------------|----------|-------|
| 4-phase agile pipeline | `OS/BMAD-METHOD/src/bmm-skills/{1-analysis,2-plan-workflows,3-solutioning,4-implementation}/` | Workflow sequencial explícito |
| Specialized agent roles (12+) | `src/bmm-skills/1-analysis/bmad-agent-analyst/`, `src/bmm-skills/4-implementation/bmad-agent-dev/` | PM, Architect, Dev, Analyst, Tech Writer, etc. |
| Party Mode (multi-agent roundtable) | `src/core-skills/bmad-party-mode/SKILL.md` | Spawna subagents paralelos via tool Agent |
| Brainstorming / elicitation | `src/core-skills/bmad-brainstorming/`, `src/core-skills/bmad-advanced-elicitation/` | Skills pre-código |
| Adversarial review + edge case | `src/core-skills/bmad-review-adversarial-general/`, `src/core-skills/bmad-review-edge-case-hunter/` | Review agressivo via subagents |

### Extensibility / Governance

| Capability | Evidence | Notes |
|------------|----------|-------|
| Skills system (YAML+MD) | `src/core-skills/`, `tools/validate-skills.js` | Cada capability é skill validada |
| bmad-help onboarding | `src/core-skills/bmad-help/` | Next-step guidance |
| Deterministic skill validator | `tools/validate-skills.js`, `tools/skill-validator.md` | Lint estrito no CI |
| Installer + module ecosystem | `tools/installer/bmad-cli.js`, `package.json#bin` | Módulos externos (BMM, BMB, TEA, etc.) |

## Tests / Quality Signals

| Signal | Value | Evidence |
|--------|-------|----------|
| Test framework | jest + custom node scripts | `package.json#devDependencies` |
| Test file count | 5 | `test/` |
| Linter | eslint + markdownlint-cli2 + prettier | `package.json` + `eslint.config.mjs` |
| CI/CD | GitHub Actions | `.github/workflows/{quality,publish,docs,discord,coderabbit-review}.yaml` |

## Documentation

| Type | Path | Status |
|------|------|--------|
| README | `README.md` | rico, ~200 linhas |
| CONTRIBUTING | `CONTRIBUTING.md` | presente |
| Architecture docs | `docs/` | presente (concepts, tutorials, how-to, reference) |
| Agents doc | `AGENTS.md` | presente |

## Extension Points

| Type | Where | How |
|------|-------|-----|
| Modules externos | npm packages (BMM, BMB, TEA, BMGD, CIS) | `npx bmad-method install --modules <name>` |
| Skills custom | `src/*-skills/{name}/SKILL.md` | Frontmatter YAML + MD, validado |
| Husky hooks | `.husky/` + package.json `lint-staged` | pre-commit |

## Notable Design Decisions

- **Pipeline numerada** — fases 1-4 são diretórios — evidência: `src/bmm-skills/`
- **Subagents reais** — Party Mode invoca Agent tool (processos LLM independentes) — evidência: `src/core-skills/bmad-party-mode/SKILL.md`
- **Scale-adaptive** — workflow ajusta profundidade — evidência: README "adjusts from bug fixes to enterprise systems"

## Limitations / Known

- Sem observabilidade embutida (depende do IDE host)
- Sem runtime próprio — é um pacote de skills; execução ocorre no Claude Code/Cursor
- Delegation é editorial (MD), não programática

## Unique Selling Points

- Pipeline agile explícita com skills numeradas
- Scale-adaptive (bug fix → enterprise)
- Party Mode com subagents independentes reais
- Instalação single-command e integração nativa com Claude Code / Cursor

---

## Extraction Notes

- Scanned directories: `src/`, `tools/`, `docs/`, `test/`, `website/`
- Skipped: `node_modules`, `.git`
- Data sources: filesystem 100%
- Tools used: ls, wc, find, grep, Read

---

_Generated by os-bench inventory task | Template v1.0_
