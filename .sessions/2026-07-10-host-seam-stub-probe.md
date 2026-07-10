# Session — host-seam conformance stub probe (superbot-games): battery v0 → park(build-direct, sequenced)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-10 (dispatched by the continuous-mode coordinator per Q-0265)

## What this session did

Probing `ideas/superbot-games/host-seam-conformance-stub-2026-07-10.md` through battery
v0 (single-pass — README panel default per sim-lab VERDICT 002: no repeat-disagreement
signal, no irreversible/high-blast-radius surface) against LIVE state: superbot-games @
HEAD `b134961` (ls-remote 23:52Z — unmoved since PR #39's read), superbot-next @ HEAD
`c3f7a02` (ls-remote 23:52Z; `control/inbox.md` ORDER 002 raw-read at that pin —
`status: new`, acked in the lane's status but NOT in `done=`, so the plugin/manifest
contract is live-verified still unbuilt). Twin-check resolved before probing: this idea
targets the cross-repo host/plugin seam PR #39's probe explicitly fenced off ("host
wiring stays in their own slices"; its Q4 ruled the cross-repo plane binds shape, not
code) — it is NOT PR #39's resolver-conformance remainder, but the probe must reconcile
the reward-routing overlap (PR #39 pinned audited reward routing as payload INTENTS
inside the encounter contract, host's audited workflow op sole writer per Q-0186) and
the sequencing collision (both slices live under claim-first `games/shared/**`).
Section claimed first (`claims/superbot-games-host-seam-probe.md`), claim cleared
before merge. Close-out fills outcomes below.

**📊 Model:** fable-5 · high · docs-only (probe report + heartbeat + card; no code)

## 💡 Session idea

A **foreign-order dependency token in the Sequence grammar**: this probe's blocking
dependency is another repo's inbox order (superbot-next ORDER 002 item 4), expressible
today only as prose inside the `> **Sequence:**` body. Bless a machine-readable token
form — e.g. `after superbot-next#ORDER-002` — that `check_ideas.py` recognizes, and the
manager's nudge list falls out of lint: one grep surfaces every idea in the tree blocked
on a given foreign order, exactly the fan-in the :30 sweep currently reassembles from
heartbeat prose. Grooming-round-3 seed; pairs with the PR #41 card's post-verdict
state-grammar gap.

## ⟲ Previous-session review

PR #42 (open-work preflight sweep) turned the ls-remote sibling-branch recipe into the
always-run `preflight --open-work` advisory — this session benefits directly: the
branch-time sweep is one command, not a remembered incantation, and its
unconditionally-exit-0 design means the advisory cannot red a docs-only probe branch.
PR #39 (encounter-contract probe) set the exemplar this card mirrors and did one thing
this session leans on hard: it probed against LIVE state rather than the capture's
snapshot, catching that the capture's headline ask had partially shipped — the same
move here catches that this capture's "seams exist only as prose" claim is now slightly
stale (the encounter seam has executable shape @ `b134961`). One honest observation:
PR #39's Q8 fence ("host wiring stays in their own slices") is exactly what makes this
probe non-twin, but neither its report nor the heartbeat fan-in note named WHO owns the
host seam's shape — this probe has to settle that ownership question explicitly.

## Outcomes

Verdict: **park(build-direct — sequenced)** — no reproducible-evidence question for
sim-lab (the uncertainty is contract OWNERSHIP and timing, settled by routing): the
seam's shape is superbot-next's ORDER 002 item 4 to define, so a games-invented stub
today would be a second source of truth guessing the host's shape — the buildable slice
is a schema-MIRROR host stub + package conformance test in superbot-games AFTER the
host's contract doc lands, bundled BEHIND the PR #39-routed encounter-contract slice on
the same claim-first `games/shared/**` path and gen-2 boot, its fake reward seam
deferring to (never redefining) that contract's payload-INTENTS rule. State advanced
forward-only captured → parked; blessed Grounding ×2 (superbot-games @ `b134961`,
manifest row: behind — the datapoint-ELEVEN staleness persists; superbot-next @
`c3f7a02`) + a Sequence line pinning the ordering; capture's "seams exist only as
prose" honestly flagged as partially stale (the encounter seam is executable @
`b134961`). NO proposal appended (outbox stays at 5, all pulled). Claim
`claims/superbot-games-host-seam-probe.md` taken first commit, cleared in the close-out
commit. Preflight (6 checks) + `python3 bootstrap.py check --strict` green before push;
landed per README § Landing conventions (PR READY, merge-on-green).

## Handoff → next wake

Inbox first (verified empty at origin/main `528f045` at branch time). The
superbot-games section is now FULLY probed-or-parked on its captured heads except
`ci-collection-parity-guard` and `gen2-boot-pack-kit-upgrade-lane-adopt` — both
gen-2-boot-adjacent, and this probe's Sequence finding (one `games/shared/**` claim,
ordered slices, all riding the same externally-fired boot) is direct input to either.
Manager fan-in for this verdict is on the heartbeat: nudge superbot-next ORDER 002
item 4 (or extract a minimal manifest-types pre-slice), then bundle the host-seam stub
behind the encounter-contract slice. Other ripe heads unchanged from the PR #43
handoff: websites probe heads, check_harvest output-refinement bundle, grooming
round 3 (now three seeds: freshest-wins, post-verdict state grammar, this card's
foreign-order dependency token).
