# Session — fleet slice: squash-merge head-ref provenance (enabler + tripwire, the PR #62 follow-up)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-11 ~02:45Z (worker slice, dispatched by the continuous-mode coordinator per Q-0265)

## Scope

Consume the PR #62 card's 💡: squash landings write `<title> (#N)` subjects with NO
branch name, and this repo's enabler squashes — so the branch-prefix drift tripwire's
data source (`git log --merges` PR-merge subjects) thins as squash-only history
accumulates, and every convention born after the enabler cutover is invisible to the
survey. Close the blind spot at its source: the enabler's squash merge records
head-ref provenance (`Head-ref: <branch>` in the squash commit body), and
`check_branch_prefix_drift()` reads that line as a second branch-name source, with
the existing subject parsing kept as the fallback.

## What this session did

- **Branched `fix/squash-headref-provenance`** from origin/main `4307a98` (the PR #62
  merge). Prefix `fix/*` matches the live enabler patterns, so this PR is expected to
  self-arm at open. Inbox verified EMPTY at branch time (re-read at origin/main HEAD
  first, per the ritual); `control/claims/` verified README-only. Pre-slice hook-born
  telemetry residue (guard-fires/reflections/state) STASHED, not committed — the
  telemetry lane owns those appends (PR #32/#58/#62 precedent).
- **Claim taken FIRST commit** (`control/claims/fix-squash-headref-provenance.md`,
  ideas/fleet section), pushed immediately as the early in-flight signal, cleared in
  the close-out commit per the PR #42/#49/#62 precedent.
- **Enabler side** (`.github/workflows/auto-merge-enabler.yml`, arm step): the
  `gh pr merge --auto --squash` call now passes `--body "Head-ref: $HEAD_REF"`, with
  `HEAD_REF: ${{ github.head_ref }}` env-passed (never interpolated into the script —
  injection-safe). Every enabler-armed squash commit body records its source branch
  from this PR onward (`pull_request` workflows run from the PR's merge ref, so the
  enabler run on THIS PR already carries the change — its own merge is the live-fire).
  The refuse-to-arm guard (required status-check CONTEXT count), the sleep-15 fresh
  label re-read, and the job-level pattern/label conditions are UNTOUCHED. Honest
  tradeoff, recorded on the idea file's extension note: `--body` REPLACES GitHub's
  default squash body (the concatenated commit-message trail) — the per-commit trail
  stays readable on the PR itself. The file is KIT-OWNED: the customization is marked
  in-file and joins the PR #18 re-apply-after-regen duty (gate-step class, enabler
  edition).
- **Tripwire side** (`scripts/preflight.py::check_branch_prefix_drift`): second
  branch-name source — `HEAD_REF_BODY_RE` (`^Head-ref: (\S+)$`, MULTILINE) parsed from
  non-merge commit bodies via `git log --no-merges -n 200 --pretty=%b` — feeding the
  same fnmatch/recurrence pipeline; PR-merge-subject parsing stays the fallback for
  the pre-provenance history. Every failure leg still prints-and-passes (the advisory
  hermeticity rule unchanged — a failed provenance read continues on subjects alone);
  the OK line now reports the provenance count. Docstrings (module bullet + function)
  updated to the two-source reality.
- **Extension note appended** to `ideas/fleet/branch-prefix-drift-tripwire-2026-07-11.md`
  per the PR #36/#47 precedent — probe report and state untouched, state stays
  `historical(#62)`.
- **RIDER — found red mid-slice, fixed to unjam the whole repo:** at ~02:45Z the wake
  preflight went red on `check_sections` (exit 2, "no table rows parsed") — superbot
  had retired `docs/eap/fleet-manifest.md` to a pointer stub ELEVEN MINUTES earlier
  (superbot `34ebbac1`, 02:34:12Z: Status flipped historical/SUPERSEDED, ALL table
  rows removed, canonical fleet state moved to the fleet-manager GENERATED roster,
  `menno420/fleet-manager` `docs/roster.md`). Since the CI gate's non-control lane
  runs the same preflight with a LIVE manifest fetch, every non-control PR repo-wide
  reds from the raw-CDN cache expiry onward (the 02:42:17Z sibling telemetry run
  squeaked through green on the cache window). Bounded fix in
  `scripts/check_sections.py`: detect the EXPLICIT supersede tombstone (zero rows AND
  the SUPERSEDED marker) and pass LOUDLY with an advisory naming the roster; genuine
  parse failures (no rows, no tombstone) still exit 2 — fail-loud preserved.
  Re-pointing the section derivation at the roster (lane→section mapping, new-section
  duties — the roster carries lanes with no section yet, e.g. superbot-mineverse,
  superbot-idle) is a REAL grooming slice, deliberately NOT folded in — flagged as
  the ripest follow-up in the heartbeat.
- **Not touched:** no proposal (outbox stays at 5, all pulled — a one-line provenance
  stamp has no simulator question), no new idea file (this extends a built
  `historical(#62)` idea; extension-note shape, no new battery pass), README/config
  untouched, substrate-gate.yml untouched (byte-identical to the PR #54 bytes).

### Live tripwire run (real output, this tree)

```
$ python3 scripts/preflight.py --branch-prefix-drift
branch-prefix-drift: OK — every recurring merged-branch prefix matches a configured pattern (41 merged branches surveyed (0 via Head-ref provenance), 13 patterns, 1 one-off unmatched branch(es) below the recurrence bar)
branch-prefix-drift: OK — advisory sweep complete (report-only, never affects the exit)
exit=0
```

(0 via provenance is HONEST: no squash commit on main carries a `Head-ref:` line yet —
the first one is this slice's own merge. Note the survey base is already thinning
exactly as the PR #62 card's Q4 predicted: 41 merge-subject branches recoverable on
main now vs the 46 that slice counted on its own tree ~20 minutes earlier — its extra
forward-merge commits aged out with the squash-only window.)

### Planted-provenance smoke (real output, scratch git repos — tree untouched)

Scratch repo = `scripts/preflight.py` copied beside a doctored `substrate.config.json`
(REPO_ROOT derives from the script path, so the checker runs against the scratch
history — the same tree-untouched seam as the PR #62 doctored-config replays).

```
# patterns ["fix/*"]; commits with bodies Head-ref: probe/alpha, probe/beta,
# fix/covered; plus one REAL merge commit "Merge pull request #4 from menno420/slice/gamma"
$ python3 scripts/preflight.py --branch-prefix-drift
branch-prefix-drift: DRIFT (advisory) — 1 recurring merged-branch prefix(es) match NO automerge.branch_patterns entry (the enabler never arms on these — the PR #55 silent-no-op class; add the pattern or retire the convention):
branch-prefix-drift:   probe/*  ×2  (e.g. probe/beta, probe/alpha)
branch-prefix-drift: OK — advisory sweep complete (report-only, never affects the exit)
exit=0

# patterns ["fix/*","probe/*","slice/*"] — everything covered, provenance counted
branch-prefix-drift: OK — every recurring merged-branch prefix matches a configured pattern (4 merged branches surveyed (3 via Head-ref provenance), 3 patterns, 0 one-off unmatched branch(es) below the recurrence bar)
exit=0

# fresh repo, one plain commit — pre-provenance window degrades honestly
branch-prefix-drift: no PR merge subjects or Head-ref provenance lines in local history (shallow clone or pre-provenance squash window) — nothing to compare, still PASS
exit=0
```

The DRIFT leg fires from provenance lines ALONE (probe/* ×2 — both squash-style
commits, zero merge subjects for them); the covered `fix/covered` provenance matches;
the classic merge-subject landing (`slice/gamma`) still parses via the fallback and
correctly sits below the recurrence bar as a one-off.

### check_sections rider smoke (real output)

```
$ python3 scripts/check_sections.py            # live fetch = the tombstone
check_sections: SUPERSEDED (advisory) — the fleet manifest is a retirement tombstone (zero lane rows; canonical fleet state moved to the fleet-manager GENERATED roster, menno420/fleet-manager docs/roster.md). Section-vs-lane sync is UNCHECKABLE until the section derivation is re-pointed at the roster (queued follow-up slice) — passing LOUDLY, never silently.
exit=0

$ python3 scripts/check_sections.py --manifest <scratch>/manifest-0fd30433.md   # the REAL last-rows manifest, pinned pre-tombstone SHA
check_sections: OK — 10 sections in sync with the manifest
exit=0

$ python3 scripts/check_sections.py --manifest <scratch>/broken-manifest.md    # no rows, NO tombstone marker
check_sections: cannot read/parse manifest: no table rows parsed — manifest format changed? (…)
exit=2
```

### Local pre-push runs (real output)

```
$ python3 scripts/preflight.py
preflight: PASS — check_sections (exit 0)
preflight: PASS — check_ideas (exit 0)
preflight: PASS — check_ideas --outbox (exit 0)
preflight: PASS — bootstrap check --strict --status-only (exit 0)
preflight: PASS — gate-wiring self-check (exit 0)
preflight: PASS — open-work advisory (report-only, never gates) (exit 0)
preflight: PASS — branch-prefix-drift advisory (report-only, never gates) (exit 0)
preflight: OK — all 7 checks green

$ python3 bootstrap.py check --strict
check: all checks passed.
```

(Both re-run green after the heartbeat overwrite, immediately before push — 284 idea
files conform. This card is written before push per the honest-stamps rule; no merge
outcome is claimed here for this slice's own PR. The LIVE-FIRE check — does this
slice's own squash commit on main carry the `Head-ref:` line, and does the tripwire
count it — happens post-merge and is reported to the coordinator, not pre-written
here.)

**📊 Model:** fable-5 · fix payload (enabler arm-step `--body` provenance line +
in-file re-apply marker, tripwire second source + regex + docstrings, extension note,
check_sections tombstone rider, claim add+clear, card, heartbeat; no proposal, no new
idea file)

## 💡 Session idea

**The supersede tombstone class deserves a kit-side name.** Twice in one day an
upstream contract surface this repo's checkers consume changed shape underneath a
consumer (the kit regenerating the gate file; now the fleet retiring the manifest
mid-flight — found red ~11 minutes after the upstream commit, only because a slice
happened to be running preflight). Both times the fix was the same shape: detect the
EXPLICIT retirement marker, degrade loud-not-red, flag the re-pointing as its own
slice. Kit-seam candidate (cross-link shape, `ideas/substrate-kit/README.md`): a
convention for consumed-surface tombstones — a machine-readable `superseded-by:` line
in the retiring doc's banner — so every downstream checker can implement the same
three-step (detect → advisory-pass → queue re-point) without each lane rediscovering
the failure live in CI. The re-point itself for THIS repo (section derivation ←
fleet-manager `docs/roster.md`) is the companion build slice: the roster has lanes
with NO section yet (superbot-mineverse, superbot-idle at minimum), so it is a
sections-contract grooming slice, not a parser swap.

## ⟲ Previous-session review

PR #62 (branch-prefix drift tripwire; merge `4307a98`) — claims verified against this
tree and the GitHub API, all TRUE: seventh CHECKS entry + `check_branch_prefix_drift()`
live in `scripts/preflight.py` exactly as carded (this slice extends it) ✓; idea file
state `historical(#62)`, probe report intact ✓; claim cleared — `control/claims/` held
only README.md at this slice's branch time ✓; fleet index row + substrate-kit
Cross-links row present ✓; its card honestly claimed no merge outcome pre-push, and
the outcome is now recorded with evidence (API read 02:47Z): `merged: true`,
`merged_by: github-actions[bot]`, created 02:37:26Z → merged 02:37:54Z — 28 seconds
open-to-merge, the enabler's THIRD convention-prefix live-fire (`slice/*` @ #55,
`upgrade/*` @ #57, now `build/*`) ✓. Its Q4 honesty aged WELL and fast: the "survey
thins as squash-only history accumulates" prediction is already measurable — 46
recoverable branch names on its tree, 41 on main twenty minutes later (its own
forward-merge commits were the difference). One thing its card could not know: the
fleet manifest its repo's section checker consumes was retired upstream ~3 minutes
BEFORE its merge (superbot `34ebbac1` 02:34:12Z vs merge 02:37:54Z) — its final green
preflight ran on the raw-CDN cache of the old manifest; the red surfaced in THIS
slice's first preflight instead. No fault, pure timing — but it is the sharpest
possible datapoint for this card's 💡 (a consumed-surface tombstone convention), and
its card's own 💡 (this slice) shipped one wake later exactly as sized.

## Handoff → next wake

Inbox first, as always (verified empty at `4307a98` at branch time). From this PR's
merge onward every enabler-armed squash commit carries `Head-ref: <branch>` in its
body and the drift tripwire counts those lines as first-class survey input — check
the count in the OK line ("N via Head-ref provenance") to watch the provenance base
grow. RIPEST follow-up (flagged, not built): re-point `scripts/check_sections.py`'s
section derivation at the fleet-manager GENERATED roster
(`menno420/fleet-manager docs/roster.md` — kill-switch rule: trust heartbeats if
`generated-at` goes stale >24h) — a sections-contract grooming slice: decide
lane→section mapping and create/park sections for roster lanes with none
(superbot-mineverse, superbot-idle; codetool-labs are wound down). Until then
check_sections passes with a loud SUPERSEDED advisory and section drift is
UNCHECKED. Standing re-apply duty extended: `auto-merge-enabler.yml` now carries a
host customization (the `--body` provenance line) in a KIT-OWNED file — re-apply
after any adopt/upgrade regeneration, same class as the PR #18 gate step (in-file
comment marks it; the tripwire degrades honest-not-red if the line stops being
written, so the loss is visible at the next wake's OK-line provenance count). The
stash holds pre-slice guard-fire residue (telemetry lane pattern, PR #32/#58
precedent) if a telemetry sweep wants it.
