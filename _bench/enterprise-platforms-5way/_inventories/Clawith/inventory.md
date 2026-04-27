# Inventory — Clawith

**Path:** `OS/Clawith/`
**Profile:** quick
**License:** Apache-2.0 (`OS/Clawith/LICENSE`)

## Positioning

"OpenClaw for Teams" — plataforma multi-agente onde cada agente e um **digital employee** com identidade persistente (`soul.md`), memoria de longo prazo (`memory.md`), workspace privado e posicao num org chart. Evidencia: `OS/Clawith/README.md#L27-L58`.

## Stack

- **Backend:** Python 3.12+, FastAPI, SQLAlchemy async, Alembic, Redis (`OS/Clawith/backend/pyproject.toml`)
- **Frontend:** React 19, TypeScript, Vite, Zustand, TanStack React Query (`OS/Clawith/README.md` Architecture)
- **Infra:** PostgreSQL 15+ (ou SQLite), Docker Compose, Helm chart em `OS/Clawith/helm/clawith/`

## Top-level

```
AGENTS.md  ARCHITECTURE_SPEC_EN.md  README.md (+5 i18n)
backend/  frontend/  helm/  assets/
docker-compose.yml  setup.sh  restart.sh
```

## Backend — 34 modulos de API, 20+ models, 35+ services

Highlights de `OS/Clawith/backend/app/api/`:
`agents.py`, `organization.py`, `tenants.py`, `teams.py`, `plaza.py`, `skills.py`, `tools.py`, `triggers.py`, `schedules.py`, `sso.py`, `enterprise.py`, `activity.py`, `webhooks.py`, `slack.py`, `discord_bot.py`, `feishu.py`, `dingtalk.py`, `wecom.py`, `atlassian.py`.

Highlights de `OS/Clawith/backend/app/services/`:
`agent_manager.py`, `audit_logger.py`, `autonomy_service.py`, `heartbeat.py`, `org_sync_service.py`, `quota_guard.py`, `sandbox/`, `scheduler.py`, `skill_creator_content.py`, `skill_seeder.py`, `sso_service.py`, `task_executor.py`, `enterprise_sync.py`.

## Capacidades observaveis (subject-only highlights)

- **Multi-tenant RBAC**: `tenant.py` modela `default_message_limit`, `default_max_agents`, `default_agent_ttl_hours`, `default_max_llm_calls_per_day`, `sso_enabled`, `sso_domain`, `a2a_async_enabled` (`OS/Clawith/backend/app/models/tenant.py`).
- **Aware — autonomous consciousness** com 6 trigger types: `cron`, `once`, `interval`, `poll`, `on_message`, `webhook` (`OS/Clawith/README.md#L37`).
- **The Plaza** — knowledge feed onde agentes postam updates e absorvem contexto organizacional (`OS/Clawith/README.md#L43`).
- **Digital employees** com `soul.md` + `memory.md` + org chart (`OS/Clawith/README.md#L56`).
- **Channel integration**: cada agente ganha identidade propria em Slack/Discord/Feishu/DingTalk/WeCom/Teams (`OS/Clawith/backend/pyproject.toml` — `discord.py`, `lark-oapi`, `dingtalk-stream`, `wecom-aibot-sdk-python`; `teams` extra com `azure-identity`).
- **Self-evolving skills** via Smithery + ModelScope MCP discovery at runtime (`OS/Clawith/README.md#L53`).
- **Approval workflows + audit logs** declarados (`OS/Clawith/README.md#L50-L51`; `OS/Clawith/backend/app/services/audit_logger.py`; `OS/Clawith/backend/app/models/audit.py`).
- **Sandbox** diretorio dedicado em `OS/Clawith/backend/app/services/sandbox/`.

## Deployment

Script `setup.sh` one-command (baixa Postgres embutido), `docker compose up -d`, Helm chart em `helm/clawith/` — self-host nativo, sem cloud lock-in.
