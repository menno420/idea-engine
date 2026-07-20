# PROPOSAL 195 — intransitive / Efron's dice: A≻B≻C≻D≻A each at exactly 2/3, no best die (round-46 GAME slot, P195 → V208, +13)

> **Status:** complete
> 📊 Model: Claude Opus · high · idea/planning
> heartbeat: 2026-07-20T03:43:00Z — born-red HOLD cleared; CI confirmed the only red was `[session-card-hold]` (HOLD by design, zero doc findings); flipping to complete releases the merge-on-green landing.

**Born-red HOLD (cleared).** This card landed `in-progress` on the FIRST commit to hold the proposal PR RED on the born-red convention (the added-card gate keeps a `> **Status:** in-progress` card red until the deliberate flip); it flips to `complete` here as the LAST commit, after the verifier reproduced byte-identical (results-dict sha256 `2dcf880be80df99fc6b30c63a3ff0682831cfbe34c4f3b41b48b984bb0f6d183` across an in-process double-run and separate cross-invocations) and the G1/G2/G3 battery passed green (all_pass=true, first_failing_gate=null; G1 min z=148.519635, G2 max MC dev 0.001883, G3 MC best-of-7 min z=292.119921). CI on PR #725 confirmed the only red was the designed `[session-card-hold]` (zero doc findings). Merge-on-green is the only merge path — this session issued zero merge calls.

## 💡 Session idea
The folk model of "stronger than" is a total order: if die A beats die B and B beats C, then A must beat C, and there is a single best die you'd want to grab first. Efron's four dice — A(4,4,4,4,0,0), B(3,3,3,3,3,3), C(6,6,2,2,2,2), D(5,5,5,1,1,1) — refute it exactly: A beats B beats C beats D beats A, every arrow at probability EXACTLY 2/3 (24 of 36 face pairs, zero ties), so the "beats-more-than-half" relation is a directed 4-cycle with no maximum element. There is no best die; whichever a player commits to, the die just before it in the cycle beats it 2:1, so first-mover is the losing role and the only well-defined strategy is procedural (force the opponent to pick first). The lever for a game designer: any "each side draws from its own distribution, higher wins" resolution (weapon damage ranges, stat spreads, gacha comparisons) can be intransitive, so a buff can make an item beat its target yet newly LOSE to a third — a "tier list" can be a cycle wearing a ladder's clothes. The result is exactly-true (exhaustive face enumeration in `fractions.Fraction`), reproducible under SEED=20260717, and externally grounded in Wikipedia's "Intransitive dice" article.

## ⟲ Previous-session review
This previous-session review covers the round-46 rotation to date. P193 (price of anarchy — selfish two-pool routing costs at most 4/3 of optimum, Pigou-tight; round-46 FLEET opener) and P194 (newsvendor critical fractile — stock a high-margin good ABOVE its mean demand; round-46 VENTURE slot) are on the outbox ledger queued P193 → V206 and P194 → V207 (+13), both with byte-identical reproducing verifiers and green gate batteries. The round-46 rotation (fleet→venture→game→unrelated) now advances to the GAME slot; this session opens P195 → V208 (+13). Claim PR #723 (control fast-lane, branch `claude/proposal-195`) opens and lands before this born-red proposal PR reuses the branch for the work.

## Objective
Author + land PROPOSAL 195 → VERDICT 208 (+13): the intransitive-dice / Efron's-dice result (four dice cycle A≻B≻C≻D≻A, each arrow at exactly 2/3; no best die; second-mover-decided), with a stdlib deterministic verifier (SEED=20260717) carrying a ≥3σ statistical gate on the cyclic edges, an exactly-true exhaustive-enumeration gate (closed forms 2/3 / 5/9 / 1/2 == 36-face enumeration, zero ties, cycle holds), and a robustness/shift gate (best-of-k majority amplification persists and strengthens).

## Constraints honored
- stdlib-only verifier (random, math, json, hashlib, fractions); SEED=20260717; byte-identical across in-process double-run + separate invocation.
- PR opens READY; merge-on-green only (zero agent merge calls); born-red HOLD via this card.
- Model line family-level only (no version identifiers); timestamps from `date -u`; external grounding pinned live (Wikipedia "Intransitive dice" raw-wikitext revision sha1 `b3fdd4b02fcf23195db6e6d217d34ef5b394a5c7`, oldid 1357047248).
- DEDUP clean: author-time grep of `ideas/` + `control/outbox.md` for efron / intransitive / nontransitive / non-transitive returned zero real hits; distinct from Condorcet cycle (P168), Penney's game (P191), and the balance-triangle RPS matrix game — disclosed in the doc's Dedup section.

## Pinned world (committed constants, SEED=20260717)
Efron's four fair d6: A(4,4,4,4,0,0), B(3,3,3,3,3,3), C(6,6,2,2,2,2), D(5,5,5,1,1,1), each face probability 1/6. CYCLE = [A>B, B>C, C>D, D>A]. Exact win matrix via 36-face enumeration in `fractions.Fraction`. TRIALS=200000 single rolls per pair; SHIFT_K=7; BEST_OF_KS=[1,3,5,7]; Z_GATE=3.0; EXACT_TOL=0.01. One `random.Random(20260717)` consumed in fixed order (four single-roll legs, then four best-of-7 legs). Digest posture: WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY, floats 6dp.

## Gate-plan (pre-registered — frozen, z_gate = 3.0)
- **G1 statistical (≥3σ):** across the four cyclic pairs, min z of (MC earlier-die winrate − 0.5) ≥ 3.0 AND all cyclic winrates > 0.5. Measured: min z = 148.519635, winrates 0.66705 / 0.66855 / 0.66605 / 0.666475.
- **G2 exactly-true:** enumerated win matrix == closed forms as exact Fractions — every cyclic pair == 2/3 with tie-prob == 0, cycle A≻B≻C≻D≻A holds (each cyclic > 1/2, each reverse < 1/2), C-over-A == 5/9, A-over-C == 4/9, B-vs-D == 1/2; AND max MC deviation from exact ≤ 0.01. Measured: all exact, max MC dev = 0.001883.
- **G3 robustness/shift:** best-of-k majority k∈{1,3,5,7} — cyclic dominance persists (all > 1/2 at every k) and strictly strengthens (0.666667 < 0.740741 < 0.790123 < 0.826703), MC best-of-7 min z ≥ 3.0. Measured: monotone true, MC best-of-7 min z = 292.119921.
- all_pass = G1 ∧ G2 ∧ G3 = true; first_failing_gate = null.

## GROUNDING (verified live)
Wikipedia "Intransitive dice" § "Efron's dice" fetched live this session (`action=raw`, HTTP 200, 33840 bytes; revision sha1 `b3fdd4b02fcf23195db6e6d217d34ef5b394a5c7`, oldid 1357047248, byte-identical to the locally re-hashed wikitext) states the four dice with exactly the committed faces and the sentence "Each die is beaten by the previous die in the list with wraparound, with probability 2/3. C beats A with probability 5/9, and B and D have equal chances of beating the other" — supporting the 2/3 cyclic Efron probabilities, the 5/9 and 1/2 non-cyclic closed forms, and the cyclic dominance verbatim. Honest caveat: the pin is the RAW wikitext sha1 (the rendered article carries the same claims, so the rendered-vs-wikitext gap is nil for this head). The exact-enumeration G2 gate is the firsthand witness.

## Disclosed digest
results-dict sha256 = `2dcf880be80df99fc6b30c63a3ff0682831cfbe34c4f3b41b48b984bb0f6d183` (full 64 hex, WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY; identical across in-process double-run and separate cross-invocation).
