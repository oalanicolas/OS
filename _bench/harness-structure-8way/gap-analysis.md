# Gap Analysis (field-level): harness-structure-8way

**Date:** 2026-08-12  
**Mode:** n-way field (not N² pairs)  
**Confidence:** HIGH  
**Counts:** 24 gaps · P0=1 · P1=10 · P2=7 · P3=6

Every subject has gaps **and** uniques. That is the bidirectional property in n-way form.

## P0

| ID | Subject | Gap | Evidence |
|---|---|---|---|
| GAP-GSD-001 | gsd-pi | Living tree moved to open-gsd/gsd-pi | `OS/gsd-pi/README.md` |

Do not absorb from this clone without checking the successor.

## P1 (absorb these first)

| ID | Subject | Steal from | What |
|---|---|---|---|
| GAP-GS-001 | gstack | superpowers hook | Tiny bootstrap; kill preamble bloat |
| GAP-GS-002 | gstack | superpowers SDD | 5-round review breaker |
| GAP-GSD-002 | gsd-pi | superpowers | SessionStart-class force-invoke |
| GAP-BM-001 | BMAD | openclaw caps | Listing budget / install profiles |
| GAP-PC-001 | paperclip | superpowers | TDD + SDD ledger as requiredSkills |
| GAP-HE-002 | hermes | gstack | Factory spine office-hours→ship |
| GAP-HE-003 | hermes | superpowers | Bootstrap, not just an index |
| GAP-OC-001 | openclaw | spec-kit / gstack | SDLC spine + implementation gates |
| GAP-SK-001 | spec-kit | gsd-pi skills runtime | SKILL.md adapter so hosts discover it |
| GAP-SK-003 | spec-kit | superpowers ledger | Compaction-safe controller state |

## Per-subject gap rollup

| Subject | P0 | P1 | P2 | P3 | Pattern of the hole |
|---|---:|---:|---:|---:|---|
| superpowers | 0 | 0 | 1 | 2 | Platform (org/MCP) — out of scope on purpose |
| gstack | 0 | 2 | 0 | 1 | Context cost + no breaker |
| gsd-pi | 1 | 1 | 0 | 1 | Archive + weaker bootstrap |
| BMAD-METHOD | 0 | 1 | 1 | 1 | No budget, no own runtime |
| paperclip | 0 | 1 | 2 | 0 | No software-process discipline |
| hermes-agent | 0 | 2 | 1 | 0 | No factory, no org, hopeful invoke |
| openclaw | 0 | 1 | 2 | 0 | Employee OS, not an SDLC |
| spec-kit | 0 | 2 | 0 | 1 | Invisible to Agent Skills hosts |

## What not to “fix”

- Do not add an org-chart to Superpowers. It would break the zero-dep process plugin.
- Do not turn spec-kit into personas. The atom is the spec.
- Do not give OpenClaw a CEO. That is Paperclip’s product.
- Do not give Paperclip a TDD iron law *in core* — ship it as a requiredSkills pack.

Full records: `gap-analysis.json`.
