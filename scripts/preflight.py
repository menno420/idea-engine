#!/usr/bin/env python3
"""preflight.py — one-command wake/pre-push preflight wrapper (stdlib only).

Runs the whole preflight ritual in sequence and reports one PASS/FAIL line per
check, exiting with the WORST (max) exit code so a single red check reds the run:

- `check_sections.py`          — partition: sections ↔ fleet-manifest active lanes.
- `check_ideas.py`             — contents: every idea file parses per the README grammar.
- `check_ideas.py --outbox`    — integrity: outbox proposals ↔ sim-ready ideas.
- `bootstrap.py check --strict --status-only` — control gate: the status heartbeat.

Convention source: control/README.md § Per-session ritual + README § Landing
conventions — this collects the (previously discipline-only) multi-command ritual
into one command; each check stays independently runnable. Report-only: it never
edits files. Origin: PR #2 session card 💡 (wake-preflight wiring).

Usage:
    python3 scripts/preflight.py

Exit codes: worst child exit — 0 = all green · 1 = violations · 2 = a check could
not run (missing input / unparseable manifest / crashed child, reported as 2).
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PY = sys.executable or "python3"

# The ritual, in order — ONE edit here per new preflight check (keep in sync with
# control/README.md § Per-session ritual, loudly: a check missing here silently
# falls back to session discipline).
CHECKS: list[tuple[str, list[str]]] = [
    ("check_sections", [PY, "scripts/check_sections.py"]),
    ("check_ideas", [PY, "scripts/check_ideas.py"]),
    ("check_ideas --outbox", [PY, "scripts/check_ideas.py", "--outbox"]),
    ("bootstrap check --strict --status-only",
     [PY, "bootstrap.py", "check", "--strict", "--status-only"]),
]


def main() -> int:
    worst = 0
    for name, cmd in CHECKS:
        try:
            code = subprocess.run(cmd, cwd=REPO_ROOT).returncode
        except OSError as exc:  # fail loud: a check that cannot run is not a pass
            print(f"preflight: could not run {name}: {exc}", file=sys.stderr)
            code = 2
        verdict = "PASS" if code == 0 else "FAIL"
        print(f"preflight: {verdict} — {name} (exit {code})")
        worst = max(worst, code)
    if worst == 0:
        print(f"preflight: OK — all {len(CHECKS)} checks green")
    else:
        print(f"preflight: FAIL — worst exit {worst}")
    return worst


if __name__ == "__main__":
    sys.exit(main())
