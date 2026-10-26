#!/usr/bin/env sh
set -eu
command -v node >/dev/null 2>&1 || { echo 'Node.js 20+ required' >&2; exit 1; }
HERE=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
exec node "$HERE/../bin/rcc-consortium" "$@"
