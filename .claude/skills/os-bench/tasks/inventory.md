# Task: inventory — Fact-extraction de 1 subject

## Propósito

Produzir um inventário estruturado de um subject em `OS/`. Serve como baseline reusável para qualquer `*bench-pair`, `*bench-nway` ou `*bench-absorb` que cite esse subject.

Se o inventário já existe em `OS/_bench/_inventories/{subject}/inventory.json` E foi gerado há menos de 7 dias (ver `generatedAt`), **reusar** — não regerar. Caso contrário, regenerar.

## Inputs

| Input | Required | Description |
|-------|----------|-------------|
| `subject` | sim | slug do diretório em `OS/` (ex: `gbrain`, `claude-code-main`) |
| `profile` | não | `quick` (default, ~5min) ou `full` (gera também fact-database.yaml) |

## Outputs

| File | Format |
|------|--------|
| `OS/_bench/_inventories/{subject}/inventory.json` | JSON |
| `OS/_bench/_inventories/{subject}/inventory.md` | MD |
| `OS/_bench/_inventories/{subject}/fact-database.yaml` | YAML (apenas se `profile=full`) |

## Pré-condições

- `OS/{subject}/` existe e é um diretório (verificar com `ls`)
- `templates/inventory-tmpl.md` e `templates/fact-database-tmpl.yaml` carregados

## Passos

### Passo 1: Validar subject

```
ACTION: ls OS/{subject}/
FAIL_IF: diretório não existe → HALT com erro "subject {subject} não encontrado em OS/"
```

### Passo 2: Detectar stack

Examinar manifests no root do subject:

| Manifest | Indica |
|----------|--------|
| `package.json` | Node.js/TS — ler `name`, `dependencies`, `scripts` |
| `pyproject.toml` ou `requirements.txt` | Python — ler `tool.poetry.dependencies` ou requirements |
| `go.mod` | Go |
| `Cargo.toml` | Rust |
| `pom.xml` / `build.gradle` | Java/Kotlin |
| `Gemfile` | Ruby |
| Múltiplos | Monorepo/polyglot — listar todos |

Detectar frameworks por inspection:

- Node: Next.js, Express, Ink, Bun (via `package.json`)
- Python: FastAPI, asyncio, Chroma, SwiftUI bindings
- Tell-tale files: `next.config.*`, `tsconfig.json`, `Dockerfile`, `docker-compose.yml`

### Passo 3: Coletar métricas básicas

Usar tools (Grep/Glob/Bash):

```
Bash: find OS/{subject} -type f -not -path '*/.git/*' -not -path '*/node_modules/*' -not -path '*/.venv/*' -not -path '*/dist/*' -not -path '*/build/*' | wc -l
Bash: find OS/{subject} -type f -not -path '*/.git/*' -not -path '*/node_modules/*' -not -path '*/.venv/*' -name '*.ts' -o -name '*.tsx' -o -name '*.js' -o -name '*.py' -o -name '*.go' -o -name '*.rs' | xargs wc -l | tail -1
Bash: ls -la OS/{subject}/ | head -20
Read: OS/{subject}/README.md (primeiras 100 linhas)
Bash: cd OS/{subject} && git log -1 --format='%ci %H %s' 2>/dev/null || echo "not a git repo"
```

Coletar:
- LOC ballpark
- File count
- Top-level dirs
- README tagline (primeira linha descritiva após o H1)
- Last commit date

### Passo 4: Identificar modules

Um módulo top-level é um diretório no root que contém código ou config significativo. Excluir: `.git`, `node_modules`, `.venv`, `dist`, `build`, `.next`, `target`, caches.

Para cada módulo:
- Nome
- Path relativo
- Type (inferido):
  - `app` se tem entry point CLI/HTTP
  - `package` se tem `package.json` próprio
  - `service` se tem Dockerfile próprio
  - `library` caso contrário
- LOC estimate (via `find ... | xargs wc -l`)

### Passo 5: Entry points

Buscar:
- `package.json#bin` ou `scripts#start` → CLI
- `main.py`, `__main__.py`, `app.py`, `index.ts`, `index.js`, `src/index.*` → Main
- `server.py`, `app.ts` com `app.listen` → HTTP server
- Arquivos com `mcp.server.Server` ou `@modelcontextprotocol/sdk` → MCP server

### Passo 6: Capabilities

Essa é a parte cognitiva — **ler** os docs e **inferir** capabilities observáveis.

Fontes (em ordem):
1. `README.md` sections "Features", "What it does", "Capabilities"
2. `docs/` pasta se existir
3. `CHANGELOG.md` — features marcadas como added
4. Nomes de diretórios principais (orchestration/, agents/, skills/, memory/, etc)

Para cada capability:
- Nome curto
- 1 frase descrevendo
- Evidence path — um arquivo concreto que prova a capability
- Category: `core | extensibility | integration | governance | ux`

**Regra:** se não conseguir apontar um evidence path, a capability NÃO vai pro inventário.

### Passo 7: Quality signals

- Tests: procurar `**/*.test.*`, `**/*_test.py`, `tests/`, `__tests__/`
- Linting: `.eslintrc*`, `ruff.toml`, `pyproject.toml#tool.ruff`
- CI: `.github/workflows/*.yml`
- Docs: contar arquivos em `docs/` se existir

### Passo 8: External deps (top 10)

De `package.json#dependencies` ou equivalente. Apenas top 10 por alfabética. Listar name + version + purpose (inferido do nome).

### Passo 9: Montar JSON + MD

JSON (`inventory.json`):

```json
{
  "generatedAt": "{ISO-8601}",
  "subject": "{subject_slug}",
  "path": "OS/{subject_slug}/",
  "primary_language": "{lang}",
  "secondary_languages": ["{lang}"],
  "stack": ["{framework_list}"],
  "license": "{license_or_unknown}",
  "tagline": "{from_readme}",
  "metrics": {
    "loc_estimate": 0,
    "file_count": 0,
    "top_level_dirs": [],
    "readme_lines": 0,
    "last_commit_date": "{ISO-8601 or null}",
    "github_stars": null,
    "github_contributors": null
  },
  "modules": [
    { "name": "...", "path": "...", "type": "app", "loc_estimate": 0 }
  ],
  "external_dependencies_top10": [
    { "package": "...", "version": "...", "purpose": "..." }
  ],
  "entry_points": [
    { "kind": "cli", "path": "...", "command": "..." }
  ],
  "capabilities": [
    { "name": "...", "evidence_paths": ["OS/{s}/..."], "category": "core", "description": "..." }
  ],
  "quality_signals": {
    "test_framework": "...",
    "test_file_count": 0,
    "linter": "...",
    "ci_provider": "...",
    "ci_workflow_count": 0
  },
  "documentation": {
    "readme_sections": [],
    "has_contributing": false,
    "has_architecture_doc": false,
    "docs_page_count": 0
  },
  "extension_points": {
    "plugins": { "mechanism": "...", "path": "..." },
    "hooks": { "mechanism": "...", "events": [] },
    "mcp": { "client": false, "server": false }
  },
  "unique_selling_points": ["..."],
  "limitations": [
    { "description": "...", "source": "..." }
  ],
  "confidence": "HIGH | MEDIUM | LOW",
  "extraction_method": "filesystem-scan",
  "skill_version": "1.0.0"
}
```

MD (`inventory.md`) — renderizar a partir do template em `templates/inventory-tmpl.md` substituindo placeholders.

### Passo 10: Fact-database (se profile=full)

Se `profile=full`, renderizar `templates/fact-database-tmpl.yaml` com deep data (dependencies graph, data model, api surface, rule catalog stub).

## Veto conditions

- `OS/{subject}/` não existe → HALT
- README.md vazio OU inexistente + zero capabilities observáveis → produzir inventário mínimo com confidence=LOW e notar no JSON
- Não conseguir inferir linguagem primária → ABORT com erro

## Confidence tagging

| Level | Criteria |
|-------|----------|
| HIGH | Stack detectada, 5+ capabilities com evidence, README rico, CI presente |
| MEDIUM | Stack detectada, 2–4 capabilities com evidence, README básico |
| LOW | Stack inferida, <2 capabilities com evidence, README curto ou ausente |

## Verificação final

- [ ] `OS/_bench/_inventories/{subject}/inventory.json` existe e parseia
- [ ] `OS/_bench/_inventories/{subject}/inventory.md` existe e renderiza
- [ ] Toda capability tem pelo menos 1 evidence path real
- [ ] `generatedAt` em formato ISO-8601
- [ ] Confidence declarado
- [ ] Nenhum placeholder `{...}` restou no output
- [ ] Se profile=full, fact-database.yaml também existe

---

_os-bench / inventory task / v1.0_
