# When N agents bid to claim a task by their own unbiased-but-noisy estimate of its common value, the highest bid wins — but the winner is precisely the agent whose estimate was the most upward-biased, so committing resources sized to your own signal earns NEGATIVE expected profit despite every estimate being individually unbiased. The cure is an N-dependent order-statistic shading.

> **State:** sim-ready
> **Class:** FLEET-domain (round-23 opener) · multi-agent fleet economics — the winner's curse in a common-value auction (Capen, Clapp & Campbell 1971; Milgrom & Weber 1982)
> **Target:** sim-lab (VERDICT 114, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine@9e8cd78 · fetched 2026-07-17T22:51:57Z
> **Source basis:** E. C. Capen, R. V. Clapp & W. M. Campbell, "Competitive Bidding in High-Risk Situations," J. Petroleum Technology 23 (1971) 641–653 (the original winner's-curse diagnosis); P. Milgrom & R. Weber, "A Theory of Auctions and Competitive Bidding," Econometrica 50 (1982) 1089–1122 (the common-value / affiliation formalization) — standard textbook results; no external repo fetched.
> **Verifier (firsthand):** committed stdlib-only reference sim `ideas/fleet/winners_curse_task_auction.py` (random, math, json, hashlib) — dry-sim exit 0, all gates PASS, results-dict sha256 df79ddf3…b98eb54 (see Verifier + Dry-sim below).

## The phenomenon (one line)
N agents compete to claim a single task whose true value V is COMMON (the same for whoever wins) but unknown; each agent sees an unbiased-but-noisy private signal s_i = V + e_i (e_i i.i.d., mean 0) and the highest signal wins the claim — but the winner is by construction the agent whose noise e_i was the LARGEST of the N draws, so E[e_winner] = E[max of N noises] > 0, and an agent that commits resources sized to its own signal overpays by exactly that order-statistic bias and earns NEGATIVE expected profit even though every individual estimate is unbiased.

## The folk belief
"My estimate is unbiased, so bidding my honest estimate is fair — on average I neither overpay nor underpay." Each agent reasons locally: E[s_i]=V, so "value it at s_i and claim it if I'm the highest bidder" feels like the calibrated, truthful policy. "Bid what you think it's worth" and "the market clears at the best-informed valuation" are the folk expressions. The trap is that this reasoning conditions on the WRONG event: it uses the unconditional E[s_i]=V, but the payoff only lands in the world where you WON, and winning is evidence your signal was the highest of N.

## The thesis (reasoned to its fuller form — Q-0254 duty)
Winning is information, and a naive bidder throws it away. Condition on the event that actually pays you — "I placed the highest bid." Among N agents with i.i.d. mean-zero noise, the winner is the argmax signal, so the winner's noise is not a generic draw but the MAXIMUM of N draws, whose expectation is strictly positive and grows with N. For e ~ Uniform(−w, w) the order statistic is exact:

  E[max of N] = w·(N−1)/(N+1).

If the winner "pays" its own signal s_win = V + e_win (commits resources sized to its estimate), realized profit is V − s_win = −e_win, so

  E[profit_naive] = −E[e_win] = −w·(N−1)/(N+1) < 0.

The bid is individually unbiased yet collectively self-selecting: the auction hands the task to whoever most overestimated it. Two forces sharpen the trap as N rises: (1) more competitors means the winning signal is a higher order statistic, so the upward bias grows toward w; (2) the very agents most likely to win are the ones most fooled. The correction is not "estimate better" — the estimates are already unbiased — but to SHADE the bid by the expected winning-noise: bid b_i = s_i − w·(N−1)/(N+1). Since shading every bid by a constant leaves the winner unchanged (a monotone transform), the winner still pays s_win − shade, and E[profit_shaded] = −E[e_win] + shade = 0: break-even is restored exactly. The counterintuitive core: the fix depends on the number of RIVALS, not on your own signal quality — the more competition, the MORE you must shade, the opposite of the folk instinct that competition disciplines valuations toward truth.

## The formal model (committed constants — sim-lab must reproduce exactly)
- One task with common value V = V_TRUE, shared by whoever wins; agents observe only their own signal, never V.
- Each of N agents draws a private signal s_i = V_TRUE + e_i, e_i ~ Uniform(−W_NOISE, +W_NOISE) i.i.d. (unbiased: E[e_i]=0).
- Highest signal wins the claim and "pays" its bid; bid = s_i − shade.
- Realized winner profit = V_TRUE − (s_win − shade) = −e_win + shade, where e_win = max_i e_i.
- Analytic anchors (uniform order statistics):
  - E[max of N iid Uniform(−w, w)] = w·(N−1)/(N+1).
  - Naive (shade=0) expected winner profit = −w·(N−1)/(N+1).
  - Optimal shading shade* = w·(N−1)/(N+1) → E[profit] = 0 (break-even).
  - Curse deepens monotonically in N: −w·(N−1)/(N+1) is strictly decreasing in N.

## Pinned world (committed constants)
- SEED = 20260717 (proposal-owned; SEEDLESS discipline)
- N_BIDDERS = 8 (agents competing to claim each task — the headline world)
- W_NOISE = 1.0 (signal-noise half-width; s_i = V + Uniform(−1, 1))
- V_TRUE = 10.0 (common task value; agents observe only s_i, never V — profit is invariant to the V level, so V_TRUE only fixes the units)
- N_AUCTIONS = 200000 (independent common-value auctions / Monte-Carlo)
- SWEEP_N = [2, 4, 8, 16] (bidder counts for the "curse deepens with N" sweep)
- SWEEP_AUCTIONS = 50000 (auctions per sweep point)
- Derived: shade* = w·(N−1)/(N+1) = 1.0·7/9 = 0.777778; naive closed-form winner profit = −0.777778.

## Pre-registered gates (all ≥ 3σ unless noted; APPROVE iff ALL hold)
- **G1 — winner's-curse headline:** the naive policy (bid = own signal, shade=0) yields a mean winner profit that is NEGATIVE at ≥ 3σ (mean_naive < 0 and |z| ≥ 3). The winner systematically LOSES despite every individual signal being unbiased.
- **G2 — order-statistic shading cures it:** the shaded policy (bid = signal − w·(N−1)/(N+1)) beats the naive policy by ≥ 3σ AND is not significantly negative (mean_shaded ≥ −3·se_shaded, i.e. break-even or better). The N-dependent shade is the fix, not better estimation.
- **G3 — analytic-anchor MATCH:** the simulated naive mean winner profit matches the closed-form order-statistic bias −w·(N−1)/(N+1) within 3σ: |z| < 3. Confirms the sim implements the process the closed form rests on.

## Pre-registered decision rule
APPROVE iff G1 ∧ G2 ∧ G3 all hold at their stated thresholds on the pinned world with SEED=20260717 and the committed reference verifier. Any gate failing → REJECT (the winner's-curse / order-statistic-shading claim is falsified for these constants). No post-hoc threshold moves; SEED is not changed; margins reported in σ. The bidder-count sweep is disclosed as descriptive corroboration (monotone deepening) and is NOT a gate.

## Dry-sim results (SEED=20260717, verbatim from the committed verifier)
- shade* = 0.777778 (= w·(N−1)/(N+1), N=8) · naive_profit_closed_form = −0.777778
- mean_naive_profit = −0.778285 (se 0.000443) — NEGATIVE despite unbiased signals
- mean_shaded_profit = −0.000250 (se 0.000445) — break-even restored
- **G1 winner's-curse:** z = −1755.27 — PASS (mean_naive < 0, |z| ≫ 3σ)
- **G2 shading-cure:** z_vs_naive = 1238.54 — PASS (shaded beats naive by ≫3σ; mean_shaded = −0.00025 > −3·se = −0.001335, not significantly negative)
- **G3 anchor-match:** |z| = 1.14 — PASS (< 3σ; sim −0.778285 vs closed −0.777778)
- Curse deepens with N (descriptive sweep, mean naive profit vs closed form): N=2 → −0.332540 (closed −0.333333); N=4 → −0.600240 (−0.600000); N=8 → −0.777774 (−0.777778); N=16 → −0.882667 (−0.882353). Monotone deepening = true (each larger N strictly more negative).
- **all_pass = true; exit 0**
- **Disclosed results-dict sha256 = df79ddf35990ae250d096ada20a7f10d1e5320b2f83f49fc551d97415b98eb54**

## Verifier
Stdlib-only python3 (`random, math, json, hashlib` — no numpy), committed alongside this idea as `ideas/fleet/winners_curse_task_auction.py`. Seed once with SEED=20260717. It computes shade* = w·(N−1)/(N+1) analytically, Monte-Carlo simulates N_AUCTIONS=200000 common-value auctions of N_BIDDERS=8 (each auction: draw 8 i.i.d. Uniform(−1,1) noises, the max wins, record realized winner profit) under the naive (shade 0) and shaded (shade*) policies, computes means and standard errors, evaluates G1/G2/G3, runs the descriptive N∈{2,4,8,16} bidder-count sweep, and emits a canonical (sorted-keys, comma/colon-separated) results JSON with its sha256. Exit 0 iff all gates pass.

Reproduce:

```
python3 ideas/fleet/winners_curse_task_auction.py
```

Expected: all_pass=true, exit 0, shade*=0.777778, results-dict sha256 = df79ddf35990ae250d096ada20a7f10d1e5320b2f83f49fc551d97415b98eb54. (Verified deterministic: byte-identical digest across repeated invocations.)

## Why it matters (transferable mechanism)
Any fleet surface where multiple agents bid/vote/self-assign to claim a scarce item of UNCERTAIN COMMON value by their own private estimate inherits this trap: dispatching a task to the seat that estimated it cheapest/most-valuable, routing a lead to the agent most confident it will convert, or letting the highest-confidence model win an ensemble vote — the winner is systematically the most over-optimistic estimator, so realized outcomes run below the winning estimate even when every estimator is calibrated. The transferable audit: whenever a selection rule hands a common-value resource to the extreme (max/min) of many noisy-but-unbiased estimates, the SELECTED estimate is biased by an order-statistic gap that grows with the number of competitors — correct for it by shading the winning bid/commitment by ≈ E[max noise over N rivals] (or equivalently set a reserve / require independent corroboration before committing), and note that the correction scales with the count of RIVALS, not with your own estimate quality. As a fleet-economics head the deliverable is a citable measured verdict plus the "shade common-value claims by the N-dependent order-statistic bias" correction; whether to wire a concrete claim-shading rule into any lane's dispatch/auction is a named follow-up, not in scope here.

## Dedup
Distinct from the nearby priors:
- **kelly-overbet-ruin** (P100): repeated MULTIPLICATIVE self-betting by ONE agent; the trap is the arithmetic-vs-geometric (ensemble-vs-time) mean gap in compounding wealth. This head is a SINGLE-shot MULTI-agent auction; the trap is an order-statistic SELECTION bias (winning is information), with no compounding and no time-average — a different mechanism entirely.
- **shop-reroll-ruin** (P099): single-agent optimal STOPPING with a per-reroll cost. No competing bidders, no common value, no order-statistic-of-rivals bias.
- **friendship-paradox-sensor** (P096): size-biased sampling of a fixed network ("your friends have more friends"). Both are selection-bias heads, but the friendship paradox biases via DEGREE-weighted neighbor sampling on a static graph; the winner's curse biases via the MAX order statistic of competing i.i.d. estimates in an auction — different selection operator, different domain (network sampling vs common-value bidding).
- **braess-selfish-routing-trap** (P092) / **long-chain-flexibility** (P097): congestion-game routing and process-flexibility topology — no private-signal auction, no winner's curse.
- No prior idea in the tree prices a common-value auction, the winner's curse, or order-statistic bid-shading; grep of the full ideas/ tree + outbox history for "winner's curse / common-value auction / order statistic bidding" returns nothing.

## Model basis (declared model-dependence — the P024 discipline)
The curse and the shading cure are robust to the specific constants but DO depend on structural assumptions: (a) the value is COMMON (shared by the winner), not PRIVATE — under independent private values, bidding your value is safe and the curse vanishes; (b) signals are noisy (w>0) and the winner is selected by the extreme (max) signal — a random or signal-blind allocation has no order-statistic bias; (c) the winner bears the realized common value (pays/commits at its bid). The exact −w·(N−1)/(N+1) magnitude is specific to Uniform(−w,w) noise; for other symmetric mean-zero noise the sign and the "deepens with N" monotonicity persist while the constant changes (the order-statistic mean is distribution-specific). The claim is scoped: under a common-value first-price claim with unbiased Uniform noise and max-signal selection, naive own-signal bidding has strictly negative expected winner profit and an N-dependent order-statistic shading restores break-even — demonstrated on the pinned constants, mechanism-explained, not asserted as a universal law.

## Probe report (v0, 2026-07-17)

**1. What is this really?** A common-value-auction winner's-curse claim: with N=8 agents each seeing an UNBIASED noisy signal s_i = V + Uniform(−1,1) of a shared task value and the highest signal winning, an agent that commits at its own signal earns NEGATIVE expected profit (−0.778 in units of the noise half-width), because the winner is the max-noise draw; shading every bid by the order-statistic mean w·(N−1)/(N+1)=0.778 restores break-even.
**2. What would make it false?** If naive own-signal bidding had non-negative mean winner profit (no curse), or if the order-statistic shading failed to lift profit to break-even, or if the simulated naive profit failed to reproduce the closed form −w·(N−1)/(N+1). Any of G1/G2/G3 failing → REJECT.
**3. Simplest version that still bites?** SEED=20260717, N=8 bidders, Uniform(−1,1) signal noise, V=10; 200000 auctions; per auction draw 8 noises, the max wins, score winner profit = −e_win (naive) and −e_win + 0.778 (shaded).
**4. What is the counterintuitive core?** Every estimate is individually unbiased (E[s_i]=V), yet the auction's WINNER is precisely the agent who most overestimated, so conditioning on winning turns a mean-zero error into a strictly positive one — the collective outcome is biased even though no individual is. The needed correction grows with the number of RIVALS, not with your own estimate quality: at N=16 you must shade 0.882, at N=2 only 0.333.
**5. Where could I be fooling myself?** The exact 0.778 magnitude is Uniform-noise-specific; under a different noise law the constant moves (only the sign and monotonicity are law-free). With N=200000 auctions the gate sigmas are enormous (G1 |z|=1755σ, G2 1238σ) so sampling noise is not the risk; the risk is over-reading the specific constant as universal, which the model-basis section scopes. G3 |z|=1.14 confirms the sim reproduces the closed form (not a coincidence of tuning).
**6. What is the honest calibration?** Dry-sim margins at SEED=20260717: G1 winner's-curse z=−1755.27σ (mean_naive=−0.778285 < 0), G2 shading-cure z=1238.54σ (mean_shaded=−0.00025, break-even), G3 anchor |z|=1.14σ (sim −0.778285 vs closed −0.777778) — all clear the ≥3σ bar; exit 0; results-dict sha256 df79ddf3…b98eb54. Descriptive sweep confirms monotone deepening N=2→16 (−0.333→−0.883), each matching its closed form.
**7. What decision does it change?** When a fleet selects among many noisy-but-unbiased estimates by the extreme (dispatch to the cheapest bid, route to the most-confident agent, let the highest-confidence vote win an ensemble), shade the winning commitment by ≈ E[max noise over N rivals] (or set a reserve / require corroboration) before acting — the selected estimate is optimistic by an order-statistic gap that widens with the number of competitors.
**8. How will we know it worked?** The committed stdlib verifier reproduces mean_naive ≈ closed-form −w·(N−1)/(N+1) within 3σ, the shaded policy reaches break-even, and all three gates hold at their thresholds under SEED=20260717, with the results-dict sha256 matching df79ddf35990ae250d096ada20a7f10d1e5320b2f83f49fc551d97415b98eb54.

**Recommendation: sim-ready**
