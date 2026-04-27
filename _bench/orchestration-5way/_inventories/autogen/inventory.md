# Inventário: autogen

**Path:** `OS/autogen/`
**Date:** 2026-04-19
**Extraction Method:** filesystem-scan + doc-scan
**Confidence:** HIGH

---

## Identity

| Field | Value |
|-------|-------|
| Slug | autogen |
| Source URL | https://github.com/microsoft/autogen |
| Primary language | Python |
| Secondary languages | C# (.NET), TypeScript (Studio frontend) |
| Stack | Python >=3.10 (monorepo uv), Pydantic 2, .NET, gRPC/CloudEvents, OpenTelemetry |
| License | MIT + CLA |
| Tagline | Framework MS para apps multi-agente conversacionais — **maintenance mode** (sucessor: Microsoft Agent Framework). |

## Key Metrics

| Metric | Value | Source |
|--------|-------|--------|
| LOC (Python) | 112.463 | `wc -l` |
| Files | 1.837 | filesystem scan |
| Top-level dirs | python, dotnet, docs, protos | `ls` |
| README length | ~400 linhas | `README.md` |
| Docs pages | 200+ | `python/docs/` |
| Last commit | 2026-04-06 | `git log -1` |

## Modules / Top-level Structure

| Module | Path | Type | Descrição |
|--------|------|------|-----------|
| autogen-core | `python/packages/autogen-core/` | package | Runtime, messaging, subscriptions, serialization |
| autogen-agentchat | `python/packages/autogen-agentchat/` | package | API high-level conversacional + teams |
| autogen-ext | `python/packages/autogen-ext/` | package | Modelos, runtimes gRPC, MCP tools, memória, code exec |
| autogen-studio | `python/packages/autogen-studio/` | app | UI no-code (React+FastAPI) |
| autogen-magentic-one | `python/packages/autogen-magentic-one/` | package | Magentic-One generalist orchestrator |
| magentic-one-cli | `python/packages/magentic-one-cli/` | app | CLI m1 |
| agbench | `python/packages/agbench/` | package | Benchmark harness |
| dotnet | `dotnet/` | package | Implementação .NET paralela |
| protos | `protos/` | library | agent_worker.proto, cloudevent.proto |

## External Dependencies (top 10)

| Package | Version | Purpose |
|---------|---------|---------|
| pydantic | >=2.10.0,<3.0.0 | Core models |
| protobuf | ~=5.29.3 | gRPC serialization |
| opentelemetry-api | >=1.34.1 | Tracing |
| pillow | >=11.0.0 | Image handling |
| typing-extensions | >=4.0.0 | Typing |
| jsonref | ~=1.1.0 | JSON schema |
| openai | opcional (autogen-ext[openai]) | OpenAI |
| anthropic | opcional (autogen-ext) | Anthropic |
| mcp | opcional (autogen-ext) | MCP workbench |
| azure-identity | opcional | Azure auth |

## Entry Points

| Entry | Path | Command |
|-------|------|---------|
| Python API | `python/packages/autogen-agentchat/src/autogen_agentchat/agents/` | `from autogen_agentchat.agents import AssistantAgent` |
| Runtime | `python/packages/autogen-core/src/autogen_core/_single_threaded_agent_runtime.py` | `SingleThreadedAgentRuntime()` |
| CLI | `python/packages/magentic-one-cli/` | `m1` |
| GUI | `python/packages/autogen-studio/` | `autogenstudio ui` |

## Capabilities

### Core

| Capability | Evidence | Notes |
|------------|----------|-------|
| Conversational agent abstraction | `python/packages/autogen-agentchat/src/autogen_agentchat/agents/`, `base/_chat_agent.py` | AssistantAgent, UserProxyAgent, SocietyOfMindAgent |
| 4 group chat topologies | `teams/_group_chat/{_round_robin_group_chat.py,_selector_group_chat.py,_swarm_group_chat.py,_magentic_one/}` | round-robin, selector LLM-driven, swarm, magentic |
| Graph-based team | `teams/_group_chat/_graph/` | DAG entre agents |
| Distributed gRPC runtime | `autogen-ext/src/autogen_ext/runtimes/grpc/`, `protos/agent_worker.proto`, `protos/cloudevent.proto` | Escalável horizontal — multi-worker |
| Topic-based subscriptions | `autogen-core/src/autogen_core/_topic.py`, `_type_subscription.py` | Pub/sub messaging |
| State save/load | `autogen-agentchat/src/autogen_agentchat/state/` | Checkpoint em agents e teams |
| Memory + model-context | `autogen-core/src/autogen_core/{memory,model_context}/`, `autogen-ext/.../memory/` | Protocols + impls Redis/mem0/Chroma |
| Code executors | `autogen-ext/.../code_executors/`, `autogen-core/.../code_executor/` | Docker/Jupyter/local |
| Intervention handlers | `autogen-core/src/autogen_core/_intervention.py` | Hook para mod mensagens runtime |

### Integration / UX

| Capability | Evidence | Notes |
|------------|----------|-------|
| MCP workbench | `autogen-ext/.../tools/` | McpWorkbench, StdioServerParams |
| AutoGen Studio UI | `python/packages/autogen-studio/` | No-code GUI |
| Magentic-One orchestrator | `python/packages/autogen-magentic-one/` | Generalist agent com WebSurfer/FileSurfer/Coder |
| OTel tracing nativo | `autogen-core/src/autogen_core/_telemetry/` | Tracing in-band |
| .NET parity | `dotnet/AutoGen.sln` | Mesma API em C# |

## Tests / Quality Signals

| Signal | Value | Evidence |
|--------|-------|----------|
| Test framework | pytest + pytest-asyncio | per-package pyproject |
| Test file count | 117 (Python) | `tests/` subpastas |
| Linter | ruff + mypy + pyright | pyprojects |
| CI/CD | GitHub Actions | `.github/workflows/` (25+ workflows) |

## Documentation

| Type | Path | Status |
|------|------|--------|
| README | `README.md` | rico |
| CONTRIBUTING | `CONTRIBUTING.md` | presente |
| Docs site | `python/docs/` | 200+ páginas (tutorials, user-guide, api-ref) |

## Extension Points

| Type | Where | How |
|------|-------|-----|
| Extensions | `autogen-ext/` + Component protocol | package via pip |
| Intervention hooks | `autogen_core._intervention.py` | on_message, on_publish |
| MCP client | `autogen-ext/.../tools/` | McpWorkbench |

## Notable Design Decisions

- **Protocol-first** — Component protocol + protos para distribuição — evidência: `autogen-core/_component_config.py`, `protos/`
- **Separation of concerns** — core (runtime) / agentchat (API) / ext (batteries) — evidência: `python/packages/`
- **Research-oriented** — agbench + Magentic-One — evidência: `autogen-magentic-one/`, `agbench/`

## Limitations

- **Maintenance mode** — sem novas features (banner README)
- Curva de aprendizado alta — 3 pacotes + C# paralelo
- Sem DSL visual declarativa (só código)

## USPs

- Runtime distribuído gRPC + CloudEvents real — escala horizontal
- 4+ topologias embutidas (round-robin/selector/swarm/magentic/graph)
- Paridade .NET + Python
- AutoGen Studio no-code UI
- Research-grade (agbench, Magentic-One, papers MS)

---

_Generated by os-bench inventory task | Template v1.0_
