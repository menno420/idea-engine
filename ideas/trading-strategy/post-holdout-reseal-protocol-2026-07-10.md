# Post-holdout re-seal protocol — pre-register the NEXT holdout before the current one is spent

> **State:** parked(overtaken-by-events — P5 ran 2026-07-10T16:47Z before any pre-registration could land; successor protocol is owner-gated per p5-holdout-protocol §6 and carried by the lane's own paper-lane standing mission)
> **Class:** process · **Target:** `menno420/trading-strategy`
> **Grounding:** https://github.com/menno420/trading-strategy@e713abb125766db2b1562980369a11290b8772b9 · fetched 2026-07-10T21:32Z (manifest row: behind)
> *(pin annotation: capture pin; re-checked live @ d0fc23b23969256df4bc9c4104b7d523ef6b3495 same fetch; manifest-row detail: superbot@655e0fe row still reads "ORDER 007 … in flight; holdout SEALED" — lane reality is 008 done, holdout SPENT)*
> **Sequence:** before trading-strategy ORDER 008 (P5 one-shot evaluation) — **EXPIRED**: P5 executed 2026-07-10T16:47Z (run stamps `20260710T1647*`, lane PR #37, merge `ffdd6f6`) before this probe ran; the constraint can no longer be met.

## Problem

The lane's single most valuable asset — its pre-registered one-shot holdout
(`HOLDOUT_START = 2025-01-09`, code-enforced at the loader and both ledger choke
points) — is about to be consumed: ORDER 008 (P0, Q-0262.2) authorizes the P5
evaluation now that ORDER 007's significance bar is done, and the manifest row shows
that exact 007→008 sequencing live. The moment P5 runs, every committed bar is
consumed data. The repo has **no doctrine for what becomes the next holdout** —
QUEUE.md's next-session brief says "No other undone roadmap items" — so the first
post-P5 experiment would either touch unsealed data or stall the lane.

## Idea

Pre-register the successor holdout **before** P5 executes, in the same
write-the-verdict-rules-before-the-numbers style as `docs/p5-holdout-protocol.md`:
new `HOLDOUT_START` = the current committed data end; caches extended forward only
under the new seal; the existing rails (the `load_ohlcv` filter, the
`data_end < HOLDOUT_START` ledger refusal, the CI audit over `experiments/index.jsonl`
— all already parameterized per `docs/holdout-enforcement.md`) re-pointed at the new
boundary in one PR. The protocol doc, not the code, is the deliverable: unlock
conditions, minimum accrual period before any future unlock, and how post-P5
subjects re-enter the pipeline.

## Grounding

- Manifest trading-strategy row: "holdout SEALED … with unlock ORDER 008 landed @ fd5e9fe (Q-0262.2, sequences AFTER ORDER 007); ORDER 007 … in flight"
  ([superbot @ `6f283b9`](https://raw.githubusercontent.com/menno420/superbot/6f283b91160546af2864a0fd30b6e2d81b148a8f/docs/eap/fleet-manifest.md), fetched 2026-07-10).
- Lane reality @ [`e713abb`](https://github.com/menno420/trading-strategy/tree/e713abb125766db2b1562980369a11290b8772b9):
  `control/status.md` (007 DONE, 008 acked-not-executed, "NEXT: ORDER 008 … FRESH dedicated session"),
  `docs/succession/QUEUE.md` item 8 + next-session brief ("No other undone roadmap items"),
  `docs/holdout-enforcement.md` (the rails to re-point).

**Why now:** pre-registration only counts before the numbers exist — the window to
seal the successor holdout closes the moment the ORDER 008 session runs P5.

## Probe report (v0, 2026-07-10)

*Probed 2026-07-10T21:35Z against the capture pin (lane @ `e713abb`) AND a live re-check at
lane HEAD `d0fc23b` — the re-check is the probe's decisive input. Timing first, per the
capture's own "Why now": the idea's entire value proposition was a window, and the window
is closed. Lane status @ `d0fc23b` (updated 2026-07-10T21:08:05Z): "holdout: **SPENT.**
The one-shot was consumed 2026-07-10 (run stamps 2026-07-10T1647Z)" — ORDER 008's P5
evaluation ran and merged (PR #37, merge `ffdd6f6`) roughly one hour BEFORE this capture's
probe could even be dispatched. Every judgment below reckons with that fact.*

**1. What is this really?**
A race that has already been lost, wrapping a doctrine slice that mostly survives. The
capture proposed two things: (a) a timing act — seal the successor holdout BEFORE P5
consumes the current one, so pre-registration "counts"; (b) a mechanism — a protocol doc
plus one PR re-pointing three already-parameterized rails (`load_ohlcv` filter, ledger
`data_end` refusal, CI audit — `docs/holdout-enforcement.md` @ `e713abb`) at a new
`HOLDOUT_START`. Part (a) is dead: P5 ran 2026-07-10T16:47Z. Part (b) is a spec a lane
session could still execute — but it is a protocol to adopt, not a hypothesis a simulator
can test; there is nothing here for sim-lab even in the revived case.

**2. What is the possibility space?**
Three axes, all now conditioned on post-P5 reality. **What the successor seal protects:**
a new backtest holdout at the evaluated-window end (the capture's proposal) vs a forward
paper-trading protocol on genuinely-new bars (what the lane actually chose: status @
`d0fc23b` names the paper lane its standing mission, "no holdout re-use, ever") vs no
successor at all. **Unlock conditions:** minimum accrual period, owner gate, how post-P5
subjects re-enter — `docs/p5-holdout-protocol.md` §6 already pre-answers the frame:
"Follow-on research would require genuinely new data (post-2026 bars accruing beyond the
evaluated window) and a new pre-registered protocol — an owner decision, out of scope
here." **Who consumes it:** the sibling capture `cross-sectional-momentum-family-2026-07-10.md`
(first post-holdout hypothesis class) is the only named future customer for a new
evaluation seal.

**3. What is the most advanced capability reachable by the simplest implementation?**
In the revived (owner-authorized) case: one PR re-pointing `HOLDOUT_START` to the
evaluated-window end + one protocol doc yields pre-registration-by-construction for every
future hypothesis class — the rails are already parameterized per
`docs/holdout-enforcement.md`, so the marginal cost is a constant change, a test-pin
update, and prose. It would also convert the spent window (2025-01-09 → 2026-07-10) into
legally loadable dev data through the normal path — today those bars are still
loader-locked for everything except the P5-only unlock kwarg.

**4. What breaks it?**
- **Timing — already broken.** The capture's "Why now" said the window closes the moment
  the ORDER 008 session runs P5; that happened 2026-07-10T16:47Z (PR #37 / `ffdd6f6`),
  before this probe. Pre-registration of a successor *before* the spend can no longer
  happen; a doc written now is post-hoc by the capture's own standard.
- **Superseded by the lane's own doctrine.** Status @ `d0fc23b` sets the standing mission
  as the paper lane — a NEW pre-registered protocol for forward paper-trading of the
  RULE-PASS candidate, owner-gated — which occupies exactly the "what comes after the
  holdout" slot this idea wanted to fill, with a stronger answer (forward data cannot be
  peeked at by construction).
- **The feared failure mode did not materialize.** The capture worried post-P5 work would
  "touch unsealed data or stall the lane" — in fact the rails still lock every bar
  ≥ 2025-01-09 by default (the unlock kwarg was scoped to the P5 session only, per
  protocol §7 and the enforcement contract), so nothing is leaking while no successor seal
  exists. Urgency was real for pre-registration optics, not for leakage.
- **Accrual math.** A successor backtest holdout sealed at the evaluated end protects zero
  usable evaluation bars until months of new data accrue (and the ~35-month moving hourly
  floor, protocol §4, erodes hourly windows from behind). Not measured: the minimum
  accrual any future evaluation would need — that is precisely what a successor protocol
  doc would have to pre-register.

**5. What does it unlock?**
If revived at owner direction: an evaluation seal for the sibling cross-sectional-momentum
family (which needs a portfolio-level engine extension first — see its capture), plus
dev-data access to the spent 2025-01-09→2026-07-10 window through the normal loader path.
Nothing is blocked today by its absence: the lane is green, its next work (paper-lane
protocol) is already named, and the old rails still prevent leakage.

**6. What does it depend on?**
An owner decision, explicitly: protocol §6 reserves the follow-on-research call ("an owner
decision, out of scope here"), and the lane's ⚑/orders surface shows no ORDER commissioning
a successor backtest holdout — the post-008 inbox is empty of newer orders (status @
`d0fc23b`: "no order newer than 008"). Mechanically it depends only on the existing
parameterized rails (all shipped, `docs/holdout-enforcement.md`). It also now depends on
NOT colliding with the paper-lane protocol the lane names as its standing mission — two
competing "what comes next" doctrines would be worse than one.

**7. Which lane should build it?**
`menno420/trading-strategy` itself, and only on an owner ORDER — the rails, the binding
docs, and the pre-registration culture all live there; idea-engine can only capture and
route. Not sim-lab: there is no hypothesis here, only a protocol to adopt (spec, not
simulation).

**8. What is the smallest shippable slice?**
Today: none that honors the idea — the pre-P5 slice no longer exists, and a post-hoc
"reseal now" PR would pre-empt an owner call that protocol §6 explicitly reserves and the
paper-lane mission may moot. If the owner ever authorizes new backtest research (e.g. the
cross-sectional-momentum family), the slice is exactly the capture's mechanism: one PR —
new `HOLDOUT_START` = the P5-evaluated data end, test pin updated, caches extended forward
under the new seal — plus the successor protocol doc with pre-registered unlock conditions
and minimum accrual.

**Recommendation: park** — the P5 run (2026-07-10T16:47Z, lane PR #37/`ffdd6f6`) closed the
pre-registration window before this probe; the surviving mechanism is owner-gated per
p5-holdout-protocol §6 and the lane's paper-lane standing mission already occupies the
successor slot — revive only if the owner authorizes a new backtest holdout.
