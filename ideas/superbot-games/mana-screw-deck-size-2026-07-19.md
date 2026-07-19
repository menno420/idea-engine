# PROPOSAL 163 — mana-screw deck-size: opening-hand "mana screw" consistency is governed by DECK SIZE, not land FRACTION; the land count in a 7-card opening hand is hypergeometric with variance n·p·(1−p)·(N−n)/(N−1), and the finite-population correction (N−n)/(N−1) shrinks as the deck N shrinks, so a 40-card deck at 40% lands is strictly more consistent (fewer off-curve hands) than a 60-card deck at 40% lands even though the expected land count per card (2.8) is identical

> **State:** sim-ready
> **Class:** superbot-games · tabletop deck-building / opening-hand consistency · hypergeometric order statistics (finite-population correction)
> **Slot:** round-38 GAME
> **Anchor:** the number of lands in a 7-card opening hand drawn without replacement is Hypergeometric(N, K, n) with mean n·(K/N) and variance n·p·(1−p)·(N−n)/(N−1); the finite-population correction (N−n)/(N−1) monotonically shrinks the variance as the deck size N shrinks at a FIXED land fraction p=K/N, so consistency is a deck-size lever, not a land-ratio lever
> **Target:** sim-lab (VERDICT 176, +13 offset)
> **Grounding:** https://en.wikipedia.org/wiki/Hypergeometric_distribution@1364778061 · fetched 2026-07-19T09:03:49Z
> **Reference (external, reachable):** Wikipedia, "Hypergeometric distribution" — fetched live HTTP 200 at revision 1364778061 (permalink https://en.wikipedia.org/w/index.php?title=Hypergeometric_distribution&oldid=1364778061); the article states the variance as n·(K/N)·((N−K)/N)·((N−n)/(N−1)) and explicitly names the finite-population correction (N−n)/(N−1). Also: Frank Karsten, "How Many Lands Do You Need in Your Deck?" (channelfireball.com) — the standard mana-consistency treatment of opening-hand land counts as hypergeometric draws.
> **Verifier (firsthand):** `ideas/superbot-games/mana_screw_deck_size.py` · results-dict sha256 `1280ae6278b508f00d3737841768181288e7ed31f12a443d5982b5f03b898e33`
> 📊 Model: Claude Opus · high · idea/planning

## The phenomenon (one line)
Draw a 7-card opening hand without replacement from a deck of N cards containing K = p·N lands; the land count is Hypergeometric(N, K, 7) with mean 7p (identical for any deck at fraction p) and variance 7·p·(1−p)·(N−n)/(N−1) — the finite-population correction (N−n)/(N−1) shrinks as N shrinks, so at a MATCHED land fraction a smaller deck has strictly lower opening-hand variance and therefore lands inside the [2,4] keep window more often: a 40-card deck at 40% lands is measurably more consistent than a 60-card deck at 40% lands, even though both expect 2.8 lands.

## The folk belief
"Consistency is set by the land RATIO — 40% lands is 40% lands, so a 40-card deck and a 60-card deck at the same fraction get mana-screwed equally often." This is the ratio-only null, and it predicts EQUAL off-curve rates. It is false: the mean lands-per-card is indeed identical (7·0.4 = 2.8 in both), but the SPREAD is not — the 40-card deck's finite-population correction is 33/39 while the 60-card deck's is 53/59, so the smaller deck's opening hand clusters tighter around 2.8 and dodges the screwed (≤1) and flooded (≥5) tails more often. Deck SIZE, not fraction, is the lever a consistency-minded deckbuilder actually pulls.

## The mechanism (reasoned to its fuller form — Q-0254 duty)
Model an opening hand as n = 7 cards drawn WITHOUT replacement from a deck of N cards with K = round(p·N) lands. The land count X is Hypergeometric(N, K, n):

    E[X]   = n · (K/N) = n·p                          (identical across matched-fraction decks)
    Var[X] = n · p · (1−p) · (N−n)/(N−1)              (the finite-population correction (N−n)/(N−1))

Two decks matched at p = 0.40 — Deck A (N=40, K=16) and Deck B (N=60, K=24) — share the SAME opening-hand mean 2.8, but their variances differ ONLY through the correction: Var_A = 1.68·(33/39) = 1.421538, Var_B = 1.68·(53/59) = 1.509153, so Var_B/Var_A = (53/59)/(33/39) = **1.061633**. Because both distributions center on 2.8 but B is wider, B places MORE mass outside the keep window [2,4]. Define an "off-curve" opening hand as a land count OUTSIDE [2,4] (≤1 = screwed, ≥5 = flooded). Exact hypergeometric off-curve probabilities: Deck A = **0.209662**, Deck B = **0.225433** — the 60-card deck is off-curve ~1.58 percentage points MORE often at the identical land fraction. The whole gap is the finite-population correction and nothing else: the ratio-only null (dt/dN = 0, equal off-curve) is the object we reject.

Concretely (SEED = 20260717, TRIALS = 400000): the measured off-curve proportions are pA = 0.209482 and pB = 0.224975, a two-proportion separation of z = **16.804944** (reject the equal-off-curve null); the measured variance ratio 1.061314 agrees with the closed-form FPC ratio 1.061633 at |z| = **0.100413** (mechanism = the finite-population correction); and the same ordering survives a shift to a DIFFERENT matched fraction p = 0.30 (window recentered to [1,3]) at z = **16.446510**.

## The formal model (committed constants — sim-lab must reproduce exactly)
- Per Monte-Carlo trial, draw n = 7 cards without replacement from a deck of N cards with K lands, using the urn recurrence (each pick is a land with probability lands_left/cards_left), and count the lands X in the opening hand.
- p = 0.40 decks (feed G1 head + G2 mechanism): Deck A = N=40 / K=16, Deck B = N=60 / K=24; keep window [2,4]; off-curve = X ≤ 1 or X ≥ 5.
- p = 0.30 shifted decks (feed G3 robustness): Deck A′ = N=40 / K=12, Deck B′ = N=60 / K=18; hand size still 7; keep window RECENTERED to [1,3] (mean 2.1); off-curve = X ≤ 0 or X ≥ 4.
- Closed-form anchors: hypergeometric variance Var = n·p·(1−p)·(N−n)/(N−1); FPC_A = 33/39, FPC_B = 53/59, FPC ratio (53/59)/(33/39) = 1.061633.
- Two-proportion z on independent-sample SE: z = (pB − pA)/sqrt(pA(1−pA)/T + pB(1−pB)/T). Variance-ratio z on the delta method for F = s²_B/s²_A with independent A,B samples (SE from the empirical 4th central moments).
- **Model note (declared):** the head is an objective identity of hypergeometric order statistics — the mean is matched by construction and the variance ordering is forced by (N−n)/(N−1). The single declared modelling choice is the keep window [2,4] (the standard 7-card play/draw heuristic that "2–4 lands is a keep"); the SIGN of the effect (larger deck ⇒ more off-curve) is window-independent because it follows from the variance ordering of two same-mean distributions, and G3 re-derives it under a different fraction and a recentered window.

## Pinned world (committed constants)
- SEED = 20260717
- Z_GATE = 3.0
- TRIALS = 400000
- HAND = 7
- Deck A = N=40/K=16, Deck B = N=60/K=24, keep [2,4] (p=0.40)
- Deck A′ = N=40/K=12, Deck B′ = N=60/K=18, keep [1,3] (p=0.30 shift)
- Var_A = 1.421538, Var_B = 1.509153, FPC ratio = 1.061633
- offcurve_A theory = 0.209662, offcurve_B theory = 0.225433

## Pre-registered gates (APPROVE iff ALL hold, in order G1 → G2 → G3; z_gate = 3.0)
- **G1 — head (deck size, ≥3σ separation).** Measured off-curve proportion for Deck B (60) strictly GREATER than Deck A (40) at matched 40% fraction, with z = (pB − pA)/sqrt(pA(1−pA)/T + pB(1−pB)/T) ≥ 3. Rejects the ratio-only null (which predicts pA = pB). (Measured pA = 0.209482, pB = 0.224975, z = **16.804944**.)
- **G2 — mechanism (closed-form FPC match).** Measured variance ratio Var_B/Var_A agrees with the closed-form finite-population-correction ratio [(53/59)/(33/39)] within Monte-Carlo error; agreement z (delta method) PASSES when |z| < 3 — validation that the effect IS the finite-population correction. (Measured ratio 1.061314 vs 1.061633, z = **−0.100413**.)
- **G3 — robustness (shifted distribution, ≥3σ).** Re-run the G1 head at a DIFFERENT matched fraction p = 0.30 (Deck A′ = N=40/12, Deck B′ = N=60/18, window recentered [1,3]) and confirm Deck B′ off-curve > Deck A′ at z ≥ 3. The naive p=0.30 shift DOES separate at 3σ, so it is the shift used. (Measured pA′ = 0.167433, pB′ = 0.181385, z = **16.446510**.)

## Pre-registered decision rule
APPROVE (sim-ready confirmed) iff G1 AND G2 AND G3 all hold in order and the verifier exits 0 with a reproducible results-dict sha256 across a deterministic double-run. Any gate failing ⇒ REJECT/REVISE naming first_failing_gate. Observed all_pass = **true**, first_failing_gate = **null**.

## Dry-sim results (SEED=20260717, verbatim from the committed verifier)
```
{
  "all_pass": true,
  "first_failing_gate": null,
  "g1_head_deck_size": {
    "diff_b_minus_a": 0.015493,
    "offcurve_a_40card": 0.209482,
    "offcurve_b_60card": 0.224975,
    "pass": true,
    "ratio_only_null": "equal off-curve (pB == pA)",
    "se": 0.000922,
    "z": 16.804944
  },
  "g2_mechanism_fpc": {
    "fpc_ratio_closed_form": 1.061633,
    "mean_a_check": 2.799585,
    "mean_b_check": 2.7988,
    "pass": true,
    "se_ratio": 0.003175,
    "var_a_measured": 1.418017,
    "var_b_measured": 1.504962,
    "var_ratio_measured_b_over_a": 1.061314,
    "z": -0.100413
  },
  "g3_robustness_shift": {
    "diff_b_minus_a": 0.013952,
    "offcurve_a_40card": 0.167433,
    "offcurve_b_60card": 0.181385,
    "pass": true,
    "se": 0.000848,
    "shift": "p=0.30, keep window [1,3]",
    "z": 16.44651
  },
  "gates": [
    {"id": "G1", "name": "head_deck_size", "pass": true, "z": 16.804944},
    {"id": "G2", "name": "mechanism_fpc", "pass": true, "z": -0.100413},
    {"id": "G3", "name": "robustness_shift", "pass": true, "z": 16.44651}
  ],
  "params": {
    "deck_a": {"N": 40, "lands": 16, "p": 0.4},
    "deck_a_shift": {"N": 40, "lands": 12, "p": 0.3},
    "deck_b": {"N": 60, "lands": 24, "p": 0.4},
    "deck_b_shift": {"N": 60, "lands": 18, "p": 0.3},
    "g3_shift": "matched fraction shifted 0.40->0.30, keep window recentered [2,4]->[1,3]",
    "hand_size": 7,
    "keep_window": [2, 4],
    "keep_window_shift": [1, 3],
    "off_curve_def": "land count outside the keep window (<lo screwed, >hi flooded)",
    "seed": 20260717,
    "trials": 400000,
    "z_gate": 3.0
  },
  "theory": {
    "fpc_a_33_39": 0.846154,
    "fpc_b_53_59": 0.898305,
    "fpc_ratio_b_over_a": 1.061633,
    "mean_lands": 2.8,
    "offcurve_a_shift_theory": 0.167978,
    "offcurve_a_theory": 0.209662,
    "offcurve_b_shift_theory": 0.182016,
    "offcurve_b_theory": 0.225433,
    "var_a_hypergeom": 1.421538,
    "var_b_hypergeom": 1.509153,
    "var_ratio_theory_b_over_a": 1.061633
  }
}
Results-JSON sha256: 1280ae6278b508f00d3737841768181288e7ed31f12a443d5982b5f03b898e33
```
Results-dict sha256: `1280ae6278b508f00d3737841768181288e7ed31f12a443d5982b5f03b898e33` (deterministic double-run, exit 0 both times, two cross-invocation stdouts byte-identical).

## Verifier
`ideas/superbot-games/mana_screw_deck_size.py` — stdlib only (`random, math, json, hashlib`). Runs TRIALS = 400000 opening-hand draws per deck under one seeded stream; each hand is drawn without replacement via the urn recurrence and its land count is scored against the keep window. Computes the closed-form hypergeometric variance and FPC anchors, the exact off-curve probabilities via `math.comb`, and runs the three ordered z-gates (G1 two-proportion head deck B>A at p=0.40, G2 variance-ratio-vs-FPC delta-method agreement, G3 the same head under the p=0.30 shift with recentered window). Emits the whole results dict (no self-referential sha field; every float rounded to 6 decimals; the compact-canonical serialization's sha256 IS the disclosed digest; stdout dumps the pretty indent=2 view — WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY posture). Writes no JSON to disk; asserts the in-process double-run digests are identical before printing.

## Reproduce
```
python3 ideas/superbot-games/mana_screw_deck_size.py
```
Expected: prints the results JSON, `Results-JSON sha256: 1280ae6278b508f00d3737841768181288e7ed31f12a443d5982b5f03b898e33`, exit 0 (all_pass=true).

## Why it matters (game design / deckbuilding)
Every "how many lands should my deck run?" heuristic is a statement about opening-hand land counts, and every one of them is a hypergeometric-draw question. Two design consequences invert intuition: (1) consistency is a DECK-SIZE lever, not only a ratio lever — a format that mandates a 40-card minimum (Limited) hands players strictly tighter opening hands than a 60-card format at the SAME land fraction, so "just match the ratio" under-delivers consistency in the larger deck; a designer who wants a low-variance early game shrinks the deck, not just the land count. (2) The mean is a red herring — matched-fraction decks have identical expected lands (2.8), so a designer reasoning from average mana curves will see NO difference while players feel a real one in screw/flood frequency. The right instrument is the variance n·p·(1−p)·(N−n)/(N−1): price the finite-population correction, not the land ratio alone.

## Dedup (contrast vs prior lane heads)
- vs **speedrun-record-drought (P155)** — that is running minima of an i.i.d. sequence (record COUNTS growing as the harmonic number); this is the VARIANCE of a hypergeometric opening-hand draw under the finite-population correction. Both are order-statistics results, but one is about record indicators of exchangeable draws with replacement-free ranks, the other about the spread of sampling WITHOUT replacement at fixed fraction.
- vs **drop-rate-median-gap / shop-reroll-ruin / pity-anticipation-collapse** — those are gacha/drop-rate timing and median-vs-mean gaps under geometric/negative-binomial draws; none models the hypergeometric opening hand or the (N−n)/(N−1) finite-population correction.
- vs **st-petersburg-cap-collapse / htk-breakpoint-variance-comb** — a divergent-EV pricing collapse and a hits-to-kill breakpoint comb respectively; neither is a same-mean/different-variance deck-size consistency claim.
- Crossover honesty: the effect GENERALIZES to any "reach k copies of a card type in the opening hand" question — colored sources, combo pieces, a specific answer — because all of them are hypergeometric draws whose variance carries the same (N−n)/(N−1) correction. The VERIFIED claim here is the land-count deck-size variance dominance; the k-copies generalization is disclosed as a crossover, not asserted.

## Model basis (declared model-dependence — the P024 discipline)
The head is an **objective identity of hypergeometric order statistics**, not a behavioural claim: matched-fraction decks share the mean n·p exactly, and the variance is n·p·(1−p)·(N−n)/(N−1), so the smaller-deck variance is strictly lower whenever N shrinks at fixed p — confirmed by Monte-Carlo to the σ margin (G2 matches the FPC ratio at |z| = 0.10). The **one declared modelling choice** (flagged, not hidden): the keep window [2,4] operationalizes "off-curve"; the SIGN of the effect is window-independent (it follows from the variance ordering of two same-mean distributions), and G3 re-derives it under a different fraction p=0.30 and a recentered window [1,3]. Dependence disclosed: (a) the London-mulligan and card-selection effects (scry, cantrips, bottoming) are NOT modelled — this is the raw opening-hand draw, the correct baseline a mulligan then modifies; (b) discrete keep windows mean the exact off-curve MAGNITUDE moves with the window, but the deck-size ORDERING does not. The magnitudes (off-curve 0.21 vs 0.225, FPC ratio 1.0616) are pinned to (N, K, n, window); the SIGN and the finite-population-correction scaling are structural to sampling without replacement.

## Gate power + margin ledger
| Gate | Type | Threshold | Observed | z | Verdict |
|------|------|-----------|----------|---|---------|
| G1 | head + separation | z ≥ 3, pB > pA | pA 0.209482 vs pB 0.224975 | +16.804944 | PASS |
| G2 | mechanism anchor | \|z\| < 3 vs FPC ratio | ratio 1.061314 vs 1.061633 | −0.100413 | PASS |
| G3 | robustness (shift) | z ≥ 3, pB′ > pA′ | pA′ 0.167433 vs pB′ 0.181385 | +16.446510 | PASS |

## Probe report (v0, self-adversarial)
**1. What is this really?** A same-mean/different-variance consistency law for opening hands. The land count in a 7-card hand is hypergeometric with variance n·p·(1−p)·(N−n)/(N−1); at a matched land fraction the smaller deck has a smaller finite-population correction, so it lands in the [2,4] keep window more often — deck SIZE, not land ratio, sets consistency.
**2. What would make it false?** If the 60-card deck were NOT off-curve more often than the 40-card deck at matched fraction (G1 — the head is wrong), or if the measured variance ratio did NOT match the closed-form FPC ratio (G2 — the effect is not the finite-population correction), or if the ordering flipped or vanished under the p=0.30 shift (G3 — the law is an artifact of 40%). Any of G1/G2/G3 failing → REJECT.
**3. Simplest version that still bites?** SEED = 20260717; two decks both at 40% lands, both expecting 2.8 lands in the opening 7 — yet the 60-card deck is off-curve 22.5% of the time versus the 40-card deck's 21.0%. Same ratio, same mean, measurably different screw/flood rate.
**4. What is the counterintuitive core?** "Same land fraction ⇒ same consistency" is inverted: the mean IS the same, but the variance is not, and screw/flood is a variance phenomenon. A 40-card deck at 40% lands is strictly steadier than a 60-card deck at 40% lands.
**5. Where could I be fooling myself?** The G2 anchor is a TWO-SIDED test (small |z| = MC matches the closed-form FPC ratio), so it cannot be inflated into a false pass by large T — a wrong mechanism would show |z| ≫ 3. G1/G3 are one-sided separations whose z is large because the effect is real (Δ ≈ 1.5 points at T=400000), not because of over-precision; the mean checks (2.7996 / 2.7988 ≈ 2.8) confirm the two decks are genuinely matched in fraction, so the whole gap is variance, not a fraction mismatch.
**6. Determinism?** SEED = 20260717 pinned; in-process double run asserted byte-identical before hashing; cross-invocation double run printed IDENTICAL stdout with sha256 1280ae62…b898e33. All dict floats round()-ed to 6 dp; power sums accumulated in fixed order; compact JSON with sort_keys; no set/dict-ordering nondeterminism.
**7. Real or toy?** The hypergeometric opening-hand model is the standard, empirically load-bearing tool of competitive deckbuilding (Frank Karsten's land-count work; every deck calculator), and the finite-population correction is a textbook identity (Wikipedia, "Hypergeometric distribution"). The 40-vs-60 matched-fraction comparison is exactly the Limited-vs-Constructed consistency gap players report, so the law is the correct baseline, not a toy.
**8. How will we know it worked?** The committed stdlib verifier reproduces, under SEED = 20260717, the deck-size head (G1), the finite-population-correction mechanism anchor (G2), and the shifted-fraction robustness head (G3) at their Z_GATE = 3.0 bars, with the results-dict sha256 matching 1280ae6278b508f00d3737841768181288e7ed31f12a443d5982b5f03b898e33 across a deterministic double-run.

## One-line design fix
Tune opening-hand consistency against the hypergeometric variance n·p·(1−p)·(N−n)/(N−1) — shrink the DECK (the finite-population correction) to sharpen the early game, not just the land ratio — because two decks at the same land fraction share a mean but not a screw/flood rate.

**Recommendation: sim-ready**
