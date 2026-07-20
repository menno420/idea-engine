# Hex is never a draw: exactly one player connects, so under a uniform random fill P(first player wins) = 1/2 EXACTLY

> **State:** sim-ready
> **Status:** `sim-ready` — PROPOSAL 227 (round-54 GAME slot) → VERDICT 240 (+13 offset)
> **Grounding:** https://en.wikipedia.org/w/index.php?title=Hex_(board_game)&oldid=1361476133@7a7263dbf907f9d92011cf4b8f2af614c632fa4a · fetched 2026-07-20
>
> Verifier (staged in sim-lab): `sims/verdict-240-hex-never-a-draw/hex-never-a-draw.py`. Paired verdict: VERDICT 240 (offset +13).
> results_sha256 = `76d9a3267140171bec9ad335b370c6028e1359d23f39c7c87f3d7125598ebed8`

## Head

On the n×n Hex rhombus, Red owns the top and bottom edges (a Red chain must connect row 0 to row n−1) and Blue owns the left and right edges (column 0 to column n−1), under the six-neighbour hex adjacency (r,c) ~ (r−1,c), (r+1,c), (r,c−1), (r,c+1), (r−1,c+1), (r+1,c−1). The **Hex theorem**: for *every* complete two-colouring of the board exactly one player has a winning connection — never both, never neither. Never-neither is the no-draw half (topological, equivalent to the 2-D Brouwer fixed-point theorem); never-both is the planarity / Jordan-curve half.

The exactly-true corollary this proposal pins: the map that transposes the board and swaps the two colours is a measure-preserving bijection on the 2^(n²) complete colourings that carries "Red connects" onto "Blue connects". With no draws and no double-wins, the two win-sets partition all colourings, so

- **#{Red connects} = #{Blue connects} = 2^(n²−1)** (exact integer identity), and
- under a fair independent fill, **P(Red connects) = 1/2 EXACTLY** — a rational constant, independent of board size and of the first-mover advantage that perfect play would confer.

## Why it matters (fleet framing)

A "who-connects" invariant with a provable exact probability is the cleanest possible unit test for any board-connectivity or percolation-style component in the fleet: a correct flood-fill / union-find over hex adjacency must reproduce draws==0 and a 1/2 split to the last bit, while the *same* code over 4-neighbour (square) adjacency must NOT — it draws. The gate battery turns that contrast into a live regression check that "hex-ness" (the two diagonal neighbours) is actually wired in, not silently degraded to a rook graph.

## Exact core identities (what the verifier proves)

1. **Exhaustive exact (n ∈ {2,3,4}):** enumerate all 2^(n²) colourings; draws = 0, double-wins = 0, and Red-wins = Blue-wins = 2^(n²−1) exactly (16→8, 512→256, 65536→32768), so Fraction(Red-wins, 2^(n²)) = Fraction(1,2) for each n.
2. **Transpose-swap symmetry:** the exact 1/2 is the fixed point of P(Red|p) = 1 − P(Red|1−p) at p = 1/2; the verifier checks the complement identity P(Red|p) + P(Red|1−p) = 1 at p = 3/10 vs 7/10.
3. **Adjacency dependence:** the no-draw property is special to hex adjacency — under square (4-neighbour) adjacency draws occur at a positive rate.

## Gate battery (each in its own direction)

- **G1 — EQUALITY (exhaustive, exact):** all colourings for n = 2,3,4; draws==0, both==0, Red==Blue==2^(n²−1); Fraction identity == 1/2. Exact, no sampling.
- **G2 — AGREEMENT |z| < 3:** Monte-Carlo fair fill at n = 11 (the standard board), N = 120 000; z of the Red-win count vs N/2 is z = −0.826 (p̂ = 0.498808), draws==both==0.
- **G3 — INVARIANT + AGREEMENT:** never-draw invariant draws==both==0 across n ∈ {5,7,9,11} × p ∈ {3/10, 1/2, 7/10}; complement-symmetry z within |z| < 3 at every size (−0.776 / 0.179 / −0.585 / −0.480).
- **G4 — REJECTION |z| > 6:** on the same fair fills at n = 7, the 4-neighbour square lattice draws (square_draws = 63 128, q = 0.526) while hex draws = 0; the naive hypothesis "hex draws at the square rate" predicts N·q draws, observed 0 → z = −364.97. Naive alternative REJECTED.

## Determinism & digest

`SEED = 20260717`; a single `random.Random(SEED)` is consumed in the fixed order G2 → G3 → G4. `build_results()` is a pure function of the seed and fixed constants; `main()` runs it twice in-process and asserts byte-identical canonical JSON, and a separate re-invocation is byte-identical. Whole-dict sha256 (no self-field), stdout only:

`results_sha256 = 76d9a3267140171bec9ad335b370c6028e1359d23f39c7c87f3d7125598ebed8`

## Grounding & scope

Grounding pins English Wikipedia "Hex (board game)" at oldid 1361476133 (2026-06-28T04:20:21Z), raw-wikitext sha1 `7a7263db…632fa4a`. **On that pinned revision (quoted):** the no-draw theorem — *"Draws are impossible in Hex due to the topology of the game board"* and *"no matter how the board is filled with stones, there will always be one and only one player who has connected their edges"*; the first-player winning strategy and Nash's strategy-stealing argument; the Gale-1979 equivalence to the 2-D Brouwer fixed-point theorem; Piet Hein's 1942 invention and the 11×11 standard board. **Derived, NOT on the page:** the exact probability P(first player wins under a uniform random fill) = 1/2 and the 2^(n²−1) count identity — the pinned revision states no probability over random colourings at all. Sperner's lemma and the Jordan curve theorem are not named on the revision; they are the standard mechanisms behind the two halves and are attributed as derived here. Every number in the gate battery is computed by the verifier, not quoted.

## Reproduce

```
python3 sims/verdict-240-hex-never-a-draw/hex-never-a-draw.py
# exit 0; prints the results dict, four PASS lines, all_pass: True,
# results_sha256: 76d9a3267140171bec9ad335b370c6028e1359d23f39c7c87f3d7125598ebed8
```

## Probe report (v0, self-adversarial)

**1. Is the core identity exactly true (not merely approximate)?** Yes. G1 enumerates every colouring for n = 2,3,4 and finds draws==0, both==0, Red==Blue==2^(n²−1) with zero slack; the 1/2 is a `fractions.Fraction` equality, not a float.

**2. Could the 1/2 be an artefact of the sampler rather than the geometry?** No. It falls out of a counting bijection (transpose + colour-swap) verified exhaustively; the Monte-Carlo gates (G2/G3) only confirm the asymptotics agree, and G3's complement-symmetry check ties the value to the geometry at p ≠ 1/2.

**3. What is the most plausible wrong belief this could be confused with?** That any planar connection game is draw-free, or that a random fill favours the first player (who wins under perfect play). G4 refutes the first by exhibiting square-lattice draws at q ≈ 0.53; G2 refutes the second — the random-fill split is 1/2, the perfect-play advantage does not leak into it.

**4. Is the verifier deterministic and self-checking?** Yes. Single seeded RNG in a fixed consumption order; in-process double-run + separate re-invocation both byte-identical; whole-dict sha256 with no self-reference.

**5. Does the grounding actually support the claim, or is it overstated?** The theorem and its topological basis are quoted verbatim from the pinned revision; the *quantitative* 1/2 and the count identity are explicitly flagged as derived-not-quoted, so the citation is not overstated.

**6. Does it scale / is it robust?** G3 holds the never-draw invariant across four board sizes and three fill densities and confirms the symmetry identity at each; the exact 1/2 is size-independent by construction.

**7. Is it falsifiable, and does it survive?** Yes — G4 pre-registers a plausible-but-wrong alternative (draws impossible under square adjacency too) and rejects it at z = −365; had hex adjacency been mis-wired to a rook graph, G4 would fire.

**8. Any residual risk before ruling?** Exhaustive coverage stops at n = 4 (n = 5 is 2^25 colourings); n ≥ 5 rests on the cited theorem plus the Monte-Carlo invariant gates, which is the intended division of labour. No further blocker.

**Recommendation: sim-ready**
