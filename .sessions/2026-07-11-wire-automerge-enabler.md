# Session — fleet slice: wire the staged auto-merge enabler live + fix branch_patterns

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-11 ~01:45Z (worker slice, dispatched by the continuous-mode coordinator per Q-0265)

## Scope

Consume the PR #54 card's 💡: the kit v1.8.0 staged auto-merge enabler
(`.substrate/ci/auto-merge-enabler.yml`) was a silent no-op — its default
`automerge.branch_patterns: ["claude/*"]` matches ZERO of this repo's real branch
prefixes. Fix the patterns to the empirically-observed set, wire the enabler live via
`adopt --wire-enforcement`, and live-fire it on this very PR (branch `slice/*` matches
the new patterns; the enabler is `pull_request`-triggered, so it runs on the PR that
ships it).

## What this session did

- **Empirical pattern set** (merged-PR branch-prefix survey, PRs #5–#54; carried over
  from the coordinator's survey, spot-consistent with `git log` merge subjects):
  `probe/*` ×17 · `seed-*` ×7 (NO slash — e.g. `seed-games-ideas-2026-07-10`) ·
  `slice/*` ×6 · `groom/*` ×4 · `harvest/*` ×4 · `build/*` ×3 · `upgrade/*` ×1 ·
  `refine/*` ×1 · `fix/*` ×1 · `batch/*` ×1 · `telemetry/*` ×1 · `heartbeat/*` ×1 ·
  `docs/*` ×1 — and **zero `claude/*` ever**. `substrate.config.json::automerge.branch_patterns`
  set to all 13 prefixes; `required_context` stays `substrate-gate`. Broad is safe
  here: arming never merges anything — the merge stays gated by the required
  `substrate-gate` check, and the `do-not-automerge` label is the per-PR escape hatch.
- **Ran `python3 bootstrap.py adopt --wire-enforcement`** (the kit's documented
  installer for the staged enabler). Result: `.github/workflows/auto-merge-enabler.yml`
  PLANTED LIVE — the job-level `if` carries all 13 `startsWith(github.head_ref, …)`
  clauses regenerated from config (verified `seed-` is slashless); the refuse-to-arm
  guard (counts required status-check CONTEXTS via the rules API, refuses on zero
  rather than inverting the gate), the sleep-15 fresh label re-read (stale-payload
  race guard), and the `gh pr merge --auto --squash` arm step all survived
  regeneration. Workflow name `auto-merge-enabler` ≠ `substrate-gate` and it is NOT a
  required context — no conflict with the gate. `--wire-enforcement` implies
  `--include-claude`, so `.claude/CLAUDE.md` + `.claude/settings.json` (the kit nag
  hooks, rendered from the filled interview slots) were planted too and are shipped
  with this slice (`.substrate/state.json` records the CLAUDE.md plant hash — the
  plant and the record travel together).
- **The predicted gate clobber happened a THIRD time, detected a third time:** adopt
  regenerated the kit-owned `substrate-gate.yml` and dropped the PR #18
  `wake preflight` step; carve-out protection named it and banked the full pre-regen
  gate at `.substrate/backup/substrate-gate.pre-regen-1ce5228e.yml` (precedent: PR #35,
  PR #54). Since the regenerated gate's ONLY delta vs HEAD was the dropped step (the
  kit template itself is unchanged since the v1.8.0 upgrade), the re-apply was done as
  `git checkout HEAD -- .github/workflows/substrate-gate.yml` — the gate ships
  **byte-identical to HEAD `935ebaa`** (PR #18 step intact between `setup-python` and
  the session-card gate step; `git diff HEAD` on the file is empty; the PR #36
  gate-wiring tripwire fired green, see the preflight run below). Workflow name + job
  id `substrate-gate` unchanged — the required-check context renamed nothing.
- **Live-fire test — this PR is the experiment:** branch
  `slice/wire-automerge-enabler` matches `slice/*`; the PR opens READY (the enabler's
  own condition requires `draft == false`). Expected sequence on open: enabler job
  runs → refuse-to-arm guard counts the base branch's required contexts (must find
  `substrate-gate`) → label re-read finds no `do-not-automerge` → arm via
  `gh pr merge --auto --squash`. **The arm result is verified in this slice's PR
  thread post-push** (this card is written before push, per the honest-stamps rule —
  no outcome claimed here). Known inertness preconditions (adopt's repo-settings
  checklist, owner UI): "Allow auto-merge" ON + a ruleset requiring `substrate-gate`
  on main — this repo's existing landing convention already arms auto-merge by hand
  per PR, which implies both are set; if the live-fire fails anyway, the exact
  workflow-run failure becomes the follow-up (and a ⚑ owner-action if it names a repo
  setting).
- **Not touched:** no idea-tree changes, no proposal (outbox stays at 5, all pulled —
  process slice, nothing earned an append), no claim (kit/config surface, same
  no-claim shape as PR #50's root-contract precedent; `control/claims/` verified empty
  at branch time), inbox verified empty at origin/main `935ebaa` at branch time.

### Local pre-push runs (real output)

```
$ python3 scripts/preflight.py
preflight: PASS — check_sections (exit 0)
preflight: PASS — check_ideas (exit 0)
preflight: PASS — check_ideas --outbox (exit 0)
preflight: PASS — bootstrap check --strict --status-only (exit 0)
gate-wiring: OK — .github/workflows/substrate-gate.yml non-control lane runs scripts/preflight.py
preflight: PASS — gate-wiring self-check (exit 0)
preflight: PASS — open-work advisory (report-only, never gates) (exit 0)
preflight: OK — all 6 checks green

$ python3 bootstrap.py check --strict
check: all checks passed.
```

(Both runs re-executed green after the heartbeat overwrite, immediately before push.
The gate-wiring OK line is the PR #36 tripwire proving the gate still carries the
re-applied PR #18 step on the post-adopt tree.)

**📊 Model:** fable-5 · high · config + wiring payload (substrate.config.json
branch_patterns ×13, live + staged enabler, .claude/ nag-hook plants, state.json,
banked backups, gate verbatim-restore; no idea-tree changes, no proposal)

## 💡 Session idea

**Branch-prefix drift tripwire — keep `branch_patterns` honest against reality.**
The claude/* no-op was invisible for a whole slice because nothing checks the config's
patterns against the branch names the repo actually merges. Lane-sized check (fits the
`scripts/preflight.py::CHECKS` seam or `check_ideas`-style advisory): derive the live
prefix set from `git log --merges` subjects (or the PR head refs of the last N merges)
and warn when a recurring prefix (≥2 occurrences) matches NO pattern in
`substrate.config.json::automerge.branch_patterns` — the exact silent-no-op class this
slice just fixed, caught at wake time instead of by survey. Kit-generic (the enabler +
config key are kit-planted, so the checker belongs on the kit's seam — cross-link
candidate for `ideas/substrate-kit/README.md`); a local advisory copy is one small
stdlib function. Anchors: `substrate.config.json::automerge`,
`.github/workflows/auto-merge-enabler.yml` (job-level `if`), the fnmatch-vs-startsWith
materialization in the kit's adopt path.

## ⟲ Previous-session review

PR #54 (kit self-upgrade v1.7.1 → v1.8.0 + claims-dir reconcile; merge `935ebaa`)
promised, and this tree verifies: vendored `bootstrap.py --version` → 1.8.0 ✓;
root `claims/` GONE and `control/claims/README.md` present (the reconcile executed as
written — one convention, not two) ✓; the regenerated gate carries the re-applied
PR #18 `wake preflight` step (1 match in the live file; the PR #36 tripwire fired
green on this slice's runs too) ✓; `.substrate/ci/auto-merge-enabler.yml` staged with
the two new config keys (`automerge`, `claims_dir`) ✓; its claim was cleared at
close-out (`control/claims/` held only README.md at this slice's branch time) ✓.
Its card's 💡 sized THIS slice precisely — including the exact failure mode ("wiring
it as-is would be a silent no-op") and the three-step recipe (patterns → adopt →
verify guard), consumed as written. Two honest deltas from its framing: (1) its 💡
proposed verifying the refuse-to-arm guard "against the branch-protection rules API
from this seat" — not done from this seat (anonymous api.github.com 403s through the
proxy; the enabler's guard step IS that verification, run with the workflow's own
token on the PR itself — the live-fire subsumes the seat-local check with strictly
better provenance); (2) its card said the enabler pattern-materialization was
`claude/*` in ONE clause — the regen confirms patterns materialize 1:1 into
`startsWith` clauses (13 in, 13 out), and `seed-*` correctly materializes slashless,
which the survey flagged as the one pattern a naive `<prefix>/*` convention would have
gotten wrong.

## Handoff → next wake

Inbox first, as always (verified empty at origin/main `935ebaa` at branch time). The
auto-merge enabler is LIVE from this PR's merge onward: every matching-prefix READY PR
self-arms at open and merges when `substrate-gate` goes green — the by-hand
per-PR arming convention is now structural (hand-arming remains harmless/idempotent).
`do-not-automerge` label = opt-out per PR. If this slice's live-fire showed an arm
failure in the PR thread, read the enabler run log first — a repo-settings failure
("Allow auto-merge" off / no required context) is a ⚑ owner-action, not a code fix.
NEW planted surfaces shipped here: `.claude/settings.json` nag hooks (kit-owned,
regenerated by future adopts) — sessions in this repo now get the kit's
sessionstart/stopcheck hooks. Still queued: `upgrade --apply-docs` (two template
versions deep on 2 docs), grooming round 4 seeds (unchanged, see heartbeat), and this
card's 💡 (branch-prefix drift tripwire).
