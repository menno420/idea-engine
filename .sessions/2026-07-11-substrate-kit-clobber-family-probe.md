# Session — substrate-kit clobber-family batched probe (both host-customizations-on-kit-owned-files heads through the battery)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-11 ~07:46Z (worker slice, dispatched by the continuous-mode coordinator per Q-0265)

## Scope

The `ideas/substrate-kit/` section carries a same-family pair captured one slice apart:
`enabler-card-status-guard-upstream-2026-07-11.md` (PR #86's arm guard + the gate
preflight seam → kit template features) and `carveout-needles-config-2026-07-11.md`
(host-declared byte-needles → the kit's carve-out scan stops being step-blind). Both
say: host customizations layered on KIT-OWNED files must become kit features, or the
next hop clobbers them. This slice probes both, batched. Section claimed first —
control/claims/probe-substrate-kit-clobber-family.md landed on main via fast-lane
PR #130 (merged 07:35:00Z by the enabler) before any build work; the only sibling
claim at HEAD is `probe-pokemon-mod-lab-post-eap-playtest-kit.md` (PR #129) — a
disjoint section, no collision.

## Probe shape (stated per the batch precedent)

Two FULL battery-v0 reports, not primary+pointer: the #87 pointer shape is for
one-surface pairs, and this pair targets two DISTINCT kit surfaces — the enabler
template + gate config schema vs the carve-out scan in `adopt.py` — with different
failure modes and different smallest slices (the #102/#116 sibling-batteries
precedent). One shared verify-first sweep at one kit pin served both reports.

## Verify-first (≤20 min, one sweep, both reports)

- **substrate-kit live HEAD `09837de`** (`git ls-remote` 2026-07-11T07:34:56Z;
  blobless clone at that pin 07:36Z — raw-path fetch not used this session, the
  git protocol read the same public bytes). Tag list at the same ls-remote:
  **v1.10.0 is the newest tag, NO v1.11.0**; `CHANGELOG.md` @ `09837de` has an
  **EMPTY `## [Unreleased]`** section (immediately followed by
  `## [1.10.0] - 2026-07-11`) — the next release is not staged.
- **Neither idea is adopted or in flight at HEAD:** zero `carveout_needles` /
  byte-needle hits anywhere in `src/`, `dist/bootstrap.py`, `docs/`, `CHANGELOG.md`;
  `gate_carveouts()` (`src/engine/adopt.py:882`) is still step-granular — docstring
  verbatim: "Removals and edits of kit content are NOT reported here"; the enabler
  template (rendered in `adopt.py`) carries exactly TWO guards (refuse-to-arm on
  zero required contexts + fresh `do-not-automerge` label re-check), no card-status
  guard; no `extra_checks`/preflight config key exists; the kit's own
  `docs/ideas/` backlog (29 entries) and `control/inbox.md` have no matching entry.
  Post-v1.10.0 commits at HEAD are T5 bench re-scope work (kit PRs #180/#182/#183)
  plus the release close-out (#179) — no template/scan feature in flight.
- **Fork resolution: park(routed), NOT parked(overtaken), for both.**
- **Two capture corrections found live** (recorded in the reports): (1)
  `src/engine/grammar.py` EXISTS at HEAD but does NOT carry `_BADGE_RE` — the badge
  regex lives at `src/engine/checks/check_docs.py:40` and the in-progress parse at
  `src/engine/checks/check_session_log.py:103`; (2) v1.10.0's `session-card-hold`
  (shipped post-capture, live-fired on this repo's own PR #125) absorbed the arm
  guard's PRIMARY race at the required check — the guard half of the upstream ask
  is now defense-in-depth, and the probe scope-sharpens the routed core accordingly.

## Verdicts (one per idea)

- `carveout-needles-config` → **parked(routed — substrate-kit lane build;
  manager-ORDER-worthy)**: the step-blindness class is two-hop-evidenced
  (PR #120 `f417a1f` · PR #125 `b11fe68`), un-adopted at `09837de`, and one config
  key closes it for every adopter; no simulator question.
- `enabler-card-status-guard-upstream` → **parked(routed — substrate-kit lane
  build, scope-sharpened)**: un-adopted at `09837de`, but v1.10.0's
  session-card-hold absorbed the guard's primary race — the routed core is the
  gate-preflight config seam + badge-grammar single-sourcing, the arm guard as
  opt-in; no simulator question.

No outbox proposal (nothing sim-shaped — template/scan features are proven by
their own red/green, the #114 precedent for this same target lane). Section README
index re-badged for both rows.

## Verification (real runs, this tree)

Full `python3 scripts/preflight.py` (all 8 checks) + `python3 bootstrap.py check
--strict` run green immediately before push, after the heartbeat overwrite; a
pre-push `git fetch origin main` reconciles the in-flight pokemon-mod-lab sibling
forward-only per the README recipe if main moves. Telemetry residue: this seat's
hook-born `.substrate/` appends left uncommitted for the telemetry lane per the
PR #32/#58/#62 precedent.

**📊 Model:** fable-5 · medium · batched probe slice (2 probe reports + state
lines + section index + card + claim clear + heartbeat; no scripts, no workflows,
no proposal — task-class: bounded same-family battery pass)

## 💡 Session idea

**A blobless `git clone --filter=blob:none --no-checkout` of a lane repo is a
sharper verify-first instrument than raw-path fetches for "is X adopted at HEAD"
questions — but `git checkout HEAD -- .` on one defeats it** (every blob fetches
serially; this session's full-tree checkout timed out at 2m and left a PARTIAL
working tree that briefly made `src/engine/grammar.py` look nonexistent — a
false capture-correction narrowly avoided by re-listing via `git ls-tree` before
concluding). The verify-first recipe worth writing down for probe slices: ls-remote
for the pin, blobless clone for log/tree topology, `git checkout HEAD -- <named
paths>` for exactly the files the question needs, and NEVER grep the working tree
of a partial checkout — `git ls-tree -r --name-only` is the existence oracle.

## ⟲ Previous-session review

Reviewed: `.sessions/2026-07-11-superbot-mineverse-first-batch.md` (the
coordinator-named predecessor thread; later sibling cards — seed-carveout-needles,
verdict-registry-probe — were consumed via the heartbeat chain instead). Its claims
verified against this tree: all five mineverse captures + the section index exist
as carded and lint-clean (300 idea files conform at this slice's preflight); its
claim file is gone from `control/claims/` (deleted at session close, as the
convention requires); ORDER 001 remains the only inbox order, and this card
carries the same family-level `📊 Model:` line its handoff said the standing rule
needs. Its method notes aged well and were adopted here: claim + born-red card as
the earliest commits (this slice's claim rode #130 before any build byte), and
"verify-first at lane HEAD before probing anything" applied with force — this
probe's whole verdict fork (routed vs overtaken) hung on a live-HEAD read of a
lane that shipped three releases yesterday-today, and the read indeed moved the
scope (the v1.10.0 session-card-hold correction). Its 💡 (harvest sweep keyed on
the 💡 byte-marker across kit-adopted lanes' `.sessions/`) is still ungraduated —
NOT executed by this slice (substrate-kit section claim only, disjoint scope);
it remains the ripest process head for a fleet-section claim.

## Handoff → next wake

The substrate-kit section now has 4/6 heads probed-or-routed; the two remaining
captured heads (`parallel-session-heartbeat-reconcile`, `behind-stall-auto-updater`)
are non-expiring and un-sequenced — batchable the same way (same section claim
shape). The kit-lane fan-in is now THREE routed heads deep (kit-line-self-drift +
this pair) — that is a manager-ORDER-worthy bundle: one kit-lane ORDER could carry
all three (the heartbeat notes say so explicitly). Watch the kit's release cadence:
three tags dated 2026-07-11 alone; any next hop should re-verify both parks at the
new HEAD before relaying (an [Unreleased] entry naming needles/guard would flip
either park to overtaken in one line). The pokemon-mod-lab sibling probe was in
flight this session (claim #129) — its heartbeat facts were reconciled forward at
push time, per the recipe.
