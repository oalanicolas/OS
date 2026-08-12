# Armadilhas e aprendizados de grafo — minerados de issues + commits reais

> **Deep dive VISA-BRAIN (prompt aplicado):** ver  
> [`visa-brain-graph-feature-lessons.md`](./visa-brain-graph-feature-lessons.md)  
> + [`visa-brain-graph-feature-lessons.citations.json`](./visa-brain-graph-feature-lessons.citations.json)  
> (gap map doutrina↔enforcement, T1–T22, backlog líquido, code-confirm).

**Date:** 2026-08-06  
**Slug:** brain-6way  
**Subjects:** LifeOS · gbrain · mempalace · mem0 · memori-labs · gsd-2  
**Sources:** issues abertas/fechadas via `gh`, CHANGELOGs e commits nos clones em `OS/`  
**Foco:** grafo / entidades / arestas / temporal / projeção / isolamento  
**Audience:** VISA-BRAIN / evidence graph design (clean-room — não copiar código dos peers)
> **Bottom line:** os 6 não falharam por “não ter grafo” — falharam por **extract silencioso, over-typing, dual-SoT, temporal frágil, isolamento furado e métricas mentirosas**. O VISA-BRAIN evita a maior parte se tratar grafo como **projeção reconciliada com receipts e fail-closed na conclusão**, não como feature de ranking.

---

## Clones e tips de referência (no momento da mineração)

| Subject | Path | Tip (aprox.) |
|---------|------|----------------|
| gbrain | `OS/gbrain` | `15b9863d1` v0.42.73.2 |
| mempalace | `OS/mempalace` | `8ab251c` |
| LifeOS | `OS/lifeos` | `27c94f9` |
| memori | `OS/memori-labs` | `538b61f` |
| gsd-2 | `OS/gsd-2` | `33c00aaff` |
| mem0 | `OS/mem0` | `4a0a9a92` |

Artefatos irmãos neste pack:

- `executive-report.md` — ranking + product framing
- `comparison-matrix.md` — jobs e feature classes
- `scorecard.md` / `scorecard.json` — pack memory quantitativo
- `_inventories/*/` — inventários por subject

---

## Como ler isto

| Símbolo | Significado |
|--------|-------------|
| ☠️ | Bug de classe **silenciosa** (parece ok, dados errados) |
| 🔒 | Isolamento / multi-tenant / escopo |
| ⏱ | Temporal / supersession |
| 🔁 | Dual-write / dual-SoT / projeção |
| 📊 | Métrica de saúde **mentirosa** |
| 🧭 | API “documentada” ≠ comportamento real |

Cada item: **armadilha → evidência → o que o VISA deve fazer**.

---

## 1. Extração de arestas que falha em silêncio

### ☠️ Whitelist / ontologia hard-coded no extractor

| Evidência | Detalhe |
|-----------|---------|
| **gbrain #3038** (closed) | `DIR_PATTERN` com ~16 dirs de “wiki pessoal”; corpus importado de 4 370 páginas → **21 edges, 99,7% orphan, sem erro** |
| **gbrain #2576 / #3188** | dirs fora da lista (`ops/`, `sources/` plural) → links caem no chão |
| **gbrain #3190** (open) | schema-pack custom com `link_types` + `frontmatter_links` **decorativo** — extract continua preso ao whitelist hardcoded |

**Aprendizado:** extractor que só “funciona no corpus do autor” é a armadilha mais cara.

**VISA:** ontologia de arestas **declarativa e versionada** no workspace/produto; zero whitelist de path que mate edges; se 0 arestas em lote com N candidatos → **fail/warn com contagem**, nunca “done 0”.

### ☠️ Over-typing sem evidência no texto

| Evidência | Detalhe |
|-----------|---------|
| **gbrain #3466** (closed) | `people/→companies/` → sempre `works_at` **sem ler o texto** → **19 497** “empregos” falsos (artista “works_at” museu) |
| Commit `dba0ae7b1` | `fix(extract): stop asserting works_at from bare people/→companies/ adjacency (#3466)` |

**Aprendizado:** tipo de aresta sem trecho/locator = **fato fabricado em escala**.

**VISA:** aresta tipada (`SUPPORTS`, `ROLE_AT`, …) **só com base textual ou registo canónico**; adjacência de path/dir no máximo vira `RELATED_TO` / candidate, nunca emprego/autoria.

### ☠️ Paths de extract divergentes (fs vs db vs stale vs dream)

| Evidência | Detalhe |
|-----------|---------|
| **gbrain #3607** | fs-mode 0 edges; **db-mode** 1 533 no mesmo corpus |
| **gbrain #3799** (closed) | `extract --stale` “target doesn't exist” com ambos os slugs existentes |
| **gbrain #1184** (open) | dream cycle extract **silently no-ops** (0 links) enquanto extract manual funciona |
| **gbrain #2849** (open) | webhook sync `noExtract` default true → bookmark avança, **edges permanentemente stale** |

**Aprendizado:** um “pipeline único” com N entrypoints que divergem = grafo podre em produção.

**VISA:** **um** reconciler de grafo; todo ingest chama o mesmo; watermark/version stamp (`LINK_EXTRACTOR_VERSION_TS` do gbrain) + teste de paridade entre paths; nunca “sync ok” sem receipt de extract.

### ☠️Slugify / basename / CJK

| Evidência | Detalhe |
|-----------|---------|
| **gbrain #1964** | `[[AI 3.0]]` no MD vs slug `ai-3.0` no store → 0 edges |
| **gbrain #2367** | `normalizeBasename` strip CJK → resolução quebrada |
| **gbrain #1846** | bare-name resolver dropa edges em targets **unambiguous** |

**VISA:** normalização canónica única (slugify + locale); teste com nomes BR/acentos; candidatos não resolvidos → **lista auditável**, não drop silencioso.

### ☠️ Edges aditivas sem purge

| Evidência | Detalhe |
|-----------|---------|
| **gbrain #3674** (open) | `--by-mention` só **adiciona**; re-scan após fix de tokenizer → **estale + corretas** juntos |

**VISA:** re-extract = **reconcile set** (add + remove stale por `link_source`/origem), como o gbrain já faz em `reconcileLinks` para markdown — e **não** só insert batch.

---

## 2. Soft-delete, saúde e UI mentem sobre o grafo

### ☠️ Soft-deleted ainda no grafo

| Evidência | Detalhe |
|-----------|---------|
| **gbrain #1702, #3754** (open) | `get_links` / `backlinks` / `graph-query` **não filtram** `deleted_at`; search/list filtram |
| Commit doctor/health | `fix(engine): exclude soft-deleted from getHealth` (#1305) — **só parte** da superfície |

**VISA:** **toda** leitura de grafo (traversal, export, dashboard) com o mesmo predicado de lifecycle; teste “delete unit → some em traversal”.

### 📊 Health score contraditório

| Evidência | Detalhe |
|-----------|---------|
| **gbrain #3591** | store com **13 908** links; `link_coverage: 0` + `most_connected` zero; **e** `link_density_score: 25` full marks no mesmo payload |

**VISA:** métricas de grafo **query no mesmo store** que o traversal; se cobertura e density discordam → **fail do health**, não score “bonito”.

### 🧭 CLI/renderer ≠ traversal

| Evidência | Detalhe |
|-----------|---------|
| **gbrain #2931** (open) | `direction both` retorna inbound no engine; **tree printer esconde** |
| **gsd #5148** | `gsd graph` no CLI; slash `/gsd graph` **não registrado** |

**VISA:** testes no **artefato que o agent/operador vê**, não só na API interna.

---

## 3. Multi-source / multi-workspace (isolamento)

### 🔒 Cross-source edges sumindo ou vazando

| Evidência | Detalhe |
|-----------|---------|
| **gbrain #2589** (open) | wikilink resolve cross-source; edge **drop silencioso** se target não está no mesmo source/`default` |
| **gbrain #1747** | extract 0 wikilinks em source não-default |
| Commits security | `fix(security): close cross-source and scope-escalation gaps` |
| **mem0 #5439 / #5597** | entity merge **cruza** `user_id`/`agent_id` (similarity ≥ 0.95) → leak cross-scope |
| **memori #404** | headers MCP de attribution manuais → **mix de projetos** |
| Commit memori `e10b57e` | docs project-scoped attribution |

**VISA:**

1. case root / workspace em **toda** aresta e hop;
2. merge de entidade **nunca** só por similaridade de embedding;
3. attribution obrigatória e **não vazia** (memori #578: `reject empty strings in attribution`);
4. cross-workspace **impossível** por construction, não por “não se esqueça do header”.

### 🔒 Cache keyed por path string (macOS)

| Evidência | Detalhe |
|-----------|---------|
| **mempalace #1372 / CHANGELOG** | KG cache: `/palace` vs `/Palace` vs symlink → **dois caches**, stale read |
| Fix | `realpath` + `normcase` |

**VISA:** chave de projeção = **canonical absolute path** (ou case id), nunca string crua do user.

### 🔒 Singleton KG em multi-tenant

| Evidência | Detalhe |
|-----------|---------|
| **mempalace CHANGELOG (#1136)** | `_kg` module-level → `MEMPALACE_PALACE_PATH` rotacionado → **SQLite errado** |

**VISA:** zero singleton global de grafo de caso; um grafo por workspace connection.

---

## 4. Temporal e supersession (classe P0)

### ⏱ Intervalo invertido = row “fantasma”

| Evidência | Detalhe |
|-----------|---------|
| **mempalace #1214** | `valid_to < valid_from` **armazenado** mas **invisível a todo as_of** — P0 data integrity |
| Fix | reject no `add_triple` com `ValueError` claro |

**VISA:** validator no write; fixture “intervalo invertido → rejeita”.

### ⏱ Invalidate+add com date-only = dois fatos no mesmo dia

| Evidência | Detalhe |
|-----------|---------|
| **mempalace CHANGELOG + `supersede()`** | invalidate+add com `D` date-only → as_of `D` retorna **ambos** |
| Commit `9815f0a` | half-open `[from, to)` |
| #1913 | `supersede()` atômico no mesmo instante |

**VISA:** **um primitivo** de supersession (como `supersede`); proibir hand-roll invalidate+add sem shared boundary; half-open documentado e testado.

### ⏱ Datas “natural language” aceitas → vazio silencioso

| Evidência | Detalhe |
|-----------|---------|
| **mempalace #1164 / #1167** | `"March 2026"` / `"yesterday"` → empty result; **indistinguível** de “sem fato” |
| Fix | `sanitize_iso_temporal` + raise |

**VISA:** parse estrito de datas de aresta; erro tipado ≠ empty set.

### ⏱ ADD-only sem UPDATE → contradição eterna

| Evidência | Detalhe |
|-----------|---------|
| **mem0 #4956** | v3 extraction **ADD-only** → “works at A” + “works at B” convivem; retrieval devolve lixo |
| **gsd** | `supersedes` / `superseded_by` no memory graph — modelo melhor para tribal knowledge |

**VISA:** estado mutável (cargo, status, contagem) **exige** lifecycle; não só append de CLM/edge.

---

## 5. Dual-write / dual-SoT (o maior anti-padrão de “grafo + MD + SQL”)

### 🔁 Grafo lê MD; memória canónica está no SQL

| Evidência | Detalhe |
|-----------|---------|
| **gsd #5149** | graph only from markdown; **SQLite memories** é SoT (ADR-013) → grafo **não vê** capture_thought |
| **gsd #5755** | cutover: stop dual-write, memories canonical; MD = **projeção** |
| **gsd #6342** | capture sem `structuredFields` → projeção KNOWLEDGE.md **tabelas vazias** com 40+ memórias |
| **gsd #6414** | scanner de consolidação **antes** do DB open → “12/12 não migrados” **falso** |

**VISA:**

- **uma** autoridade de escrita (registers / ledger);
- grafo = projeção regenerável **só** dessa autoridade;
- nunca graph-from-MD e truth-from-SQLite em paralelo sem cutover explícito;
- health de “migration complete” só com DB open + receipt.

### 🔁 Feature “shipada” mas sem deps / sem wire

| Evidência | Detalhe |
|-----------|---------|
| **LifeOS #1605** | `MemoryGraph.ts` importa graphology; **package.json só tem yaml** → graph dead on install |
| **LifeOS #1172** | dashboard “0 edges” com corpus cheio (UX de grafo morto) |
| **LifeOS #1255** | retriever **só top-level** de KNOWLEDGE → subdirs invisíveis |
| **LifeOS #1573** | `getRelevantContext` no Telegram, **não** no CLI principal |
| **gsd #5148** | graph CLI existe; slash não |

**VISA:** smoke test de **install fresco** → graph tool + projection; feature sem wire no path principal = bug P0.

### 🔁 Escrita “ok” que não persiste

| Evidência | Detalhe |
|-----------|---------|
| **LifeOS #1409** | templates sem `BEGIN ENTRIES` → write “sucesso”, read **0** |
| **LifeOS #1761** | shrink guard só catástrofe; **erosão lenta** da hot memory passa no guard |
| **gsd #4967** | `capture_thought` engole SQL error → `create_failed` genérico; auto-mode **continua** |
| **gsd #3372** | LLM extract `return null` sem modelo → 0 memories, zero feedback |

**VISA:** write path com **read-back** ou row count; erros de store **nunca** engolidos em silent null; “reviewed/promoted” exige extract + locator, não só status.

---

## 6. Entidade: merge, tipo e ambiguidade

### ☠️ Merge por similaridade 0.95

| Evidência | Detalhe |
|-----------|---------|
| **mem0 #5438** | mesmo surface form, sentidos diferentes → merge |
| **mem0 #5587** | person “Apple” + company “Apple” mergeados |

**VISA:** identidade só com **alias registry + tipo + workspace**; embedding = candidate, nunca merge automático canónico.

### ☠️ Entity detection polui o grafo

| Evidência | Detalhe |
|-----------|---------|
| **mempalace CHANGELOG #1605** | “system”, “user”, “memory”… viram “people” |
| **#1557** | case-insensitive no init, **case-sensitive no mine** → “Aya” ≠ “aya” |
| Commit ReDoS | `fix(entity): defuse entity-candidate ReDoS` (#2063) |

**VISA:** denylist de termos genéricos; matching case-fold **único** em todos os paths; limites de regex.

---

## 7. Síntese / think / graph signals (não confiar cegamente)

### 🧭 Grafo no gather ≠ páginas hidratadas

| Evidência | Detalhe |
|-----------|---------|
| **gbrain #2903** (open) | `query` rank #1; `think` **Pages:0**, Graph:1 — resposta “no information” |
| **gbrain #2365** | free-form think **sem auto-anchor**; query relacional já auto-walk |

**Aprendizado:** ter arestas no store **não** garante que a síntese as use; stream graph e stream pages podem divergir.

**VISA:** preflight: seed entities → traversal → **reopen extracts**; se graph hit sem unit reaberta → incompleto.

### ☠️ Flags que gravam nada

| Evidência | Detalhe |
|-----------|---------|
| **gbrain #2556** (open) | `think --take` → Takes:0, silencioso |
| Commit dream | `honor configured 0` (#3552) — config “0” virava default |

**VISA:** flag de persistência sem side-effect = **exit non-zero** ou erro explícito.

### Graph signals fail-open

Código gbrain (`src/core/search/graph-signals.ts`): erro → resultados inalterados; só reordena top-K (adjacency ×1.05, cross-source ×1.10, session demote ×0.95).

**VISA:** OK para **rank**; **nunca** fail-open para gate de conclusão material. Cross-source hit count ≠ independência probatória.

---

## 8. Concorrência e races no grafo/entity store

| Evidência | Detalhe |
|-----------|---------|
| **mem0 #6243** | `_upsert_entity` RMW **sem lock** → lost `linked_memory_ids` |
| **gbrain operations** | advisory lock `auto_link:${slug}` (eles **aprenderam** a race de concurrent put_page) |
| **mempalace** | file-level lock no mine concurrente (#784) |
| **LifeOS #1711** | review-state.json **global** → N sessões corrompem contadores |

**VISA:** reconcile de edges sob lock/lease por unit; estado de run **por session/run_id**, nunca global de máquina.

---

## 9. Retrieval “hybrid” que descarta hits

| Evidência | Detalhe |
|-----------|---------|
| **mem0 #5742** | hybrid: BM25/entity scoreados mas **só top-k semântico** entra no rank final |
| **gsd #4497** | FTS5 ausente → LIKE silencioso, sem stemming/BM25 |

**VISA:** união de listas **explícita** antes de fundir; degradação FTS → **flag no receipt** (“degraded”), não LIKE quieto.

---

## 10. mem0: remover o grafo externo (lição de produto)

| Evidência | Detalhe |
|-----------|---------|
| Commits v3 | `graph store removal`, `delete remaining graph test files` |
| **#6442** | “por que removeram Neo4j?” |
| **#6591** | AGENTS.md ainda documenta graph removido |
| Histórico | soft-delete relations (#4188), Cypher hyphen (#4154), LLM config fallback (#4466), prefix entity merge (#5630) |

**Aprendizado:** grafo opcional pluggable + LLM triples + multi-backend = **custo de bugs permanente**; eles **sairam** do path OSS.

**VISA:** não adotar Neo4j sidecar; grafo nativo workspace-local com schema pequeno.

---

## Catálogo de armadilhas → testes de regressão VISA (checklist)

Use isto antes de “shipar” qualquer feature de grafo:

| # | Armadilha a evitar | Teste / gate |
|---|-------------------|--------------|
| T1 | Extract 0 edges sem alarme | Se `candidates > 0 && edges == 0` → fail run |
| T2 | Over-type sem texto | Fixture artist→museum; assert **não** ROLE_AT/employment |
| T3 | Paths extract divergentes | Mesmo corpus: batch A ≡ batch B (hash de edges) |
| T4 | Soft-delete no traversal | Unit deleted → ausente de graph + export |
| T5 | Health mentirosa | coverage query ≡ count(*) store |
| T6 | Cross-workspace edge | impossível por schema/FK |
| T7 | Attribution vazia | reject `""` |
| T8 | valid_to < valid_from | write reject |
| T9 | supersede date-only dual-truth | as_of boundary = 1 fact only |
| T10 | Dual SoT MD+SQL | graph rebuild só de ledger/extracts canónicos |
| T11 | Merge por embedding | identity só com tipo+alias+workspace |
| T12 | Silent null on write fail | exception propagated + no “complete” |
| T13 | Concurrent reconcile | two writers same unit → no lost edges |
| T14 | Degraded search | FTS fail → receipt `degraded:true` |
| T15 | Synthesis without reopen | graph hit sem extract → block material conclusion |
| T16 | Stale edges after re-extract | reconcile removes old link_source set |
| T17 | Future watermark masks edits | version stamp ≤ now (gbrain D4) |
| T18 | Install fresco | graph deps + one smoke traversal |

---

## Top 12 lições (ordem de severidade para o VISA)

1. **Silêncio é o inimigo** — 0 edges, 0 takes, health 100 com grafo vazio, extract dream no-op: todos os peers sangraram nisto.
2. **Tipo de aresta sem evidência é alucinação em massa** (#3466).
3. **Whitelist/ontologia do autor no extractor** (#3038) torna o grafo inútil em corpora reais (e em imigração o vocabulário é outro).
4. **Um reconcilador, N entrypoints iguais** (stale/fs/db/webhook/dream).
5. **Temporal half-open + supersede atômico** — mempalace pagou caro para descobrir; copiar o **invariante**, não o SQLite.
6. **Soft-delete incompleto** em traversal é bug de classe “fantasma no counsel”.
7. **Dual-write MD/SQL/grafo** — gsd ADR-013: uma canónica, resto projeção.
8. **Merge por similarity = leak e falsa identidade** (mem0).
9. **Isolation é write-path + read-path + cache key + no singleton**.
10. **Métrica de grafo deve ser a mesma query do produto** (#3591).
11. **Graph boost ≠ prova**; fail-open só no rank.
12. **Feature sem wire no path principal** (LifeOS #1573, #1605) = não existe.

---

## O que **não** reimplementar (já queimaram)

| Evitar | Por quê (evidência) |
|--------|---------------------|
| Neo4j/Memgraph opcional + Cypher de LLM | mem0 removeu do OSS; bugs Cypher/hyphen/cleanup |
| DIR_PATTERN hard-coded de “wiki pessoal” | #3038 |
| `works_at` por adjacência de pasta | #3466 |
| Dual-write decisions+memories+MD sem cutover | gsd #5755/#5149 |
| Entity merge threshold único 0.95 | #5438/#5587 |
| KG singleton + path string cache | mempalace #1136/#1372 |
| `invalidate`+`add` manual com date-only | supersede commit |
| Health/score composto que mascara zeros | #3591 |
| Extract assíncrono que pode ser skipped por default | #2849 webhook |
| Attribution opcional/manual por header | memori #404 |

---

## Índice de issues/commits citados (por subject)

### gbrain

| ID / ref | Tema |
|----------|------|
| #3038, #2576, #3188, #3190 | whitelist DIR_PATTERN / schema-pack decorativo |
| #3466 + commit `dba0ae7b1` | over-typing `works_at` |
| #3607, #3799, #1184, #2849 | extract path divergence / dream no-op / webhook stale |
| #1964, #2367, #1846 | slugify / CJK / bare-name |
| #3674 | mentions additive without purge |
| #1702, #3754, #1305 | soft-delete in graph reads |
| #3591 | health score contradiction |
| #2931 | direction both UI bug |
| #2589, #1747 | cross-source silent drop |
| #2903, #2365 | think gather vs graph |
| #2556 | `--take` silent no-op |
| security commits | cross-source / scope-escalation |
| `graph-signals.ts` | top-K only, fail-open, boosts |

### mempalace

| ID / ref | Tema |
|----------|------|
| #1214 | inverted valid_to/from invisible |
| #1913 + `9815f0a` | supersede + half-open |
| #1164, #1167 | NL dates → empty silent |
| #1372 / #1383 | path cache duplicate KG |
| #1136 | module-level KG singleton |
| #1605, #1557 | entity pollution / case mismatch |
| #2063 | ReDoS entity candidates |
| #784 | concurrent mine lock |

### LifeOS

| ID / ref | Tema |
|----------|------|
| #1605 | graphology deps missing |
| #1172 | dashboard empty graph UX |
| #1255 | top-level-only index |
| #1573 | retrieval not on main CLI path |
| #1409 | hot-layer markers missing |
| #1761 | slow erosion past shrink guard |
| #1711 | global review-state race |

### memori-labs

| ID / ref | Tema |
|----------|------|
| #404 | project-scoped attribution |
| #578 + `0d40a64` | empty attribution rejected |
| #98 | auto_ingest infinite loop |
| #434 | conversation injection vs tool-calling |
| #590 | BYODB still hits cloud |
| #362 | empty recall leaks schema |

### gsd-2

| ID / ref | Tema |
|----------|------|
| #5149, #5755 | graph MD vs SQLite SoT / dual-write cutover |
| #6342 | structuredFields missing → empty projection |
| #6414 | consolidation scanner before DB open |
| #5148 | slash command not wired |
| #4497 | FTS5 silent LIKE degrade |
| #4967, #3372 | silent write/extract failure |

### mem0

| ID / ref | Tema |
|----------|------|
| #5438, #5587 | entity merge by similarity / type |
| #5439, #5597 | cross-scope entity linking |
| #6243 | entity store TOCTOU |
| #5742 | hybrid drops keyword-only hits |
| #4956 | ADD-only stale contradictions |
| #6442, #6591 | graph removal from OSS + doc drift |
| v3 commits | graph store removal |

---

## Ligação com práticas de grafo (confirmação de código)

Documento complementar da mesma sessão de análise (código em `OS/`, não só bench):

| Prática | Confirmada no código? | Armadilha relacionada acima |
|---------|----------------------|------------------------------|
| Write-path zero-LLM edges | Sim (gbrain) | §1 over-typing, whitelist |
| Graph = rank, não veredito | Sim (graph-signals) | §7 fail-open / cross-source ≠ proof |
| Temporal as-of / supersede | Sim (mempalace) | §4 half-open, inverted, NL dates |
| Declared edges first | Sim (LifeOS) | §5 dual-SoT, missing deps |
| Attribution / scope | Sim (memori, gbrain) | §3 isolation |
| Fixed point + unlinked search | **Não nos 6** (hop 2–5) | VISA deve liderar, não copiar hop fixo |
| Dual SoT | Anti-padrão (gsd) | §5 |
| External graph DB | Removido OSS (mem0) | §10 |

---

## Relação com o resto do pack

| Se você quer… | Leia |
|---------------|------|
| Ranking memory pack | `scorecard.md` |
| Job de produto de cada peer | `comparison-matrix.md` / `executive-report.md` |
| Inventário por subject | `_inventories/<subject>/inventory.md` |
| **Evitar bugs que eles já tiveram em grafo** | **este arquivo** |

---

## Nota de método

- Issues obtidas com `gh issue list` / `gh issue view` nos repos públicos apontados pelo clone.
- Commits via `git log --grep` e leitura de CHANGELOG (especialmente mempalace).
- Não substitui revalidação se o tip local divergir de `origin`.
- Clean-room: **invariantes e testes**, nunca adapters ou cópia de schema/API dos peers.

---

## Closing

> Silêncio na extract, tipo sem texto, dual-SoT, temporal frágil, isolamento por header e health mentirosa são as cinco famílias de falha que o pack `brain-6way` documenta com sangue de produção.
>
> VISA-BRAIN: **grafo = projeção reconciliada + receipt + fail-closed na conclusão material**.

---

# PROMPT — Feature lessons from GitHub projects (full report)

Reusable prompt to produce reports **of the same class** as this file: evidence-backed pitfalls and learnings extracted from real GitHub projects (issues, PRs, commits, CHANGELOG, code), not blog marketing.

Copy the block below, fill the `{{PLACEHOLDERS}}`, and run with an agent that has: local clone access (or `gh` + network), `git`, `gh issue`/`gh pr`, and permission to write the report path.

---

## Prompt (copy from here)

```markdown
# Role

You are a forensic product/engineering researcher. Your job is to extract **implementation lessons** about a **feature class** from one or more real open-source (or local) GitHub projects — especially **mistakes already paid for in production** — and write a durable markdown report.

You do **not** write a marketing comparison or a star ranking of “who is best.”
You do **not** copy code, schemas, APIs, or brand names into a product as dependencies.
You **do** abstract **invariants, failure modes, tests, and anti-patterns** that a downstream system can re-implement cleanly (clean-room).

# Goal

Produce a report equal in depth and structure to the reference:
- pitfalls grouped by failure family (silent failure, isolation, temporal, dual-SoT, metrics lies, API≠behavior, races, …)
- each pitfall: **trap → evidence (issue/PR/commit/CHANGELOG/code path) → what the consumer system must do**
- regression checklist (T1…Tn) as testable gates
- top N lessons by severity for the consumer domain
- “do not reimplement” table (already burned)
- index of cited issues/commits per subject
- method note + tip SHAs so the report is re-auditable

# Inputs (fill before run)

| Field | Value |
|-------|--------|
| **Feature class** | `{{FEATURE_CLASS}}` e.g. knowledge graphs, memory write-path, evidence packets, hybrid search, multi-tenant isolation, soft-delete, temporal facts, agent action logs |
| **Consumer system** | `{{CONSUMER}}` e.g. VISA-BRAIN evidence graph / case ops — domain constraints and non-goals |
| **Subjects** | `{{SUBJECTS}}` list of `{name, local_path?, github_url, default_branch}` — 1–N projects |
| **Local roots** | `{{LOCAL_ROOTS}}` e.g. `OS/gbrain`, `OS/mempalace` — prefer code + git history over docs alone |
| **Output path** | `{{OUTPUT_PATH}}` e.g. `OS/_bench/<slug>/feature-pitfalls-and-lessons.md` |
| **Related pack** | `{{PACK_PATH}}` optional prior n-way bench (executive-report, inventories) |
| **Time window** | `{{SINCE}}` e.g. 2025-01-01 — for `git log` / issue filters |
| **Language** | `{{LANG}}` report language (pt-BR or en) |
| **Clean-room rule** | Always: abstract only; no adapters; no running peer runtimes on consumer private data |

# Non-negotiable research rules

1. **Evidence > narrative.** Every claim needs at least one of: issue number + title, PR, commit SHA + subject, CHANGELOG bullet, or file:line in the clone.
2. **Prefer closed bugs and fix commits** over README promises. Open bugs count if verified (repro text or code inspection).
3. **Confirm in code** when the issue and docs disagree; mark **DOC-STALE** if docs claim a feature removed or unfinished.
4. **Separate product job from feature class.** A Life OS and a vector SDK may share “graph” vocabulary with different jobs — say so.
5. **Silent failure is a first-class category.** 0 edges / 0 writes / green health with empty store / swallow exceptions are higher severity than loud crashes.
6. **No invented metrics.** If BrainBench / LongMemEval / custom benches appear, cite the file or README line; do not invent numbers.
7. **Do not leak secrets or private case data** from the consumer environment into the report.
8. **If a subject has no local clone**, use `gh` + shallow clone only if allowed; otherwise mark confidence **LOW** for that subject and say what was not inspected.
9. **Parallelize** inventory of subjects, but **serialize** the final synthesis so cross-subject failure families are merged (not six disjoint dumps).

# Method (execute in order)

## Phase 0 — Scope freeze

1. Restate the feature class in one sentence and list **in-scope surfaces** (e.g. edge extract, traversal, temporal validity, health metrics, multi-tenant keys).
2. List **out-of-scope** (e.g. voice UI, install marketing) unless it blocks the feature.
3. Map each subject to a **product job** (one line): what the project optimizes for.

## Phase 1 — Locate feature surface in each clone

For each subject:

1. Record `git rev-parse HEAD` and remote URL.
2. Find code paths: `find` / `rg` for keywords derived from the feature class (and synonyms).
3. Find schema/migrations, CLI/MCP ops, doctor/health checks, tests with the feature name.
4. Write a short inventory (capabilities claimed vs files that implement them).

## Phase 2 — Mine failure evidence

For each subject, run (adapt keywords to `{{FEATURE_CLASS}}`):

```bash
# Issues (GitHub)
gh issue list --state all --limit 50 \
  --search "{{FEATURE_KEYWORDS}} OR bug OR silently OR race OR stale OR leak"

# Optional: PRs
gh pr list --state all --limit 30 --search "{{FEATURE_KEYWORDS}}"

# Commits
git log --oneline --all --since="{{SINCE}}" \
  --grep='{{FEATURE_KEYWORDS}}' -i | head -80

# CHANGELOG / docs
rg -n -i '{{FEATURE_KEYWORDS}}|breaking|fix|silent|race|stale' CHANGELOG.md docs/ || true
```

Pull bodies for the **highest-signal** issues (closed bugs with repro, P0/P1 labels, fix commits linked):

```bash
gh issue view <N> --json title,body,state,labels,closedAt
```

Keyword seeds (edit per feature class):

| Feature class | Seed terms (examples) |
|---------------|------------------------|
| Graphs / edges | graph, edge, link, wikilink, hop, traverse, related, triple, kg |
| Temporal | valid_from, valid_to, as_of, supersede, invalidate, bitemporal |
| Isolation | cross-source, tenant, scope, user_id, attribution, workspace, leak |
| Memory write | extract, capture, reconcile, dual-write, projection, silent, FTS |
| Soft-delete | deleted_at, soft-delete, orphan, tombstone |
| Search/rank | hybrid, RRF, BM25, rerank, fail-open, top-k |
| Entity | merge, alias, disambiguation, similarity, entity store |

## Phase 3 — Code confirmation (spot-check)

For each high-severity claim:

1. Open the cited file or search the symbol.
2. Confirm whether the bug is still open, fixed, or only partially fixed (e.g. health fixed but traversal not).
3. Note **fail-open vs fail-closed** behavior on error paths.
4. Note **default flags** that skip the feature (e.g. `noExtract` default true).

## Phase 4 — Cluster into failure families

Merge across subjects into families (add/remove as evidence dictates):

1. Silent extract / silent write / silent drop
2. Over-typing or wrong semantics without evidence
3. Divergent entrypoints (fs vs db vs async vs webhook)
4. Soft-delete / lifecycle incomplete on feature surface
5. Health / metrics / UI lying about store state
6. Multi-tenant / scope / cache-key / singleton isolation bugs
7. Temporal / supersession / ADD-only contradiction
8. Dual-write / dual-SoT / projection without cutover
9. Feature shipped without deps or without wire on primary path
10. Entity merge / identity pollution
11. Synthesis/retrieval not consuming the feature store
12. Concurrency / RMW races
13. Hybrid retrieval discarding non-primary lists
14. Doc/API surface removed or stale

Each family section must include a table: Evidence | Detail.

## Phase 5 — Consumer mapping

For `{{CONSUMER}}`:

1. For each family: **what to do** (invariant + preferred gate), not “integrate project X.”
2. Build checklist **T1…Tn** (testable: inputs, expected fail/pass).
3. **Top 12 lessons** ordered by severity for the consumer domain (not by peer star count).
4. **Do not reimplement** table (burned approaches).
5. Optional: map to existing consumer doctrine files if paths are provided.

## Phase 6 — Write the report

Write to `{{OUTPUT_PATH}}` in `{{LANG}}` with this **exact skeleton** (sections may grow; do not drop required ones):

```markdown
# Armadilhas e aprendizados — {{FEATURE_CLASS}}
# mined from issues + commits ({{SUBJECTS short list}})

**Date:** …
**Subjects:** …
**Sources:** gh issues/PRs, git log, CHANGELOG, code paths
**Consumer:** {{CONSUMER}}
**Confidence:** HIGH | MEDIUM | LOW (per subject if mixed)

> **Bottom line:** 3–6 sentences.

## Clones e tips de referência
(table: subject | path | tip SHA | remote)

## Como ler isto
(symbols legend: silent / isolation / temporal / dual-SoT / metrics / API≠behavior)

## 1…N — Failure families
### each: trap, evidence table, aprendizado, VISA/consumer action

## Catálogo → testes de regressão (T1…Tn)

## Top 12 lições (por severidade para o consumer)

## O que não reimplementar

## Índice de issues/commits citados (por subject)

## Ligação com práticas confirmadas no código
(table: practice | confirmed? | related family)

## Relação com packs/benches irmãos (if any)

## Nota de método
(how mined; clean-room rule; staleness caveat)

## Closing
(quote-style one-paragraph takeaway)
```

Also produce a **one-page executive blurb** at the top after the bottom-line (optional table: Top traps × which subjects hit them).

# Quality bar (fail the run if unmet)

- [ ] ≥ 15 distinct issue/PR/commit citations across the report (or explicit “thin subject” notes if a repo has almost no history)
- [ ] Every Top-12 lesson maps to at least one evidence row
- [ ] At least one **code-confirmed** finding that differs from README marketing
- [ ] At least three **silent-failure** class items if the feature has a write or extract path
- [ ] Checklist items are **mechanically testable** (no “be careful”)
- [ ] No recommendation to vendor-lock or sidecar-run peer runtimes on consumer private data
- [ ] Tips SHAs recorded; method reproducible
- [ ] Consumer section does not paste private case facts

# Output packaging

1. Main report: `{{OUTPUT_PATH}}`
2. If under a bench pack, add a one-line pointer from `executive-report.md` § Artefatos (only if that file exists and user allowed edit)
3. Optional JSON sidecar (same stem `.citations.json`): list of `{subject, kind: issue|pr|commit|path, id, title, url?}` for re-audit

# Anti-patterns in *your* report (do not do these)

- Ranking subjects by stars or by a memory pack score as if it answered feature quality
- “Just use Neo4j/X like project Y”
- Copying code blocks large enough to be a derivative implementation
- Treating open feature requests as proven designs
- Claiming “fixed in main” without SHA or release tag
- Collapsing all subjects into one without labeling which project taught which lesson

# Kickoff sentence (agent starts here)

Research `{{FEATURE_CLASS}}` across `{{SUBJECTS}}` under `{{LOCAL_ROOTS}}` since `{{SINCE}}`. Mine issues, fix commits, and code paths for production pitfalls. Write a clean-room lessons report for `{{CONSUMER}}` to `{{OUTPUT_PATH}}` following the skeleton and quality bar above. Prefer silent failures, isolation bugs, dual-SoT, temporal errors, and lying health metrics. Abstract invariants and regression tests only — no adapters, no peer runtime integration.
```

---

## Prompt — filled example (this report)

| Field | Example value used for *this* file |
|-------|-------------------------------------|
| FEATURE_CLASS | knowledge graphs / typed edges / temporal KG / graph signals / projection |
| CONSUMER | VISA-BRAIN evidence graph + investigate-case-evidence |
| SUBJECTS | gbrain, mempalace, LifeOS, mem0, memori-labs, gsd-2 |
| LOCAL_ROOTS | `OS/{gbrain,mempalace,lifeos,mem0,memori-labs,gsd-2}` |
| OUTPUT_PATH | `OS/_bench/brain-6way/graph-pitfalls-and-lessons.md` |
| PACK_PATH | `OS/_bench/brain-6way/` |
| SINCE | 2025-01-01 |
| LANG | pt-BR |
| FEATURE_KEYWORDS | `graph OR edge OR link OR wikilink OR hop OR temporal OR valid_from OR supersede OR cross-source OR entity OR attribution OR dual-write OR soft-delete` |

---

## Prompt — shorter slash form

For a quick re-run on a **new** feature class with the same six clones:

```text
/feature-pitfalls
feature: {{FEATURE_CLASS}}
consumer: VISA-BRAIN
subjects: gbrain, mempalace, lifeos, mem0, memori-labs, gsd-2
roots: /Users/…/OS
out: OS/_bench/{{slug}}/{{feature}}-pitfalls-and-lessons.md
since: 2025-01-01
lang: pt-BR
follow: OS/_bench/brain-6way/graph-pitfalls-and-lessons.md (structure + quality bar)
```

Expand `/feature-pitfalls` to the full prompt in the previous section; do not skip Phases 2–3 (issues + code confirm).

---

## Operator checklist (human)

Before launching the agent:

1. [ ] Clones present and roughly up to date (`git fetch` if claims must be current)
2. [ ] `gh auth status` works for private repos if needed
3. [ ] Feature class and consumer non-goals written in one paragraph
4. [ ] Output path outside private case trees (`VISA-LENDARIO/` never)
5. [ ] After run: spot-check 3 citations open in browser/clone
6. [ ] Promote only **invariants + T-tests** into product backlog — not peer APIs
