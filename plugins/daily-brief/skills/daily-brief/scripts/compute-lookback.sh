#!/usr/bin/env bash
# Compute the daily-brief lookback window and demos timestamp.
# Outputs JSON with all values needed by Step 1 of the daily-brief skill.
# Usage: ./compute-lookback.sh [state_file_path] [timezone]

set -euo pipefail

STATE_FILE="${1:-Dashboards/snapshots/daily-brief-state.json}"
TZ_NAME="${2:-America/New_York}"
export TZ="$TZ_NAME"

TODAY=$(date +%Y-%m-%d)
DOW=$(date +%u) # 1=Mon … 7=Sun

OS="$(uname)"

if [ "$DOW" -eq 1 ]; then
  # Monday → Friday
  if [ "$OS" = "Darwin" ]; then
    PREV_BIZ=$(date -v-3d +%Y-%m-%d)
  else
    PREV_BIZ=$(date -d "3 days ago" +%Y-%m-%d)
  fi
elif [ "$DOW" -eq 7 ]; then
  # Sunday → Friday
  if [ "$OS" = "Darwin" ]; then
    PREV_BIZ=$(date -v-2d +%Y-%m-%d)
  else
    PREV_BIZ=$(date -d "2 days ago" +%Y-%m-%d)
  fi
else
  if [ "$OS" = "Darwin" ]; then
    PREV_BIZ=$(date -v-1d +%Y-%m-%d)
  else
    PREV_BIZ=$(date -d "yesterday" +%Y-%m-%d)
  fi
fi

# With TZ exported, date commands use the configured timezone
if [ "$OS" = "Darwin" ]; then
  CUTOFF_UNIX=$(date -j -f "%Y-%m-%d %H:%M:%S" "$PREV_BIZ 17:00:00" +%s)
else
  CUTOFF_UNIX=$(date -d "$PREV_BIZ 17:00:00" +%s)
fi

CURRENT_UNIX=$(date +%s)
CURRENT_ISO=$(date +%Y-%m-%dT%H:%M:%S%z | sed 's/\([0-9][0-9]\)\([0-9][0-9]\)$/\1:\2/')
CURRENT_TIME=$(date +%-I:%M\ %p)
TZ_ABBREV=$(date +%Z)

# Read demos lookback from state file, fall back to 24h ago
DEMOS_LOOKBACK_UNIX=""
DEMOS_LOOKBACK_ISO=""
if [ -f "$STATE_FILE" ]; then
  DEMOS_LOOKBACK_UNIX=$(python3 -c "
import json, sys
try:
    with open('$STATE_FILE') as f:
        d = json.load(f)
    print(d.get('last_run_unix', ''))
except Exception:
    print('')
" 2>/dev/null || echo "")
  DEMOS_LOOKBACK_ISO=$(python3 -c "
import json, sys
try:
    with open('$STATE_FILE') as f:
        d = json.load(f)
    print(d.get('last_run_iso', ''))
except Exception:
    print('')
" 2>/dev/null || echo "")
fi

if [ -z "$DEMOS_LOOKBACK_UNIX" ]; then
  DEMOS_LOOKBACK_UNIX=$((CURRENT_UNIX - 86400))
  DEMOS_LOOKBACK_ISO="(24h fallback)"
fi

cat <<EOF
{
  "today": "$TODAY",
  "prev_biz_day": "$PREV_BIZ",
  "cutoff_unix": $CUTOFF_UNIX,
  "current_unix": $CURRENT_UNIX,
  "current_iso": "$CURRENT_ISO",
  "current_time": "$CURRENT_TIME $TZ_ABBREV",
  "timezone": "$TZ_NAME",
  "timezone_abbrev": "$TZ_ABBREV",
  "demos_lookback_unix": $DEMOS_LOOKBACK_UNIX,
  "demos_lookback_iso": "$DEMOS_LOOKBACK_ISO"
}
EOF
