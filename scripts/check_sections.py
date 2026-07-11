#!/usr/bin/env python3
"""check_sections.py — manifest-derived section sync checker (stdlib only).

Diffs this repo's `ideas/<section>/` directories against the ACTIVE lane rows of the
fleet manifest (superbot `docs/eap/fleet-manifest.md`) and reports drift:

- MISSING section — an active manifest lane has no `ideas/<section>/` directory.
- ORPHAN section  — an `ideas/<section>/` directory matches no active lane (a closed
  lane's leftover, or an ad-hoc invention the README forbids).

Convention source: README.md § Sections — one section per active fleet lane, plus the
always-expected `fleet` section for cross-cutting ideas. The manifest is read-only to
this repo (public raw path, Q-0260).

Usage:
    python3 scripts/check_sections.py                  # fetch manifest from the raw URL
    python3 scripts/check_sections.py --manifest FILE  # offline run against a saved copy

Exit codes: 0 = in sync · 1 = drift found · 2 = could not read/parse the manifest.
"""

from __future__ import annotations

import argparse
import re
import sys
import urllib.request
from pathlib import Path

MANIFEST_URL = (
    "https://raw.githubusercontent.com/menno420/superbot/main/docs/eap/fleet-manifest.md"
)
REPO_ROOT = Path(__file__).resolve().parent.parent
OWNER = "menno420"

# Sections expected regardless of manifest rows (README § Sections: `ideas/fleet/` is
# the cross-cutting section, not a lane row).
ALWAYS_EXPECTED = {"fleet"}

# Manifest rows that are fleet infrastructure, not build lanes — they get no section.
# The manager (repo fleet-manager) is the control chair; cross-cutting ideas aimed at
# it live in `ideas/fleet/`. Keep this list short and loud.
NON_LANE_REPOS = {"fleet-manager"}

# Textual markers of a non-active row (hand-maintained living ledger — heuristics are
# unavoidable; parse failures must fail LOUD, never report a false clean).
CLOSED_MARKERS = ("project closed",)

# The manifest's own retirement tombstone (superbot 34ebbac1, 2026-07-11T02:34Z:
# "retire fleet-manifest to pointer stub" — Status flipped to historical, all table
# rows removed, canonical fleet state moved to the fleet-manager GENERATED roster,
# menno420/fleet-manager docs/roster.md). Detected EXPLICITLY so the supersede is a
# loud advisory, not a red: with zero rows upstream there is nothing to diff, and a
# hard exit 2 here reds every non-control CI run fleet-decision-wide (found live
# mid-flight of the squash-headref-provenance slice, ~10 min after the tombstone
# landed). Re-pointing the section derivation at the roster is a REAL grooming slice
# (lane→section mapping + new-section duties), deliberately not folded in here —
# genuine parse failures (rows present but unparseable) still exit 2.
SUPERSEDED_MARKER = "superseded"


def read_manifest(path: str | None) -> str:
    if path:
        return Path(path).read_text(encoding="utf-8")
    with urllib.request.urlopen(MANIFEST_URL, timeout=30) as resp:
        return resp.read().decode("utf-8")


def active_sections(manifest: str) -> set[str]:
    """Sections implied by the manifest's active lane rows: first `menno420/<repo>` in
    the Repo(s) cell of every table row that is not closed and has a real repo."""
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
    ap.add_argument("--manifest", help="path to a local manifest copy (offline run)")
    ap.add_argument(
        "--ideas-dir", default=str(REPO_ROOT / "ideas"), help="ideas tree to check"
    )
    args = ap.parse_args()

    try:
        manifest = read_manifest(args.manifest)
    except Exception as exc:  # fail loud: a false clean is worse than a crash
        print(f"check_sections: cannot read/parse manifest: {exc}", file=sys.stderr)
        return 2
    try:
        expected = active_sections(manifest) | ALWAYS_EXPECTED
    except Exception as exc:  # fail loud — EXCEPT the explicit retirement tombstone
        if SUPERSEDED_MARKER in manifest.lower():
            print(
                "check_sections: SUPERSEDED (advisory) — the fleet manifest is a "
                "retirement tombstone (zero lane rows; canonical fleet state moved "
                "to the fleet-manager GENERATED roster, menno420/fleet-manager "
                "docs/roster.md). Section-vs-lane sync is UNCHECKABLE until the "
                "section derivation is re-pointed at the roster (queued follow-up "
                "slice) — passing LOUDLY, never silently."
            )
            return 0
        print(f"check_sections: cannot read/parse manifest: {exc}", file=sys.stderr)
        return 2

    ideas_dir = Path(args.ideas_dir)
    if not ideas_dir.is_dir():
        print(f"check_sections: no ideas dir at {ideas_dir}", file=sys.stderr)
        return 2
    actual = actual_sections(ideas_dir)

    missing = sorted(expected - actual)
    orphans = sorted(actual - expected)
    for s in missing:
        print(f"MISSING section: ideas/{s}/ (active lane in manifest, no directory)")
    for s in orphans:
        print(f"ORPHAN section:  ideas/{s}/ (no active lane row in manifest)")
    if missing or orphans:
        print(f"check_sections: DRIFT — {len(missing)} missing, {len(orphans)} orphan")
        return 1
    print(f"check_sections: OK — {len(actual)} sections in sync with the manifest")
    return 0


if __name__ == "__main__":
    sys.exit(main())
