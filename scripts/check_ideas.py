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
- UNFILLED     — an unfilled `[[fill:…]]` auto-draft stub slot committed in an
                 idea file (a pasted --emit-entries stub must be fully filled;
                 backtick-quoted mentions of the slot grammar are exempt).
- GROUNDING    — a `> **Grounding:**` optional header line (README § Idea file
                 grammar, blessed by PR #21) present but malformed: must be
                 `> **Grounding:** <url>@<sha> · fetched <ISO time>` with an
                 optional ` (manifest row: behind|matches|ahead)` suffix.
- SEQUENCE     — a `> **Sequence:**` optional header line present but malformed:
                 must be `> **Sequence:** <before|after|behind> <event/order/claim>`.

The two optional-line checks fire only where the line is present (the lines are
forward-only — retrofit never required). Severity is date-gated on the filename's
YYYY-MM-DD: files dated on or after the grammar bless date (PR #21 merged
2026-07-10) get a hard violation (gate tightened `>` → `>=` per the PR #24 card
part b, once the boundary day ran clean at 0 warnings); files dated before it
and files without a parseable date get an advisory WARN that never affects the
exit code (legacy files are not churned; the debt is reported, not enforced).

`--outbox` switches to outbox↔ideas link-integrity mode (README § The outbox) and
validates `control/outbox.md` against the tree instead:

- PROPOSAL     — a `## PROPOSAL` block whose heading is not
                 `## PROPOSAL <nnn> · <ISO8601> · status: sim-ready`, or missing a
                 required field (`target:` / `idea:` / `question:` / `done-when:`;
                 `depends:` is OPTIONAL).
- LINK         — a proposal's `idea:` line carries no this-repo `ideas/…` link, the
                 linked idea file does not exist, or its state is not `sim-ready`
                 (`historical(…)` is also legal — a proposal outlives its idea's
                 advance to built, states move forward only).
- UNPROPOSED   — an ideas/ file in state `sim-ready` that no outbox PROPOSAL names
                 (a sim-ready verdict that never reached the sim-lab pull surface).

Shape only — it cannot judge honesty ("confident padding" passes); it exists to kill
silent half-probes and grammar drift. Report-only: it never edits files.

Usage:
    python3 scripts/check_ideas.py                # lint ./ideas
    python3 scripts/check_ideas.py --ideas-dir D  # lint another tree
    python3 scripts/check_ideas.py --outbox       # outbox↔ideas integrity mode
    python3 scripts/check_ideas.py --outbox F --ideas-dir D  # …against another tree

Exit codes: 0 = clean · 1 = violations found · 2 = no tree/outbox to lint.
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
# Unfilled auto-draft stub slots (PR #47 card 💡): `--emit-entries` stubs use the
# kit's `[[fill:…]]` slot grammar; a stub pasted into a committed idea file
# UNFILLED must red the run. Backtick-quoted mentions (prose ABOUT the grammar —
# three live instances) are exempt: a real slot is never backtick-wrapped.
UNFILLED_SLOT_RE = re.compile(r"(?<!`)\[\[fill:")

# Optional header lines (README § Idea file grammar — the PR #21 bless; same loud
# co-edit rule as above). Checked only where present: a line that *carries* the bold
# label is held to the blessed byte-form; a file without the line passes untouched
# (forward-only — retrofit never required). `## Grounding` heading sections are a
# different, older construct and are deliberately NOT matched here.
OPTIONAL_LABEL_RE = re.compile(r"^\s*(?:>\s*)?\*\*(Grounding|Sequence):\*\*\s?(.*)$")
GROUNDING_PREFIX = "> **Grounding:** "
SEQUENCE_PREFIX = "> **Sequence:** "
GROUNDING_BODY_RE = re.compile(
    r"^https?://\S+@[0-9a-fA-F]{7,40}"                       # <url>@<sha>
    r" · fetched \d{4}-\d{2}-\d{2}(?:T\d{2}:\d{2}(?::\d{2})?Z?)?"  # · fetched <ISO time>
    r"(?: \(manifest row: (?:behind|matches|ahead)\))?$"     # optional staleness flag
)
SEQUENCE_BODY_RE = re.compile(r"^(?:before|after|behind) \S.*$")
# Severity date-gate: the optional-line grammar was blessed by PR #21 (merged
# 2026-07-10). Files whose filename date is on or after that date must conform
# (hard violation — tightened from strictly-after per the PR #24 card part b once
# the boundary day ran clean); earlier-dated filenames — and filenames without a
# parseable date — WARN only (advisory, never exit-affecting; legacy files are
# reported as debt, never churned).
OPTIONAL_LINE_GRAMMAR_DATE = "2026-07-10"
FILENAME_DATE_RE = re.compile(r"-(\d{4}-\d{2}-\d{2})\.md$")

# Outbox grammar constants (README § The outbox — same co-edit rule as above).
PROPOSAL_HEADING_RE = re.compile(r"^## PROPOSAL .*$", re.MULTILINE)
LEGAL_PROPOSAL_HEADING_RE = re.compile(
    r"^## PROPOSAL \d{3} · \d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z · status: sim-ready\s*$"
)
PROPOSAL_REQUIRED_FIELDS = ("target", "idea", "question", "done-when")  # depends: OPTIONAL
THIS_REPO = "menno420/idea-engine"
# An `idea:` link must point into THIS repo's ideas/ tree (blob or raw path form).
IDEA_LINK_RE = re.compile(
    rf"https://(?:github\.com/{THIS_REPO}/blob|raw\.githubusercontent\.com/{THIS_REPO})"
    rf"/[^/\s]+/(ideas/\S+?\.md)"
)
SIM_READY_STATE = "sim-ready"
# A proposal outlives its idea's advance to built (states move forward only, the
# outbox is append-only) — `historical(…)` therefore also satisfies the link check.
LINKED_STATE_OK_RE = re.compile(r"^(?:sim-ready$|historical\()")


def optional_lines_hard(name: str) -> bool:
    """True when a malformed optional line is a hard violation for this file:
    the filename date is on or after the PR #21 grammar bless date (>= per the
    PR #24 card part b). Undated or earlier-dated filenames stay advisory (WARN)."""
    m = FILENAME_DATE_RE.search(name)
    return bool(m) and m.group(1) >= OPTIONAL_LINE_GRAMMAR_DATE


def check_optional_lines(text: str, rel: str) -> list[str]:
    """Shape-check `> **Grounding:**` / `> **Sequence:**` lines where present.
    Returns bare messages; the caller assigns severity via optional_lines_hard()."""
    msgs: list[str] = []
    for lineno, line in enumerate(text.splitlines(), 1):
        m = OPTIONAL_LABEL_RE.match(line)
        if not m:
            continue
        label, prefix = m.group(1), (
            GROUNDING_PREFIX if m.group(1) == "Grounding" else SEQUENCE_PREFIX
        )
        tag = f"{label.upper():<10} {rel}:{lineno}"
        if not line.startswith(prefix):
            msgs.append(f"{tag}: not a `{prefix}…` blockquote line")
            continue
        body = line[len(prefix):].rstrip()
        if label == "Grounding":
            if not GROUNDING_BODY_RE.match(body):
                msgs.append(
                    f"{tag}: not `<url>@<sha> · fetched <ISO time>"
                    f"[ (manifest row: behind|matches|ahead)]`"
                )
        elif not SEQUENCE_BODY_RE.match(body):
            msgs.append(f"{tag}: not `<before|after|behind> <event/order/claim>`")
    return msgs


def first_state(text: str) -> str | None:
    for line in text.splitlines():
        m = STATE_LINE_RE.match(line)
        if m:
            return m.group(1)
    return None


def lint_file(path: Path, rel: str) -> tuple[list[str], list[str]]:
    """Returns (problems, warnings) — problems red the run, warnings are advisory."""
    problems: list[str] = []
    warnings: list[str] = []
    if not FILENAME_RE.match(path.name):
        problems.append(f"FILENAME   {rel}: not <slug>-YYYY-MM-DD.md")

    text = path.read_text(encoding="utf-8")

    state = first_state(text)
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

    for lineno, line in enumerate(text.splitlines(), 1):
        if UNFILLED_SLOT_RE.search(line):
            problems.append(
                f"UNFILLED   {rel}:{lineno}: unfilled `[[fill:…]]` stub slot — "
                f"fill every slot before committing an --emit-entries stub"
            )

    opt = check_optional_lines(text, rel)
    (problems if optional_lines_hard(path.name) else warnings).extend(opt)

    return problems, warnings


def check_outbox(outbox_path: Path, ideas_dir: Path) -> list[str] | int:
    """Outbox↔ideas link integrity. Returns violations, or an exit code on
    usage/internal error (missing outbox — an empty scan must never report clean)."""
    if not outbox_path.is_file():
        print(f"check_ideas: no outbox file at {outbox_path}", file=sys.stderr)
        return 2

    text = outbox_path.read_text(encoding="utf-8")
    root = ideas_dir.parent  # `ideas/…` link paths resolve against the tree root
    problems: list[str] = []
    linked_paths: set[str] = set()

    headings = list(PROPOSAL_HEADING_RE.finditer(text))
    bounds = [m.start() for m in headings] + [len(text)]
    for i, m in enumerate(headings):
        block = text[bounds[i] : bounds[i + 1]]
        num_m = re.search(r"PROPOSAL (\d+)", m.group(0))
        where = f"PROPOSAL {num_m.group(1)}" if num_m else f"proposal block #{i + 1}"

        if not LEGAL_PROPOSAL_HEADING_RE.match(m.group(0)):
            problems.append(
                f"PROPOSAL   {where}: heading not `## PROPOSAL <nnn> · <ISO8601> · status: sim-ready`"
            )
        fields = {
            fm.group(1): fm.group(2).strip()
            for fm in re.finditer(r"^([a-z-]+):\s*(.*)$", block, re.MULTILINE)
        }
        for field in PROPOSAL_REQUIRED_FIELDS:
            if not fields.get(field):
                problems.append(f"PROPOSAL   {where}: missing required field `{field}:`")

        idea_line = fields.get("idea", "")
        if not idea_line:
            continue  # already flagged above; nothing to resolve
        link_m = IDEA_LINK_RE.search(idea_line)
        if not link_m:
            problems.append(
                f"LINK       {where}: `idea:` carries no {THIS_REPO} ideas/ link"
            )
            continue
        rel = link_m.group(1)
        linked_paths.add(rel)
        idea_path = root / rel
        if not idea_path.is_file():
            problems.append(f"LINK       {where}: linked idea file {rel} does not exist")
            continue
        state = first_state(idea_path.read_text(encoding="utf-8"))
        if state is None or not LINKED_STATE_OK_RE.match(state):
            problems.append(
                f"LINK       {where}: linked idea {rel} state {state!r} is not "
                f"sim-ready (or historical(…))"
            )

    # Reverse pass: every sim-ready idea must be named by an outbox proposal.
    for path in sorted(p for p in ideas_dir.rglob("*.md") if p.name != "README.md"):
        rel = str(path.relative_to(root))
        if first_state(path.read_text(encoding="utf-8")) == SIM_READY_STATE:
            if rel not in linked_paths:
                problems.append(
                    f"UNPROPOSED {rel}: state 'sim-ready' but no outbox PROPOSAL names it"
                )

    return problems


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument(
        "--ideas-dir", default=str(REPO_ROOT / "ideas"), help="ideas tree to lint"
    )
    ap.add_argument(
        "--outbox",
        nargs="?",
        const=str(REPO_ROOT / "control" / "outbox.md"),
        default=None,
        metavar="FILE",
        help="outbox↔ideas link-integrity mode (default FILE: control/outbox.md)",
    )
    args = ap.parse_args()

    ideas_dir = Path(args.ideas_dir)
    if not ideas_dir.is_dir():
        print(f"check_ideas: no ideas dir at {ideas_dir}", file=sys.stderr)
        return 2

    if args.outbox is not None:
        result = check_outbox(Path(args.outbox), ideas_dir)
        if isinstance(result, int):
            return result
        for p in result:
            print(p)
        if result:
            print(f"check_ideas: FAIL — {len(result)} outbox↔ideas violation(s)")
            return 1
        print("check_ideas: OK — outbox proposals and sim-ready ideas are consistent")
        return 0

    files = sorted(
        p for p in ideas_dir.rglob("*.md") if p.name != "README.md"
    )
    if not files:  # fail loud: an empty scan must never report a false clean
        print(f"check_ideas: no idea files under {ideas_dir}", file=sys.stderr)
        return 2

    problems: list[str] = []
    warnings: list[str] = []
    for path in files:
        p, w = lint_file(path, str(path.relative_to(ideas_dir.parent)))
        problems.extend(p)
        warnings.extend(w)

    for w in warnings:  # advisory only — legacy optional-line debt, never exit-affecting
        print(f"warn: {w}")
    for p in problems:
        print(p)
    if problems:
        print(f"check_ideas: FAIL — {len(problems)} violation(s) across {len(files)} idea files"
              + (f" (+{len(warnings)} warning(s), advisory)" if warnings else ""))
        return 1
    print(f"check_ideas: OK — {len(files)} idea files conform to the README grammar"
          + (f" ({len(warnings)} warning(s), advisory)" if warnings else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
