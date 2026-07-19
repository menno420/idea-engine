# Full-ratchet anti-dilution turns a down round into a convex, super-linear transfer of shares to the ratcheted investor — and strictly beats weighted-average dilution at the founders' expense

> **State:** sim-ready
> **Class:** counterintuitive-captable / venture-lab (fundraising / dilution slot)
> **Slot:** round-39 VENTURE
> **Target:** sim-lab (VERDICT 179, +13 offset)
> **Grounding:** https://github.com/menno420/idea-engine/blob/cd13dcd27640ff2d95f3b5ee62833d30d2cc19d7/control/outbox.md@924aba8100f6a3d7394c6d20ef85113bc61a08f8 · fetched 2026-07-19T10:42:45Z
> **Reference (external):** Wikipedia (Stock dilution) — https://en.wikipedia.org/w/index.php?title=Stock_dilution&oldid=1359000150 (HTTP 200, fetched 2026-07-19T10:42:45Z): "Many venture capital contracts contain an anti-dilution provision in favor of the original investors, to protect their equity investments."
> **Harvest source (firsthand):** ideas/venture-lab/full_ratchet_convexity.py + its recorded double-run (this branch).

## The phenomenon (one line)
On a down round a full-ratchet anti-dilution clause resets the earlier investor's conversion price all the way to the new, lower price, so the extra shares they receive scale as d/(1-d) in the drop d — a convex, super-linear transfer — while a broad-based weighted-average clause only partially adjusts and hands over strictly fewer shares.

## The folk belief
"Anti-dilution is anti-dilution, and a down round costs founders about as much as the price fell." Two errors hide here: the choice of ratchet formula is treated as a lawyer's footnote, and the cost is imagined as proportional to the price cut. Both are wrong — full ratchet is strictly worse for founders than weighted-average, and the share transfer is convex in the depth of the cut.

## The mechanism (reasoned to its fuller form — Q-0254 duty)
Let the pre-round fully-diluted cap be A0 (normalized to 1). A prior investor holds N_A as-converted shares bought at conversion price P_old (=1); founders/common hold N_C = A0 - N_A. A down round raises `money` at P_new = p*P_old with p in (0,1) and drop d = 1-p, issuing N_B = money/P_new new shares. The investor's anti-dilution resets their conversion price CP, multiplying their as-converted count by P_old/CP; the extra shares are dAD = N_A*(P_old/CP - 1), issued from the company and diluting common.

- Full ratchet: CP = P_new = p, so dAD_FR = N_A*(1/p - 1) = N_A*d/(1-d). This is convex and increasing in the drop: doubling d more than doubles dAD_FR, because dAD_FR(2d) - 2*dAD_FR(d) = 2*N_A*d*[1/(1-2d) - 1/(1-d)] > 0 for every d in (0, 1/2).
- Broad-based weighted-average: CP = P_old*(A + B)/(A + C) with A = A0, B = money/P_old, C = N_B. Because CP stays strictly above P_new, dAD_WA < dAD_FR on every scenario.

Founder ownership loss attributable to anti-dilution is loss = N_C/T - N_C/(T + dAD) with T = A0 + N_B. Since loss is increasing in dAD and dAD_FR >= dAD_WA pointwise, full-ratchet founder loss is strictly larger. The share transfer dAD_FR is the clean convex object; the ownership-fraction loss is a dampened image of it — see the honesty disclosure below.

## Pinned world (committed constants — the verifier is the contract)
SEED=20260717 · N=4000 scenarios per world · z_gate=3.0 · P_old=1.0 · A0=1.0. Baseline world: preferred stake ~U(0.15,0.35), drop d~U(0.08,0.24), raise money~U(0.20,0.50). Shifted world: preferred stake ~U(0.30,0.50), drop d~U(0.15,0.30), raise ~U(0.40,0.80). Floats rounded to 6 dp before hashing; deterministic in-process double-run asserted; cross-invocation byte-identical.

## Pre-registered gates (evaluation order G1 → G2 → G3; APPROVE iff ALL hold, z_gate=3.0)
- **G1 — full ratchet dilutes founders more than weighted-average.** Paired mean of (loss_FR - loss_WA) over the baseline world. Observed **mean 0.012813**, **se 8.2e-05**, **z 155.71** — pass.
- **G2 — the ratchet share transfer is convex (super-linear) in the drop.** Mean of (dAD_FR(2d) - 2*dAD_FR(d)) over the baseline world. Observed **mean 0.028025**, **se 0.000336**, **z 83.28** — pass. This rejects the proportional folk belief.
- **G3 — both hold in a shifted world** (heavier preferred, larger raise, deeper drops). Observed FR-minus-WA loss **z 203.90** (mean 0.013013) and transfer convexity **z 106.65** (mean 0.112724) — pass.

Non-gated honesty disclosure: `nongated_fraction_convexity_mean` = **0.001305** — the ownership-*fraction* second difference is small and, unlike the share transfer, is **not** globally positive: new-money issuance inflates the base T, so for deep enough rounds the fraction loss saturates and its convexity fails. The convexity claim is therefore scoped to the **share transfer**, not the fraction. The `nongated_shallow_crossover` (drop=0.02) shows FR loss 0.00207 vs WA 0.000538 (gap 0.001532) — near a flat round the two clauses nearly coincide; the transfer opens as the drop deepens.

## Pre-registered decision rule
APPROVE iff G1 and G2 and G3 all hold at z >= 3.0 with `all_pass = **true**` and `first_failing_gate = **null**`, the verifier exits 0, and the reproduced results-dict sha256 matches EXACTLY. Any gate below 3σ, any sign flip, a nonzero exit, or a digest mismatch is a REJECT.

## Disclosed verifier (the sim-lab spec)
`ideas/venture-lab/full_ratchet_convexity.py` — stdlib only (hashlib, json, math, random, statistics). WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY: the ordered results dict is dumped pretty (indent=2, sort_keys) then its canonical (sort_keys, tight-separator) JSON is hashed; the digest is printed on the trailing `sha256:` line and is not stored inside the dict. **Expected results-dict sha256:** `c6c1278f5acb6cc59992e7d4300e69edfc713bef0168cd9571e85c4677c18b59`.

## Why it matters
Founders negotiating a term sheet routinely trade away "weighted-average vs full ratchet" as boilerplate while anchoring on the headline valuation. This head quantifies the cost of that trade: the ratchet's bite is convex in how far the next round falls, so the clause that looks harmless at a flat round becomes the dominant dilution term in exactly the scenario it triggers — a down round. It gives a verdict-checkable number for "how much worse is full ratchet," and bounds the claim honestly to the share transfer.

## Dedup (contrast vs prior lane heads)
Distinct from the venture-lab cap-table heads already on file: founder-dilution-waterfall (liquidation-preference payout ordering at exit) and option-pool-shuffle (pre- vs post-money pool top-up) both concern static cap-table construction; this head is about the dynamic anti-dilution response to a down round and the convexity of that response — a mechanism neither prior head touches. No existing venture-lab file models anti-dilution conversion-price resets.

## Model basis (declared model-dependence — the P024 discipline)
The result is a property of the standard broad-based weighted-average and full-ratchet conversion-price formulas (NVCA / Venture-Deals model terms) applied to a normalized single-prior-investor cap table with a single down round and no forfeiture. It assumes: one anti-dilution-protected preferred block, no pay-to-play forfeiture, no carve-outs/exemptions, and a broad-based (fully-diluted) denominator for weighted-average. Relaxing any of these (pay-to-play stripping protection, narrow base, multiple stacked rounds) changes magnitudes and is disclosed as a crossover, not modeled here.

## Gate power + margin ledger
| Gate | Type | Threshold | Observed | z | Verdict |
|------|------|-----------|----------|-----|---------|
| G1 | FR-WA founder loss (baseline) | z >= 3.0, mean > 0 | mean 0.012813, se 8.2e-05 | 155.71 | pass |
| G2 | transfer convexity (baseline) | z >= 3.0, mean > 0 | mean 0.028025, se 3.36e-04 | 83.28 | pass |
| G3a | FR-WA founder loss (shifted) | z >= 3.0, mean > 0 | mean 0.013013, se 6.4e-05 | 203.90 | pass |
| G3b | transfer convexity (shifted) | z >= 3.0, mean > 0 | mean 0.112724, se 1.057e-03 | 106.65 | pass |

## Probe report (v0, self-adversarial)
**1. Is the convexity just an algebraic tautology (d/(1-d) is obviously convex)?** Partly by design — the share-transfer convexity is provable, and the verifier confirms it survives the sampling and the 6-dp rounding; the non-trivial content is that the fraction loss does NOT inherit it (disclosed non-gated) and that full ratchet strictly beats weighted-average on every scenario (G1).
**2. Could weighted-average ever exceed full-ratchet dilution?** No — full ratchet is the maximal conversion-price reset, so dAD_FR >= dAD_WA pointwise; G1's z=155 reflects a strict per-scenario gap, not a distributional artifact.
**3. Does the claim depend on the drop range chosen?** The gated drop bands (0.08-0.24 baseline, 0.15-0.30 shifted) keep 2d < 1 so the double-depth transfer is defined; the shallow crossover (drop=0.02) is disclosed to show the clauses converge at a near-flat round, bounding the claim to genuine down rounds.
**4. Is the proportional folk belief a strawman?** It stands in for the common founder expectation that a d-percent cut costs about d-percent; G2 rejects it by showing the transfer at double depth exceeds twice the single-depth transfer at z=83.
**5. Are FR and WA evaluated on the same draws?** Yes — each scenario draws one (stake, drop, raise) tuple and evaluates both clauses on it, so G1 is a within-scenario paired difference and the SE is conservative.
**6. Does the digest depend on machine floats?** All reported floats are rounded to 6 dp before hashing; the canonical-dict sha256 is asserted stable across the in-process double-run and reproduced byte-identical across two separate processes this session.
**7. What breaks the mechanism first?** Pay-to-play forfeiture (a non-following investor can lose anti-dilution entirely), narrow-vs-broad base, and stacked multi-round conversions all change magnitudes; the model is scoped to a single standard broad-based clause with no forfeiture, disclosed under Model basis.
**8. What does the verdict session check?** Reproduce ideas/venture-lab/full_ratchet_convexity.py byte-for-byte under SEED=20260717, match the results-dict sha256 c6c1278f5acb6cc59992e7d4300e69edfc713bef0168cd9571e85c4677c18b59 EXACTLY, and confirm G1/G2/G3 z-margins with all_pass=true, first_failing_gate=null, exit 0.

**Recommendation: sim-ready**
