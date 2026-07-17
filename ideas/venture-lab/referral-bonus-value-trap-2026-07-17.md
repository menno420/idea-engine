# The referral bonus that maximizes viral coefficient R0 is strictly larger than the one that maximizes profit — so "tune the referral program for maximum virality" systematically overspends.

> **State:** sim-ready
> **Class:** venture-lab · referral economics · incentive/pricing design
> **Target:** sim-lab (VERDICT 111, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine@4de68f4 · fetched 2026-07-17T15:47:53Z
> **Harvest source (firsthand):** Galton–Watson branching-process anchor — https://en.wikipedia.org/wiki/Galton%E2%80%93Watson_process (fetched 2026-07-17T15:47:53Z, HTTP 200): "if the average number of a man's sons is 1 or less, then their surname will almost surely die out" (an almost-sure-extinction statement covering the subcritical case m<1; note it lumps in the critical case m=1 — the strict subcritical finite-progeny identity E[T]=S/(1−m) is the standard branching-process result, verified firsthand by the disclosed sim below, results sha256 5438482c…436786). Referral mechanism — https://en.wikipedia.org/wiki/Referral_marketing (fetched 2026-07-17T15:47:53Z, HTTP 200): "Referral marketing is a word-of-mouth initiative designed by a company to incentivize existing customers to introduce their family, friends, and contacts to become new customers."

## The phenomenon (one line)
Under a saturating referral response with a bonus paid per successful referral, profit peaks at an interior bonus b* whose viral coefficient R0 is well below the maximum achievable R0; spending past b* to chase virality strictly loses money, because total signups scale as S/(1−R0) and the cost of the last increment of R0 diverges.

## The folk belief
"Referral programs are growth engines — crank the bonus until the viral coefficient (k / R0) is as high as you can get it; every extra referral is (near-)free acquisition, so more virality is always better." Growth teams tune the referral incentive to maximize invites/activations (R0), treating the bonus as an investment that pays for itself through the cascade.

## The mechanism (reasoned to its fuller form — Q-0254 duty)
Model the referral cascade as a subcritical Galton–Watson branching process. A seed cohort of S paying users each makes K independent referral attempts; each attempt converts a new signup with probability q(b), where b is the bonus paid per successful referral. Offspring per user ~ Binomial(K, q(b)), so the viral coefficient is R0 = m(b) = K·q(b). The bonus response saturates: q(b) = q_max·(1 − e^(−b/b0)) — early dollars buy a lot of conversion, later dollars almost none.

Total signups across all generations follow the branching-process geometric anchor E[T] = S/(1 − m(b)); referred signups (all but the seed) = S·m/(1−m), each costing b. With net margin M per signup:

  Π(b) = M·E[T] − b·E[R] = S·(M − b·m(b))/(1 − m(b)).

Two forces oppose as b rises. (1) The 1/(1−m) amplifier: pushing R0 toward 1 multiplies the cascade super-linearly — the "virality is magic" intuition, and it is real. (2) But every referred signup now costs b, the saturating q(b) means the marginal R0 bought per dollar collapses, and the population you pay the bonus to, S·m/(1−m), explodes on the same 1/(1−m) that amplifies your margin. Past a point the bonus bill grows faster than the amplified margin.

So Π(b) is single-peaked with a hard INTERIOR optimum b*, and R0(b*) sits strictly below the maximum R0 the program can reach. The virality-maximizing bonus is on the far side of the peak and destroys profit. Counterintuitive core: the same 1/(1−R0) factor that makes virality feel free is what makes the last increment of R0 ruinously expensive — you pay the bonus to every one of the exploding referred users. "Maximize the viral coefficient" is a value trap; the right objective is Π(b), whose optimum lies strictly below the R0 optimum.

## Pinned world (committed constants — sim-lab must reproduce exactly)
- SEED = 20260717 (fixed; deterministic run)
- S = 1000 (seed cohort, generation 0)
- K = 3 (referral attempts per user)
- q_max = 0.25 (K·q_max = 0.75 < 1 → subcritical cap; max R0 over grid = 0.736263)
- b0 = 2.0 (bonus half-saturation scale)
- M = 10.0 (net margin per signup)
- N = 2000 (Monte-Carlo cohort replications per bonus level)
- Bonus grid = [0.0 … 8.0] step 0.1 (81 points); b_viral = grid max = 8.0; B_HI (bracket) = 6.0
- Offspring law: Binomial(K, q(b)); q(b) = q_max·(1 − e^(−b/b0)); m(b) = R0(b) = K·q(b)
- Analytic: E[T]=S/(1−m), E[R]=S·m/(1−m), Π(b)=S·(M−b·m)/(1−m); per-cohort profit Π_rep=(M−b)·T + b·S
- Derived pins: b* = 4.5 (argmax analytic Π on grid), R0(b*)=0.670951, Π(b*)=21214.815 (analytic); b_viral=8.0, R0=0.736263, Π=15583.320; Π(0)=10000.000; Π(B_HI=6.0)=19920.776

## Pre-registered gates (evaluation order R1 → R2 → R3; APPROVE iff ALL hold)
- **R1 — branching anchor consistency (MATCH):** the simulated mean total signups at b* reproduces the geometric anchor S/(1−m(b*)) within 3σ: |E_sim[T] − S/(1−m(b*))| / SE_T < 3. Confirms the sim implements the branching process the closed form rests on.
- **R2 — interior optimum:** Π̄(b*) exceeds BOTH Π̄(0) and Π̄(B_HI) by ≥3σ each (two-sample z). Establishes b* is a genuine interior peak, not a monotone endpoint.
- **R3 — value trap (headline):** Π̄(b*) exceeds Π̄(b_viral) by ≥3σ, where b_viral is the R0-maximizing (grid-max) bonus. Establishes that tuning for maximum virality strictly loses profit.

## Pre-registered decision rule
APPROVE iff R1 ∧ R2 ∧ R3 all hold at their stated thresholds on the pinned world with SEED=20260717 and the committed reference verifier. Any gate failing → REJECT (the interior-optimum / value-trap claim is falsified for these constants). No post-hoc threshold moves; margins reported in σ.

## Disclosed verifier (the sim-lab spec)
Stdlib-only python3 (`random, math, json, hashlib, bisect` — no numpy), committed alongside this idea as `referral_value_trap.py`. Seed once with SEED=20260717. For each b ∈ {0.0, b*=4.5, B_HI=6.0, b_viral=8.0}: run N=2000 cohort replications of the Galton–Watson cascade (Binomial(K,q(b)) offspring via a per-individual categorical draw from the exact pmf, generation-by-generation to extinction), record per-cohort profit Π_rep=(M−b)·T+b·S; compute mean and unbiased SE. Evaluate R1/R2/R3 as above; also assert m(b)<1 across the grid (subcritical), Π single-peaked on the grid, and b* strictly interior. Emit a canonical (sorted-keys, comma/colon-separated) results JSON and its sha256. Expected results-dict sha256 (dry-sim, this pinned world) = 5438482c51479370e2a80aef0a01d3fe7f5617dcc1d30a622c9e74e1c8436786. Exit 0 iff all gates pass.

## Why it matters (venture-ops)
Referral-program tuning is usually run as "maximize the viral coefficient" (invites × activation rate). This proposal says that objective is wrong whenever the bonus response saturates and you pay per successful referral: the profit-optimal bonus is strictly below the virality-optimal one, and the gap is large (here b*=4.5 vs b_viral=8.0 — a 1.78× overspend, ~27% of profit destroyed at the virality-max setting). Decision rule for an indie operator: set the referral bonus by the profit curve Π(b)=S(M−b·m(b))/(1−m(b)), not by the R0 curve; measure the bonus→conversion saturation (q_max, b0) and margin M, solve for b*, and cap the incentive there. The 1/(1−R0) amplifier is a trap that multiplies your bonus bill as fast as your cascade.

## Dedup
Distinct from the venture priors:
- P086 (series read-through): sequential catalog demand, no referral cascade / branching process.
- P090 (big-pond badge inversion / badge-starvation): reward-scarcity signalling, not incentive-tuning under a branching amplifier.
- P094 (refund-window interior optimum): interior optimum too, but on refund policy vs. abuse; here the interior optimum is on the referral bonus and is driven by the 1/(1−R0) branching amplifier + saturating conversion — a different lever and mechanism.
- versioning-depth / channel-concentration priors: pricing-tier depth / distribution mix, no viral/referral dynamics.
The shared "interior optimum" shape with P094 is acknowledged; the novel content is the branching-amplifier value trap — the objective operators actually optimize (R0) is provably the wrong one, and the profit-optimal lever sits strictly below it.

## Model basis (declared model-dependence — the P024 discipline)
The interior optimum and the b* < b_viral ordering are robust to the specific constants but DO depend on structural assumptions: (a) the bonus is paid per successful referral (not a flat one-time cost); (b) conversion saturates in the bonus (concave q(b)); (c) the process is subcritical (R0<1) so E[T]=S/(1−m) is finite. If the bonus were a fixed cost independent of referral volume, or q(b) were linear/convex, the b* < b_viral gap can shrink or vanish. The claim is scoped: under the (very common) per-referral-bonus + saturating-response regime, virality-maximization overspends — demonstrated on the pinned constants, mechanism-explained, not asserted as a universal law.

## Probe report (v0, 2026-07-17)
1. **Setup.** Subcritical Galton–Watson referral cascade; pinned world above; SEED=20260717; N=2000 cohorts/level; committed stdlib-only verifier, exit 0.
2. **Anchor (analytic).** E[T]=S/(1−m); at b*=4.5, m=0.670951 → E[T]=3039.057, Π(b*)=21214.815. At b_viral=8.0, m=0.736263 → E[T]=3791.660, Π=15583.320. Π(0)=10000.000, Π(6.0)=19920.776. Π single-peaked on the grid; max m=0.736263 < 1 (subcritical); b*=4.5 strictly interior.
3. **R1 (anchor match).** E_sim[T] at b* = 3035.927 (SE 2.6884) vs analytic 3039.057 → |z|=1.16σ < 3 → PASS.
4. **R2 (interior optimum).** Π̄(b*)=21197.596 (SE 14.7864). vs Π̄(0)=10000.000: diff 11197.596, z=757.29σ. vs Π̄(B_HI=6.0)=19932.238 (SE 13.7105): diff 1265.358, z=62.75σ. Both ≥3σ → PASS.
5. **R3 (value trap headline).** Π̄(b*)=21197.596 vs Π̄(b_viral=8.0)=15575.369 (SE 7.8439): diff 5622.227, z=335.89σ ≥3σ → PASS.
6. **All gates PASS** (exit 0). Results-dict sha256 = 5438482c51479370e2a80aef0a01d3fe7f5617dcc1d30a622c9e74e1c8436786.
7. **Correction disclosed.** During calibration the near-critical cap (K·q_max≈0.9) was rejected: at m≈0.9 the cohort-total variance ∝ 1/(1−m)³ blows the SE up at high-bonus levels, making R3 noisy. Pinned q_max=0.25 (K·q_max=0.75) keeps tails controlled while preserving the interior peak. Disclosed so the verifier reproduces the exact subcritical regime; no gate thresholds were moved.
8. **Reproduction.** `python3 referral_value_trap.py` → prints the table above, writes referral_value_trap_results.json, exit 0. Deterministic under SEED.

## Gate power + margin ledger
| Gate | Type | Threshold | Observed | Margin | Verdict |
|---|---|---|---|---|---|
| R1 anchor match | match (\|z\|<3σ) | <3σ | \|z\|=1.16σ | 1.84σ headroom | PASS |
| R2a interior vs b=0 | separation ≥3σ | ≥3σ | z=757.29σ | 754.3σ | PASS |
| R2b interior vs b_hi | separation ≥3σ | ≥3σ | z=62.75σ | 59.75σ | PASS |
| R3 value trap vs b_viral | separation ≥3σ | ≥3σ | z=335.89σ | 332.9σ | PASS |

**Recommendation: sim-ready**
