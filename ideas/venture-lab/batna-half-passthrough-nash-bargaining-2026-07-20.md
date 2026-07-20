# Improving your walk-away option by a dollar wins only fifty cents at the table: the symmetric Nash bargaining split moves your final share by exactly one-half of any gain in your threat point, and the other half dissolves into the shrinking surplus the two of you divide

> **State:** sim-ready
> **Class:** venture / negotiation / cooperative-bargaining
> **Target:** sim-lab (VERDICT 227, +13 offset)
> **Grounding:** https://en.wikipedia.org/w/index.php?title=Cooperative_bargaining&oldid=1357241381@3874ef53eaa5cc3033622ca373fbfb836e9f0119 · fetched 2026-07-20T13:46:18Z
> **Reference (external, reachable):** https://en.wikipedia.org/wiki/Cooperative_bargaining — states the Nash bargaining solution as the unique allocation maximizing the product of utility gains over the disagreement point under Nash's four axioms.
> **Harvest source (firsthand):** the partial-x1/partial-d1 = 1/2 threat-point pass-through, the closed-form-vs-exhaustive-enumeration agreement, the alpha-shift robustness, and the conservation/falsifiability legs are encoded and gate-verified in ideas/venture-lab/batna-half-passthrough-nash-bargaining-2026-07-20.py and its recorded double-run.

## The phenomenon (one line)
Strengthen your no-deal fallback by a dollar and, under the Nash bargaining solution, your negotiated share rises by exactly fifty cents — never the full dollar.

## The folk belief
A better outside option (BATNA) is pure leverage: every dollar you can credibly walk away to is a dollar you should be able to extract at the table, one-for-one. Improve your fallback by X and your deal should improve by X.

## The mechanism (reasoned to its fuller form — Q-0254 duty)
Two parties split a fixed total S. If they fail to agree, player 1 gets d1 and player 2 gets d2 (their threat/disagreement points). Only the surplus s = S − d1 − d2 is actually up for negotiation. The Nash bargaining solution selects the split maximizing the product of gains (x1 − d1)(x2 − d2) subject to x1 + x2 = S — the unique point satisfying Pareto efficiency, symmetry, scale-invariance, and independence of irrelevant alternatives.

Maximizing (x1 − d1)(x2 − d2) with x2 = S − x1 gives the closed form
  x1 = d1 + s/2 = (S + d1 − d2)/2,   x2 = d2 + s/2 = (S − d1 + d2)/2 —
each party keeps its threat point and splits the surplus evenly.

Now raise player 1's threat point by δ (d1 → d1 + δ), holding the total S fixed. The surplus s = S − d1 − d2 SHRINKS by δ. The new share is
  x1' = (S + (d1 + δ) − d2)/2 = x1 + δ/2.
So ∂x1/∂d1 = 1/2, exactly. Half of your improved threat converts to a better deal; the other half is absorbed because the pie the two of you split just got smaller by δ, and you each carry half of that shrinkage. The one-for-one leverage intuition double-counts: it credits you the full δ AND leaves the surplus split untouched, so x1 + x2 would sum to S + δ — conjuring value from nowhere.

The half is not an artifact of symmetry alone. Under generalized (asymmetric) Nash bargaining with power α on player 1, x1 = d1 + α·s and the pass-through is ∂x1/∂d1 = 1 − α — always strictly between 0 and 1 for any genuine sharing rule, never the folk's 1. Symmetric bargaining (α = ½) is simply the case where the pass-through is exactly one-half. And an alternating-offers negotiation (Rubinstein) with vanishing friction converges to this same split, so the identity is where actual back-and-forth bargaining lands, not merely where the axioms point.

## Pinned world (committed constants, SEED=20260717)
- Transferable-utility bargaining: fixed total S, disagreement (d1, d2), surplus s = S − d1 − d2 ≥ 0.
- Symmetric Nash split x1 = d1 + s/2; generalized split x1 = d1 + α·s.
- G1 exhaustive grid: half-integer grid over the feasible interval, Fraction-exact, 200 seeded problems.
- G2 negotiation model: Rubinstein alternating offers, discount drawn Uniform(0.90, 0.999), first proposer a fair coin, SPE surplus share 1/(1+δ_disc) to the proposer; N = 100000 trials per threat point; d1 = 10 and d1 + δ = 16 (δ = 6), d2 = 4, S = 40.
- G3 α-shift: α ∈ {1/10, …, 9/10}, plus a pie-size-doubling invariance check.
- Digest posture: WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY — the canonical-JSON sha256 of the full results dict IS the digest; the dict carries no hash of itself.

## Gate criteria
`all_pass = G1 ∧ G2 ∧ G3 ∧ G4`.

- **G1 — EXACT (closed form == exhaustive enumeration).** For every seeded symmetric problem, the closed-form split x1 = (S + d1 − d2)/2 is the unique argmax of the Nash product over the exhaustive half-integer grid (Fraction-exact). Direction: exact agreement AND unique maximizer on 100% of problems.
- **G2 — SURPRISE (≥3σ; a half, not a whole).** From the simulated alternating-offers negotiation, the estimated pass-through β̂ of a threat-point gain rejects the folk full-pass-through value 1.0 at z ≥ 3 while staying consistent with ½ (|β̂ − ½| ≤ 0.02). Direction: z_reject_folk ≥ 3 (high) and β̂ ≈ ½ (deviation low).
- **G3 — ROBUSTNESS (α-shift).** Across the bargaining-power shift α ∈ {0.1,…,0.9}, the pass-through equals 1 − α exactly (Fraction), lies strictly in (0, 1) for every α, and is invariant to pie size — never the folk 1.0. Direction: exact match to 1 − α AND strict interiority on 100% of the grid.
- **G4 — EXACT identity + FALSIFIABILITY.** Surplus conservation x1 + x2 = S and individual rationality x1 ≥ d1, x2 ≥ d2 hold exactly on every seeded problem; the deliberately-wrong folk accounting (full pass-through, counterparty's share held fixed) is REJECTED because it violates conservation (sums to S + δ). Direction: conservation + IR hold on 100%; folk model falsified on 100%.

## Measured results (this run)
Results-dict sha256 = `47e09254b86486e2cdff63e54ec8a276287f4f00806cf32e0fb52daa5cb4f434`
all_pass = **true**
- G1: 200/200 problems — the closed form is the unique Nash-product argmax on all 200.
- G2: β̂ = 0.5 (mean x1 at d1 = 23.000283, at d1+δ = 26.001930); z_reject_folk = 1917.499 (≥ 3 ✓), z_consistent_with_half = 1.054 (< 3 ✓).
- G3: pass-through = 1 − α exactly, strictly in (0,1), pie-size invariant, for all 9 values of α.
- G4: conservation + individual rationality 200/200; folk full-pass-through falsified 200/200.

## Caveats & crossovers (honest disclosure)
- **Grounding scope (accurate).** The pinned revision (oldid 1357241381, wikitext sha1 3874ef53…0119) DOES state the Nash bargaining solution as the unique allocation maximizing the product of utility gains over the disagreement point — verbatim "(u(x)−u(d))(v(y)−v(d))" — lists Nash's four axioms (invariance to affine transformations, Pareto optimality, independence of irrelevant alternatives, symmetry), uses the disagreement/threat-point concept with the notation d throughout, and DOES discuss the Rubinstein alternating-offers game converging to the Nash solution in the patient limit. It does NOT give the symmetric surplus-splitting closed form x1 = (S + d1 − d2)/2, does NOT compute the ∂x1/∂d1 = ½ threat-point pass-through, and does NOT discuss the generalized/asymmetric (1 − α) pass-through — those three are proven firsthand in the verifier. The page is cited for the underlying solution concept and axioms, not the pass-through identity itself.
- **Not adverse selection, not screening.** This concerns cooperative bargaining over a known surplus. It is distinct from the shipped venture-lab info-economics docs — Akerlof adverse-selection collapse (lemons-market-collapse) and Stiglitz/Rothschild independent screening (independent-screens-odds-ladder): those turn on hidden types and information; this turns on threat points in a full-information split.
- **Not double marginalization.** partner-channel-margin-stacking (shipped) concerns sequential monopoly markups; this is a two-party surplus division, a different mechanism with a different closed form.
- **Transferable utility.** The exact ½ is stated for TU (linear utility frontier). With a strictly concave frontier the pass-through is still fractional and < 1 but no longer exactly ½; the α-generalization (1 − α) captures the asymmetric-power case. G3 documents that the fractional-pass-through claim is robust while only the symmetric value is exactly ½.
- **Rubinstein as convergence, not proof.** G2's negotiation model recovers the split as its small-friction expectation with genuine sampling variance; it is evidence that the identity is where bargaining lands, not a second proof of the closed form — that exact job belongs to G1 and G4.

## Probe report
**1. Is the head crisp and falsifiable?** Yes — a single scalar claim, ∂x1/∂d1 = ½ (symmetric TU Nash), falsified by any measured pass-through ≠ ½ or any conservation violation.
**2. Is it counterintuitive but true?** Yes — the one-for-one BATNA-leverage intuition is widespread and wrong; the true pass-through is exactly one-half, proven by closed form and exhaustive enumeration.
**3. Is the model clean and fully pinned?** Yes — TU split, fixed S, seeded constants, an α-grid, and an alternating-offers model with every constant committed under SEED=20260717.
**4. Is there an exactly-true gate?** Yes — G1 (closed form == exhaustive Nash-product argmax) and G4 (conservation + IR) are Fraction-exact, and G3's 1 − α is exact.
**5. Is it deterministic and reproducible?** Yes — the Fraction-exact legs are noiseless; the MC leg uses one seeded generator with fixed draw order, verified byte-identical across an in-process double-run and a separate cross-invocation.
**6. Is the grounding real and external?** Yes — a pinned Wikipedia revision (oldid + wikitext sha1), reachable, with a caveat scoped to exactly what the page states versus what the verifier proves firsthand.
**7. Could it collide with a shipped proposal?** No — Nash bargaining has zero prior docs across all lanes; the nearest venture neighbors (lemons adverse selection, independent screens, margin stacking) are distinct mechanisms, disclosed above. Not Kelly, not gambler's-ruin, not double-marginalization.
**8. What would make sim-lab reject it?** A reproduced β̂ far from ½, a broken conservation identity, a digest mismatch on SEED=20260717, or a grounding caveat that misstates the pinned page.

**Recommendation: sim-ready**
