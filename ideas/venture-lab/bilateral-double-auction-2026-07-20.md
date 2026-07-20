# Bilateral double auction — Myerson–Satterthwaite made concrete (PROPOSAL 230 → VERDICT 243)

> **Status:** `sim-ready`
>
> Round-56 VENTURE slot (market design / mechanism design). Paired reproduction mirror VERDICT 243 (offset +13; sim-lab). Claim-first; a stdlib-only Python verifier reproduces every number below deterministically (SEED=20260717).

## Claim

A buyer with value `v` and a seller with cost `c`, drawn independently from Uniform[0,1], meet in the Chatterjee–Samuelson **k = 1/2 double auction**: each names a number, and if the buyer's bid `b` weakly exceeds the seller's ask `s` they trade at the midpoint `(b + s)/2`. The unique linear Bayes–Nash equilibrium is

- buyer bid **b(v) = (2/3)·v + 1/12**
- seller ask **s(c) = (2/3)·c + 1/4**

Because the two offer functions share the slope 2/3, trade happens **exactly when `v − c ≥ 1/4`**. The expected realized gains from trade are then **exactly 9/64 = 0.140625**, versus the first-best rule (trade whenever `v ≥ c`) of **1/6 ≈ 0.166667**. So the strategic mechanism captures exactly **27/32 ≈ 84.4%** of the achievable surplus and forgoes a deadweight of exactly **5/192 ≈ 0.026042** — a concrete, closed-form instance of the **Myerson–Satterthwaite impossibility**: no mechanism for bilateral trade under these priors is simultaneously efficient, individually rational, budget balanced, and incentive compatible, and the linear equilibrium's 5/192 gap is the surplus that impossibility costs.

## Why it holds (sketch)

Fix the seller's strategy `s(c) = (2/3)c + 1/4` (so `s ∼ U[1/4, 11/12]` in shape). A buyer of value `v` bidding `b` trades with every seller cost `c` such that `s(c) ≤ b`, i.e. `c ≤ (3/2)(b − 1/4)`, and pays the midpoint. Maximising the expected surplus `∫ (v − (b + s(c))/2) dc` over the trading region gives the first-order condition whose solution is `b*(v) = (2/3)v + 1/12`. The seller's symmetric problem against the buyer's linear rule yields `s*(c) = (2/3)c + 1/4`. Both offers have slope 2/3, so `b(v) ≥ s(c) ⇔ (2/3)(v − c) ≥ 1/4 − 1/12 = 1/6 ⇔ v − c ≥ 1/4`. Integrating the surplus over that region gives 9/64; integrating over the efficient region `v ≥ c` gives 1/6.

## Exact numbers

| quantity | value |
| --- | --- |
| trade threshold `v − c` | 1/4 |
| realized gains from trade | 9/64 = 0.140625 |
| first-best (efficient) gains | 1/6 ≈ 0.166667 |
| efficiency (realized / first-best) | 27/32 = 0.84375 |
| deadweight loss | 5/192 ≈ 0.026042 |
| trade probability | 9/32 = 0.28125 |

## Verifier and gate battery

`ideas/venture-lab/bilateral-double-auction.py` — stdlib-only, SEED=20260717, deterministic (in-process double-run and separate re-invocation byte-identical). It prints an indented results dict and `results_sha256: 5052053d3a6cb6fb1419afe0846f4f339d3537057d6ee5fbeb8a86e9b9ea42c3` (full 64 hex). Four gates, each scored in its own direction:

- **G1 EXACT EQUALITY** (`fractions.Fraction`, RNG-free): exact rational integration of the surplus over the equilibrium trade region reproduces `delta=1/4`, `realized=9/64`, `first_best=1/6`, `efficiency=27/32`, `deadweight=5/192`, `trade_prob=9/32`.
- **G2 MC AGREEMENT** (`|z| < 3`): N = 200000 draws under the equilibrium rule; mean realized gains agree with 9/64 (z_gains = −0.123561, p̂ = 0.140558) and trade frequency agrees with 9/32 (z_trade = −0.258615, p̂ = 0.28099).
- **G3 INVARIANCE / ROBUSTNESS**: a grid best-response check confirms `b*(v)` and `s*(c)` are each the payoff-maximising deviation at four probe points apiece, and a second independent exact route (integrating over the difference density `f_D(d) = 1 − d`) reproduces 9/64.
- **G4 FALSIFIABILITY** (`|z| > 6`): on the same sample the efficient rule agrees with 1/6 (z = −0.308089) while the equilibrium's realized gains reject the naive "the double auction is efficient ⇒ gains 1/6" claim at z = −47.919492.

## Grounding

Pinned external source (bare `<url>@<hex>`, oldid + raw-wikitext sha1):
`https://en.wikipedia.org/w/index.php?title=Double_auction&oldid=1346190881@ffbd1f23d644439cf57dfe7be48fc39990d9b68a` · fetched 2026-07-20.

- **Quoted** (literally on the pinned revision): the existence of a linear-strategy Bayesian Nash equilibrium under a uniform prior, and the Myerson–Satterthwaite impossibility that no mechanism is simultaneously individually rational, budget balanced, incentive compatible, and (economically) efficient — including the k = 1 bilateral corollary that the only efficient deal is given up.
- **Derived** (computed firsthand, absent from the page): the equilibrium coefficients 2/3, 1/12, 1/4; the `v − c ≥ 1/4` threshold; the values 9/64, 1/6, 27/32, 5/192; the explicit Uniform[0,1] support; and the Chatterjee–Samuelson attribution.
