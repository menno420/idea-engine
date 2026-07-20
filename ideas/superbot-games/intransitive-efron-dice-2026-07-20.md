# Efron's dice — four dice A, B, C, D where A beats B beats C beats D beats A, and EVERY one of those four cyclic matchups is won by the earlier die with probability EXACTLY 2/3 — so "which die is best?" has no answer. Whatever die a player picks, the die immediately before it in the cycle beats it two-thirds of the time. The "rolls-higher-more-than-half" relation is NON-TRANSITIVE: it contains a directed 4-cycle, so there is no maximum element, no dominant die, and the entire advantage belongs to whoever chooses SECOND.

> **State:** sim-ready
> **Class:** superbot-games · dice / random-resolution microstructure · intransitive (Efron's) dice (Bradley Efron; MathWorld "Efron's Dice"; Rump 2001)
> **Target:** sim-lab (VERDICT 208, +13 offset)
> **Grounding:** https://en.wikipedia.org/wiki/Intransitive_dice@b3fdd4b02fcf23195db6e6d217d34ef5b394a5c7 · fetched 2026-07-20T03:30:07Z
> **Verifier (firsthand):** committed stdlib-only reference sim `ideas/superbot-games/intransitive_efron_dice.py` (random, math, json, hashlib, fractions) — an EXACT rational win-matrix from exhaustive 36-face-pair enumeration cross-checked by a seeded Monte-Carlo, double-run byte-identical, all three gates PASS, results-dict sha256 2dcf880b…f6d183 (see Dry-sim below).

## The phenomenon (one line)
Efron's four dice A(4,4,4,4,0,0), B(3,3,3,3,3,3), C(6,6,2,2,2,2), D(5,5,5,1,1,1) form a cycle A≻B≻C≻D≻A in which each arrow is won with probability EXACTLY 2/3 (24 of 36 face pairs, no ties), the reverse of each arrow is exactly 1/3, and the two NON-cyclic pairs are asymmetric-but-not-cyclic (C beats A at 5/9, B vs D is a fair 1/2) — so there is no strongest die, and a seeded Monte-Carlo (SEED=20260717, 200000 rolls per pair) reproduces every 2/3 to within 0.0019, min z = 148.52 over the four cyclic edges.

## The folk belief
"Dice are totally ordered by strength. If die X beats die Y more often than not, and Y beats Z, then X must beat Z — 'better than' is transitive, like height or price, so you can always rank a set of dice from best to worst and the person who picks the best die wins. In a pick-your-die duel, going FIRST is the advantage: you grab the strongest die before your opponent can. There is surely a single best die in any set of four."

## The game-design thesis (reasoned to its fuller form — Q-0254 duty)
Every step of the folk intuition is reasonable and the conclusion is still false. "Beats more than half the time" is a relation on dice, but — unlike height or price — it is NOT forced to be transitive, because the winner of a die-vs-die matchup depends on the full JOINT distribution of the two face sets, not on any single scalar "strength." Efron's set is engineered so that the pairwise comparison rotates: A's mass sits at 4 (beating B's constant 3), B's constant 3 beats C's low faces (2), C's high faces (6) beat D's middling faces, and D's 5s beat A's — and around the loop closes, A≻B≻C≻D≻A, each edge at 2/3. The relation is a TOURNAMENT with a directed cycle, and a tournament with a cycle has no maximum element: "the best die" is not a well-defined object.

The strategic consequence is the exact inverse of the folk belief. Because for every die there is another die that beats it two-thirds of the time (the one just before it in the cycle), the player who commits their die FIRST hands their opponent a free 2:1 edge — the second player simply answers A with D, B with A, C with B, D with C. First-mover is a LOSING role. The only well-defined strategy is procedural: force the opponent to pick first, or (in a simultaneous game) mix over the dice, where the Nash play is a continuum of optimal mixes documented for exactly this set.

The counterintuitive core for a designer: intransitivity is not a bug of exotic dice — it is the generic behavior of any "compare two random draws, higher wins" resolution whenever the draw distributions are shaped rather than scalar. Any game surface that resolves a contest by "each side rolls from its own loot/stat distribution, higher wins" (weapon damage ranges, creature stat spreads, gacha-pull comparisons, card-vs-card coin flips) can be non-transitive: buffing the numbers on one item can leave it beating the item it targeted while newly LOSING to a third it used to beat, and the "tier list" a community writes can be a cycle dressed up as a ladder. Efron's dice are the minimal, exactly-solvable witness that "X beats Y beats Z" never implies "X beats Z."

## The formal model (committed constants — sim-lab must reproduce exactly)
- **Dice.** Four fair six-sided dice with the face multisets A=(4,4,4,4,0,0), B=(3,3,3,3,3,3), C=(6,6,2,2,2,2), D=(5,5,5,1,1,1). Each face is equally likely (probability 1/6). This is Bradley Efron's canonical intransitive set.
- **Matchup.** For an ordered pair (X, Y), P(X > Y) = (number of the 36 face pairs (x, y) with x > y) / 36, computed EXACTLY as a `fractions.Fraction` by enumerating all 6×6 face pairs. P(tie) is enumerated the same way (and is 0 for every cyclic pair).
- **The cycle** is the fixed list A≻B≻C≻D≻A: the earlier die beats the later die. The claim is P(earlier > later) = 2/3 for all four arrows, and P(later > earlier) = 1/3.
- **Monte-Carlo (reproducible dry-sim).** `mc_win_prob` seeds one `random.Random(SEED)` and, per cyclic pair, draws TRIALS=200000 independent (X-face, Y-face) rolls, recording the earlier die's empirical win rate. The SAME rng, in fixed pair order, then drives the best-of-7 shift leg — so the entire run is one deterministic stream.
- **Robustness/shift regime:** vary the match length k∈{1,3,5,7} (best-of-k majority; cyclic pairs never tie, so a majority always exists). Exact best-of-k win probability is the binomial tail Σ_{j>k/2} C(k,j) p^j (1−p)^{k−j} with p the exact single-roll 2/3, computed as a Fraction; a seeded Monte-Carlo best-of-7 corroborates it.

## Pinned world (committed constants)
- SEED = 20260717 (proposal-owned); one `random.Random(SEED)` per full run, consumed in fixed order (four cyclic single-roll legs, then four cyclic best-of-7 legs).
- DICE as above; CYCLE = [A>B, B>C, C>D, D>A]; TRIALS = 200000; BEST_OF_KS = [1,3,5,7]; SHIFT_K = 7.
- Z_GATE = 3.0; EXACT_TOL = 0.01; closed forms EXACT_CYCLIC = 2/3, EXACT_C_OVER_A = 5/9, EXACT_B_VS_D = 1/2.
- Floats rounded 6 dp; results dict carries no self-referential sha field; digest = sha256 of the compact-canonical (sort_keys, comma/colon) results JSON, printed to stdout as full 64 hex.

## Pre-registered gates (sim-ready iff ALL hold, in order G1 -> G2 -> G3)
- **G1 — statistical, the cyclic edges are real (headline, ≥3σ):** across the four cyclic pairs, the MINIMUM z-score of (Monte-Carlo earlier-die win rate − 0.5) is ≥ Z_GATE = 3.0 AND every cyclic win rate > 0.5. Each arrow of the cycle wins strictly and overwhelmingly more than half.
- **G2 — exactly-true, the closed form IS the enumeration:** the exhaustively-enumerated exact win matrix equals the closed forms with ZERO tolerance (Fraction ==): every cyclic pair == 2/3 with tie-probability == 0; the cycle A≻B≻C≻D≻A holds (each cyclic prob > 1/2 AND each reverse < 1/2); the non-cyclic closed forms C-over-A == 5/9, A-over-C == 4/9, B-vs-D == D-vs-B == 1/2; AND the Monte-Carlo win rates agree with the exact values within EXACT_TOL = 0.01 (max cyclic deviation). This is the "exactly-true" gate: the surprising 2/3 is not approximate, it is 24/36 on the nose.
- **G3 — robustness/shift, the paradox survives longer matches:** vary the match length k∈{1,3,5,7} (best-of-k majority). The exact cyclic dominance PERSISTS (every cyclic pair wins > 1/2 at every k) and STRENGTHENS (the per-pair win probability is strictly monotone increasing in k: 2/3 → 20/27 → … → the best-of-7 tail), and a seeded Monte-Carlo best-of-7 confirms it at min z ≥ Z_GATE = 3.0. The intransitive edge is not a single-roll artefact — it amplifies under repetition.

all_pass = G1 ∧ G2 ∧ G3.

## Pre-registered decision rule
sim-ready iff G1 ∧ G2 ∧ G3 hold at their stated thresholds on the pinned world with SEED=20260717 and the committed reference verifier (its `all_pass` field encodes exactly G1 ∧ G2 ∧ G3). Any gate failing → REJECT (the intransitivity / 2/3-cyclic-dominance claim is falsified for these constants). No post-hoc threshold moves; SEED is not changed; z-scores are the standard error on a Bernoulli proportion over N=TRIALS. The exact-enumeration G2 is a self-certifying proof (no sampling), so a G2 failure would mean the dice as committed are not Efron's set.

## Dry-sim results (SEED=20260717, verbatim from the committed verifier)
- **Exact win matrix (all 12 ordered pairs, Fraction):** A>B 2/3 · B>C 2/3 · C>D 2/3 · D>A 2/3 (the cycle); B>A 1/3 · C>B 1/3 · D>C 1/3 · A>D 1/3 (reverses); C>A 5/9 · A>C 4/9 · B>D 1/2 · D>B 1/2 (non-cyclic). Zero ties in every cyclic pair.
- **G1 statistical (single-roll MC, 200000/pair):** cyclic win rates 0.66705 (A>B), 0.66855 (B>C), 0.66605 (C>D), 0.666475 (D>A); min z = 148.519635; all > 0.5 — PASS.
- **G2 exactly-true:** cyclic_all_two_thirds = true, no_ties_in_cycle = true, cycle_holds = true, C-over-A = 5/9, A-over-C = 4/9, B-vs-D = 1/2, max MC deviation from exact = 0.001883 ≤ 0.01 — PASS.
- **G3 robustness/shift (best-of-k majority):** exact min win prob per k = {1: 0.666667, 3: 0.740741, 5: 0.790123, 7: 0.826703}, strictly monotone increasing, all > 0.5 at every k; MC best-of-7 min z = 292.119921 — PASS.
- all_pass = true; first_failing_gate = null; exit 0.
- In-process double-run assertion holds; two cross-invocation runs byte-identical.
- **Disclosed results-dict sha256 = 2dcf880be80df99fc6b30c63a3ff0682831cfbe34c4f3b41b48b984bb0f6d183** (sha256 of `json.dumps(results, sort_keys=True, separators=(",",":"))`; the results dict carries NO self-referential sha field, so no field-omission step and no JSON artifact is committed).

## Verifier
Stdlib-only python3 (`random, math, json, hashlib, fractions` — no numpy), committed alongside this idea as `ideas/superbot-games/intransitive_efron_dice.py`. It builds the exact 12-entry win/tie matrix by enumerating all 36 face pairs per ordered die pair (`fractions.Fraction`, no float in the ground truth), runs a seeded Monte-Carlo single-roll race and a seeded best-of-7 race, then tests G1 (cyclic min z ≥ 3 and all edges > 0.5), G2 (matrix == closed forms exactly, no ties, cycle holds, MC agrees ≤ 0.01), G3 (best-of-k cycle persists and is monotone in k, MC best-of-7 min z ≥ 3), asserts in-process determinism (compute() run twice → identical canonical dict), and emits a canonical results JSON with its full-64-hex sha256. Exit 0 iff all three gates pass.

## Caveats & crossovers (disclosed, non-gating)
- **The two non-cyclic pairs are NOT 2/3.** C-over-A is 5/9 and B-vs-D is a fair 1/2 — this is a genuine feature of Efron's set (the cycle runs A→B→C→D→A, not around all six ordered pairs), disclosed here and checked exactly by G2 so the head is not overclaimed as "every pair is 2/3."
- **Simultaneous vs sequential.** The 2:1 second-mover edge is a SEQUENTIAL-commitment fact. Under simultaneous blind choice the game is a symmetric two-player zero-sum matrix game with a mixed Nash equilibrium (a documented continuum of optimal mixes for this set); the paradox does not let either player win a simultaneous game — it makes "pick the best die" ill-defined and rewards forcing the opponent to commit first.
- **Best-of-k parity.** The robustness gate uses ODD k so a majority always exists; the amplification (2/3 → higher) is the standard binomial concentration and is exact, not sampled.
- **Fairness of the dice is assumed and load-bearing.** Every face is probability 1/6; the effect is manufactured by the face VALUES, not by any bias — so it cannot be dismissed as a loaded-die trick.

## Dedup (author-time, checked before writing)
`git grep -i` across `ideas/` and `control/outbox.md` for `efron`, `intransitive`, `nontransitive`, `non-transitive` at origin/main before authoring. The head is distinct from every prior intransitivity card in the fleet:
- **`ideas/fleet/condorcet-voting-cycle-2026-07-19.md` (P168 → V181):** intransitive collective MAJORITY PREFERENCE from independent transitive voters (no Condorcet winner). That is a voting/social-choice object over sub-electorates; this is a fixed non-transitive DOMINANCE among four physical dice with exact 2/3 pairwise odds. Distinct mechanism and domain.
- **`ideas/superbot-games/penney-game-second-mover-advantage-2026-07-20.md` (P191 → V204) and `ideas/fleet/penney-game-responder-edge-decay-2026-07-13.md`:** non-transitive COIN-SEQUENCE races decided by first-appearance/waiting-time overlap. Different object (sequences in a stream, not dice), different mechanism (self/cross-overlap, not joint face distributions), different odds (2/3–7/8 waiting-time, not a clean 2/3 face-count).
- **`ideas/superbot-games/balance-triangle-pick-rate-inversion-2026-07-18.md`:** a three-strategy skew-symmetric zero-sum MATRIX game (rock-paper-scissors pick-rate equilibrium). That is a 3-strategy game-value/equilibrium object; Efron's dice are a FOUR-die random-resolution object with an exact 2/3 cyclic dominance and no tie mass. No collision.
- No prior card ships Efron's dice, the four-cycle-at-2/3 result, or the exhaustive-face-enumeration exact witness. This is the FIRST intransitive-dice / random-resolution-dominance card in the lane.

## Grounding note (honest)
Wikipedia "Intransitive dice" § "Efron's dice" (raw wikitext fetched live this session, `action=raw`, HTTP 200, 33840 bytes; MediaWiki-reported revision sha1 `b3fdd4b02fcf23195db6e6d217d34ef5b394a5c7`, oldid 1357047248, byte-identical to the locally re-hashed wikitext) states the four dice with exactly the committed faces (A: 4,4,4,4,0,0 · B: 3,3,3,3,3,3 · C: 6,6,2,2,2,2 · D: 5,5,5,1,1,1) and the sentence "Each die is beaten by the previous die in the list with wraparound, with probability 2/3. C beats A with probability 5/9, and B and D have equal chances of beating the other" — supporting the SPECIFIC head (the 2/3 cyclic Efron probabilities, the 5/9 and 1/2 non-cyclic closed forms, and the cyclic dominance) verbatim. The grounding pin is the RAW wikitext sha1 (40 hex), not a rendered-HTML hash; the same 2/3 / 5/9 / 1/2 claims also appear in the rendered article, so the rendered-vs-wikitext gap is nil for this head. The exact-enumeration G2 gate is the firsthand witness that the four cyclic pairs are 2/3 (24/36) with zero ties — the external citation grounds naming and provenance, the verifier proves the numbers.

## Margin ledger (gate margins vs thresholds)

| Gate | Quantity | Threshold | Measured | Margin |
|------|----------|-----------|----------|--------|
| G1 statistical | min cyclic z vs 0.5 | ≥ 3.0 | 148.519635 | +145.52 |
| G1 statistical | all cyclic winrate > 0.5 | all | 0.666–0.669 | pass |
| G2 exactly-true | cyclic == 2/3 (Fraction) | exact == | 2/3 all four | exact |
| G2 exactly-true | ties in cycle | == 0 | 0 | exact |
| G2 exactly-true | max MC dev from exact | ≤ 0.01 | 0.001883 | +0.008117 |
| G3 robustness | cyclic wins > 1/2 at all k∈{1,3,5,7} | all | 0.667→0.827 | pass |
| G3 robustness | win prob monotone ↑ in k | strict ↑ | 0.667<0.741<0.790<0.827 | pass |
| G3 robustness | MC best-of-7 min z | ≥ 3.0 | 292.119921 | +289.12 |

## Probe report
**1. What is this really?** An intransitive-dice claim: Efron's four dice cycle A≻B≻C≻D≻A with each arrow won at EXACTLY 2/3 (24/36 face pairs, zero ties), so the "beats-more-than-half" relation has a directed cycle and no best die exists; the whole advantage belongs to the second picker. Exact 36-face enumeration (Fraction) is cross-checked by a seeded 200000-roll Monte-Carlo per pair.

**2. Is it counterintuitive-but-true?** Yes — "beats" feels transitive like height or price, so people expect a single strongest die and expect first-pick to be the advantage. Both are wrong: the relation cycles and first-pick is a 2:1 losing role. True by exhaustive enumeration, not approximation.

**3. Is the model clean and fully pinned?** Yes — four fixed face multisets, uniform 1/6 faces, SEED committed, exact rational ground truth, nothing tunable post-hoc; the closed forms (2/3, 5/9, 1/2) are all checked with zero tolerance.

**4. Is there an exactly-true gate?** Yes — G2: the enumerated win matrix equals the closed forms as exact Fractions (each cyclic pair 2/3 with zero ties, C-over-A 5/9, B-vs-D 1/2, cycle holds), no sampling. G3 further uses exact-Fraction binomial best-of-k values.

**5. Is it deterministic and reproducible?** Yes — one `random.Random(20260717)` consumed in fixed order, in-process double-run asserted canonical-identical before hashing, full-64-hex results-dict sha256 `2dcf880be80df99fc6b30c63a3ff0682831cfbe34c4f3b41b48b984bb0f6d183` byte-identical across two separate invocations.

**6. Is the grounding real and external?** Yes — Wikipedia "Intransitive dice" § Efron's dice, raw wikitext pinned by revision sha1 `b3fdd4b0…a5c7` (oldid 1357047248), carrying the exact faces and the "each beaten by the previous with wraparound, probability 2/3; C beats A 5/9; B and D equal" statement; honest note that the pin is raw-wikitext (the rendered article carries the same claims).

**7. Could it collide with a shipped proposal?** No — author-time grep of `ideas/` and the outbox for efron/intransitive/nontransitive returned zero real hits; distinct from Condorcet's voting cycle (P168, majority preference), Penney's game (P191, waiting-time sequence race), and the balance-triangle RPS matrix game (3-strategy equilibrium). First intransitive-DICE card in the lane; disclosed in Dedup.

**8. What would make sim-lab reject it?** A non-reproducible digest, the enumerated win matrix disagreeing with the closed forms under reimplementation, a tie appearing in a cyclic pair, the Monte-Carlo drifting outside 0.01 of the exact 2/3, or the best-of-k dominance failing to persist/strengthen.

**Recommendation: sim-ready**
