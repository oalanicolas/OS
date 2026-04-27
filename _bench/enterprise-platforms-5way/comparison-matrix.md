# Comparison Matrix — enterprise-platforms-5way

10 dimensoes (pack customizado `enterprise-agents-10d`) x 5 subjects. Todas as celulas citam evidencia observavel. Escala por celula = 0-5.

Legenda: `5` Excelente · `4` Forte · `3` OK · `2` Fraco · `1` Marginal · `0` Ausente.

## 1. Multi-tenancy (peso 0.12)

| Subject | Score | Evidence |
|---|---:|---|
| **Clawith** | 5 | `OS/Clawith/backend/app/models/tenant.py` define `Tenant` com quotas por tenant (`default_message_limit`, `default_max_agents`, `default_agent_ttl_hours`), SSO domain, `a2a_async_enabled`; `OS/Clawith/backend/app/api/tenants.py`, `teams.py`, `organization.py`; README: "organization-based isolation with role-based access" (`README.md#L48`). |
| **agent-governance-toolkit** | 3 | Nao e plataforma multi-tenant — e library. Porem tem zero-trust identity (Ed25519 + ML-DSA-65) e trust scoring 0-1000 que podem servir como substrato (`README.md#L154`). Sem workspace/team concept. |
| **memori-labs** | 4 | Attribution model com `entity_id` + `process_id` + `session_id` da isolamento logico por entidade (`README.md#L189-L235`). Cloud-first (multi-tenant SaaS via `MEMORI_API_KEY`). BYODB oferece isolamento a nivel de banco. Sem UI de teams. |
| **dify** | 4 | `Tenant`, `TenantAccountRole` (OWNER/ADMIN/EDITOR/NORMAL/DATASET_OPERATOR), `TenantAccountJoin`, `TenantPluginPermission` em `OS/dify/api/models/account.py#L19-L391`. Multi-workspace real, focado em dev teams. Sem org chart hierarquico. |
| **paperclip** | 5 | "True multi-company isolation — every entity is company-scoped, so one deployment can run many companies with separate data and audit trails" (`README.md#L155`). Org charts com roles e reporting lines. `server/src/routes/companies.ts`. |

## 2. Governance & Audit (peso 0.13)

| Subject | Score | Evidence |
|---|---:|---|
| **Clawith** | 4 | `backend/app/models/audit.py`, `backend/app/services/audit_logger.py`, README: "Approval workflows — flag dangerous operations for human review" + "Audit logs & Knowledge Base" (`README.md#L50-L51`). Sem OWASP Agentic mapping explicito. |
| **agent-governance-toolkit** | 5 | OWASP Agentic Top 10 **10/10 covered** com mapping ASI-01..ASI-10 (`README.md#L187-L201`); deterministic policy engine (YAML/OPA/Rego/Cedar); 9,500+ tests; compliance mapping EU AI Act, NIST AI RMF, SOC 2 (`README.md#L202`, `docs/compliance/`); Agent SRE com replay debugging. Best-in-class. |
| **memori-labs** | 1 | Nao e foco. Tem `SECURITY.md` e attribution model pra rastrear origem de memoria, mas sem audit trail imutavel, policy enforcement, approval gates. |
| **dify** | 3 | `TenantPluginPermission` com auto-upgrade strategy (`api/models/account.py#L359-L391`); LLMOps logs; observability via Langfuse/Opik/Phoenix (`README.md#L63`). Sem OWASP Agentic mapping, sem deterministic policy layer. |
| **paperclip** | 4 | "Governance with rollback — approval gates are enforced, config changes are revisioned, and bad changes can be rolled back safely" (`README.md#L152`); `server/src/routes/approvals.ts`, `access.ts`, `authz.ts`; ticket system com "every decision explained, full tool-call tracing and immutable audit log" (`README.md#L108`). Sem OWASP mapping explicito. |

## 3. Paradigm flexibility (peso 0.11)

| Subject | Score | Evidence |
|---|---:|---|
| **Clawith** | 4 | Digital-employee paradigm primario; suporta multi-agent collaboration (Plaza, A2A), triggers variados (`cron/once/interval/poll/on_message/webhook`). Flexivel dentro do paradigma "employees". |
| **agent-governance-toolkit** | 5 | Explicitamente framework-agnostic — integra com LangGraph, LangChain, CrewAI, AutoGen, OpenAI Agents, Google ADK, LlamaIndex, Haystack, Dify (como plugin), Semantic Kernel (`README.md#L168-L183`). Nao prescreve paradigma. |
| **memori-labs** | 4 | LLM/datastore/framework-agnostic by design (`README.md#L8`). Plugga em Agno, LangChain, Pydantic AI, OpenClaw, MCP clients. Nao prescreve paradigma de orquestracao. |
| **dify** | 2 | Paradigma primario e pipeline/workflow visual canvas + RAG + ReAct agent (`README.md#L93-L108`). Trava em low-code builder. Nao suporta role-play multi-agent nem company-sim. |
| **paperclip** | 3 | Company-sim e paradigma unico e exclusivo — "Not an agent framework. Not a workflow builder." (`README.md#L164-L167`). BYOA (Claude, OpenClaw, Codex, Cursor) da variedade de runtime, mas paradigma de orquestracao e um so. |

## 4. Memory architecture (peso 0.11)

| Subject | Score | Evidence |
|---|---:|---|
| **Clawith** | 4 | `memory.md` per-agent + `soul.md` (personality) + private file system (`README.md#L56`); Plaza serve como memoria organizacional compartilhada; Knowledge Base declarada (`README.md#L51`). Nao tem graph-typed memory. |
| **agent-governance-toolkit** | 2 | Nao e memoria — porem "Episodic memory with integrity checks" como controle ASI-06 Memory Poisoning (`README.md#L196`). Substrato pra verificar, nao armazenar. |
| **memori-labs** | 5 | Memoria tipada (attributes, events, facts, people, preferences, relationships, rules, skills) com augmentation (`README.md#L265-L282`); Rust core; FAISS vector + lexical + parsing search (`memori/search/`); entity+process+session attribution; LoCoMo 81.95% outperforma Zep/LangMem/Mem0 (`README.md#L144-L152`). Best-in-class memory. |
| **dify** | 3 | `core/memory/` + `core/rag/` + `datasets` model + dataset_operator role. Focado em RAG/KB pra apps, nao memoria estruturada multi-agent. |
| **paperclip** | 1 | ROADMAP marca "Memory / Knowledge" como nao-shipped (`README.md#L262`). `skills/para-memory-files` e file-based, nao estruturado. Ticket history supre contexto, nao memoria. |

## 5. Skill marketplace (peso 0.10)

| Subject | Score | Evidence |
|---|---:|---|
| **Clawith** | 5 | `skills.py` API, `skill.py` model, `skill_creator_content.py`, `skill_seeder.py` services, skill_creator_files dir; self-evolving via Smithery + ModelScope MCP discovery runtime (`README.md#L53`); agentes podem criar skills pra si ou pra colegas (`README.md#L53`). Melhor coverage observavel. |
| **agent-governance-toolkit** | 3 | `packages/agent-marketplace/` "Plugin lifecycle management" (`README.md#L250`, `packages/agent-marketplace/pyproject.toml`). Focado em governance do marketplace, nao distribuicao de skills com UX. |
| **memori-labs** | 1 | Nao aplicavel — e library de memoria. |
| **dify** | 4 | 50+ built-in tools + `TenantPluginPermission` + `TenantPluginAutoUpgradeStrategy` (`api/models/account.py#L359-L391`); plugin permission flow org-wide. Nao e skill-marketplace no sentido Clawith, e tool/plugin. |
| **paperclip** | 3 | "Skills Manager" marcada como shipped no ROADMAP (`README.md#L255`); `server/src/routes/company-skills.ts`, `server/src/services/company-skills.ts`; 4 skills de referencia em `skills/`. Clipmart (marketplace) e roadmap. |

## 6. Durability (peso 0.09)

| Subject | Score | Evidence |
|---|---:|---|
| **Clawith** | 4 | PostgreSQL + Alembic migrations; persistent identity per agent (soul.md/memory.md em `backend/agent_data/<agent-id>/`, `README.md#L125-L127`); Aware focus items com status markers para retomar trabalho. Sem replay explicito. |
| **agent-governance-toolkit** | 5 | Agent SRE com **replay debugging**, flight recorder, circuit breakers, saga orchestration (`README.md#L154-L156`, `README.md#L199` ASI-09 "Full audit trails + flight recorder"). |
| **memori-labs** | 3 | Persistencia nativa (Cloud ou BYODB); sessions e conversation messages persistem (`memori/memory/_conversation_messages.py`). Sem replay multi-agent. |
| **dify** | 4 | Celery + Redis broker para async; LLMOps com logs persistentes (`README.md#L110-L111`); `api/migrations/` via alembic. Workflows tem persistencia nativa. |
| **paperclip** | 4 | "Persistent agent state — Agents resume the same task context across heartbeats instead of restarting from scratch" (`README.md#L150`); "sessions persist across reboots" (`README.md#L134`); embedded PostgreSQL. Sem event-sourced replay. |

## 7. Safety & sandboxing (peso 0.09)

| Subject | Score | Evidence |
|---|---:|---|
| **Clawith** | 4 | `backend/app/services/sandbox/` dir dedicado; docker isolation (`docker>=7.0.0` em pyproject); approval workflows; quota_guard.py (`README.md#L50`). |
| **agent-governance-toolkit** | 5 | 4-tier privilege rings + execution sandboxing + kill switch + `agent-hypervisor` package + capability model least-privilege (`README.md#L154-L156`, ASI-02/ASI-04). Best-in-class. |
| **memori-labs** | 2 | Nao aplicavel a orquestracao de execucao. |
| **dify** | 3 | `core/moderation/`, tools executam em contexto Celery worker; sandbox nao e feature primaria. |
| **paperclip** | 3 | `execution-workspaces.ts`, `workspace-command-authz.ts`, `workspace-runtime-service-authz.ts` dao autorizacao por comando; ROADMAP "Cloud / Sandbox agents" ainda nao-shipped. Budget enforcement atomico. |

## 8. Observability (peso 0.09)

| Subject | Score | Evidence |
|---|---:|---|
| **Clawith** | 3 | `activity_logger.py`, `audit_logger.py`, `notification.py`, Plaza feed. Sem traces/cost-per-team dashboards explicitos. |
| **agent-governance-toolkit** | 5 | Agent SRE com SLOs, error budgets, chaos engineering, circuit breakers, Governance Dashboard (`demo/governance-dashboard/`), audit events real-time (`README.md#L154-L156`, `#L160`); BENCHMARKS.md com p50 latency e throughput. |
| **memori-labs** | 3 | Dashboard Cloud com "Memories, Analytics, Playground, API Keys" (`README.md#L136-L138`); CLI quota. Cloud-only, SaaS. |
| **dify** | 5 | Observability integrada com **Opik, Langfuse, Arize Phoenix** (`README.md#L63`); LLMOps logs nativos (`README.md#L110`); Grafana dashboard comunitario (`README.md#L157-L159`); LFX Health Score badge. |
| **paperclip** | 4 | `server/src/routes/dashboard.ts`, `costs.ts`, `activity.ts`; "Cost Control — monthly budgets per agent, when they hit the limit they stop" (`README.md#L101`); ticket tracing completo. Sem integracao nativa com Langfuse/Phoenix. |

## 9. Deployment flex (peso 0.08)

| Subject | Score | Evidence |
|---|---:|---|
| **Clawith** | 5 | `setup.sh` one-command (download local Postgres); `docker compose up -d`; Helm chart oficial em `helm/clawith/`; SQLite modo pessoal; self-host nativo. |
| **agent-governance-toolkit** | 5 | Deployment guides: Azure AKS/Foundry/Container Apps, AWS ECS/Fargate, GCP GKE, Docker Compose (`README.md#L274`). Dockerfile + Dockerfile.sidecar no `packages/agent-os/`. Library instalavel (pip/npm/nuget/cargo/go). |
| **memori-labs** | 3 | Cloud-first (SaaS em `app.memorilabs.ai`); BYODB suportado mas secondary; Dockerfile presente. Sem helm chart ou cloud deployment guides detalhados. |
| **dify** | 5 | Docker Compose, **5+ community Helm charts**, Terraform Azure/GCP, AWS CDK EKS/ECS, Alibaba Cloud one-click (`README.md#L161-L200`). Tanto Cloud quanto self-host quanto enterprise on-prem. |
| **paperclip** | 4 | `npx paperclipai onboard --yes`, Dockerfile, embedded Postgres zero-setup, bind presets local/lan/tailnet (`README.md#L172-L199`). ROADMAP: "Cloud deployments" ainda nao-shipped. |

## 10. Community (peso 0.08)

| Subject | Score | Evidence (apenas o que consta no README/package.json) |
|---|---:|---|
| **Clawith** | 4 | README com 5 traducoes (en, zh-CN, ja, ko, es); Discord link; X/Twitter; QR code de comunidade; badges de stars/forks/contributors (sem numeros fixos para citar). |
| **agent-governance-toolkit** | 4 | 3 traducoes (en, ja, zh-CN); PyPI package publicado; OpenSSF Scorecard badge; `ADOPTERS.md`, `COMMUNITY.md`, `CHANGELOG.md`, 6 RELEASE_NOTES (v1.0.0, v2.1.0-v2.3.0, v3.0.0, v3.1.0); Microsoft-signed. |
| **memori-labs** | 3 | PyPI + NPM publicados; Discord badge com discord.gg/abD4eGym6v; Trendshift badge; docs site memorilabs.ai. 1 linguagem README. |
| **dify** | 5 | **17 traducoes** de README incluindo Klingon (`README.md#L44-L60`); LFX Health Score + LFX Contributors + LFX Active Contributors badges (Linux Foundation Insights); Docker Pulls badge; Reddit `r/difyai`; Discord 1082486657678311454. Ecosistema mais visivel entre os 5. |
| **paperclip** | 3 | Discord link; star history chart; telemetry-by-default; `awesome-paperclip` plugins list; 1 linguagem README. |

---

## Consolidated observable-feature grid

| Dimensao (peso) | Clawith | AGT | Memori | Dify | Paperclip |
|---|---:|---:|---:|---:|---:|
| Multi-tenancy (0.12) | 5 | 3 | 4 | 4 | 5 |
| Governance & Audit (0.13) | 4 | 5 | 1 | 3 | 4 |
| Paradigm flexibility (0.11) | 4 | 5 | 4 | 2 | 3 |
| Memory architecture (0.11) | 4 | 2 | 5 | 3 | 1 |
| Skill marketplace (0.10) | 5 | 3 | 1 | 4 | 3 |
| Durability (0.09) | 4 | 5 | 3 | 4 | 4 |
| Safety & sandboxing (0.09) | 4 | 5 | 2 | 3 | 3 |
| Observability (0.09) | 3 | 5 | 3 | 5 | 4 |
| Deployment flex (0.08) | 5 | 5 | 3 | 5 | 4 |
| Community (0.08) | 4 | 4 | 3 | 5 | 3 |

Scores 0-5 per cell; multiplicacao pelos pesos calculada em `scorecard.md`.
