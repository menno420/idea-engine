# Rich get richer, yet the finish is a coin toss: a Pólya urn ends uniform

> **State:** sim-ready
> **Class:** counterintuitive-probability (round-49 UNRELATED slot)
> **Target:** sim-lab (VERDICT 221, +13 offset)
> 📊 Model: Claude Opus · high · idea/planning
> **Grounding:** https://en.wikipedia.org/w/index.php?title=P%C3%B3lya_urn_model&oldid=1334383855@ac150a6b0ddb3f3d3f8d54b040ce1ed29a0fbbf8 · fetched 2026-07-20
> **Reference (external, reachable):** "It is a martingale and converges to the beta distribution when n → ∞."
> **Verifier (firsthand):** ideas/fleet/polya_urn_reinforcement_uniform_finish.py · results-dict sha256 d566e380865bfb7089d5042ed7169edfddc7cab7f112af80de6ef2c29c91aa68

## The phenomenon

An urn that rewards whichever colour it draws — the textbook "rich get richer" process — does not lock in a leader. After any number of draws, every possible black-share is exactly equally likely.

## Domain

Probability / stochastic processes: the Pólya–Eggenberger urn, exchangeability, and de Finetti's theorem. Outside fleet-ops, venture, and game theory — a pure counterintuitive-math head.

## The folk belief

Positive feedback compounds, so intuition offers two stories, both wrong: (a) the share "averages out" to its 1/2 starting ratio as draws accumulate (a law-of-large-numbers reflex), or (b) an early lead runs away to an extreme. Either way the outcome should be predictable or concentrated.

## The thesis (reasoned to fuller form)

Both intuitions fail, for opposite reasons. The black-share is a bounded martingale, so it *does* converge — but to a **random** limit, not a fixed one. For the symmetric urn (1 black, 1 white, add 1 of the drawn colour) that limit is **uniform on [0,1]**: the count of black draws after n steps is exactly uniform on {0..n} with probability 1/(n+1) each, and the dispersion of the final share is a constant 1/12 that never shrinks with n.

The mechanism is **exchangeability**: any two draw sequences with the same number of blacks are equiprobable, so by de Finetti the whole process is a *uniform mixture of i.i.d. coins* — a hidden bias p is effectively drawn uniformly at the start and then merely revealed, draw by draw. That is why reinforcement neither averages out (the naive LLN is defeated — the spread does not vanish) nor runs away (perfect symmetry — every share equally likely). Change the seed to (a black, b white) and the same machinery yields a **Beta(a, b)** limit with mean a/(a+b): the *shape* is a knob, but the *non-vanishing spread* is the invariant.

## The pinned world (committed constants)

- `SEED = 20260717`
- Exact enumeration: n = 1..20 (dynamic program over exact rational transition probabilities, `fractions.Fraction`).
- Monte-Carlo: N_MC = 200 draws per trajectory, M_MC = 20000 trajectories.
- Starts: symmetric (1, 1) → uniform; shifted (2, 1) → Beta(2, 1), mean 2/3.

## Pre-registered gates

- **G1 — EXACT (AGREEMENT, zero deviation).** The exact law of the black-count for n = 1..20 equals the closed form 1/(n+1) (and the Beta-binomial(1,1) pmf), computed with `Fraction`. Direction: exact equality, `max_abs_deviation == 0`.
- **G2 — SIGNAL (≥ 3σ).** The Monte-Carlo final-share variance stays ≈ 1/12, whereas an LLN/i.i.d. null concentrates the share with variance 1/(4·N_MC) → 0. z of the gap is large and grows with n. Direction: **high z** (reinforcement defeats the LLN; dispersion does not vanish).
- **G3 — AGREEMENT (low |z|).** The Monte-Carlo middle-third occupancy matches the exact-law middle-third probability within noise. Direction: **|z| < 3** (MC converges to the exact uniform law).
- **G4 — SHIFT / robustness.** The asymmetric start (2, 1) has its exact law match the Beta-binomial(2,1) closed form (`Fraction`, zero deviation), and its MC mean share shifts to 2/3, many σ away from the symmetric 1/2. Direction: exact-agreement + directional shift.
- **G5 — DETERMINISM.** In-process double-run identical; cross-invocation byte-identical.

## Pre-registered decision rule

`sim-ready` iff G1 zero-deviation AND G2 z ≥ 3 AND G3 |z| < 3 AND G4 (zero-deviation AND |z| ≥ 3) AND G5 identical — all on the deterministic double-run.

## Dry-sim results (verbatim)

```json
{
  "G1_exact_uniform": {
    "closed_form": "P(K_n=k)=1/(n+1)",
    "direction": "exact-agreement (Fraction, zero deviation)",
    "max_abs_deviation": "0",
    "n_range": [
      1,
      20
    ],
    "pass": true,
    "sample_law_n3": [
      "1/4",
      "1/4",
      "1/4",
      "1/4"
    ]
  },
  "G2_signal_dispersion_vs_lln": {
    "direction": "high z = SIGNAL (dispersion does not vanish; LLN defeated by reinforcement)",
    "iid_observed_var": 0.0012472517,
    "lln_null_var": 0.00125,
    "observed_var": 0.0838204573,
    "pass": true,
    "se_null": 1.2500313e-05,
    "threshold": 3.0,
    "uniform_pred_var": 0.0833333333,
    "z": 6605.4714
  },
  "G3_agreement_mc_matches_exact": {
    "abs_z": 2.11,
    "direction": "low |z| = AGREEMENT (Monte-Carlo converges to the exact uniform law)",
    "exact_middle_third_prob": 0.3333333333,
    "mc_middle_third_rate": 0.3263,
    "pass": true,
    "se": 0.0033333333,
    "threshold": 3.0
  },
  "G4_shift_asymmetric_start": {
    "direction": "exact-agreement to Beta(2,1) + mean shifts many sigma from 1/2 (robustness/shift)",
    "exact_max_abs_deviation": "0",
    "mc_mean_share": 0.6665581281,
    "pass": true,
    "predicted_mean": 0.6666666667,
    "threshold": 3.0,
    "z_vs_half": 100.9484
  },
  "G5_determinism": {
    "in_process_double_run": "IDENTICAL",
    "pass": true
  },
  "all_gates_pass": true,
  "head": "polya-urn-reinforcement-uniform-finish",
  "params": {
    "m_mc": 20000,
    "n_enum_max": 20,
    "n_mc": 200,
    "start_shift": [
      2,
      1
    ],
    "start_symmetric": [
      1,
      1
    ]
  },
  "seed": 20260717
}
```

`results_sha256: d566e380865bfb7089d5042ed7169edfddc7cab7f112af80de6ef2c29c91aa68` · `in_process_double_run: IDENTICAL` · cross-invocation byte-identical.

## Honest nuance (disclosed)

- The *flat* (uniform) limit is exact only for the symmetric +1 urn. A general start (a, b) or reinforcement +c gives a Beta(a/c, b/c) limit — still non-degenerate (spread never vanishes), but only (1,1,+1) is uniform. G4 exercises this.
- The exact claim is discrete: for finite n the black-count is exactly uniform on a grid of n+1 points; "uniform on [0,1]" is the n→∞ statement. G1 proves the finite-n exactness; G3 only illustrates convergence.
- G2's z is astronomically large **by construction** (a constant-variance process against a variance-→0 null); it certifies the *direction* of the surprise, not a delicate effect. The rigorous claim is the exact gate G1.

## Dedup

Grep across ALL `ideas/` lanes (fleet, venture-lab, superbot-games) on 2026-07-20 found no prior Pólya-urn, reinforcement, or exchangeability head. Distinct from the friendship paradox (P164), giant-component threshold, the arcsine law (P116), and martingale-flavoured ergodicity / positive-EV ruin (which concern *time averages* and *ruin*, not a reinforcement limit law).

## Reproduce

`python3 ideas/fleet/polya_urn_reinforcement_uniform_finish.py` — prints the results dict and `results_sha256`. Run twice; stdout is byte-identical.

## Verifier

`ideas/fleet/polya_urn_reinforcement_uniform_finish.py` (stdlib only: `fractions`, `random`, `hashlib`, `json`, `math`).

## Why it matters

The urn is the cleanest counterexample to "positive feedback ⇒ predictable winner." It shows a process can be *strongly* path-dependent (highly autocorrelated, a genuine martingale) yet have a *maximally* spread, non-collapsing outcome law. The exchangeability lens — a random bias fixed once and then revealed — is the same trick behind Bayesian conjugate priors and preferential-attachment models, so the head generalises well beyond the toy.

## Model basis

Reasoned and pre-registered by an idea/planning pass; all constants committed before the dry-sim; gates and directions fixed in advance.

## Probe report (v0)

**1. Is the head exactly true or only approximately?**
Exactly. G1 enumerates the black-count law with `Fraction` for n = 1..20 and matches 1/(n+1) (and Beta-binomial(1,1)) with `max_abs_deviation == 0`.

**2. Could the surprise be an artifact of small n?**
No. The exact result holds for every n; the MC run at n = 200 (G3) confirms convergence to the same law, and G2 shows the spread is constant in n rather than shrinking.

**3. Does the ≥3σ signal test a real effect or a tautology?**
It certifies a real direction — the final-share variance stays ≈ 1/12 while an i.i.d. LLN null drives it to 0 — but the z is huge by construction (z = 6605.4714). This is disclosed; the rigorous claim rests on the exact gate G1, with G2 as the empirical illustration.

**4. Is the mechanism reproducible deterministically?**
Yes. `SEED = 20260717`; in-process double-run IDENTICAL and cross-invocation byte-identical (G5).

**5. Is it genuinely unbuilt in the lab?**
Yes. A grep across all `ideas/` lanes on 2026-07-20 found no Pólya / urn / exchangeability head; the nearest neighbours (friendship paradox, arcsine, giant component) use different mechanisms.

**6. What breaks the "uniform" claim?**
Only the symmetric +1 urn is flat. An asymmetric start (2, 1) gives Beta(2, 1) (G4 confirms exact agreement and a mean shift to 2/3, |z| = 100.9484); reinforcement +c gives Beta(a/c, b/c). Disclosed above.

**7. Is the grounding external and specific?**
Yes — a pinned Wikipedia "Pólya urn model" revision (raw-wikitext sha1). It supports both the reinforcement dynamics and the Beta/uniform limit; the caveat is that the page states the general Beta limit with the uniform case as the symmetric example, whereas the verifier is that specific worked example.

**8. What would a verdict measure?**
Re-run the verifier and confirm G1 zero-deviation, G2 z ≥ 3, G3 |z| = 2.11 < 3, G4 zero-deviation and |z| ≥ 3, G5 identical, then recompute the results-dict sha256 and check it matches d566e380865bfb7089d5042ed7169edfddc7cab7f112af80de6ef2c29c91aa68.

**Recommendation: sim-ready**
