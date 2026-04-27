# Executive Report — enterprise-platforms-5way

**Pergunta-guia:** qual opensource melhor resolve "agentes de IA servindo multiplas equipes/projetos numa empresa sem perder contexto"?

**Pack:** `enterprise-agents-10d` — 10 dimensoes ponderadas, pesos somando 1.00.

## TL;DR

| # | Plataforma | Overall | Vence em |
|---:|---|---:|---|
| 1 | **Clawith** | 84.20 | Product focus, multi-tenancy, skill marketplace, memoria-por-agente |
| 2 | **AGT** | 83.00 | Engineering focus, governance, OWASP Agentic 10/10 |
| 3 | **dify** | 74.00 | Observability, community (17 idiomas), deployment |
| 4 | **paperclip** | 68.20 | Multi-company isolation real, governance com rollback |
| 5 | **memori-labs** | 58.00 | Memory architecture (LoCoMo 81.95%) |

Os cinco resolvem **pedacos complementares** — nenhum resolve tudo.

## Leitura por projeto

**Clawith** e o mais proximo da visao "agentes como funcionarios". Seu modelo `Tenant` (`OS/Clawith/backend/app/models/tenant.py`) carrega quotas nativas (`default_max_agents`, `default_agent_ttl_hours`, `sso_enabled`). README anuncia multi-tenant RBAC, approval workflows, audit logs, channel integration (Slack/Discord/Feishu/DingTalk/WeCom/Teams), mais `soul.md`+`memory.md`+org chart e o feed **The Plaza** (`README.md#L27-L58`). No foco product team e imbativel (85.20).

**agent-governance-toolkit (AGT)** e ponta de lanca em governance: OWASP Agentic 10/10 com tabela ASI-01..ASI-10 (`README.md#L187-L201`), policy engine deterministico (YAML/OPA/Rego/Cedar), zero-trust identity Ed25519 + ML-DSA-65, Agent SRE com replay debugging, sandboxing 4-tier rings. Mas **nao e plataforma** — e library que plugga em LangChain, CrewAI, Dify.

**dify** e o maior em community: 17 traducoes de README, badges LFX, Docker Pulls, Reddit. Stack Flask DDD + Celery + Next.js. Multi-tenancy real com 5 roles em `TenantAccountRole` + `TenantPluginPermission`. Paradigma **trava em pipeline/low-code** (canvas + RAG + ReAct) — nao suporta role-play multi-agent nem company-sim.

**paperclip** e unico em company-sim: "not an agent framework, not a workflow builder" (`README.md#L164-L167`). Forte em multi-company isolation, governance com rollback, goal-aware execution. Mas ROADMAP admite **Memory/Knowledge ainda nao-shipped** (`README.md#L262`) — maior gap dos cinco.

**memori-labs** e memory-infra especializada: LoCoMo 81.95% (outperforma Zep/LangMem/Mem0), attribution entity/process/session, Advanced Augmentation tipada (8 classes). Nao tem orchestration, nao tem UI — e a peca que as outras quatro precisam.

## Gaps comuns (o que nenhum dos 5 resolve bem)

1. **Graph-typed memory multi-tenant com policy enforcement sobre queries.** Memori chega perto mas e SaaS-first; Clawith tem file-based; paperclip nao tem. Ninguem combina graph memory + OPA/Cedar sobre retrieval.
2. **Paradigm polymorphism real.** AGT e agnostico mas nao orquestra; dify trava em pipeline; paperclip em company-sim; Clawith em digital-employee. Nenhum pluga paradigmas lado a lado.
3. **Skill marketplace org-wide com approval workflow + rollback.** Clawith tem skills engine + discovery runtime sem aprovacao formal; dify tem plugin permission tool-level; AGT tem marketplace-lifecycle sem UX. Ninguem liga publish -> review -> propagacao com rollback.
4. **OWASP ASI-0x integrado em UI de orchestration.** Apenas AGT tem mapping 10/10 — mas sem UI de teams. Clawith/paperclip tem audit sem ASI labels.
5. **Cost-per-team + per-skill + per-memory-query observability.** Paperclip tem budget per agent; dify tem LLMOps; Clawith tem quota_guard. Ninguem junta as tres dimensoes.
6. **Event-sourced replay cross-platform.** So AGT tem flight recorder. Para incidentes longos sem perder contexto, isso e critico.

## What AIOX Enterprise + Sinkra could add

Colando os gaps acima, AIOX Enterprise + Sinkra tem janela clara:

- **Graph-typed memory multi-tenant com policy-aware queries (Sinkra).** Combina a tipagem de Memori (attributes/events/facts/people/rules/skills) com o policy engine de AGT (YAML/OPA/Cedar) aplicado sobre o **retrieval path**. Memoria e recuperada *apos* autorizacao por tenant/role/skill-scope. Nenhum dos 5 oferece.

- **Paradigm multiplexer (AIOX).** Roda pipeline (estilo Dify), role-play (estilo CrewAI/AutoGen), digital-employee (estilo Clawith) e company-sim (estilo Paperclip) lado a lado, compartilhando graph memory, skill marketplace e governance layer.

- **Skill marketplace com approval workflow nativo + rollback.** Publish -> review board (humano ou agente) -> versionamento semantico -> propagacao progressiva por team com circuit breaker. Cola Clawith (UX) + AGT (lifecycle) + paperclip (rollback).

- **OWASP ASI-0x dashboard UI-first.** AGT expoe ASI-01..ASI-10 em CLI/library; UI com drill-down por agent/skill/memory-access seria tabela-stake enterprise.

- **Cost + governance observability em 3 eixos.** Tenant x skill x memory-query — nenhum dos 5 junta.

- **Flight recorder portavel.** Consumir eventos de Clawith/Dify/Paperclip/AGT/Memori num storage comum e reexecutar incidente com estado de memoria, policies e skills daquele dia.

- **BYOA + BYOLLM + BYODB estrita.** Dify faz BYOLLM; paperclip faz BYOA; Memori faz BYODB. Faltam os tres juntos sob UX coerente e governance compartilhada.

O mercado tem **piece parts excelentes** — memoria (Memori), governance (AGT), plataforma (Clawith/Dify), company-sim (Paperclip). Falta o *system-of-systems* que cole essas pecas por baixo de um graph memory multi-tenant, um paradigm multiplexer e um marketplace governado. E essa lacuna que AIOX Enterprise + Sinkra podem ocupar.
