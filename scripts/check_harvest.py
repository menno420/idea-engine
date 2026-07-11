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
- CHANGED doc  — same filename upstream, different CONTENT (blob sha) than the
                 section's recorded pin — the drift class the filename-set diff is
                 blind to (the PR #49 lived case: the websites backlog moved 47/31
                 lines while the checker said `docs unchanged`; the PR #52 re-pin
                 rider had to be hand-sized). Needs a pin record (`--write-pins`,
                 below) or `--bullet-drift`; without either, content drift stays
                 invisible and the checker SAYS SO instead of implying freshness.
- STATE-DRIFT  — `--states` only (the PR #22 card 💡's full per-doc state-drift
                 depth): for EVERY indexed entry, the canonical doc's own state
                 marker at HEAD (`state:`/`status:`/`shipped_pr:` front-matter)
                 is diffed against the local entry's recorded `> **State:**` at
                 lifecycle-stage granularity (built ↔ historical(…) ·
                 retired ↔ rejected(…) · open ↔ everything else), and BOTH drift
                 directions report — a `captured` entry whose canonical doc
                 advanced to built (the PR #22 test case), AND a `historical(…)`
                 entry whose canonical doc walked back or retired (the reverse
                 direction `--re-badge` cannot see). Suggestion pass,
                 report-only: it names the pairs, the harvester judges the fix.
                 An index bullet carrying the blessed
                 `(state-drift: deliberate — <reason/PR>)` annotation (README §
                 Idea file grammar, the PR #149 card 💡) reports as ACK'd —
                 named, never counted as harvest work — so a ruled-on
                 divergence stops re-sizing every future wake.
                 OFF by default — it reads canonical doc BLOBS (one batched
                 blobless-clone checkout per section), the same depth flag-gating
                 rationale as `--re-badge`; the default run's network legs stay
                 exactly as before.
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

Report-only: the CHECK never edits files. Drift is INFORMATION, not failure — the
check exits 0 whenever it RAN, drift or no drift. The ONE deliberate exception is
`--write-pins` (a separate mode, never combined with checking): it records the pin.

Content identity — the pin record (`.harvest-pin.json`):

The section README's pin line names a COMMIT; per-doc content identity needs per-doc
BLOB shas at that commit. `--write-pins`, run by the harvester in the same session
that (re-)pins the README, records `ideas/<section>/.harvest-pin.json` — the live
per-doc blob-sha map (the same listing data the checker already fetches: the
contents-API `sha` field, or `git ls-tree`) plus the head it was recorded at. It
REFUSES to write unless the README pin equals the live HEAD (a record taken away
from the pin would be a lie). At check time the recorded shas are compared against
the live listing at ZERO extra network cost, and same-name/different-sha docs report
as CHANGED — distinct from NEW and DELETED. Backward compatible: a section without
a pin record (every pin older than this leg) degrades to the old filename-set
behavior WITH A NOTE naming the blindness; it never crashes.

`--bullet-drift` — content-delta sizing (pin → HEAD), for re-pin riders:

For each HEAD-moved section, one blobless clone fetches the pin commit and runs
`git diff --numstat/--name-status <pin> HEAD -- <canonical_dir>/` — exact per-doc
+N/-M line deltas since the pin, with only the changed blobs lazy-fetched. This is
how a section-level backlog file's drift (e.g. the websites lane-backlog) gets
SIZED — "this backlog file moved +47/-31 lines since the pin" — so a re-pin rider
is sized by data, not by hand-diffing (the PR #52 rider cost). Works even without
a pin record (it derives pin-time truth from git itself), and its M-rows feed the
CHANGED class. Flag-gated OFF by default: it adds a clone+fetch network leg per
moved section, and the default run's network legs stay exactly as before.

Usage:
    python3 scripts/check_harvest.py [--emit-entries] [--re-badge] [--bullet-drift]
                                     [--states]
    python3 scripts/check_harvest.py --write-pins

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

# Per-section pin record — per-doc blob shas at the harvest pin (written by
# `--write-pins` in the same session that pins the README; read at check time).
PIN_RECORD_NAME = ".harvest-pin.json"
PIN_RECORD_FORMAT = "harvest-pin/v1"

# Local link-index entry state line (README § Idea file grammar) — read by the
# --re-badge pass only; `\S+` keeps `historical(menno420/websites#41)` whole.
STATE_RE = re.compile(r"^>\s*\*\*State:\*\*\s*(\S+)", re.MULTILINE)

# Canonical-doc built-outcome markers (front-matter / header lines) — the
# outcome-mirroring signals PR #37's harvest actually cross-read by hand.
CANON_STATE_RE = re.compile(r"^(?:state|status):\s*(\S+)", re.IGNORECASE)
CANON_SHIPPED_RE = re.compile(r"^shipped_pr:\s*(\S+)", re.IGNORECASE)
BUILT_STATES = {"built", "shipped", "done", "historical"}
CANON_HEAD_LINES = 40  # markers live in front-matter / the first header lines

# `--states` lifecycle-stage vocabulary (the PR #22 card 💡's full depth): the
# canonical repos' marker vocabulary and this repo's state grammar differ, so
# the diff runs at STAGE granularity — built / retired / open — never on raw
# tokens (a raw compare of `built` vs `historical(#41)` would false-drift on
# every correctly mirrored entry). Same loud co-edit rule as every grammar
# constant here.
CANON_RETIRED_STATES = {"retired", "rejected", "dropped", "superseded", "wontfix"}
LOCAL_BUILT_PREFIX = "historical("
LOCAL_RETIRED_PREFIX = "rejected("

# `--states` ACK annotation (README § Idea file grammar, PR #149 card 💡): an
# index bullet may mark a divergence as ruled-on-deliberate; the reason must
# not contain `)` (the regex stops at the first close-paren).
STATE_DRIFT_ACK_RE = re.compile(r"\(state-drift:\s*deliberate\s*—\s*([^)]+)\)")


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


def _md_only(entries: dict[str, str]) -> dict[str, str]:
    return {n: sha for n, sha in entries.items()
            if n.endswith(".md") and n != "README.md"}
    # README.md = the canonical index itself, never harvested as a doc


def live_docs(repo: str, canonical_dir: str, branch: str) -> dict[str, str]:
    """Current `*.md` filename → BLOB SHA map for the canonical dir at HEAD (both
    sources already carry the blob sha — the contents-API `sha` field / the
    ls-tree object column — so content identity costs zero extra network).
    Primary: ONE unauthenticated GitHub contents-API request (urllib honors
    HTTPS_PROXY from the environment). Fallback on an API 403/404 wall (e.g. an
    egress proxy that gates api.github.com per-repo while git egress stays open):
    a blobless no-checkout shallow clone + `git ls-tree` — exact, ~1s, trees only,
    no blobs (the blobless fetch tactic already on the heartbeat's
    operational-recipes list)."""
    url = f"https://api.github.com/repos/{repo}/contents/{canonical_dir}?ref={branch}"
    req = urllib.request.Request(url, headers={"User-Agent": "idea-engine-check-harvest"})
    try:
        with urllib.request.urlopen(req, timeout=API_TIMEOUT) as resp:
            listing = json.load(resp)
        if not isinstance(listing, list):
            raise ValueError(f"contents API did not return a directory listing for {url}")
        return _md_only({e["name"]: e["sha"] for e in listing if e.get("type") == "file"})
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
            ["git", "-C", tmp, "ls-tree", "HEAD", "--", f"{canonical_dir}/"],
            capture_output=True, text=True, timeout=60, check=True,
        ).stdout
    entries: dict[str, str] = {}
    for line in out.splitlines():  # `<mode> <type> <sha>\t<path>`
        meta, _, path = line.partition("\t")
        parts = meta.split()
        if len(parts) == 3 and parts[1] == "blob" and path:
            entries[path.rsplit("/", 1)[-1]] = parts[2]
    return _md_only(entries)


def load_pin_record(section_dir: Path, repo: str, canonical_dir: str,
                    pin: str) -> dict[str, str] | None:
    """The section's recorded per-doc blob-sha map at the README pin, or None with
    a printed note (backward compatibility: a missing/old/stale record NEVER
    crashes the check — it degrades to the filename-set behavior and says so)."""
    record_path = section_dir / PIN_RECORD_NAME
    if not record_path.is_file():
        print(f"  (no pin record {PIN_RECORD_NAME} — content identity untracked for this "
              "section: NEW/DELETED below are filename-set-only and same-name content "
              "drift is INVISIBLE; record one with --write-pins at the next re-pin, or "
              "run --bullet-drift for a git-derived content delta)")
        return None
    try:
        record = json.loads(record_path.read_text(encoding="utf-8"))
        docs = record["docs"]
        if not isinstance(docs, dict):
            raise ValueError("docs is not a map")
    except Exception as exc:
        print(f"  (pin record {PIN_RECORD_NAME} unparseable ({exc}) — degrading to "
              "filename-set behavior; re-record with --write-pins at the next re-pin)")
        return None
    if record.get("pin") != pin:
        print(f"  (pin record {PIN_RECORD_NAME} is for pin "
              f"{str(record.get('pin', '?'))[:7]}, README pin is {pin[:7]} — STALE "
              "record ignored; degrading to filename-set behavior. --write-pins must "
              "run in the same session that re-pins the README)")
        return None
    if (record.get("repo"), record.get("canonical_dir")) != (repo, canonical_dir):
        print(f"  (pin record {PIN_RECORD_NAME} names a different canonical source — "
              "ignored; re-record with --write-pins)")
        return None
    return {n: str(sha) for n, sha in docs.items()}


def pin_tree_delta(repo: str, branch: str, pin: str,
                   canonical_dir: str) -> dict[str, tuple[str, str]]:
    """`--bullet-drift` only — exact per-doc content delta pin → HEAD, as
    `name → (status, "+N/-M")`, via ONE blobless clone that fetches the pin commit
    (GitHub serves reachable shas to fetch) and diffs the two trees; only the
    changed blobs are lazy-fetched by the promisor. Raises on could-not-run —
    a silent "no drift" would be a false clean."""
    with tempfile.TemporaryDirectory() as tmp:
        subprocess.run(
            ["git", "clone", "--quiet", "--depth", "1", "--filter=blob:none",
             "--no-checkout", "--branch", branch, f"https://github.com/{repo}.git", tmp],
            capture_output=True, text=True, timeout=120, check=True,
        )
        subprocess.run(
            ["git", "-C", tmp, "fetch", "--quiet", "--depth", "1",
             "--filter=blob:none", "origin", pin],
            capture_output=True, text=True, timeout=120, check=True,
        )
        def diff(mode: str) -> str:
            return subprocess.run(
                ["git", "-C", tmp, "diff", "--no-renames", mode, pin, "HEAD",
                 "--", f"{canonical_dir}/"],
                capture_output=True, text=True, timeout=120, check=True,
            ).stdout
        status_out = diff("--name-status")
        numstat_out = diff("--numstat")
    statuses: dict[str, str] = {}
    for line in status_out.splitlines():
        st, _, path = line.partition("\t")
        name = path.rsplit("/", 1)[-1]
        if name.endswith(".md") and name != "README.md":
            statuses[name] = st.strip()[:1]  # A / M / D
    deltas: dict[str, tuple[str, str]] = {}
    for line in numstat_out.splitlines():
        parts = line.split("\t")
        if len(parts) != 3:
            continue
        added, deleted, path = parts
        name = path.rsplit("/", 1)[-1]
        if not name.endswith(".md") or name == "README.md":
            continue
        size = "binary" if added == "-" else f"+{added}/-{deleted} lines"
        deltas[name] = (statuses.get(name, "M"), size)
    return deltas


def write_pin_record(section_dir: Path, repo: str, canonical_dir: str, branch: str,
                     pin: str, head: str, live: dict[str, str]) -> None:
    """`--write-pins` only — the ONE writing mode. Records the live per-doc
    blob-sha map as the section's pin record. The caller has already verified
    README pin == live HEAD (a record taken away from the pin would be a lie)."""
    record = {
        "format": PIN_RECORD_FORMAT,
        "repo": repo,
        "canonical_dir": canonical_dir,
        "branch": branch,
        "pin": pin,
        "recorded": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "docs": {n: live[n] for n in sorted(live)},
    }
    path = section_dir / PIN_RECORD_NAME
    path.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    print(f"  recorded {len(live)} doc blob sha(s) @ pin {pin[:7]} → "
          f"{path.relative_to(REPO_ROOT)}")


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


def canonical_stage(text: str) -> tuple[str, str]:
    """`--states` only — (lifecycle stage, marker-or-note) from a canonical doc's
    front-matter/header lines: 'built' / 'retired' / 'open'. The marker is
    returned verbatim for honest reporting; a doc with no marker at all is
    ('open', '<no state marker>') — unmarked upstream docs are the common case,
    never a drift by themselves."""
    for line in text.splitlines()[:CANON_HEAD_LINES]:
        m = CANON_SHIPPED_RE.match(line)
        if m and m.group(1) not in ("", "~", "null", "none"):
            return "built", line.strip()
        m = CANON_STATE_RE.match(line)
        if m:
            token = m.group(1).lower().rstrip(".,;")
            if token in BUILT_STATES:
                return "built", line.strip()
            if token in CANON_RETIRED_STATES:
                return "retired", line.strip()
            return "open", line.strip()
    return "open", "<no state marker>"


def local_stage(state: str) -> str:
    """Local `> **State:**` value → lifecycle stage ('built'/'retired'/'open')."""
    if state.startswith(LOCAL_BUILT_PREFIX):
        return "built"
    if state.startswith(LOCAL_RETIRED_PREFIX):
        return "retired"
    return "open"


def state_drift_pairs(section_dir: Path, repo: str, canonical_dir: str,
                      branch: str, indexed: set[str]) -> list[tuple[str, str, str]]:
    """`--states` only — `(name, local_state, canonical_marker)` per indexed entry
    whose local state and canonical state marker disagree at lifecycle-stage
    granularity, in EITHER direction (the full PR #22 depth; `--re-badge` only
    sees the local-open ↔ canonical-built quadrant)."""
    texts = canonical_doc_texts(repo, canonical_dir, branch, indexed)
    out: list[tuple[str, str, str]] = []
    for name in sorted(indexed):
        entry = section_dir / name
        if not entry.is_file() or name not in texts:
            continue  # NEW/DELETED classes already report the existence gaps
        state_m = STATE_RE.search(entry.read_text(encoding="utf-8"))
        if not state_m:
            continue  # a state-less local entry is check_ideas' problem
        local = state_m.group(1)
        canon_stage, marker = canonical_stage(texts[name])
        if canon_stage == "open" and marker == "<no state marker>":
            continue  # unmarked upstream doc — nothing recorded to diff against
        if local_stage(local) != canon_stage:
            out.append((name, local, marker))
    return out


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
                  emit_entries: bool = False, re_badge: bool = False,
                  bullet_drift: bool = False, states: bool = False) -> tuple[int, bool]:
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
    live_names = set(live)

    # A live doc absent from the machine index but present as a same-named local
    # file is an ENTRY-FORMAT gap (an entry predating the harvest grammar), not a
    # new upstream doc — classify it honestly so NEW stays a true re-harvest count.
    section_dir = readme.parent
    candidates = sorted(live_names - indexed)
    new = [n for n in candidates if not (section_dir / n).is_file()]
    unmarked = [n for n in candidates if (section_dir / n).is_file()]
    deleted = sorted(indexed - live_names)

    print(f"section {readme_rel} ← {repo}/{canonical_dir} @ {branch}")

    # CHANGED — content identity. Cheap leg: recorded pin blob shas vs the live
    # listing (zero extra network). Exact leg (--bullet-drift): git-derived
    # pin→HEAD tree diff with +N/-M sizing. Either source defeats a false
    # `docs unchanged`; with neither, the blindness is NAMED, never implied away.
    changed: dict[str, str] = {}
    record = load_pin_record(section_dir, repo, canonical_dir, pin)
    if record is not None:
        for name in sorted(live_names & set(record)):
            if live[name] != record[name]:
                changed[name] = f"blob {record[name][:7]} → {live[name][:7]}"
    deltas: dict[str, tuple[str, str]] = {}
    if bullet_drift and head != pin:
        deltas = pin_tree_delta(repo, branch, pin, canonical_dir)
        for name, (status, size) in sorted(deltas.items()):
            if status == "M":
                changed[name] = (changed[name] + " · " if name in changed else "") + size
    content_verified = record is not None or (bullet_drift and head != pin)

    doc_work = len(new) + len(unmarked) + len(deleted) + len(changed)
    moved_only = head != pin and doc_work == 0

    if head == pin:
        print(f"  HEAD UNMOVED: {repo}@{branch} = harvest pin {pin[:7]}")
    elif moved_only:
        verified = ("content-verified" if content_verified
                    else "filename set only — content drift invisible without a pin "
                         "record or --bullet-drift")
        print(f"  HEAD MOVED (docs unchanged): {repo}@{branch} is {head[:7]} ({head}), "
              f"harvest pin is {pin[:7]} — pin-bump-only ({verified}), sizes no harvest work")
    else:
        print(f"  HEAD MOVED:   {repo}@{branch} is {head[:7]} ({head}), harvest pin is {pin[:7]}")
    for name, detail in sorted(changed.items()):
        print(f"  CHANGED upstream doc (same name, content moved since pin): "
              f"{canonical_dir}/{name} — {detail}")
    for name in new:
        size = f" ({deltas[name][1]})" if name in deltas else ""
        print(f"  NEW upstream doc (not indexed): {canonical_dir}/{name}{size}")
    for name in unmarked:
        print(f"  UNMARKED entry (local file exists, no machine-readable canonical marker): {canonical_dir}/{name}")
    for name in deleted:
        size = f" ({deltas[name][1]})" if name in deltas else ""
        print(f"  DELETED upstream (still indexed): {canonical_dir}/{name}{size}")

    badges: list[tuple[str, str, str]] = []
    if re_badge:
        badges = re_badge_candidates(section_dir, repo, canonical_dir, branch, indexed)
        for name, local_state, marker in badges:
            print(f"  RE-BADGE candidate: {canonical_dir}/{name} — index entry says "
                  f"'{local_state}', canonical records `{marker}` (suggestion only — "
                  "verify, then mirror as historical(…))")

    drifted_states: list[tuple[str, str, str]] = []
    acked_states: list[tuple[str, str, str, str]] = []
    if states:
        for name, local_state, marker in state_drift_pairs(
                section_dir, repo, canonical_dir, branch, indexed):
            # ACK'd deliberate divergence: the index bullet naming this canonical
            # doc carries the blessed annotation — report, never count as work.
            ack = next(
                (m.group(1).strip() for line in text.splitlines()
                 if f"{canonical_dir}/{name}" in line
                 and (m := STATE_DRIFT_ACK_RE.search(line))),
                None,
            )
            if ack:
                acked_states.append((name, local_state, marker, ack))
            else:
                drifted_states.append((name, local_state, marker))
        for name, local_state, marker in drifted_states:
            print(f"  STATE-DRIFT: {canonical_dir}/{name} — local entry says "
                  f"'{local_state}', canonical records `{marker}` (lifecycle stages "
                  "disagree; suggestion only — verify at the canonical doc, then "
                  "mirror forward-only)")
        for name, local_state, marker, ack in acked_states:
            print(f"  STATE-DRIFT (ACK'd deliberate): {canonical_dir}/{name} — local "
                  f"'{local_state}' vs canonical `{marker}` — index annotation: {ack} "
                  "(ruled-on divergence; sizes no harvest work)")

    head_state = ("unmoved" if head == pin
                  else "moved (docs unchanged)" if moved_only else "moved")
    print(
        f"  summary: {len(indexed)} indexed · {len(live)} live upstream · "
        f"{len(new)} new · {len(unmarked)} unmarked · {len(deleted)} deleted · "
        f"{len(changed)} changed"
        + (f" · {len(badges)} re-badge" if re_badge else "")
        + (f" · {len(drifted_states)} state-drift" if states else "")
        + (f" ({len(acked_states)} ack'd deliberate)" if acked_states else "")
        + f" · HEAD {head_state}"
    )

    if emit_entries:
        for name in new:
            emit_entry_stub(str(section_dir.relative_to(REPO_ROOT)), repo,
                            canonical_dir, name, head)

    work = (doc_work + len(badges) + len(drifted_states)
            + (1 if head != pin and not moved_only else 0))
    return work, moved_only


def write_pins() -> int:
    """`--write-pins` mode — record each section's per-doc blob shas at its pin.
    Refuses (exit 2) when a README pin is not the live HEAD: the record must be
    taken AT the pin, in the same session that (re-)pins the README."""
    failed = False
    for readme_rel, repo, canonical_dir, branch in SECTIONS:
        readme = REPO_ROOT / readme_rel
        print(f"section {readme_rel} ← {repo}/{canonical_dir} @ {branch}")
        try:
            pin_m = PIN_RE.search(readme.read_text(encoding="utf-8"))
            if not pin_m:
                raise ValueError("no harvest pin line (`pinned @ … (<full-sha>)`)")
            pin = pin_m.group(1)
            head = ls_remote_head(repo, branch)
            if head != pin:
                raise ValueError(
                    f"README pin {pin[:7]} != live HEAD {head[:7]} — a record taken "
                    "away from the pin would lie; re-pin the README first, then "
                    "re-run --write-pins in the same session")
            live = live_docs(repo, canonical_dir, branch)
            write_pin_record(readme.parent, repo, canonical_dir, branch, pin, head, live)
        except Exception as exc:
            print(f"check_harvest: could not write pin record for {readme_rel}: {exc}",
                  file=sys.stderr)
            failed = True
    return 2 if failed else 0


def main() -> int:
    argv = sys.argv[1:]
    known = ("--emit-entries", "--re-badge", "--bullet-drift", "--states",
             "--write-pins")
    unknown = [a for a in argv if a not in known]
    if unknown:
        print(f"check_harvest: unknown argument(s): {' '.join(unknown)} "
              f"(usage: check_harvest.py [{'] ['.join(known[:4])}] | --write-pins)",
              file=sys.stderr)
        return 2
    if "--write-pins" in argv:
        if len(argv) > 1:
            print("check_harvest: --write-pins is a separate mode — combine it with "
                  "nothing (the check stays report-only)", file=sys.stderr)
            return 2
        return write_pins()
    emit_entries = "--emit-entries" in argv
    re_badge = "--re-badge" in argv
    bullet_drift = "--bullet-drift" in argv
    states = "--states" in argv

    work = 0
    moved_only_sections = 0
    for readme_rel, repo, canonical_dir, branch in SECTIONS:
        try:
            section_work, moved_only = check_section(
                readme_rel, repo, canonical_dir, branch, emit_entries, re_badge,
                bullet_drift, states)
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
