#!/usr/bin/env python3
"""check_ideas.py — idea-grammar lint for the ideas/ tree (stdlib only).

Lints every idea file against the README idea grammar (README § Idea file grammar +
§ The probe battery) and reports violations:

- FILENAME     — not `<slug>-YYYY-MM-DD.md` (section `README.md` files are exempt).
- STATE        — state line missing, or not one of the legal states:
                 captured | probed | sim-ready | parked(<reason>) |
                 park(built-here — <what shipped>) | rejected(<reason>) |
                 historical(<merged PR>).
- PROBE        — a `## Probe report` section missing any of the 8 battery questions,
                 or not ending in exactly ONE legal recommendation
                 (sim-ready / park / reject / needs-more-grooming; park may carry
                 a `(built-here — …)` qualifier per the PR #6 grammar).
- HALF-PROBE   — state claims `probed`/`sim-ready` but the file has no probe report.
- LINK-INDEX   — a harvested link-index entry (declares a canonical idea elsewhere)
                 without a canonical `https://github.com/…` link.

Shape only — it cannot judge honesty ("confident padding" passes); it exists to kill
silent half-probes and grammar drift. Report-only: it never edits files.

Usage:
    python3 scripts/check_ideas.py                # lint ./ideas
    python3 scripts/check_ideas.py --ideas-dir D  # lint another tree

Exit codes: 0 = clean · 1 = violations found · 2 = no ideas tree to lint.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Grammar constants — ONE edit here per README grammar change (keep them in sync,
# loudly: a loosened pattern silently passes new violations).
FILENAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]*-\d{4}-\d{2}-\d{2}\.md$")
STATE_LINE_RE = re.compile(r"^> \*\*State:\*\* (.+?)\s*$")
LEGAL_STATE_RE = re.compile(
    r"^(?:captured|probed|sim-ready"
    r"|parked\(.+\)"
    r"|park\(built-here\b.*\)"
    r"|rejected\(.+\)"
    r"|historical\(.+\))$"
)
PROBE_HEADING_RE = re.compile(r"^## Probe report\b", re.MULTILINE)
QUESTION_MARKS = [re.compile(rf"^\*\*{n}\.\s", re.MULTILINE) for n in range(1, 9)]
RECOMMENDATION_RE = re.compile(r"^\*\*Recommendation:", re.MULTILINE)
LEGAL_RECOMMENDATION_RE = re.compile(
    r"^\*\*Recommendation: (?:sim-ready|park(?:\(built-here\b[^)]*\))?"
    r"|reject|needs-more-grooming)\*\*",
    re.MULTILINE,
)
CANONICAL_MARKER = "Canonical idea"
CANONICAL_LINK_RE = re.compile(
    r"https://(?:github\.com|raw\.githubusercontent\.com)/\S+"
)


def lint_file(path: Path, rel: str) -> list[str]:
    problems: list[str] = []
    if not FILENAME_RE.match(path.name):
        problems.append(f"FILENAME   {rel}: not <slug>-YYYY-MM-DD.md")

    text = path.read_text(encoding="utf-8")

    state = None
    for line in text.splitlines():
        m = STATE_LINE_RE.match(line)
        if m:
            state = m.group(1)
            break
    if state is None:
        problems.append(f"STATE      {rel}: no `> **State:** …` line")
    elif not LEGAL_STATE_RE.match(state):
        problems.append(f"STATE      {rel}: illegal state {state!r}")

    # Probe reports are appended, never rewritten — lint each block independently.
    blocks = PROBE_HEADING_RE.split(text)[1:]  # text after each probe heading
    starts = [m.start() for m in PROBE_HEADING_RE.finditer(text)]
    for i, block in enumerate(blocks):
        # A block runs to the next probe heading (split already bounds it).
        where = f"{rel} probe report #{i + 1}"
        missing = [str(n + 1) for n, q in enumerate(QUESTION_MARKS) if not q.search(block)]
        if missing:
            problems.append(f"PROBE      {where}: missing battery question(s) {','.join(missing)}")
        recs = RECOMMENDATION_RE.findall(block)
        if len(recs) != 1:
            problems.append(f"PROBE      {where}: {len(recs)} recommendation lines (need exactly 1)")
        elif not LEGAL_RECOMMENDATION_RE.search(block):
            problems.append(f"PROBE      {where}: recommendation is not one of sim-ready/park/reject/needs-more-grooming")
        else:
            q8 = QUESTION_MARKS[7].search(block)
            rec = LEGAL_RECOMMENDATION_RE.search(block)
            if q8 and rec and rec.start() < q8.start():
                problems.append(f"PROBE      {where}: recommendation does not END the report (appears before Q8)")
    if state in ("probed", "sim-ready") and not starts:
        problems.append(f"HALF-PROBE {rel}: state {state!r} but no `## Probe report` section")

    if CANONICAL_MARKER in text and not CANONICAL_LINK_RE.search(text):
        problems.append(f"LINK-INDEX {rel}: declares a canonical idea but carries no canonical GitHub link")

    return problems


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument(
        "--ideas-dir", default=str(REPO_ROOT / "ideas"), help="ideas tree to lint"
    )
    args = ap.parse_args()

    ideas_dir = Path(args.ideas_dir)
    if not ideas_dir.is_dir():
        print(f"check_ideas: no ideas dir at {ideas_dir}", file=sys.stderr)
        return 2

    files = sorted(
        p for p in ideas_dir.rglob("*.md") if p.name != "README.md"
    )
    if not files:  # fail loud: an empty scan must never report a false clean
        print(f"check_ideas: no idea files under {ideas_dir}", file=sys.stderr)
        return 2

    problems: list[str] = []
    for path in files:
        problems.extend(lint_file(path, str(path.relative_to(ideas_dir.parent))))

    for p in problems:
        print(p)
    if problems:
        print(f"check_ideas: FAIL — {len(problems)} violation(s) across {len(files)} idea files")
        return 1
    print(f"check_ideas: OK — {len(files)} idea files conform to the README grammar")
    return 0


if __name__ == "__main__":
    sys.exit(main())
