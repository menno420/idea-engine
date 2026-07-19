# Win the hot round, overpay for it: when K investors bid on the same company the winning valuation is the maximum of K unbiased-but-noisy estimates — so the investor who closes the deal holds, in expectation, the most over-optimistic view, and the overpayment deepens with every additional term sheet

> **State:** sim-ready
> **Class:** counterintuitive-selection / venture-lab (VENTURE slot — pricing / competitive fundraising)
> **Slot:** round-40 VENTURE
> **Target:** sim-lab (VERDICT 183, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine@47e70c45a0e256991b6f957d347af3432faed6cc · fetched 2026-07-19T13:16:33Z
> **Reference (external, reachable):** Winner's curse — the common-value auction result that when K bidders form unbiased but noisy estimates and the top bid wins, the winner's estimate is the maximum order statistic and hence biased above the true value; first named by Capen, Clapp & Campbell (1971). https://en.wikipedia.org/wiki/Winner%27s_curse — verified live HTTP 200 this session. Applied to a competitive VC round, the term-sheet auction is a common-value auction on the company's intrinsic worth.
> **Harvest source (firsthand):** ideas/venture-lab/term_sheet_winners_curse.py + its recorded double-run (this branch).

## The phenomenon (one line)
When K investors compete for the same round, each prices the company at its intrinsic value V0 plus an independent, unbiased estimation error; the founder takes the highest offer, so the winning valuation is the maximum of K noisy draws — and the maximum of unbiased draws is biased high. The winner overpays by the expected top order statistic of the error, which grows with K.

## The folk belief
"A competitive round is validation: more term sheets means the market has confirmed the price, so the winning VC is simply the one who saw the value first." Competition is read as price discovery that converges on the truth, and the winner is presumed the best-informed investor rather than the most-mistaken one.

## The mechanism (reasoned to its fuller form — Q-0254 duty)
Model the round as a common-value auction — every investor bids on the SAME underlying V0, and their disagreement is estimation noise, not taste. A naive (unshaded) bidder offers its own point estimate V0 + eps_i, with eps_i mean-zero. The founder accepts max_i(V0 + eps_i) = V0 + max_i eps_i. Because E[max_i eps_i] > 0 for K >= 2 and rises in K (the expected maximum of K standard normals is about 0.56 sigma at K=2 and 1.42 sigma at K=8), the accepted price sits ABOVE V0 by an amount that deepens with the number of bidders. The winner's realised excess value V0 - price = -max_i eps_i is negative in expectation — the winner overpays — and that overpayment is monotone increasing in K.

The load-bearing twist is selection. Any single investor's estimate is unbiased (E[eps_i] = 0), so ex ante no one is systematically wrong; the bias appears only after conditioning on the event "I won", which selects the most over-optimistic draw. The rational correction is Bayesian shading — bid below your own estimate by the expected winner's-curse margin — but the naive investor who "pays what they think it's worth" is exactly the one the auction punishes. Finally, the effect is not a gaussian artefact: replace the error law with a heavier-tailed, higher-dispersion Laplace world and both the sign and the deepening-in-K survive, and in fact the overpayment grows, because fatter tails make the maximum more extreme.

## Pinned world (committed constants — the verifier is the contract)
SEED=20260717 · V0=1.0 (normalised intrinsic value) · sigma=0.25 (gaussian estimation-error SD) · sigma_heavy=0.35 (Laplace robustness world) · TRIALS=200000 · K in {2, 8} (n_low, n_high) · z_gate=3.0. Bidders are naive/unshaded (bid = own estimate); winner = highest bid; winner excess = V0 - winning bid = -max(eps). Digest posture: WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY — the compact-canonical results dict's own sha256 is the digest.

## Gate criteria (independently checkable by the verdict session)
Run `python3 ideas/venture-lab/term_sheet_winners_curse.py`; it must exit 0, print `all_pass=true`, and print `Results-JSON sha256 e5cdbfec872e5879a66c13029e003fd37b8a8aa72738ec2b1ba7e18030b8e4f7`, byte-identical across two invocations. The three pre-registered gates (z_gate = 3.0):
- **G1 — winner overpays, deepening with K (gaussian):** mean winner excess at K=8 is negative (measured -0.355814) with z=1041.75 >= 3, and more negative than at K=2 (-0.141221) with z=373.85 >= 3 on the difference.
- **G2 — conditional-on-winning reversal:** a single arbitrary bidder's excess is unbiased (measured +0.000385, about 0), while the winner's excess is -0.355814; the gap is negative with z=544.53 >= 3 — the overpayment is a pure selection effect of conditioning on winning.
- **G3 — robustness under a heavier-tailed, shifted world (Laplace, sigma_heavy=0.35):** winner still overpays at K=8 (-0.500907, z=730.51 >= 3) and still deepens with K versus K=2 (-0.185565, z=330.73 >= 3).
- all_pass = G1 AND G2 AND G3 (measured **true**).

## Caveats & crossovers (honest disclosure)
- **Naive-bidding assumption is load-bearing.** The head is a claim about UNSHADED bidders; a fully rational common-value bidder shades and can avoid the curse. The point is that the naive "pay your estimate" strategy — common when investors chase a hot deal on FOMO — is what the auction selects against.
- **Common-value, not private-value.** If investors genuinely value the same company differently (strategic fit, portfolio synergy), part of the dispersion is private value and the curse weakens; the model isolates the common-value component.
- **Unbiased-error idealisation.** Real estimates carry systematic biases (stage, sector hype); the verifier zeroes those on purpose to show the curse arises from noise plus selection alone, not from a pre-existing bias.
- **Crossover with existing venture-lab heads.** This is an order-statistics / selection result on PRICE, distinct from the cap-table mechanics of option-pool-shuffle and founder-dilution-waterfall (which hold price fixed and move ownership); here ownership is fixed and price is the selected quantity. No overlap with the concentration-risk (HHI) or dominance heads.
- **sigma and K are illustrative.** Magnitude scales with estimation dispersion and bidder count; the pinned sigma/K are a representative competitive round, and the gates test direction and monotonicity — which are scale-robust — not the specific dollar magnitude.

## Probe report (v0, self-adversarial)
**1. Is the curse real or just a restatement of "max > mean"?** It is the max-order-statistic effect, but the content is that winning an auction SELECTS that maximum: the average bidder is unbiased (G2 measures +0.000385, ~0) while the winner is not, so the phenomenon is the conditioning, not the arithmetic identity.
**2. Do the >=3 sigma z-values just reflect a huge TRIALS?** No — the effect size is large (winner excess -0.356 at K=8, a 36% overpay on normalised V0=1) relative to the tiny standard error; a null world with no selection leaves winner excess at exactly 0 for any TRIALS, so the gate tests sign and direction, not mere significance.
**3. Is "deepening with K" trivial?** It is the falsifiable half: E[max of K] rises in K, so the overpay must grow from K=2 (-0.141) to K=8 (-0.356) with the difference itself >=3 sigma (z_diff=373.85); a private-value world would show no such monotone deepening.
**4. Could the G2 reversal be an artifact of comparing different draw counts?** The unconditional arm draws one bidder's error directly (mean +0.000385, confirming zero per-bidder bias) and is compared to the K=8 winner from the same error law; the negative gap is the selection effect, isolated by construction.
**5. Is the result a gaussian artifact?** No — G3 re-runs under a heavier-tailed, higher-dispersion Laplace world and both the sign and the deepening-in-K persist (K=8 -0.500907, z=730.51; K=2 -0.185565), and the overpay grows because fatter tails make the maximum more extreme.
**6. Is determinism real?** SEED=20260717 pinned; compute() runs twice in-process and is asserted byte-identical before hashing; the compact-canonical results dict's sha256 (e5cdbfec...30b8e4f7) reproduces cross-invocation (two runs byte-identical, confirmed).
**7. Are sigma and K cherry-picked to force a pass?** No — sigma=0.25 and K in {2,8} are a representative competitive round; the gates test direction and monotonicity, which hold for any sigma>0 and any K>=2 (the expected top order statistic is positive and increasing in K for every mean-zero error law), so no constant sits near a pass margin.
**8. Real venture phenomenon or textbook auction toy?** The winner's curse is a documented, named result (Capen, Clapp & Campbell 1971) and a competitive VC round is a common-value auction on the company's intrinsic worth; the naive "pay your estimate" bid is exactly the FOMO behaviour it warns against, and Bayesian shading is its known correction — disclosed, not hidden.

**Recommendation: sim-ready**
