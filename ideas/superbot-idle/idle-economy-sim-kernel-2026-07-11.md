# Idle-economy sim kernel — SIM-001 is armed and executable; relay it across the one seam the lane cannot write

> **State:** captured
> **Class:** product · **Target:** `menno420/superbot-idle`
> **Grounding:** https://github.com/menno420/superbot-idle@f11c71a52d4d2adf88b2bf11f5d1134bad495be2 · fetched 2026-07-11T03:31Z (manifest row: behind)
> *(pin annotation: "manifest row" reads against the manifest's successor, the fleet-manager GENERATED roster — its superbot-idle row @ fleet-manager `93d3a4d` (gen #4, generated-at 01:58Z) records lane HEAD `97bfff2` 01:49:33Z; live HEAD `f11c71a` is three merged PRs ahead (#43–#45: catalog wave 3 + steady-state heartbeat). Blobless clone at the live pin, ls-remote 03:31:35Z.)*
> **Sequence:** after the lane pre-registers economy params — the §6 arming condition recorded at harvest ("probeable once the idle seat exists and pre-registers economy params"): CONDITION MET at lane PRs #9+#12+#13 — `docs/design/economy-v1.md` pre-registers pacing targets T1–T10 with acceptance bands AND the executable SIM-001 request, parameter parity with `idle_engine/economy.py` test-enforced. The probe window is OPEN.

## Problem

The games directive §6 named idle-economy balance the pipeline's **first fully-numeric
game consumer**: "the idle seat pre-registers economy params → sim-lab verdicts them"
(canonical doc @ superbot `41899e1`, cross-linked in this section's README). The lane
did its half beyond the ask: T1–T10 are falsifiable numbers with bands, and SIM-001 is
written to be executable without follow-up questions — scenarios S1–S3, outputs O1–O6,
acceptance criteria A1–A10, driving the REAL engine functions (deterministic,
integer-exact, stdlib-only) at a pinned commit. But SIM-001 is routed only as a ⚑ to
the manager and sits "awaiting manager relay" (lane `control/status.md` § SIM-001 +
QUEUE; roadmap item 3 BLOCKED, @ `f11c71a`) while sim-lab idles by design on an EMPTY
queue — VERDICTs 001–005 all finalized, declared 30-min idle cadence (sim-lab
`control/status.md` updated 23:50:16Z, read at HEAD `f70fbea`, ls-remote 03:37:05Z;
roster row concurs). Meanwhile every economy parameter stays PROVISIONAL by the lane's
own integrity floor — no tuning until the verdict — and the lane deliberately holds new
engine surface pending exactly SIM-001 (or PLUG-001/orders).

## Idea

Probe this head, and if it holds, mark it sim-ready with an outbox PROPOSAL targeting
sim-lab that **relays SIM-001's own committed spec** rather than inventing a question:
question = "do the provisional parameters hit T1–T10 per A1–A10?"; done-when = the
report format SIM-001 already pins (one results doc per O1–O6 + a verdict row per
criterion, ALL-PASS graduates the table PROVISIONAL → SIM-PINNED). idea-engine's outbox
is the surface sim-lab pulls DIRECTLY on its wakes (README pipeline position, Q-0264) —
the one seam the lane cannot write itself (Q-0260: lanes write only their own repo).

## Grounding

- Executable request + targets: lane `docs/design/economy-v1.md` @ `f11c71a`
  (§ Pre-registered pacing targets · § Simulation request — SIM-001).
- Stall + hold: lane `control/status.md` @ `f11c71a` (§ SIM-001 ⚑ to manager · § QUEUE
  "ON HOLD-PENDING-UPSTREAM: economy tuning (SIM-001)" · phase line "deliberately holds
  new engine surface"); `docs/current-state.md` roadmap item 3 BLOCKED.
- Idle simulator: sim-lab `control/status.md` @ HEAD `f70fbea` (queue EMPTY, 001–005
  finalized); roster row @ fleet-manager `93d3a4d` ("idle-by-design, queue EMPTY").
- The §6 kernel + first-numeric-consumer framing: superbot @ `41899e1` (canonical doc,
  by-link index `../superbot/games-theme-engine-website-first-2026-07-10.md`).

**Why now:** the simulator is idle while its first fully-numeric consumer waits on a
relay; each un-verdicted day keeps seven parameters provisional and the lane's tuning
roadmap blocked. Verify-first at probe time: if the manager's relay (or a sibling
proposal) has already landed in sim-lab's intake by then, this head parks as overtaken
— re-read sim-lab's queue and the lane QUEUE at live HEADs before the battery runs.
