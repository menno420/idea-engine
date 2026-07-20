# At a 1% base rate two independent 95%-accurate diligence screens flag a ~78%-good shortlist that even a 99%-accurate single screen cannot match, because independent positives MULTIPLY the odds — the k-th screen need only be about (odds-against)^(1/k) accurate, and the whole gain vanishes exactly when the screens are redundant

> **State:** sim-ready
> **Class:** venture (round-49 VENTURE slot)
> **Target:** sim-lab (VERDICT 219, +13 offset)
> 📊 Model: Claude Opus · high · idea/planning
> **Grounding:** https://en.wikipedia.org/w/index.php?title=Likelihood_ratios_in_diagnostic_testing&oldid=1363827685@bd86f75187e89db916dbd57fcbdcca2e9fd95d1a · fetched 2026-07-20
> **Reference (external, reachable):** [Likelihood ratios in diagnostic testing — Wikipedia](https://en.wikipedia.org/w/index.php?title=Likelihood_ratios_in_diagnostic_testing&oldid=1363827685) — "The pretest odds of a particular diagnosis, multiplied by the likelihood ratio, determines the post-test odds. This calculation is based on Bayes' theorem." Byte-pinned to the raw-wikitext sha1 of the cited revision.
> **Verifier (firsthand):** ideas/venture-lab/independent_screens_odds_ladder.py · results-dict sha256 b04322fa5698021f2a78679abd43cdc3c3a878cbd4c5692a2376d222833e98c6

## The phenomenon (one line)
At a 1% base rate, TWO independent 95%-accurate screens (a candidate passes only if BOTH flag) yield a posterior precision PPV_2 = 361/460 ≈ 0.7848 — a majority-good shortlist — while a SINGLE 95% screen yields only PPV_1 = 19/118 ≈ 0.161, and a single screen would need accuracy above 99% just to break even; the second independent positive does the work by MULTIPLYING the odds, not by being more accurate.

## Domain
Venture / diligence & underwriting — staged screening under a low base rate (probability / Bayesian inference applied to multi-signal decision funnels). The object is the COMPOSITION of several imperfect screens (how independent positives stack), deliberately distinct from what a single positive means. It governs any staged diligence funnel, multi-signal underwriting stack, fraud/KYC pipeline, or hiring loop.

## The folk belief
"A bad base rate can only be fixed by one very accurate test; stacking a couple of mediocre checks can't beat it." The instinct is that precision is a property of the single best instrument — to trust a positive at a 1% base rate you need a near-perfect (99%+) screen, and adding a second modest check is a rounding error. This is the multi-test cousin of base-rate neglect: it ignores that two *independent* positives multiply the likelihood ratio, so the pre-test odds are updated twice.

## The thesis (reasoned to its fuller form — Q-0254 duty)
Model a population where a fraction `p` of candidates are "good" (the base rate). There are `k` conditionally-independent symmetric screens; each has sensitivity = specificity = `a`, and a candidate "passes" only if ALL `k` screens flag it (the AND rule). The posterior precision after `k` positives is the Bayes ratio of true-positive mass to total-positive mass.

1. **The closed form.** `PPV_k = p·a^k / ( p·a^k + (1−p)(1−a)^k )` — true-positive mass `p·a^k` over itself plus false-positive mass `(1−p)(1−a)^k`. Each additional independent positive multiplies the good mass by `a` and the bad mass by `(1−a)`.
2. **The odds engine.** In odds form this is exactly `posterior_odds = prior_odds · (a/(1−a))^k`, with `prior_odds = p/(1−p)` and per-screen likelihood ratio `LR = a/(1−a)`. Independent positives *multiply* the odds — the update is a product, not a sum, which is why a second modest screen is not a rounding error.
3. **The k-th-root ladder.** Majority-good (`PPV_k > 1/2`) ⟺ `p·a^k > (1−p)(1−a)^k` ⟺ `(a/(1−a))^k > (1−p)/p`. So each of `k` screens need only clear `a/(1−a) > ((1−p)/p)^(1/k)` — the required per-screen accuracy is the **k-th ROOT** of the odds-against. At `p=1/100` the odds-against is 99: a single screen needs `a/(1−a) > 99` (i.e. `a > 99/100`), but `k=2` needs only `a/(1−a) > √99 ≈ 9.95` (clears near `a ≈ 0.91`) and `k=3` needs `a/(1−a) > 99^(1/3) ≈ 4.63` (clears near `a ≈ 0.83`). The minimal integer-percent clearing accuracies are 100 / 91 / 83 — strictly decreasing in `k`.
4. **Independence is load-bearing.** The gain is exactly as real as the screens' independence. If the second screen is a redundant copy of the first with probability ρ, the posterior after two positives strictly decreases in ρ and equals `PPV_1` exactly at ρ=1 — a fully redundant second screen adds nothing. The multiplication assumes conditional independence given the true state; correlation deflates the effective `k`.

Fuller form, one sentence: *whether a low-base-rate positive can be trusted is decided not by any single screen's accuracy but by the PRODUCT of independent likelihood ratios — so the k-th screen need only be about the k-th root of the odds-against, and the entire advantage evaporates precisely to the degree the screens are redundant.*

## The formal model / Pinned world (committed constants)
- SEED = 20260717 (proposal-owned; one `random.Random(SEED)`, consumed only by G3 in a fixed per-candidate order: good? → screen1 → screen2).
- Base rate `p = 1/100`; symmetric screen accuracy `a = 95/100`; `k ∈ {1, 2, 3}`; AND rule (pass iff all k flag).
- Closed anchors: `PPV_2 = 361/460 ≈ 0.7848`, `PPV_1 = 19/118 ≈ 0.161`.
- Ladder threshold: `(a/(1−a))^k > (1−p)/p` (majority-good), equivalently `p·a^k > (1−p)(1−a)^k` (polynomial, root-free) — the form the verifier uses to avoid irrational roots.
- Determinism discipline: exact values held as `fractions.Fraction`; all Monte-Carlo floats `round(x, 6)` BEFORE storing; results-dict sha256 is of the WHOLE compact-canonical dict and is NOT a field of it (WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY posture).

## Pre-registered gates
- **G1 — EXACTLY-TRUE (direct == odds-form == exhaustive enumeration).** Over a grid of rational `(p, a, k)`: (a) `PPV_k` direct formula; (b) odds-form `odds = (p/(1−p))·(a/(1−a))^k`, `PPV = odds/(1+odds)`; (c) exhaustive integer-population enumeration with `N = den(p)·den(a)^k` so all counts are integers (`good_pass = num_p·num_a^k`, `bad_pass = (den_p−num_p)(den_a−num_a)^k`, `PPV_enum = good_pass/(good_pass+bad_pass)`). All three EXACTLY equal per cell, Fraction-exact. *Direction:* exact three-way equality in 100% of cells (mismatches == 0).
- **G2 — EXACT k-th-root ladder threshold.** Over a grid of `(p, a, k)`: the boolean `[p·a^k > (1−p)(1−a)^k]` EQUALS `[PPV_k > 1/2]` in 100% of cells (exact Fraction comparison, no irrational roots). AND, for `p = 1/100`, an exact Fraction search over `a ∈ {1/100,…,100/100}` finds the minimal integer-percent accuracy clearing majority-good for `k = 1, 2, 3` (= 100, 91, 83) and asserts it is strictly DECREASING in `k`. *Direction:* exact boolean match in 100% of cells AND clearing-accuracy strictly decreasing in `k` (violations == 0).
- **G3 — ≥3σ vs folk belief (Monte Carlo, M=400000).** Folk belief: "a bad base rate can only be fixed by one very accurate test; stacking mediocre checks can't beat it." Headline scenario `p=1/100`, TWO independent `a=95/100` screens, AND rule. Simulate M candidates off the seeded RNG (good w.p. `p`; each screen flags a good w.p. `a`, a bad w.p. `1−a`, independently); form the empirical PPV among all-pass candidates; `SE = √(PPV_emp(1−PPV_emp)/passed_total)`. Gate: `(PPV_emp − 1/2)/SE ≥ 3` AND `|PPV_emp − 361/460| ≤ 3·SE`; the single-screen `PPV_1 = 19/118 ≈ 0.161` (minority) is recorded for contrast. *Direction:* the two-independent-screen empirical precision exceeds 1/2 by ≥3σ, while one screen of the same accuracy is far minority.
- **G4 — ROBUSTNESS / correlation-shift (independence is load-bearing).** Two shifts, both must hold. (a) **Correlation nullification:** two screens where with probability ρ screen-2 is a perfect COPY of screen-1's verdict (redundant), else independent; the closed form `PPV_2(ρ)` must satisfy, Fraction-exact, `PPV_2(ρ=1) == PPV_1` (a redundant second screen adds nothing) AND `PPV_2(ρ)` strictly DECREASING over ρ ∈ {0, 1/4, 1/2, 3/4, 1}. (b) **Odds-multiplication identity under asymmetric screens + base-rate shift:** over a grid with sens≠spec and varying `p`, `posterior_odds == prior_odds·∏ LR_i` (`LR_i = sens_i/(1−spec_i)`) EXACTLY (Fraction), AND over a decreasing sequence of `p` (fixed symmetric `a`) the minimal `k` to reach majority-good is NON-decreasing. *Direction:* redundancy exactly nullifies the second screen and PPV strictly decreasing in correlation; the odds-multiplication identity is exact in 100% of cells and k-needed is monotone in `p` (violations == 0).

## Pre-registered decision rule
`sim-ready` iff G1 ∧ G2 ∧ G3 ∧ G4 all pass on a deterministic double-run (an in-process rerun and a separate cross-invocation reproduce the identical results-dict sha256). Any gate fail ⇒ `needs-more-grooming`.

## Dry-sim results (SEED=20260717, verbatim from independent_screens_odds_ladder.py)
```
{
  "G1_exactly_true": {
    "cells_total": 27,
    "direction": "direct == odds-form == exhaustive-enumeration exact in 100% of cells (mismatches==0)",
    "mismatches": 0,
    "ok": true
  },
  "G2_kth_root_ladder": {
    "boolean_violations": 0,
    "cells_total": 36,
    "clearing_accuracy_percent_k1_k2_k3": [
      100,
      91,
      83
    ],
    "clearing_strictly_decreasing_in_k": true,
    "direction": "exact boolean [poly>] == [PPV>1/2] in 100% of cells AND clearing accuracy strictly decreasing in k (violations==0)",
    "ok": true
  },
  "G3_three_sigma_vs_folk": {
    "M": 400000,
    "PPV_1_single_screen_contrast": 0.161017,
    "PPV_2_closed": 0.784783,
    "PPV_emp": 0.789277,
    "SE": 0.006045,
    "direction": "two-independent-screen empirical PPV exceeds 1/2 by >=3 sigma (z_majority>=3) while one screen of the same accuracy is far minority (PPV_1~0.161)",
    "emp_within_3se_of_closed": true,
    "good_pass": 3592,
    "ok": true,
    "passed_total": 4551,
    "z_majority": 47.851639
  },
  "G4_correlation_robustness": {
    "correlation_nullification": {
      "ppv_at_rho1_equals_ppv1": true,
      "ppv_by_rho": [
        "361/460",
        "133/340",
        "247/940",
        "1501/7540",
        "19/118"
      ],
      "ppv_by_rho_float": [
        0.784783,
        0.391176,
        0.262766,
        0.199072,
        0.161017
      ],
      "ppv_strictly_decreasing_in_rho": true,
      "rho_grid": [
        "0",
        "1/4",
        "1/2",
        "3/4",
        "1"
      ],
      "violations": 0
    },
    "direction": "redundancy exactly nullifies the second screen (PPV(rho=1)==PPV_1) and PPV strictly decreasing in correlation; odds = prior * prod(LR_i) exact in 100% of cells and k-needed monotone in p (violations==0)",
    "odds_multiplication_identity": {
      "cells_total": 12,
      "k_needed_nondecreasing": true,
      "k_needed_over_decreasing_p": [
        1,
        1,
        2,
        3
      ],
      "mismatches": 0,
      "violations": 0
    },
    "ok": true
  },
  "decision": "sim-ready",
  "gates": {
    "G1": true,
    "G2": true,
    "G3": true,
    "G4": true
  },
  "head": "independent positives MULTIPLY the odds: k conditionally-independent symmetric screens (AND rule) compose by likelihood-ratio product; the k-th screen need only clear (odds-against)^(1/k); two 95% screens beat one 99% at 1% base rate; the gain vanishes when screens are redundant",
  "pinned_world": {
    "PPV_1": "19/118",
    "PPV_2": "361/460",
    "a_accuracy": "95/100",
    "k_grid": [
      1,
      2,
      3
    ],
    "ladder_threshold": "(a/(1-a))^k > (1-p)/p",
    "p_base_rate": "1/100"
  },
  "seed": 20260717
}

in_process_double_run: IDENTICAL
results_sha256: b04322fa5698021f2a78679abd43cdc3c3a878cbd4c5692a2376d222833e98c6
decision: sim-ready
```
results-dict sha256: `b04322fa5698021f2a78679abd43cdc3c3a878cbd4c5692a2376d222833e98c6`

## Honest nuance (disclosed)
- **The multiplication assumes CONDITIONAL INDEPENDENCE given the true state.** Real diligence signals are correlated (shared data rooms, overlapping reference networks, common founder narratives, the same third-party report re-cited), so the effective `k` is smaller than the count of screens — G4(a) prices exactly this: at correlation ρ the two-screen posterior slides from 361/460 (ρ=0) down to `PPV_1 = 19/118` (ρ=1). Treat `k` as *independent bits of evidence*, not *number of steps in the funnel*.
- **The k-th-root ladder is exact only for SYMMETRIC screens** (sensitivity = specificity = `a`). For asymmetric screens the exact object is the general odds-multiplication identity `posterior_odds = prior_odds·∏ sens_i/(1−spec_i)` (G4(b)); the clean "(odds-against)^(1/k)" statement is the symmetric special case.
- **The AND rule is a choice.** Requiring ALL k screens to flag (a confirmatory funnel) is the modeled rule; the dual any-flag / OR rule (a broad net that catches if ANY screen fires) gives the mirror-image arithmetic and a different operating point — named, not modeled here.
- **Grounding caveat.** The cited Wikipedia article STATES `post-test odds = pre-test odds × likelihood ratio` (and the successive-test multiplication is its direct iterate); it does NOT prove our specific k-th-root ladder or the correlation-nullification — those the verifier proves from first principles (G2, G4).

## Dedup
Grep across the tree (`grep -rn --exclude=bootstrap.py --exclude-dir=.substrate`) for "likelihood ratio", "odds form", "post-test odds", "independent test/screen", "two-stage"/"two stage", "confirmatory", "sequential screen/test", "multiply the odds", "diligence funnel", "naive bayes", "combine tests" returns NO proposal shipping the multi-test odds-composition invariant (k-th-root ladder / correlation-nullification).

- **Nearest adjacency — P136 → V149 base-rate-ppv-collapse** (`ideas/fleet/base-rate-ppv-collapse-2026-07-18.md`): the SINGLE-test knife-edge — a positive updates the prior prevalence to `PPV = (sens·prev)/(sens·prev+(1−spec)(1−prev))`, with the symmetric-`q` knife-edge at `prev* = 1−q`. DISTINCT: P136 prices what ONE positive means; this proposal is the MULTI-test COMPOSITION — how k independent positives multiply the odds (the k-th-root ladder) and how that gain nullifies under redundancy. P136's own card and V149 both explicitly name "the MULTI-test posterior: two independent positives multiply the likelihood ratio LR=sens/(1−spec) again" as the distinct next verifier object *held out of scope* — this proposal builds exactly that. No shared metric object (single PPV vs the k-composition/ladder/correlation surface).
- Also disclosed: **P126 double-marginalization** (a "two-stage" object, but successive-markup channel pricing — different domain, different math); **P072 pooled-screening-prevalence-wall** (Dorfman two-stage pooled testing with PERFECT tests — test-COUNT economics, not the posterior of imperfect screens); the **cascade independence quota** (likelihood ratios inside a herding DP, not diagnostic-screen composition). None ships this invariant.

## Reproduce
```
python3 ideas/venture-lab/independent_screens_odds_ladder.py
```
Deterministic: SEED=20260717, stdlib-only. Prints the results dict and its sha256; the same 64-hex digest `b04322fa…98c6` appears here, in the session card, and in control/outbox.md's P206 block. An in-process double-run (compute() ×2, canonical strings asserted equal) plus a separate cross-invocation reproduce the identical digest byte-for-byte.

## Verifier
`ideas/venture-lab/independent_screens_odds_ladder.py` — stdlib-only (`json`, `hashlib`, `math`, `random`, `fractions`). Implements the exact PPV closed forms (direct / odds-form / integer-population enumeration), the root-free majority test, the k-th-root ladder search, the seeded two-proportion Monte-Carlo scenario, and the correlation-shift + asymmetric odds-multiplication closed forms; asserts an in-process double-run reproduces the identical results-dict before emitting the digest.

## Why it matters
"Buy the one best signal" is the underwriting reflex — perfect a single screen and trust its positives. The k-th-root ladder is the sharper design rule: at a punishing base rate, adding one *genuinely independent* modest check beats grinding a single screen toward perfection, because independent positives multiply the odds and the per-screen bar you must clear is only the k-th root of the odds-against. This is the quantified backbone of staged diligence funnels (screen broadly, then require independent confirmations), multi-signal underwriting and credit stacks, fraud / KYC pipelines (independent identity, device, and behavioral checks), and hiring loops (independent interviewers beat one long panel). The load-bearing caveat is equally actionable: the whole gain is exactly as real as the independence — correlated checks (shared data rooms, reference networks, the same underlying report) collapse the ladder, so audit your signals for redundancy before you count them as separate evidence.

## Model basis (declared model-dependence)
The result depends only on Bayes' rule under conditional independence given the true state, symmetric screens (sens = spec = `a`) for the clean k-th-root statement, and the AND (require-all) combination rule. G1, G2, and G4 are model-free exact identities (they hold for every rational `p, a, k` in the grids); the G3 rates are specific to the seeded uniform Monte-Carlo model and the pinned scenario `p=1/100, a=95/100, k=2, M=400000`. Relaxing independence (G4(a)) or symmetry (G4(b)) is priced inside the verifier, not left to assertion; the AND-rule choice and the OR-rule dual are the declared modeling boundary.

## Probe report (v0, 2026-07-20)
**1. What is the precise claim, and which parts are exact vs statistical?**

`PPV_2 = 361/460 ≈ 0.7848` for two independent 95% screens vs `PPV_1 = 19/118 ≈ 0.161` for one, and the k-th-root ladder (per-screen bar `(odds-against)^(1/k)`, clearing accuracies 100/91/83 strictly decreasing) are EXACT Fraction identities (G1, G2, corroborated by exhaustive integer enumeration); the two-screen empirical PPV clearing ½ by ≥3σ (G3, z_majority ≈ 47.85) is statistical but overwhelming; G4 (correlation-nullification, odds-multiplication identity) is again exact.

**2. Is it counterintuitive in a defensible way?**

Yes — the folk belief that a bad base rate needs one very accurate test (and that stacking mediocre checks can't beat it) is false: two independent 95% screens beat a single 99% screen at 1% base rate because independent positives multiply the odds, so the per-screen accuracy bar is the k-th ROOT of the odds-against, not the whole of it.

**3. Is the model clean and pinned?**

Yes — SEED=20260717, `p=1/100`, `a=95/100`, `k∈{1,2,3}`, AND rule, closed anchors PPV_2=361/460 and PPV_1=19/118, ladder threshold `(a/(1−a))^k>(1−p)/p`; exact values held as `fractions.Fraction`, all Monte-Carlo floats `round(x,6)` before storing, one seeded RNG consumed in a fixed documented order.

**4. Is it deterministic (in-process double-run + cross-invocation)?**

Yes — `compute()` runs twice with canonical strings asserted equal ("in_process_double_run: IDENTICAL"), and a separate cross-invocation reproduces the identical 64-hex digest `b04322fa…98c6` byte-for-byte; stdlib-only (`json/hashlib/math/random/fractions`).

**5. Are the gates feasible and in-direction?**

Yes — all four pass on the true mechanism (constants were probe-printed BEFORE pre-registration): G1 27 cells 0 mismatches; G2 36 cells 0 boolean violations + clearing 100/91/83 strictly decreasing; G3 z_majority≈47.851639 with PPV_emp 0.789277 within 3·SE of closed 0.784783; G4 correlation strictly decreasing to PPV_1 at ρ=1 (0 violations) + odds-multiplication identity 12 cells 0 mismatches with k_needed 1,1,2,3 non-decreasing.

**6. Is the grounding real and on-point?**

Yes — Wikipedia "Likelihood ratios in diagnostic testing" (byte-pinned raw-wikitext sha1 bd86f75187e89db916dbd57fcbdcca2e9fd95d1a, revision 1363827685) states firsthand "The pretest odds … multiplied by the likelihood ratio, determines the post-test odds. This calculation is based on Bayes' theorem"; caveat: it establishes the odds×LR engine (successive multiplication is its direct iterate), NOT our specific k-th-root ladder or the correlation-nullification, which the verifier proves from first principles.

**7. What is the dedup status vs P136?**

Clear on the composition invariant — the nearest adjacency is P136 → V149 base-rate-ppv-collapse (single-test PPV knife-edge `a*=1−p`), which is DISTINCT: this is the multi-test odds-composition (k-th-root ladder + correlation-nullification) that P136 explicitly LEFT UN-BUILT and named as its next verifier object; P126 (two-stage channel pricing) and P072 (perfect-test pooled screening) are disclosed non-overlaps.

**8. Are the honest caveats disclosed (independence assumption)?**

Yes — the multiplication assumes conditional independence given the true state (real diligence signals are correlated, so effective `k` is smaller — priced by G4(a)); the k-th-root ladder is exact only for symmetric screens (asymmetric case is the general odds-multiplication identity, G4(b)); and the AND rule is a modeling choice whose OR-rule dual is named, not modeled.

**Recommendation: sim-ready**
