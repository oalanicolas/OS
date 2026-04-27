# Inventário: crewAI

**Path:** `OS/crewAI/`
**Date:** 2026-04-19
**Extraction Method:** filesystem-scan + doc-scan
**Confidence:** HIGH

---

## Identity

| Field | Value |
|-------|-------|
| Slug | crewAI |
| Source URL | https://github.com/crewAIInc/crewAI |
| Primary language | Python |
| Secondary languages | Markdown |
| Stack | Python 3.10–3.12, Pydantic 2, LiteLLM, OpenTelemetry, ChromaDB, uv |
| License | MIT |
| Tagline | Framework de orquestração de agentes autônomos role-playing (Crew = time com papéis + tasks). |

## Key Metrics

| Metric | Value | Source |
|--------|-------|--------|
| LOC (Python) | 23.651 | `wc -l` |
| Files | 500 | filesystem scan |
| Top-level dirs | 3 | `ls` |
| README length | ~300 linhas | `README.md` |
| Docs pages | ~30 | `docs/` mkdocs |
| Last commit | 2024-12-22 (snapshot local) | `git log -1` |

## Modules / Top-level Structure

| Module | Path | Type | Descrição |
|--------|------|------|-----------|
| crewai | `src/crewai/` | package | Core package — Agent, Crew, Task, Process, Flow |
| memory | `src/crewai/memory/` | library | Short/long/entity/user memory + storage |
| flow | `src/crewai/flow/` | library | Orquestração graph-based com visualizer HTML |
| cli | `src/crewai/cli/` | app | `crewai create crew <project>` |
| telemetry | `src/crewai/telemetry/` | library | OpenTelemetry wiring |
| tests | `tests/` | library | Pytest suite (43 arquivos) |

## External Dependencies (top 10)

| Package | Version | Purpose |
|---------|---------|---------|
| pydantic | >=2.4.2 | Core models |
| openai | >=1.13.3 | LLM client default |
| litellm | >=1.44.22 | Multi-provider routing |
| chromadb | >=0.5.23 | Vector store (memory) |
| opentelemetry-sdk | >=1.22.0 | Telemetry |
| instructor | >=1.3.3 | Structured outputs |
| click | >=8.1.7 | CLI |
| auth0-python | >=4.7.1 | Tools enterprise |
| pyvis | >=0.3.2 | Flow visualization |
| pdfplumber | >=0.11.4 | Knowledge source PDF |

## Entry Points

| Entry | Path | Command |
|-------|------|---------|
| CLI | `src/crewai/cli/cli.py` | `crewai create crew <project>` |
| Python API | `src/crewai/crew.py` | `from crewai import Crew, Agent, Task` |

## Capabilities

### Core

| Capability | Evidence | Notes |
|------------|----------|-------|
| Role-playing agents (role/goal/backstory) | `src/crewai/agent.py` | Persona no system prompt |
| Sequential & Hierarchical process | `src/crewai/crew.py`, `src/crewai/process.py` | Process enum |
| Task graph com dependências | `src/crewai/task.py`, `src/crewai/tasks/conditional_task.py` | Tasks com context, expected_output |
| Flow (graph DSL) | `src/crewai/flow/flow.py`, `src/crewai/flow/flow_visualizer.py` | Decorators @start/@listen/@router + viz HTML |
| Multi-tier memory | `src/crewai/memory/{short_term,long_term,entity,user}/` | Chroma/SQLite |
| Planner | `src/crewai/utilities/planning_handler.py` | Planning automático decompõe tasks |
| Task guardrails | `src/crewai/task.py` (v0.86) | Validação antes de passar ao próximo task |

### Integration / Governance

| Capability | Evidence | Notes |
|------------|----------|-------|
| Knowledge sources | `src/crewai/knowledge/` | PDF/CSV/texto compartilhado |
| LiteLLM multi-provider | `src/crewai/llm.py` | OpenAI/Anthropic/Ollama/Groq |
| OTel telemetry | `src/crewai/telemetry/telemetry.py` | Export externo |
| Task output storage + training | `src/crewai/utilities/task_output_storage_handler.py`, `training_handler.py` | Persistência + training mode |

## Tests / Quality Signals

| Signal | Value | Evidence |
|--------|-------|----------|
| Test framework | pytest + pytest-vcr + pytest-asyncio | `pyproject.toml#tool.uv.dev-dependencies` |
| Test file count | 43 | `tests/` |
| Linter | ruff + mypy | `pyproject.toml#tool.mypy` |
| CI/CD | GitHub Actions | `.github/workflows/{tests,linter,type-checker,security-checker,mkdocs,stale}.yml` |

## Documentation

| Type | Path | Status |
|------|------|--------|
| README | `README.md` | rico, ~300 linhas |
| CONTRIBUTING | — | n/d |
| Architecture docs | `docs/concepts/` | presente |
| Mkdocs site | `mkdocs.yml` | presente |

## Extension Points

| Type | Where | How |
|------|-------|-----|
| Tools | `src/crewai/tools/` + `crewai-tools` package | `BaseTool` subclass |
| Callbacks | Task/Crew constructors | `task_start/task_end/crew_start/crew_end` |

## Notable Design Decisions

- **Crew metáfora** — Agents cooperam como um "crew" — evidência: `src/crewai/crew.py` + README
- **Topologias fixas** — apenas `sequential` e `hierarchical` declaradas — evidência: `src/crewai/process.py`
- **Flow como alternativa** — para grafos dinâmicos — evidência: `src/crewai/flow/flow.py`

## Limitations

- Paralelismo limitado pelo GIL Python — fan-out requer async manual
- Sem UI de monitoramento oficial (depende de OTel backend externo)
- Failure recovery rudimentar — sem DLQ/replay determinístico embutido

## USPs

- Abstração role-playing (role/goal/backstory) — modelo mental natural
- Sequential + hierarchical + Flow cobre múltiplas topologias
- Multi-tier memory embutido (Chroma)
- OTel-first (observabilidade delegada ao stack externo)

---

_Generated by os-bench inventory task | Template v1.0_
