# Comparison Matrix: case-ops-8way

**Date:** 2026-08-12 · **Pack:** case-ops · **Features:** 16  
**Method:** n-way `yes | partial | no | n/a`. Evidence per cell lives in `scorecard.json` signals.

## Subjects

| Subject | Path | Job |
|---|---|---|
| VISA-BRAIN | `VISA-BRAIN/` (external kit) | Case OS |
| gsd-pi | `OS/gsd-pi/` | Coding factory |
| gbrain | `OS/gbrain/` | Knowledge cortex |
| superpowers | `OS/superpowers/` | Process plugin |
| spec-kit | `OS/spec-kit/` | Spec SoT |
| paperclip | `OS/paperclip/` | Company control plane |
| mempalace | `OS/mempalace/` | Verbatim archive |
| LifeOS | `OS/LifeOS/` | Life OS |

## Matrix

| Feature | VISA | gsd-pi | gbrain | SP | spec-kit | paperclip | mempalace | LifeOS |
|---|---|---|---|---|---|---|---|---|
| Fact/claim/finding split | Y | N | P | N | P | N | P | P |
| Category errors blocked | Y | N | P | N | N | N | N | N |
| Generated dashboard/digest | Y | P | P | N | P | Y | N | P |
| Fingerprint rebuild-if-stale | Y | N | P | N | N | P | N | N |
| Product kit ≠ live data | Y | P | Y | P | P | P | N | P |
| One explicit root / no sibling scan | Y | P | P | P | N | P | N | N |
| Mechanical extract reject | Y | N | N | P | N | N | N | N |
| Disk restart / ledger | Y | Y | P | Y | P | Y | P | P |
| Graph ≠ oracle | Y | n/a | N | n/a | n/a | n/a | Y | P |
| Independence groups | Y | N | N | N | N | N | N | N |
| Independent counsel/review | Y | P | N | Y | P | P | N | N |
| Coverage ≠ eligibility | Y | P | N | P | P | P | N | N |
| USER/SOUL ≠ evidence | Y | N | P | N | N | P | P | P |
| Portal vs canonical vault | Y | N | N | N | N | Y | N | P |
| Phases + fail-closed gates | Y | Y | P | Y | Y | P | N | P |
| Honest completion speech | Y | P | P | P | P | P | N | N |

Y = yes · P = partial · N = no · n/a = not that product

## Uniques

| Subject | Only they have |
|---|---|
| VISA-BRAIN | Script extract-before-reviewed; Boundary Card + SAME_ORIGIN_GROUP |
| gbrain | Company-brain sources + OAuth (`docs/tutorials/company-brain.md`) |
| mempalace | Atomic temporal supersede (`knowledge_graph.py`) |

## Reading

The empty cells are not missing features — they are **other jobs**. The only portable uniques *into* VISA are mempalace temporal supersede (B-028) and, if the product becomes a firm, gbrain sources **outside** the vault.
