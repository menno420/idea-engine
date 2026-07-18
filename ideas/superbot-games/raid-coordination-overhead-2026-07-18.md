# PROPOSAL 139 — raid team-size coordination overhead: the Ringelmann DPS cliff. In a co-op raid each added member adds nominal DPS but also imposes coordination overhead (per-member uptime decays with roster size, burst windows collide), so total raid DPS = (Σ base_i)·uptime(N)·(1−collision_loss(N)) PEAKS at a roster size N* strictly SMALLER than the max allowed roster — against an enrage-timer boss a smaller premade out-clears a full stack, and "stack more bodies" is negative-EV past N*.

> **State:** sim-ready
> **Class:** superbot-games · co-op raid composition / group-size diminishing per-capita output (Ringelmann effect)
> **Anchor:** Ringelmann (1913) rope-pull experiments; Ingham, Levinger, Graves & Peckham (1974) — per-member productivity falls with group size through coordination loss + motivation loss
> **Target:** sim-lab (VERDICT 152, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine@23c1ad5 · fetched 2026-07-18T15:50:54Z
> **Reference (external, reachable):** [Ringelmann effect — Wikipedia](https://en.wikipedia.org/wiki/Ringelmann_effect) — verified reachable 2026-07-18 ("the tendency for individual members of a group to become increasingly less productive as the size of their group increases", via coordination and motivation loss)
> **Verifier (firsthand):** `ideas/superbot-games/raid_coordination_overhead.py` · results-dict sha256 `16225c9a8e53cc23cfaa6a5df4b9631e5224d36a80ebada7f1a86546606c9fa3`
> 📊 Model: Claude Opus · high · idea/planning

## The phenomenon (one line)
Total raid DPS is a nominal sum (grows linearly in roster size N) multiplied by two decaying overhead factors — per-member uptime and a burst-collision survival factor — so the product peaks at a roster size N* strictly interior to [1, NMAX]; adding bodies past N* LOWERS total DPS.

## The folk belief
"More raiders = more DPS. Against an enrage-timer boss (a raw-DPS race) always bring a full roster — every extra body is extra damage, so the biggest allowed group is the strongest group." Raid leaders fill to the cap by default.

## The game-design thesis (reasoned to its fuller form — Q-0254 duty)
Model a co-op raid of N members against a single boss. Each member i has a nominal single-target DPS **base_i** (heterogeneous — gear, class, skill). The realized total raid DPS is NOT Σ base_i, because two coordination-overhead terms scale with roster size:

- **Uptime decay.** As the roster grows each member spends more of the fight NOT dealing damage — dodging shared mechanics, repositioning, swapping targets, waiting for their window. Model per-member uptime as **uptime(N) = max(FLOOR, 1 − c·(N−1))**: it starts at 1 for a solo pull and decays linearly (floored) as bodies are added.
- **Burst-window collision.** Cooldowns and burst windows overlap; overlapping damage on the same brief window is partly wasted (overkill, shared debuff caps, mechanic interrupts). Model the surviving fraction multiplicatively as **1 − collision_loss(N) = (1 − q)^(N−1)** — each added member compounds a small waste factor q on the group's effective burst.

So the realized total is

    DPS(N) = ( Σ_{i=1..N} base_i ) · uptime(N) · (1 − collision_loss(N)).

The bracket grows **linearly** in N; uptime(N) and (1−q)^(N−1) **decay**. Their product is single-peaked: at small N the linear gain dominates, at large N the compounding decay dominates, and the maximum lands at an **interior N\* with 1 < N\* < NMAX**. Concretely, with mean base DPS 100, c=0.06 (floor 0.35), q=0.07 and NMAX=8, the mean-model total peaks at **N\*=6** (292.19) and is strictly higher there than at the full roster of 8 (279.19) — a **+13.0 DPS / ~4.7%** deficit for bringing the extra two bodies. Against an enrage timer that is the difference between a clear and a wipe: the six-person premade out-DPSes the eight-stack. "Stack more bodies" is negative-EV past N\*.

## The formal model (committed constants — sim-lab must reproduce exactly)
- Roster sizes N = 1..NMAX, NMAX = 8 (an 8-person raid cap).
- base_i ~ Gamma(shape K=4, scale θ=25) i.i.d. → mean 100, CoV 1/√K = 0.5 (DPS heterogeneity).
- uptime(N) = max(FLOOR, 1 − c·(N−1)), c = 0.06, FLOOR = 0.35.
- Collision-survival factor 1 − collision_loss(N) = (1 − q)^(N−1), q = 0.07.
- DPS(N) = (Σ_{i=1..N} base_i) · uptime(N) · (1 − collision_loss(N)); per trial the same base draw feeds every N (paired) and both the overhead and placebo worlds.
- Deterministic mean-model peak N\* = argmax_N [ 100·N·uptime(N)·(1−q)^(N−1) ] = 6 (pre-registered, computed in code, not hard-coded).
- Monte-Carlo: draw NMAX base values per trial, form prefix sums, evaluate DPS(N) for all N; the paired difference and the per-trial argmax are the estimators.

## Pinned world (committed constants)
- SEED = 20260717
- TRIALS = 20000
- SIGMA_GATE = 3.0
- NMAX = 8; base Gamma(K=4, θ=25) → mean 100, CoV 0.5; c = 0.06; FLOOR = 0.35; q = 0.07
- Mean-model peak N\* = 6; mean-model DPS(6) = 292.1891151059999 vs DPS(8) = 279.18920396191237 (interior peak strictly beats the full roster)
- Interior null proportion p0 = 0.5 (one-proportion z for G2)

## Pre-registered gates (APPROVE iff ALL hold, in order G1 → G2 → G3)
- **G1 — cliff.** With N\* the pre-registered mean-model peak (=6), the paired per-trial difference DPS(N\*) − DPS(NMAX) has Monte-Carlo mean > 0 with z = mean/se ≥ 3σ — the smaller premade STRICTLY out-DPSes the full roster, not by selection but at a fixed pre-registered roster size.
- **G2 — interior peak.** The per-trial argmax roster size N\*_t is strictly interior (1 < N\*_t < NMAX). The fraction of interior trials, tested as a one-proportion z against the null p0 = 0.5, is ≥ 3σ AND the mean-model peak N\* is itself interior. The optimum is an interior team size, not a boundary (neither solo nor full stack).
- **G3 — placebo.** Remove the coordination overhead (c = 0, q = 0): DPS(N) = Σ base_i is monotone increasing, so the interior fraction is 0.0 EXACTLY and the paired mean DPS(NMAX) − DPS(N\*) > 0 with z ≥ 3σ — with no overhead the full roster reliably wins. The interior peak is CAUSED by the overhead terms, not by the Monte-Carlo noise.

## Pre-registered decision rule
APPROVE (sim-ready confirmed) iff G1 AND G2 AND G3 all hold in order and the verifier exits 0 with a reproducible results-dict sha256 across a deterministic double-run. Any gate failing ⇒ REJECT/REVISE.

## Dry-sim results (SEED=20260717, verbatim from the committed verifier)
```
{
  "all_pass": true,
  "g1_cliff": true,
  "g1_mean_cliff_diff": 13.179610112229906,
  "g1_se": 0.21050120075714365,
  "g1_z": 62.61061725455567,
  "g2_interior": true,
  "g2_interior_fraction": 0.8598,
  "g2_n_star_interior": true,
  "g2_p0": 0.5,
  "g2_z": 101.76680794836793,
  "g3_interior_fraction_placebo": 0.0,
  "g3_mean_fullbeats_diff": 199.4478103198337,
  "g3_placebo": true,
  "g3_se": 0.4990879180414521,
  "g3_z": 399.6246014179579,
  "mean_dps_at_n_star": 292.1891151059999,
  "mean_dps_at_nmax": 279.18920396191237,
  "mean_model_dps": {
    "1": 100.0,
    "2": 174.83999999999997,
    "3": 228.33359999999996,
    "4": 263.82909599999994,
    "5": 284.2597637999999,
    "6": 292.1891151059999,
    "7": 289.8516021851519,
    "8": 279.18920396191237
  },
  "n_star": 6,
  "nmax": 8,
  "params": {
    "c_uptime": 0.06,
    "floor": 0.35,
    "k_shape": 4.0,
    "mu_base": 100.0,
    "q_collision": 0.07,
    "theta": 25.0
  },
  "proposal": 139,
  "seed": 20260717,
  "sigma_gate": 3.0,
  "trials": 20000
}
Results-JSON sha256: 16225c9a8e53cc23cfaa6a5df4b9631e5224d36a80ebada7f1a86546606c9fa3
G1 cliff        : PASS (DPS(N*)-DPS(Nmax)=+13.1796, z=+62.61)
G2 interior     : PASS (N*=6, interior_frac=0.85980, z=+101.77)
G3 placebo      : PASS (interior_frac=0.0, full-beats=+199.4478, z=+399.62)
```
Results-dict sha256: `16225c9a8e53cc23cfaa6a5df4b9631e5224d36a80ebada7f1a86546606c9fa3` (deterministic double-run, exit 0 both times).

## Verifier
`ideas/superbot-games/raid_coordination_overhead.py` — stdlib only (`random, math, json, hashlib`). Draws NMAX heterogeneous base-DPS values per trial (Gamma(4,25)), forms prefix sums, evaluates DPS(N) = prefix(N)·uptime(N)·(1−q)^(N−1) across all roster sizes, computes the pre-registered mean-model peak N\* in code, and runs the three ordered z-gates (paired cliff difference at N\*, one-proportion interior z on the per-trial argmax, and a zero-overhead placebo). Emits the whole results dict (no self-referential sha field; the compact canonical serialization's sha256 IS the disclosed digest; stdout dumps the pretty indent=2 view).

## Reproduce
```
python3 ideas/superbot-games/raid_coordination_overhead.py
```
Expected: prints the results JSON, `Results-JSON sha256: 16225c9a8e53cc23cfaa6a5df4b9631e5224d36a80ebada7f1a86546606c9fa3`, three `PASS` lines, exit 0.

## Why it matters (game design)
Roster size is a lever with a sweet spot, not a monotone "bigger is better." Because total output is a linear sum times decaying coordination factors, the DPS-maximizing team is an INTERIOR size — and a game that caps the raid at NMAX but rewards raw clear speed silently punishes leaders who fill to the cap. Design consequences: (1) if you WANT full rosters to be optimal, attack the overhead directly — flatten the uptime decay (fewer forced-movement mechanics, wider burst windows) or the collision term (stagger cooldowns, remove shared damage caps) so N\* rises to NMAX; (2) if you want a genuine size/coordination tradeoff, tune c and q so N\* sits where you want the "ideal" team size; (3) surface effective DPS, not headcount — a roster bar that shows 8/8 hides that the group is past its own peak. Read "we brought more people and cleared slower" as the Ringelmann cliff, not bad luck.

## Dedup
- Distinct from all prior game-lane cards: shop-reroll (optimal stopping), streak-shield (regression), energy-cap (renewal overflow forfeiture), matchmaking-winrate-mirage (Elo compression under SBMM), compounding-reward-inequality (log-normal Gini), PRD proc compression, snipe-clearing-leak (auction microstructure), guild-volunteer-dilemma (N-player public-goods *provision* — a free-rider/participation threshold, symmetric, non-zero-sum; NOT a per-member output-decay curve), pity-anticipation-collapse, rubber-band controller, single-elim favorite-collapse (tournament order statistics), balance-triangle pick-rate inversion (zero-sum matrix equilibrium). None model **per-capita output falling with group size (Ringelmann) / an interior team-size optimum**.
- Closest neighbor is guild-volunteer-dilemma: that is about WHO acts (participation / free-riding in a public good) at fixed group value; this is about how much a group PRODUCES as its size changes (a diminishing-returns output curve with an interior maximum). Different object, different lever (attack overhead vs. attack incentives). This is the FIRST group-size / diminishing-per-capita-output card in the game lane.

## Model basis (declared model-dependence — the P024 discipline)
The interior-peak result is exact for any total of the form (linear sum) × (decreasing factor(s)) whenever the factors decay fast enough to overtake the linear gain before NMAX — here a floored-linear uptime and a geometric collision-survival term. The DIRECTION (an interior DPS-maximizing roster size; adding bodies past N\* lowers total DPS; the effect vanishes when overhead is removed) holds for any positive uptime-decay c and collision waste q with the peak below NMAX. The specific magnitude (N\*=6, ~4.7% deficit at 8) is pinned to (c, q, FLOOR, NMAX) = (0.06, 0.07, 0.35, 8) and mean base 100. Real raids have role composition (tanks/healers/DPS), non-multiplicative mechanic gates, and enrage timers that make the tradeoff a hard clear/wipe threshold rather than a smooth curve; the single-boss raw-DPS model is the minimal object that exhibits the Ringelmann cliff, and adding roles or hard gates only sharpens the penalty for overstacking.

## Probe report (v0, 2026-07-18)

**1. What is this really?** A group-size output identity: total raid DPS(N) = (Σ base_i)·uptime(N)·(1−collision_loss(N)) is a linear sum times decaying coordination factors, so it is single-peaked with an **interior** maximum N\* (1 < N\* < NMAX). It is the game-lane instance of the Ringelmann effect — per-member productivity falls as the group grows. At (c, q, FLOOR, NMAX) = (0.06, 0.07, 0.35, 8) the peak is N\*=**6**, and DPS(6) > DPS(8): the smaller premade out-DPSes the full stack.
**2. What would make it false?** If the paired DPS(N\*) − DPS(NMAX) were ≤ 0 or z < 3σ (G1 fails — the full roster is not actually beaten), or if the per-trial argmax were NOT interior (G2 fails — the optimum sits at a boundary, so "bring everyone" or "go solo" would be right), or if the zero-overhead placebo showed an interior peak (G3 fails — the peak would be a sim artifact, not the overhead). Any of G1/G2/G3 failing → REJECT.
**3. Simplest version that still bites?** SEED=20260717; 8-cap raid, mean base 100, a 6%-per-member uptime decay and a 7%-per-member burst-collision waste already move the DPS-maximizing roster to **6** — bringing the 7th and 8th body drops total DPS ~4.7%, a clear/wipe swing against an enrage timer, with a one-line closed form and no tuning.
**4. What is the counterintuitive core?** "More raiders = more DPS; bring a full roster" is inverted. Because output is a sum scaled by decaying coordination factors, the DPS-maximizing team is a SMALLER interior size, and adding bodies past N\* actively lowers the raid's damage while the roster bar reads "fuller." Effective output is not headcount.
**5. Where could I be fooling myself?** Comparing the per-trial-best roster to the full roster would be selection-biased (the max is always ≥ any fixed size). G1 avoids this by fixing N\* at the pre-registered MEAN-model peak before looking at any trial, so the cliff is an honest paired difference. And G3's placebo is the control: with overhead off the same sim is monotone (interior fraction exactly 0.0), so the peak is caused by the overhead terms, not by Gamma noise or the estimator.
**6. What is the honest calibration?** Dry-sim at SEED=20260717: G1 cliff mean DPS(6)−DPS(8) = **+13.1796**, z = **+62.61** ≥ 3σ; G2 interior N\*=**6**, interior fraction **0.85980** (z = **+101.77** vs p0=0.5) ≥ 3σ; G3 placebo interior fraction **0.0** exactly with full-roster-beats mean **+199.4478**, z = **+399.62** ≥ 3σ; all PASS in order, exit 0; results-dict sha256 **16225c9a…6c9fa3**; two runs byte-identical. G2's interior fraction is 0.86 (not 1.0) because heavy-tailed Gamma draws occasionally push the argmax onto the boundary, but the interior proportion is overwhelmingly above the 0.5 null.
**7. What decision does it change?** Stop defaulting to a full roster on a DPS-race boss. Compute or measure the effective-output curve; either attack the overhead (reduce forced movement / widen burst windows / stagger cooldowns) to push N\* up to the cap, or accept the interior optimum and field N\* bodies. Read a "we brought more and cleared slower" report as the Ringelmann cliff and price roster changes by effective DPS, not headcount.
**8. How will we know it worked?** The committed stdlib verifier reproduces the paired cliff (G1, DPS(N\*) > DPS(NMAX)), the interior-peak proportion (G2, argmax strictly interior), and the zero-overhead placebo (G3, monotone, interior fraction exactly 0.0) at their 3σ bars under SEED=20260717, with the results-dict sha256 matching 16225c9a8e53cc23cfaa6a5df4b9631e5224d36a80ebada7f1a86546606c9fa3.

## One-line design fix
Optimize effective DPS over roster size, not headcount: total output is a linear sum times decaying coordination factors, so the DPS-maximizing team is an interior N\* < cap — either field N\* bodies, or kill the overhead (uptime decay c, collision waste q) so the peak climbs to the roster cap.

**Recommendation: sim-ready**
