# Scorecard: superpowers vs paperclip

**Date:** 2026-08-12  
**Type:** pair  
**Pack:** harness-structure  
**Method:** installed (filesystem of `OS/superpowers/` and `OS/paperclip/`)  
**Confidence overall:** HIGH  
**Parent:** `harness-structure-8way`

## Weighted totals

| | superpowers | paperclip | Delta |
|---|---:|---:|---:|
| **Total** | **85.74** | 83.88 | **+1.86** |

Winner: **superpowers**. Dim wins 5–3. Complementary products — the number picks the process pole.

## Per dimension

| Dimension | W | SP | PC | Δ | Winner |
|---|---:|---:|---:|---:|---|
| Skill System | 0.16 | **92** | 78 | +14 | superpowers |
| Squad Model | 0.14 | 78 | **94** | −16 | paperclip |
| Plugin Extensibility | 0.12 | 82 | **86** | −4 | paperclip |
| Context Architecture | 0.16 | **86** | 76 | +10 | superpowers |
| Complex-Work Spine | 0.16 | **90** | 84 | +6 | superpowers |
| Gates & Discipline | 0.10 | **95** | 78 | +17 | superpowers |
| Handoff & State | 0.10 | **93** | 90 | +3 | superpowers |
| Governance | 0.06 | 55 | **92** | −37 | paperclip |

## Rankings

- **superpowers strongest:** Gates (+17), Skill System (+14), Context (+10)
- **paperclip strongest:** Governance (−37), Squad (−16), Plugin (−4)
- **Closest:** Handoff (+3), Plugin (−4)

## Analysis

**Gates** is the gap that decides the weighted race. Superpowers is the only side with TDD iron law + a reviewer that is not the implementer + a 5-round breaker (`OS/superpowers/skills/subagent-driven-development/SKILL.md`). Paperclip has `in_review` and a QA employee. That is governance of *work*, not discipline of *code*.

**Governance** is the opposite cliff. Paperclip has budgets, board hire/pause, plugin capabilities (`OS/paperclip/docs/companies/companies-spec.md`). Superpowers 55 is prompt text. Porting a board into Superpowers would break the zero-dep process plugin.

**Squad** is the same split: standing CEO/CTO/QA vs ephemeral implementer/reviewer.

**Handoff is a near-tie.** Both refused chat-as-SoT. Superpowers uses brief files because a 42k paste failed; Paperclip uses issue comments with a required field list.

## Limitations

The pack rewards “structure for complex *coding* work.” A pack named `company-ops` would flip the winner. Do not read 85.74 as “Superpowers replaces Paperclip.”
