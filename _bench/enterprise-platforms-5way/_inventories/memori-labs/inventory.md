# Inventory — memori-labs

**Path:** `OS/memori-labs/`
**Profile:** quick
**License:** Apache-2.0 (`OS/memori-labs/README.md#L30`)
**Pacote PyPI:** `memori` (v3.3.0rc1 em `OS/memori-labs/pyproject.toml`)
**Pacote NPM:** `@memorilabs/memori`

## Positioning

> "Memory from what agents do, not just what they say. Memori plugs into the software and infrastructure you already use. It is LLM, datastore and framework agnostic."
> (`OS/memori-labs/README.md#L4-L10`)

E **memory-infra**, nao plataforma de orquestracao — nao tem UI de teams, skill marketplace, orchestration.

## Stack

- **Python SDK** (`memori/`, Python >=3.10)
- **TypeScript SDK** (`memori-ts/`, `@memorilabs/memori`)
- **Rust core** (`core/`, `setuptools-rust>=1.10` em pyproject)
- Dependencies hard: `aiohttp`, `faiss-cpu`, `sentence-transformers`, `numpy`, `torch>=2.4,<2.11`, `grpcio`, `protobuf`, `botocore`
- Optional extras: `sqlalchemy`, `cockroachdb` (BYODB)
- `Dockerfile`, `docker-compose.yml` na raiz

## Top-level

```
README.md  CHANGELOG.md  CONTRIBUTING.md  SECURITY.md
pyproject.toml  setup.py  setup.cfg  MANIFEST.in  Makefile
Dockerfile  docker-compose.yml
core/       # Rust (Cargo.toml, bindings, src)
memori/     # Python SDK
memori-ts/  # TypeScript SDK
integrations/openclaw/  # Drop-in plugin
benchmarks/ docs/ examples/ tests/
```

## Python SDK modules (`memori/`)

`api/`, `embeddings/`, `llm/`, `memory/ (augmentation/, recall.py, _collector.py, _writer.py, _manager.py, _struct.py, _conversation_messages.py)`, `search/ (_faiss, _lexical, _parsing, _core, _api)`, `storage/`, `_cli.py`, `_config.py`, `_network.py`, `_rust_core.py`.

## Capacidades observaveis (subject-only highlights)

- **LoCoMo benchmark**: 81.95% overall accuracy com 1,294 tokens avg — 4.97% do full-context footprint; outperforma Zep/LangMem/Mem0 (`OS/memori-labs/README.md#L144-L152`).
- **Attribution model**: `entity_id` (user/thing) + `process_id` (agent/program) + `session_id` — base para multi-tenancy de memoria por design (`OS/memori-labs/README.md#L189-L235`).
- **Advanced Augmentation** com 8 tipos: attributes, events, facts, people, preferences, relationships, rules, skills (`OS/memori-labs/README.md#L265-L282`).
- **LLM coverage**: Anthropic, Bedrock, DeepSeek, Gemini, Grok (xAI), OpenAI — sync/async/streamed (`OS/memori-labs/README.md#L237-L246`).
- **Framework coverage**: Agno, LangChain, Pydantic AI (`OS/memori-labs/README.md#L248-L252`).
- **MCP transport** para Claude Code, Cursor, Codex, Warp, Antigravity — sem SDK integration (`OS/memori-labs/README.md#L172-L187`).
- **OpenClaw plugin** nativo: `openclaw plugins install @memorilabs/openclaw-memori` — drop-in persistent memory (`OS/memori-labs/README.md#L154-L170`; `OS/memori-labs/integrations/openclaw/`).
- **Rust core** para performance (`OS/memori-labs/core/Cargo.toml`, `memori/_rust_core.py`).
- **BYODB** via extras: `sqlalchemy`, `cockroachdb` (`OS/memori-labs/pyproject.toml#L44-L50`; README link docs/memori-byodb/).

## Observacao de escopo

**Cloud-first**: README push pra `app.memorilabs.ai` e `MEMORI_API_KEY`. BYODB existe mas e secondary path. **Nao tem UI** de teams, governance, orchestration — e uma library pra ser consumida por outras plataformas.
