# Armadilhas e aprendizados — knowledge graphs / typed edges / temporal KG / graph signals / projection

**mined from issues + commits (gbrain · mempalace · LifeOS · mem0 · memori-labs · gsd-2)**

| Field | Value |
|-------|--------|
| **Date** | 2026-08-06 |
| **Feature class** | Knowledge graphs, typed edges, temporal KG, graph signals, projections, entity identity |
| **Consumer** | VISA-BRAIN evidence graph + `$investigate-case-evidence` (case ops; clean-room) |
| **Sources** | `gh issue`/`pr`, `git log`, CHANGELOG, code paths in local clones under `OS/` |
| **Related pack** | `OS/_bench/brain-6way/` (executive-report, scorecard, inventories) |
| **Prior pass** | `graph-pitfalls-and-lessons.md` (first mine + reusable PROMPT) |
| **Language** | pt-BR |
| **Confidence** | **HIGH** gbrain, mempalace, mem0, gsd-2 · **HIGH** LifeOS (issues+code; public issue surface thinner on graph) · **MEDIUM-HIGH** memori (attribution/KG code + issues; fewer pure-graph bugs) |

> **Bottom line.** Os seis projetos pagaram caro por **silêncio no write/extract**, **tipo de aresta sem evidência**, **dual-SoT**, **temporal frágil**, **isolamento furado** e **métricas mentirosas** — não por “não ter grafo”. O VISA-BRAIN já codifica a doutrina certa (`evidence-graph.md`: grafo ≠ oráculo; fixed point + unlinked candidates; Boundary Card; `SAME_ORIGIN_GROUP`; fail-closed estrutural no P3). O valor deste pack é **fechar a lacuna entre doutrina e enforcement mecânico**: receipts de extract, reconcile set, lifecycle uniforme em toda leitura, supersession temporal, health honest, e testes T1–T22. **Não** integrar Neo4j/gbrain/mempalace como sidecar sobre dados de caso.

### Executive blurb — top traps × subjects

| Trap family | gbrain | mempalace | LifeOS | mem0 | memori | gsd-2 |
|-------------|:------:|:---------:|:------:|:----:|:------:|:-----:|
| Silent extract/write/drop | ●●● | ● | ●● | ● | ● | ●● |
| Over-typing without evidence | ●●● | · | · | · | · | · |
| Divergent entrypoints | ●●● | ● | ● | · | · | ● |
| Soft-delete / lifecycle holes | ●● | ● | · | ● | · | ● |
| Lying health / UI | ●● | · | ●● | ● | · | ● |
| Isolation / scope / cache | ●● | ●● | ● | ●●● | ●● | · |
| Temporal / supersession | ● | ●●● | · | ●● | · | ● |
| Dual-SoT / projection | ● | · | ● | · | · | ●●● |
| Shipped but unwired / missing deps | ● | · | ●●● | ● DOC-STALE | · | ●● |
| Entity merge pollution | ● | ● | · | ●●● | · | · |
| Synthesis ≠ store | ●●● | · | ● | ● | · | · |
| Races / concurrent RMW | ● (learned lock) | ● | ● | ●● | · | · |
| Hybrid drops secondary lists | ● | · | · | ●● | · | ● (FTS) |

● = evidence present · more dots = higher severity/frequency in this mine

---

## Clones e tips de referência

| Subject | Path | Tip SHA (short) | Remote |
|---------|------|-----------------|--------|
| gbrain | `OS/gbrain` | `15b9863d1` (2026-08-05) | https://github.com/garrytan/gbrain |
| mempalace | `OS/mempalace` | `8ab251c` (2026-07-17) | https://github.com/milla-jovovich/mempalace *(local remote; upstream MemPalace)* |
| LifeOS | `OS/lifeos` | `27c94f9` (2026-08-05) | https://github.com/danielmiessler/LifeOS |
| mem0 | `OS/mem0` | `4a0a9a92` (2026-08-06) | https://github.com/mem0ai/mem0 |
| memori-labs | `OS/memori-labs` | `538b61f` (2026-07-28) | https://github.com/MemoriLabs/Memori |
| gsd-2 | `OS/gsd-2` | `33c00aaff` (2026-05-22) | https://github.com/gsd-build/gsd-2 |

### Product job (não confundir com feature class)

| Subject | Job-to-be-done | Papel do grafo |
|---------|----------------|----------------|
| **gbrain** | Knowledge brain: search → **answer** (think + gaps) | Typed edges on write; multi-hop; graph **signals** re-rank top-K |
| **mempalace** | Verbatim local memory | Temporal entity-relationship KG (`valid_from`/`valid_to`, as-of) |
| **LifeOS** | Life OS / DA / TELOS | Declared MD edges (wikilink/related/tag); Louvain/PageRank analytics |
| **mem0** | Memory SDK multi-app | **DOC-STALE:** external graph store **removed from OSS v3**; entity linking remains |
| **memori** | Memory of what agents **do** | S-P-O tables + attribution(entity, process) |
| **gsd-2** | Coding-agent tribal memory | `memory_relations` enum + graph CLI (often dual-SoT with MD) |

---

## Como ler isto

| Símbolo | Família |
|--------|---------|
| ☠️ | Falha **silenciosa** (parece sucesso; dados errados ou vazios) |
| 🔒 | Isolamento / multi-tenant / cache key |
| ⏱ | Temporal / supersession |
| 🔁 | Dual-write / dual-SoT / projeção |
| 📊 | Métrica ou UI **mentirosa** |
| 🧭 | API documentada ≠ comportamento real |
| ✅ | VISA-BRAIN **já tem** doutrina ou mecanismo parcial |
| ⚠ | VISA-BRAIN **lacuna de enforcement** ou risco residual |

Cada seção: **armadilha → evidência → aprendizado → ação VISA**.

---

## Phase 0 — Scope freeze

### Feature class (uma frase)

Superfícies de **grafo de conhecimento e projeção**: extração e reconciliação de arestas tipadas, travessia, validade temporal, sinais de ranking baseados em grafo, identidade de entidade, e projeções regeneráveis — **não** a UI de voz, TELOS, ou marketing de install.

### In-scope

- Edge extract / auto-link / mention edges / reconcile vs additive-only  
- Traversal (depth, direction, both-ways)  
- Temporal triples (as-of, supersede, inverted intervals)  
- Graph signals / hybrid fusion interaction  
- Soft-delete / lifecycle on graph reads  
- Multi-source / multi-tenant / attribution scoping  
- Dual-SoT (MD ↔ SQL ↔ graph.json)  
- Health/doctor metrics about link coverage  
- Entity merge / alias / type  
- Synthesis paths that **should** consume the graph (`think`, retrieval inject)

### Out-of-scope (salvo bloqueio)

- Voice / Pulse / Siri  
- Multi-vector-store zoo marketing  
- Coding-agent orchestration (exceto quando memory graph dual-SoT)  
- Case facts privados VISA-LENDARIO

### Consumer non-goals

- Não rodar peer runtimes sobre dados de caso  
- Não Neo4j/sidecar obrigatório  
- Não copiar schema `links` / `triples` / API `think`  
- Abstrair **invariantes + testes** para `evidence-graph.json`, hot-index, traversals, Claims-Matrix

---

## 1. ☠️ Silent extract / silent write / silent drop

### Armadilha

Pipelines reportam sucesso com **0 edges**, **0 takes**, páginas vazias, ou “target doesn't exist” falso — operador e agent seguem.

### Evidência

| Source | Detail |
|--------|--------|
| gbrain **#3038** (closed) | DIR_PATTERN whitelist → 4 370 pages, **21 edges**, 99.7% orphan, **no error** |
| gbrain **#3799** (closed) | `extract --stale` drops all wikilinks as missing targets when both resolve |
| gbrain **#1184** (open) | dream extract phase **0 links**; manual extract works |
| gbrain **#2849** (open) | webhook sync defaults `noExtract` → permanent stale edges |
| gbrain **#2822** (open) | empty stdin `put` → empty page, invisible to embed --stale |
| gbrain **#2556** (open) | `think --take` → Takes:0, silent |
| gbrain **#3737** (open) | `extract --stale` abort **exit 0** |
| gbrain **#2821** (open) | fence-reconcile inserts **NULL-embedding** facts when gateway down |
| gsd **#4967** | `capture_thought` swallows SQL → generic `create_failed`; auto-mode continues |
| gsd **#3372** | memory extract `null` without model — 0 memories, no user feedback |
| LifeOS **#1409** | hot-layer write “ok”, read **0** (missing BEGIN markers) |
| memori **#362** | empty recall query crashes / leaks schema |

### Aprendizado

**Silêncio > crash** na severidade forense. “Done: 0” sem denominador de candidatos é bug P0.

### Ação VISA

| | |
|--|--|
| ✅ | P3 fail-closed sem matrix/traversal (`run-contract.md`) |
| ⚠ | Falta gate universal: `candidates_reviewed > 0 && edges_or_roles_emitted == 0` → **fail batch** com contagens |
| ⚠ | Todo path de ingest/review deve emitir **receipt** de extract (não só status unit) |
| Invariante | `complete ⇒ receipt com denominadores; never exit-0 on structural zero when candidates existed` |

---

## 2. Over-typing / semântica sem evidência

### Armadilha

Heurística de path/dir atribui predicado forte (`works_at`) sem texto.

### Evidência

| Source | Detail |
|--------|--------|
| gbrain **#3466** (closed) | people→companies → always `works_at` → **19 497** false employment claims on art brain |
| commit `dba0ae7b1` | fix: stop asserting works_at from bare adjacency |
| gbrain `link-extraction.ts` | `inferLinkType` regex + role priors; #3466 watermark re-extract |

### Aprendizado

Tipo de aresta **é claim**. Sem locator/trecho = alucinação em massa.

### Ação VISA

| | |
|--|--|
| ✅ | Ontology tipada + “Record the semantic basis of every edge” (`evidence-graph.md`) |
| ✅ | Fixture semantic-boundary-card |
| ⚠ | Validar mecanicamente: arestas `ROLE_AT` / `SUPPORTS` / `AUTHORED_BY` exigem `basis` + `unit_id` + locator quando `deep_reviewed` |
| ⚠ | Path/domain co-occurrence → no máximo `RELATED_TO` / candidate, **nunca** ROLE_AT automático |
| Invariante | `typed_evidentiary_or_role_edge ⇒ textual_or_canonical_basis` |

---

## 3. Entrypoints divergentes (fs / db / stale / webhook / dream)

### Armadilha

N “extracts” com resolvers diferentes → grafo depende do comando.

### Evidência

| Source | Detail |
|--------|--------|
| gbrain **#3607** (closed) | fs-mode 0 edges; db-mode **1533** same corpus |
| gbrain **#2576** | `--stale` used nullResolver for basename |
| gbrain **#1964** | slugify mismatch filename vs stored slug |
| gbrain **#1184**, **#2849** | dream / webhook skip materialize |
| LifeOS **#1573** | `getRelevantContext` on Telegram only, not primary CLI |
| gsd **#5148** | `gsd graph` CLI wired; slash `/gsd graph` not |

### Aprendizado

Feature “existe” no código ≠ path principal a usa.

### Ação VISA

| | |
|--|--|
| ✅ | Single skill path P2→P3 com preflight obrigatório |
| ⚠ | Um **reconciler** de grafo; mailbox/computer/web review lotes chamam o mesmo apply-batch |
| ⚠ | Teste de paridade: dois entrypoints no mesmo fixture corpus → **hash de edges igual** |
| Invariante | `all material write paths share one edge-reconcile function` |

---

## 4. Soft-delete / lifecycle incompleto na superfície do grafo

### Armadilha

Search/list filtram mortos; **traversal/backlinks** ainda os veem.

### Evidência

| Source | Detail |
|--------|--------|
| gbrain **#1702**, **#3754** (open) | get_links/backlinks/graph-query missing `deleted_at` filter on joins |
| gbrain #1305 fix commit | health counts exclude soft-deleted — **partial** surface only |
| **CODE-CONFIRM** | `postgres-engine`/`pglite-engine` filter `deleted_at` on page get/list; issues still open for link joins at tip `15b9863d1` |
| mem0 soft-delete relations history | prior graph path used soft-delete vs hard DELETE (pre-removal) |
| gsd **#6484** | delete misses FK cascades → orphan sibling rows |

### Aprendizado

Lifecycle é **por superfície de leitura**. Esquecer uma JOIN = fantasma no counsel.

### Ação VISA

| | |
|--|--|
| ✅ | `record_lifecycle` on Claims-Matrix |
| ⚠ | Toda leitura de evidence-graph / hot-index / export_claim_graph filtra `excluded`/`superseded`/`deleted` com **mesmo predicado** |
| ⚠ | Teste: unit tombstoned → absent from traversal + matrix roles |
| Invariante | `graph_read_predicate ≡ catalog_active_predicate` |

---

## 5. 📊 Health / metrics / UI mentirosos

### Armadilha

Score “verde” com store vazio ou densidades contraditórias.

### Evidência

| Source | Detail |
|--------|--------|
| gbrain **#3591** (closed) | 13 908 links in store; `link_coverage: 0`; density score full marks **same payload** |
| LifeOS **#1172** | populated knowledge feels empty (0 edges UX) |
| LifeOS **#1605** | MemoryGraph **cannot run as shipped** — graphology missing; package.json only `yaml` (**CODE-CONFIRM** tip `27c94f9`) |
| gsd **#6414** | consolidation scanner before DB open → false “all unmigrated” |
| mem0 **#6705** | docs print vector score as reranker score |
| gbrain **#3630** | docs/code drift rollup (doctor claims checks code lacks) |

### Aprendizado

Métrica de grafo deve ser **a mesma query** do produto. Install fresco deve smoke-testar a feature.

### Ação VISA

| | |
|--|--|
| ✅ | `recompute-kpis.mjs` — never hand-type Open conflicts / Single-source |
| ⚠ | Doctor/validate: se `edge_count` store ≠ coverage projection → **fail**, não score composto |
| ⚠ | Smoke pós-install skill: load evidence-graph schema + one fixture traversal |
| Invariante | `health_metric M derives from same store S as runtime path P` |

---

## 6. 🔒 Isolamento / scope / cache / singleton

### Armadilha

Cross-tenant edges, merge cross-scope, cache path string, KG singleton.

### Evidência

| Source | Detail |
|--------|--------|
| gbrain **#2589** (open) | cross-source wikilink resolved then edge **silently dropped** |
| gbrain **#1747** | extract 0 on non-default source |
| gbrain security commits | scope-escalation / write fence (tip message #3809) |
| mem0 **#5439**, **#5597** | entity merge across user_id/agent_id at ≥0.95 similarity |
| mem0 **#5587**, **#6529** | same name different **types** merge (TS lag) |
| memori **#404** | manual MCP attribution headers → project mix |
| memori **#578** / `0d40a64` | reject empty attribution strings |
| mempalace CHANGELOG **#1372/#1383** | KG cache key raw path → duplicate graphs macOS case/symlink |
| mempalace **#1136** | module-level `_kg` singleton → wrong sqlite when path rotates |

### Aprendizado

Isolamento = write + read + **cache key** + **no process singleton** + identity rules (not embedding alone).

### Ação VISA

| | |
|--|--|
| ✅ | Workspace private; product never holds case data; PRODUCT.yml pin |
| ✅ | `SAME_ORIGIN_GROUP` for independence (not file count) |
| ⚠ | Entity merge **never** by embedding threshold alone; type+alias+workspace |
| ⚠ | Projection DB/file keys: case root canonical path only |
| ⚠ | Zero global KG handle across cases |
| Invariante | `edge.workspace_id = unit.workspace_id` enforced; empty attribution reject |

---

## 7. ⏱ Temporal / supersession / ADD-only

### Armadilha

Intervalos invertidos invisíveis; date-only dual-truth; append-only state.

### Evidência

| Source | Detail |
|--------|--------|
| mempalace **#1214** | `valid_to < valid_from` stored, **invisible** to every as_of |
| mempalace CHANGELOG **#1913** | atomic `supersede()`; half-open `[from,to)` |
| commit `9815f0a` | half-open as-of for KG supersession |
| mempalace **#1164/#1167** | NL dates → empty set ≡ “no fact” |
| mem0 **#4956** | v3 ADD-only → contradictory employer facts coexist |
| gsd `memory-relations.ts` | `supersedes` relation + `superseded_by` hop |
| gbrain facts `valid_from`/`valid_until` | present; population sparse (proposal docs) |

### Aprendizado

Temporal correctness is a **write primitive**, not a query filter alone.

### Ação VISA

| | |
|--|--|
| ⚠ | Claims / roles / metrics with validity: half-open intervals; reject inverted |
| ⚠ | Single `supersede` op for mutable state (title, employer-equivalent, counts) |
| ⚠ | Parse dates strict on graph/claim time fields; error class ≠ empty |
| ⚠ | Sustained acclaim / chronology backlog: do not fake with ADD-only extracts |
| Invariante | `as_of(T) returns ≤1 open value per (subject, predicate) single-valued facts` |

---

## 8. 🔁 Dual-write / dual-SoT / projection without cutover

### Armadilha

Graph reads MD; truth lives in SQL (or reverse); projections empty.

### Evidência

| Source | Detail |
|--------|--------|
| gsd **#5149** | graph from markdown only; SQLite memories are SoT (ADR-013) |
| gsd **#5755** | cutover: stop dual-write; MD pure projection |
| gsd **#6342** | capture without structuredFields → empty KNOWLEDGE tables, rich DB |
| gsd **#4512** | decommission legacy writers / double-injection |
| LifeOS MemorySystem.md | files as SoT; graph rebuild from MD — good **if** single SoT |
| gbrain | links table is operational store; markdown source of extract — reconcile model |

### Aprendizado

Cutover explícito: **uma** write authority; resto rebuildable.

### Ação VISA

| | |
|--|--|
| ✅ | Registers first; dashboard `data.js` projection; no hand KPIs |
| ✅ | hot-index / evidence-graph as projections not authority (`lifeos-native` research alignment) |
| ⚠ | Never promote investigation graph candidates to Claims-Matrix without workflow |
| ⚠ | Rebuild graph from extracts+ledger only; delete projection → zero proof loss |
| Invariante | `canonical_write_set ∩ projection_write_set = ∅` |

---

## 9. Feature shipped without deps / without primary-path wire

### Armadilha

README/CLI claim feature; install or main path dead.

### Evidência

| Source | Detail |
|--------|--------|
| LifeOS **#1605** + **CODE-CONFIRM** `install/package.json` only `yaml` | graphology imports fail stock install |
| LifeOS **#1255** | MemoryRetriever top-level only — subdirs invisible |
| LifeOS **#1573** | retrieval not on main CLI turn path |
| gsd **#5148** | slash graph unwired |
| gbrain **#2089** (open) | takes.embedding **no writer** — vector takes search structurally dead |
| gbrain **#2365** | think free-form skips subgraph without `--anchor`; query auto-walks |
| mem0 **#6591** DOC-STALE | AGENTS.md documents graph removed in #4805 |
| **CODE-CONFIRM** | `mem0/mem0/graphs` **absent**; enable_graph stripped v3 |

### Aprendizado

Primary path + install smoke define reality.

### Ação VISA

| | |
|--|--|
| ✅ | Codex skill loads evidence-graph before material conclusion |
| ⚠ | Audit mid-run chat paths: any conclusion outside P3 must still open hot-index neighborhood (doctrine already says so — enforce) |
| ⚠ | CI: fixture investigation without graph artifact fails closed |
| Invariante | `documented_feature F ⇒ smoke(F) on fresh install + main operator path` |

---

## 10. Entity merge / identity pollution

### Armadilha

String/embedding sameness collapses distinct entities; stopwords become people.

### Evidência

| Source | Detail |
|--------|--------|
| mem0 **#5438** | 0.95 similarity sole merge criterion |
| mem0 **#5587** | person Apple vs company Apple |
| mempalace CHANGELOG **#1605** | “system/user/memory” as people |
| mempalace **#1557** | case-insensitive init vs case-sensitive mine |
| mempalace **#2063** | ReDoS on entity candidate regex |
| gbrain #3466 class | false role edges create false identity graph |

### Aprendizado

Identity is **typed + scoped + alias-registry**, not cosine.

### Ação VISA

| | |
|--|--|
| ✅ | “Do not merge entities merely because labels are similar” (`evidence-graph.md`) |
| ✅ | Keep ambiguous identities separate in preflight |
| ⚠ | Mechanical: merge proposal requires human/counsel gate or dual independent sources |
| ⚠ | Denylist tokens for auto entity promotion from OCR/email |
| Invariante | `auto_merge forbidden; candidate_alias only` |

---

## 11. Synthesis / retrieval not consuming the feature store

### Armadilha

Graph exists; answer path ignores it or hydrates 0 pages.

### Evidência

| Source | Detail |
|--------|--------|
| gbrain **#2903** (open) | query rank #1; think **Pages:0**, Graph:1 — “no information” |
| gbrain **#2365** | think no auto-anchor |
| gbrain `think/index.ts` **CODE-CONFIRM** | `--rounds` loop `break` + `ROUNDS_GT_1_NOT_GAP_DRIVEN_IN_V028` — gap array not driving retrieval |
| gbrain `gather.ts` | graph stream = **slug set** only, not typed edge bundle for synthesis |
| gbrain `graph-signals.ts` **CODE-CONFIRM** | top-K only, fail-open, ×1.05/×1.10/×0.95; not proof |
| LifeOS **#1573** | retriever unused on primary path |
| mem0 **#5742** | hybrid scores BM25/entity but ranks only semantic top-k pool |

### Aprendizado

**CODE-CONFIRMED vs marketing:** gbrain README sells synthesis+gaps+graph; rounds gap-fill **not implemented**; graph signals ≠ corroboration; think can miss the page that query finds.

### Ação VISA

| | |
|--|--|
| ✅ | Decision Preflight: reopen extracts of neighborhood |
| ✅ | Edge alone proves nothing |
| ⚠ | Gate: material conclusion requires traversal receipt **and** reopened unit set non-empty for SUPPORTS roles |
| ⚠ | Never treat multi-source graph boost as independence |
| ⚠ | Do not ship “gap-driven multi-round” until tests show new retrieval from residual gaps |
| Invariante | `conclusion ⇒ reopened_units ⊇ role_supporting_units` |

---

## 12. Concurrency / RMW races

### Evidência

| Source | Detail |
|--------|--------|
| mem0 **#6243** | entity store RMW without lock → lost linked_memory_ids |
| gbrain `operations.ts` | advisory lock `auto_link:${slug}` — **learned** concurrent put_page race |
| mempalace #784 | file lock concurrent mine |
| LifeOS **#1711** | global review-state.json multi-session corruption |
| gbrain **#2840** (open) | page-lock PID namespace steal in containers |

### Ação VISA

| | |
|--|--|
| ⚠ | apply-batch / graph reconcile under lease per unit/run |
| ⚠ | Run state keyed by run_id, not machine-global |
| Invariante | `concurrent_reconcile(unit) serializes; no silent last-write-wins on edges` |

---

## 13. Hybrid retrieval discarding non-primary lists

### Evidência

| Source | Detail |
|--------|--------|
| mem0 **#5742** (open, P1) | keyword/entity outside semantic top-k never ranked |
| gsd **#4497** | FTS5 missing → silent LIKE degrade |
| gbrain hybrid + graph signals | signals only reorder existing top-K (**CODE-CONFIRM**) |

### Ação VISA

| | |
|--|--|
| ⚠ | Candidate union: FTS ∪ path ∪ alias ∪ gap ∪ entity before fusion |
| ⚠ | Degraded search → `receipt.degraded=true`; block conclusions that needed that surface |
| Invariante | `fusion_input = union(lists); never rank-only-primary-pool` |

---

## 14. Doc/API surface removed or stale

### Evidência

| Source | Detail |
|--------|--------|
| mem0 v3 commits | graph store removal; tests deleted |
| mem0 **#6442**, **#6591** | users/docs still expect Neo4j graph |
| gbrain **#3630** | doctor/CLI doc drift |

### Ação VISA

| | |
|--|--|
| ⚠ | AGENTS.md / skill version: remove claims without mechanism |
| Invariante | `policy enforcement-or-aspiration` — no fake gates |

---

## VISA-BRAIN — gap map (doctrine vs peer burns)

| VISA doctrine (already) | Peer burn if under-enforced | Priority |
|-------------------------|----------------------------|----------|
| Graph ≠ truth oracle | gbrain signals / health treated as proof | P0 keep |
| Fixed point + unlinked candidate searches | peers use hop 2–5 only — **VISA leads** | P0 keep |
| Boundary Card + semantic fixture | gbrain gaps array without re-retrieve | P0 keep |
| `SAME_ORIGIN_GROUP` / independent groups | mem0 cross-source boost confusion | P0 keep |
| single_source from groups not file count | — | P0 keep |
| Registers → projection dashboard | gsd dual-SoT | P0 keep |
| Extract-before-reviewed | LifeOS/gsd silent empty writes | P0 keep |
| **Missing: candidate>0 ∧ edge=0 fail** | #3038 class | **P0 add** |
| **Missing: typed edge basis locator gate** | #3466 class | **P0 add** |
| **Missing: single reconcile all entrypoints** | #3607/#2849 | **P1 add** |
| **Missing: uniform lifecycle on all graph reads** | #1702/#3754 | **P1 add** |
| **Missing: temporal supersede primitive on mutable CLM** | mempalace #1913 / mem0 #4956 | **P1 add** |
| **Missing: degraded retrieval flag** | #4497/#5742 | **P1 add** |
| **Missing: health vs store equality check** | #3591 | **P2 add** |

---

## Catálogo → testes de regressão (T1…T22)

| # | Armadilha | Teste mecânico (pass/fail) |
|---|-----------|----------------------------|
| T1 | Silent zero extract | Fixture with ≥3 wikilink/mention candidates; if 0 edges/roles → **FAIL** |
| T2 | Over-type without text | Artist unit + museum org; auto ROLE_AT/employment **must not** emit |
| T3 | Entrypoint parity | Same corpus via path A and B → edge-set hash equal |
| T4 | Soft-delete leak | Tombstone unit → absent traversal + export |
| T5 | Lying health | Mutate store edge_count; health coverage must match ±0 |
| T6 | Cross-workspace edge | Insert edge with foreign case id → schema/validator **reject** |
| T7 | Empty attribution/scope | Empty workspace key → reject |
| T8 | Inverted temporal | valid_to < valid_from → reject write |
| T9 | Supersede boundary | as_of(boundary) → exactly one successor value |
| T10 | Dual SoT | Delete projection rebuild from ledger; proof unchanged |
| T11 | Embedding merge | Similar names different types remain distinct without human gate |
| T12 | Silent write fail | Force store error → no “complete”; error class logged |
| T13 | Concurrent reconcile | Two writers same unit → no lost edges (final set = union reconciled) |
| T14 | Degraded search | Disable FTS → receipt.degraded; material conclusion blocked if depended |
| T15 | Synthesis without reopen | SUPPORTS edge without reopened extract → P3 **FAIL** |
| T16 | Stale additive edges | Re-extract after basis removal → old edge gone |
| T17 | Future watermark | Extractor version stamp ≤ now |
| T18 | Fresh install smoke | Validator + one fixture graph loads |
| T19 | Gap loop honesty | If multi-round claimed, residual gap must change retrieval set or flag unimplemented |
| T20 | single_source independence | Two files same origin group → single_source true |
| T21 | Caveat non-erasure | Fixture semantic-boundary-card must continue to pass |
| T22 | Graph boost ≠ independence | Multi source_id link count must not set corroboration alone |

---

## Top 12 lições (severidade para VISA-BRAIN)

1. **Silêncio é P0** — 0 edges/0 writes/exit 0 com candidatos (#3038, #3799, #1184, #4967).  
2. **Tipo sem base textual é alucinação em massa** (#3466).  
3. **Um reconciler, todos os entrypoints** (#3607, #2849, #1573).  
4. **Lifecycle em toda JOIN de grafo** (#1702, #3754) — fantasma no counsel.  
5. **Temporal half-open + supersede atômico** (mempalace #1913) para estado mutável.  
6. **Uma autoridade de escrita; grafo é projeção** (gsd ADR-013 / #5755).  
7. **Isolamento não é header MCP** (memori #404; mem0 #5439; mempalace cache #1372).  
8. **Identity ≠ cosine 0.95** (mem0 #5438/#5587).  
9. **Health = mesma query do runtime** (#3591; LifeOS #1605).  
10. **Graph signals / hybrid boosts reordenam — não corroboram** (graph-signals.ts; #5742).  
11. **Síntese deve reabrir unidades** (#2903; VISA preflight) — edge slug list ≠ prova.  
12. **Não prometa gap-driven multi-round sem implementação** (think rounds CODE-CONFIRM).

---

## O que não reimplementar

| Evitar | Evidência |
|--------|-----------|
| Neo4j/Memgraph/Kuzu optional + LLM Cypher | mem0 removed from OSS; #6442/#6591 DOC-STALE |
| DIR_PATTERN personal-wiki whitelist | gbrain #3038 |
| `works_at` / ROLE from directory adjacency | #3466 |
| Dual-write MD+SQL without cutover | gsd #5149/#5755 |
| Entity auto-merge similarity threshold | mem0 #5438 |
| KG process singleton + raw path cache | mempalace #1136/#1372 |
| Hand-rolled invalidate+add date-only | mempalace supersede rationale |
| Composite brain_score masking zero coverage | #3591 |
| Webhook/async skip extract by default | #2849 |
| Manual per-session attribution only | memori #404 |
| Fail-open graph signals as counsel gate | graph-signals.ts |
| Sidecar peer brain on case data | monorepo safety + clean-room |

---

## Índice de issues/commits citados (por subject)

### gbrain
#3038, #3466, #2576, #3607, #3799, #1184, #2849, #1964, #2367, #1846, #3674, #1702, #3754, #3591, #2931, #2589, #1747, #2903, #2365, #2556, #2822, #2821, #3737, #2089, #3630, #2840, #3190, #3188 · commits `dba0ae7b1`, tip `15b9863d1` · files `graph-signals.ts`, `think/index.ts`, `gather.ts`, `link-extraction.ts`, `operations.ts`

### mempalace
#1214, #1913, #1164, #1167, #1372, #1383, #1136, #1605, #1557, #2063, #784 · commits `9815f0a`, `8ab251c` · file `knowledge_graph.py` supersede/half-open

### LifeOS
#1605, #1172, #1255, #1573, #1409, #1761, #1711 · tip `27c94f9` · `install/package.json` yaml-only · `MemoryGraph.ts` / `KnowledgeGraph.ts`

### mem0
#5438, #5439, #5587, #5597, #6243, #5742, #4956, #6442, #6591, #6529, #6705 · commits graph removal / tip `4a0a9a92` · **no** `mem0/graphs` at tip

### memori-labs
#404, #578, #362, #98, #434, #590 · commits `0d40a64`, `e10b57e`, `538b61f` · `augmentation/pipeline.rs` knowledge_graph.create · `attribution()`

### gsd-2
#5149, #5755, #6342, #6414, #5148, #4497, #4967, #3372, #4471, #4512, #6484 · tip `33c00aaff` · `memory-relations.ts`

---

## Ligação com práticas confirmadas no código

| Practice | Confirmed in peers? | Related family | VISA stance |
|----------|--------------------:|----------------|-------------|
| Write-path cheap typed edges | **Yes** gbrain auto-link | 1–3 | Adopt invariant; not API |
| Graph reorders top-K only | **Yes** graph-signals | 11, 13 | Rank only; never gate truth |
| Temporal supersede + half-open | **Yes** mempalace | 7 | Adopt for mutable CLM fields |
| Declared edges first | **Yes** LifeOS | 2, 9 | Candidates vs accepted edges |
| Attribution required | **Yes** memori | 6 | Workspace binding |
| Dual-SoT cutover | **Yes as anti-pattern** gsd | 8 | Already product doctrine |
| External graph DB | **Removed** mem0 OSS | 14 | Do not reintroduce |
| Fixed point + unlinked search | **No peer leader** | — | **VISA advantage — keep** |
| Gap-driven multi-round synthesis | **Not implemented** gbrain | 11 | Don't claim until built |

---

## Relação com packs/benches irmãos

| Artefato | Papel |
|----------|--------|
| `executive-report.md` / `scorecard.md` | Ranking **memory pack** — não substitui este relatório de falhas |
| `comparison-matrix.md` | Jobs de produto |
| `_inventories/*` | Snapshot de capabilities |
| `graph-pitfalls-and-lessons.md` | Primeira mina + **PROMPT reutilizável** |
| **este arquivo** | Deep dive clean-room → **VISA-BRAIN backlog/tests** |
| `docs/research/2026-08-06-gbrain-cerebras-evidence-runtime/` | Runtime evidence packet / synthesize PROP-X |
| `docs/research/2026-08-06-memory-5way-native-lessons/` | Packet + literal locator gates |
| `VISA-BRAIN/.../evidence-graph.md` | Consumer doctrine SoT |

Sidecar: `visa-brain-graph-feature-lessons.citations.json`

---

## Nota de método

1. Phase 0–1: tips via `git rev-parse` / remotes; feature surfaces via prior inventories + `rg`.  
2. Phase 2: `gh issue list --search` per subject; CHANGELOG (mempalace heavy); `git log --grep`.  
3. Phase 3: code-confirm — think rounds break; graph-signals fail-open; LifeOS package.json; mem0 graphs absent; mempalace supersede; soft-delete issues still OPEN at gbrain tip.  
4. Phase 4–5: families merged; mapped to VISA skill refs without case data.  
5. Clean-room: invariants + T-tests only; no adapters; no peer execution on case trees.  
6. **Staleness:** re-run if tips move; open issues may close; re-verify #1702/#3754/#2589 before claiming fixed.  
7. mempalace local remote may be fork (`milla-jovovich`); issue numbers still from GitHub search against clone auth context — treat IDs as search-linked, re-open URL if fork diverges.

---

## Closing

> Os peers ensinam com sangue o que o scorecard de memória esconde. O VISA-BRAIN já tem doutrina superior. O trabalho mecânico **não** é implementar T1–T22 à letra — ver adendo de revisão Codex abaixo.

---

## Adendo — revisão Codex (2026-08-06): onde T1–T22 errou e o que fazer

**Parecer:** análise de peers forte como mapa de falhas; **não** como implementação literal. Misturava lacunas reais, proteções já existentes e capacidades futuras.

### Por que o relatório original errou

| Classe | Erro | Por quê |
|--------|------|---------|
| **A. Peer → gate cego** | T1: `candidates > 0 ⇒ edges > 0` | Zero arestas *aceitas* pode ser correto; forçar edge recria #3466. Candidatos precisam de **disposição** (accepted/rejected/ambiguous/irrelevant). |
| **B. Gap peer = “VISA não tem”** | T2/T15 como falta total de basis/reopen | P3 **já** exige `semantic_basis`, `visited_unit_ids`, `reviewed_by_llm` (`investigation_run.py` ~405–530). Falta **profundidade** (locator/digest/bytes reabertos). |
| **C. Doutrina ignorada** | T6/T7/T20/T21 como arch nova | Isolation, single_source, Boundary Card fixture **já** enforced — só hardening. |
| **D. Metáfora de store** | T5 edge_count store vs projection | VISA não tem graph DB; métrica = **fingerprint dos inputs** da projection. |
| **E. Backlog deliberado** | T8/T9 temporal P1 imediato | **B-028** adiado em `BACKLOG.md`; invariante mempalace não autoriza pular fila. |
| **F. Futuro como presente** | T3 parity, T14 degraded | Valor quando multi-adapter/FTS real (B-020/B-036+). |
| **G. Guarda vendida como feature** | T19 multi-round, T22 graph boost | Produto **não** tem; correto é não prometer, não portar gbrain signals. |

### Disposição T1–T22

| ID | Disposição | Nota |
|----|------------|------|
| **T1** | **REESCREVER** | disposition por candidato; zero accepted OK |
| **T2** | **DEEPEN P3** | basis já existe; + locator/digest |
| **T3** | **FUTURO** | B-020/B-036 multi-path |
| **T4** | **IMPLEMENTAR** | lifecycle module; export_claim_graph sem filter |
| **T5** | **TRADUZIR** | fingerprint inputs, não count graph store |
| **T6–T7, T20–T21** | **JÁ TEM** | não greenfield |
| **T8–T9** | **B-028 later** | ratificação explícita |
| **T10, T16–T18** | **PROJECTION FRESHNESS** | hot-index preserve por ID ignora conteúdo (L1253+) |
| **T11** | **JÁ TEM** (doutrina) | |
| **T12–T13** | **B-020/B-036** | apply_batch sequencial |
| **T14** | **FUTURO** | |
| **T15** | **DEEPEN P3** | visited sim; reopen-bytes não |
| **T19, T22** | **GUARDA** | não implementar engine |

### Ordem de implementação endossada

1. **Projection freshness** — fingerprint extracts/aliases, watermark, invalidate claims, P3 block se stale  
2. **Grounding forte P3** — strong edges: reviewed + locator + digest + reopened set ⊇ SUPPORTS  
3. **Lifecycle uniforme** — um módulo active/inactive para export, dashboard, audit, validator  
4. **Transactional reconcile** em B-020/B-036 (`apply_batch` atômico)  
5. **B-028 temporal** só depois  

**Não:** Neo4j, GraphRAG, embeddings, PageRank, graph signals, multi-round, sidecar peers.

### Backlog líquido recalibrado (substitui P0–P10 abaixo)

1. P0 Projection freshness  
2. P0 P3 grounding (locator + digest + reopened)  
3. P1 Lifecycle module compartilhado  
4. P1 Transactional apply_batch / ingest receipts (B-020/B-036)  
5. P1 Disposition de candidatos (T1 reescrito)  
6. Defer B-028 · multi-entrypoint · degraded retrieval  
7. Never peer graph runtime / GraphRAG  

### Código verificado nesta correção

- `semantic_basis` / traversal visit: `investigation_run.py` L458–522  
- hot-index preserve: L1253–1274  
- `apply_batch`: L290+  
- export sem lifecycle: `export_claim_graph.py` L43–52  
- dashboard com lifecycle: `build_dashboard_projection.py` L24, L728–729  
- B-028: `BACKLOG.md` L115–118  
- B-020/B-036 open: ADR-INGEST-RUNTIME L448–452  

---

## Backlog líquido sugerido (clean-room stories) — **SUPERSEDED**

> Lista original abaixo **não implementar à letra**. Usar **Backlog líquido recalibrado** no adendo.

1. ~~P0 Gate candidates⇒edges~~ → disposition  
2. ~~P0 basis+locator from zero~~ → deepen P3  
3. ~~P0 reopen from zero~~ → deepen P3  
4. ~~P1 multi-entrypoint agora~~ → futuro  
5. P1 Lifecycle module — **mantém**  
6. ~~P1 supersede temporal~~ → B-028  
7. ~~P1 degraded retrieval agora~~ → futuro  
8. ~~P2 health count store~~ → fingerprint  
9. P2 entity auto-merge — doutrina já  
10. Defer embeddings / Neo4j / multi-round — **mantém**