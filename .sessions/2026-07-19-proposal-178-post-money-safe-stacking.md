# PROPOSAL 178 — post-money SAFEs don't share dilution: stacking taxes founders convexly (round-42 VENTURE slot, P178 → V191, +13)

> **Status:** `in-progress`
> 📊 Model: Claude Opus · high · idea/planning

Born-red HOLD: this card lands as the FIRST commit with `Status: in-progress` to hold the PR red on the substrate docs-gate. It flips to `complete` as the final commit of the slice, once the verifier, proposal doc, and outbox block are in place and `python3 bootstrap.py check --strict` is green.

## Objective
Author PROPOSAL 178 for the round-42 VENTURE slot: a fresh, documented, quantifiable startup-economics mechanism. Head — for a stack of SAFEs with aggregate post-money ownership x, founders retain 1−x under post-money SAFEs but 1/(1+x) under pre-money SAFEs; the post-money "stacking tax" is x²/(1+x), strictly positive and convex in x, so each additional SAFE costs the founder disproportionately more. Pairs with sim-lab VERDICT 191 (+13).

## Constraints honored
- Fresh mechanism — dedup search across ideas/venture-lab/ (20 existing verifiers) found no SAFE / convertible-note dilution mechanism; nearest cousins (option-pool-shuffle, founder-dilution-waterfall, full-ratchet-convexity) are option-pool / liquidation-preference / down-round mechanics, disclosed in the proposal doc's caveats.
- Verifier: stdlib-only, SEED=20260717 pinned, deterministic in-process double-run + identical cross-invocation output, ≥3σ gates including a robustness gate under a shifted (heavier-stacking) distribution; prints the results dict and its sha256.
- Digest posture WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY (P127+ twist), floats 6 dp.
- Timestamps from `date -u`; family-level model name only.

## Gate-plan (pre-registered — must match the shipped verifier)
- **G1 — post-money strictly more dilutive:** mean founder tax (f_pre − f_post) > 0 with z ≥ 3.
- **G2 — convex in stack size:** mean tax in the top-x tercile ≥ 3× the bottom-x tercile, the difference significant at z ≥ 3.
- **G3 — robustness under heavier stacking:** under a shifted distribution (more SAFEs, lower caps → larger x) the tax stays positive (z ≥ 3) and its mean strictly exceeds the baseline mean (z ≥ 3) — the effect strengthens, not reverses.
- all_pass = G1 ∧ G2 ∧ G3.

## GROUNDING (verified at HEAD)
Repo pinned at main HEAD `a1aa6a579634a5ec0cead1bfdf73fa471b8fd27a`. Mechanism grounded in the documented post-money SAFE contract term that a post-money SAFE holder's ownership is fixed and not diluted by other SAFEs or the option-pool top-up, whereas pre-money SAFEs share dilution on a common conversion base. External reference verified live HTTP 200 this session (Wikipedia "Simple agreement for future equity"; corroborated by Avisen Legal), recorded in the proposal doc.

## Probe questions
**1. Is the pre-money founder-retention 1/(1+x) a defensible mechanic, not just convenient algebra?**
Yes — a share-count derivation gives it: a pre-money SAFE i buys o_i·N0 shares on the founders' pre-SAFE base N0, so total shares = N0(1+x) and founders keep N0/(N0(1+x)) = 1/(1+x); each pre-money holder ends with o_i/(1+x) < o_i, i.e. the SAFEs dilute each other.
**2. Does the tax ever go negative (post-money ever cheaper for the founder)?**
No — x²/(1+x) > 0 for all x > 0; G1 confirms it across 200k sampled stacks.
**3. Is this a duplicate of an existing venture-lab idea?**
No — the 20 existing verifiers cover option pools, liquidation waterfalls, ratchets, IRR, take-rates, churn/LTV; none model SAFE-vs-SAFE dilution sharing. Disclosed in caveats.
**4. Does the effect survive a heavier-stacking distribution?**
G3 tests exactly this: more SAFEs and lower caps push x up; the tax stays positive and its mean grows.
**5. What real decision does this change?**
A founder choosing between a pre-money and a post-money SAFE at the same cap and check should price the post-money "cleaner accounting" convenience against a convex dilution tax that compounds with each additional SAFE.

## Outcome
Pending — born-red HOLD. Filled at flip with the actual gate z-scores, the results-dict sha256, and the PR / merge references.

## ⟲ Previous-session review
PROPOSAL 177 (round-42 FLEET slot, two-choices-marginal-probe) landed via PR #670, advancing proposal high-water P176 → P177. This slice continues round-42 into the VENTURE slot (P177 → P178), pairing with sim-lab VERDICT 191.

## 💡 Session idea
The dilution-sharing contrast generalizes: any instrument whose ownership is fixed post-money (rather than sharing dilution pre-money) imposes a convex tax on the residual claimant — a candidate cross-cutting "fixed-vs-shared dilution" family spanning SAFEs, warrants, and anti-dilution top-ups.
