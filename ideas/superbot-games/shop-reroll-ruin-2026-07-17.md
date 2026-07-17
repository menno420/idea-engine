# The auto-battler/roguelike habit of "rerolling the shop until you hit a near-perfect item" is a value trap — there is an interior optimal accept-threshold tau*, and greedy near-perfect rerolling (tau=0.95) is strictly worse net-value than accepting at tau*.

> **State:** sim-ready
> **Class:** superbot-games · shop economics · optimal-stopping / accept-threshold design
> **Target:** sim-lab (VERDICT 112, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine · pinned world below · dry-sim SEED=20260717
> **Verifier (firsthand):** committed stdlib-only reference sim `ideas/superbot-games/shop_reroll_ruin.py` (random, math, json, hashlib) — dry-sim exit 0, all gates PASS, results-dict sha256 7d7d7ad8…c662622b (see Verifier + Dry-sim below).

## The phenomenon (one line)
In a shop that shows K=3 items per roll (each item's power ~ Uniform(0,1)) with a per-reroll cost C=0.05, the net-utility-maximizing accept-threshold tau* is strictly interior (≈0.80); "reroll until you see a near-perfect item" (tau=0.95) and "accept whatever the first roll gives" (tau=0) both leave value on the table, and near-always-rerolling (tau=0.99) is catastrophic.

## The folk belief
"Shop rerolls are cheap — keep spinning until you land a top-tier item; a near-perfect item is worth the extra gold." Players (and shop-tuning designers reasoning about player behaviour) treat the reroll button as an almost-free lottery re-draw and push the accept bar as high as they can stomach, chasing item quality without pricing in the accumulating reroll cost and the sharply diminishing quality gain near the top of the distribution.

## The game-design thesis (reasoned to its fuller form — Q-0254 duty)
This is a classic optimal-stopping problem wearing a shop skin. Each roll draws K iid item powers ~ U(0,1); the player keeps the roll's best item M unless M < tau, in which case they pay reroll cost C and roll again. The value of a threshold policy tau is

  U(tau) = E[M_kept] − C · E[rerolls].

Two forces oppose as tau rises. (1) Raising the accept bar raises the quality you eventually keep — but M is already the best-of-K, so its distribution is concentrated near 1 (CDF x^K) and the *marginal* quality bought by a higher bar collapses. (2) Each notch of tau makes acceptance rarer, so E[rerolls] = tau^K/(1−tau^K) climbs — and it diverges as tau→1. Past the peak, the reroll bill grows faster than the quality gain, so U(tau) is single-peaked with a hard INTERIOR optimum tau*. Greedy near-perfect rerolling (tau=0.95) sits on the far, ruinous side of that peak; near-always-reroll (tau=0.99) is worse still (E[rerolls] explodes). The counterintuitive core: because you keep the best of K each roll, the top of the quality distribution is *cheap to reach and expensive to exceed* — chasing the last sliver of item power is exactly where the reroll cost overtakes the quality gain. "Reroll for near-perfect" is a value trap; the right objective is U(tau), whose optimum is strictly below the near-perfect bar.

## The formal model (committed constants — sim-lab must reproduce exactly)
- Each shop roll shows K=3 items, powers iid ~ Uniform(0,1); the roll's value is the best of the K, M = max of K draws.
- Keep M iff M >= tau; else pay reroll cost C=0.05 and roll again. Utility U = M_kept − C · (rerolls performed).
- Best-of-K CDF: P(M <= x) = x^K, so P(accept) = 1 − tau^K.
- Analytic anchors (infinite-horizon threshold policy):
  - E[rerolls] = tau^K / (1 − tau^K)  (geometric count of pre-accept rolls)
  - E[M | M >= tau] = (K/(K+1)) · (1 − tau^(K+1)) / (1 − tau^K)
  - U(tau) = E[M | M >= tau] − C · E[rerolls]; at tau=0, U = K/(K+1).

## Pinned world (committed constants)
- SEED = 20260717 (proposal-owned; SEEDLESS discipline)
- K = 3 (items shown per shop roll)
- C = 0.05 (reroll cost, in item-power units)
- N = 100000 (Monte-Carlo episodes per evaluated policy)
- R_MAX = 500 (hard reroll cap / termination guard; tau<1 ⇒ P(accept)>0)
- GRID_STEP = 0.01 (tau grid resolution for analytic argmax)
- TAU_GREEDY = 0.95 (the "reroll for near-perfect" trap policy)
- TAU_MAX = 0.99 (near-always-reroll comparison policy)
- Derived: tau* = 0.80 (analytic argmax of U on the grid), U(tau*) analytic = 0.854918.

## Pre-registered gates (all >= 3σ unless noted; APPROVE iff ALL hold)
- **G1 — value-trap headline:** greedy near-perfect rerolling (tau=TAU_GREEDY=0.95) is strictly worse than the optimal threshold tau*: U(tau*) − U(0.95) >= 3σ.
- **G2 — interior optimum:** U(tau*) beats accept-first (tau=0) AND near-always-reroll (tau=TAU_MAX=0.99), each >= 3σ. Establishes tau* is a genuine interior peak, not an endpoint.
- **G3 — analytic-anchor MATCH:** the simulated E[rerolls] at tau* matches the geometric count tau*^K/(1−tau*^K) within 3σ: |z| < 3. Confirms the sim implements the process the closed form rests on.

## Pre-registered decision rule
APPROVE iff G1 ∧ G2 ∧ G3 all hold at their stated thresholds on the pinned world with SEED=20260717 and the committed reference verifier. Any gate failing → REJECT (the interior-optimum / value-trap claim is falsified for these constants). No post-hoc threshold moves; SEED is not changed; margins reported in σ.

## Dry-sim results (SEED=20260717, verbatim from the committed verifier)
- tau_star = 0.8
- U_star = 0.854837 (se 0.000293) · U_star_analytic = 0.854918
- U_zero (tau=0) = 0.750851 (se 0.000612)
- U_greedy (tau=0.95) = 0.676363 (se 0.001021)
- U_max (tau=0.99) = −0.632192 (se 0.005251)
- rerolls_star = 1.04947 (se 0.004612) · rerolls_analytic = 1.04918
- **G1 value-trap:** z = 167.96 — PASS (U(tau*) ≫ U(0.95))
- **G2 interior:** z_vs_zero = 153.35, z_vs_max = 282.75 — PASS (both ≥3σ)
- **G3 anchor-match:** |z| = 0.06 — PASS (< 3σ)
- **all_pass = true; exit 0**
- **Disclosed results-dict sha256 = 7d7d7ad834978e75508c0c645935d6214b97550328d07c19d5b88130c662622b**

## Verifier
Stdlib-only python3 (`random, math, json, hashlib` — no numpy), committed alongside this idea as `ideas/superbot-games/shop_reroll_ruin.py`. Seed once with SEED=20260717. It computes tau* by analytic argmax of U(tau) on the GRID_STEP grid, then Monte-Carlo simulates N=100000 episodes each for tau*, tau=0, TAU_GREEDY=0.95, and TAU_MAX=0.99 (per-episode: draw best-of-K, reroll while M<tau up to R_MAX, record U=M−C·rerolls), computes means and standard errors, evaluates G1/G2/G3, and emits a canonical (sorted-keys, comma/colon-separated) results JSON with its sha256. Exit 0 iff all gates pass.

Reproduce:

```
python3 ideas/superbot-games/shop_reroll_ruin.py
```

Expected: all_pass=true, exit 0, tau_star=0.8, results-dict sha256 = 7d7d7ad834978e75508c0c645935d6214b97550328d07c19d5b88130c662622b.

## Why it matters (game design)
Reroll economics is one of the most-tuned levers in auto-battlers and roguelike shops (TFT, Backpack Battles, Slay-the-Spire-likes). Both the player-facing advice and the designer-facing balance intuition default to "reroll for quality." This proposal says that objective is wrong whenever there is a per-reroll cost and the item pool tops out (best-of-K quality is concentrated near 1): the net-value-optimal accept-threshold tau* is strictly interior and well below the near-perfect bar. Decision rule for a designer or a shop-AI: set the accept-threshold by the utility curve U(tau) = E[M|M≥tau] − C·E[rerolls], measure the reroll cost C and the pool depth K, solve for tau*, and either cap the AI there or price the reroll so the player's greedy bar coincides with tau*. The E[rerolls] = tau^K/(1−tau^K) divergence near tau=1 is the trap that turns "one more spin" ruinous.

## Dedup
Distinct from the nearby game priors:
- **pity-anticipation-collapse** (P091): gacha *pity* dynamics — a hard/soft pity counter that guarantees a drop after N misses; the value distortion is anticipation of a ceiling, not an accept-threshold on iid draws. No reroll-cost / optimal-stopping lever.
- **rubber-band-controller-instability** (P095): a PID/rubber-band feedback controller oscillating around a setpoint; a control-theory instability, not an economics accept-threshold.
- This proposal is **optimal-stopping / accept-threshold economics** — a single-peaked utility over a stopping bar with a per-reroll cost, whose interior optimum sits strictly below the greedy near-perfect bar. Different lever (accept-threshold), different mechanism (best-of-K stopping vs. reroll cost), different math (geometric E[rerolls] divergence vs. gacha pity or PID control).

## Model basis (declared model-dependence — the P024 discipline)
The interior optimum and the tau* < 0.95 ordering are robust to the specific constants but DO depend on structural assumptions: (a) there is a per-reroll cost C>0; (b) item powers are iid within a roll and the kept value is best-of-K (quality concentrated near 1, CDF x^K); (c) the horizon is effectively unbounded (R_MAX only guards termination; tau<1 ⇒ acceptance is almost sure). If rerolls were free (C=0), or item power did not saturate, or the pool were shallow/degenerate, the interior optimum can move toward the endpoints. The claim is scoped: under the (very common) per-reroll-cost + best-of-K shop regime, greedy near-perfect rerolling overspends — demonstrated on the pinned constants, mechanism-explained, not asserted as a universal law.
