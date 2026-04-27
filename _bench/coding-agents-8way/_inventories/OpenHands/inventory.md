# Inventário: OpenHands

**Path:** `OS/OpenHands/`
**Date:** 2026-04-19
**Extraction Method:** filesystem-scan + doc-scan
**Confidence:** HIGH

---

## Identity

| Field | Value |
|-------|-------|
| Slug | OpenHands |
| Source URL | https://github.com/OpenHands/OpenHands |
| Primary language | Python |
| Secondary languages | TypeScript (frontend) |
| Stack | Python 3.12-3.14, Poetry, FastAPI, Docker, Kubernetes, React |
| License | MIT (core) + source-available (enterprise/) |
| Tagline | AI-Driven Development — SDK + CLI + GUI + Cloud + Enterprise; SWE-bench 77.6 |

## Key Metrics

| Metric | Value | Source |
|--------|-------|--------|
| LOC (ballpark) | ~200k (python) | find openhands |
| Files .py | 484 | find openhands |
| Top-level dirs | openhands, frontend, enterprise, tests, skills, third_party, containers, dev_config, openhands-ui, kind | ls |
| README length | 153 | wc -l |
| Last commit | 2026-04-19 | git log |
| CI workflows | 19 | .github/workflows |
| SWE-bench | 77.6 | README.md:11 badge |

## Modules / Top-level Structure

| Module | Path | Type | Loc estimate | Description |
|--------|------|------|--------------|-------------|
| openhands | `openhands/` | package | ~180k | Core: agenthub/, controller/, events/, runtime/, memory/, llm/, mcp/, resolver/, security/, server/, integrations/ |
| frontend | `frontend/` | app | ~40k | React SPA |
| enterprise | `enterprise/` | service | ~30k | Source-available enterprise |
| skills | `skills/` | library | — | Skill system |
| tests | `tests/` | library | ~20k | e2e, runtime, unit |

## External Dependencies (top 10)

| Package | Version | Purpose |
|---------|---------|---------|
| anthropic[vertex] | — | LLM |
| litellm | >=1.74.3 | Roteador LLM |
| fastapi | — | HTTP API |
| mcp | >=1.25 | MCP protocol |
| fastmcp | >=3.2,<4 | MCP helpers |
| docker | — | Runtime sandbox |
| kubernetes | >=33.1 | K8s deploy |
| playwright | >=1.55 | Browser agent |
| sqlalchemy[asyncio] | >=2.0.40 | ORM |
| redis | >=5.2,<7 | State |

## Entry Points

| Entry | Path | Command |
|-------|------|---------|
| CLI | `openhands/` | openhands CLI (docs.openhands.dev/openhands/usage/run-openhands/cli-mode) |
| HTTP server | `openhands/server/` | FastAPI |
| SDK | `openhands-sdk==1.17` | pip install openhands-ai |

## Capabilities (observed)

### Core Capabilities

| Capability | Evidence | Notes |
|------------|----------|-------|
| AgentHub (6 agents) | `OS/OpenHands/openhands/agenthub/` | browsing_agent, codeact_agent, dummy_agent, loc_agent, readonly_agent, visualbrowsing_agent |
| Runtime sandbox | `OS/OpenHands/openhands/runtime/` + `docker-compose.yml` | Docker/K8s isolation |
| Controller + events | `OS/OpenHands/openhands/controller/` + `events/` | Event-driven loop |
| Memory system | `OS/OpenHands/openhands/memory/` | Persistent memory |
| MCP client+server | `OS/OpenHands/openhands/mcp/` | fastmcp >=3.2 |

### Optional/Extensibility

| Capability | Evidence | Notes |
|------------|----------|-------|
| Microagents | `OS/OpenHands/openhands/microagent/` | Small specialized agents |
| Skills | `OS/OpenHands/skills/` | Skill system |
| Resolver (issue→PR) | `OS/OpenHands/openhands/resolver/` | Auto PR from issue |
| Integrations | `OS/OpenHands/openhands/integrations/` | Slack, Jira, Linear |
| Security | `OS/OpenHands/openhands/security/` | Security layer |
| Enterprise (k8s) | `OS/OpenHands/enterprise/`, `kind/` | VPC deploy |

## Tests / Quality Signals

| Signal | Value | Evidence |
|--------|-------|----------|
| Test framework | pytest + pytest-asyncio + pytest-playwright | `pytest.ini`, `pyproject.toml` |
| Linter | ruff 0.12.5 + mypy 1.17 | `pyproject.toml` |
| CI | GitHub Actions | 19 workflows (py-tests, e2e-tests, fe-e2e, fe-unit, resolver, pypi-release, enterprise-check-migrations etc.) |

## Documentation

| Type | Path | Status |
|------|------|--------|
| README | `README.md` | 153 linhas, estruturado |
| Development | `Development.md` | presente |
| Architecture | `openhands/architecture/` | presente |
| Tech report | arxiv.org/abs/2511.03690 | README.md:14 |

## Extension Points

| Extension Type | Where | How to extend |
|----------------|-------|---------------|
| Agents | `openhands/agenthub/` | Add subdir |
| Microagents | `openhands/microagent/` | Registrar |
| Skills | `skills/` | — |
| MCP | `openhands/mcp/` | fastmcp server |
| Runtime | `openhands/runtime/` | Daytona/E2B/Modal/Runloop optional |

## Notable Design Decisions

- Deploy ladder: SDK → CLI → Local GUI → Cloud → Enterprise
- Sandbox docker/k8s nativo pra segurança
- 6 agents especializados no AgentHub
- Browser automation de primeira classe (Playwright + browsing agents)

## Limitations

- Enterprise requer licença paga após 1 mês — `README.md:68-69`
- Setup docker/k8s mais pesado que concorrentes CLI-only

## Unique Selling Points

- Único com deploy ladder SDK→Enterprise no benchmark
- SWE-bench 77.6 badge oficial
- Sandbox docker/k8s nativo
- Integrations corp (Slack/Jira/Linear)
- Browser agents nativos (visualbrowsing, browsing)
- RBAC + multi-user em Cloud/Enterprise
- Tech report arxiv (único com paper)

---

_Generated by os-bench inventory task | Template v1.0_
