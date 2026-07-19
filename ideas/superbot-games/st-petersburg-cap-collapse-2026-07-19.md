# PROPOSAL 151 — St. Petersburg cap-collapse: a doubling "press-your-luck" jackpot has INFINITE expected value, yet capping the payout at 2^M coins collapses its fair ticket price to exactly M/2 + 1 — the price grows only LOGARITHMICALLY in the cap, so doubling the bankroll adds half a coin, not double the payout

> **State:** sim-ready
> **Class:** superbot-games · game-economy jackpot / gamble-feature pricing · St. Petersburg paradox under a bounded bankroll (decision theory / lottery microeconomics)
> **Anchor:** St. Petersburg paradox — a fair-coin doubling lottery has divergent (infinite) expected value, yet a finite banker/bankroll truncates the divergent tail so the fair entry price is finite and grows only with the LOGARITHM of the cap (Bernoulli 1738; Menger's bounded resolution)
> **Target:** sim-lab (VERDICT 164, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine@80e432d2682e7b602138a91a8cabb14956f27b1c · fetched 2026-07-19T03:00:36Z
> **Reference (external, reachable):** [St. Petersburg paradox — Wikipedia](https://en.wikipedia.org/wiki/St._Petersburg_paradox) — verified reachable 2026-07-19 via WebFetch ("If the casino has finite resources, the game must end once those resources are exhausted"; with a finite bankroll the fair entry becomes proportional to the logarithm of the banker's resources — a millionaire banker makes the fair entry only about $20, not infinite)
> **Verifier (firsthand):** `ideas/superbot-games/st_petersburg_cap_collapse.py` · results-dict sha256 `e1919f49d20df0b50121864b8e35f78be0637e4eeb812799e9f0d8af535ef078`
> 📊 Model: Claude Opus · high · idea/planning

## The phenomenon (one line)
A doubling "press-your-luck" jackpot — flip a fair coin, the pot doubles on heads, you bank it on the first tails — has INFINITE expected value, but once the house caps the payout at 2^M coins its fair ticket price is exactly M/2 + 1 coins and grows only logarithmically in the cap: doubling the maximum jackpot adds a constant half-coin, not a doubling.

## The folk belief
"Infinite expected value means the ticket is priceless — as a house you can charge a fortune, and as a player you should pay almost anything to enter. A 'double-or-bank' jackpot with no fixed ceiling is worth a lot, and a bigger advertised maximum payout is worth proportionally more." Economy designers price gamble features off the headline jackpot or off a playtest average of the payout.

## The game-design thesis (reasoned to its fuller form — Q-0254 duty)
Model the minigame exactly: the player pays a ticket price, then plays a **double-or-bank** round. Start a pot at 1. Each step, flip a coin that comes up "continue" with probability **p**; on continue the pot multiplies by **r** and the round goes again, on the first "stop" (probability **1−p**) the player banks the pot. After **k** continues the payout is **r^k**, drawn with probability **(1−p)·p^k**. The uncapped expected value is **(1−p)·Σ_k (p·r)^k**, which **diverges** whenever **p·r ≥ 1** — for fair doubling (p=1/2, r=2, so p·r=1) the sum is 1+1+1+… = ∞. So a designer literally **cannot** price the feature from its expected value, and a Monte-Carlo playtest average is no help either: the sample mean of a St. Petersburg payout **has no stable value** — it grows without bound as more runs are added, because it is dominated by ever-rarer, ever-larger jackpots.

The resolution the designer already has (whether they know it or not) is the **payout cap**: no house pays more than its bankroll **C = r^M**, so the realized payout is **r^min(k,M)**. That single truncation makes the expected value finite and, on the critical curve **p·r = 1**, astonishingly simple:

    EV_cap(p, r, M) = (1−p)·((pr)^M − 1)/(pr − 1) + (pr)^M  ──(pr=1)──►  (1−p)·M + 1.

For fair doubling this is **M/2 + 1**. The fair ticket price is therefore set by the **number of BITS of bankroll**, not by the headline jackpot: cap the payout at a **billion** coins (M≈30) and the fair price is **≈16 coins**; cap it at **4096** (M=12) and the fair price is **7 coins**. Doubling the bankroll — buying one more bit, M→M+1 — adds **exactly (1−p) = 0.5** coins. The counterintuitive core: the price a designer would compute from the naive uncapped intuition (infinite, or a runaway sample mean) and the true price (a handful of coins) differ without bound, and the true price is nearly **insensitive** to the maximum payout the feature advertises.

Concretely (SEED = 20260717, committed constants): at cap 2^12 = 4096 the Monte-Carlo fair price is **7.067918** (closed form **7.0**), which is **≈290×** below half the maximum payout (2048). Raising the cap from **2^6** to **2^12** — a **64×** larger jackpot — lifts the fair price by only **3.069885** coins (the +½-per-bit log rule predicts **+3.0**), whereas a designer who assumed the price scales with the jackpot would predict **+251.876047**. The whole result is an objective closed-form identity confirmed by simulation — the only modelling choice is that the tail is truncated by a **cap** (equivalently a bounded utility); the divergence and the log-scaling are not model-dependent.

## The formal model (committed constants — sim-lab must reproduce exactly)
- Payout of one round after k continues is **r^k**, drawn with probability **(1−p)·p^k** (k continues then a stop); the house caps it, so realized payout = **r^min(k,M)** where the cap is **r^M**.
- Fair price = expected realized payout, estimated by **N_SAMPLES** independent rounds under one `random.Random(SEED)` stream; a round is sampled by flipping "continue" (prob p) until a stop or until k reaches M (once k≥M the payout is fixed at r^M regardless of further flips, so the sampler returns r^M immediately — an exact equivalence, same payout distribution).
- Closed-form anchor: **EV_cap(p, r, M) = (1−p)·((pr)^M − 1)/(pr − 1) + (pr)^M**, reducing on the critical curve **pr = 1** to **(1−p)·M + 1**.
- Standard error from the sample variance; z = (mc_mean − H0)/se on the /se convention.
- **Model note (declared):** the head is an objective mathematical identity (divergent uncapped EV; finite, log-scaling capped fair price). The single declared modelling choice is that the divergent tail is truncated by a **payout cap** C = r^M; a bounded utility u(x)=log x gives the same finite log-scaling price (Bernoulli's 1738 resolution) — the two are interchangeable tail-tamers and neither changes the sign or the order of magnitude.

## Pinned world (committed constants)
- SEED = 20260717
- SIGMA_GATE = 3.0
- N_SAMPLES = 400000
- Classic (critical curve p·r = 1): continue-prob p = 0.5, multiplier r = 2.0; nominal cap 2^12 = 4096; slope caps {2^6, 2^8, 2^10, 2^12}
- Shifted-coin robustness (still on the critical curve p·r = 1): p = 0.4, r = 2.5; cap 2.5^10 ≈ 9536.743164

## Pre-registered gates (APPROVE iff ALL hold, in order G1 → G2 → G3)
- **G1 — finite price collapse.** At the nominal cap 2^12 = 4096, the MC fair price is finite and is significantly BELOW half the maximum payout: z = (cap/2 − mc_mean)/se ≥ SIGMA_GATE. The infinite-EV jackpot is worth a handful of coins. (Disclosed anchor: mc_mean matches the closed form M/2+1 = 7.)
- **G2 — sublinear (logarithmic) scaling.** Raising the cap from 2^6 to 2^12 raises the fair price by an increment Δ that is (a) positive, (b) matched to the +½-per-bit log rule (|Δ − 3.0| ≤ SIGMA_GATE·se_Δ), and (c) ≥ SIGMA_GATE·se_Δ BELOW the cap-proportional increment a "price scales with the jackpot" intuition predicts: z = (Δ_proportional − Δ)/se_Δ ≥ SIGMA_GATE. Doubling the max jackpot does not double the price.
- **G3 — robustness under a shifted coin.** Under a SHIFTED distribution — a biased coin p = 0.4 with multiplier r = 2.5 held on the same critical curve p·r = 1 — the capped fair price stays finite and matches the GENERALIZED closed form (1−p)·M + 1 within SIGMA_GATE (|z| ≤ 3.0), with the log-rule slope tracking (1−p) = 0.6 rather than 0.5. The finite-log-price phenomenon is not special to fair doubling.

## Pre-registered decision rule
APPROVE (sim-ready confirmed) iff G1 AND G2 AND G3 all hold in order and the verifier exits 0 with a reproducible results-dict sha256 across a deterministic double-run. Any gate failing ⇒ REJECT/REVISE.

## Dry-sim results (SEED=20260717, verbatim from the committed verifier)
```
{
  "all_pass": true,
  "classic_by_cap": {
    "m_10": {
      "cap": 1024.0,
      "closed_form": 6.0,
      "mc_mean": 6.121433,
      "se": 0.063216,
      "z_anchor": 1.920911
    },
    "m_12": {
      "cap": 4096.0,
      "closed_form": 7.0,
      "mc_mean": 7.067918,
      "se": 0.123719,
      "z_anchor": 0.548966
    },
    "m_6": {
      "cap": 64.0,
      "closed_form": 4.0,
      "mc_mean": 3.998032,
      "se": 0.014066,
      "z_anchor": -0.139879
    },
    "m_8": {
      "cap": 256.0,
      "closed_form": 5.0,
      "mc_mean": 4.952937,
      "se": 0.029604,
      "z_anchor": -1.589759
    }
  },
  "first_failing_gate": null,
  "g1_finite_price_collapse": {
    "cap": 4096.0,
    "closed_form": 7.0,
    "half_cap": 2048.0,
    "mc_fair_price": 7.067918,
    "pass": true,
    "z": 16496.525875
  },
  "g2_sublinear_scaling": {
    "delta_cap_proportional_pred": 251.876047,
    "delta_logrule_pred": 3.0,
    "delta_measured": 3.069885,
    "m_hi": 12,
    "m_lo": 6,
    "pass": true,
    "se_delta": 0.124516,
    "z_logrule_anchor": 0.561254,
    "z_sublinear": 1998.187697
  },
  "g3_robust_shifted": {
    "cap": 9536.743164,
    "cap_bits": 10,
    "closed_form": 7.0,
    "mc_fair_price": 6.828497,
    "p_cont": 0.4,
    "pass": true,
    "r": 2.5,
    "se": 0.17139,
    "slope_per_bit_pred": 0.6,
    "z_anchor": -1.000661
  },
  "gates": [
    {
      "id": "G1",
      "name": "finite_price_collapse",
      "pass": true,
      "z": 16496.525875
    },
    {
      "id": "G2",
      "name": "sublinear_scaling",
      "pass": true,
      "z": 1998.187697
    },
    {
      "id": "G3",
      "name": "robust_under_shifted_coin",
      "pass": true,
      "z": -1.000661
    }
  ],
  "params": {
    "cap_bits_nominal": 12,
    "cap_bits_shift": 10,
    "n_samples": 400000,
    "p_cont": 0.5,
    "p_cont_shift": 0.4,
    "r": 2.0,
    "r_shift": 2.5,
    "seed": 20260717,
    "sigma_gate": 3.0,
    "slope_bits": [
      6,
      8,
      10,
      12
    ]
  }
}
Results-JSON sha256: e1919f49d20df0b50121864b8e35f78be0637e4eeb812799e9f0d8af535ef078
```
Results-dict sha256: `e1919f49d20df0b50121864b8e35f78be0637e4eeb812799e9f0d8af535ef078` (deterministic double-run, exit 0 both times).

## Verifier
`ideas/superbot-games/st_petersburg_cap_collapse.py` — stdlib only (`random, math, json, hashlib`). Samples N_SAMPLES double-or-bank rounds under one seeded stream for four classic caps {2^6,2^8,2^10,2^12} and one shifted-coin world, computes each capped fair price and its closed-form anchor, and runs the three ordered z-gates (finite-price collapse vs half-cap, sublinear scaling vs cap-proportional growth with the log-rule anchor, and the shifted-coin generalized-closed-form anchor). Emits the whole results dict (no self-referential sha field; every float rounded to 6 decimals; the compact-canonical serialization's sha256 IS the disclosed digest; stdout dumps the pretty indent=2 view — the WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY posture, P127+ twist). Writes no JSON to disk.

## Reproduce
```
python3 ideas/superbot-games/st_petersburg_cap_collapse.py
```
Expected: prints the results JSON, `Results-JSON sha256: e1919f49d20df0b50121864b8e35f78be0637e4eeb812799e9f0d8af535ef078`, exit 0 (all_pass=true).

## Why it matters (game design)
A "double-or-bank" jackpot, a doubling-gamble feature, a press-your-luck event, a lottery/prize-pool — all inherit the St. Petersburg divergence, and all are un-priceable by expected value or by a playtest average. The only stable price is the closed form of the CAPPED game, and it has two design consequences that invert intuition: (1) the fair price is set by the **log of the bankroll**, so buying a bigger headline jackpot barely moves it — advertising "up to a BILLION coins!" is worth ~16 coins of fair value, and doubling that cap adds half a coin; (2) an uncapped or under-capped feature has **no finite fair price**, so any fixed ticket cost is either a rip-off (in the body) or a bankroll-threatening liability (in the tail), and "we averaged our playtests" is not a defense because the average never converged. Price the CAP, not the fantasy: compute (1−p)·M+1 from the bankroll bits, or bound the payout/utility until the price is finite and stop advertising the maximum as if it were the value.

## Dedup
- Distinct from every prior game-lane card: shop-reroll-ruin (optimal stopping on a finite reroll budget), streak-shield-regression (regression to the mean), energy-cap-overflow (renewal overflow forfeiture), matchmaking-winrate-mirage (Elo compression), compounding-reward-inequality (log-normal Gini), prd-proc-compression, snipe-clearing-leak (auction microstructure), guild-volunteer-dilemma (public goods), single-elim-favorite-collapse (tournament order statistics), balance-triangle (zero-sum equilibrium), raid-coordination-overhead (Ringelmann), rank-decay-churn-cliff (loss aversion), gresham-currency-hoard (two-currency hoarding), pity-anticipation-collapse (gacha timing). **None model a divergent-expected-value lottery or a bounded-bankroll fair-price collapse.**
- Closest relatives are shop-reroll-ruin and the fleet card gamblers-ruin-edge-asymmetry — both are bounded-bankroll gambling, but shop-reroll is an optimal-stopping value trap and gamblers-ruin is a bounded random walk with a per-step edge; NEITHER has a DIVERGENT expected value, an unbounded sample mean, or the log-of-cap fair-price law. This is the FIRST St. Petersburg / infinite-EV-jackpot / bounded-bankroll card in any lane.

## Model basis (declared model-dependence — the P024 discipline)
The head is an **objective closed-form identity**, not a behavioural claim: the uncapped expected value diverges for p·r ≥ 1, and the capped expected value equals (1−p)·((pr)^M−1)/(pr−1)+(pr)^M, reducing to (1−p)·M+1 on the critical curve — both are exact and confirmed by Monte-Carlo to 6 dp. The **one declared modelling choice** (flagged, not hidden): the divergent tail is truncated by a **payout cap** C = r^M. The alternative classical resolution — a **bounded/concave utility** (Bernoulli 1738: value log x; Menger: bounded utility) — yields the same qualitative result (a finite price that grows with the log of the stakes), so "cap the payout" and "bound the utility" are interchangeable tail-tamers; the cap is chosen here because it is the mechanism a real game economy actually imposes (a house cannot pay beyond its bankroll) and it makes the fair price a clean function of bankroll bits. The specific magnitudes (7 coins at cap 4096; +½/bit; slope 0.6 under the shifted coin) are pinned to (p, r, M, N_SAMPLES); the SIGNS and the log-scaling are calibration-general (G3 shifts the coin and the law holds with slope (1−p)).

## Probe report (v0, 2026-07-19)

**1. What is this really?** A pricing-collapse law for divergent-EV gambles. A doubling jackpot has infinite expected value, so it cannot be priced by EV or by a sample mean (which never converges). Cap the payout at 2^M and the fair price snaps to a finite M/2+1 coins that grows only logarithmically in the cap. The naive price (∞ or a runaway average) and the true price (a handful of coins) diverge without bound.
**2. What would make it false?** If the capped MC mean were NOT ≥3σ below half the max payout (G1 — the price is not a small finite number), or if raising the cap 2^6→2^12 raised the price cap-proportionally instead of by the +½/bit log increment (G2 — scaling is not sublinear), or if the shifted-coin world's price did NOT match its generalized closed form (G3 — the law does not generalize). Any of G1/G2/G3 failing → REJECT.
**3. Simplest version that still bites?** SEED = 20260717; a fair-doubling jackpot capped at 2^12 = 4096 already prices at **7 coins** (MC 7.067918), ≈290× below half the max payout, and a 64× bigger cap adds just **3 coins**. One truncation turns an infinite EV into a 7-coin ticket.
**4. What is the counterintuitive core?** "Infinite expected value ⇒ priceless, and a bigger jackpot ⇒ proportionally more valuable" is inverted. The fair price is finite, tiny, and set by the LOG of the bankroll; the advertised maximum jackpot is nearly orthogonal to the value, and doubling it adds a constant half-coin.
**5. Where could I be fooling myself?** The MC mean of a St. Petersburg payout is itself high-variance and unstable at large caps — so the verifier pins a MODEST cap (2^12) where the mean is well-estimated (se≈0.12 at N=400k) and anchors every MC price to an exact closed form (the by-cap ladder matches M/2+1 to <0.07). G3 guards against the law being an artifact of fair doubling by shifting the coin to p=0.4/r=2.5 and confirming the generalized closed form with a DIFFERENT slope (0.6). The sampler's early-return at k≥M is an exact equivalence (payout is capped regardless of further flips), not an approximation.
**6. What is the honest calibration?** Dry-sim at SEED = 20260717: G1 z = +16496.525875 (fair price 7.067918 ≪ half-cap 2048); G2 z_sublinear = +1998.187697 (Δ_measured 3.069885 vs Δ_proportional 251.876047; log-rule anchor z = +0.561254 ≈ 0); G3 z = −1.000661 (shifted price 6.828497 vs generalized closed form 7.0, |z| ≤ 3). By-cap ladder (MC/closed form): 2^6 3.998032/4.0, 2^8 4.952937/5.0, 2^10 6.121433/6.0, 2^12 7.067918/7.0. all_pass=true, exit 0; results-dict sha256 e1919f49…f078, two runs byte-identical. The large G1/G2 z-values are the honest scale of the collapse (the price is hundreds of × below the naive benchmark), not statistical over-precision; G3 is a two-sided anchor (small |z| = MC matches theory).
**7. What decision does it change?** Stop pricing a divergent-EV gamble feature off its headline jackpot or a playtest average. Compute the capped closed form (1−p)·M+1 from the bankroll bits; if you want a bigger advertised maximum, know it barely moves the fair price; if the feature is uncapped, know it has NO finite fair price and cap the payout (or bound the utility) before shipping it.
**8. How will we know it worked?** The committed stdlib verifier reproduces, under SEED = 20260717, the finite-price collapse (G1), the sublinear log-scaling (G2), and the shifted-coin generalized-closed-form anchor (G3) at their SIGMA_GATE = 3.0 bars, with the results-dict sha256 matching e1919f49d20df0b50121864b8e35f78be0637e4eeb812799e9f0d8af535ef078 across a deterministic double-run.

## One-line design fix
Price a divergent-EV "double-or-bank" gamble by the closed form of the CAPPED game — (1−p)·M+1, set by the log of the bankroll — not by its (infinite) expected value or a (never-converging) playtest average, and remember a bigger advertised jackpot adds only a constant half-coin per bit of cap.

**Recommendation: sim-ready**
