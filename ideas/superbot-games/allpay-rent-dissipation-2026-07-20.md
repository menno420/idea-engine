# Complete rent dissipation in the all-pay auction — n rivals burn a total of exactly V, no more, and every bidder breaks even

> **State:** sim-ready
> **Class:** superbot-games · mechanism design / contest theory · all-pay auction, rent dissipation
> **Target:** sim-lab (VERDICT 220, +13 offset)
> **Grounding:** https://en.wikipedia.org/w/index.php?title=All-pay_auction&oldid=1345188183@276dc7a58c201dce404fb2e3ef0006f072b01c8a · fetched 2026-07-20T10:06:48Z
> **Verifier (firsthand):** committed stdlib-only reference sim `ideas/superbot-games/allpay-rent-dissipation-2026-07-20.py` (hashlib, json, sys, random, fractions.Fraction) — results-dict sha256 f771cd42… (full 64 hex in Dry-sim below).

## The phenomenon (one line)
In a symmetric complete-information all-pay auction for a prize worth V among n ≥ 2 risk-neutral bidders (highest bid wins; EVERYONE pays their own bid), the symmetric mixed-strategy equilibrium burns total expected effort **exactly V — independent of n** — and every bidder's expected net payoff is **exactly zero**: adding rivals does not raise total effort, it only splits the same V into thinner per-head slices (V/n each).

## The folk belief
"More competitors means more total effort." Design a contest, a bidding war, a grind-for-one-prize event, or a rank-1 leaderboard payout, and the intuition is that a bigger field burns more aggregate effort — so a scarce prize contested by many is "worth" more effort in total than the same prize contested by two. It isn't.

## The game-design thesis (reasoned to its fuller form — Q-0254 duty)
When winning requires out-bidding rivals and losers forfeit their bid (an all-pay contest — leaderboard grinds, sunk-cost auctions, war-of-attrition events, "top contributor wins" drives), the equilibrium is a mixed strategy that makes every participant *exactly indifferent across all effort levels*: their expected payoff is zero at every bid. Because the prize is worth V and, by symmetry, each of the n bidders wins with probability 1/n, each bidder's expected gross is V/n; indifference forces expected payment to also equal V/n, so the field burns n·(V/n) = V in aggregate — the **entire rent, and nothing more**, regardless of how many show up. The design consequence is sharp: a bigger field does NOT extract more total effort from the crowd; it only makes each individual's expected effort (and expected payoff) smaller. A designer who adds contestants hoping to grow the total grind is fooling themselves — they are thinning the per-head slice of a fixed pie. And every rational contestant breaks even in expectation, so an all-pay contest transfers no surplus to the participants: it is a pure rent-dissipation machine.

## The formal model (committed constants — sim-lab must reproduce exactly)
- Symmetric complete-information all-pay auction, prize value V, n ≥ 2 risk-neutral bidders, highest bid wins, every bidder pays their own bid.
- Symmetric equilibrium CDF: **F(b) = (b/V)^(1/(n-1))** on [0, V]. Inverse-CDF sampler: draw u ~ U(0,1), bid **b = V·u^(n-1)**.
- Win probability at bid b: **F(b)^(n-1) = ((b/V)^(1/(n-1)))^(n-1) = b/V** — the fractional root cancels, so P(win) = b/V is an EXACT rational in b (no irrational arithmetic).
- Expected payoff at bid b: **Π(b) = V·(b/V) − b = 0** for every b ∈ [0, V] — exact indifference proves both the equilibrium and the break-even result.
- Per-bidder expected payment: **E[b] = V·E[u^(n-1)] = V·(1/n) = V/n**. Total expected revenue **R = n·(V/n) = V, exactly, for all n ≥ 2**. Win prob 1/n ⇒ expected gross V/n, minus payment V/n ⇒ expected net = 0.

## Pinned world (committed constants)
SEED = 20260717 · Z_GATE = 3.0. G1 exact grid: n ∈ {2..8} × V ∈ {1, 2, 3, 1/2}, rational bid grid b = k·V/12 for k = 0..12 (all Fraction arithmetic). G2 effect: n = 5, V = 1, M = 100 000 Monte-Carlo auctions. G3 robustness: n ∈ {2..10} × V ∈ {1, 2, 3, 1/2}, M = 10 000 auctions per cell (36 cells). Digest recipe: sha256 of `json.dumps(results, sort_keys=True, separators=(",",":"))`, exact Fractions serialized as "num/den" strings, floats rounded to 6 dp, whole results dict, stdout-only, no self-referential sha field. One rng `random.Random(SEED)` threaded through G2 then G3 in fixed draw order.

## Feasibility probe (true values measured FIRST, then thresholds set)
Before pre-registering any gate the verifier probed the true quantities: closed-form total R = V exactly and per-player = V/n exactly for every probed n (G1 residuals are 0/0 — thresholds are exact equality, which the math meets by construction, not by tuned tolerance); measured n=5 revenue ≈ 0.998 vs naive n·(V/2) = 2.5 (a gap of ≈ 1.5, ~800 SE wide — the ≥3σ effect threshold is met with vast margin); worst-cell robustness deviation z ≈ 2.37 < 3.0 across all 36 cells (the "within 3σ of ratio 1" threshold holds in every cell, with headroom). No threshold was pre-registered that the math cannot hit.

## Pre-registered gates (sim-ready iff ALL hold, in order G1 → G2 → G3)
- **G1 — exact rent dissipation + break-even (EXACT, Fraction, no floats; direction: residual == 0, exact equality).** For n ∈ {2..8} × V ∈ {1,2,3,1/2}: closed-form total R == V and per-player == V/n exactly (revenue residual max = 0), AND Π(b) == 0 for the whole rational b-grid (payoff residual max = 0). Proves the equilibrium and break-even in closed form.
- **G2 — competition does NOT scale total effort with n (≥3σ EFFECT; direction: measured ≪ naive, AND |measured−V| < 3σ).** Over M = 100 000 auctions at n = 5: measured total revenue sits ≥ 3σ BELOW the naive linear-growth prediction n·(V/2) (captures "more rivals ≠ more total effort"), and is simultaneously within 3σ of the closed-form V (consistency).
- **G3 — the total is V across the whole grid (ROBUSTNESS/SHIFT; direction: ratio → 1, max deviation < 3σ).** Across n ∈ {2..10} × V ∈ {1,2,3,1/2} (36 cells): measured R̂/V stays within 3σ of 1 in EVERY cell.

## Pre-registered decision rule
APPROVE (VERDICT 220) iff an independent sim-lab re-implementation reproduces `results_sha256` byte-for-byte AND all three gates hold in order. Any gate failing, or any digest mismatch, is a REJECT.

## Dry-sim results (SEED=20260717, verbatim from the committed verifier)
```
G1: PASS
G2: PASS
G3: PASS
all_pass: True
```
- **G1** exact: revenue_residual_max = 0, pi_residual_max = 0, per_player_ok_all = true. Witnessed cell n=5, V=1: per_player = 1/5, total = 1 (= closed 1/5, V). Direction: residual == 0 (exact fraction equality).
- **G2** effect (n=5, V=1, M=100 000): measured_R = 0.99836, naive_R = 2.5, closed_R = 1.0, se = 0.001876, **z_below_naive = 800.469813** (measured ≥3σ below naive), consistency_abs = 0.00164 < 3·se → within_3se = true. Direction: measured ≪ naive AND |measured−V| < 3σ.
- **G3** robustness (36 cells): all_within_3sigma = true, **max_dev_z = 2.365573** (< 3.0) at worst cell n=8, V=2 (ratio 0.984982). Direction: ratio → 1, max deviation < 3σ.

**Disclosed results-dict sha256 = f771cd427068cd273eb545a40179233ddbc5ec7658e69cf4e6cadb97dbb91d70**

## Verifier
`exact_cell()` computes, in exact Fraction arithmetic, the closed-form per-player payment V/n, the total n·(V/n), the revenue residual (total − V), and Π(b) = V·(b/V) − b over the rational bid grid — no floats, no irrational roots (F(b)^(n-1) collapses to the rational b/V). `gate1()` sweeps the whole n×V grid and pins the max residuals. `mc_auctions()` runs M seeded all-pay auctions (bid = V·u^(n-1), per-auction revenue = sum of n bids) and returns the mean revenue and the standard error of that mean. `gate2()` contrasts the n=5 measured revenue against the naive n·(V/2) prediction (≥3σ below) and the closed-form V (within 3σ). `gate3()` sweeps the 36-cell n×V grid and pins the worst-cell ratio deviation z. `build_results()` double-runs in-process (aborts exit 3 on divergence) before `main()` emits the digest.
Reproduce:
```
python3 ideas/superbot-games/allpay-rent-dissipation-2026-07-20.py
```
Expected output ends with `all_pass: True` and `results_sha256: f771cd427068cd273eb545a40179233ddbc5ec7658e69cf4e6cadb97dbb91d70` (exit 0). A separate second invocation reproduces the identical digest (cross-invocation determinism, verified: three separate processes all emit f771cd42…b91d70).

## Why it matters (game design)
All-pay dynamics are everywhere in live systems: "top contributor this week wins the skin" drives, leaderboard grinds where everyone spends stamina but only rank 1 is paid, sunk-cost bidding events, war-of-attrition guild races. This says two things a designer must internalize: (1) enlarging the field does NOT grow the total effort you extract — the crowd burns exactly the prize value V in aggregate no matter how many contest it, so scaling participation only thins each player's slice and their expected payoff; (2) rational contestants break even in expectation, so an all-pay contest is a pure rent-dissipation machine that transfers no surplus to participants — dangerous for retention if players learn it. If you want total effort to scale with the crowd, the payout structure must NOT be winner-take-all-pay.

## Dedup
Distinct from every existing head. `grep -ri` across ideas/** for all-pay / "all pay auction" / rent dissipation / rent-seeking / Tullock / war-of-attrition returns nothing prior to this doc (the only hit is a forward-looking "future head" mention in the P199 Vickrey card, not a built head). Adjacent but distinct heads: P199 Vickrey second-price (truthful dominance in a sealed-bid *winner-pays* auction — here EVERYONE pays, and the result is a revenue/effort invariance, not a dominant strategy); superbot-games balance-triangle (zero-sum matrix value); fleet price-of-anarchy / Braess (routing inefficiency). No prior head computes an all-pay equilibrium or the rent-dissipation invariant.

## Model basis (declared model-dependence — the P024 discipline)
Depends on: the standard symmetric complete-information all-pay auction (risk-neutral bidders, common known value V, highest bid wins, all bidders pay, symmetric mixed equilibrium F(b) = (b/V)^(1/(n-1))). Under this standard model the results are theorems: total revenue = V and net payoff = 0 are exact for every n ≥ 2, and the win-probability identity F(b)^(n-1) = b/V makes the break-even check exact-rational with no irrational arithmetic. Departures that break it (asymmetric values, incomplete information / private values, risk aversion, bid caps) change the numbers — the incomplete-information IPV variant, e.g., yields a strictly smaller expected revenue (see grounding caveat).

## One-line design fix
If you want a bigger crowd to burn more total effort, do not make the contest winner-take-all-pay: under all-pay the field dissipates exactly the prize value V no matter how many enter, and every entrant breaks even — so scale the *prize*, not the field, to move total effort.

## Probe report (v0, 2026-07-20)
**1. What is this really?** The complete-information all-pay auction rent-dissipation result: in the symmetric mixed-strategy equilibrium (CDF F(b) = (b/V)^(1/(n-1))) the field burns total expected effort exactly V for every n ≥ 2, and each bidder's expected net payoff is exactly zero — competition fully dissipates the rent and splits it into V/n per-head slices.
**2. Is it genuinely surprising / counterintuitive?** Yes — the near-universal intuition is "more competitors ⇒ more total effort." The truth is that total effort is invariant at V regardless of n; adding rivals only thins each player's slice, never grows the aggregate.
**3. Is it TRUE (exactly, under a clean model)?** Yes. Under the standard symmetric complete-information model the results are exact: the win-probability identity F(b)^(n-1) = b/V collapses to a rational, so Π(b) = V·(b/V) − b = 0 for every b (exact Fraction), per-player payment = V/n, and total = V for all n ∈ {2..8} probed — revenue and payoff residuals are 0 with no float in any equality decision.
**4. Is it reproducible deterministically with stdlib only?** Yes — hashlib/json/sys/random/fractions only, SEED=20260717, exact Fraction arithmetic for G1, a single seeded rng threaded in fixed draw order for the Monte-Carlo gates, an in-process double-run guard, and a byte-identical second (and third) invocation; results-dict sha256 f771cd42…b91d70 disclosed.
**5. What would REFUTE it?** Any G1 residual ≠ 0 (total ≠ V or Π(b) ≠ 0 for some rational b); a measured n=5 revenue NOT ≥3σ below the naive n·(V/2), or not within 3σ of V; any robustness cell with R̂/V outside 3σ of 1; or a digest mismatch under independent re-implementation.
**6. Is it distinct from every prior head (dedup)?** Yes — `grep -ri` across ideas/** for all-pay / rent dissipation / rent-seeking / Tullock / war-of-attrition is clean (only a forward-looking mention in the P199 card). Distinct from Vickrey (winner-pays, truthfulness), balance-triangle (matrix value), and price-of-anarchy/Braess (routing). See Dedup.
**7. Is the grounding real and specific to this head?** Yes — Wikipedia "All-pay auction" rev 1345188183 states firsthand, for the complete-information case, "The Nash equilibrium is such that each bidder plays a mixed strategy and expected pay-offs are zero" — exactly the break-even / full-rent-dissipation leg of this head, and it names the mixed-strategy complete-information equilibrium. Honest caveat: the page does not print the words "total bids = V"; the exact R = V is the arithmetic consequence of zero net payoff + win-prob 1/n (phenomenon-on-page, derived here firsthand). A second caveat: the page's worked "E[R] = 1/3" example is the DIFFERENT incomplete-information / independent-private-values model (uniform valuations), not our common-value complete-information model — disclosed in Model basis.
**8. What does it unblock / why does sim-lab care?** It gives the fleet an exactly-verified warning — with a reusable stdlib all-pay-equilibrium harness — that winner-take-all-pay contests (leaderboard grinds, top-contributor drives, war-of-attrition events) dissipate exactly the prize value no matter the crowd size and leave every entrant breaking even, so total extracted effort cannot be grown by enlarging the field.

**Recommendation: sim-ready**
