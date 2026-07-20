# Add a thousand competing sellers and a one-cent search cost and the price does not fall a single penny toward marginal cost: with any strictly positive cost to inspect one more price, the unique symmetric equilibrium is the full monopoly (reservation) price for every number of sellers — the Bertrand descent to marginal cost never begins, and the competitive limit lives only at exactly zero friction

> **State:** sim-ready
> **Class:** venture / market-microstructure / search-frictions
> **Target:** sim-lab (VERDICT 231, +13 offset)
> **Grounding:** https://en.wikipedia.org/w/index.php?title=Price_dispersion&oldid=1345367307@930ead7d5a9ce98d5ae063c4cbfea4bf3315c63f · fetched 2026-07-20
> **Reference (external, reachable):** https://en.wikipedia.org/wiki/Price_dispersion — the "Search alone is insufficient" section states Diamond's paradox: when consumers each sample only one firm, "each firm acts as a monopoly on its share of consumers" and charges "the monopoly price," and only once all consumers sample at least two firms do prices fall "equal to marginal costs of production, as in a Bertrand economy."
> **Harvest source (firsthand):** the discrete-grid unique-equilibrium enumeration (closed form p*=v == exhaustive best-response fixed point), the N- and s-invariance, the s→0 discontinuity, the monopoly-profit-split identity, and the Bertrand-profile falsifiability leg are encoded and gate-verified in ideas/venture-lab/diamond-search-cost-monopoly-price-2026-07-20.py and its recorded double-run.

## The phenomenon (one line)
Put N identical sellers in a market and charge buyers any strictly positive cost to look at one more price; the unique symmetric equilibrium price is the full monopoly value v — the same for N = 2 and for N = 1000 — so adding competitors lowers the price by nothing.

## The folk belief
More sellers means more competition means lower prices: with many identical firms selling an identical good, Bertrand competition should drive the price down to marginal cost. Each additional competitor should shave the price a little further toward cost.

## The mechanism (reasoned to its fuller form — Q-0254 duty)
A unit mass of buyers each values one unit at v; N sellers have marginal cost 0 and post prices. Buyers search sequentially: the first price they see is free, but inspecting any further seller costs s > 0. Buyers hold rational expectations about the price distribution.

Consider any candidate symmetric equilibrium where every seller charges p. Because buyers expect every seller to charge the same p, a buyer who has sampled one seller has no reason to pay s to sample another — the expected saving is zero and the search costs s > 0. So buyers buy from the first seller they encounter and each seller serves its 1/N first-visit share.

Now let one seller deviate to p_j while all others stay at p. Buyers who first land elsewhere never discover the deviant — they do not search, because they still expect a uniform price. Only the deviant's own first-visit buyers see p_j, and they walk away only if the expected saving from one more search exceeds s, i.e. only if p_j > p + s. So the deviant keeps its entire 1/N captive share for any p_j ≤ min(v, p + s), and — since it can raise price without losing a single captive buyer — its profit-maximizing deviation is p_j = min(v, p + s). Whenever p < v this is strictly greater than p: the seller strictly gains by raising price. So NO price below v survives; the only price a seller cannot profitably raise is p = v, where buyers refuse to pay more (surplus would be negative). Hence the unique symmetric equilibrium is p* = v — the reservation value, which for unit demand is exactly the monopoly price. The number of sellers N never enters the argument, so the result is identical for every N ≥ 2.

The discontinuity is the sharp part. At s = 0 exactly, search is free, buyers observe every price, and the standard Bertrand undercutting logic returns: any p > marginal cost is undercut, so the competitive price obtains. The instant s becomes positive — a penny, a fraction of a penny — the undercutting channel is severed, because a rival's lower price is invisible to a buyer who will not pay to look. The competitive outcome is not the limit of the positive-cost equilibria; it is an isolated point at exactly zero friction. This is Diamond's (1971) paradox: an arbitrarily small search cost flips a competitive market to pure monopoly pricing.

## Pinned world (committed constants, SEED=20260717)
- Sellers: N identical, marginal cost 0; buyers: unit mass, common value v, unit demand.
- Prices on an integer grid {0, 1, …, v}; search cost s a positive integer (≥ one grid step, so a one-step upward deviation is representable on the grid). The continuous-price result is the s→0+ limit; the discrete model represents a positive cost as s ≥ Δ.
- Demand: s > 0 captive-market rule (first sample free and uniform; a buyer keeps its seller iff p_j ≤ min(v, p_bg + s); non-first-visit buyers never search under rational expectations of a uniform price). s = 0 full-information Bertrand rule (buyers observe all prices, buy the cheapest ≤ v, ties split).
- G1 grid: v ∈ [3,20], N ∈ [2,8], s ∈ [1, v−1], 200 seeded problems; equilibria by exhaustive best-response enumeration, Fraction-exact.
- G2: M = 3000 random markets, v ∈ [2,40], N ∈ [2,400], s ∈ [1, max(1, v//4)]; equilibrium solved (not assumed); folk null = marginal cost 0.
- G3: v ∈ [3,15], N ∈ {2,3,5,10}, s ∈ {1, 2, v−1}, plus the s=0 vs s=1 discontinuity check at N=5.
- G4: v ∈ [3,20], N ∈ [2,8], s ∈ [1, v−1]; monopoly-profit-split identity and the folk Bertrand-profile falsification.
- Digest posture: WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY — the canonical-JSON sha256 of the full results dict IS the digest; the dict carries no hash of itself.

## Gate criteria
`all_pass = G1 ∧ G2 ∧ G3 ∧ G4`.

- **G1 — EXACT (closed form == exhaustive enumeration).** For every seeded (N, s>0, v), the closed-form prediction p* = v is the UNIQUE symmetric price equilibrium found by exhaustive best-response enumeration (Fraction-exact). Direction: unique equilibrium equals v on 100% of problems.
- **G2 — SURPRISE (≥3σ; competition does not lower price).** Across random markets with genuine competition (N ≥ 2) and a small positive search cost, the solved equilibrium price rejects the folk marginal-cost/Bertrand prediction (price → 0) at z ≥ 3 while equalling the monopoly price v in every market. Direction: z_reject_folk ≥ 3 (high) and per-market price == v (exact).
- **G3 — ROBUSTNESS (N/s invariance + zero-friction discontinuity).** The equilibrium price is invariant to N and to every positive s (always = v); and the monopoly price v is a symmetric equilibrium IF AND ONLY IF s > 0 (at s = 0 full-information Bertrand undercutting destroys it). Direction: invariance on 100%; iff-s-positive on 100%.
- **G4 — EXACT identity + FALSIFIABILITY.** At the s>0 equilibrium each of the N sellers earns v/N and industry profit = v (the monopoly profit), invariant to N; and the folk Bertrand profile (all sellers at marginal cost 0) is REJECTED as a non-equilibrium because a unilateral upward deviation is strictly profitable. Direction: industry profit == v on 100%; folk profile falsified on 100%; true profile deviation-free on 100%.

## Measured results (this run)
Results-dict sha256 = `c71985cb55577757ed79772b3fabb7677611f3469531c10ab60f8e73a91d8036`
all_pass = **true**
- G1: 200 problems — the closed-form monopoly price v is the unique symmetric equilibrium on all of them.
- G2: mean equilibrium price = 20.757 across 3000 random competitive markets (N up to 400); z_reject_folk_marginal_cost = 100.551 (≥ 3 ✓); price == v in all 3000 markets.
- G3: equilibrium invariant to N and to every positive s (= v) on 120/120; monopoly price is an equilibrium iff s > 0 on 120/120 (the s→0 discontinuity).
- G4: industry profit == monopoly v (split v/N) on 200/200; folk Bertrand profile falsified 200/200; true monopoly profile deviation-free 200/200.

## Caveats & crossovers (honest disclosure)
- **Grounding scope (accurate).** The pinned Price dispersion revision (oldid 1345367307, wikitext sha1 930ead7d5a9ce98d5ae063c4cbfea4bf3315c63f) states Diamond's paradox qualitatively: "This is referred to as Diamond's paradox" (citing Diamond 1971); with one sample per consumer "each firm acts as a monopoly on its share of consumers. Firms choose a price that maximizes profit: the monopoly price"; and the competitive limit needs at least two samples — "prices must be as low as possible: equal to marginal costs of production, as in a Bertrand economy." So the page states the mechanism and both endpoints (positive-cost monopoly pricing; zero-friction Bertrand limit). It does NOT compute the three things the verifier proves firsthand: the discrete-grid exact unique-equilibrium enumeration, the explicit N- and s-invariance (monopoly price for every N ≥ 2 and every s > 0), and the monopoly-profit-split identity (v/N per seller, industry == v) with the Bertrand-profile falsification.
- **Not a contest / all-pay mechanism.** The nearest shipped neighbor, all-pay rent-dissipation (superbot-games lane), is contest theory — bidders sink effort competing for a prize. This is a posted-price search market: the mechanism is buyers' unwillingness to pay a positive cost to observe a rival's price, not effort dissipation.
- **Not double marginalization, not lemons, not Nash bargaining.** partner-channel-margin-stacking (sequential markups), lemons-market-collapse (adverse selection over hidden quality), and batna-half-passthrough-nash-bargaining (cooperative surplus division) are distinct venture-lane mechanisms with distinct closed forms; this turns purely on search frictions in a full-quality, posted-price market.
- **Discrete grid & captive-demand modeling choice.** Prices sit on an integer grid and the positive search cost is s ≥ one grid step; the exact ½-penny language is the continuum idealization. The s>0 demand rule models buyers who do not search off the equilibrium path (rational expectations of a uniform price) — the standard Diamond assumption; it is a model of the search channel, not a claim that every real market's buyers behave so. The s=0 branch recovers Bertrand explicitly, which is what makes the discontinuity firsthand rather than asserted.
- **Homogeneous value.** The exact p* = v uses common valuation v (reservation = monopoly price for unit demand). With heterogeneous valuations the equilibrium is the monopoly price of the induced demand curve rather than v itself; the N-independence and the positive-cost-vs-zero discontinuity survive, but the closed form is argmax p(1−F(p)) instead of v. The pinned constants use the homogeneous case for Fraction-exact gates.

## Probe report
**1. Is the head crisp and falsifiable?** Yes — a single claim, p* = v for every N under any s > 0, falsified by any solved equilibrium below v, any N-dependence, or any failure of the s=0-vs-s>0 discontinuity.
**2. Is it counterintuitive but true?** Yes — "more competitors ⇒ lower price" is the textbook Bertrand intuition; here any positive search cost pins the price at full monopoly regardless of N, proven by exhaustive enumeration.
**3. Is the model clean and fully pinned?** Yes — integer price grid, unit demand, an explicit s>0 captive-search rule and an s=0 Bertrand rule, and every constant committed under SEED=20260717.
**4. Is there an exactly-true gate?** Yes — G1 (unique equilibrium == closed-form v by exhaustive enumeration) and G4 (industry profit == v, split v/N) are Fraction-exact, and G3's N/s-invariance and iff-s-positive checks are exact.
**5. Is it deterministic and reproducible?** Yes — the exact legs are noiseless; the G2 Monte-Carlo uses one seeded generator with a fixed draw order, verified byte-identical across an in-process double-run and a separate cross-invocation.
**6. Is the grounding real and external?** Yes — a pinned Wikipedia revision (oldid + wikitext sha1), reachable, with a caveat scoped to exactly what the page states versus what the verifier proves firsthand.
**7. Could it collide with a shipped proposal?** No — search-friction pricing / the Diamond paradox has zero prior docs across all lanes; the nearest neighbors (all-pay rent-dissipation, margin-stacking, lemons, Nash bargaining) are distinct mechanisms, disclosed above.
**8. What would make sim-lab reject it?** A solved equilibrium below v, any N-dependence of the equilibrium price, a broken monopoly-profit-split identity, a digest mismatch on SEED=20260717, or a grounding caveat that misstates the pinned page.

**Recommendation: sim-ready**
