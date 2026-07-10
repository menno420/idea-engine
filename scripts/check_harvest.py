#!/usr/bin/env python3
"""check_harvest.py — link-index harvest freshness checker (stdlib only).

Compares each harvested link-index section against its CANONICAL repo, live, and
reports drift three ways:

- HEAD MOVED   — the canonical branch HEAD no longer equals the section's harvest pin
                 (the snapshot is stale; everything below quantifies by how much).
- NEW doc      — a canonical doc exists upstream that no index entry names (pending
                 re-harvest; the COUNT sizes the next harvest slice).
- DELETED doc  — an index entry names a canonical doc that no longer exists upstream
                 (a dead link in the trail).

Convention source: README.md § Idea file grammar — harvested lane-born ideas are
indexed BY LINK, pinned at a harvest sha (e.g. `ideas/superbot/README.md`, 233 docs
@ superbot `fd638e3`); a pin is a checkable claim, not decoration. The canonical repo
is read-only to this repo (public raw/API path, Q-0260). Origin: PR #7 session card
💡, dispatched via the PR #21 card; probed in
`ideas/fleet/harvest-freshness-checker-2026-07-10.md`.

NETWORK-DEPENDENT — WAKE-TIME USE ONLY. Do NOT add this to `scripts/preflight.py`
or any CI workflow: CI stays hermetic, and a GitHub blip must never red a PR. The
live comparison IS the point, so there is no offline mode — a failed fetch is
exit 2 (could-not-run), never a false clean.

Report-only: it never edits files. Drift is INFORMATION, not failure — the check
exits 0 whenever it RAN, drift or no drift.

Usage:
    python3 scripts/check_harvest.py

Exit codes: 0 = ran and reported (drift or clean) · 2 = could not run (network
failure, missing/unparseable index, zero parsed entries).
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
import tempfile
import urllib.error
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Harvested link-index sections — ONE row here per harvested lane (a second lane's
# harvest is a one-line addition): (section README, canonical repo, canonical dir,
# canonical branch).
SECTIONS: list[tuple[str, str, str, str]] = [
    ("ideas/superbot/README.md", "menno420/superbot", "docs/ideas", "main"),
    ("ideas/websites/README.md", "menno420/websites", "docs/ideas", "main"),
]

# Index grammar constants (must match the harvested README's format — a reformat
# parses to ZERO and fails loud, never a false clean).
PIN_RE = re.compile(r"pinned @ .*?\(`([0-9a-f]{40})`\)")
API_TIMEOUT = 30


def canonical_entry_re(canonical_dir: str) -> re.Pattern[str]:
    """Matches `canonical: <repo-shortname> \\`<canonical_dir>/<file>.md\\`` entries."""
    return re.compile(rf"canonical: \S+ `{re.escape(canonical_dir)}/([^`/]+\.md)`")


def ls_remote_head(repo: str, branch: str) -> str:
    """Live canonical HEAD sha via git ls-remote (honors HTTPS_PROXY)."""
    out = subprocess.run(
        ["git", "ls-remote", f"https://github.com/{repo}.git", f"refs/heads/{branch}"],
        capture_output=True, text=True, timeout=60, check=True,
    ).stdout
    sha = out.split()[0] if out.split() else ""
    if not re.fullmatch(r"[0-9a-f]{40}", sha):
        raise ValueError(f"ls-remote returned no sha for {repo}@{branch}: {out!r}")
    return sha


def _md_names(names: list[str]) -> set[str]:
    return {n for n in names if n.endswith(".md") and n != "README.md"}
    # README.md = the canonical index itself, never harvested as a doc


def live_docs(repo: str, canonical_dir: str, branch: str) -> set[str]:
    """Current *.md filenames in the canonical dir at HEAD. Primary: ONE
    unauthenticated GitHub contents-API request (urllib honors HTTPS_PROXY from the
    environment). Fallback on an API 403/404 wall (e.g. an egress proxy that gates
    api.github.com per-repo while git egress stays open): a blobless no-checkout
    shallow clone + `git ls-tree` — exact, ~1s, trees only, no blobs (the blobless
    fetch tactic already on the heartbeat's operational-recipes list)."""
    url = f"https://api.github.com/repos/{repo}/contents/{canonical_dir}?ref={branch}"
    req = urllib.request.Request(url, headers={"User-Agent": "idea-engine-check-harvest"})
    try:
        with urllib.request.urlopen(req, timeout=API_TIMEOUT) as resp:
            listing = json.load(resp)
        if not isinstance(listing, list):
            raise ValueError(f"contents API did not return a directory listing for {url}")
        return _md_names([e["name"] for e in listing if e.get("type") == "file"])
    except urllib.error.HTTPError as exc:
        if exc.code not in (403, 404):
            raise
        print(f"  (contents API {exc.code} — falling back to blobless ls-tree)")
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(
            ["git", "clone", "--quiet", "--depth", "1", "--filter=blob:none",
             "--no-checkout", "--branch", branch, f"https://github.com/{repo}.git", tmp],
            capture_output=True, text=True, timeout=120, check=True,
        )
        out = subprocess.run(
            ["git", "-C", tmp, "ls-tree", "--name-only", "HEAD", "--", f"{canonical_dir}/"],
            capture_output=True, text=True, timeout=60, check=True,
        ).stdout
    return _md_names([line.rsplit("/", 1)[-1] for line in out.splitlines() if line.strip()])


def check_section(readme_rel: str, repo: str, canonical_dir: str, branch: str) -> int:
    """Returns a drift count for one harvested section. Raises on could-not-run."""
    readme = REPO_ROOT / readme_rel
    text = readme.read_text(encoding="utf-8")  # missing file raises -> exit 2

    pin_m = PIN_RE.search(text)
    if not pin_m:
        raise ValueError(f"{readme_rel}: no harvest pin line (`pinned @ … (<full-sha>)`)")
    pin = pin_m.group(1)

    indexed = set(canonical_entry_re(canonical_dir).findall(text))
    if not indexed:
        raise ValueError(
            f"{readme_rel}: zero canonical entries parsed — index format changed? "
            "(update the grammar constants; do not trust this run)"
        )

    head = ls_remote_head(repo, branch)
    live = live_docs(repo, canonical_dir, branch)

    print(f"section {readme_rel} ← {repo}/{canonical_dir} @ {branch}")
    if head == pin:
        print(f"  HEAD UNMOVED: {repo}@{branch} = harvest pin {pin[:7]}")
    else:
        print(f"  HEAD MOVED:   {repo}@{branch} is {head[:7]} ({head}), harvest pin is {pin[:7]}")

    # A live doc absent from the machine index but present as a same-named local
    # file is an ENTRY-FORMAT gap (an entry predating the harvest grammar), not a
    # new upstream doc — classify it honestly so NEW stays a true re-harvest count.
    section_dir = readme.parent
    candidates = sorted(live - indexed)
    new = [n for n in candidates if not (section_dir / n).is_file()]
    unmarked = [n for n in candidates if (section_dir / n).is_file()]
    deleted = sorted(indexed - live)
    for name in new:
        print(f"  NEW upstream doc (not indexed): {canonical_dir}/{name}")
    for name in unmarked:
        print(f"  UNMARKED entry (local file exists, no machine-readable canonical marker): {canonical_dir}/{name}")
    for name in deleted:
        print(f"  DELETED upstream (still indexed): {canonical_dir}/{name}")
    print(
        f"  summary: {len(indexed)} indexed · {len(live)} live upstream · "
        f"{len(new)} new · {len(unmarked)} unmarked · {len(deleted)} deleted · "
        f"HEAD {'moved' if head != pin else 'unmoved'}"
    )
    return len(new) + len(unmarked) + len(deleted) + (0 if head == pin else 1)


def main() -> int:
    drift = 0
    for readme_rel, repo, canonical_dir, branch in SECTIONS:
        try:
            drift += check_section(readme_rel, repo, canonical_dir, branch)
        except Exception as exc:  # fail loud: a false clean is worse than a crash
            print(f"check_harvest: could not run for {readme_rel}: {exc}", file=sys.stderr)
            return 2
    if drift:
        print(f"check_harvest: DRIFT — {drift} finding(s) across {len(SECTIONS)} section(s) (report-only; sizes the next re-harvest slice)")
    else:
        print(f"check_harvest: OK — {len(SECTIONS)} harvested section(s) fresh at canonical HEAD")
    return 0


if __name__ == "__main__":
    sys.exit(main())
