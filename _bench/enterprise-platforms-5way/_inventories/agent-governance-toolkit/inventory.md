# Inventory — agent-governance-toolkit (AGT)

**Path:** `OS/agent-governance-toolkit/`
**Profile:** quick
**License:** MIT (`OS/agent-governance-toolkit/LICENSE`)
**Mantido por:** Microsoft (Public Preview; `OS/agent-governance-toolkit/README.md#L14-L16`)

## Positioning

> "Runtime governance for AI agents — deterministic policy enforcement, zero-trust identity, execution sandboxing, and SRE for autonomous agents. Covers all 10 OWASP Agentic risks with 9,500+ tests." (`OS/agent-governance-toolkit/README.md#L21`)

**Nao e** uma plataforma de agentes — e a camada policy/identity/audit que plugga em outras plataformas (LangChain, CrewAI, AutoGen, Dify, etc.) (`OS/agent-governance-toolkit/README.md#L166-L183`).

## Stack

- **Python** principal: `pip install agent-governance-toolkit[full]`
- **Multi-language SDKs:** TypeScript (`@microsoft/agentmesh-sdk`), .NET (`Microsoft.AgentGovernance`), Rust (`agentmesh`), Go
- **Dockerfile** + `docker-compose.yml` na raiz; deployment guides para Azure AKS/Foundry/Container Apps, AWS ECS/Fargate, GCP GKE

## Top-level

```
README.md  QUICKSTART.md  BENCHMARKS.md  CHANGELOG.md
ADOPTERS.md  COMMUNITY.md  INDEPENDENCE.md  SECURITY.md
packages/  docs/  examples/  demo/  notebooks/
fuzz/  pipelines/  benchmarks/  action/  scripts/
Dockerfile  docker-compose.yml  mkdocs.yml
```

## Packages (13 subpackages)

`agent-compliance`, `agent-discovery`, `agent-governance-dotnet`, `agent-hypervisor`, `agent-lightning`, `agent-marketplace`, `agent-mcp-governance`, `agent-mesh`, `agent-os`, `agent-os-vscode`, `agent-runtime`, `agent-sre`, `agentmesh-integrations` (`OS/agent-governance-toolkit/packages/`).

## Capacidades observaveis (subject-only highlights)

- **OWASP Agentic Top 10 — 10/10 covered** com mapping por ASI-01..ASI-10 e link para `docs/OWASP-COMPLIANCE.md` (`OS/agent-governance-toolkit/README.md#L187-L202`).
- **Policy engine determinstico** claimed < 0.1 ms/action; YAML, OPA/Rego e Cedar policies (`OS/agent-governance-toolkit/README.md#L33-L38`, `#L152`).
- **Zero-trust identity** Ed25519 + quantum-safe ML-DSA-65, trust scoring 0-1000, SPIFFE/SVID (`OS/agent-governance-toolkit/README.md#L154`).
- **Execution sandboxing** com 4-tier privilege rings, saga orchestration, kill switch (`agent-runtime/`, `agent-hypervisor/`).
- **Agent SRE**: SLOs, error budgets, replay debugging, chaos engineering, circuit breakers (`packages/agent-sre/`).
- **Shadow AI Discovery** — inventory de agentes nao registrados (`packages/agent-discovery/`).
- **MCP Security Scanner** — detecta tool poisoning, typosquatting, hidden instructions (`packages/agent-os/src/agent_os/mcp_security.py`).
- **Unified `agt` CLI**: `agt verify`, `agt doctor`, `agt lint-policy` (`packages/agent-compliance/src/agent_compliance/cli/agt.py`).
- **Agent Marketplace** pacote para plugin lifecycle management (`packages/agent-marketplace/`).
- **Governance Dashboard** demo em `demo/governance-dashboard/`.
- **Compliance mapping** para EU AI Act, NIST AI RMF, SOC 2, Colorado AI Act (`OS/agent-governance-toolkit/README.md#L202`, `docs/compliance/`).
- **9,500+ tests**, CI badges, OpenSSF Scorecard, CodeQL, Gitleaks, ClusterFuzzLite (7 fuzz targets), Dependabot em 13 ecosystems (`OS/agent-governance-toolkit/README.md#L290-L296`).

## Integracoes de stack (como plugga em outras plataformas)

Microsoft Agent Framework, Semantic Kernel, Microsoft AutoGen, LangGraph/LangChain, CrewAI, OpenAI Agents SDK, Google ADK, LlamaIndex, Haystack, **Dify** (plugin), Azure AI Foundry (`OS/agent-governance-toolkit/README.md#L168-L183`).

## Observacao de escopo

**Nao tem orquestracao, UI de times, memory propria, nem skill marketplace no sentido Clawith** — e uma governance-only library. Explicitamente diz: "This is not a prompt guardrail or content moderation tool. It governs agent *actions*, not LLM inputs/outputs" (`OS/agent-governance-toolkit/README.md#L30-L31`).
