# Session — substrate-kit heartbeat-behind pair batched probe (the section's two remaining captured heads through the battery)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-11 ~08:15Z (worker slice, dispatched by the continuous-mode coordinator per Q-0265)

## Scope

The `ideas/substrate-kit/` section carried two remaining captured heads, captured the
same day one slice apart: `parallel-session-heartbeat-reconcile-2026-07-10.md` (the
one-writer rule's same-lane blind spot → planted control/README section + checker
advisories) and `behind-stall-auto-updater-2026-07-10.md` (a committed workflow closing
⚑ OWNER-ACTION 11's behind-stall residual agent-side). This slice probes both, batched.
Section claimed first — control/claims/probe-substrate-kit-heartbeat-behind-pair.md
landed on main via fast-lane PR #136 (merged 08:11:15Z by the enabler) before any build
work; the only sibling claim at HEAD is `probe-pokemon-mod-lab-patch-only-egress.md`
(PR #135) — a disjoint section, no collision.

## Probe shape (stated per the batch precedent)

Two FULL battery-v0 reports, not primary+pointer: the #87 pointer shape is for
one-surface pairs, and this pair targets two DISTINCT kit surfaces — the planted
control/README template + status checker vs the CI workflow set + enabler generator —
with different failure modes and different smallest slices (the #102/#116/#132
sibling-batteries precedent). One shared verify-first sweep at one kit pin served both
reports.

## Verify-first (one sweep, both reports)

- **substrate-kit live HEAD `be72c09`** (`git ls-remote` 2026-07-11T08:13:45Z; blobless
  clone at the pin). The coordinator's evidence sweep earlier this session read the same
  surfaces at `c970f0a` (the v1.10.0 wave close-out, 07:52:13Z); the `c970f0a..be72c09`
  delta is ONE control-only claim file (kit PR #186's in-flight v1.10.1 payload claim —
  gate tail-1 multi-card shadowing fix + doctrine emphasis normalization, disjoint from
  both heads), so both reads bind. Newest tag **v1.10.0, NO v1.11.0**; `CHANGELOG.md` @
  `be72c09` has an **EMPTY `## [Unreleased]`** — neither head overtaken kit-side.
- **Head A premise HOLDS:** the kit-planted control/README template
  (`src/engine/templates/control-README.md.tmpl@fa20735`; dist embeds the same bytes)
  carries NO same-lane reconcile guidance — repo-wide `git grep -i reconcil` outside
  `dist/` hits only `.sessions/` retros plus one "reconciled as twins" aside about
  duplicate ORDER execution; its only "parallel sessions" sentence is the work-claims
  prevention paragraph. The recipe exists ONLY host-side (this repo's README § Landing
  conventions, proven PRs #10–#17 + the PR #52 renumber rule, lived ~20 times).
- **Head B premise HOLDS but mechanism is WRONG as written:** kit workflows at HEAD
  (enabler/disarm/ci/release) and the planted-enabler generator
  (`automerge_enabler_workflow()`, `src/engine/adopt.py@37bd7e2`, relpath at
  `adopt.py:910`) carry ZERO update-branch machinery; ⚑ OWNER-ACTION 11 still open at
  kit `control/status.md@5d0f59b` (heartbeat 07:05:00Z; VERIFIED-NEEDED cites #107 +
  manual updates #144/#147/#150/#153; the #111 synchronize fix "a partial, not a full,
  close"). The sharpened finding: updates pushed with plain `GITHUB_TOKEN` do not
  trigger workflow runs (recursive-workflow guard), so the capture's naïve
  update-branch call trades the behind-stall for a checks-never-report stall — the
  routed build must pick an owner PAT/App token or an explicit gate re-dispatch.
- **Fork resolution: park(routed), NOT parked(overtaken), for both.**
- **Grounding drift recorded in both reports (one line):** both captures pin superbot
  `docs/eap/fleet-manifest.md@dc19b1e` for "why now" — now a tombstone (superseded
  2026-07-11 by fleet-manager `docs/roster.md`); the premise survives, the pointer is
  historical.

## Verdicts (one per idea)

- `parallel-session-heartbeat-reconcile` → **parked(routed — substrate-kit lane
  build)**: planted control/README "parallel sessions, same lane" section + two
  mechanical checker advisories (non-monotonic `updated:` stamp ·
  reconcile-dropped-facts); this repo's README § Landing conventions recipe is the
  working reference implementation; no simulator question.
- `behind-stall-auto-updater` → **parked(routed — substrate-kit lane build,
  scope-sharpened)**: un-adopted at `be72c09` and ⚑ OWNER-ACTION 11 still open, but the
  workflow must solve the GITHUB_TOKEN no-retrigger gotcha (owner PAT/App token or gate
  re-dispatch — the naïve call makes a WORSE silent stall); the owner checkbox stays
  the cleanest full close, this workflow is the agent-side fallback; no simulator
  question.

No outbox proposal (nothing sim-shaped — template/checker/workflow features are proven
by their own red/green, the #114 precedent for this same target lane, reaffirmed by
#132). Section README index re-badged for both rows. Section milestone NOT claimed:
`host-checkers-one-gate-2026-07-10.md` remains `captured` — the section's last open
head.

## Verification (real runs, this tree)

Full `python3 scripts/preflight.py` (all 8 checks) + `python3 bootstrap.py check
--strict` run green immediately before push, after the heartbeat overwrite; a pre-push
`git fetch origin main` reconciles any mid-flight sibling forward-only per the README
recipe if main moves (the pokemon patch-only-egress probe is in flight, claim #135).
This slice also commits the session's own `.substrate/reflections.json` mine
(`bootstrap reflect --mine`, R-0034/R-0035) on the slice branch, keeping the claim PR
control-only.

**📊 Model:** fable-5 · medium · batched probe slice (2 probe reports + state lines +
section index + card + claim clear + heartbeat + reflections commit; no scripts, no
workflows, no proposal — task-class: bounded same-family battery pass)

## 💡 Session idea

**The GITHUB_TOKEN no-retrigger gotcha is a capability-ledger-worthy fact for THIS
repo's `docs/CAPABILITIES.md` too.** The behind-stall probe's sharpest finding —
branch updates/pushes made with a workflow's own `GITHUB_TOKEN` do not trigger new
workflow runs, so any automation that updates a PR head with the plain token silently
produces a checks-never-report stall — is not kit-specific: any future auto-updater,
auto-fixer, or bot-push workflow in THIS repo inherits it, and this repo's
control/README already documents the sibling "zero check runs" failure family without
naming this cause. One ledger entry (wall + the two fixes: PAT/App token or explicit
re-dispatch) would make the class discoverable before the next automation slice
re-derives it live.

## ⟲ Previous-session review

Reviewed: `.sessions/2026-07-11-substrate-kit-clobber-family-probe.md` (the #132
clobber-family batched probe — this slice's direct precedent and shape template). Its
claims verified against the tree at HEAD: (1) both its heads are badged
`parked(routed)` with probe parentheticals in `ideas/substrate-kit/README.md` (the
enabler-card-status-guard-upstream and carveout-needles-config rows, verified in this
slice's own index edit); (2) its claim file
`control/claims/probe-substrate-kit-clobber-family.md` is GONE from `control/claims/`
(deleted at session close per the convention — only README + the pokemon #135 claim +
this slice's claim exist at HEAD); (3) its heartbeat facts are stamped and survived
two subsequent overwrites — the pokemon #134 slice demoted its `last-shipped:` head
WITH its real PR number ("Prior: #132 … number stamped by this next session per the
#72/#79 precedent"), and its THREE-routed-heads fan-in note chains intact under the
pokemon slice's notes head. Its method notes were adopted here: claim fast-laned
before any build byte (#136), verify-first at the LIVE lane HEAD before probing (this
slice re-verified at `be72c09` after the coordinator's `c970f0a` sweep — the HEAD had
moved by one claim commit, and the re-read is what makes the pin honest), and its 💡
(blobless clone + `git checkout HEAD -- <named paths>`, never grep a partial checkout)
was executed verbatim as this slice's read recipe.

## Handoff → next wake

The substrate-kit section is now 5/6 probed-or-routed; the ripest next slice is the
`host-checkers-one-gate-2026-07-10.md` probe — the section's LAST captured head, and
probing it closes the section (first claim the section per the ritual). The kit-lane
fan-in bundle now stands at FIVE routed heads (carveout-needles-config +
enabler-card-status-guard-upstream(sharpened) + kit-line-self-drift +
parallel-session-heartbeat-reconcile + behind-stall-auto-updater(sharpened)) plus the
pokemon ruling-sync kernel rider the #134 slice added — one manager ORDER could carry
the whole bundle, same config/template/check seam family; the heartbeat notes say so
for the :30 sweep. Watch the kit's release cadence: a v1.10.1 payload claim is in
flight at `be72c09` (gate tail-1 multi-card shadowing fix — disjoint from all five
heads, but any next hop should re-verify the parks at the new HEAD before relaying).
The pokemon patch-only-egress probe (claim #135) was in flight this session — expect
its heartbeat facts to need a forward reconcile if it lands first.
