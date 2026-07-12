# Routine-cadence economics sim — replay the seat's own wake trail, price every wake policy

> **State:** sim-ready
> **Class:** process · **Target:** `menno420/sim-lab` (verification target per the Q-0264
> pipeline; the verdict routes to the manager/owner — the buildable artifact is a
> one-file stdlib simulator sim-lab can run and any lane can re-run)
> **Grounding:** https://raw.githubusercontent.com/menno420/fleet-manager/171e24fefd6c75116915acaa0736932ad676f05b/docs/owner-queue.md@171e24f · fetched 2026-07-12T14:16Z
> *(pin annotation: fm live HEAD = `171e24fefd6c75116915acaa0736932ad676f05b` by
> `git ls-remote` 2026-07-12T14:13Z; the pinned queue's sitting bundle
> `id: OQ-SITTING-0714-DECISIONS` carries, verbatim at line 589, "**post-EAP routine
> posture** — HARD deadline: decide **≤2026-07-13**; RECOMMENDED **Option A**." —
> the live owner decision this sim's output prices. Option A's content, from this
> repo's own heartbeat @ `42f9642`: "core-6 Projects keep current cadence (per
> Q-0261), every other standing cron drops to daily, one-shots expire on completion".)*
> **Sequence:** before the ≤2026-07-13 owner sitting (fm owner-queue
> `OQ-SITTING-0714-DECISIONS` item 4, post-EAP routine posture — the sim's verdict is
> useful after the deadline too, fleet-wide, but its highest-leverage consumer decides
> tomorrow)

**Origin:** generated this slice from the seat's own operating record — the first ~14h
of the merged coordinator seat left a complete, commit-pinned wake/trigger/catch trail
in `control/status.md` history, and the fleet is about to hand-pick a routine posture
(Option A recommended) with zero measured latency/cost numbers behind it.

## The idea (reasoned to its fuller form — Q-0254 duty)

Every fleet coordinator seat wakes three ways: a **failsafe cron** (this seat: live
`0 */2 * * *` — a 2-hourly deadman, explicitly "not the work cadence" per the Q-0265
continuous-mode ruling, README § Coordination @ `139932e`), a **pacemaker send_later
chain** (~15-min self-re-arm while work is open, paused when the queue drains — the
honesty guard), and **event-driven wakes** (webhook/PR activity — free but partial:
nothing webhooks this seat when a foreign repo appends an ORDER to an inbox file).
Each wake costs real tokens: a pacemaker re-arm burns ≈ one worker turn, a failsafe
sweep ≈ one recon worker (cost proxies, as-given — see Q4). Each policy buys signal
latency: how long a filed trigger sits uncaught.

The fragment "should the failsafe be 2h or 30m?" reasons out to a fuller, better
question: **wake policy is a 3-axis point (failsafe cadence × chain policy ×
event-wake coverage), the fleet is choosing one by intuition tomorrow, and this seat
accidentally recorded exactly the calibration corpus a deterministic replay needs.**
The first ~14h of this seat is 13 heartbeat overwrites on `control/status.md`
(`fc0bab6` #220, first wake 2026-07-12T00:05:51Z → `531b109` #258, the 12:00Z sweep —
`git log fc0bab6..531b109 -- control/status.md`, run this slice), each recording the
wake, its trigger, and what it caught. Real, commit-pinned datapoints:

- **sim-lab ORDER 003**: fm-filed 08:30Z, caught and executed at the 10:00Z failsafe
  sweep (`65cd284` #256; done-when evidence merged 10:31:24Z per `531b109` line 10) —
  **~90 min arrival-to-catch latency** under the 2h failsafe.
- **fm 8-seat restructure**: merges landed 03:15–03:28Z, and the signal was priced at
  the 06:0x failsafe sweep (#253 honest-null reconcile, recorded @ `38f8857`) —
  **~2.5–3h latency**.
- **Pacemaker chain**: alive and re-armed every turn while the queue had work —
  verified alive at `42f9642` (#224, committed 00:34Z, next fire 00:43Z, "15-minute
  send_later chain") and still alive at `d7c74d1` (#245, next fire 02:54Z) — then
  **paused under the honesty guard** once the queue drained (`0fd8b65` #252,
  re-declared `f92bd26` #257). Roughly a 00:3xZ–02:5xZ verified-alive window
  (endpoints beyond that not independently verified).
- **A live spec-vs-live mismatch already flagged**: the v3.2 failsafe-prompt spec says
  cron `30 1-23/2 * * *` vs live `0 */2 * * *` (RESIDUAL FLAG, `control/status.md` @
  `531b109` line 10, deliberately held for cutover alignment) — evidence the fleet is
  already editing cadence values without a pricing instrument.

The sim: a **seeded discrete-event replay-and-sweep**. Input: a trigger-arrival trace
T (the real ~14h corpus reconstructed from the heartbeat history above, plus seeded
synthetic Poisson/burst variants to break the n=1 dependence) with each arrival tagged
by visibility class (webhook-visible vs inbox-only). Policy grid G: failsafe-only at
2h/1h/30m; failsafe-2h + 15-min pacemaker-chain-while-work-open; event-driven-only;
hybrid (event + failsafe-2h). Cost model C: 1 worker-turn per chain re-arm, 1
recon-worker per failsafe sweep, ~0 marginal per webhook wake. Output per grid cell:
{wake count, worker-turn cost, median/p95 catch latency, missed-window count} → a
cost/latency frontier and a dominance table. Generalization: the fleet runs many
cron+chain seats — fm trigger telemetry counted 783 triggers in the snapshot @ fm
`4111da4` (as-given, not verified; the locally-quoted gen #5 roster @ fm `7c13be7`
recorded "324-record export, 32 enabled: 15 standing crons + 2 poke-only + 15
one-shots", quoted in
[`../superbot/usage-limit-aware-routines-2026-07-10.md`](../superbot/usage-limit-aware-routines-2026-07-10.md)'s
probe pins) — so the frontier prices not just this seat but the standing-cron
population Option A would demote to daily.

## Probe report (v0, 2026-07-12)

> Single-pass battery (panel not escalated: process head, reversible, no
> security/data/spend/public blast radius — README § probe battery). Verify-first,
> run live this slice: (a) the corpus EXISTS and is replayable — 13 `control/status.md`
> commits in `fc0bab6..531b109`, each a wake record with trigger + catch facts
> (`65cd284` 10:00Z sweep + ORDER 003 same-wake execution; `38f8857` 06:0x sweep +
> restructure pricing; `42f9642`/`d7c74d1` chain-alive; `0fd8b65`/`f92bd26`
> chain-paused); (b) the consuming decision is LIVE — fm owner-queue @ `171e24f`
> line 589, "post-EAP routine posture — HARD deadline: decide ≤2026-07-13; RECOMMENDED
> Option A"; (c) the doctrine layer is pinned — Q-0265 continuous-mode ruling in
> README § Coordination (@ `139932e`), failsafe = deadman not work-cadence; (d) the
> fleet already touches cadence values blind — the v3.2 `30 1-23/2` vs live `0 */2`
> mismatch stands as a residual flag @ `531b109`.

**1. What is this really?** A pricing instrument for wake policy — for the
manager/owner deciding routine posture (a live ⚑ decision, deadline ≤2026-07-13), and
generalizing to every cron+chain-woken seat in the fleet. It converts "how often
should seats wake?" from intuition ("more wakes = fresher but pricier" — obvious,
directionless) into a measured frontier: worker-turns per caught trigger vs p95 catch
latency, per policy, on this fleet's actual arrival pattern.

**2. What is the possibility space?** (i) Do nothing — the posture decision lands on
recommendation-by-feel, and the next cadence edit (the v3.2 cron alignment is already
queued) also lands unpriced. (ii) Analytic note only — for pure Poisson arrivals and
cron-interval I, expected catch latency is ~I/2 and cost ∝ 1/I; closed-form, no sim.
This dies on exactly the parts that matter: the chain policy's cost depends on the
open-work duty cycle, event wakes cover only webhook-visible arrivals (ORDER 003
arrived inbox-only), and dominance between MIXED policies has no clean closed form.
(iii) The captured shape — a seeded discrete-event replay over real-trace + synthetic
variants and the 6-policy grid, single stdlib file, deterministic, swept. (iv) A live
telemetry loop — instrument every seat's wakes fleet-wide and tune continuously;
manager territory, an order of magnitude more machinery, and (iii) tells us whether
it's worth it. Value peak is (iii).

**3. What is the most advanced capability reachable by the simplest implementation?**
One afternoon of stdlib code yields a dominance table over the whole policy grid —
including the two decision-changing outputs intuition cannot produce: a **knee** (the
cadence beyond which extra wakes buy ~no latency because arrivals cluster around
fleet-active hours) and any **strictly dominated policy** (e.g. failsafe-30m dominated
by hybrid at every tested trace — which would retire a whole option from the posture
debate). The same run re-prices Option A itself: what "drop every non-core cron to
daily" costs in p95 catch latency on the observed arrival classes.

**4. What breaks it? (assumptions made explicit)** (a) **Cost-proxy accuracy** — "1
worker-turn per re-arm, 1 recon-worker per sweep" is as-given, not measured; the fm
economics doctrine records that actual token/dollar costs are NOT agent-visible (the
honest-nulls rule, quoted in the usage-limit-aware-routines probe pins @ fm
`7c13be7`), so the sim's cost axis is in worker-turn UNITS, and a verdict must state
that unit honestly — relative dominance survives unit error, absolute
"tokens-per-trigger" does not. (b) **Arrival representativeness — n=1, stated
plainly**: the real corpus is ONE seat's first ~14h (a fleet-restructure night, likely
busier than steady state); the seeded Poisson/burst variants are load-bearing, not
decoration, and any verdict holds only across all variants or says so per-variant.
(c) **Webhook wakes are free-but-partial** — they miss inbox/ORDER-file arrivals
(ORDER 003 is the live proof); if the fleet later adds a push channel for inbox
writes, event-driven-only's coverage changes and the sim must be re-run with the new
visibility tags. (d) The honest kill test on sim-worthiness itself: if the frontier
comes out smooth with no knee and no dominated policy, the sim's answer IS the
intuition restated — that outcome is possible, cheap to discover, and the verdict
would still retire the question with evidence instead of feel.

**5. What does it unlock?** The ≤2026-07-13 posture decision gets a number where it
currently has a recommendation; the queued v3.2 cron alignment (`30 1-23/2` vs
`0 */2`) gets priced instead of pattern-matched; the manager gets a reusable
instrument for every future cadence edit across the standing-cron population (15
standing crons at gen #5; 783-trigger telemetry as-given @ fm `4111da4`); and the
honesty-guard pause policy (chain only-while-work-open) gets tested against
always-chain and never-chain instead of being doctrine-by-default.

**6. What does it depend on? (cheapest confirm/kill, priced)** Nothing unshipped: the
corpus is committed git history in THIS repo (verified, SHAs above), the policy grid
is doctrine already written down (Q-0265 + the trigger grammar), and the runtime is
stdlib. Cheapest confirm evidence — already in hand this probe: two real
arrival→catch latency datapoints (90 min; ~2.5–3h), a verified chain-alive window
with per-turn re-arm cost, and a live consuming decision. Cheapest kill evidence
would be either (a) fm already publishing a wake-economics analysis — not found in
the fetched owner-queue @ `171e24f`, and the fm economics doctrine's honest-nulls
rule says cost cells are "not measurable", i.e. nobody has priced this; or (b) the
posture decision being already executed — the queue item says decide ≤2026-07-13,
still open at fetch time. Neither kill fired.

**7. Which lane should build it — and what does it displace or duplicate?** sim-lab
runs it (it is exactly sim-shaped: deterministic, seeded, swept, with a falsifiable
one-question output); the manager consumes the verdict. Duplicates nothing, swept by
name this slice (`rg` over ideas/ for cadence/cron/trigger/wake/routine/pacemaker/
heartbeat/polling/economics): nearest neighbor is
[`../superbot/usage-limit-aware-routines-2026-07-10.md`](../superbot/usage-limit-aware-routines-2026-07-10.md)
— parked(routed) INTO the same ≤07-13 owner decision, but it is the limit-aware
deferral MECHANISM (detect/defer/report); this head prices the CADENCE choice —
complementary inputs to one decision, zero mechanism overlap.
[`../superbot/recon-cadence-boundary-jitter-2026-07-10.md`](../superbot/recon-cadence-boundary-jitter-2026-07-10.md)
guards one lane's recon-marker jitter, not policy economics;
[`../superbot/external-cron-trigger-for-routines-2026-07-10.md`](../superbot/external-cron-trigger-for-routines-2026-07-10.md)
and [`../trading-strategy/wake-resilience-fresh-session-rebind-2026-07-10.md`](../trading-strategy/wake-resilience-fresh-session-rebind-2026-07-10.md)
are scheduler/binding RELIABILITY, orthogonal to cadence choice;
[`carried-watch-verdict-inheritance-guard-2026-07-12.md`](carried-watch-verdict-inheritance-guard-2026-07-12.md)
and [`coordinator-archive-handoff-ceremony-2026-07-11.md`](coordinator-archive-handoff-ceremony-2026-07-11.md)
govern heartbeat CONTENT and trigger DISPOSITION, not wake frequency;
[`open-work-preflight-sweep-2026-07-10.md`](open-work-preflight-sweep-2026-07-10.md)
is a per-wake advisory (a cost COMPONENT the model can price, not a chooser);
[`../superbot-next/parity-flip-cadence-2026-07-10.md`](../superbot-next/parity-flip-cadence-2026-07-10.md)
is a work-output cadence rule, different axis. Relation to the v3.2/v3.3
stateless-prompt cadence specs: the live `30 1-23/2` vs `0 */2` mismatch
(`control/status.md` @ `531b109`) is a CONSUMER of this sim's output — alignment at
cutover should pick the priced value, not whichever spec wins by seniority.

**8. What is the smallest shippable slice?** One stdlib Python file (~200 lines) in a
sim-lab intake dir: parse a trace file (the real corpus transcribed from the
heartbeat SHAs above, arrivals tagged webhook-visible/inbox-only) + a seeded
synthetic-trace generator; simulate the 6-policy grid; emit one CSV/markdown table of
{policy × trace-variant → wakes, worker-turns, median/p95 latency, missed windows} and
a one-line dominance verdict. No network, no state, reproducible from the seed.

**Recommendation: sim-ready** — the corpus is real and commit-pinned, the consuming
decision is live with a hard deadline, and the output (knee + dominance table, or an
honest "no knee, frontier is smooth" null) changes what the manager can say tomorrow
in a way intuition cannot. THE ONE QUESTION for the simulator: *Given trigger-arrival
trace T (the real ~14h corpus reconstructed from idea-engine `control/status.md`
history `fc0bab6..531b109`, each arrival tagged webhook-visible vs inbox-only, plus
seeded Poisson/burst variants) and cost model C (1 worker-turn per pacemaker re-arm,
1 recon-worker-turn per failsafe sweep, ~0 marginal per webhook wake — units stated
as worker-turns, not tokens), which policy in grid G = {failsafe-2h, failsafe-1h,
failsafe-30m, failsafe-2h + chain-15m-while-work-open, event-driven-only,
hybrid(event-driven + failsafe-2h)} minimizes worker-turns per caught trigger subject
to p95 catch-latency ≤ 2h, and is any policy strictly dominated across all trace
variants?* Done-when: the per-cell table + dominance verdict + a stated per-variant
sensitivity note on the n=1 real trace.
