# Parallel-session heartbeat reconcile — the one-writer rule's blind spot, codified

> **State:** captured
> **Class:** process · **Target:** `menno420/substrate-kit`

## Problem

The coordination protocol's conflict-freedom rests on "one writer per file" — which
holds across Projects but **not within one**: a lane running parallel slices (the
Q-0265 continuous-chaining mode this repo operates under) has N in-flight branches
that each end with a `control/status.md` overwrite. This repo hit the collision
repeatedly on one day: PR #15's branch had to `git merge origin/main` mid-flight and
hand-reconcile the heartbeat after siblings #13/#14 landed (merge commit 25b26b2);
PR #12 pre-wrote a predicted PR number that turned out wrong and needed a fixup
commit (7ce1607); and successive stamps landed out of order against wall-clock
(21:40Z/22:25Z stamps on commits that landed 20:31Z/20:44Z — recorded in the 20:55Z
heartbeat). The reconcile recipe is proven but *oral* — nothing the kit plants warns
a second parallel session, and nothing checks the result.

## Idea

Codify the discipline in the kit, cheapest teeth first: (1) the planted
`control/README.md` gains a "parallel sessions, same lane" section — forward-only
reconcile on conflict (`git merge origin/main`, recommit a heartbeat that keeps BOTH
sides' facts, rerun the full preflight), never pre-write facts you don't have yet
(PR numbers, merge shas). (2) The status checker learns two advisories it can verify
mechanically from git history: a non-monotonic `updated:` stamp (newer commit,
older timestamp) and a heartbeat that *lost* a sibling's `last-shipped`/orders facts
across a merge (the reconcile-dropped-facts failure). (3) Optionally later: a
`bootstrap heartbeat` helper that regenerates the file from structured fields so
reconciliation is a field-merge instead of prose surgery. The one-writer rule stays
the contract; this covers the case the contract never named.

## Grounding

- Live collisions in this repo: PR #15 (merge commit 25b26b2, sibling fold recorded
  in its message), PR #12 heartbeat-number fixup (commit 7ce1607, "created as #12,
  heartbeat predicted #11"), and the timestamp-sequence note in `control/status.md`
  @ 03ae14d — all `menno420/idea-engine` git history.
- The rule with the blind spot: planted `control/README.md` § "The one rule that
  keeps it conflict-free" (two *Projects* never touch the same file — same-Project
  parallel sessions do).
- Continuous mode as the new normal: README § Coordination (owner ruling 2026-07-10,
  Q-0265) — every lane that adopts chained slices inherits this collision shape.

**Why now:** gen-2 lanes are arming standing wakes fleet-wide (manifest @
[`dc19b1e`](https://raw.githubusercontent.com/menno420/superbot/dc19b1e8a5443101a1a4cadf9a2f4e65133f49a3/docs/eap/fleet-manifest.md),
post-launch note) — parallel-session heartbeat collisions stop being an idea-engine
quirk the moment a second lane chains slices.
