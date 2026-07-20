# A first-price auction and a second-price auction hand the seller the same expected revenue — exactly (n-1)/(n+1) — even though nobody pays the same way.

> **State:** sim-ready
> **Class:** venture / mechanism-design / auction-revenue
> **Target:** sim-lab (VERDICT 235, +13 offset)
> **Grounding:** https://en.wikipedia.org/w/index.php?title=Revenue_equivalence&action=raw&oldid=1332022174@555839d12a9b03dd50bad5bb284c1f6c50259000 · fetched 2026-07-20
> **Reference (external, reachable):** https://en.wikipedia.org/wiki/Revenue_equivalence — states the revenue equivalence theorem and the first-price = second-price equivalence under symmetric independent private values; carries a two-player Uniform[0,1] worked example (revenue 1/3).
> **Harvest source (firsthand):** `ideas/venture-lab/revenue-equivalence-first-second-price.py` and its recorded double-run (SEED=20260717).

## The phenomenon (one line)
With n bidders whose private values are i.i.d. Uniform(0,1), a sealed-bid first-price auction and a sealed-bid second-price (Vickrey) auction produce identical expected seller revenue: exactly (n-1)/(n+1).

## The folk belief
"First-price auctions raise more money — bidders actually pay what they bid, instead of only the runner-up's price." Or the stronger confusion: "the seller ends up capturing the winner's valuation." Both are false. Charging the full bid is exactly offset by bidders shading their bids down to (n-1)/n of their value, and the winner always keeps an information rent.

## The mechanism (reasoned to its fuller form — Q-0254 duty)
- Second-price: truthful bidding is dominant, so the winner (highest value) pays the second-highest value. Expected revenue = E[2nd-highest of n U(0,1)] = (n-1)/(n+1).
- First-price: the symmetric Bayesian-Nash bid is b(v) = (n-1)/n * v (your value shaded by the expected maximum of the other n-1 rivals, conditional on winning). The winner pays b(v_max) = (n-1)/n * v_max, so expected revenue = (n-1)/n * E[max] = (n-1)/n * n/(n+1) = (n-1)/(n+1).
- The two mechanisms differ pathwise (a given draw pays different amounts) but the expectations coincide — the revenue equivalence theorem. The gap between the winner's value n/(n+1) and the revenue (n-1)/(n+1) is the information rent 1/(n+1), which vanishes as competition (n) grows.

## Pinned world (committed constants, SEED=20260717)
- Values i.i.d. Uniform(0,1); n bidders; a single `random.Random(20260717)` consumed in a fixed order.
- Gate n's: G2 n=7, N=500k; G3 sweep n in {2,5,10,50} N=150k plus scale k=5, n=6, N=150k; G4 n=7, N=500k.
- Agreement threshold Z_AGREE=3.0; rejection threshold Z_REJECT=5.0.

## Gate criteria (all_pass = G1 and G2 and G3 and G4)
- **G1 — EXACT identity (fractions.Fraction).** For n in {2,3,5,10,20,50}, first-price revenue (n-1)/n * E[max] and second-price revenue E[2nd] are formed by exact polynomial integration (integral of x^j over [0,1] = 1/(j+1)) and must equal each other and (n-1)/(n+1) as identical rationals. Direction: exact algebraic equality.
- **G2 — Monte-Carlo agreement.** Empirical mean revenue of each mechanism, and their paired difference, vs the exact (n-1)/(n+1). PASS = |z|<3 for all three. Direction: fail-to-reject agreement.
- **G3 — Robustness.** (a) Revenue is strictly increasing in n toward 1 and every MC mean agrees (|z|<3); (b) scale invariance: values ~ U(0,k) give revenue k*(n-1)/(n+1) exactly and empirically. Direction: invariance holds.
- **G4 — Falsifiability.** The naive "seller captures the winner's value" model predicts revenue = E[max] = n/(n+1). PASS = that model is REJECTED at |z|>5 while the true model holds (|z|<3). Direction: reject the wrong alternative.

## Measured results (this run)
Results-dict sha256 = `b22b9f2767755feb2334594f2671060c61818e192ee3c24b99f9705e3f9951d2`
determinism_double_run = **true** · cross-invocation byte-identical · all_pass = **true**
- G1: fpa == spa == (n-1)/(n+1) for every n (n=2 -> 1/3, 3 -> 1/2, 5 -> 2/3, 10 -> 9/11, 20 -> 19/21, 50 -> 49/51).
- G2: z_fpa=1.343, z_spa=0.155, z_diff=0.958 — all <3.
- G3: sweep z's {n2:1.696, n5:-0.366, n10:0.666, n50:-0.145}, monotone increasing; scale z_fpa=-1.104, z_spa=-0.373, exact scaled equivalence holds.
- G4: z_vs_naive=-612.81 (naive n/(n+1) model rejected by >600 sigma), z_vs_true=0.639 (<3).

## Caveats & crossovers (honest disclosure)
- **Grounding scope.** The pinned Wikipedia revision (oldid 1332022174) states the revenue equivalence theorem and the first-price = second-price equivalence under symmetric independent private values, and carries a two-player Uniform[0,1] worked example whose revenue is 1/3 — matching our G1 n=2 row. It does NOT contain the general n-bidder closed form (n-1)/(n+1); that identity is our own exact derivation, not a quote. `grep -in "(n-1)/(n+1)"` returned zero hits on the pinned bytes.
- **Crossover.** The "Vickrey truthful dominance" idea covers the dominant-strategy property of second-price bidding; this proposal is disjoint — its core is the revenue identity across two formats and the (n-1)/(n+1) closed form, using truthfulness only as a lemma. The all-pay rent-dissipation idea shares the auction family but concerns full rent dissipation, not format-invariant revenue.
- **Assumptions.** Symmetric bidders, independent private values, risk neutrality, no reserve price. Relaxing symmetry or risk-neutrality breaks the equivalence; that is out of scope and named here to bound the claim.

## Probe report
**1. Is the head crisp and falsifiable?** Yes — a single number (n-1)/(n+1) predicted for two mechanisms; any measured revenue gap between formats, or a mean off (n-1)/(n+1), falsifies it.
**2. Is it counterintuitive but true?** Yes — the intuition that pay-your-bid raises more money is widely held and wrong; equilibrium bid shading exactly cancels it.
**3. Does it have an exact core, not just a simulation?** Yes — G1 proves fpa == spa == (n-1)/(n+1) as identical rationals via exact integration; the Monte-Carlo legs only corroborate.
**4. Is the world fully pinned and deterministic?** Yes — SEED=20260717, single rng in fixed order; double-run and separate re-invocation are byte-identical; results sha256 disclosed.
**5. Are the gates read in independent directions?** Yes — G1 exact equality, G2 fail-to-reject agreement, G3 invariance, G4 reject-the-wrong-model at >5 sigma (measured -612 sigma).
**6. Is the grounding external and honestly scoped?** Yes — pinned Wikipedia revision with matching sha1; the caveat states plainly that the article grounds the theorem and the n=2 case but not the general closed form.
**7. Could a plausible wrong belief survive?** No — the naive "revenue = winner's value = n/(n+1)" model is rejected at |z|=612.8; the residual gap is exactly the information rent 1/(n+1).
**8. What would make sim-lab reject it?** A digest mismatch on re-run, any agreement z>=3, a non-monotone sweep, a broken scale-invariance identity, or the falsifiability model failing to reject — none observed.

**Recommendation: sim-ready**
