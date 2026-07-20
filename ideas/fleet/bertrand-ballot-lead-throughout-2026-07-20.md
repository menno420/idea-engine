# Counting A's a votes and B's b<a votes in random order, the probability A is STRICTLY ahead at every prefix is exactly (a−b)/(a+b) — the winning margin ratio alone, NOT A's vote share a/(a+b)

> **State:** sim-ready
> **Class:** counterintuitive-but-exactly-true · combinatorics/probability (round-52 UNRELATED slot)
> **Target:** sim-lab (VERDICT 233, +13 offset)
> **Grounding:** https://en.wikipedia.org/w/index.php?title=Bertrand%27s_ballot_theorem&action=raw&oldid=1361316938@sha1:45e367783ba2926b9ff7c826b97dba3206c45219 · fetched 2026-07-20
> **Verifier (firsthand):** stdlib-only, SEED=20260717; results-dict sha256 d52f08b930d92b01ee8d0f81089974843262710f301dd738594602bf3d4378aa

## The phenomenon (one line)
A ballot box holds a votes for A and b < a votes for B; the ballots are drawn and tallied in uniformly random order. The probability that A is STRICTLY ahead of B at EVERY prefix of the count — A leads wire-to-wire, never tied, never once behind — is EXACTLY (a−b)/(a+b). The answer is a clean rational in the two tallies, and it depends only on the winning margin ratio: scale both tallies by any k and the probability does not move.

## The folk belief
"A won by a lot, so A almost surely led the whole way" — and, when pressed for a number, the plausible reflex is A's share of the vote, a/(a+b): the fraction of ballots that are A's, equivalently the chance the FIRST ballot drawn is an A. Both readings are wrong. The lead-throughout probability is the MARGIN ratio (a−b)/(a+b), which is strictly smaller than the vote share a/(a+b) for every b>0, and unlike the share it is scale-invariant. A 3-to-1 landslide (a=3, b=1) leads throughout only half the time (1/2), not the 3/4 the vote-share intuition suggests; a 7-to-3 win leads throughout just 2/5 of the time, not 7/10.

## The thesis (reasoned to fuller form — Q-0254 duty)
Lining up a+b ballots in a uniformly random order is choosing one of the C(a+b, a) distinct A/B arrangements with equal weight; "A strictly ahead throughout" is the event that every prefix has strictly more A's than B's — a path from (0,0) that stays strictly above the diagonal after the first step. Counting those favourable arrangements is a lattice-path problem, and the reflection / cycle-lemma argument shows their number is exactly (a−b)/(a+b)·C(a+b, a), so the probability is (a−b)/(a+b). Two things make this counterintuitive and worth pinning. First, the answer is the MARGIN, not the mass: the vote share a/(a+b) is the probability the LAST (or first) ballot is A's, a genuinely different quantity that the induction proof uses as an intermediate step but never as the answer — so "share of the vote" is a plausible impostor, not the truth. Second, the answer is scale-free: (ka−kb)/(ka+kb) = (a−b)/(a+b), so doubling every tally leaves the lead-throughout probability unchanged even though the counts, and the number of favourable arrangements, both explode. The probability rides purely on the ratio of the winning margin (a−b) to the total (a+b); the absolute scale of the election is irrelevant. That the exact count carries the factor (a−b)/(a+b) out front of the binomial is the whole surprise: a wire-to-wire lead is governed by how decisively A won, not by how many votes A piled up.

## The formal model (committed constants, the (a,b) grids, exact)
- **Sample space.** For tallies (a, b) with b < a, the a+b ballots are opened in uniformly random order; equivalently one of the C(a+b, a) distinct A/B arrangements is chosen uniformly. "A ahead throughout" = every non-empty prefix has (#A so far) > (#B so far).
- **Exact core identity (G1).** The brute-force favourable count over ALL C(a+b, a) arrangements gives `Fraction(brute_favorable, C(a+b, a)) == Fraction(a−b, a+b)`, evaluated on the enumeration grid (a,b) ∈ {(3,1),(4,2),(5,2),(5,3),(6,3),(7,2)}. Equivalently `brute_favorable == (a−b)/(a+b)·C(a+b, a)` exactly. No float enters this leg.
- **Exact scale-invariance (G2).** Base pair (2,1) with ratio 1/3: for k ∈ {1,2,3,5}, `Fraction(k·a−k·b, k·a+k·b) == Fraction(a−b, a+b)` AND the brute count identity still holds on each enumerable scaled case, up to (10,5) → 1001/3003 = 1/3. The value depends only on the margin ratio.
- **Monte-Carlo grid (G3/G4).** MC_PAIRS = {(3,1),(5,2),(7,3)}, MC_T = 200000 seeded shuffles per pair, drawn back-to-back in listed order from a single `random.Random(20260717)`; the empirical lead-throughout rate is compared to (a−b)/(a+b) (G3, agreement) and to the naive a/(a+b) (G4, rejection). Binomial SE = sqrt(p(1−p)/T).
- All exact legs (G1, G2, and G4's corrupt-count leg) use `fractions.Fraction` — no floating point enters any exact identity; floats appear only in the Monte-Carlo z-scores.

## Pinned world (committed constants)
SEED=20260717 · all randomness from `random.Random(20260717)` consumed in a fixed, documented order · G1 enumeration grid (a,b) ∈ {(3,1),(4,2),(5,2),(5,3),(6,3),(7,2)} · G2 base (2,1) scaled by k∈{1,2,3,5} · G3/G4 Monte-Carlo pairs {(3,1),(5,2),(7,3)}, T=200000 trials each · G4 naive model prob=a/(a+b) · G4 corrupt-count model a/(a+b)·C(a+b,a).

## Pre-registered gates (sim-ready iff ALL hold, in order)
**G1 — Exact identity (Fraction ==).** For (a,b) ∈ {(3,1),(4,2),(5,2),(5,3),(6,3),(7,2)}, the brute favourable count over ALL C(a+b,a) arrangements gives `Fraction(brute, C(a+b,a)) == Fraction(a−b, a+b)` exactly. *Direction:* exact equality — pass iff rational equality holds for every pair (no float).
**G2 — Exact scale-invariance (Fraction ==).** For base (2,1) and k ∈ {1,2,3,5}, `Fraction(k·a−k·b, k·a+k·b) == Fraction(a−b, a+b)` AND the brute count identity holds on each enumerable scaled case up to (10,5)→1001/3003=1/3. *Direction:* exact equality — the value depends only on the margin ratio, not scale.
**G3 — Monte-Carlo agreement (|z| ≤ 3).** For (a,b) ∈ {(3,1),(5,2),(7,3)}, T=200000 seeded shuffles: the empirical lead-throughout rate lands within 3·SE of (a−b)/(a+b). *Direction:* within 3σ = agreement — pass iff `|z| ≤ 3` for all three pairs (z = 1.01965, −1.2489, −0.392605).
**G4 — Falsifiability (naive REJECTED at |z| > 5).** On the SAME Monte-Carlo sample that agrees with the true law (G3), the plausible-but-wrong model prob=a/(a+b) (A's vote share = P(first vote is A)) is rejected at large |z| (−222.587729, −259.552892, −274.303069); PLUS an exact leg confirms the corrupt count a/(a+b)·C(a+b,a) ≠ the brute favourable count on all six G1 pairs. *Direction:* naive rejected at |z|>5 (and exact corrupt count ≠ brute) — the gate FAILS if the naive model is NOT rejected.

## Pre-registered decision rule
sim-ready iff G1 ∧ G2 ∧ G3 ∧ G4 all hold in their stated directions, AND the naive vote-share model a/(a+b) is REJECTED (Monte-Carlo |z|>5 on the same sample) while the true (a−b)/(a+b) is NOT (|z|≤3), AND the corrupt count a/(a+b)·C(a+b,a) ≠ the brute favourable count on every G1 pair, AND the in-process double-run digest is stable.

## Dry-sim results
```json
{
  "g1_exact_identity": {
    "3,1": {
      "brute_prob": "1/2",
      "closed_form": "1/2",
      "equal": true,
      "favorable": 2,
      "total": 4
    },
    "4,2": {
      "brute_prob": "1/3",
      "closed_form": "1/3",
      "equal": true,
      "favorable": 5,
      "total": 15
    },
    "5,2": {
      "brute_prob": "3/7",
      "closed_form": "3/7",
      "equal": true,
      "favorable": 9,
      "total": 21
    },
    "5,3": {
      "brute_prob": "1/4",
      "closed_form": "1/4",
      "equal": true,
      "favorable": 14,
      "total": 56
    },
    "6,3": {
      "brute_prob": "1/3",
      "closed_form": "1/3",
      "equal": true,
      "favorable": 28,
      "total": 84
    },
    "7,2": {
      "brute_prob": "5/9",
      "closed_form": "5/9",
      "equal": true,
      "favorable": 20,
      "total": 36
    }
  },
  "g2_scale_invariance": {
    "all_count_identities_hold": true,
    "all_ratios_equal_base": true,
    "base_pair": [
      2,
      1
    ],
    "base_ratio": "1/3",
    "per_k": {
      "1": {
        "a": 2,
        "b": 1,
        "brute_prob": "1/3",
        "count_identity_holds": true,
        "favorable": 1,
        "ratio_equals_base": true,
        "scaled_ratio": "1/3",
        "total": 3
      },
      "2": {
        "a": 4,
        "b": 2,
        "brute_prob": "1/3",
        "count_identity_holds": true,
        "favorable": 5,
        "ratio_equals_base": true,
        "scaled_ratio": "1/3",
        "total": 15
      },
      "3": {
        "a": 6,
        "b": 3,
        "brute_prob": "1/3",
        "count_identity_holds": true,
        "favorable": 28,
        "ratio_equals_base": true,
        "scaled_ratio": "1/3",
        "total": 84
      },
      "5": {
        "a": 10,
        "b": 5,
        "brute_prob": "1/3",
        "count_identity_holds": true,
        "favorable": 1001,
        "ratio_equals_base": true,
        "scaled_ratio": "1/3",
        "total": 3003
      }
    }
  },
  "g3_montecarlo": {
    "3,1": {
      "mean": 0.50114,
      "se": 0.001118031083,
      "target": 0.5,
      "target_frac": "1/2",
      "within_3sigma": true,
      "z": 1.01965
    },
    "5,2": {
      "mean": 0.42719,
      "se": 0.001106116413,
      "target": 0.428571429,
      "target_frac": "3/7",
      "within_3sigma": true,
      "z": -1.2489
    },
    "7,3": {
      "mean": 0.39957,
      "se": 0.001095248408,
      "target": 0.4,
      "target_frac": "2/5",
      "within_3sigma": true,
      "z": -0.392605
    }
  },
  "g4_falsifiability": {
    "all_corrupt_neq_brute": true,
    "all_naive_rejected": true,
    "exact_corrupt_count_leg": {
      "3,1": {
        "brute_favorable": 2,
        "corrupt_count": "3/1",
        "corrupt_neq_brute": true
      },
      "4,2": {
        "brute_favorable": 5,
        "corrupt_count": "10/1",
        "corrupt_neq_brute": true
      },
      "5,2": {
        "brute_favorable": 9,
        "corrupt_count": "15/1",
        "corrupt_neq_brute": true
      },
      "5,3": {
        "brute_favorable": 14,
        "corrupt_count": "35/1",
        "corrupt_neq_brute": true
      },
      "6,3": {
        "brute_favorable": 28,
        "corrupt_count": "56/1",
        "corrupt_neq_brute": true
      },
      "7,2": {
        "brute_favorable": 20,
        "corrupt_count": "28/1",
        "corrupt_neq_brute": true
      }
    },
    "naive_model": "prob = a/(a+b) (A vote share / P(first vote is A))",
    "per_pair": {
      "3,1": {
        "mean": 0.50114,
        "naive_frac": "3/4",
        "naive_rejected": true,
        "naive_value": 0.75,
        "z_naive": -222.587729
      },
      "5,2": {
        "mean": 0.42719,
        "naive_frac": "5/7",
        "naive_rejected": true,
        "naive_value": 0.714285714,
        "z_naive": -259.552892
      },
      "7,3": {
        "mean": 0.39957,
        "naive_frac": "7/10",
        "naive_rejected": true,
        "naive_value": 0.7,
        "z_naive": -274.303069
      }
    }
  },
  "gates": {
    "G1": true,
    "G2": true,
    "G3": true,
    "G4": true
  },
  "mc_pairs": [
    [
      3,
      1
    ],
    [
      5,
      2
    ],
    [
      7,
      3
    ]
  ],
  "mc_trials": 200000,
  "proposal": 220,
  "seed": 20260717,
  "sim_ready": true,
  "slot": "round-52 UNRELATED (fleet->venture->game->unrelated)",
  "theorem": "Bertrand ballot theorem (lead-throughout)",
  "verdict": 233
}
```
results_sha256=d52f08b930d92b01ee8d0f81089974843262710f301dd738594602bf3d4378aa

**Disclosed results-dict sha256 = `d52f08b930d92b01ee8d0f81089974843262710f301dd738594602bf3d4378aa`** — A leads throughout with probability exactly (a−b)/(a+b) (G1 exact identity holds for all six pairs — e.g. (3,1)→1/2, (7,2)→5/9; G2 scale-invariance holds for base (2,1) up to (10,5)→1001/3003=1/3; G3 Monte-Carlo means match the margin ratio within z = 1.02, −1.25, −0.39; G4 the naive vote-share model a/(a+b) is rejected at z ≈ −222.6, −259.6, −274.3 on the SAME sample).

## Verifier
`sims/verdict-233-bertrand-ballot/bertrand-ballot-lead-throughout.py` (sim-lab; merged) — stdlib only (`hashlib`, `itertools`, `json`, `math`, `random`, `fractions.Fraction`), SEED=20260717, all randomness from a single `random.Random(20260717)` consumed in a fixed, documented order; the results dict is built twice and both canonical dumps are asserted identical (`determinism_double_run=True`) before exit, and two separate invocations print the byte-identical digest.
```reproduce
python3 sims/verdict-233-bertrand-ballot/bertrand-ballot-lead-throughout.py
# prints the results JSON, then results_sha256=d52f08b930d92b01ee8d0f81089974843262710f301dd738594602bf3d4378aa, then determinism_double_run=True, sim_ready=True; exits 0
```

## Why it matters
It is a clean counterexample to reading "how decisively A won" off the wrong number. The margin ratio (a−b)/(a+b) governs wire-to-wire dominance, and it is strictly and often dramatically smaller than the vote share a/(a+b) — a 3-to-1 result leads throughout only half the time, not three-quarters. The same lattice-path count is the engine behind the Catalan numbers, the reflection principle, and the run-of-luck questions that recur everywhere a sequential tally is read as a proxy for strength: which side "was ahead the whole game," how often a favourite never trails, the fraction of order-books where bids stay strictly above asks. Scale-invariance is the extra teeth: the probability of a wire-to-wire lead is fixed by the ratio, so a bigger election with the same margin ratio is no more (and no less) likely to produce a never-behind winner.

## Dedup
Grepped all lanes (`ideas/**`) at boot high-water P219: no Bertrand-ballot / lead-throughout / ballot-theorem card exists (`ls ideas/fleet/ | grep -iE 'ballot|lead-through'` returned NO slug; no collision on `bertrand-ballot-lead-throughout`). The only `bertrand`-slug hit is a DIFFERENT theorem — **bertrand-paradox-chord** (Bertrand's *paradox*: three natural definitions of "random chord" give 1/3, 1/2, 1/4 — an under-specification result about continuous geometric probability, sharing only the name "Bertrand"; this card is Bertrand's *ballot theorem*, a discrete exact lattice-path count). Distinct from the two nearest probabilistic neighbours in `ideas/fleet/`: **arcsine-lead-illusion** (Lévy's arcsine law — the *distribution of time spent in the lead* in a FAIR (a=b in expectation) zero-edge walk is U-shaped; this card is the *probability of leading at every prefix* in an UNFAIR count with a fixed margin b<a, an exact rational not an arcsine density); **gamblers-ruin-edge-asymmetry** (absorbing-barrier ruin probability (1−(q/p)^i)/(1−(q/p)^N), exponential in the edge — a first-passage-to-a-barrier quantity, whereas this card is a stay-strictly-above-the-diagonal count with no barriers and an exact margin-ratio answer). No existing card computes the ballot-theorem lead-throughout probability.

## Model basis (declared model-dependence — the P024 discipline)
The result is exact GIVEN the model: a+b ballots opened in uniformly random order (all C(a+b,a) arrangements equally likely), "ahead throughout" = every non-empty prefix strictly more A's than B's, tallies fixed at (a, b) with b<a. G1/G2 (and G4's corrupt-count leg) carry no probabilistic assumption — they are `Fraction` identities over full enumeration; G3/G4's Monte-Carlo legs are seeded sampling cross-checks of the closed form, not the proof. Non-uniform draw orders (e.g. correlated ballots, stratified precincts), ties counted as "ahead," or a weak-inequality "≥" definition would change the count and are out of scope.

## One-line design fix
When you want "how convincingly A led," report the margin ratio (a−b)/(a+b), not the vote share a/(a+b): the former is the exact probability of a wire-to-wire lead and is scale-invariant, while the share systematically overstates dominance (and grows with turnout at fixed margin).

## Probe report (v0, 2026-07-20)
**1. Is the headline claim exactly true or only statistically likely?** Exactly true for the identity: G1 proves `Fraction(brute, C(a+b,a)) == Fraction(a−b, a+b)` by rational equality over FULL enumeration for all six pairs, and equivalently brute = (a−b)/(a+b)·C(a+b,a); the Monte-Carlo gates (G3) only cross-check the closed form by sampling, they do not establish it.
**2. Is the sample space unambiguously defined?** Yes: tallies fixed at (a,b) with b<a, the a+b ballots opened in uniformly random order (one of C(a+b,a) equally likely arrangements), and "ahead throughout" committed as: every non-empty prefix has strictly more A's than B's — no ties, no weak inequality.
**3. Does the favourable count actually carry the (a−b)/(a+b) factor, or is that asserted?** It is computed, not asserted: G1 enumerates every arrangement and checks the count against (a−b)/(a+b)·C(a+b,a) as `Fraction`s; e.g. (5,2) gives 9 favourable of 21 = 3/7, (7,2) gives 20 of 36 = 5/9 — both exact.
**4. Is the scale-invariance a real check or a restatement?** Real: G2 both algebraically checks `Fraction(ka−kb, ka+kb) == Fraction(a−b, a+b)` for k∈{1,2,3,5} AND re-enumerates each scaled case where tractable — (2,1)→1/3, (4,2)→1/3, (6,3)→1/3, (10,5)→1001/3003=1/3 — so the invariance is confirmed by independent brute counts, not just cancellation.
**5. Is the ≥3σ gate a real check or a tautology given the exact identity?** Independent seeded sampling cross-check: G3 draws 200000 fresh shuffles per pair from `random.Random(20260717)` and tests the empirical rate against the closed form (z = 1.02 at (3,1), −1.25 at (5,2), −0.39 at (7,3), all within 3σ); a mismatch between sampler and formula would flag here.
**6. Does the gate battery actually REJECT the plausible wrong model?** Yes — this is G4's whole point: on the SAME sample that confirms (a−b)/(a+b), the naive vote-share model a/(a+b) is rejected at z ≈ −222.6, −259.6, −274.3 (|z|≫5), and an exact leg shows a/(a+b)·C(a+b,a) ≠ the brute count on all six pairs. The falsifiability is two-sided: the truth is not rejected, the impostor is.
**7. Is the grounding an external citation and is its caveat accurate to the pinned revision?** The grounding pins Wikipedia "Bertrand's ballot theorem" oldid 1361316938 (raw-wikitext sha1 45e367783ba2926b9ff7c826b97dba3206c45219; "Bertrand's ballot problem" is a redirect to this title). That revision states, in its own variables p=a, q=b: *"candidate A receives p votes and candidate B receives q votes with p>q … the probability that A will be strictly ahead of B throughout the count … The answer is (p−q)/(p+q)"* and carries the favourable-count form binom(p+q,q)·(p−q)/(p+q) — both re-confirmed by WebFetch of the raw wikitext. Honestly, the term a/(a+b) DOES appear on the page, but only as P(last vote is A) inside the induction step (and q/(p+q) as P(sequence begins with B) in the reflection proof), NOT as the answer — so the G4 naive model is a genuine impostor the page itself distinguishes. The SEED, the (a,b) grids, the Monte-Carlo procedure, and the results_sha256 are NOT on the page — they are this verifier's firsthand computation.
**8. Is the verifier deterministic and reproducible cross-invocation?** Yes: no wall-clock or OS entropy; all randomness from `random.Random(20260717)` consumed in a fixed order, the results dict is built twice and both canonical dumps asserted identical (determinism_double_run=True), and two separate invocations print the byte-identical digest d52f08b930d92b01ee8d0f81089974843262710f301dd738594602bf3d4378aa. The sim-lab verifier for this head is already merged (PROPOSAL 220 → VERDICT 233, +13 offset).

### Grounding-accuracy assessment
The caveat is honest — neither oversold nor undersold. It does NOT claim Wikipedia contains this sim: the SEED=20260717, the (a,b) enumeration/Monte-Carlo grids, the seeded 200000-shuffle procedure, and the results_sha256 are disclosed as firsthand reproduction, absent from the pinned revision. And it does NOT undersell the source: the analytic theorem and its exact answer (p−q)/(p+q), together with the favourable-count form binom(p+q,q)·(p−q)/(p+q), ARE literally on oldid 1361316938 (sha1 45e367783ba2926b9ff7c826b97dba3206c45219, re-confirmed by raw-wikitext WebFetch). The one subtlety is stated plainly rather than hidden: the vote-share term a/(a+b) is present on-page, but only as P(last vote is A) in the induction — not as the answer — which is exactly why the G4 naive model is a legitimate impostor the page distinguishes, per the V222 grounding-scrutiny lesson.

**Recommendation: sim-ready**
