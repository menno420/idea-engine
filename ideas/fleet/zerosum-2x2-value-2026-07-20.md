# The value of a 2×2 zero-sum game (von Neumann minimax)

> **State:** sim-ready
> **Status:** sim-ready

**Lane:** fleet · game-theory / strategic-form minimax value
**Proposal:** 235 → Verdict 248 (+13 offset)
**Verifier:** [`verify_235_zerosum_2x2_value.py`](verify_235_zerosum_2x2_value.py) · stdlib only · SEED=20260717
**Digest:** `results_sha256 = a8d766a845b4cd53518fc572f30041dfb154148a67f399c39463476ec1e4276a`

## Claim

For a two-player zero-sum game with row-maximiser payoff matrix M = [[a, b], [c, d]] that has **no pure-strategy saddle point** (pure maximin < pure minimax, equivalently the optimal mixing weights lie strictly in (0, 1)), the game value is the exact rational

    v = (a·d − b·c) / (a + d − b − c)

attained by the mixed strategies: row plays row0 with probability (d − c)/(a+d−b−c), column plays col0 with probability (d − b)/(a+d−b−c). This is the closed form of von Neumann's minimax theorem specialised to the 2×2 case.

## Exact reference

M = [[3, −1], [−2, 1]] (row maximiser). Denominator a+d−b−c = 3+1−(−1)−(−2) = 7.

| quantity | value |
|---|---|
| value v = (3·1 − (−1)·(−2))/7 = (3 − 2)/7 | 1/7 |
| row mix (row0, row1) = ((d−c)/7, ·) | (3/7, 4/7) |
| column mix (col0, col1) = ((d−b)/7, ·) | (2/7, 5/7) |
| pure-strategy maximin (security level) | −1 |
| pure-strategy minimax | 1 |

Because maximin = −1 < 1 = minimax there is no pure saddle point, so the mixed value v = 1/7 genuinely sits strictly above the naive security level −1. The plausible rule "the value equals the pure-strategy security level" is off by v − (−1) = 8/7.

## Four gates (each in its own direction)

- **G1 — exact value identity (`fractions.Fraction`).** Over a 4-game no-saddle rational panel, the closed-form value equals an independent indifference-equation route (row mix that makes the column player indifferent, then the resulting payoff) as equality of exact rationals, and each game is confirmed to have no pure saddle point with an interior mix. A saddle-game cross-check confirms the maximin = minimax collapse when a pure saddle does exist.
- **G2 — Monte-Carlo agreement.** 400 000 trials with both players sampling their optimal mixed strategy; the Monte-Carlo mean payoff agrees with the exact target v = 1/7 at z = 0.345941, |z| < 3.
- **G3 — invariance / robustness.** (a) minimax guarantee: with the row fixed at its optimal mix, the expected payoff equals v EXACTLY against every column strategy in a panel (q = 1, 0, 1/2, 1/3, q*); (b) affine invariance: M → α·M + β shifts the value to α·v + β exactly and leaves both optimal mixes unchanged, for α∈{2,3,1/2}, β∈{5,−1,10}. Both exact via `Fraction`.
- **G4 — falsifiability.** On the same MC sample, the naive rule "value == pure-strategy security level (maximin) = −1" is rejected at z_naive = 462.564053, |z| ≥ 6.

All four gates PASS; `all_gates_pass = true`, `first_failing_gate = null`, `decision = sim-ready`. Deterministic: in-process double-run and separate re-invocation are byte-identical.

## Grounding

Zero-sum game (Wikipedia), pinned revision:
`https://en.wikipedia.org/w/index.php?title=Zero-sum_game&oldid=1356567765&action=raw@7fdc2358933b14b00b9b0340eca8e88a593d5ac2` (rev 2026-05-28, 29581 bytes; API `revisions.sha1` == self-computed `sha1sum` of the raw wikitext — exact match).

- **Quoted** literally on the pinned revision: "zero-sum" (46×), the "minimax theorem" and the equivalence "the different game theoretic solution concepts of Nash equilibrium, minimax, and maximin all give the same solution" for finite two-player zero-sum games under mixed strategies (with "Notice that this is not true for pure strategy"), "von Neumann" and the Borel–von Neumann probability insight that "minimax method can compute … optimal strategies for all two-player zero-sum games", "value of the game" (the LP route to compute it), and — notably — the additive half of the affine-invariance leg: "add a constant to every element … will increase the value of the game by that constant, and will not affect the equilibrium mixed strategies".
- **Derived** firsthand (grep count 0 on the pinned raw wikitext): the specific 2×2 closed form v = (a·d − b·c)/(a + d − b − c) and the optimal-mix formulas (the article gives only the general linear-programming route, NOT the 2×2 closed form); the literal term "saddle point" (absent from this revision — the no-saddle concept is derived here from maximin < minimax); "matching pennies" (count 0); the reference matrix [[3,−1],[−2,1]], v = 1/7, the mixes (3/7,4/7) and (2/7,5/7); the 4-game panel; the multiplicative (α) scaling half of the affine-invariance check; the security-level −1 falsifier value; and every Monte-Carlo z-value (G2 z = 0.345941, G4 z_naive = 462.564053) and the results_sha256. The minimax theorem is textbook and cited as such; the firsthand contribution is the exact rational 2×2 instantiation, the four-gate machine-checked reproduction, and the falsification of the security-level error. Nothing oversold as novel.

## Probe report (v0, self-adversarial)

**1. Is the core claim exactly true (not merely approximate)?** Yes. G1 computes each panel game's value two independent exact ways — the closed form v = (a·d − b·c)/(a+d−b−c) and an indifference-equation route (solve for the row mix x = (d−c)/g that equalises the column player's two payoffs, then take that payoff) — entirely in `fractions.Fraction` (RNG-free), and checks equality of exact rationals. The reference game returns v = 1/7, row = (3/7,4/7), column = (2/7,5/7) exactly; the other three panel games return v = 1, 5/2, −1, each matching its indifference-route value exactly. Every game is confirmed no-saddle (maximin < minimax) with an interior mix, so the mixing is genuine, not a disguised pure strategy.

**2. Could the numbers be an artefact of the sampler rather than the mechanism?** No. Every headline value is fixed by exact rational arithmetic (G1, G3) before any RNG is touched; the Monte-Carlo gate (G2, N=400000) only confirms the exact target v = 1/7 survives under sampling (z = 0.345941, |z| < 3). Both players draw their optimal mix, so the sampled mean payoff is an unbiased estimator of v by construction — the sample stress-tests a value already pinned exactly.

**3. What is the most plausible wrong belief this could be confused with?** That the value equals the pure-strategy security level (maximin), −1 in the reference game. G4 pre-registers exactly that naive rule and rejects it at z_naive = 462.564053 (≥6) on the SAME sample where the correctly-mixed target agrees at z = 0.345941 — the 8/7 gap between v and the security level is the mixed-strategy premium, not sampling noise.

**4. Is the verifier deterministic and self-checking?** Yes. The single sampling gate consumes one seeded `random.Random(20260717)` in fixed order; `build_results()` is a pure function of SEED and the module constants (no wall-clock / PID / unordered-set iteration in the hashed payload). `main()` asserts an in-process double-run is byte-identical, and a separate re-invocation reproduces the digest byte-for-byte. Whole-dict `results_sha256 = a8d766a845b4cd53518fc572f30041dfb154148a67f399c39463476ec1e4276a`, carrying no self-reference.

**5. Does the grounding actually support the claim, or is it overstated?** Honest split. The pinned Zero-sum game revision carries the minimax theorem, the minimax = maximin = Nash equivalence for finite two-player zero-sum games under mixed strategies, the von Neumann attribution, the "value of the game" via the LP route, and even the additive-shift invariance of the value with unchanged equilibrium mixes — quoted. The specific 2×2 closed form, the optimal-mix formulas, the reference matrix and its numbers (v=1/7, (3/7,4/7), (2/7,5/7)), the multiplicative-scaling half of affine invariance, the security-level −1 falsifier, and every z-value and the digest are flagged derived-not-quoted; the literal term "saddle point" is not on this revision. Neither oversold (the sim/seed/digest are firsthand) nor undersold (the minimax theorem genuinely appears and is cited as textbook).

**6. Does it scale / is it robust?** The claim is a closed-form identity for the 2×2 no-saddle case, so it is structurally parameter-independent within that class. G1 confirms it on a 4-game panel spanning distinct rational payoffs and values (1/7, 1, 5/2, −1). G3 adds two robustness legs, both exact via `Fraction`: (a) the minimax guarantee — the optimal row mix pays exactly v against every column strategy tested; (b) affine reparametrisation — α·M + β maps the value to α·v + β and fixes the optimal mixes for α∈{2,3,1/2}, β∈{5,−1,10}.

**7. Is it falsifiable, and does it survive?** Yes — G4 pre-registers the plausible-but-wrong security-level rule and rejects it at ~463σ on the same sample G2 shows agreeing with the truth. Any mis-stated value or mix, or treating the game as having a pure saddle, would break the exact indifference-route equality in G1 or move the G2 z past the accept band.

**8. Any residual risk before ruling?** The no-saddle precondition (maximin < minimax) is asserted per game — a game WITH a pure saddle is out of scope by construction (its value is the saddle entry, covered by the G1 cross-check), not a defect. The minimax theorem itself is textbook and cited as such; the firsthand contribution is the exact rational 2×2 instantiation, the four-gate machine-checked reproduction, and the falsification of the security-level error. The paired sim-lab VERDICT 248 reproduction is a separate coordinator-driven slice. No further blocker.

**Recommendation: sim-ready**
