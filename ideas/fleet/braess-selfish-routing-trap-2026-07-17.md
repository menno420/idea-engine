# Adding a free A→B shortcut lane to a congested 4-node routing network makes every selfishly-routed task SLOWER, not faster: under greedy lowest-latency routing the zero-cost shortcut is a dominant strategy that overloads both congestible legs, lifting the equilibrium mean latency from 1.5 to ~2.0 (Braess's paradox); the harm is a monotone dose-response in the shortcut's OWN latency s that decays to zero above an interior threshold s*, and a social-optimum router minimizing TOTAL latency simply refuses the shortcut — proving the loss is a pure artifact of selfish routing, not of the added capacity

> **State:** sim-ready
> **Class:** fleet (pipeline rotation — the standing ORDER 003 COMPLETELY-UNRELATED-domain slot, round 20 CLOSER; domain: NETWORK ROUTING / CONGESTION GAMES — Braess's paradox and selfish (Wardrop) routing, outside fleet/venture/game. fleet→venture→GAME→unrelated per ORDER 004 rule 3 — the prior pipeline slices served fleet (P089), venture (P090), game (P091), so the unrelated closer is next. Adjudication: sim-lab VERDICT 105 (+13 offset).)
> **Target:** sim-lab (verification target menno420/sim-lab per the Q-0264 pipeline; routing is the manager's per Q-0260, this repo never edits sim-lab files; P092 → V105)
> **Grounding:** https://github.com/menno420/idea-engine@5bf0bb4313772ce3281cbf811c66cb8c7e02fce6 · fetched 2026-07-17T06:59:49Z
> **Harvest source (firsthand):** Braess's paradox core statement read FIRSTHAND — https://en.wikipedia.org/wiki/Braess%27s_paradox · fetched 2026-07-17T06:29:42Z — "Adding one or more roads to a road network can slow down overall traffic flow through it." The normalized 4-node unit-latency network gives closed 1.5 → open 2.0 (pure-Nash), confirmed analytically in the dry-sim self-checks.
> **Origin:** standing ORDER 003 (continuous new ideas per repo) under the deliberate lane rotation (rule 3, "COMPLETELY UNRELATED domains — I want those too"); round 20 unrelated closer.

**Placement note (decide-and-flag):** this fleet-external pure-mechanism head lives in `ideas/fleet/` per the `check_sections` carve-out for cross-cutting heads (the P088 Berkson precedent) — the mechanism is domain-general routing theory, not a fleet-lane content idea; it edits no other repo, builds/publishes/spends nothing.

## The folk belief
More capacity helps. If a network is congested, adding a fast link — a shortcut, an extra lane, a fresh server — can only reduce travel time, or at worst leave it unchanged. "Give the busy path an escape valve and everyone moves faster." Applied to a fleet: add a fast shared lane and greedy dispatch will use it to drain the backlog.

## The mechanism (reasoned to its fuller form — Q-0254 duty)
Take the canonical 4-node network: source S, sink T, two middle nodes A and B. Four legs carry unit demand of N agents from S to T:
- S→A latency = x (congestible: cost rises with the fraction x of agents on it),
- S→B latency = 1 (fixed),
- A→T latency = 1 (fixed),
- B→T latency = x (congestible),
and a shortcut A→B with latency = s (a tunable constant; s=0 is the classic free shortcut).

Without the shortcut there are two routes: "up" S→A→T (cost x_SA + 1) and "down" S→B→T (cost 1 + x_BT). Selfish equilibrium splits the demand 50/50, so x_SA = x_BT = 0.5 and every agent pays 1.5.

Open the free shortcut and a third route appears: "cross" S→A→B→T (cost x_SA + s + x_BT). At s=0 an agent on "cross" pays x_SA + x_BT, and from any state it weakly beats both other routes — so "cross" is a dominant strategy and every agent migrates to it. But then x_SA = 1 (everyone uses S→A) AND x_BT = 1 (everyone uses B→T), so the "cross" cost climbs to 2.0. The unique selfish equilibrium pays 2.0 — worse than the 1.5 they paid before the shortcut existed. Adding a strictly-helpful-looking free link made everyone slower. That is Braess's paradox.

The fuller form has three moving parts worth pinning:
1. **It is a dose-response, not a knife-edge.** Give the shortcut its own latency s>0 and the migration weakens: at large s nobody wants "cross" and the paradox disappears. So excess latency (open minus closed) is a monotone decreasing function of s with an interior threshold s* above which the fast lane stops hurting. The harm is worst when the shortcut is fastest.
2. **It is a selfishness artifact, not a topology artifact.** The added edge never *removes* options — the old routes still exist. A planner minimizing TOTAL latency has the open network's strictly-larger strategy set, so its optimum can only match or beat the closed network. It refuses the shortcut. The loss lives entirely in the gap between selfish (Wardrop/Nash) routing and the social optimum — the price of anarchy.
3. **Finite-temperature realism.** Real dispatchers aren't perfectly sharp. Model choice as a logit/quantal response with inverse-temperature β: an agent picks route i with probability ∝ exp(−β·cost_i). As β→∞ this recovers the pure-Nash 2.0; at finite β the equilibrium sits a little below (soft response leaks some flow off "cross"), but the paradox sign and its magnitude survive across a wide β band.

## Pinned world (committed constants — sim-lab must reproduce exactly)
- Network: nodes {S, A, B, T}; legs S→A cost = x_SA, S→B cost = 1, A→T cost = 1, B→T cost = x_BT, shortcut A→B cost = s. x_SA = (n_up + n_cross)/N, x_BT = (n_down + n_cross)/N.
- Routes: up = S→A→T (cost x_SA + 1); down = S→B→T (cost 1 + x_BT); cross = S→A→B→T (cost x_SA + s + x_BT), available only when the shortcut is OPEN.
- Agents N = 1000. Inverse temperature β = 12.0. Damped-logit revision protocol: each round, every agent revises with probability α = 0.10; revisers are reassigned across the available routes by logit probabilities ∝ exp(−β·cost) evaluated at the current fractions; non-revisers stay (the damping is required — full synchronous resampling oscillates in this anti-coordination game, while damped revision relaxes to the logit quantal-response fixed point, independent of α).
- Rounds R = 120; the per-seed statistic is the mean realized latency averaged over the last 30 rounds.
- Seeds: N_SEEDS = 30, seed = SEED_BASE + i for i = 0..29, SEED_BASE = 20260719 (a private date-encoded constant; the shared seed-ledger next-free block 20261730 is left UNTOUCHED — the P089/P090/P091 SEEDLESS precedent). Each seed uses `random.Random(seed)`.
- s-grid for R2: s ∈ {0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2}.
- Robustness grid for R3: N ∈ {250, 500, 1000} × β ∈ {6, 12, 24}, all at s = 0.
- Social-optimum router: exhaustive grid search over the route split at step 0.001, minimizing total latency, at s = 0.
- Significance floor SIG = 3.0σ, where σ is the standard error of the reported effect across the 30 seeds. stdlib-only (random, math, json, hashlib; no numpy).

## Probe report (v0, 2026-07-17)
> Single-pass battery (panel not escalated — the mechanism is a textbook result with a closed-form anchor, and the dry-sim reproduces the anchor exactly).

**1. What is this really?** A congestion (routing) game where a strictly-added edge lowers every player's payoff at Nash equilibrium — the canonical price-of-anarchy counterexample. Decision content: greedy lowest-latency dispatch plus a fast shared lane can degrade the whole system.
**2. What would make it false?** If the selfish equilibrium with the shortcut were no worse than without (gap ≤ 0 within noise), or if a social optimizer also suffered, the "selfishness artifact" claim would fail.
**3. Simplest version that still bites?** The 4-node unit-latency network above — the smallest graph exhibiting the paradox, with the exact closed-form anchor closed = 1.5, open = 2.0.
**4. What's the counterintuitive core?** Adding capacity (a free link) makes everyone slower; and the damage is *maximized* when the new link is *fastest*.
**5. Where could I be fooling myself?** Dynamics artifacts — an unstable update rule could manufacture a spurious mean. Guarded by (a) damped revision that provably relaxes to the QRE fixed point, (b) an analytic self-check that the closed equilibrium equals 1.5 exactly, (c) two byte-identical runs.
**6. What's the honest calibration?** At finite β the open equilibrium is ~1.76 (β=12), not the pure-Nash 2.0 — disclosed. The excess decays to zero *from above* as s rises (the soft response never over-corrects into a negative gap), so R2 is a harm-*vanishing* threshold, not a sign reversal; the pure-Nash unused-shortcut threshold is s=0.5, and the empirical noise-band crossing is s*≈1.095. Both disclosed below.
**7. What decision does it change?** Whether to add a fast shared lane / route greedily: the answer is "not without a global objective or a toll," because the fast lane is a Braess trap under selfish routing.
**8. How will we know it worked?** All four pre-registered gates hold in evaluation order on the committed pinned world, byte-identical across two runs.

**Recommendation: sim-ready**

## Pre-registered gates (evaluation order R1 → R2 → R3 → R4; APPROVE iff ALL hold)
- **R1 — the paradox exists.** At s = 0, the selfish-equilibrium mean latency with the shortcut OPEN exceeds the CLOSED mean by ≥ SIG. **Dry-sim:** closed 1.50010 ± 0.00003, open 1.76083 ± 0.00402, gap +0.26072, **355.3σ**. HARD-FAIL if the gap is ≤ 0 or < 3σ.
- **R2 — the harm is a monotone dose-response with an interior threshold.** Sweeping s over the grid, excess(s) = latency(OPEN, s) − latency(CLOSED) is (a) ≥ 3σ positive at small s, (b) monotone non-increasing in s, and (c) drops below 3σ significance at an interior threshold s* strictly inside the grid. **Dry-sim:** excess falls monotonically from +0.26072 (355σ) at s=0 to +0.00008 (2.6σ) at s=1.1 and +0.00000 (0.4σ) at s=1.2; interpolated **s* = 1.095**. HARD-FAIL on any non-monotone step beyond noise, or on any *significantly negative* excess (the QRE must not over-correct).
- **R3 — robustness across scale and sharpness.** Re-running R1 (s=0) across N ∈ {250,500,1000} × β ∈ {6,12,24}, every one of the 9 cells shows OPEN > CLOSED at ≥ 3σ with the same sign. **Dry-sim:** all 9 cells pass; smallest margin 134.9σ (N=250, β=6); gap grows with β (toward the pure-Nash 0.5) and σ grows with N. HARD-FAIL if any cell flips sign or falls below 3σ.
- **R4 — mechanism knockout (social optimum).** Replacing selfish routing with a router that minimizes TOTAL latency at s=0, the OPEN social optimum is ≤ the CLOSED social optimum (gap ≤ 0), and the optimizer places zero flow on the shortcut. **Dry-sim:** social closed = 1.500000, social open = 1.500000, gap 0.000000, optimal split (up,down,cross) = (0.5,0.5,0.0) in both — the paradox vanishes, isolating selfish routing as the sole cause. HARD-FAIL if the social gap is > 0 (that would mean the topology, not selfishness, is to blame).

## Pre-registered decision rule (evaluation order: R1 → R2 → R3 → R4)
- **APPROVE** iff R1 ∧ R2 ∧ R3 ∧ R4 all hold in order.
- **REJECT** on the first HARD-FAIL (name the first-failing gate).
- **NULL** if R1's gap is within ±3σ of zero (the paradox does not register on the pinned world — a calibration miss, not a refutation).
- **INVALID** if determinism fails (the two runs are not byte-identical) or the self-checks do not all pass (the harness is untrustworthy — re-run, do not rule).
Twin evaluators (an ordered R1→R4 if-chain and a table-driven scan) must agree on the verdict token and the first-failing gate; disagreement raises SystemExit.

## Disclosed verifier (the sim-lab spec)
A self-contained stdlib-only module under `sims/verdict-105-braess-selfish-routing-trap/` (no cross-imports, no numpy; imports limited to random, math, json, hashlib, os):
- Pinned constants at file top: `N=1000`, `BETA=12.0`, `ROUNDS=120`, `MEASURE_LAST=30`, `N_SEEDS=30`, `SEED_BASE=20260719` (seeds = SEED_BASE+i), `ALPHA=0.10`, `S_GRID=[0.0,0.1,…,1.2]`, `R3_N=[250,500,1000]`, `R3_BETA=[6,12,24]`, `SOCIAL_STEP=0.001`, `SIG=3.0`.
- `route_costs(n_up,n_down,n_cross,N,s,is_open)` returns the three route costs from current counts; `logit_probs(costs,beta)` is a softmax with a max-shift for numerical safety and infinite cost for the unavailable "cross" route when the shortcut is closed.
- `sample_equilibrium(N,s,is_open,beta,rounds,measure_last,seed,alpha)` seeds `random.Random(seed)`, initializes counts by a uniform split, then each round draws revisers via a seeded binomial (n≤30 exact Bernoulli loop, else a `gauss(μ,σ)` normal approximation clamped to [0,n]) and reassigns them by `multinomial3`; returns the mean realized latency over the last `measure_last` rounds. The per-round fraction-conservation check (counts sum to N) feeds the self-check tally.
- `social_optimum(step,s,is_open)` is an exhaustive grid search over the feasible route split minimizing total latency.
- Emits `results.json` via `json.dumps(…, sort_keys=True, indent=2) + "\n"`; prints the sha256 of `results.json`; runs the whole battery TWICE and asserts byte-identical output; gates exit 0 on ≥ 8 self-checks (fraction conservation on every round plus the analytic anchors: closed Nash = 1.5, all-cross Nash = 2.0, social-open ≤ social-closed, logit probs sum to 1). Issues exactly one APPROVE/REJECT/NULL/INVALID ruling naming the first-failing gate under R1→R2→R3→R4.
- **Disclosed landing:** dry-sim APPROVE. Reference results.json sha256 `d2a893dd82626f3d49e3b8ad7516aafed06fcbf3198bec64af387822bd17a93c` (SEED_BASE=20260719, the exact pinned world above); 118805/118805 self-checks; two byte-identical runs.

## Non-adjacency justification (vs the recent unrelated closers)
Distinct domain and mechanism from every prior unrelated closer: P076 (coding theory / codes), P080 (shared-randomness correlation), P084 (Simpson's paradox — aggregation reversal), P088 (Berkson collider — selection-induced anticorrelation), P089 (M/G/1 queueing — variance-driven SLA), P090 (big-pond badge inversion). P092 is a **congestion game / selfish-routing equilibrium** result: the counterintuitive object is an *added resource lowering global welfare at Nash*, adjudicated by a price-of-anarchy knockout — no selection gate, no aggregation reversal, no queue, no coding bound. The closest neighbor is P089 (also operations-flavored), but P089 prices variance in a single queue while P092 prices strategic route choice across a network; the mechanisms and gates share nothing.

## Dedup
Searched the idea tree (ideas/ across all sections) for prior routing / congestion / Braess / Wardrop / price-of-anarchy heads: none. The fleet lane holds selection/statistics heads (P088) and queueing (P089) but no network-routing game. New head.

## Model basis (declared model-dependence — the P024 discipline)
The claim is model-dependent in the standard, disclosed way: the pure-Nash 1.5→2.0 gap is exact for the pinned unit-latency topology; the finite-β logit equilibrium (~1.76 at β=12) is the realistic softening, and R3 shows the sign is robust across β ∈ {6,24} and N ∈ {250,1000}. The result is a property of *selfish* routing on *this* topology — R4 makes that dependence explicit by removing selfishness and watching the paradox vanish. It does not claim every network exhibits Braess (most do not); it claims this canonical one does, robustly, and that the cause is strategic routing.

## Consequence (pre-registered; routing the manager's per Q-0260 — this repo edits no other repo, nothing here builds/publishes/spends)
If sim-lab confirms APPROVE at V105, the reusable lesson for fleet dispatch: a fast shared lane under greedy lowest-latency routing can be a Braess trap — global throughput can fall when you add it — and the fix is a global objective or a toll (bias dispatch away from the shortcut), not more capacity. Named follow-ups, none in scope: (a) a *toll-calibration* head finding the minimum shortcut penalty that restores the social optimum; (b) a *Braess-detection* head that flags, for a given task-routing graph, whether adding a lane will help or trap.
