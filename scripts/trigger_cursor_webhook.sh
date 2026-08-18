#!/usr/bin/env bash
# Trigger a Cursor Automation webhook with a hard retry cap.
# Required env: CURSOR_AUTOMATION_WEBHOOK_URL, CURSOR_AUTOMATION_WEBHOOK_TOKEN
# Optional env: REASON, MAX_ATTEMPTS (default 3)
set -euo pipefail

url="${CURSOR_AUTOMATION_WEBHOOK_URL:-}"
token="${CURSOR_AUTOMATION_WEBHOOK_TOKEN:-}"
reason="${REASON:-manual}"
max_attempts="${MAX_ATTEMPTS:-3}"

if [[ -z "$url" || -z "$token" ]]; then
  echo "Missing CURSOR_AUTOMATION_WEBHOOK_URL or CURSOR_AUTOMATION_WEBHOOK_TOKEN." >&2
  echo "Add them as GitHub Actions secrets; do not commit the values." >&2
  exit 1
fi

# Accept either "crsr_..." or "Bearer crsr_..."
token="${token#Bearer }"
token="${token#bearer }"

# Seconds to wait BEFORE attempts 2 and 3
sleep_before=(0 180 300)

retryable() {
  local code="$1"
  local body="$2"
  case "$code" in
    408|425|429|500|502|503|504) return 0 ;;
  esac
  # Cursor returns HTTP 400 with resource_exhausted when Cloud Agent slots are full.
  if echo "$body" | grep -Eiq 'resource_exhausted|too many concurrent|rate[- ]limited|temporarily unavailable|service unavailable|failed to start background composer'; then
    return 0
  fi
  return 1
}

attempt=1
while [[ "$attempt" -le "$max_attempts" ]]; do
  delay="${sleep_before[$((attempt - 1))]:-300}"
  if [[ "$delay" -gt 0 ]]; then
    echo "Retryable failure. Waiting ${delay}s before attempt ${attempt}/${max_attempts}..."
    sleep "$delay"
  fi

  echo "Attempt ${attempt}/${max_attempts}: POST webhook (reason=${reason})"
  tmp="$(mktemp)"
  http_code="$(
    curl -sS -o "$tmp" -w "%{http_code}" \
      -X POST "$url" \
      -H "Authorization: Bearer ${token}" \
      -H "Content-Type: application/json" \
      -d "{\"reason\":\"${reason}\",\"source\":\"github-actions\",\"attempt\":${attempt}}" \
      || true
  )"
  body="$(cat "$tmp")"
  rm -f "$tmp"

  echo "HTTP ${http_code}"
  if [[ -n "$body" ]]; then
    echo "$body" | head -c 800
    echo
  fi

  if [[ "$http_code" =~ ^2 ]]; then
    if retryable "$http_code" "$body"; then
      echo "HTTP 2xx but response looks rate-limited."
    else
      echo "Trigger accepted."
      exit 0
    fi
  elif [[ "$http_code" == "401" || "$http_code" == "403" ]]; then
    echo "Auth rejected. Regenerate the webhook token in Automations and update the GitHub secret." >&2
    exit 1
  elif [[ "$http_code" == "000" ]]; then
    echo "Network/curl failure."
  elif ! retryable "$http_code" "$body"; then
    echo "Non-retryable HTTP ${http_code}." >&2
    exit 1
  fi

  attempt=$((attempt + 1))
done

echo "Gave up after ${max_attempts} attempts." >&2
exit 1
