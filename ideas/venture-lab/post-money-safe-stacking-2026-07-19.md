# Post-money SAFEs don't share dilution: stacking them taxes founders convexly

> **State:** sim-ready
> **Class:** venture-lab · fundraising / SAFE dilution
> **Target:** sim-lab (VERDICT 191, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine@a1aa6a579634a5ec0cead1bfdf73fa471b8fd27a · fetched 2026-07-19T17:38:00Z
> **Reference (external, reachable):** https://en.wikipedia.org/wiki/Simple_agreement_for_future_equity — verified live HTTP 200 this session; corroborated by https://www.avisenlegal.com/pre-money-vs-post-money-safes-the-dilution-math-founders-miss/ (HTTP 200).
> **Harvest source (firsthand):** Wikipedia, "Simple agreement for future equity": "Under this structure, the dilution from issuing several SAFEs falls on the founders rather than being shared among the SAFE holders."

## The phenomenon (one line)
Swapping a pre-money SAFE for a post-money SAFE at the same cap and check moves the whole burden of every *other* SAFE's dilution onto the founder — and stacking SAFEs makes that burden grow faster than the count.

## The folk belief
The post-money SAFE (YC's 2018 standard) is sold to founders as "cleaner accounting": same cap, same check, easier to model exactly how much of the company has been sold. The corollary founders infer is that it costs them nothing extra versus the older pre-money SAFE.

## The mechanism (reasoned to its fuller form — Q-0254 duty)
Write each SAFE's post-money ownership target as o_i = investment_i / post_money_cap_i, and let x = Σ o_i be the aggregate ownership the SAFE stack represents.

**Post-money regime.** By contract a post-money SAFE holder's percentage is fixed on a post-all-SAFEs basis and is *not* diluted by the other SAFEs or by the option-pool top-up. So the holders collectively own exactly x and the founders retain

f_post = 1 − x.

**Pre-money regime.** A pre-money SAFE converts on the founders' pre-SAFE fully-diluted base N0: SAFE i buys s_i = o_i·N0 shares, so the post-conversion total is N0 + Σ s_i = N0(1 + x). The founders retain

f_pre = N0 / (N0(1+x)) = 1 / (1 + x),

and each pre-money holder ends up with o_i/(1+x) < o_i — the SAFEs dilute *each other*, so the founder's slice of the dilution is smaller.

**The stacking tax.** Choosing post-money over pre-money at identical caps and checks costs the founder

tax(x) = f_pre − f_post = 1/(1+x) − (1−x) = x² / (1 + x).

This is strictly positive for any x > 0 and convex/super-linear in x: the marginal cost of the next SAFE rises as the stack grows. Two $250k SAFEs at a $10M cap (x = 0.05) cost the founder ~0.24 points; a stack reaching x = 0.40 costs ~11.4 points — roughly 48× the tax for 8× the ownership sold, because the tax scales with x², not x. That convexity is the counterintuitive part the "cleaner accounting" framing hides.

## Pinned world (committed constants, SEED=20260717)
Verifier `ideas/venture-lab/post_money_safe_stacking.py`, stdlib-only, SEED=20260717, TRIALS=200,000 per distribution.
- Baseline stack: k ~ U{2..6} SAFEs; each investment ~ U(0.25, 2.0) $M, cap ~ U(5, 20) $M; o_i = inv/cap; reject-and-resample any stack with x ≥ 0.85 (a company cannot sell >85% via SAFEs).
- Shifted (heavier-stacking) stack: k ~ U{3..8}, cap ~ U(3, 12) $M (lower caps and more SAFEs ⇒ larger x), same investment range and reject rule.
- For each stack: f_pre = 1/(1+x), f_post = 1−x, tax = f_pre − f_post.

## Gate criteria
A verdict session can reproduce all three at SEED=20260717 and check them independently.
- **G1 — post-money strictly more dilutive:** mean tax over the baseline sample > 0 with z = mean / (sd/√N) ≥ 3.
- **G2 — convex in stack size:** split the baseline sample into x-terciles; mean tax in the top-x tercile ÷ mean tax in the bottom-x tercile ≥ 3.0, and the top−bottom difference is significant at z ≥ 3.
- **G3 — robustness under heavier stacking:** on the shifted distribution the tax stays positive (z ≥ 3) *and* its mean strictly exceeds the baseline mean (z ≥ 3) — the effect strengthens, it does not reverse.
- **all_pass = G1 ∧ G2 ∧ G3.**

Digest posture: WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY (P127+ twist) — the sha256 of the compact-canonical results dict IS the digest; stdout is the pretty indent=2 dump (floats 6 dp); no on-disk JSON. The verifier runs `compute()` twice in-process and asserts the two dicts are identical before printing, and two separate invocations produce byte-identical stdout.

## Measured results (this run)

```
{
  "all_pass": true,
  "baseline": {
    "mean_tax": 0.127846,
    "mean_x": 0.403207,
    "rejects": 4862,
    "sd_tax": 0.090528
  },
  "gate_G1_postmoney_more_dilutive": {
    "mean_tax": 0.127846,
    "pass": true,
    "z": 631.562768,
    "z_gate": 3.0
  },
  "gate_G2_convex_in_stack": {
    "mean_tax_high_x": 0.235555,
    "mean_tax_low_x": 0.037163,
    "pass": true,
    "ratio_gate": 3.0,
    "ratio_high_over_low": 6.338353,
    "z_diff": 824.297,
    "z_gate": 3.0
  },
  "gate_G3_robust_under_heavier_stacking": {
    "mean_tax_base": 0.127846,
    "mean_tax_shift": 0.229045,
    "pass": true,
    "shift_rejects": 260788,
    "z_gate": 3.0,
    "z_increase": 344.175738,
    "z_positive": 1074.028387
  },
  "head": "post-money SAFEs don't share dilution; stacking tax = x^2/(1+x), convex in aggregate SAFE ownership x",
  "proposal": 178,
  "seed": 20260717,
  "trials": 200000,
  "x_cap": 0.85
}
Results-JSON sha256 78758a602a36ba32bc1fd97b77820c97e86abbe7828a160ddbdd22ae7e8b2549
```

## Caveats & crossovers (honest disclosure)
- **Closed-form core.** The two retention formulas are exact given the simplifying share model (no discount, no MFN, single pre-SAFE base; priced-round new money and pool held out of the SAFE-vs-SAFE comparison). The Monte Carlo does not discover the sign — it quantifies the tax's distribution and its convexity across realistic stacks and confirms robustness under a heavier regime. Disclosed rather than dressed up as an empirical surprise.
- **Discounts / MFN ignored.** Real SAFEs often carry a discount and an MFN clause; a discount lowers the effective cap symmetrically in both regimes and changes magnitude, not the sign of the tax.
- **Pool and priced round.** Holding the option-pool top-up and priced-round new money out of both regimes is the conservative choice; including them widens the gap, since a post-money pool refresh dilutes founders alone.
- **Crossovers, not duplicates.** `option-pool-shuffle` (pre-money pool comes from founders), `founder-dilution-waterfall` (liquidation-preference stacking), and `full-ratchet-convexity` (down-round anti-dilution) are the nearest venture-lab neighbors. None models the pre-money-vs-post-money SAFE dilution-sharing distinction; a `git grep -il` over ideas/ for "safe", "post-money", and "convertible" returned no existing verifier on this head.

## Probe report (v0, self-adversarial)
**1. Is f_pre = 1/(1+x) the right pre-money mechanic, or a convenient fiction?**
It is the share-count result: a pre-money SAFE i buys o_i·N0 shares on the pre-SAFE base N0, total becomes N0(1+x), founders keep 1/(1+x). The o_i/(1+x) < o_i outcome for each holder is exactly the "SAFEs dilute each other" the sources describe.
**2. Could post-money ever be the cheaper choice for the founder?**
No, on this comparison: tax(x) = x²/(1+x) > 0 for every x > 0. Post-money is never cheaper at equal caps and checks; it can be preferable for other reasons (transparency, control) but not on founder retention.
**3. Is the convexity real or an artifact of the tercile split?**
Real: tax(x) = x²/(1+x) has positive second derivative for x > 0; the tercile ratio (G2) is one legible witness, and the shifted-distribution gate (G3) independently shows the mean tax rising as the stack gets heavier.
**4. Does the head reverse under a different distribution?**
G3 pushes caps down and SAFE counts up (x larger); the tax stays positive with z ≥ 3 and its mean strictly rises. The sign is distribution-free (it is x²/(1+x)); only the magnitude moves.
**5. Is this a duplicate of an existing venture-lab proposal?**
No — see the crossovers caveat and the disclosed `git grep` dedup search. The 20 existing verifiers cover option pools, liquidation waterfalls, ratchets, IRR, take-rates, churn/LTV, billing variance; none touches SAFE-vs-SAFE dilution sharing.
**6. What would make a verdict session REJECT?**
A non-reproducing digest, a gate that misses its z-threshold, or a demonstration that a mainstream SAFE mechanic (e.g. standard post-money conversion including the pool) reverses the sign. The pool-excluded framing is chosen so the head does not depend on the most aggressive assumption.
**7. Is the grounding source authoritative and live?**
Wikipedia's SAFE article (verified HTTP 200 this session) states the dilution "falls on the founders rather than being shared among the SAFE holders"; Avisen Legal (HTTP 200) documents stacking three or four post-money SAFEs as a common way founders reach Series A with less ownership than expected. Both resolve live.
**8. What does a founder do differently after reading this?**
Model the post-money convenience as a convex tax: negligible for a single small SAFE, but a stack of four post-money SAFEs at a low cap can cost several extra points of ownership versus the same pre-money stack — a term-sheet conversation, not a rounding error.

**Recommendation: sim-ready**
