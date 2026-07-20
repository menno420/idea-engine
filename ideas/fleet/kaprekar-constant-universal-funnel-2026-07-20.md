# Kaprekar's routine funnels every 4-digit number to the single constant 6174 in at most 7 steps

> **State:** sim-ready
> **Class:** counterintuitive-but-exactly-true · recreational number theory (round-51 UNRELATED slot)
> **Target:** sim-lab (VERDICT 229, +13 offset)
> **Grounding:** https://en.wikipedia.org/w/index.php?title=Kaprekar's_routine&oldid=1364472561@9190b7328602bbc2de0eaad722e5bba4218d8c5b · fetched 2026-07-20
> **Verifier (firsthand):** stdlib-only, SEED=20260717; results-dict sha256 6ef877698bbb91eadffa8473c4a0ec6276f62fd3b8af73fd90855288b38ebf0d

## The phenomenon (one line)
Take any 4-digit number with at least two different digits, repeatedly replace it with (its digits sorted descending) minus (its digits sorted ascending), and within at most seven steps you land on 6174 and stay there — from every one of the 8991 valid starting numbers.

## The folk belief
Iterating an arithmetic shuffle on arbitrary inputs ought to scatter: different starts drift to different endpoints, or wander without ever settling. One universal endpoint, reached from all 8991 valid starts inside a fixed step budget, sounds like sleight of hand.

## The Kaprekar thesis (reasoned to fuller form — Q-0254 duty)
The map D(n) = desc(n) − asc(n) on 4-digit strings is not a scrambler; it is a contraction onto a single absorbing state. Three facts make the whole domain collapse: (a) D maps the valid domain into itself under 4-digit zero-padding; (b) among non-repdigit inputs D has exactly one fixed point, 6174, and no longer cycles; (c) every trajectory is strictly finite and short — the longest takes exactly 7 steps. So "which start you pick" changes only how many of those ≤7 steps you spend, never the destination. The behaviour is base- and width-specific: the 3-digit routine collapses just as hard but onto a DIFFERENT constant, 495.

## The formal model (committed constants, exact)
- Domain: integers 1000–9999 with at least two distinct digits (the 9 repdigits 1111…9999 excluded) → 8991 inputs.
- Step map: D(n) = int(digits sorted descending) − int(digits sorted ascending); intermediate values are zero-padded back to 4 digits before the next step.
- Fixed point under test: 6174.
- Dimension-shift control: 3-digit domain 100–999 non-repdigit (891 inputs), fixed point 495, ≤6 steps.
- All of G1/G2/G4 are integer-exact by exhaustive enumeration (no floating point); the exact mean step-count is reported as a `fractions.Fraction`.

## Pinned world (committed constants)
SEED=20260717 · N_MC=200000 · null p0=99/100 · 4-digit domain size 8991 · 3-digit domain size 891.

## Pre-registered gates (sim-ready iff ALL hold, in order)
**G1 — Exhaustive convergence + tight bound (exact, integer).** Over all 8991 valid 4-digit inputs, `nonconverge == 0` and `max_steps == 7`. *Direction:* pass iff every input reaches 6174 AND the maximum step-count equals 7 — this simultaneously REJECTS the deliberately-wrong tighter bound "≤6 steps" (falsifiability leg).
**G2 — Unique fixed point (exact).** The valid 4-digit domain contains exactly one fixed point of D, equal to 6174. *Direction:* pass iff `four_fixed_points == [6174]`.
**G3 — Monte-Carlo confirmation (≥3σ).** 200000 seeded uniform draws (SEED=20260717) all reach 6174 in ≤7 steps; the one-sided z of the observed success rate against H0 `p0 = 0.99` ("numbers do NOT all converge") is ≥3. *Direction:* pass iff `z ≥ 3` and `successes == n_draws` (observed z ≈ 44.946657, rejecting the not-all-converge null far beyond 3σ).
**G4 — Dimension-shift robustness (exact).** The 3-digit routine funnels all 891 valid inputs to the DIFFERENT constant 495 within ≤6 steps. *Direction:* pass iff `nonconverge == 0` and `three_fixed_points == [495]` and `max_steps == 6`.

## Pre-registered decision rule
sim-ready iff G1 ∧ G2 ∧ G3 ∧ G4 all hold in their stated directions, AND the deliberately-wrong bound "max_steps ≤ 6" is rejected, AND the in-process double-run digest is stable.

## Dry-sim results
```json
{
  "four_digit": {
    "domain_size": 8991,
    "max_steps": 7,
    "mean_steps": "42065/8991",
    "nonconverge": 0,
    "total_steps": 42065
  },
  "four_fixed_points": [
    6174
  ],
  "gates": {
    "G1": true,
    "G2": true,
    "G3": true,
    "G4": true
  },
  "mc_4digit": {
    "n_draws": 200000,
    "null_p0": "99/100",
    "p_hat": "1/1",
    "successes": 200000,
    "z": 44.946657
  },
  "proposal": 216,
  "seed": 20260717,
  "sim_ready": true,
  "three_digit": {
    "domain_size": 891,
    "max_steps": 6,
    "mean_steps": "2866/891",
    "nonconverge": 0,
    "total_steps": 2866
  },
  "three_fixed_points": [
    495
  ],
  "wrong_bound_max6_rejected": true
}
```
results_sha256=6ef877698bbb91eadffa8473c4a0ec6276f62fd3b8af73fd90855288b38ebf0d

**Disclosed results-dict sha256 = `6ef877698bbb91eadffa8473c4a0ec6276f62fd3b8af73fd90855288b38ebf0d`**

## Verifier
`ideas/fleet/kaprekar-constant-universal-funnel-2026-07-20.py` — stdlib only (`hashlib`, `json`, `fractions`), SEED=20260717, custom LCG for the seeded draws so cross-invocation output is byte-identical.
```reproduce
python3 ideas/fleet/kaprekar-constant-universal-funnel-2026-07-20.py
# prints the results JSON, then results_sha256=6ef877698bbb91eadffa8473c4a0ec6276f62fd3b8af73fd90855288b38ebf0d, then determinism_double_run=True; exits 0
```

## Why it matters
It is a clean counterexample to the intuition that "arithmetic scrambling scatters." A deterministic digit map can be a global contraction to a unique attractor reached in a tiny, provable number of steps. The same shape recurs wherever a state-reducing map has one absorbing state and no other cycles — the analysis pattern (enumerate the domain, prove single fixed point, bound the trajectory length) transfers directly to fixed-point/termination arguments in other finite systems.

## Dedup
Grepped all lanes (`ideas/**`) at boot high-water P215: no dedicated Kaprekar card exists (`grep -ril kaprekar ideas/` returned nothing). Distinct from the built urn/probability cards (polya-urn, banach-matchbox, bertrand, hundred-prisoners) and from base-rate/arcsine/coupon builds — this is a deterministic digit-map fixed-point result, not a stochastic one. "buffon" and "monty" appear only as passing mentions inside `hundred-prisoners`; 6174 is unrelated to both. No slug collision.

## Model basis (declared model-dependence — the P024 discipline)
The result is exact GIVEN the committed step definition D(n) = desc − asc over base-10, width-4, zero-padded representation. It is base- and width-dependent: the shift control shows width 3 collapses to 495, a different constant, and other bases/widths need not admit a single Kaprekar constant at all. No probabilistic assumptions enter G1/G2/G4 (exhaustive); G3 is only a sampling cross-check of the exhaustive result.

## One-line design fix
n/a — this is a mathematical fact, not a system defect; the transferable lesson is that "shuffling arithmetic scatters" is false for maps with a single absorbing state.

## Probe report (v0, 2026-07-20)
**1. Is the headline claim exactly true or only statistically likely?** Exactly true: G1/G2/G4 are exhaustive integer enumerations over the full finite domains (8991 and 891 inputs), so the "all converge / max 7 / unique 6174" statements are proven, not estimated.
**2. Is the input domain unambiguously defined?** Yes: integers 1000–9999 (resp. 100–999) with at least two distinct digits, the repdigits explicitly excluded; domain sizes 8991 and 891 are committed constants and reproduced by the verifier.
**3. Does the step map handle leading zeros and intermediate values correctly?** Yes: every value is zero-padded to the fixed width before sorting, so intermediates like 0999 are handled; the verifier's `zfill(width)` encodes this and the exhaustive gate would expose any mishandling as a non-convergence.
**4. Could other fixed points or cycles exist that the claim ignores?** No: G2 enumerates every fixed point in the valid domain and finds exactly [6174] (resp. [495]); since G1 shows zero non-convergences, there are no other terminal cycles.
**5. Is the ≥3σ gate a real check or a tautology given the exhaustive gate?** It is an independent seeded sampling cross-check: it draws 200000 numbers and tests the success rate against a concrete null (p0=0.99), rejecting "not all converge" at z ≈ 44.946657; it would flag any discrepancy between the sampler and the exhaustive claim.
**6. Is the result base/width dependent, and is that disclosed?** Yes and yes: the Model-basis section states the dependence on base 10 and width 4, and G4 demonstrates a different constant (495) at width 3.
**7. Is the grounding an external citation and is its caveat accurate to the pinned revision?** The grounding pins a specific Wikipedia revision (oldid 1364472561 + text sha1 9190b73…) of the article "Kaprekar's routine". That revision literally states both that 6174 is Kaprekar's constant / a fixed point AND that "any four-digit number (in base 10) with at least two distinct digits will reach 6174 within seven iterations" (citing Hanover 2017), plus that Prichett et al. 1981 limited the decadic Kaprekar constants to 495 (3-digit) and 6174 (4-digit). The page asserts the seven-iteration bound by citation; our verifier proves that exact ≤7-step bound (and the ≤6-step 3-digit bound) firsthand by exhaustive enumeration over the full domains rather than relying on the cited claim.
**8. Is the verifier deterministic and reproducible cross-invocation?** Yes: no wall-clock or OS randomness; the seeded draws use a fixed-constant LCG, and the double-run digest equality is asserted before exit 0, so a separate invocation reproduces the same results_sha256.

**Recommendation: sim-ready**
