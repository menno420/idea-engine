#!/usr/bin/env python3
"""
benford_multiplicative_growth.py -- reference verifier for PROPOSAL 124 (round-28,
UNRELATED slot closer). Domain: number theory / statistics -- the leading-digit
law (Benford's law) EMERGING from multiplicative growth. Fleet-external
pure-mechanism head.

The "random growth spreads the leading digit evenly" trap. Intuition says that if
a quantity grows by random factors for a long time, its first significant digit
should land uniformly on 1..9 (each digit ~1/9 = 11.1%). It does NOT. A quantity
under MULTIPLICATIVE growth has log10(x) doing a random walk, so after enough
steps the FRACTIONAL part of log10(x) equidistributes on [0,1) -- the mantissa is
log-uniform -- and the leading digit d follows BENFORD'S LAW:

    P(d) = log10(1 + 1/d)   (d = 1..9)

so digit 1 leads ~30.1% of the time and digit 9 under 4.6% -- NOT 11.1%. The
counterintuitive core: the smallest digit is ~6.6x more likely than the largest,
purely from the growth being multiplicative.

Two facts the "uniform digits" instinct misses:
 (1) it is caused by MULTIPLICATIVITY, not by "randomness" -- the SAME random
     shocks ADDED instead of MULTIPLIED do NOT give Benford: an additive sum of
     positive shocks concentrates by the CLT (CV shrinks like 1/sqrt(n)) around a
     single magnitude, so its leading digit spikes on one value and is FAR from
     Benford;
 (2) it EMERGES with mixing -- the Benford fit improves as the number of
     multiplicative steps grows (more log-decades => better equidistribution of
     the mantissa), so few-step growth is measurably farther from Benford than
     many-step growth.

Gates (all on the /se margin, the P104..P122 convention -- z on an estimated
statistic via its standard error se = std / sqrt(TRIALS)):
  G1 existence (headline): the digit-1 frequency under many-step multiplicative
     growth EXCEEDS the uniform-null 1/9 by >= 3 sigma -- the leading digit is
     Benford-heavy (~30%), not uniform (~11%).
  G2 dose-response (emergence): the total-variation distance to Benford SHRINKS
     from few-step to many-step multiplicative growth by >= 3 sigma (paired common
     random numbers -- the SAME trajectories measured at an early and a late
     checkpoint) -- the Benford fit improves with multiplicative mixing.
  G3 specificity (multiplicativity, not randomness): the TV-to-Benford under the
     ADDITIVE process (same shocks, summed) EXCEEDS the TV-to-Benford under the
     MULTIPLICATIVE process by >= 3 sigma -- additive growth is NOT Benford; the
     effect is specific to multiplication.

Plus a closed-form ANCHOR cross-check (reported, not a gate): the many-step
multiplicative leading-digit frequencies reproduce the exact Benford law
P(d)=log10(1+1/d) -- max abs error over d=1..9 is disclosed.

stdlib only; fully deterministic under SEED.
"""
import random
import math
import json
import hashlib

SEED = 20260717        # proposal-owned pinned seed; SEEDLESS discipline
POP = 5000             # independent growth trajectories per replication (the per-trial batch)
TRIALS = 200           # independent replications (the /se convention averages over these)
STEPS_MANY = 100       # multiplicative steps for the converged (many-step) measurement
STEPS_FEW = 2          # multiplicative steps for the early (few-step, under-mixed) checkpoint
LOG_MU = 0.0           # per-step natural-log drift of the growth factor (drift-free)
LOG_SIGMA = 0.5        # per-step natural-log volatility of the growth factor
START = 1.0            # starting value for every trajectory (both processes)
SIGMA_GATE = 3.0       # pre-registered gate threshold (sigma)

DIGITS = (1, 2, 3, 4, 5, 6, 7, 8, 9)
UNIFORM_NULL = 1.0 / 9.0                                   # naive "even digits" expectation
BENFORD = {d: math.log10(1.0 + 1.0 / d) for d in DIGITS}   # exact leading-digit law


def leading_digit(v):
    """First significant (base-10) digit of a positive value v, in 1..9."""
    f = math.log10(v)
    d = int(10 ** (f - math.floor(f)))
    if d < 1:
        d = 1
    elif d > 9:
        d = 9
    return d


def digit_freqs(values):
    """Empirical leading-digit frequency vector over a batch of positive values."""
    counts = {d: 0 for d in DIGITS}
    for v in values:
        counts[leading_digit(v)] += 1
    n = len(values)
    return {d: counts[d] / n for d in DIGITS}


def tv_to_benford(freqs):
    """Total-variation distance between an empirical digit distribution and Benford."""
    return 0.5 * sum(abs(freqs[d] - BENFORD[d]) for d in DIGITS)


def run_trial(rng):
    """One replication over POP trajectories with paired common random numbers.

    Each trajectory draws STEPS_MANY iid lognormal shocks exp(N(LOG_MU,LOG_SIGMA)).
    The SAME shocks drive three measurements:
      - multiplicative value at STEPS_FEW  (early checkpoint, product of first FEW),
      - multiplicative value at STEPS_MANY (late checkpoint, product of all),
      - additive value at STEPS_MANY       (START + sum of all shocks).
    Returns the batch digit-1 frequency (mult, many), and the batch TV-to-Benford
    for {mult-few, mult-many, add-many}."""
    mult_few, mult_many, add_many = [], [], []
    for _ in range(POP):
        log_sum_few = 0.0
        log_sum_all = 0.0
        add_sum = 0.0
        for step in range(STEPS_MANY):
            g = rng.gauss(LOG_MU, LOG_SIGMA)     # natural-log growth increment
            shock = math.exp(g)                  # lognormal multiplicative factor
            log_sum_all += g
            add_sum += shock
            if step < STEPS_FEW:
                log_sum_few += g
        mult_few.append(START * math.exp(log_sum_few))
        mult_many.append(START * math.exp(log_sum_all))
        add_many.append(START + add_sum)
    f_few = digit_freqs(mult_few)
    f_many = digit_freqs(mult_many)
    f_add = digit_freqs(add_many)
    return (f_many[1],
            tv_to_benford(f_few),
            tv_to_benford(f_many),
            tv_to_benford(f_add),
            f_many)


def mean_se(xs):
    """Sample mean and standard error of the mean (se = std / sqrt(n))."""
    n = len(xs)
    m = sum(xs) / n
    var = sum((x - m) ** 2 for x in xs) / n
    se = math.sqrt(var / n)
    return m, se


def main():
    rng = random.Random(SEED)

    f1_many, tv_few, tv_many, tv_add = [], [], [], []
    freq_accum = {d: 0.0 for d in DIGITS}     # for the closed-form anchor cross-check
    for _ in range(TRIALS):
        a, b, c, d, fm = run_trial(rng)
        f1_many.append(a)
        tv_few.append(b)
        tv_many.append(c)
        tv_add.append(d)
        for dig in DIGITS:
            freq_accum[dig] += fm[dig]

    # Anchor cross-check: mean multiplicative many-step digit distribution vs Benford.
    mean_freq = {dig: freq_accum[dig] / TRIALS for dig in DIGITS}
    anchor_max_abs_err = max(abs(mean_freq[dig] - BENFORD[dig]) for dig in DIGITS)

    mean_f1, se_f1 = mean_se(f1_many)
    mean_tv_few, se_tv_few = mean_se(tv_few)
    mean_tv_many, se_tv_many = mean_se(tv_many)
    mean_tv_add, se_tv_add = mean_se(tv_add)

    # G1 existence: digit-1 frequency exceeds the uniform null 1/9 by >= 3 sigma.
    g1_excess = mean_f1 - UNIFORM_NULL
    z_g1 = g1_excess / se_f1 if se_f1 > 0 else float("inf")
    g1 = z_g1 >= SIGMA_GATE

    # G2 dose-response: TV-to-Benford shrinks from few-step to many-step (paired CRN).
    #   metric per trial = tv_few - tv_many; se via paired difference.
    dose = [b - c for b, c in zip(tv_few, tv_many)]
    mean_dose, se_dose = mean_se(dose)
    z_g2 = mean_dose / se_dose if se_dose > 0 else float("inf")
    g2 = z_g2 >= SIGMA_GATE

    # G3 specificity: additive TV-to-Benford exceeds multiplicative TV by >= 3 sigma
    #   (paired CRN: same trajectories' shocks summed vs multiplied).
    spec = [d - c for d, c in zip(tv_add, tv_many)]
    mean_spec, se_spec = mean_se(spec)
    z_g3 = mean_spec / se_spec if se_spec > 0 else float("inf")
    g3 = z_g3 >= SIGMA_GATE

    all_pass = g1 and g2 and g3

    results = {
        "params": {"SEED": SEED, "POP": POP, "TRIALS": TRIALS,
                   "STEPS_MANY": STEPS_MANY, "STEPS_FEW": STEPS_FEW,
                   "LOG_MU": LOG_MU, "LOG_SIGMA": LOG_SIGMA, "START": START,
                   "SIGMA_GATE": SIGMA_GATE},
        "benford_law": {str(d): round(BENFORD[d], 6) for d in DIGITS},
        "uniform_null": round(UNIFORM_NULL, 6),
        "anchor": {
            "mean_mult_many_freqs": {str(d): round(mean_freq[d], 6) for d in DIGITS},
            "max_abs_err_vs_benford": round(anchor_max_abs_err, 6),
        },
        "sim": {
            "mean_digit1_freq_mult_many": round(mean_f1, 6), "se_digit1_freq": round(se_f1, 6),
            "digit1_excess_over_uniform": round(g1_excess, 6),
            "mean_tv_mult_few": round(mean_tv_few, 6), "se_tv_mult_few": round(se_tv_few, 6),
            "mean_tv_mult_many": round(mean_tv_many, 6), "se_tv_mult_many": round(se_tv_many, 6),
            "mean_tv_add_many": round(mean_tv_add, 6), "se_tv_add_many": round(se_tv_add, 6),
            "mean_dose_few_minus_many": round(mean_dose, 6), "se_dose": round(se_dose, 6),
            "mean_spec_add_minus_mult": round(mean_spec, 6), "se_spec": round(se_spec, 6),
        },
        "gates": {
            "G1_benford_heavy_not_uniform": {"z": round(z_g1, 4), "pass": g1},
            "G2_emergence_with_steps": {"z": round(z_g2, 4), "pass": g2},
            "G3_specific_to_multiplicativity": {"z": round(z_g3, 4), "pass": g3},
        },
        "all_pass": all_pass,
    }
    canonical = json.dumps(results, sort_keys=True, separators=(",", ":"))
    digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    results["results_sha256"] = digest

    with open("benford_multiplicative_growth_results.json", "w") as fh:
        json.dump(results, fh, indent=2, sort_keys=True)

    print(json.dumps(results, indent=2, sort_keys=True))
    print("Results-JSON sha256:", digest)
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
