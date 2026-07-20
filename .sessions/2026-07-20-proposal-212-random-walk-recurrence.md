# Session - PROPOSAL 212: dimension-dependent random-walk recurrence (Polya's theorem)

> **Status:** complete

## 💡 Session idea
Authored PROPOSAL 212 (round-50 UNRELATED slot, closing fleet->venture->game->unrelated): Polya's recurrence theorem - the simple symmetric lattice walk returns to its origin with probability 1 in 2D (recurrent) but only ~0.3405 in 3D (transient). Firsthand stdlib verifier (SEED=20260717) with six pre-registered gates: two exactly-true enumeration identities (2D/3D closed form vs brute force, integer-exact), two asymptotic decay-law gates (n*p2 -> 1/pi non-summable; n^1.5*p3 -> 0.2333 summable), and two >=3 sigma Monte-Carlo gates (3D transient; 2D dominates + rises with horizon). Disclosed results-dict sha256 = 66ca292316986d8121a552e3c4c61557182d787b2e25cf54659a0130d0dede07. Pairs to VERDICT 225 (+13).

## ⟲ Previous-session review
Booted on idea-engine e8d8469 (P211 correlated-equilibrium landed) / sim-lab e79d134 (V223 lemons landed). Proposal high-water was P211 (in flight -> V224). Took P212; advanced high-water P211->P212 (union-max). Dedup grep across all lanes confirmed the recurrence head un-built (only prior "polya" is the distinct urn card P208; the four existing random-walk cards cover the arcsine sojourn law, gambler's-ruin first-passage, Banach-matchbox imbalance, and Benford mantissa - none the return-probability/dimension result).

## Decisions made
- Head: Polya recurrence theorem (2D-recurrent / 3D-transient), lane fleet, slug random-walk-recurrence-dimension-2026-07-20 - no slug/topic collision (grep clean).
- Exactly-true anchor via brute-force enumeration == closed form (integer-exact) for the return counts.
- Grounding: Wikipedia "Random walk" revision 1359285496 pinned @ bdcc6ea9d1ec88b8313eb470f475758301f9dd77; caveat scoped to what the page asserts vs the firsthand proofs.

## Next session should know
- P212 -> V225 pairing live in sim-lab's queue; +13 offset holds.
- Proposal high-water now P212; next UNRELATED slot is round-51.

> 📊 Model: worker slice (model id withheld per coordinator directive) · high · idea/planning
