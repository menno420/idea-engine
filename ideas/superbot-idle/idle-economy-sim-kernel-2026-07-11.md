# Idle-economy sim kernel — SIM-001 is armed and executable; relay it across the one seam the lane cannot write

> **State:** sim-ready
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

## Probe report (v0, 2026-07-11)

*Single-pass battery per the README panel default (sim-lab VERDICT 002): a relay of an
already-pre-registered numeric spec has no irreversible/high-blast-radius surface, and the
verify-first read below did not disagree with the capture. Verify-first ran FIRST per the
capture's own written duty — the manager's relay could have mooted this head overnight; it
had not (details in Grounding). Every load-bearing claim below was re-fetched live this
probe, not inherited from the capture.*

**1. What is this really?**
A relay, not a design. The lane already did the hard half beyond the games directive §6 ask:
`docs/design/economy-v1.md` @ `f11c71a` pre-registers pacing targets T1–T10 as falsifiable
numbers with acceptance bands, pins seven PROVISIONAL parameters test-enforced against
`idle_engine/economy.py` (`tests/test_economy_design_doc.py` — tune without re-registering
and the suite goes red), and writes SIM-001 to be executable without follow-up questions:
scenarios S1–S3, outputs O1–O6, acceptance criteria A1–A10, driving the REAL engine
functions (deterministic, integer-exact, stdlib-only) at the pinned commit. What's missing
is ONE seam-crossing: SIM-001 is routed only as a ⚑ to the manager ("awaiting manager
relay") while sim-lab's documented intake surface is this repo's outbox (Q-0264.6) — a
surface the lane cannot write itself (Q-0260). The idea = convert SIM-001's committed spec
into a `status: sim-ready` outbox proposal, verbatim in substance, invented in nothing.

**2. What is the possibility space?**
Three routes exist for the crossing: (a) the manager's relay — ⚑'d since lane PR #12,
verified NOT landed at sim-lab HEAD `f70fbea`; (b) sim-lab spontaneously reading the lane's
docs — but its intake contract is explicit ("INTAKE entries … pulled from `menno420/idea-engine`
`control/outbox.md`", sim-lab `control/inbox.md` header @ `f70fbea`), and its own empty-queue
plan names step (a) as "pull the idea-engine outbox at HEAD for any new sim-ready PROPOSAL
beyond 005" (its `control/status.md` § Queue / next slice @ `f70fbea`); (c) this repo's
outbox — the pipeline-designed path. Beyond route choice the space is deliberately EMPTY:
the question, scenarios, outputs, criteria, and verdict semantics are all pre-registered;
inventing a parallel or "improved" ask would fork the lane's pre-registration and weaken the
evidence (the same reason the trading-strategy probe @ PR #51 refused a sim-lab re-run of a
pre-registered protocol). The only degree of freedom worth exercising is fidelity.

**3. What is the most advanced capability reachable by the simplest implementation?**
One append-only outbox entry mobilizes an idle-by-design simulator (queue EMPTY, VERDICTs
001–005 all finalized) against the fleet's first fully-numeric game consumer: a
10-criterion, 6-output, 3-scenario pre-registered parameter sweep whose ALL-PASS graduates
seven provisional parameters PROVISIONAL → SIM-PINNED and unblocks the lane's entire tuning
roadmap. And it is rung-1 cheapest-adequate by construction: no randomness anywhere in the
engine, so a single run per scenario is the distribution's support — the exact shape of
sim-lab's settled gen3/VERDICT-001 precedents, minus even their seeding needs.

**4. What breaks it?**
- **Double-enqueue** — the capture's own named risk: if the manager's relay lands between
  this probe and sim-lab's pull, two intake entries would chase one SIM-001. Verified ABSENT
  at sim-lab HEAD `f70fbea` (ls-remote 03:54:53Z; raw-fetched `control/inbox.md` at that pin:
  INTAKE 001–005 only, all finalized as VERDICT 001–005, plus a manager ORDER 001 about model
  attribution — no SIM-001, no ORDER touching superbot-idle). Residual race is narrow and
  self-healing: sim-lab intake cites source proposals verbatim by number, so a duplicate is
  visible at intake time, and the empty-queue honesty guard (Q-0265) has it reading before
  running.
- **Pin drift** — SIM-001 binds "engine at the pinned commit"; if the lane's HEAD moves
  before the sim runs, the pin could go stale. Mitigated by the lane's own declared policy:
  phase STEADY-STATE HOLD "deliberately holds new engine surface pending … SIM-001"
  (lane `control/status.md` @ `f11c71a`) — the engine freezes itself on exactly this verdict.
- **Scope creep at the simulator** — T10 carries NO criterion (mechanic unimplemented;
  SIM-001's own scope statement: "T10 is out of SIM-001's scope … and carries no
  criterion"); a verdict that rules on T10 would be inventing. The proposal must carry that
  exclusion forward, and does.

**5. What does it unlock?**
The lane's roadmap item 3 ("Economy tuning / parameter graduation — BLOCKED (SIM-001)",
`docs/current-state.md` @ `f11c71a`) and its self-imposed integrity floor (no tuning until
the verdict); parameter graduation PROVISIONAL → SIM-PINNED on ALL-PASS, or an
evidence-named re-registration on ANY-FAIL — either outcome is forward motion where today
there is none. Fleet-level: the pipeline's first fully-numeric game verdict, the exact shape
the games directive §6 named this seat for, and the natural predecessor of the
generator-purchase-path slice (T10's target is already pre-registered waiting for it).

**6. What does it depend on?**
Providing lane superbot-idle @ `f11c71a`, all committed and public-raw reachable (the README
reachability discipline — verified by fetching, this probe: economy-v1.md, control/status.md,
docs/current-state.md all fetched at the pin): the REAL engine functions SIM-001 names
(`tick`/`offline_progress` proven exactly equal, `purchase_upgrade`, `upgrade_cost`,
`prestige_eligible`/`prestige_award`/`apply_prestige`, `build_upgrade_spec`/
`build_prestige_spec`), the seven-parameter provisional table (parity test-enforced), and
the reference-world constants — every input the simulator needs is in the doc at the pinned
SHA. Theme-schema interaction is documented by the same doc and is a NON-dependency worth
stating: themes carry ZERO economy numbers (nouns plus schema-bounded multiplier slots, none
used by any shipped pack; the one legacy theme-side number, `generators[].base_rate` bounded
1–1000, is slated to move engine-side) — the verdict is theme-independent by construction,
so no theme pack blocks or is blocked by it. Consumer side: sim-lab's intake contract +
empty queue, verified live (Grounding).

**7. Which lane should build it?**
sim-lab. Q-0264 makes it the pipeline's reproduced-evidence stage; its queue is EMPTY with a
declared next action of pulling this exact surface ("pull the idea-engine outbox at HEAD for
any new sim-ready PROPOSAL beyond 005" @ `f70fbea`); and SIM-001 is rung-1 numeric
simulation, the cheapest-adequate rung its own intake ladder prefers. Nobody else CAN: the
lane cannot write sim-lab's intake (Q-0260), and the manager relay — the only alternative
writer — has demonstrably not fired. This repo's outbox append is the build.

**8. What is the smallest shippable slice?**
PROPOSAL 006 (this PR): one append-only outbox entry whose question IS SIM-001's own
pre-registered ask (provisional parameters vs T1–T10 per A1–A10) and whose done-when IS the
report format SIM-001 already pins (one results doc per O1–O6 + a verdict row per criterion,
ALL-PASS graduates the table, ANY-FAIL names the break and the margin). Zero new design
surface; the slice ships in the same PR as this report.

### Grounding (probe-time pins — all fetched this probe, 2026-07-11T03:54–03:56Z)

- superbot-idle HEAD **unchanged** at `f11c71a52d4d2adf88b2bf11f5d1134bad495be2`
  (`git ls-remote` 03:54:53Z) — the capture's pin is still live; all lane citations below
  read raw at that SHA.
- Executable request: lane `docs/design/economy-v1.md` @ `f11c71a` — T1–T10 table with
  acceptance bands; seven-parameter PROVISIONAL table; § "Simulation request — SIM-001
  (Q-0264)" (S1–S3, O1–O6, A1–A10, verdict semantics ALL-PASS → SIM-PINNED, T10 excluded);
  parity test `tests/test_economy_design_doc.py` named in its header; themes-carry-no-
  economy-numbers paragraph.
- Stall + hold: lane `control/status.md` @ `f11c71a` — phase "STEADY-STATE HOLD …
  deliberately holds new engine surface pending PLUG-001 … SIM-001"; blockers "economy
  tuning (SIM-001) — … upstream"; § "SIM-001 — ⚑ to manager"; § QUEUE "ON
  HOLD-PENDING-UPSTREAM: economy tuning (SIM-001)" + "SIM-001 + PLUG-001 awaiting manager".
- Blocked roadmap: lane `docs/current-state.md` @ `f11c71a` — item 3 "Economy tuning /
  parameter graduation — BLOCKED (SIM-001)".
- **Verify-first, the decisive read**: sim-lab HEAD `f70fbea1872724f37268d7e95640e93d3b11ab16`
  (ls-remote 03:54:53Z — unchanged since the capture's 03:37Z read); `control/inbox.md`
  raw at that pin: intake = INTAKE 001–005 ONLY, every one finalized (VERDICT 001–005),
  NO SIM-001 relay, no superbot-idle entry of any kind; `control/status.md` at the same
  pin: "QUEUE STATE: EMPTY", next action (a) "pull the idea-engine outbox at HEAD for any
  new sim-ready PROPOSAL beyond 005". The park(routed) branch the capture pre-wrote does
  NOT apply — the relay has not landed anywhere sim-lab reads.
- Pipeline seam: this repo's README § "The outbox" + § pipeline position (Q-0264.6:
  sim-lab direct-pulls `status: sim-ready` entries; Q-0260: lanes write only their own
  repo) — read at this branch's base, origin/main `b13aa36`.

### Sequence

- **after** the verify-first read of sim-lab's live intake @ `f70fbea` (this probe,
  03:54:53Z — no manager relay landed; had it landed, this head's honest verdict was the
  capture's pre-written park(routed) branch and no proposal).
- **before** sim-lab's next outbox pull consumes PROPOSAL 006 — after that pull the
  proposal, not this file, is the live coordination surface; a late manager relay should
  then be reconciled at sim-lab intake (duplicate visible by source citation), not here.

**Recommendation: sim-ready** — the lane pre-registered a falsifiable, executable,
theme-independent parameter sweep (T1–T10 / A1–A10, real engine functions at a pinned
commit) that is exactly reproduced-evidence work, the simulator it needs is idle on an
empty queue with this repo's outbox as its declared next pull, and the only alternative
writer (the manager relay) is verified un-fired — one outbox append closes the seam.
