"""PROPOSAL 189 verifier — poll-jitter inspection paradox.

Head: decorrelating health-check / telemetry poll intervals (holding the mean
poll rate fixed) inflates the mean time a randomly-timed fault waits for its
next poll, from T/2 (deterministic period) to (T/2)(1 + CV^2). This is the
renewal inspection paradox: a random observer's forward-recurrence (residual)
life has mean E[R] = E[X^2] / (2 E[X]).

Gates (pre-registered, >=3 sigma):
  G1 paradox       — exponential jittered polls: mean residual >> T/2, ~= T.
  G2 null contrast — deterministic polls: residual ~= T/2; exp-vs-det z_contrast large.
  G3 robustness    — hyperexponential (same mean) polls: residual matches E[X^2]/(2mu)=164.

DIGEST-POSTURE: WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY. The sha256 of the
compact canonical results dict IS the digest; stdout prints the pretty dump
(indent=2) and the digest line; no on-disk JSON.
"""
import bisect
import hashlib
import json
import math
import random

SEED = 20260717

# ---- pinned world ----
T = 100.0                # mean poll interval (all arms share this mean rate)
N_INTERVALS = 200000     # renewal intervals per arm
N_OBSERVERS = 500000     # uniform random fault arrival times
BAND = 0.01              # 1% relative tolerance
Z_MIN = 3.0              # sigma gate
H2_P = 0.5               # hyperexponential mixing weight
H2_M1 = 20.0             # component 1 mean
H2_M2 = 180.0            # component 2 mean


def _mean_std(xs):
    n = len(xs)
    m = math.fsum(xs) / n
    var = math.fsum((x - m) * (x - m) for x in xs) / n
    return m, math.sqrt(var)


def _residuals(intervals, rng):
    """Forward-recurrence times seen by uniform random observers over the timeline."""
    cum = []
    t = 0.0
    for x in intervals:
        t += x
        cum.append(t)
    horizon = cum[-1]
    out = []
    for _ in range(N_OBSERVERS):
        u = rng.uniform(0.0, horizon)
        idx = bisect.bisect_right(cum, u)
        out.append(cum[idx] - u)
    return out


def _deterministic(rng):
    return [T] * N_INTERVALS


def _exponential(rng):
    return [rng.expovariate(1.0 / T) for _ in range(N_INTERVALS)]


def _hyperexp(rng):
    out = []
    for _ in range(N_INTERVALS):
        if rng.random() < H2_P:
            out.append(rng.expovariate(1.0 / H2_M1))
        else:
            out.append(rng.expovariate(1.0 / H2_M2))
    return out


def run():
    rng = random.Random(SEED)
    r = lambda x: round(x, 6)
    half_T = T / 2.0

    h2_second_moment = H2_P * 2.0 * H2_M1 * H2_M1 + (1.0 - H2_P) * 2.0 * H2_M2 * H2_M2
    h2_mean = H2_P * H2_M1 + (1.0 - H2_P) * H2_M2
    theory_h2 = h2_second_moment / (2.0 * h2_mean)

    det = _residuals(_deterministic(rng), rng)
    exp = _residuals(_exponential(rng), rng)
    h2 = _residuals(_hyperexp(rng), rng)

    m_det, s_det = _mean_std(det)
    m_exp, s_exp = _mean_std(exp)
    m_h2, s_h2 = _mean_std(h2)
    se_det = s_det / math.sqrt(len(det))
    se_exp = s_exp / math.sqrt(len(exp))
    se_h2 = s_h2 / math.sqrt(len(h2))

    z1 = (m_exp - half_T) / se_exp
    rel_err_exp = abs(m_exp - T) / T
    ratio_exp = m_exp / half_T
    g1_pass = bool(z1 >= Z_MIN and rel_err_exp < BAND and m_exp > half_T)

    band_det = abs(m_det - half_T) / half_T
    z_contrast = (m_exp - m_det) / math.sqrt(se_exp * se_exp + se_det * se_det)
    g2_pass = bool(band_det < BAND and z_contrast >= Z_MIN)

    z3 = (m_h2 - half_T) / se_h2
    rel_err_h2 = abs(m_h2 - theory_h2) / theory_h2
    g3_pass = bool(rel_err_h2 < BAND and z3 >= Z_MIN)

    all_pass = bool(g1_pass and g2_pass and g3_pass)

    return {
        "world": {
            "seed": SEED,
            "T": r(T),
            "n_intervals": N_INTERVALS,
            "n_observers": N_OBSERVERS,
            "z_min": r(Z_MIN),
            "band": r(BAND),
        },
        "g1_paradox_exponential": {
            "mean_residual_sim": r(m_exp),
            "theory_residual": r(T),
            "det_baseline_half_T": r(half_T),
            "ratio_vs_half_T": r(ratio_exp),
            "rel_err_vs_theory": r(rel_err_exp),
            "z": r(z1),
            "pass": g1_pass,
        },
        "g2_null_deterministic_contrast": {
            "mean_residual_det": r(m_det),
            "expected_half_T": r(half_T),
            "band_rel": r(band_det),
            "z_contrast_exp_vs_det": r(z_contrast),
            "pass": g2_pass,
        },
        "g3_robustness_hyperexp_shift": {
            "mean_residual_sim": r(m_h2),
            "theory_residual": r(theory_h2),
            "rel_err": r(rel_err_h2),
            "z": r(z3),
            "pass": g3_pass,
        },
        "all_pass": all_pass,
    }


def main():
    r1 = run()
    r2 = run()
    assert r1 == r2, "in-process double-run mismatch: non-deterministic"
    payload = json.dumps(r1, sort_keys=True, separators=(",", ":"))
    digest = hashlib.sha256(payload.encode()).hexdigest()
    print(json.dumps(r1, indent=2, sort_keys=True))
    print(f"Results-JSON sha256: {digest}")
    raise SystemExit(0 if r1["all_pass"] else 1)


if __name__ == "__main__":
    main()
