# On a favorable repeated bet, "bet bigger for bigger expected value" is a value trap: the growth-optimal stake fraction f* is strictly interior, and the naive double-Kelly overbet (f=2f*) has NEGATIVE long-run growth — the typical gambler goes broke while the ensemble average balloons.

> **State:** sim-ready
> **Class:** UNRELATED-domain (round-22 closer) · information theory / mathematical finance — growth-optimal capital allocation (Kelly 1956) · fleet-external pure-mechanism head
> **Target:** sim-lab (VERDICT 113, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine@a8c10e3 · fetched 2026-07-17T22:00:41Z · J. L. Kelly Jr., "A New Interpretation of Information Rate," Bell System Technical Journal 35 (1956) 917–926 (the log-optimal / geometric-growth criterion)
> **Verifier (firsthand):** committed stdlib-only reference sim `ideas/fleet/kelly_overbet_ruin.py` (random, math, json, hashlib) — dry-sim exit 0, all gates PASS, results-dict sha256 d6e489de…75ad65a5 (see Verifier + Dry-sim below).

## The phenomenon (one line)
In a repeated favorable even-money bet (win probability p=0.6) where you stake a fixed fraction f of your current wealth each round, the arithmetic-mean (ensemble) wealth grows monotonically in f — so an expected-value maximizer wants to bet as much as possible — yet the time-average per-round growth rate g(f)=p·ln(1+f)+q·ln(1−f) peaks at a strictly interior Kelly fraction f*=2p−1=0.20 and turns NEGATIVE past a ruin boundary f_c≈0.389; the naive "double-Kelly" overbet f=2f*=0.40 sits just past that boundary and drives the typical trajectory to zero.

## The folk belief
"This bet has positive expected value, so bet as much as you can — the more you stake, the more you expect to win." The expected value of a single round is maximized by betting everything (E[wealth multiplier]=1+f·(2p−1) is increasing in f), and a naive gambler, a leveraged trader, or an EV-maximizing agent reads that arithmetic mean as the thing to grow. "Double down when you have an edge" and "bet it all on a sure-thing edge" are the folk expressions.

## The thesis (reasoned to its fuller form — Q-0254 duty)
The arithmetic (ensemble) average and the time-average (what a single gambler actually experiences over many rounds) diverge for a multiplicative process, and it is the time-average that governs almost every trajectory. Wealth compounds multiplicatively: after T rounds with W wins, W_T/W_0 = (1+f)^W · (1−f)^(T−W). The per-round log-growth is therefore an average of iid terms, and by the law of large numbers the a.s. growth rate is

  g(f) = p·ln(1+f) + q·ln(1−f)   (q = 1−p).

Maximizing g gives the Kelly fraction f* = p−q = 2p−1 (set g'(f)=p/(1+f)−q/(1−f)=0). Two forces oppose as f rises: (1) a bigger stake magnifies each win's log-gain, but (2) it magnifies each loss's log-drag MORE, because ln is concave and ln(1−f) → −∞ as f → 1. Past f* the loss-drag wins, and past the ruin boundary f_c (the larger root of g(f)=0, here ≈0.389) the time-average growth is NEGATIVE: the median trajectory decays to zero even though the bet has a positive edge. The counterintuitive core: the arithmetic mean E[W_T]=W_0·(1+f·(2p−1))^T is dominated by a vanishingly rare set of all-win paths and keeps climbing with f, so an EV-maximizer chases f→1 straight into certain ruin, while the fraction of paths that actually lose money rises above one-half well before f reaches 1. "Bet bigger for bigger EV" is a value trap; the right objective is the growth rate g(f), whose optimum is strictly interior and well below the naive overbet.

## The formal model (committed constants — sim-lab must reproduce exactly)
- Each round: stake fraction f of current wealth on a favorable even-money bet. Win w.p. p → wealth ×(1+f); lose w.p. q=1−p → wealth ×(1−f).
- After T rounds with W wins, realized per-round growth is G = [W·ln(1+f) + (T−W)·ln(1−f)] / T, with W ~ Binomial(T,p).
- Time-average (a.s.) growth rate: g(f) = p·ln(1+f) + q·ln(1−f).
- Analytic anchors:
  - Kelly optimum f* = 2p−1 (maximizes g; here f*=0.20).
  - g(f*) closed form = p·ln(1+f*) + q·ln(1−f*).
  - Ruin boundary f_c = larger root of g(f)=0 in (f*,1) (time-average turns negative above it).
  - Arithmetic per-round expectation E[W_{t+1}/W_t] = 1 + f·(2p−1), increasing in f (the ensemble grows fastest at f=1).

## Pinned world (committed constants)
- SEED = 20260717 (proposal-owned; SEEDLESS discipline)
- P_WIN = 0.6 (win probability of the favorable even-money bet, p>1/2)
- N_PATHS = 100000 (independent wealth trajectories / Monte-Carlo paths)
- T_ROUNDS = 400 (bets per trajectory / time horizon)
- GRID_STEP = 0.01 (bet-fraction grid resolution for analytic argmax)
- F_UNDER = 0.02 (timid under-bet comparison fraction)
- F_OVER = 0.40 (naive "double-Kelly" overbet = 2·f*; the trap policy)
- F_MAX = 0.90 (near-all-in catastrophic comparison fraction)
- Derived: f* = 2·P_WIN−1 = 0.20 (analytic Kelly, confirmed grid argmax), g(f*) analytic = 0.020136, ruin boundary f_c = 0.389391.

## Pre-registered gates (all ≥ 3σ unless noted; APPROVE iff ALL hold)
- **G1 — overbet-trap headline:** the growth-optimal fraction f* strictly beats the naive double-Kelly overbet F_OVER=2f*=0.40: g(f*) − g(F_OVER) ≥ 3σ, AND the trap fraction has NEGATIVE time-average growth (g(F_OVER)<0) while f* is positive (g(f*)>0). Betting "bigger for bigger EV" ruins.
- **G2 — interior optimum:** g(f*) beats a timid under-bet (F_UNDER=0.02) AND a near-all-in bet (F_MAX=0.90), each ≥ 3σ. Establishes f* is a genuine interior peak, not an endpoint.
- **G3 — analytic-anchor MATCH:** the simulated mean per-round growth at f* matches the closed form g(f*)=p·ln(1+f*)+q·ln(1−f*) within 3σ: |z| < 3. Confirms the sim implements the process the closed form rests on.

## Pre-registered decision rule
APPROVE iff G1 ∧ G2 ∧ G3 all hold at their stated thresholds on the pinned world with SEED=20260717 and the committed reference verifier. Any gate failing → REJECT (the interior-optimum / overbet-ruin claim is falsified for these constants). No post-hoc threshold moves; SEED is not changed; margins reported in σ.

## Dry-sim results (SEED=20260717, verbatim from the committed verifier)
- f_star_grid = 0.2 (= analytic 2p−1) · g_star_grid_analytic = 0.020136 · f_ruin_boundary = 0.389391
- g_star = 0.020134 (se 0.000031) · g_star_closed = 0.020136
- g_under (f=0.02) = 0.003800 (se 0.000003)
- g_over (f=0.40, double-Kelly) = −0.002451 (se 0.000065) — NEGATIVE time-average growth
- g_max (f=0.90) = −0.535935 (se 0.000227)
- Ergodicity gap at F_OVER=0.40: arith per-round mult = 1.08, log10 ensemble-mean wealth after 400 rounds = 13.3695 (≈10^13.4×), median-path wealth = 0.375181 (the typical gambler ends with ~37.5% of stake); fraction of paths that LOSE money = 0.55888 at f=0.40 vs 0.02326 at f*.
- **G1 overbet-trap:** z = 311.63 — PASS (g(f*) ≫ g(0.40); g(0.40)<0<g(f*))
- **G2 interior:** z_vs_under = 519.58, z_vs_max = 2424.85 — PASS (both ≥3σ)
- **G3 anchor-match:** |z| = 0.06 — PASS (< 3σ)
- **all_pass = true; exit 0**
- **Disclosed results-dict sha256 = d6e489de505de1d44a24f0b5164aec83233d8a82fc864dfbb5356c2b75ad65a5**

## Verifier
Stdlib-only python3 (`random, math, json, hashlib` — no numpy), committed alongside this idea as `ideas/fleet/kelly_overbet_ruin.py`. Seed once with SEED=20260717. It computes f* by analytic argmax of g(f) on the GRID_STEP grid (and confirms it equals 2p−1), computes the ruin boundary f_c by bisection, then Monte-Carlo simulates N_PATHS=100000 wealth trajectories of T_ROUNDS=400 rounds each under a single coherent coin stream (the SAME per-path win count drives every evaluated fraction), records per-path realized growth G for {F_UNDER, f*, F_OVER, F_MAX}, computes means and standard errors, evaluates G1/G2/G3, and emits a canonical (sorted-keys, comma/colon-separated) results JSON with its sha256. Exit 0 iff all gates pass.

Reproduce:

```
python3 ideas/fleet/kelly_overbet_ruin.py
```

Expected: all_pass=true, exit 0, f_star_grid=0.2, results-dict sha256 = d6e489de505de1d44a24f0b5164aec83233d8a82fc864dfbb5356c2b75ad65a5.

## Why it matters (transferable mechanism)
Any repeatedly-compounded resource under an EV-maximizing policy inherits this trap: the arithmetic mean is the wrong objective for a multiplicative process, and "bigger stake, bigger expected value" leads to almost-sure ruin despite a genuine edge. The correct objective is the time-average growth rate g(f), whose optimum is strictly interior at the Kelly fraction f*=2p−1 (or, for general odds, edge/odds). The transferable audit: whenever a policy sizes a repeated multiplicative commitment (bet fraction, leverage, reinvestment rate, retry-aggressiveness on a compounding resource) by maximizing the per-step arithmetic expectation, check whether the per-step MEDIAN (geometric/log) outcome is actually positive — if the sizing sits above the ruin boundary f_c, the ensemble average is hiding a typical-case collapse. As a fleet-external pure-mechanism head there is NO lane build here; the deliverable is a citable measured verdict plus the "size multiplicative commitments by geometric-mean growth, not arithmetic EV" correction.

## Dedup
Distinct from the nearby priors:
- **shop-reroll-ruin** (P099): an optimal-STOPPING accept-threshold on iid best-of-K draws with a per-reroll cost — an additive-utility U(tau)=E[M|M≥tau]−C·E[rerolls]. This head is MULTIPLICATIVE wealth compounding with a stake FRACTION, and the trap is the arithmetic-vs-geometric-mean (ensemble-vs-time) gap, not a stopping bar; the "ruin" here is a.s. long-run wealth decay, not reroll overspend.
- **parrondo-losing-games-combine** (P048): two LOSING games alternated into a winning combination (state-dependent switching) — the opposite object. Kelly is a single FAVORABLE game whose optimal STAKE is interior.
- **braess-selfish-routing-trap** (P092) / **friendship-paradox-sensor** (P096): congestion-game routing and size-biased network sampling — different domains entirely.
- No prior idea in the tree prices the growth-optimal betting fraction / log-optimal (Kelly) criterion or the ensemble-vs-time-average divergence; grep of the full ideas/ tree + outbox history returns only a passing "fractional-Kelly ticket counts" note in a casino-fairness file (P-era), not this mechanism.

## Model basis (declared model-dependence — the P024 discipline)
The interior optimum and the overbet-ruin ordering are robust to the specific constants but DO depend on structural assumptions: (a) the process is multiplicative (fixed FRACTION of current wealth staked each round, not a fixed absolute amount); (b) the bet is favorable (p>1/2) with iid rounds; (c) the horizon is long enough for the time-average to dominate. Under an ADDITIVE stake (fixed dollar bet), the arithmetic mean IS the right objective and the trap vanishes. The claim is scoped: under repeated multiplicative (fractional) betting on a favorable iid edge, the growth-optimal fraction is strictly interior at f*=2p−1 and the naive EV-driven overbet has negative time-average growth — demonstrated on the pinned constants, mechanism-explained, not asserted as a universal law.

## Probe report (v0, 2026-07-17)

**1. What is this really?** A log-optimal-growth (Kelly) claim: for repeated fractional betting on a favorable iid even-money edge (p=0.6), the time-average growth rate g(f)=p·ln(1+f)+q·ln(1−f) has a strictly interior maximum at f*=2p−1=0.20, and the naive double-Kelly overbet f=0.40 (which an arithmetic-EV maximizer favors as "bet bigger") has NEGATIVE long-run growth.
**2. What would make it false?** If g(f) were monotone in f (no interior peak), or if f* coincided with/exceeded the overbet bar, or if the simulated mean growth at f* failed to reproduce the closed form g(f*), or if the overbet did NOT have negative growth. Any of G1/G2/G3 failing → REJECT.
**3. Simplest version that still bites?** SEED=20260717, p=0.6, N_PATHS=100000 trajectories of T_ROUNDS=400 rounds; four fractions {0.02, f*=0.20, 0.40, 0.90}; per path count wins ~Binomial(T,p) and score realized growth G=[W·ln(1+f)+(T−W)·ln(1−f)]/T.
**4. What is the counterintuitive core?** The arithmetic-mean wealth E[W_T]=(1+f·(2p−1))^T grows monotonically in f (at f=0.40 the ensemble mean reaches ≈10^13.4× after 400 rounds), yet it is carried by a vanishingly rare all-win minority: 55.9% of individual paths at f=0.40 actually LOSE money, and the median path ends at 0.375× stake. The ensemble grows while the typical gambler is ruined — the arithmetic vs geometric (ensemble vs time) mean gap.
**5. Where could I be fooling myself?** Near f=1 the log-drag and its variance blow up (f=0.90 gives g=−0.536), which could inflate SEs; the pinned comparison fractions and N=100000 keep all gate sigmas far above 3σ (G1 311.63σ, G2 519.58σ/2424.85σ). The result is model-dependent: it needs multiplicative (fractional) staking, a favorable iid edge, and a long horizon.
**6. What is the honest calibration?** Dry-sim margins at SEED=20260717: G1 overbet-trap z=311.63σ (g(f*)=0.020134 vs g(0.40)=−0.002451), G2 interior z=519.58σ (vs f=0.02) / 2424.85σ (vs f=0.90), G3 anchor |z|=0.06σ (g_star 0.020134 vs closed 0.020136) — all clear the ≥3σ bar; exit 0; results-dict sha256 d6e489de…75ad65a5. f*=0.20 = analytic 2p−1; ruin boundary f_c=0.389391.
**7. What decision does it change?** Size any repeated multiplicative commitment (bet fraction, leverage, reinvestment rate) by the geometric-mean growth rate g(f), taking the interior Kelly optimum f*=2p−1 (edge/odds in general) rather than maximizing per-step arithmetic EV — and never stake above the ruin boundary f_c, where a positive-edge bet still decays the typical trajectory to zero.
**8. How will we know it worked?** The committed stdlib verifier reproduces g_sim(f*) ≈ g_closed(f*) within 3σ and all three gates hold at their thresholds under SEED=20260717, with the results-dict sha256 matching d6e489de505de1d44a24f0b5164aec83233d8a82fc864dfbb5356c2b75ad65a5.

**Recommendation: sim-ready**
