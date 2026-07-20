# Uniform random hashing is lopsided — the busiest node owns H_n/n of the ring, a factor H_n ≈ ln n above its fair share 1/n

> **State:** sim-ready
> **Class:** counterintuitive-but-exactly-true · distributed systems / combinatorial probability (round-52 FLEET slot)
> **Target:** sim-lab (VERDICT 230, +13 offset)
> **Grounding:** https://en.wikipedia.org/w/index.php?title=Consistent_hashing&oldid=1362790808@04e4621d7d3ec6c945d65c66c583dde9eda80cef · fetched 2026-07-20
> **Verifier (firsthand):** stdlib-only, SEED=20260717; results-dict sha256 41394b56e4ebec3d14eb340fbfbd896db530d794fcea2ca495212948f74184ac

## The phenomenon (one line)
Drop n servers onto a hash ring by choosing n independent uniform points on a unit circle; the circle is cut into n arcs, and the EXPECTED largest arc — the load of the busiest node — equals H_n/n, where H_n = Σ_{j=1}^n 1/j ≈ ln n + γ. That is a factor H_n above the fair share 1/n, and it is exactly why consistent hashing needs virtual replicas.

## The folk belief
"Uniform random placement spreads load evenly, so with n nodes each owns about 1/n of the ring." The word *uniform* invites the reading *balanced*. But uniform placement of the boundaries is not uniform ownership of the arcs: the gaps between n random points are far from equal, and the biggest gap is systematically a logarithmic factor larger than 1/n. The naive "busiest owns 1/n" understates the real worst-case load by H_n ≈ ln n.

## The thesis (reasoned to fuller form — Q-0254 duty)
Placing n nodes uniformly is placing n independent uniform cut-points on the circle; the arc each node owns is the gap to the next clockwise cut-point. The n gaps are exchangeable and sum to 1, so the *mean* gap is 1/n — but the folk claim silently swaps the maximum for the mean. The maximum gap is a genuinely different, larger quantity: by inclusion–exclusion the expected largest of n uniform spacings is exactly Σ_{k=1}^n (-1)^(k+1) C(n,k)/k · (1/n), and that alternating sum telescopes to the harmonic number, giving E[max arc] = H_n/n. So the busiest node's expected load is H_n/n, an H_n ≈ ln n multiple of fair share. The imbalance is not a hash-function defect to be tuned away; it is intrinsic to uniform placement, and the standard fix — give each node r virtual replicas — replaces n by nr independent points, shrinking the expected max load to H_{nr}/(nr), which drives the imbalance factor H_{nr} down toward the fair 1/n only slowly (logarithmically), which is why production systems use hundreds of virtual nodes.

## The formal model (committed constants, exact)
- Circle = unit circumference [0,1); n nodes = n i.i.d. uniform points; the busiest node's load = the maximum of the n circular gaps (spacings), which sum to 1.
- Exact core identity (the survival/inclusion–exclusion form): A(n) = Σ_{k=1}^n (-1)^(k+1) · C(n,k) · Fraction(1, k·n), and the closed form B(n) = H_n/n with H_n = Σ_{j=1}^n Fraction(1,j). Claim: A(n) == B(n) exactly for every n.
- Discrete-ring analogue: m cells on a ring, n occupied uniformly at random; the normalized mean maximum circular gap E(m,n) = Fraction(Σ max-gap, C(m,n)·m) converges to H_n/n as m → ∞.
- All of G1/G2/G4's exact leg use `fractions.Fraction` — no floating point enters the identity or the invariance ratio; G3/G4's Monte-Carlo legs are seeded sampling cross-checks of the closed form.

## Pinned world (committed constants)
SEED=20260717 · all randomness from `random.Random(20260717)` · G1/G4 identity range n=2..12 · G2 discrete ring n=4 at m∈{8,12,16,20} · G3/G4 Monte-Carlo n∈{32,64}, T=200000 trials each · G4 shift circumference L=7.0.

## Pre-registered gates (sim-ready iff ALL hold, in order)
**G1 — Exact alternating identity (Fraction ==).** For n=2..12, A(n) = Σ_{k=1}^n (-1)^(k+1) C(n,k) Fraction(1,k·n) equals B(n) = H_n/n exactly (rational equality, no float). *Direction:* exact equality — pass iff `A(n) == B(n)` for every n.
**G2 — Exhaustive discrete-ring enumeration (Fraction), monotone convergence.** For n=4 enumerate all C(m,4) occupied-cell subsets at m=8,12,16,20, take the exact rational mean normalized max-gap E(m,4). *Direction:* monotone convergence — pass iff |E(m,4) − H_4/4| STRICTLY decreases as m grows AND the largest m (m=20) is within 0.03 of H_4/4 (= 25/48 ≈ 0.5208).
**G3 — Monte-Carlo confirmation (≥3σ).** For n=32 and n=64, T=200000 seeded trials of n uniform points; the sample mean max arc lands within 3·SE of the closed form H_n/n. *Direction:* within 3σ — pass iff `|mean − H_n/n| ≤ 3·SE` for both n.
**G4 — Invariance / shift.** (a) The exact ratio n·A(n)/H_n == 1 for every G1 n (Fraction). (b) Rerunning G3's Monte-Carlo on a circle of a DIFFERENT circumference (L=7.0) and normalizing by L reproduces H_n/n within 3σ. *Direction:* invariance holds — the result is independent of circumference and the exact ratio is identically one.
**G5 — Falsifiability (the gate must REJECT wrong models).** (a) The naive "busiest owns 1/n" is false: H_n/n ≠ 1/n exactly for n≥2, and the Monte-Carlo z of the naive value 1/n at n=32 is far beyond 3σ → the naive model is marked REJECTED. (b) A corrupted survival with the alternating sign dropped, A_wrong(n) = Σ_k C(n,k) Fraction(1,k·n), does NOT equal H_n/n → REJECTED. *Direction:* pass iff BOTH wrong models are rejected; the gate FAILS if either wrong model matches the truth.

## Pre-registered decision rule
sim-ready iff G1 ∧ G2 ∧ G3 ∧ G4 ∧ G5 all hold in their stated directions, AND both deliberately-wrong models (naive 1/n; dropped-sign survival) are REJECTED, AND the in-process double-run digest is stable.

## Dry-sim results
```json
{
  "g1_identity": {
    "10": {
      "A": "7381/25200",
      "B": "7381/25200",
      "H_n": "7381/2520",
      "equal": true,
      "ratio_nA_over_H": "1/1"
    },
    "11": {
      "A": "83711/304920",
      "B": "83711/304920",
      "H_n": "83711/27720",
      "equal": true,
      "ratio_nA_over_H": "1/1"
    },
    "12": {
      "A": "86021/332640",
      "B": "86021/332640",
      "H_n": "86021/27720",
      "equal": true,
      "ratio_nA_over_H": "1/1"
    },
    "2": {
      "A": "3/4",
      "B": "3/4",
      "H_n": "3/2",
      "equal": true,
      "ratio_nA_over_H": "1/1"
    },
    "3": {
      "A": "11/18",
      "B": "11/18",
      "H_n": "11/6",
      "equal": true,
      "ratio_nA_over_H": "1/1"
    },
    "4": {
      "A": "25/48",
      "B": "25/48",
      "H_n": "25/12",
      "equal": true,
      "ratio_nA_over_H": "1/1"
    },
    "5": {
      "A": "137/300",
      "B": "137/300",
      "H_n": "137/60",
      "equal": true,
      "ratio_nA_over_H": "1/1"
    },
    "6": {
      "A": "49/120",
      "B": "49/120",
      "H_n": "49/20",
      "equal": true,
      "ratio_nA_over_H": "1/1"
    },
    "7": {
      "A": "363/980",
      "B": "363/980",
      "H_n": "363/140",
      "equal": true,
      "ratio_nA_over_H": "1/1"
    },
    "8": {
      "A": "761/2240",
      "B": "761/2240",
      "H_n": "761/280",
      "equal": true,
      "ratio_nA_over_H": "1/1"
    },
    "9": {
      "A": "7129/22680",
      "B": "7129/22680",
      "H_n": "7129/2520",
      "equal": true,
      "ratio_nA_over_H": "1/1"
    }
  },
  "g2_enumeration": {
    "12": {
      "E": "311/660",
      "E_float": 0.471212121,
      "abs_err": 0.049621212
    },
    "16": {
      "E": "63/130",
      "E_float": 0.484615385,
      "abs_err": 0.036217949
    },
    "20": {
      "E": "9541/19380",
      "E_float": 0.492311662,
      "abs_err": 0.028521672
    },
    "8": {
      "E": "31/70",
      "E_float": 0.442857143,
      "abs_err": 0.07797619
    },
    "_largest_m_within_0p03": true,
    "_monotone_strict_decrease": true,
    "_target": "25/48",
    "_target_float": 0.520833333
  },
  "g3_montecarlo": {
    "32": {
      "mean": 0.12673757,
      "se": 7.1857191e-05,
      "target": 0.126827975,
      "within_3sigma": true,
      "z": -1.258124
    },
    "64": {
      "mean": 0.074105441,
      "se": 3.9228281e-05,
      "target": 0.074123295,
      "within_3sigma": true,
      "z": -0.45513
    }
  },
  "g4_invariance": {
    "exact_ratio_one_all_n": true,
    "shift": {
      "32": {
        "circumference": 7.0,
        "normalized_mean": 0.126895589,
        "target": 0.126827975,
        "within_3sigma": true,
        "z": 0.933517
      },
      "64": {
        "circumference": 7.0,
        "normalized_mean": 0.074116772,
        "target": 0.074123295,
        "within_3sigma": true,
        "z": -0.166919
      }
    }
  },
  "g5_falsifiability": {
    "both_wrong_models_rejected": true,
    "dropped_sign_REJECTED": true,
    "dropped_sign_survival_neq": true,
    "naive_1_over_n_neq_Hn_over_n": true,
    "naive_1_over_n_z_n32": 1322.80024,
    "naive_REJECTED": true
  },
  "gates": {
    "G1": true,
    "G2": true,
    "G3": true,
    "G4": true,
    "G5": true
  },
  "n_list": [
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12
  ],
  "proposal": 217,
  "seed": 20260717,
  "sim_ready": true
}
```
results_sha256=41394b56e4ebec3d14eb340fbfbd896db530d794fcea2ca495212948f74184ac

**Disclosed results-dict sha256 = `41394b56e4ebec3d14eb340fbfbd896db530d794fcea2ca495212948f74184ac`** — the busiest node's expected load is H_n/n (G1 exact identity holds for all n=2..12; G3 Monte-Carlo means 0.12674 (n=32) and 0.07411 (n=64) match H_n/n within z = −1.26 and −0.46; the naive 1/n model is rejected at z ≈ 1322.8).

## Verifier
`ideas/fleet/consistent-hashing-max-gap-harmonic.py` — stdlib only (`fractions`, `itertools`, `math`, `random`, `hashlib`, `json`, `sys`), SEED=20260717, all randomness from `random.Random(20260717)`; the results dict is built twice and both canonical dumps are asserted identical before exit.
```reproduce
python3 ideas/fleet/consistent-hashing-max-gap-harmonic.py
# prints the results JSON, then results_sha256=41394b56e4ebec3d14eb340fbfbd896db530d794fcea2ca495212948f74184ac, then determinism_double_run=True; exits 0
```

## Why it matters
It is a clean counterexample to "uniform placement means balanced load." A logarithmic worst-case imbalance is baked into any scheme that maps n nodes to n independent ring positions, so a single hash of each node is never enough for even load — the H_n ≈ ln n factor is why every production consistent-hashing system (Dynamo, Cassandra, Akamai) assigns each physical node many virtual replicas. The same max-of-spacings shape governs any "largest gap among random cut-points" question: shard-size skew, longest idle interval, widest coverage hole.

## Dedup
Grepped all lanes (`ideas/**`) at boot high-water P216: no consistent-hashing / max-arc / max-gap / H_n-imbalance card exists (`grep -rilE 'consistent.hashing|max.gap' ideas/` returned nothing; no slug collision on `consistent-hashing-max-gap-harmonic`). Distinct from the five nearest neighbours: **two-choices-routing-cliff** (the *fix* — power-of-two-choices load balancing — not the uniform-placement imbalance itself); **grid-quorum-sqrt-intersection** (√n quorum intersection, a set-cover geometry, not ring spacings); **birthday-collision-sqrt-n** (the √n *collision* threshold, a coincidence count, not a max-gap); **coupon-collector-tail** (n·H_n *time to cover all*, the harmonic number as a sum over coupons — a different H_n appearance, about completion time not max spacing); **littles-law-distribution-free** (L=λW queue identity, unrelated). This card's object is the maximum of n uniform circular spacings and its exact H_n/n closed form — no existing card computes it.

## Model basis (declared model-dependence — the P024 discipline)
The result is exact GIVEN the model: n i.i.d. uniform ring positions and load measured as the maximum circular spacing. It assumes independent uniform hashing (a good hash approximates this) and one ring position per node; correlated or non-uniform hashes, or weighted nodes, shift the constant. G1/G2/G4's exact legs carry no probabilistic assumption (Fraction identities and exhaustive enumeration); G3/G4's Monte-Carlo legs are seeded sampling cross-checks of the closed form, not the proof.

## One-line design fix
Give each physical node r virtual replicas: n nodes become nr independent ring points, shrinking the busiest node's expected max-replica load to H_{nr}/(nr) and the per-node imbalance toward the fair 1/n — the logarithmic H_{nr} factor is why r is set to hundreds in practice.

## Probe report (v0, 2026-07-20)
**1. Is the headline claim exactly true or only statistically likely?** Exactly true for the identity: G1 proves A(n) == H_n/n by rational `Fraction` equality for every n=2..12, and G4's ratio n·A/H_n == 1 exactly; the Monte-Carlo gates (G3) only cross-check the closed form by sampling, they do not establish it.
**2. Is the load model unambiguously defined?** Yes: the circle has unit circumference, n nodes are n i.i.d. uniform points, and a node's load is the maximum of the n circular spacings (gaps to the next clockwise point), which sum to 1 — so the mean gap is exactly 1/n and the object of study is the maximum, committed as a constant in the model section.
**3. Does the exact identity actually telescope to the harmonic number, or is that asserted?** It is computed, not asserted: G1 evaluates the alternating inclusion–exclusion sum A(n) and the harmonic closed form B(n)=H_n/n independently as `Fraction`s and asserts equality; G5(b) further shows that dropping the alternating sign breaks the identity, so the sign structure is load-bearing.
**4. Could the discrete-ring convergence be an artifact of the chosen m values?** No: G2 enumerates EVERY C(m,4) subset exactly (Fraction, no sampling) at four increasing m and requires the error |E−H_4/4| to strictly decrease AND the largest m to fall within 0.03 of the target; a non-converging gap definition would fail the monotonicity assertion rather than pass quietly.
**5. Is the ≥3σ gate a real check or a tautology given the exact identity?** It is an independent seeded sampling cross-check: G3 draws 200000 fresh configurations per n from `random.Random(20260717)` and tests the sample mean against the closed form (z = −1.26 at n=32, −0.46 at n=64, both within 3σ); it would flag any mismatch between the sampler and the H_n/n formula.
**6. Is the result invariant to circumference / does scale sneak in?** Yes and checked: G4 reruns the Monte-Carlo on a circle of circumference L=7.0, normalizes by L, and reproduces H_n/n within 3σ (z = 0.93, −0.17), while the exact ratio n·A/H_n == 1 holds identically — the H_n/n load is a pure fraction of whatever circumference is used.
**7. Is the grounding an external citation and is its caveat accurate to the pinned revision?** The grounding pins Wikipedia "Consistent hashing" oldid 1362790808 (raw-wikitext sha1 04e4621d…). That revision has a "Variance reduction" section that motivates *virtual nodes* to reduce load skew from non-uniform placement, and notes adding the nth server relocates a 1/n fraction of keys; its only "log" appearances are the O(log N) lookup cost of the binary search, NOT a load bound. The page does NOT state the E[max arc] = H_n/n identity or the H_n ≈ ln n imbalance factor — our verifier proves that firsthand; the caveat is accurate.
**8. Is the verifier deterministic and reproducible cross-invocation?** Yes: no wall-clock or OS entropy; all randomness comes from `random.Random(20260717)` consumed in a fixed order, the results dict is built twice and both canonical dumps asserted identical (determinism_double_run=True), and two separate invocations printed the byte-identical digest 41394b56e4ebec3d14eb340fbfbd896db530d794fcea2ca495212948f74184ac.

**Recommendation: sim-ready**
