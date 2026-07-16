# Round-robin domain rotation starves the deepest backlog

> **Status:** `proposed` — round-18 fleet-backlogs opener (standing ORDER 003 · rotation slot per ORDER 004 rule 3). Adjudication: sim-lab VERDICT 098.
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
