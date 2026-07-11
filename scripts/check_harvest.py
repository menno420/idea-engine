#!/usr/bin/env python3
"""check_harvest.py — link-index harvest freshness checker (stdlib only).

Compares each harvested link-index section against its CANONICAL repo, live, and
reports drift these ways:

- HEAD MOVED   — the canonical branch HEAD no longer equals the section's harvest pin
                 (the snapshot is stale; everything below quantifies by how much).
                 When the doc set is byte-list-identical (0 new/unmarked/deleted) it
                 reports as `HEAD MOVED (docs unchanged)` — pin-bump-only drift that
                 sizes NO harvest work and never turns the exit line to DRIFT (the
                 PR #38 card 💡: the hub commits far faster than its docs/ideas tree
                 changes, so pin-vs-HEAD inequality alone overstates the queue).
- NEW doc      — a canonical doc exists upstream that no index entry names (pending
                 re-harvest; the COUNT sizes the next harvest slice).
- DELETED doc  — an index entry names a canonical doc that no longer exists upstream
                 (a dead link in the trail).
- RE-BADGE     — `--re-badge` only: an indexed entry whose LOCAL state is not
                 `historical(…)` while the canonical doc's own front-matter records a
                 built outcome (`state:`/`status:` built/shipped/done, or a
                 `shipped_pr:`) — the outcome-mirroring staleness NEW/DELETED can't
                 see (the PR #37 card 💡). Suggestion pass, report-only: it names the
                 candidates, the harvester judges the re-badge. OFF by default —
                 it reads canonical doc BLOBS (one batched blobless-clone checkout
                 per section), the depth the PR #22 card flagged as non-trivial.

Convention source: README.md § Idea file grammar — harvested lane-born ideas are
indexed BY LINK, pinned at a harvest sha (e.g. `ideas/superbot/README.md`, 233 docs
@ superbot `fd638e3`); a pin is a checkable claim, not decoration. The canonical repo
is read-only to this repo (public raw/API path, Q-0260). Origin: PR #7 session card
💡, dispatched via the PR #21 card; probed in
`ideas/fleet/harvest-freshness-checker-2026-07-10.md` (output refinements: the
PR #26/#37/#38 card 💡s — see that file's extension note).

NETWORK-DEPENDENT — WAKE-TIME USE ONLY. Do NOT add this to `scripts/preflight.py`
or any CI workflow: CI stays hermetic, and a GitHub blip must never red a PR. The
live comparison IS the point, so there is no offline mode — a failed fetch is
exit 2 (could-not-run), never a false clean.

Report-only: it never edits files. Drift is INFORMATION, not failure — the check
exits 0 whenever it RAN, drift or no drift.

Usage:
    python3 scripts/check_harvest.py [--emit-entries] [--re-badge]

--emit-entries (the PR #26 card 💡): for each NEW upstream doc, also print a
ready-to-fill link-index entry stub — pinned blob+raw links @ the live HEAD, a
blessed-byte-form Grounding line, an empty gist slot, and the section-README index
row — so a re-harvest slice reduces to "read the doc, write the gists"; the
mechanical link/pin assembly (the part that drifts under a cheaper model: wrong sha,
missed raw link) comes pre-filled. Stubs go to stdout, never to files; `[[fill:…]]`
slots mark what the harvester must write from a full raw read at the pin.

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
from datetime import datetime, timezone
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

# Local link-index entry state line (README § Idea file grammar) — read by the
# --re-badge pass only; `\S+` keeps `historical(menno420/websites#41)` whole.
STATE_RE = re.compile(r"^>\s*\*\*State:\*\*\s*(\S+)", re.MULTILINE)

# Canonical-doc built-outcome markers (front-matter / header lines) — the
# outcome-mirroring signals PR #37's harvest actually cross-read by hand.
CANON_STATE_RE = re.compile(r"^(?:state|status):\s*(\S+)", re.IGNORECASE)
CANON_SHIPPED_RE = re.compile(r"^shipped_pr:\s*(\S+)", re.IGNORECASE)
BUILT_STATES = {"built", "shipped", "done", "historical"}
CANON_HEAD_LINES = 40  # markers live in front-matter / the first header lines


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


def canonical_doc_texts(repo: str, canonical_dir: str, branch: str,
                        names: set[str]) -> dict[str, str]:
    """`--re-badge` only — canonical doc contents at HEAD, via ONE blobless clone
    whose `git checkout -- <dir>` lazy-fetches just that dir's blobs in one batched
    promisor fetch (never one round-trip per doc)."""
    texts: dict[str, str] = {}
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(
            ["git", "clone", "--quiet", "--depth", "1", "--filter=blob:none",
             "--no-checkout", "--branch", branch, f"https://github.com/{repo}.git", tmp],
            capture_output=True, text=True, timeout=120, check=True,
        )
        subprocess.run(
            ["git", "-C", tmp, "checkout", "--quiet", "HEAD", "--", f"{canonical_dir}/"],
            capture_output=True, text=True, timeout=300, check=True,
        )
        for name in sorted(names):
            doc = Path(tmp) / canonical_dir / name
            if doc.is_file():
                texts[name] = doc.read_text(encoding="utf-8", errors="replace")
    return texts


def canonical_built_marker(text: str) -> str | None:
    """A built-outcome marker from a canonical doc's front-matter/header lines,
    or None. Returns the matched marker verbatim for honest reporting."""
    for line in text.splitlines()[:CANON_HEAD_LINES]:
        m = CANON_SHIPPED_RE.match(line)
        if m and m.group(1) not in ("", "~", "null", "none"):
            return line.strip()
        m = CANON_STATE_RE.match(line)
        if m and m.group(1).lower().rstrip(".,;") in BUILT_STATES:
            return line.strip()
    return None


def re_badge_candidates(section_dir: Path, repo: str, canonical_dir: str,
                        branch: str, indexed: set[str]) -> list[tuple[str, str, str]]:
    """`(name, local_state, canonical_marker)` per indexed entry whose local state
    is not historical(...) while the canonical doc records a built outcome."""
    texts = canonical_doc_texts(repo, canonical_dir, branch, indexed)
    out: list[tuple[str, str, str]] = []
    for name in sorted(indexed):
        entry = section_dir / name
        if not entry.is_file() or name not in texts:
            continue  # NEW/DELETED classes already report the existence gaps
        state_m = STATE_RE.search(entry.read_text(encoding="utf-8"))
        if not state_m or state_m.group(1).startswith("historical"):
            continue
        marker = canonical_built_marker(texts[name])
        if marker:
            out.append((name, state_m.group(1), marker))
    return out


def emit_entry_stub(section_dir: str, repo: str, canonical_dir: str,
                    name: str, head: str) -> None:
    """Ready-to-fill link-index entry stub for one NEW upstream doc (PR #26 card 💡):
    the mechanical link/pin assembly pre-filled from the live HEAD, `[[fill:…]]`
    slots for everything that needs the harvester's full raw read at the pin."""
    lane = repo.split("/", 1)[1]
    raw = f"https://raw.githubusercontent.com/{repo}/{head}/{canonical_dir}/{name}"
    blob = f"https://github.com/{repo}/blob/{head}/{canonical_dir}/{name}"
    fetched = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    print(f"""
--- emit-entries stub → {section_dir}/{name} ---
(fill every [[fill:…]] slot from a FULL raw read at the pin; verify the state
mirrors any recorded canonical outcome — built → historical(…) — and re-stamp
`fetched` at your own read; this stub's stamp is the checker's listing fetch)

# [[fill:title]] — link index

> **State:** captured
> **Class:** [[fill:product|process|venture]] · **Target:** `{repo}`
> **Grounding:** {raw}@{head[:7]} · fetched {fetched}

**Canonical idea (stays in {lane} — indexed by link, never copied):**
[`{repo} → {canonical_dir}/{name}`]({blob})
— harvested [[fill:date]] by [[fill:slice]], pinned @ {lane} `{head[:7]}`
([raw]({raw})).

[[fill:gist — in the harvester's own words, from the full raw read at the pin]]

--- index row → {section_dir}/README.md ---
- [`{name}`]({name}) — captured · [[fill:one-line gist]] (canonical: {lane} `{canonical_dir}/{name}` @ `{head[:7]}`)
--- end stub ---""")


def check_section(readme_rel: str, repo: str, canonical_dir: str, branch: str,
                  emit_entries: bool = False, re_badge: bool = False) -> tuple[int, bool]:
    """Returns `(work, moved_only)` for one harvested section: `work` counts the
    findings that size actual harvest work; `moved_only` flags a pin-bump-only HEAD
    move (docs unchanged — reported, never counted as work). Raises on could-not-run."""
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

    # A live doc absent from the machine index but present as a same-named local
    # file is an ENTRY-FORMAT gap (an entry predating the harvest grammar), not a
    # new upstream doc — classify it honestly so NEW stays a true re-harvest count.
    section_dir = readme.parent
    candidates = sorted(live - indexed)
    new = [n for n in candidates if not (section_dir / n).is_file()]
    unmarked = [n for n in candidates if (section_dir / n).is_file()]
    deleted = sorted(indexed - live)
    doc_work = len(new) + len(unmarked) + len(deleted)
    moved_only = head != pin and doc_work == 0

    print(f"section {readme_rel} ← {repo}/{canonical_dir} @ {branch}")
    if head == pin:
        print(f"  HEAD UNMOVED: {repo}@{branch} = harvest pin {pin[:7]}")
    elif moved_only:
        print(f"  HEAD MOVED (docs unchanged): {repo}@{branch} is {head[:7]} ({head}), "
              f"harvest pin is {pin[:7]} — pin-bump-only, sizes no harvest work")
    else:
        print(f"  HEAD MOVED:   {repo}@{branch} is {head[:7]} ({head}), harvest pin is {pin[:7]}")
    for name in new:
        print(f"  NEW upstream doc (not indexed): {canonical_dir}/{name}")
    for name in unmarked:
        print(f"  UNMARKED entry (local file exists, no machine-readable canonical marker): {canonical_dir}/{name}")
    for name in deleted:
        print(f"  DELETED upstream (still indexed): {canonical_dir}/{name}")

    badges: list[tuple[str, str, str]] = []
    if re_badge:
        badges = re_badge_candidates(section_dir, repo, canonical_dir, branch, indexed)
        for name, local_state, marker in badges:
            print(f"  RE-BADGE candidate: {canonical_dir}/{name} — index entry says "
                  f"'{local_state}', canonical records `{marker}` (suggestion only — "
                  "verify, then mirror as historical(…))")

    head_state = ("unmoved" if head == pin
                  else "moved (docs unchanged)" if moved_only else "moved")
    print(
        f"  summary: {len(indexed)} indexed · {len(live)} live upstream · "
        f"{len(new)} new · {len(unmarked)} unmarked · {len(deleted)} deleted"
        + (f" · {len(badges)} re-badge" if re_badge else "")
        + f" · HEAD {head_state}"
    )

    if emit_entries:
        for name in new:
            emit_entry_stub(str(section_dir.relative_to(REPO_ROOT)), repo,
                            canonical_dir, name, head)

    work = doc_work + len(badges) + (1 if head != pin and not moved_only else 0)
    return work, moved_only


def main() -> int:
    argv = sys.argv[1:]
    unknown = [a for a in argv if a not in ("--emit-entries", "--re-badge")]
    if unknown:
        print(f"check_harvest: unknown argument(s): {' '.join(unknown)} "
              "(usage: check_harvest.py [--emit-entries] [--re-badge])", file=sys.stderr)
        return 2
    emit_entries = "--emit-entries" in argv
    re_badge = "--re-badge" in argv

    work = 0
    moved_only_sections = 0
    for readme_rel, repo, canonical_dir, branch in SECTIONS:
        try:
            section_work, moved_only = check_section(
                readme_rel, repo, canonical_dir, branch, emit_entries, re_badge)
        except Exception as exc:  # fail loud: a false clean is worse than a crash
            print(f"check_harvest: could not run for {readme_rel}: {exc}", file=sys.stderr)
            return 2
        work += section_work
        moved_only_sections += 1 if moved_only else 0

    pin_note = (f"; {moved_only_sections} section(s) HEAD-moved-only (pin-bump, no work)"
                if moved_only_sections else "")
    if work:
        print(f"check_harvest: DRIFT — {work} finding(s) across {len(SECTIONS)} section(s) "
              f"(report-only; sizes the next re-harvest slice){pin_note}")
    elif moved_only_sections:
        print(f"check_harvest: OK — no harvest work across {len(SECTIONS)} harvested "
              f"section(s){pin_note}")
    else:
        print(f"check_harvest: OK — {len(SECTIONS)} harvested section(s) fresh at canonical HEAD")
    return 0


if __name__ == "__main__":
    sys.exit(main())
