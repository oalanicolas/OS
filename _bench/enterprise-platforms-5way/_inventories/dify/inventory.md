# Inventory — dify (LangGenius)

**Path:** `OS/dify/`
**Profile:** quick
**License:** Apache-2.0 com condicoes adicionais (ver `OS/dify/LICENSE`)
**Stack:** `OS/dify/CLAUDE.md` e `OS/dify/README.md`

## Positioning

> "Dify is an open-source LLM app development platform. Its intuitive interface combines AI workflow, RAG pipeline, agent capabilities, model management, observability features... letting you quickly go from prototype to production."
> (`OS/dify/README.md#L63`)

## Stack

- **Backend:** Python Flask, Domain-Driven Design + Clean Architecture, Celery + Redis broker, SQLAlchemy, `pytest` TDD (`OS/dify/CLAUDE.md`)
- **Frontend:** Next.js + TypeScript + React em `web/`
- **Monorepo:** pnpm 10.33.0 workspaces (`OS/dify/package.json`)
- **API packaging:** `uv run --project api` (uv.lock)

## Top-level

```
README.md  CLAUDE.md  AGENTS.md  CONTRIBUTING.md  LICENSE
package.json  pnpm-workspace.yaml  Makefile
api/    (Python Flask + DDD)
web/    (Next.js)
docker/ (compose, images)
docs/   (i18n: pt-BR, ja, zh-CN, zh-TW, es, fr, de, it, ko, tr, ar, hi, bn, vi, sl, tlh/klingon)
packages/ (dify-ui, iconify-collections, migrate-no-unchecked-indexed-access, tsconfig)
sdks/  e2e/  dev/  scripts/  images/
```

## Backend core modules (`api/core/`)

`agent/`, `app/`, `memory/`, `workflow/`, `rag/`, `tools/`, `plugin/`, `mcp/`, `moderation/`, `ops/`, `trigger/`, `telemetry/`, `model_manager.py`, `provider_manager.py`, `indexing_runner.py`, `llm_generator/`, `callback_handler/`, `datasource/`, `external_data_tool/`, `prompt/`.

## Multi-tenancy — tabela chave

`OS/dify/api/models/account.py` define:

- **TenantAccountRole** enum: OWNER, ADMIN, EDITOR, NORMAL, DATASET_OPERATOR (`#L19-L60`)
- **TenantStatus** enum (`#L230`)
- **Tenant** model (`#L240`)
- **TenantAccountJoin** — associacao user↔tenant com papel (`#L279`)
- **TenantPluginPermission** + **TenantPluginAutoUpgradeStrategy** — permissoes por plugin (`#L359-L391`)

## Capacidades observaveis (subject-only highlights)

- **Visual workflow canvas** ("Build and test powerful AI workflows on a visual canvas") — paradigm primario e pipeline/low-code (`OS/dify/README.md#L93-L94`).
- **RAG pipeline out-of-box** com extracao PDF/PPT/etc (`#L104-L105`).
- **50+ built-in tools** (Google Search, DALL-E, Stable Diffusion, WolframAlpha) (`#L107-L108`).
- **Hundreds of model providers** (GPT, Mistral, Llama3, OpenAI-compatible) (`#L96-L98`).
- **LLMOps** — monitor logs e performance, melhoria contnua de prompts/datasets/models (`#L110-L111`).
- **Observabilidade nativa**: Opik, Langfuse, Arize Phoenix integrados (`#L63`).
- **BaaS** — toda feature tem API (`#L113-L114`).
- **Enterprise edition paga**: `api/enterprise/` stub + e-mail `business@dify.ai` (`#L125-L127`).
- **Deploy**: Docker Compose, 5+ community Helm charts (douban, BorisPolonsky, magicsong, Winson-030, Zhoneym), Terraform (Azure/GCP), AWS CDK EKS/ECS, Alibaba Cloud Computing Nest one-click (`#L161-L200`).
- **Community**: 17 README translations (en, zh-TW, zh-CN, ja, es, fr, klingon, ko, ar, tr, vi, de, it, pt-BR, sl, bn, hi) (`#L44-L60`); LFX Health Score + LFX Contributors badges (`#L35-L40`).

## Observacao de escopo

Dify brilha como **low-code builder** e **LLMOps**. Multi-tenancy existe (TenantAccountRole + TenantPluginPermission) mas e voltada a workspaces de dev, nao a times de negocio com org chart. **Nao tem** org chart, digital employees, role-play multi-agent, company-sim. Paradigma trava em pipeline/workflow.
