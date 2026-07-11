# Session — single-pass probe: gba-homebrew seeded-cave-runs (section close)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-11 ~09:40Z (worker slice, dispatched by the
> continuous-mode coordinator per Q-0265)

## Scope

The `ideas/gba-homebrew` section's LAST captured head —
`seeded-cave-runs-2026-07-10.md` (thread a run seed through the pure row functions:
infinite caves, seed sharing, per-seed BEST — the concrete "keep investing in Lumen
Drift" option, new scope owner-gated by the concept pick; seeded by PR #17's first
batch). Probed single-pass battery v0. Claim fast-laned first per the ritual —
`control/claims/probe-gba-seeded-cave-runs.md` via PR #148 (squash `8bcd252`, merged
by the enabler ~09:35Z), claims dir re-read at post-claim HEAD: mine is the only
gba-homebrew claim; the #146 lint-bundle claim (ideas/fleet) is disjoint. Branch
`probe/gba-seeded-cave-runs` cut from post-claim main.

## Verify-first (blobless clone at the live pin)

Lane HEAD `c7592d6` (`git ls-remote` 09:29:21Z) — the lane moved a LOT since the
capture pin `bc73da7`: session-8 slices 1–6 + kit v1.8.0→v1.10.0 (lane PRs #28–#37).
Findings that shaped the verdict:

- **NOT overtaken**: zero run-seed anywhere at HEAD — stem-greps (`seed`/`daily`/
  `share`) hit only build-time asset-generator LCGs and one false friend
  (`gl_run_state.h:44` "Seed the best score" — read in the body, SRAM load, no cave
  seed). Lane inbox = ORDERs 001/002/003 only; no new-scope ruling landed.
- **The owner gate is REAL and live**: the concept pick is still the lane's top ⚑
  ("The menu is WITH THE OWNER … An explicit pick still gates the remaining
  sessions") and the lane self-reports IDLE on it ("backlog now empty or
  owner-gated"). Slices 4–6 deepened Lumen Drift (v1.1–v1.3) under the coordinator's
  announced default, then the lane deliberately idled rather than invent scope.
- **Premise mutation recorded honestly**: v1.1's depth tiers fixed the capture's
  difficulty-flatness half (rows 0–123 cell-identical to v1.0; tiers plateau at row
  244); the SINGULARITY half is fully intact — one cave, and the lane's own v1.3
  route-recorder autopilots it byte-identically (the memorization ceiling proven
  mechanically by the lane's own tool).
- **Strengthened since capture**: the row-#23 junction guard (slice 3) is
  CONSTRUCTIVE and pure-per-row — crystal death-gates cannot recur under ANY seed by
  construction; `tools/check-cave.py` full-period scans (rows 0..20405) cost seconds
  per seed; route-recorder makes per-seed replay proofs cheap to record. New wrinkle
  found: GBA carts have no RTC — "daily seed" is a PUBLISHED CODE (the itch.io
  listing's job), not a cartridge feature.
- **Sibling-head upstream outcome** (index-noted): the play-kit park was
  LANE-SELF-SERVED — slice 3 (lane PR #31 `41708da`) committed `dist/lumen-drift.gba`
  + `docs/PLAYING.md` with CI sha256 per lane ORDER 000.

## Verdict

**parked(build-direct — owner-gated new scope)**: the concept pick is the explicit
gate the capture predicted, verified open at `c7592d6`; this head is now the pick's
"keep investing in Lumen Drift" arm fully costed for the ≤2026-07-14 EAP sitting
(one post-pick lane PR: u32 seed as wave-phase offsets with seed 0 = byte-identity,
the lockstep TRIPLE `main.cpp`+`check-cave.py`+`route-recorder.py` moving together,
CI divergence assert + per-seed full-period scan + 64-seed smoke sweep). Nothing
sim-shaped — the only empirical question, per-seed passability, is self-served by
the lane's own `check-cave.py` mirror in its own CI (the #114 precedent, same family
as the #102 shim-replay park). NO outbox proposal; NO new ⚑ owner ask (the pick ask
already lives on the LANE's heartbeat — one ask, one owner surface; the sitting
bundle note in the status ⚑ block gains the pick as a same-sitting item).

**SECTION MILESTONE: gba-homebrew 4/4 probed-or-parked — the TENTH complete
section** (after superbot-games · trading-strategy · superbot-mineverse @ #107 ·
venture-lab @ #110 · superbot-idle @ #116 · pokemon-mod-lab @ #137 · substrate-kit
@ #141 · superbot-next @ #143 · product-forge @ #147 — count verified against the
`control/status.md` sections ledger @ `d213efa`, 9 named + this one; open captured
heads remain in superbot · websites · fleet).

## Verification (real runs, this tree)

Full `python3 scripts/preflight.py` + `python3 bootstrap.py check --strict` run
green immediately before push, after the heartbeat overwrite; pre-push `git fetch
origin main` reconciles any mid-flight sibling forward-only per the README recipe.

**📊 Model:** fable-5 · docs-only (one probe append + state flip + Sequence line +
index re-badge ×2 + section-complete note + card + heartbeat; claim #148 added
pre-build / deleted here; no code, no workflow edits)

## 💡 Session idea

The battery's Reachability-check block covers "where the data lives" and "what a
zero-toolchain surface carries" — this probe adds a third leg: an idea pricing a
TIME-KEYED feature must verify the target platform actually carries a clock. The
capture's "daily seed" silently assumed an RTC the GBA cart does not have; the
honest design (published daily code, owned by the distribution surface) only
appeared once the hardware was checked. Same family: constructive-guard checking —
when probing a "parameterize the generator" idea, check whether the generator's
safety properties are enforced constructively (the row-#23 junction guard: holds
under any seed by construction) or statistically (needs per-seed testing); a
constructive guard collapses what would otherwise look like a sim question.

## ⟲ Previous-session review

Reviewed: `.sessions/2026-07-11-product-forge-final-two.md` (the #147 probe — this
slice's direct predecessor and card template). Its claims verified: (1) PROPOSAL 007
is live in `control/outbox.md` exactly as described (outbox = 7 entries, 007
sim-ready, the depends: line carrying the duplicate-reconcile clause); (2) its
section-complete claim (ninth) checks against the ledger this card's tenth builds
on; (3) its CAPABILITIES wall entry (`*.github.io` proxy-blocked) landed as the
append log's newest entry — honored here by reading the gba lane via ls-remote +
blobless clone, never Pages; (4) its handoff named the lint-bundle build as ripest
LOCAL slice — CONSUMED mid-flight of this very slice: the #146 claim's build PR #149
merged `d8b0425` while this probe was in flight and was forward-merged in, never
rebased (this slice consumed a disjoint section close, per the coordinator's
dispatch). Also
reviewed the dispatch-named `.sessions/2026-07-11-venture-lab-revenue-relay-probe.md`
(#104): its verify-at-live-HEAD-before-probing discipline and its "one ask, one
owner surface" hygiene were both adopted verbatim here (no duplicate ⚑ for the
concept pick); its park stands, un-contradicted by anything this slice read.

## Handoff → next wake

gba-homebrew section CLOSED (tenth). Nothing to route: no proposal (park), no new
owner ask (the pick lives on the lane's heartbeat; the status ⚑ sitting-bundle note
now names it as a third same-sitting item). For the :30 sweep: the manager should
treat the ≤2026-07-14 EAP sitting as carrying THREE bundled decisions — Lumen Drift
itch.io go/no-go (⚑ standing entry) + the pokemon playtest verdicts (fm owner-queue
item 3) + the gba concept pick (lane ⚑, with seeded-cave-runs as the costed "more
Lumen" arm). Ripest LOCAL slice: the lint-bundle build shipped mid-flight as #149,
so the local queue moves to the grooming frontier — the superbot / websites / fleet
open heads, plus the #149 note's websites harvest re-sizing (`d862364→6663e6c`
CHANGED). Sections ledger: 10 of 13 complete; open captured heads remain in
superbot · websites · fleet.
