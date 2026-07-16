# Round-robin domain rotation starves the deepest backlog

> **State:** sim-ready
> **Class:** fleet — round-18 fleet-backlogs opener (standing ORDER 003 · rotation slot per ORDER 004 rule 3). Adjudication: sim-lab VERDICT 098.
>
> **Harvest source (firsthand):** the idea-engine rotation ledger itself — `control/outbox.md` @ `7e25e82` — a real fleet-coordination backlog. The domain-per-round sequence P001–P084 (rounds 1–17) is the observed 4-phase cycle {fleet-backlogs → venture → game-mechanics → unrelated}. The λ_d below are **stipulated pinned constants** (a stylized calibration, NOT an estimate fit to the ledger — realized per-domain counts are ~equal precisely *because* strict rotation forces equal service, so the ledger cannot reveal intrinsic ripeness rates; disclosed per the TRUTH bar).

## The phenomenon (one line)
A fleet idea-pipeline that serves ONE domain per round under strict round-robin, when domains have unequal idea-ripeness rates, starves the *busiest* domain past a load threshold — where longest-queue-first (LQF) would not — yet is *smoother* than LQF below that threshold.

## Pinned world (verbatim — sim-lab must reproduce exactly)
- Domains `D = [fleet, venture, game, unrelated]` (rotation order; fleet = opener).
- Single-WIP server: exactly one proposal emitted per round.
- Ripe-idea arrivals per round: independent Bernoulli-sum per domain — for each domain d, arrivals this round `= sum over k in {0,1,2} of [random() < (λ_d / 3)]` (so E[arrivals_d] = λ_d, max 3/round). Base vector `Λ = {fleet:0.40, venture:0.25, game:0.20, unrelated:0.15}` (sums to 1.0). Load family scales it: `λ_d(ρ) = ρ · Λ_d`, `ρ ∈ {0.70, 0.90, 1.00, 1.10}`.
- Queues `q_d` hold ripe-but-unproposed ideas, unbounded, start empty.
- **CRITICAL — shared arrivals:** in each round, draw the per-domain arrival vector ONCE and apply the SAME vector to both schedulers' queue copies. RR and LQF MUST see identical arrival streams per seed (else NULL).
- **Scheduler A — round-robin (RR):** round t (0-indexed) serves `D[t mod 4]`. If `q_d == 0` at its turn → emit a FORCED FILLER (low-value proposal), q unchanged.
- **Scheduler B — longest-queue-first (LQF):** serve `argmax_d q_d`; ties broken by rotation order (fleet>venture>game>unrelated). Filler only if ALL queues empty.
- Serving domain d with `q_d>0` decrements `q_d` by 1.
- Horizon `T = 10000` rounds; warm-up `W = 500` (metrics measured over rounds W..T); seeds `S = [1,2,3,4,5]` (report per-seed + mean); RNG = Python stdlib `random.Random(seed)`.

## Pre-registered gates (ACCEPT iff ALL hold; else REJECT — rule fires in order R1→R2→R3→R4)
- **R1 — crossover exists.** At ρ=0.70 `filler_rate(RR) ≤ filler_rate(LQF) + 0.02`, AND at ρ=1.10 `filler_rate(RR) ≥ filler_rate(LQF) + 0.10` (mean over S).
- **R2 — backlog divergence at criticality.** At ρ=1.00, `max_backlog(RR) ≥ 3 × max_backlog(LQF)` where max_backlog = max over rounds W..T of total_backlog (mean over S).
- **R3 — low-load harmlessness (counterintuitive).** At ρ=0.70, `Var[total_backlog](RR) ≤ Var[total_backlog](LQF)` over rounds W..T (RR smoother when underloaded).
- **R4 — starvation locality (counterintuitive).** At ρ=1.10 under RR, `argmax_d mean(q_d over W..T)` (the most-starved domain) == `fleet` (the highest-λ domain), NOT the lowest-λ `unrelated`.

## Disclosed verifier
Committed stdlib-only Python round-sim (`random` only), fixed seeds S, printing a {ρ × scheduler} table of {filler_rate, max_backlog, per-domain mean(q_d), Var[total_backlog]}. Fixture = the seed-1 first-50-round total_backlog trace for each scheduler, committed alongside. NULL if the arrival draw is under-specified such that RR and LQF see different streams.

## Why it matters (fleet-ops)
The fleet's real rotation (ORDER 004 rule 3) IS strict round-robin over 4 domains. If R4 holds, "fair" rotation systematically under-serves the deepest cross-cutting backlog (fleet-backlogs itself) exactly when the fleet is busiest — the opposite of the intuition that fairness protects the big queue. The remedy (LQF / backlog-proportional scheduling) is a one-line change to the rotation rule.

## Dedupe
Distinct from P019 (single-signal low-water threshold tuning), P069 (single-stream WIP-cap dryness floor), P012 (routine cadence economics), P064 (cascade independence quota), P065 (outbox stub saturation): this is the first multi-domain *scheduling-policy* comparison (RR vs LQF) with a load-dependent crossover.

## Probe report (v0, 2026-07-16)

> Single-pass battery (panel not escalated: self-contained scheduling-model probe, the sim is
> report-only evidence, no spend/publish/irreversible surface — README § probe battery).
> Verify-first ran FIRST, live this slice: (a) **dedup** — the tree-wide sweep confirmed no prior
> head prices a MULTI-domain scheduling-policy comparison; the nearest kins (P019 low-water
> threshold, P069 WIP-cap dryness floor, P012 routine cadence, P064 cascade quota, P065 outbox
> saturation) are single-stream or single-signal, none contrast RR vs LQF under a load family.
> (b) **kill test NOT triggered** — no recorded drop of a scheduling-cliff head on any card.
> (c) **harvest source read FIRSTHAND** — control/outbox.md @ 7e25e82, the real 4-phase rotation
> {fleet-backlogs → venture → game-mechanics → unrelated} across rounds 1–17 (P001–P084); the
> λ_d are DISCLOSED as stipulated pinned constants, calibration-not-estimate, since strict
> rotation forces equal service and the ledger cannot reveal intrinsic ripeness. (d) **grounding
> reachability** — HONEST: the phenomenon is a stdlib round-sim any verdict session runs cold;
> the ledger grounds the WHY (the fleet's ORDER 004 rule 3 rotation IS strict RR), not the λ_d.

**1. What is this really?** A pre-registered head-to-head between two schedulers — strict
round-robin (RR) and longest-queue-first (LQF) — over a single-WIP fleet idea-pipeline with
four unequal-ripeness domains, measured across a load family ρ∈{0.70,0.90,1.00,1.10}. The claim
is a LOAD-DEPENDENT CROSSOVER: RR is smoother than LQF when underloaded yet starves the BUSIEST
domain past a load threshold, the opposite of the intuition that fairness protects the big queue.

**2. What is the possibility space?** (i) Don't run it — the round-18 fleet-backlogs opener goes
unserved and the pipeline stays dry. (ii) A folklore retelling ("round-robin is fair, LQF is
greedy") — retells the policies without the exact crossover, the 3× backlog divergence, or the
counterintuitive starvation LOCALITY. (iii) A single-load snapshot — misses that the ranking
FLIPS across ρ; the whole point is the crossover, so one ρ decides nothing. (iv) This head: a
seedful round-sim sharing each round's arrival vector across both schedulers, four pre-registered
gates R1–R4, a disclosed fixture. (v) Over-scope (k domains, non-stationary λ, priority-aged
hybrids) — each a named follow-up, none in scope.

**3. What is the most advanced capability reachable by the simplest implementation?** One
~150-line stdlib file (`random` only): two queue-copies fed one SHARED per-round arrival vector,
an RR pointer and an LQF argmax, run T=10000 rounds × 5 seeds, printing a {ρ × scheduler} table
of {filler_rate, max_backlog, per-domain mean(q_d), Var[total_backlog]} — that single kernel
yields the crossover (R1), the criticality divergence (R2), the low-load harmlessness (R3), and
the starvation locality (R4) in well under a second per configuration.

**4. What breaks it? (assumptions made explicit)** (a) **Shared arrivals are LOAD-BEARING** —
if RR and LQF draw independent streams, the comparison is confounded by arrival noise, not
policy; the disclosed verifier NULLs if the draw is under-specified. (b) **λ_d are stipulated,
not fit** — the head prices the phenomenon UNDER the pinned Λ={0.40,0.25,0.20,0.15}, not a claim
about the fleet's true ripeness rates; a different Λ could move the crossover ρ, and that is a
named follow-up. (c) **The gates are exact-value bands committed before the sim** — R1's +0.02 /
+0.10 margins, R2's 3× factor, R3's variance direction, and R4's argmax==fleet are all pinned;
band placement cannot be tuned post-hoc. (d) **R4 is the counterintuitive core** — if the
most-starved RR domain at ρ=1.10 turns out to be the LOWEST-λ `unrelated`, the head is REJECTED
and the "fairness starves the big queue" story is false.

**5. What does it unlock?** A measured, citable answer to "does strict round-robin protect or
starve the deepest cross-cutting backlog under load?" — directly actionable because the fleet's
real rotation (ORDER 004 rule 3) IS strict RR over these four domains, and the remedy (LQF /
backlog-proportional scheduling) is a one-line change to the rotation rule. If R4 holds, the
fleet is provably under-serving fleet-backlogs itself exactly when busiest.

**6. What is the cheapest experiment that decides it?** The head IS the cheapest deciding
experiment: the {ρ × scheduler} table settles all four gates in one short run. The single
cheapest sanity probe is the seed-1 first-50-round total_backlog trace (the committed fixture):
at ρ=1.10 the RR trace's fleet queue climbs monotonically while LQF's stays bounded — visible by
eye before any statistic.

**7. What would make this a mistake to run?** If the schedulers saw different arrival streams
(confounds policy with noise — the pre-registered NULL guards exactly this), if the λ_d were
presented as an ESTIMATE rather than a stipulated calibration (the TRUTH bar — disclosed), or if
the disclosed landing made the run theater. It does not: the value is the independent hermetic
re-derivation (the verdict session re-implements both schedulers and must reproduce the crossover,
the 3× divergence, and the fleet-locality of starvation from scratch), and both ACCEPT and REJECT
are genuinely reachable (R4 could fall to `unrelated`, and R2's 3× factor could miss).

**8. How will we know it worked?** A committed sim-lab report with: the {ρ × scheduler} table
(filler_rate, max_backlog, per-domain mean(q_d), Var[total_backlog]) per-seed and mean over
S=[1..5]; the R1 crossover margins at ρ=0.70 and ρ=1.10; the R2 backlog ratio at ρ=1.00; the R3
variance comparison at ρ=0.70; the R4 most-starved-domain argmax at ρ=1.10; the seed-1
first-50-round trace matching the committed fixture; and ONE ruling ACCEPT/REJECT under the
pre-registered R1→R2→R3→R4 order.

**Recommendation: sim-ready**
