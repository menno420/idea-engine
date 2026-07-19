# PROPOSAL 181 — more hash functions make Bloom-filter false positives worse: past the optimum k* = (m/n)·ln2 each extra hash raises the false-positive rate, and no choice of k beats the bits-per-element floor ≈ 0.6185^(m/n)

> **State:** sim-ready
> **Class:** FLEET-OPS — membership filters / caching / dedup (round-43 FLEET slot)
> **Anchor:** the Bloom-filter optimal-k result — FPR = (1 − e^{−kn/m})^k, minimized at k = (m/n)·ln2 (Bloom 1970)
> **Target:** sim-lab VERDICT 194 (+13)
> **Grounding:** https://en.wikipedia.org/wiki/Bloom_filter@15d7f16cabd1b2e9f33543aa383f4aee8a81896b · fetched 2026-07-19T19:05:56Z
> **Reference (external, reachable):** https://en.wikipedia.org/wiki/Bloom_filter — Bloom, "Space/Time Trade-offs in Hash Coding with Allowable Errors" (CACM 1970); Kirsch & Mitzenmacher, "Less Hashing, Same Performance" (2006). Grounding pin = sha256 of the retrieved page, first 40 hex.
> **Verifier (firsthand):** `ideas/fleet/bloom-optimal-k-fpr-floor-2026-07-19.py` — stdlib-only, SEED=20260717, deterministic in-process + cross-invocation double-run; results-dict sha256 3fdfc867123a80a1476d414610413060c24b3580841f1d808dac10a75f8b5d7f
> 📊 Model: Claude Opus · high · idea/planning

## Domain
Probabilistic membership filters: a Bloom filter packs n inserted keys into an m-bit array using k hash functions per key; a lookup that finds all k bits set reports "present," and may be wrong (a false positive) for a key never inserted. Bloom filters are everywhere in fleet infrastructure — cache-admission (keeping one-hit-wonders out of a cache), dedup, LSM/SSTable read-avoidance, routing/membership tables, DHT placement.

## The folk belief
More hash functions means more independent checks, so a false positive must clear a higher bar — therefore more hashes should mean monotonically fewer false positives. Tune k up when you want fewer false hits.

## The thesis (reasoned to its fuller form — Q-0254 duty)
False-positive rate is not monotone in k — it is U-shaped, FPR(k) = (1 − e^{−kn/m})^k, minimized at k* = (m/n)·ln2. Each extra hash cuts both ways: it adds one more bit a false positive must clear (good), but it also sets one more bit per inserted key, filling the array faster (bad). Below k* the checking win dominates; above k* the fill cost dominates and FPR climbs back up. Worse for the "just tune k" instinct: the achievable minimum is floored at φ = (½)^{(m/n)·ln2} ≈ 0.6185^{(m/n)}, a function of bits-per-element ALONE. No value of k crosses that floor; the only lever that lowers it is more memory per element. Operationally: size the filter by bits-per-element for the FPR you need, set k = round((m/n)·ln2), and stop — adding hashes past k* spends CPU to make false positives worse.

## The trap
A team seeing false positives raises k ("more checks = safer"). Past k* this increases the false-positive rate, adds a hash computation to every insert and lookup, and burns the CPU budget — a strict lose-lose. The lever they needed was bits-per-element (m/n), not k.

## Formal model (committed constants)
n = 1500 keys inserted into an m-bit filter; Q = 1500 never-inserted keys queried; R = 150 independent trials per (config, k) with explicit per-(config,trial) seeds (SEED + config·1000003 + trial·7919). Hash indices by Kirsch–Mitzenmacher double hashing: for key x, two 64-bit words g1,g2 from sha256(salt:x), bit i = (g1 + i·g2) mod m (g2 forced odd). Metric: false-positive fraction over the Q absent queries, its mean and standard error over R trials. Base config: bits-per-element c = m/n = 8 (m = 12000), k ∈ {1, k*=6, 2k*=12}. Robustness config: c = 12 (m = 18000), k ∈ {1, k*=8, 2k*=16}. Predicted floor φ(c) = (½)^{c·ln2}.

## Pre-registered gates (ordered, ≥3σ; each tests the head)
| Gate | Claim | Statistic | Pass rule |
|------|-------|-----------|-----------|
| G1 | both ends of the k-sweep beat the optimum | z of (FPR[k=1] − FPR[k*]) and z of (FPR[2k*] − FPR[k*]) at c=8 | both gaps > 0 and both z ≥ 3 |
| G2 | more hashes hurt (the head) + memory floor | penalty = FPR[2k*] − FPR[k*]; z(penalty); floor match |FPR[k*] − φ| ≤ 0.20·φ and no tested k beats φ by >20% | penalty > 0, z ≥ 3, floor match holds |
| G3 | robustness under shifted bits-per-element (c=12) | G1 + penalty statistics recomputed at c=12 | dominance z ≥ 3 both ends, penalty > 0 z ≥ 3, floor match holds |

## Pre-registered decision rule
sim-ready ⇔ G1 ∧ G2 ∧ G3 all pass (all_pass=true) on two cross-invocation-identical runs of the committed verifier at SEED=20260717.

## Dry-sim results (SEED=20260717, verbatim from the committed verifier)
```
{
  "all_pass": true,
  "base_config_c8": {
    "bits_per_elem": 8,
    "dom_pass": true,
    "floor_pass": true,
    "floor_phi": 0.021416,
    "fpr_high": 0.04928,
    "fpr_low": 0.117938,
    "fpr_opt": 0.022213,
    "fpr_opt_predicted": 0.021577,
    "k_high": 12,
    "k_low": 1,
    "k_opt": 6,
    "m_bits": 12000,
    "penalty_high_minus_opt": 0.027067,
    "penalty_sig": true,
    "se_high": 0.000552,
    "se_low": 0.000741,
    "se_opt": 0.000324,
    "z_high_vs_opt": 42.29791,
    "z_low_vs_opt": 118.376354
  },
  "gate_g1_optimum_dominance_pass": true,
  "gate_g2_more_hashes_hurt_and_floor_pass": true,
  "gate_g3_robust_shift_pass": true,
  "head": "bloom filter: past the optimum k*, more hash functions raise the false-positive rate; the minimum is floored by bits-per-element",
  "n_elements": 1500,
  "n_queries": 1500,
  "seed": 20260717,
  "shift_config_c12": {
    "bits_per_elem": 12,
    "dom_pass": true,
    "floor_pass": true,
    "floor_phi": 0.003134,
    "fpr_high": 0.007484,
    "fpr_low": 0.081013,
    "fpr_opt": 0.003324,
    "fpr_opt_predicted": 0.003142,
    "k_high": 16,
    "k_low": 1,
    "k_opt": 8,
    "m_bits": 18000,
    "penalty_high_minus_opt": 0.00416,
    "penalty_sig": true,
    "se_high": 0.000193,
    "se_low": 0.000585,
    "se_opt": 0.000124,
    "z_high_vs_opt": 18.148262,
    "z_low_vs_opt": 129.804852
  },
  "tol": 0.2,
  "trials": 150,
  "z_gate": 3.0
}
Results-JSON sha256: 3fdfc867123a80a1476d414610413060c24b3580841f1d808dac10a75f8b5d7f
G1 optimum dominance:        PASS
G2 more-hashes-hurt + floor: PASS
G3 robust (shifted config):  PASS
```
Both runs (in-process double-call and a second process invocation) produced byte-identical output; results-dict sha256 = 3fdfc867123a80a1476d414610413060c24b3580841f1d808dac10a75f8b5d7f.

Read-out: at 8 bits/element the false-positive rate is 11.79% at k=1, bottoms at 2.22% at k*=6 (right on the memory floor φ=2.14%, closed-form predicted 2.16%), then climbs back to 4.93% at k=12 — the extra six hashes past the optimum more than double the false-positive rate (penalty +2.71 points, z=42.3), while k=1 sits 118σ above the optimum. Under the 12-bit shift the U-shape holds: 8.10% → 0.33% (k*=8, floor 0.31%) → 0.75% (k=16), penalty z=18.1, k=1 z=129.8.

## Reproduce
```
python3 ideas/fleet/bloom-optimal-k-fpr-floor-2026-07-19.py
```
Exit 0 ⇔ all_pass; the printed "Results-JSON sha256" must equal 3fdfc867123a80a1476d414610413060c24b3580841f1d808dac10a75f8b5d7f.

## Verifier
`ideas/fleet/bloom-optimal-k-fpr-floor-2026-07-19.py` (stdlib only: hashlib, json, math). WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY: the compact-canonical results dict's own sha256 is the digest; the pretty dump is indent=2, floats 6 dp.

## Fleet relevance
Cache-admission filters, LSM/SSTable read-avoidance, dedup, and membership/routing tables all pick (m/n, k). The head gives the operating rule: choose bits-per-element for the target FPR (φ = 0.6185^{m/n}: ~2% at 8 bits, ~0.3% at 12 bits, ~0.05% at 16 bits), set k = round((m/n)·ln2), and do NOT raise k to chase fewer false hits — past k* it raises them and wastes CPU on every insert and lookup. Capacity spent widening k is capacity better spent on bits.

## Why it matters (beyond the fleet)
Any structure with a "more checks must be safer" knob that also consumes the shared resource being checked rides the same U-curve — counting Bloom filters, cuckoo/quotient filters, and multi-probe hashing all trade probe count against fill. The lesson generalizes: past the balance point, adding redundancy to a shared substrate degrades the very metric it was meant to protect.

## Dedup
`git grep -il` across ideas/ for: "bloom", "false positive", "false-positive", "hash function", "membership", "bits per element" — no prior fleet head on Bloom filters or hash-based membership false-positive rates. The "false positive" hits are unrelated object classes: base-rate/PPV Bayesian posteriors (P136), linter/checker false-alarm framing (heartbeat-contradiction-linter, section-sync-checker), and grace-budget cliffs — none prices a k/m/n filter tradeoff. control/outbox.md scanned: no bloom/membership-filter head. This is fresh.

## Model basis (declared model-dependence — the P024 discipline)
The verifier uses Kirsch–Mitzenmacher double hashing (two base hashes → k indices), which the grounding source documents as giving effectively the same FPR as k independent hashes; the empirical FPR(k*) matches the closed-form (1 − e^{−k*n/m})^{k*} to within ~3% (2.22% vs 2.16% at c=8), so the double-hashing choice is not load-bearing. The model assumes distinct keys and uniform hashing; correlated or skewed key distributions shift constants but not the U-shape or the memory floor (both follow from the fill fraction 1 − e^{−kn/m}, which depends only on the total number of set bits). The floor tolerance (20%) absorbs the integer-k granularity of the optimum.

## Probe report (v0, 2026-07-19)
**1. Do both k=1 and k=2k* have a higher false-positive rate than k* at c=8?** Yes — 11.79% (k=1, z=118.4) and 4.93% (k=12, z=42.3) both exceed the 2.22% optimum at k*=6, each at ≫3σ. The sweep is U-shaped, not monotone.

**2. Is the past-optimum penalty real — do extra hashes past k* raise the FPR at ≥3σ?** Yes — FPR(2k*) − FPR(k*) = +2.71 points at z=42.3 (c=8) and +0.42 points at z=18.1 (c=12). Adding hashes past the optimum measurably worsens false positives.

**3. Does the optimum match the bits-per-element floor, and does no k beat it?** Yes — FPR(k*)=2.22% vs floor φ=2.14% (within 4%, tolerance 20%) at c=8, and 0.33% vs 0.31% at c=12; the minimum over all tested k equals FPR(k*), so no k crosses the floor. The floor is a function of m/n alone.

**4. Does the effect survive a shifted bits-per-element config (c=12)?** Yes — G3 reruns at 12 bits/element: dominance holds (z=129.8 and z=18.1), the penalty is positive at z=18.1, and the optimum sits on φ(12). Not an artifact of c=8.

**5. Is the result deterministic and reproducible?** Yes — the in-process double-run assertion holds and a second process invocation reproduces the results-dict sha256 (3fdfc867…) byte-for-byte at SEED=20260717.

**6. Does the grounding URL resolve live and document the head?** Yes — HTTP 200; the page states verbatim "the value of k that minimizes the false positive probability is k = m/n ln 2" and gives ε = (1 − e^{−kn/m})^k. Honest caveat: it states the minimizing k (which makes FPR convex, so the past-optimum rise follows mathematically) rather than spelling out "too many hashes hurt" in prose; the verifier demonstrates that consequence firsthand.

**7. Is the empirical optimum consistent with the closed-form prediction?** Yes — measured FPR(k*)=0.022213 vs predicted (1 − e^{−6/8})^6 = 0.021577 at c=8, and 0.003324 vs 0.003142 at c=12; within a few percent, as expected for double hashing.

**8. What would falsify the head?** A regime where raising k past k* does NOT increase the FPR (penalty ≤ 0 or z < 3), or where some k beats the memory floor φ by more than tolerance. The verifier checks exactly these; either flips all_pass to false and the proposal is not sim-ready.

**Recommendation: sim-ready**
