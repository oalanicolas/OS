# os-bench — Quick Start

Skill autocontida para benchmarkar projetos opensource em `OS/`.
Produz um set canônico de 7 artefatos por comparação, comparando 2 ou mais repos clonados.

## Instalação

Nada a instalar — a skill já está montada em `OS/.claude/skills/os-bench/`.
O Claude executa as tasks diretamente lendo os arquivos desta pasta.

## Quick start

### 1) Comparar dois projetos (2-way)

No Claude Code:

```
Rode *bench-pair gbrain mempalace --pack memory
```

Resultado: `OS/_bench/gbrain-vs-mempalace/` com 7 artefatos.

### 2) Comparar N projetos

```
Rode *bench-nway coding-agents-8way claude-code-main codex aider OpenHands gsd-2 gstack superpowers ai-website-cloner-template --pack coding-agent
```

Resultado: `OS/_bench/coding-agents-8way/` com matrix/scorecard/executive para N colunas.

### 3) Absorver features de um no outro

Depois de ter um `bench-pair`:

```
Rode *bench-absorb gbrain mempalace
```

Gera `deep/absorption-roadmap.md` com features priorizadas.

### 4) Rodar os 6 benchmarks canônicos

```
Rode *run-all
```

Executa em sequência os 6 benchmarks definidos na skill (ver `tasks/run-all.md`).

## Dimension packs (`data/dimension-packs.yaml`)

Escolha o pack baseado no tipo de projeto:

| Pack | Use pra |
|------|---------|
| `coding-agent` | claude-code, codex, aider, OpenHands, gstack, gsd-2, superpowers |
| `memory` | gbrain, mempalace, mem0 |
| `orchestration` | BMAD-METHOD, crewAI, autogen, paperclip |
| `mcp` | mcp-servers e forks |
| `observability` | langfuse e equivalentes |
| `spec-driven` | spec-kit, get-shit-done, superpowers |
| `personal-assistant` | openclaw, hermes-agent |
| `workflow-infra` | workflow, gh-aw |

## Output

Tudo em `OS/_bench/`. Nunca fora.

```
OS/_bench/
├── INDEX.md
├── _inventories/{subject}/           # cache reusável
├── {a}-vs-{b}/                       # 2-way
│   ├── metadata.json
│   ├── inventory-{a,b}.{json,md}
│   ├── comparison-matrix.{json,md}
│   ├── scorecard.{json,md}
│   ├── gap-analysis.{json,md}
│   ├── battle-card.md
│   ├── executive-report.md
│   └── deep/
└── {topic}-Nway/                     # n-way
```

## Quality gate

Antes de declarar "benchmark pronto":

- 7 artefatos canônicos presentes
- JSONs válidos (`scripts/bench.sh validate {slug}`)
- Scores 90+ com 2+ signals
- Claims sempre com path `OS/{subject}/...` ou URL
- Gaps bidirecionais
- `INDEX.md` atualizado

## Script CLI (`scripts/bench.sh`)

Orquestrador standalone (bash puro, sem deps):

```bash
./scripts/bench.sh list                        # lista benchmarks em _bench/
./scripts/bench.sh validate <slug>             # valida quality gate
./scripts/bench.sh init <a> <b>                # cria pasta + metadata stub
./scripts/bench.sh init-nway <topic> <a> <b>…  # idem pra n-way
./scripts/bench.sh index                       # regenera INDEX.md
./scripts/bench.sh clean <slug>                # remove com confirmação
./scripts/bench.sh plan                        # mostra os 6 benchmarks planejados
```

## Princípios

1. **No invented claims** — todo claim tem path/URL
2. **Evidence-based** — score 0–100 precisa de 2+ signals
3. **Bidirectional gaps** — sempre A↔B
4. **Confidence disclosure** — HIGH/MEDIUM/LOW por dimensão
5. **Local-first** — dado do filesystem > web
6. **Deterministic paths** — slug `{a}-vs-{b}` sem data

## Troubleshooting

| Sintoma | Causa | Fix |
|---------|-------|-----|
| "subject X não existe" | typo no slug | `ls OS/` pra conferir |
| Score alto sem signal | violou princípio #2 | rebaixar pra < 90 ou adicionar signals |
| Inventário desatualizado | cache antigo em `_inventories/` | rodar `*inventory {subject}` de novo |
| Pack não bate com subject | tipo detectado errado | passar `--pack <pack>` explicitamente |

## Arquivos da skill

Ver `SKILL.md` para a lista completa e instruções de ativação.
