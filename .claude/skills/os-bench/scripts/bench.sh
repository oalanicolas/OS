#!/usr/bin/env bash
# os-bench CLI orchestrator — standalone, sem deps de npm/sinkra
# Uso: ./bench.sh <command> [args]

set -euo pipefail

# ============================================================
# Resolve paths
# ============================================================

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILL_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
OS_ROOT="$(cd "${SKILL_ROOT}/../../.." && pwd)"   # OS/
BENCH_ROOT="${OS_ROOT}/_bench"

mkdir -p "${BENCH_ROOT}"

# ============================================================
# Cores
# ============================================================

if [[ -t 1 ]]; then
  BOLD=$'\033[1m'; RED=$'\033[31m'; GREEN=$'\033[32m'
  YELLOW=$'\033[33m'; BLUE=$'\033[34m'; CYAN=$'\033[36m'; RESET=$'\033[0m'
else
  BOLD=''; RED=''; GREEN=''; YELLOW=''; BLUE=''; CYAN=''; RESET=''
fi

log()    { echo "${CYAN}[os-bench]${RESET} $*"; }
ok()     { echo "${GREEN}[ok]${RESET} $*"; }
warn()   { echo "${YELLOW}[warn]${RESET} $*"; }
err()    { echo "${RED}[error]${RESET} $*" >&2; }
title()  { echo "${BOLD}$*${RESET}"; }

# ============================================================
# Helpers
# ============================================================

die() { err "$*"; exit 1; }

ensure_subject() {
  local slug="$1"
  [[ -d "${OS_ROOT}/${slug}" ]] || die "subject '${slug}' não existe em OS/"
}

json_parseable() {
  local file="$1"
  [[ -f "$file" ]] || { echo "missing"; return 1; }
  if command -v node >/dev/null 2>&1; then
    node -e "JSON.parse(require('fs').readFileSync('${file}','utf8'))" 2>/dev/null \
      && echo "ok" || echo "invalid"
  elif command -v python3 >/dev/null 2>&1; then
    python3 -c "import json,sys; json.load(open('${file}'))" 2>/dev/null \
      && echo "ok" || echo "invalid"
  else
    echo "no-validator"
  fi
}

# ============================================================
# Commands
# ============================================================

cmd_help() {
  cat <<EOF
${BOLD}os-bench${RESET} — CLI orchestrator para benchmarks de OS/

${BOLD}Uso:${RESET} bench.sh <command> [args]

${BOLD}Comandos:${RESET}
  help                      Este menu
  list                      Lista benchmarks em OS/_bench/
  plan                      Mostra os 6 benchmarks canônicos planejados
  init <a> <b>              Cria pasta OS/_bench/{a}-vs-{b}/ + metadata stub
  init-nway <topic> <a> <b> ...
                            Cria pasta OS/_bench/{topic}-Nway/ + metadata stub
  validate <slug>           Roda quality gate em um benchmark
  index                     Regenera OS/_bench/INDEX.md
  clean <slug>              Remove um benchmark (confirmação)
  packs                     Lista dimension packs disponíveis
  subjects                  Lista subjects (diretórios) em OS/

${BOLD}Paths:${RESET}
  Skill:        ${SKILL_ROOT}
  OS root:      ${OS_ROOT}
  Bench root:   ${BENCH_ROOT}
EOF
}

cmd_list() {
  title "Benchmarks em ${BENCH_ROOT}:"
  local found=0
  for d in "${BENCH_ROOT}"/*/; do
    [[ -d "$d" ]] || continue
    local name
    name="$(basename "$d")"
    [[ "$name" == "_inventories" ]] && continue
    local metadata="${d}metadata.json"
    if [[ -f "$metadata" ]]; then
      local gen_at="?"
      # evita pipefail com set -e: usa awk e tolera 0 matches
      gen_at=$(awk -F'"' '/"generatedAt"/{print $4; exit}' "$metadata" 2>/dev/null || echo "?")
      [[ -z "$gen_at" ]] && gen_at="?"
      echo "  - ${name} (generated: ${gen_at})"
    else
      echo "  - ${name} (${YELLOW}no metadata.json${RESET})"
    fi
    found=1
  done
  [[ $found -eq 0 ]] && echo "  (nenhum ainda)"
  return 0
}

cmd_plan() {
  title "6 benchmarks canônicos (*run-all):"
  cat <<'EOF'
  1. coding-agents-8way     (pack: coding-agent)
     subjects: claude-code-main, codex, aider, OpenHands, gsd-2, gstack, superpowers, ai-website-cloner-template
  2. memory-4way            (pack: memory)
     subjects: gbrain, mempalace, mem0, gsd-2
  3. orchestration-5way     (pack: orchestration)
     subjects: BMAD-METHOD, crewAI, autogen, paperclip, claude-remote-manager
  4. spec-driven-3way       (pack: spec-driven)
     subjects: spec-kit, get-shit-done, superpowers
  5. personal-assistant-3way (pack: personal-assistant)
     subjects: openclaw, hermes-agent, gbrain
  6. workflow-infra-2way    (pack: workflow-infra) — pair
     subjects: workflow, gh-aw
EOF
}

cmd_packs() {
  title "Dimension packs disponíveis:"
  grep -E '^  [a-z-]+:$' "${SKILL_ROOT}/data/dimension-packs.yaml" 2>/dev/null | sed 's/:$//;s/^  /  - /'
}

cmd_subjects() {
  title "Subjects em ${OS_ROOT}:"
  for d in "${OS_ROOT}"/*/; do
    [[ -d "$d" ]] || continue
    local name="$(basename "$d")"
    [[ "$name" == ".claude" || "$name" == "_bench" ]] && continue
    echo "  - ${name}"
  done
}

cmd_init() {
  local a="${1:-}"; local b="${2:-}"
  [[ -n "$a" && -n "$b" ]] || die "uso: init <a> <b>"
  ensure_subject "$a"
  ensure_subject "$b"

  local slug="${a}-vs-${b}"
  local dir="${BENCH_ROOT}/${slug}"

  if [[ -d "$dir" ]]; then
    warn "pasta já existe: ${dir}"
    return 0
  fi

  mkdir -p "${dir}/deep"
  cat > "${dir}/metadata.json" <<EOF
{
  "generatedAt": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "comparison_type": "pair",
  "slug": "${slug}",
  "subjects": [
    { "slug": "${a}", "path": "OS/${a}/" },
    { "slug": "${b}", "path": "OS/${b}/" }
  ],
  "dimension_pack": "TBD",
  "profile": "standard",
  "skill_version": "1.0.0",
  "output_root": "OS/_bench/${slug}/",
  "artifacts_generated": [],
  "quality_gate_passed": false
}
EOF
  ok "criado ${dir}/"
}

cmd_init_nway() {
  local topic="${1:-}"; shift || true
  [[ -n "$topic" && $# -ge 2 ]] || die "uso: init-nway <topic> <a> <b> [<c> ...]"

  local count=$#
  local slug="${topic}-Nway"
  local dir="${BENCH_ROOT}/${slug}"

  local subjects_json=""
  for s in "$@"; do
    ensure_subject "$s"
    subjects_json+="    { \"slug\": \"${s}\", \"path\": \"OS/${s}/\" },"$'\n'
  done
  subjects_json="${subjects_json%,$'\n'}"

  if [[ -d "$dir" ]]; then
    warn "pasta já existe: ${dir}"
    return 0
  fi

  mkdir -p "${dir}/deep"
  cat > "${dir}/metadata.json" <<EOF
{
  "generatedAt": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "comparison_type": "nway",
  "slug": "${slug}",
  "subject_count": ${count},
  "subjects": [
${subjects_json}
  ],
  "dimension_pack": "TBD",
  "profile": "standard",
  "skill_version": "1.0.0",
  "output_root": "OS/_bench/${slug}/",
  "artifacts_generated": [],
  "quality_gate_passed": false
}
EOF
  ok "criado ${dir}/ com ${count} subjects"
}

cmd_validate() {
  local slug="${1:-}"
  [[ -n "$slug" ]] || die "uso: validate <slug>"
  local dir="${BENCH_ROOT}/${slug}"
  [[ -d "$dir" ]] || die "benchmark não existe: ${dir}"

  title "Validando ${slug}:"

  local fail=0
  local metadata="${dir}/metadata.json"

  # Metadata
  if [[ -f "$metadata" ]]; then
    local mstat
    mstat="$(json_parseable "$metadata")"
    if [[ "$mstat" == "ok" ]]; then
      ok "metadata.json parseia"
    else
      err "metadata.json: ${mstat}"; fail=1
    fi
  else
    err "metadata.json ausente"; fail=1
  fi

  # Determinar comparison_type (via grep raso, sem jq)
  local ctype="pair"
  if [[ -f "$metadata" ]] && grep -q '"comparison_type": *"nway"' "$metadata" 2>/dev/null; then
    ctype="nway"
  fi

  # Required por tipo
  local required_pair=(
    "comparison-matrix.json" "comparison-matrix.md"
    "scorecard.json" "scorecard.md"
    "gap-analysis.json" "gap-analysis.md"
    "battle-card.md" "executive-report.md"
  )
  local required_nway=(
    "comparison-matrix.json" "comparison-matrix.md"
    "scorecard.json" "scorecard.md"
    "executive-report.md"
  )

  local required=()
  if [[ "$ctype" == "nway" ]]; then
    required=("${required_nway[@]}")
  else
    required=("${required_pair[@]}")
  fi

  for f in "${required[@]}"; do
    if [[ -f "${dir}/${f}" ]]; then
      if [[ "$f" == *.json ]]; then
        local s
        s="$(json_parseable "${dir}/${f}")"
        if [[ "$s" == "ok" ]]; then
          ok "$f"
        else
          err "$f: ${s}"; fail=1
        fi
      else
        ok "$f"
      fi
    else
      err "$f ausente"; fail=1
    fi
  done

  # Inventories: requer ≥2 inventory-*.json
  local inv_count
  inv_count=$(find "${dir}" -maxdepth 1 -name 'inventory-*.json' -type f 2>/dev/null | wc -l | tr -d ' ')
  if [[ $inv_count -ge 2 ]]; then
    ok "inventários: ${inv_count}"
  else
    err "inventários: ${inv_count} (esperado ≥2)"; fail=1
  fi

  # Pasta deep/
  if [[ -d "${dir}/deep" ]]; then
    ok "deep/ existe"
  else
    warn "deep/ ausente (opcional)"
  fi

  echo ""
  if [[ $fail -eq 0 ]]; then
    ok "${BOLD}quality gate: PASS${RESET}"
    return 0
  else
    err "${BOLD}quality gate: FAIL${RESET}"
    return 1
  fi
}

cmd_index() {
  local idx="${BENCH_ROOT}/INDEX.md"
  title "Regenerando ${idx}..."

  {
    echo "# OS Benchmarks — Index"
    echo ""
    echo "_Regenerado em $(date -u +%Y-%m-%d) via \`scripts/bench.sh index\`._"
    echo ""
    echo "| Slug | Type | Pack | Generated | Quality Gate |"
    echo "|------|------|------|-----------|--------------|"

    for d in "${BENCH_ROOT}"/*/; do
      [[ -d "$d" ]] || continue
      local name="$(basename "$d")"
      [[ "$name" == "_inventories" ]] && continue
      local metadata="${d}metadata.json"
      local ctype="?"; local pack="?"; local gen="?"; local qg="?"
      if [[ -f "$metadata" ]]; then
        ctype=$(awk -F'"' '/"comparison_type"/{print $4; exit}' "$metadata" 2>/dev/null || echo "?")
        pack=$(awk -F'"' '/"dimension_pack"/{print $4; exit}' "$metadata" 2>/dev/null || echo "?")
        gen=$(awk -F'"' '/"generatedAt"/{print $4; exit}' "$metadata" 2>/dev/null || echo "?")
        [[ -z "$ctype" ]] && ctype="?"
        [[ -z "$pack" ]] && pack="?"
        [[ -z "$gen" ]] && gen="?"
        if grep -q '"quality_gate_passed": *true' "$metadata" 2>/dev/null; then
          qg="PASS"
        else
          qg="PENDING"
        fi
      fi
      echo "| ${name} | ${ctype} | ${pack} | ${gen} | ${qg} |"
    done
    echo ""
    echo "---"
    echo ""
    echo "Gerado por \`os-bench\` skill v1.0.0"
  } > "${idx}"

  ok "INDEX.md atualizado"
}

cmd_clean() {
  local slug="${1:-}"
  [[ -n "$slug" ]] || die "uso: clean <slug>"
  local dir="${BENCH_ROOT}/${slug}"
  [[ -d "$dir" ]] || die "benchmark não existe: ${dir}"

  title "Remover ${dir}?"
  read -r -p "Tem certeza? [y/N] " confirm
  if [[ "$confirm" =~ ^[Yy]$ ]]; then
    rm -rf "$dir"
    ok "removido ${dir}"
  else
    log "cancelado"
  fi
}

# ============================================================
# Dispatch
# ============================================================

cmd="${1:-help}"
shift || true

case "$cmd" in
  help|-h|--help)  cmd_help "$@" ;;
  list|ls)         cmd_list "$@" ;;
  plan)            cmd_plan "$@" ;;
  packs)           cmd_packs "$@" ;;
  subjects)        cmd_subjects "$@" ;;
  init)            cmd_init "$@" ;;
  init-nway)       cmd_init_nway "$@" ;;
  validate|check)  cmd_validate "$@" ;;
  index)           cmd_index "$@" ;;
  clean|rm)        cmd_clean "$@" ;;
  *)               err "comando desconhecido: $cmd"; cmd_help; exit 1 ;;
esac
