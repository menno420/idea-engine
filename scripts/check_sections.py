#!/usr/bin/env python3
"""check_sections.py — roster-derived section sync checker (stdlib only).

Diffs this repo's `ideas/<section>/` directories against the ACTIVE lane rows of the
fleet's canonical lane registry and reports drift:

- MISSING section — an active lane has no `ideas/<section>/` directory.
- ORPHAN section  — an `ideas/<section>/` directory matches no active lane (a closed
  lane's leftover, or an ad-hoc invention the README forbids).

Canonical source (since 2026-07-11): the fleet-manager GENERATED roster
(`docs/roster.md`, regenerated each manager wake) — the hand-maintained superbot
fleet manifest (`docs/eap/fleet-manifest.md`) was SUPERSEDED that day (fleet-manager
PR #59, merge `b0639a9`; the manifest file itself carries the pointer and its table
was removed, which is exactly the format change this checker's original fail-loud
message anticipated). The legacy manifest parser is retained for offline runs
against saved historical copies. Both sources are read-only to this repo (public
raw path, Q-0260).

Convention source: README.md § Sections — one section per active fleet lane, plus the
always-expected `fleet` section for cross-cutting ideas.

Usage:
    python3 scripts/check_sections.py                  # fetch the roster from the raw URL
    python3 scripts/check_sections.py --manifest FILE  # offline run against a saved copy
                                                       # (roster or legacy-manifest format,
                                                       # auto-detected by table header)

Exit codes: 0 = in sync · 1 = drift found · 2 = could not read/parse the source.
"""

from __future__ import annotations

import argparse
import re
import sys
import urllib.request
from pathlib import Path

# Canonical since the 2026-07-11 manifest supersession (fleet-manager PR #59).
ROSTER_URL = (
    "https://raw.githubusercontent.com/menno420/fleet-manager/main/docs/roster.md"
)
# Legacy source, historical only — its table was removed at supersession; kept for
# provenance and for offline runs against saved copies.
MANIFEST_URL = (
    "https://raw.githubusercontent.com/menno420/superbot/main/docs/eap/fleet-manifest.md"
)
REPO_ROOT = Path(__file__).resolve().parent.parent
OWNER = "menno420"

# Roster tables are headed `| Lane | …` (generated); legacy manifest tables were
# headed `| Project | Repo(s) | …` (hand-maintained). Detect by header, loudly.
ROSTER_HEADER_RE = re.compile(r"^\|\s*Lane\s*\|", re.MULTILINE)

# Sections expected regardless of registry rows (README § Sections: `ideas/fleet/` is
# the cross-cutting section, not a lane row).
ALWAYS_EXPECTED = {"fleet"}

# Registry rows that are fleet PIPELINE infrastructure, not build lanes — they get no
# section. Keep this list short and loud:
# - fleet-manager: the control chair (Q-0264 final review + ORDER routing); ideas
#   aimed at it live in `ideas/fleet/` (pre-supersession precedent, unchanged).
# - sim-lab: the pipeline's verdict stage (Q-0264: idea-engine → sim-lab → manager),
#   not a build lane; no `ideas/sim-lab/` section has ever existed — simulator-shaped
#   ideas ride `ideas/fleet/` or the proposing section (e.g. the superbot
#   brainstorm-simulator ideas).
# - idea-engine: this repo itself; its own process/tooling ideas live in
#   `ideas/fleet/` (established practice: section-sync-checker, preflight wrapper,
#   harvest-freshness checker, open-work sweep — all `ideas/fleet/` entries).
NON_LANE_REPOS = {"fleet-manager", "sim-lab", "idea-engine"}

# Textual markers of a non-active row (hand-maintained living ledger — heuristics are
# unavoidable; parse failures must fail LOUD, never report a false clean).
CLOSED_MARKERS = ("project closed",)

# The manifest's own retirement tombstone (superbot 34ebbac1, 2026-07-11T02:34Z:
# "retire fleet-manifest to pointer stub" — Status flipped to historical, all table
# rows removed, canonical fleet state moved to the fleet-manager GENERATED roster).
# HISTORY: the PR #64 sibling detected this marker as an interim exit-0 advisory
# carve-out (the tombstone had redded every non-control CI run ~10 min after it
# landed upstream) and queued the roster re-point as a follow-up slice; the sibling
# slice that merged with it SHIPPED that re-point (read_source fetches the roster,
# roster_sections parses it), so the carve-out is retired — the live path never
# sees the tombstone anymore. The marker is kept to NAME the tombstone when an
# offline `--manifest` run points at the retired file (a usage error, exit 2 —
# never a silent or false clean).
SUPERSEDED_MARKER = "superseded"


def read_source(path: str | None) -> str:
    """A local saved copy (either format), or the live canonical roster."""
    if path:
        return Path(path).read_text(encoding="utf-8")
    with urllib.request.urlopen(ROSTER_URL, timeout=30) as resp:
        return resp.read().decode("utf-8")


def roster_sections(roster: str) -> set[str]:
    """Sections implied by the generated roster's active lane rows (fleet-manager
    `docs/roster.md`): the Lane cell of every table row, minus registry-only seats
    (rows declaring "NO repo" — e.g. a chat-coordinator seat), archived lanes (rows
    marked wound down), and the NON_LANE_REPOS pipeline infrastructure. Lane display
    decorations (`**bold**`, `(hub)`, `(NEW)`, `· Seat A`) are stripped; a lane cell
    that still doesn't reduce to a repo-name token fails LOUD — never a silent skip,
    a false clean is worse than a crash.

    Scope: ONLY the first `| Lane |`-headed table. Roster generation #5
    (machine-generated, 2026-07-11T04:28Z) added a SECOND table to the doc (the
    tool-verification sample, headed `| Lane (sample class) |`) — parsing every
    `|` line in the file swallowed that table too and invented phantom lanes
    (`lane` from its header, `codetool-lab-fable5` from a sample row whose cells
    carry no wind-down marker), redding every non-control CI run. Rows are
    collected strictly between the exact `Lane` header and the first non-table
    line after it; later tables are never lane rows."""
    sections: set[str] = set()
    rows_seen = 0
    in_table = False
    for line in roster.splitlines():
        if not line.lstrip().startswith("|"):
            if in_table:
                break  # the roster table ended — later tables are not lane rows
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2:
            continue
        lane = re.sub(r"\*+", "", cells[0]).strip()
        if not in_table:
            if lane.lower() == "lane":
                in_table = True  # the roster table's exact header row
            continue  # any pre-header table line is not a lane row
        if lane == "" or set(cells[0]) <= {"-", " ", ":"}:
            continue  # separator row
        rows_seen += 1
        if lane.startswith("↳"):
            # Roster generation #9 (fleet-manager PR #86) added `↳` sub-rows under
            # parent lanes (e.g. `↳ substrate-kit — \`control/status-…\``): detail
            # rows of the lane above, not lanes themselves — no section. Anything
            # else unparseable still fails LOUD below.
            continue
        row_l = line.lower()
        if "no repo" in lane.lower():
            # Registry-only seat — the Lane cell itself declares "NO repo" (e.g. a
            # chat-coordinator seat over other lanes): no repo, no section. Checked
            # on the Lane cell only — a full-row substring match false-positives on
            # prose like "No repo wake trigger" in the Wake-state cell.
            continue
        if len(cells) > 1 and "registry-only seat" in cells[1].lower():
            # Registry-only seat, heartbeat-cell variant — the 2026-07-14 roster
            # generation added grouped seat rows (e.g. `SuperBot World seat
            # (games+idle+mineverse)`, `Ideas Lab seat (idea-engine+sim-lab)`)
            # whose Lane cell carries no "NO repo" marker; the declaration moved
            # to the heartbeat cell (`n/a — registry-only seat (no repo)`).
            # Checked on the heartbeat cell ONLY (cells[1]) — same rationale as
            # the Lane-cell rule above: a full-row substring match could
            # false-positive on prose in the Phase/Wake-state cells. Any other
            # unparseable lane cell still fails LOUD below.
            continue
        if "wound down" in row_l or "wind-down complete" in row_l:
            continue  # archived lane (the roster's textual closed marker)
        name = re.split(r"\s*[(·]", lane)[0].strip().lower()
        if not re.fullmatch(r"[a-z0-9][a-z0-9.-]*", name):
            raise ValueError(
                f"unparseable roster lane cell {cells[0]!r} — roster format "
                "changed? update this parser, do not trust this run"
            )
        if name in NON_LANE_REPOS:
            continue
        sections.add(name)
    if rows_seen == 0:
        raise ValueError(
            "no roster table rows parsed — roster format changed? update this "
            "parser, do not trust this run"
        )
    return sections


def active_sections(manifest: str) -> set[str]:
    """LEGACY (pre-supersession manifest format, offline copies only): sections
    implied by the manifest's active lane rows — first `menno420/<repo>` in the
    Repo(s) cell of every table row that is not closed and has a real repo."""
    sections: set[str] = set()
    rows_seen = 0
    for line in manifest.splitlines():
        if not line.lstrip().startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 2:
            continue
        project = cells[0].strip("* ").lower()
        if project in ("project", "") or set(cells[0]) <= {"-", " ", ":"}:
            continue  # header / separator row
        rows_seen += 1
        row_l = line.lower()
        if any(m in row_l for m in CLOSED_MARKERS):
            continue
        repo_match = re.search(rf"{OWNER}/([\w.-]+)", cells[1])
        if not repo_match:
            continue  # no real repo (e.g. repos not created yet) -> no lane state
        repo = repo_match.group(1)
        if repo in NON_LANE_REPOS:
            continue
        sections.add(repo)
    if rows_seen == 0:
        raise ValueError(
            "no table rows parsed — manifest format changed? (it is slated to be "
            "replaced by a generated roster; update this parser, do not trust this run)"
        )
    return sections


def actual_sections(ideas_dir: Path) -> set[str]:
    return {p.name for p in ideas_dir.iterdir() if p.is_dir()}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument(
        "--manifest",
        help="path to a local saved copy (offline run; roster or legacy-manifest "
        "format, auto-detected by table header)",
    )
    ap.add_argument(
        "--ideas-dir", default=str(REPO_ROOT / "ideas"), help="ideas tree to check"
    )
    args = ap.parse_args()

    try:
        source = read_source(args.manifest)
    except Exception as exc:  # fail loud: a false clean is worse than a crash
        print(f"check_sections: cannot read lane registry: {exc}", file=sys.stderr)
        return 2
    try:
        if ROSTER_HEADER_RE.search(source):
            expected = roster_sections(source) | ALWAYS_EXPECTED
        else:
            expected = active_sections(source) | ALWAYS_EXPECTED
    except Exception as exc:  # fail loud — naming the tombstone when it is the cause
        if SUPERSEDED_MARKER in source.lower():
            # Only reachable via an explicit --manifest pointing at the retired
            # manifest file: the live path fetches the roster (see the
            # SUPERSEDED_MARKER comment above for the PR #64 interim-carve-out
            # history this replaces).
            print(
                "check_sections: the given source is the fleet manifest's "
                "retirement tombstone (zero lane rows — SUPERSEDED 2026-07-11 by "
                "the fleet-manager GENERATED roster, menno420/fleet-manager "
                "docs/roster.md). This checker now reads the roster by default: "
                "rerun without --manifest, or point it at a roster copy.",
                file=sys.stderr,
            )
            return 2
        print(f"check_sections: cannot parse lane registry: {exc}", file=sys.stderr)
        return 2

    ideas_dir = Path(args.ideas_dir)
    if not ideas_dir.is_dir():
        print(f"check_sections: no ideas dir at {ideas_dir}", file=sys.stderr)
        return 2
    actual = actual_sections(ideas_dir)

    missing = sorted(expected - actual)
    orphans = sorted(actual - expected)
    for s in missing:
        print(f"MISSING section: ideas/{s}/ (active lane in the registry, no directory)")
    for s in orphans:
        print(f"ORPHAN section:  ideas/{s}/ (no active lane row in the registry)")
    if missing or orphans:
        print(f"check_sections: DRIFT — {len(missing)} missing, {len(orphans)} orphan")
        return 1
    print(f"check_sections: OK — {len(actual)} sections in sync with the lane registry")
    return 0


if __name__ == "__main__":
    sys.exit(main())
