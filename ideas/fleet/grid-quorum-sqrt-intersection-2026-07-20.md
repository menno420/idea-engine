# A √N read/write set beats the majority: the Maekawa grid quorum

> **State:** sim-ready
> **Class:** counterintuitive-distributed-systems (round-50 FLEET opener)
> **Target:** sim-lab (VERDICT 222, +13 offset)
> 📊 Model: Claude Opus · high · idea/planning
> **Grounding:** https://en.wikipedia.org/w/index.php?title=Maekawa%27s_algorithm&oldid=1306919367@894805bdbac0adce66d1e794c45925fa9b280e89 · fetched 2026-07-20
> **Reference (external, reachable):** quorum property #1 "∀i ∀j [Rᵢ ∩ Rⱼ ≠ ∅]" with |Rᵢ| ≥ √(N−1), citing M. Maekawa, "A √N algorithm for mutual exclusion in decentralized systems".
> **Verifier (firsthand):** ideas/fleet/grid_quorum_sqrt_intersection.py · results-dict sha256 bbc54843f3693815f107f95df069c26d985a3799b2afe2c0f689a38e3659096f

## The phenomenon

Mutual exclusion and read-write consistency need only that any two quorums share a replica. Folk wisdom says that forces a majority (~N/2). It does not: arrange N=k² replicas on a k×k grid and let each quorum be one full ROW plus one full COLUMN — size 2k−1 ≈ 2√N — and every pair of quorums still intersects, guaranteed.

## Domain

Distributed systems / fault tolerance: quorum systems for mutual exclusion and replicated read/write registers (Maekawa's algorithm, grid quorums, the intersection property). A pure counterintuitive-CS head — outside fleet-ops, venture, and game theory.

## The folk belief

To guarantee two quorums always share a node you need each to hold a strict majority — anything smaller than N/2 could, in the worst case, sit entirely beside its partner and miss. So the smallest safe quorum is ⌊N/2⌋+1, and the cost of intersection is linear in N.

## The thesis (reasoned to fuller form)

The majority is sufficient but not necessary; the real requirement is a *combinatorial* intersection, and STRUCTURE delivers it at √N cost. Index the N=k² replicas as a k×k grid. Define the quorum of a cell as (all cells in its row) ∪ (all cells in its column): a cross of size k+k−1 = 2k−1. Take any two grid quorums, for cells (r₁,c₁) and (r₂,c₂). Quorum 1 contains all of row r₁; quorum 2 contains all of column c₂; those meet at the single cell (r₁,c₂), which therefore lies in both. So **every** pair of grid quorums intersects — the mutual-exclusion / read-write guarantee holds — with quorum size 2√N−1 instead of N/2.

The counterintuitive core is that size is not what buys intersection: two *randomly chosen* subsets of the SAME size 2k−1 are disjoint with strictly positive probability (for N=36, s=11 that probability is exactly 10925/1472562 ≈ 0.0074 — small but nonzero, so a random-quorum scheme genuinely fails the guarantee sometimes). The grid quorums never fail, not because they are big but because their row/column geometry forces a crossing. Structure, not magnitude, is the load-bearing property. (The 2√N−1 grid is the accessible construction; Maekawa's optimal √N quorums via finite projective planes shave the constant further, same intersection law.)

## The pinned world (committed constants)

- `SEED = 20260717`
- Main grid: `k = 6`, N = 36, quorum size s = 2k−1 = 11.
- Exhaustive enumeration: all C(36,2) = 630 unordered pairs of the 36 grid quorums (G1); grid sweep k ∈ {4,5,6,7,8,9,10} (G4).
- Monte-Carlo: `T = 2_000_000` independent two-subset draws for the disjoint-rate gates (G2, G3).
- Closed form: P(two independent uniform-random s-subsets of an N-set are disjoint) = C(N−s, s)/C(N, s).

## Pre-registered gates

- **G1 — EXACT (AGREEMENT, zero deviation).** Enumerate all 630 unordered pairs of the 36 grid quorums (k=6); the fraction that intersect must be `Fraction(1)` EXACTLY. Direction: **exact-equality** (closed-form-vs-exhaustive-enumeration agreement — the "exactly-true" gate).
- **G2 — AGREEMENT (low |z|).** The Monte-Carlo two-random-subset disjoint-rate must agree with the closed form C(N−s,s)/C(N,s) at s=11, N=36. Direction: **|z| < 3** (convergence — MC matches the exact combinatorial probability).
- **G3 — SIGNAL (≥ 3σ).** That same disjoint-rate is significantly > 0: z = p̂ / √(p̂(1−p̂)/T). Direction: **high z** (expected ~120σ) — same-size RANDOM subsets genuinely fail to always intersect, proving STRUCTURE (grid), not size, delivers the guarantee.
- **G4 — SHIFT / robustness.** For k ∈ {4,…,10}: grid intersection fraction == `Fraction(1)` EXACTLY for every k; quorum size 2k−1 < majority ⌊k²/2⌋+1 for all; and the ratio (2k−1)/k² is strictly decreasing (savings scale with N). Direction: exact-equality across k + monotone shift.
- **G5 — DETERMINISM.** In-process double-run identical; cross-invocation byte-identical.

## Pre-registered decision rule

`sim-ready` iff G1 fraction == 1 exactly AND G2 |z| < 3 AND G3 z ≥ 3 AND G4 (all-k exact-1 AND all beat majority AND ratio strictly decreasing) AND G5 identical — all on the deterministic double-run.

## Dry-sim results (verbatim)

```json
{
  "G1_exact_grid_intersection": {
    "N": 36,
    "direction": "exact-equality (Fraction == 1): EVERY grid-quorum pair intersects",
    "intersection_fraction": "1",
    "k": 6,
    "num_grid_quorums": 36,
    "num_pairs": 630,
    "pass": true
  },
  "G2_mc_agrees_closed_form": {
    "closed_form_disjoint_prob": 0.007419042458,
    "direction": "LOW |z| = CONVERGENCE (MC disjoint-rate agrees with the closed form)",
    "mc_disjoint_rate": 0.0074515,
    "pass": true,
    "se_closed": 6.0679487e-05,
    "threshold": 3.0,
    "z": 0.5349
  },
  "G3_surprise_disjoint_positive": {
    "direction": "HIGH z = SURPRISE (same-size RANDOM subsets genuinely fail to always intersect; STRUCTURE, not size, buys the guarantee)",
    "mc_disjoint_hits": 14903,
    "mc_disjoint_rate": 0.0074515,
    "pass": true,
    "se_hat": 6.0811081e-05,
    "threshold": 3.0,
    "z": 122.5352
  },
  "G4_shift_robustness": {
    "all_grid_intersection_exact_1": true,
    "all_quorum_beats_majority": true,
    "direction": "exact-equality across k: grid always intersects, 2k-1 < majority, ratio (2k-1)/N strictly decreasing (savings scale with N)",
    "k_range": [
      4,
      10
    ],
    "pass": true,
    "rows": [
      {
        "N": 16,
        "grid_intersection_fraction": "1",
        "k": 4,
        "majority_size": 9,
        "quorum_size_2k_minus_1": 7,
        "size_ratio_2k_minus_1_over_N": "7/16"
      },
      {
        "N": 25,
        "grid_intersection_fraction": "1",
        "k": 5,
        "majority_size": 13,
        "quorum_size_2k_minus_1": 9,
        "size_ratio_2k_minus_1_over_N": "9/25"
      },
      {
        "N": 36,
        "grid_intersection_fraction": "1",
        "k": 6,
        "majority_size": 19,
        "quorum_size_2k_minus_1": 11,
        "size_ratio_2k_minus_1_over_N": "11/36"
      },
      {
        "N": 49,
        "grid_intersection_fraction": "1",
        "k": 7,
        "majority_size": 25,
        "quorum_size_2k_minus_1": 13,
        "size_ratio_2k_minus_1_over_N": "13/49"
      },
      {
        "N": 64,
        "grid_intersection_fraction": "1",
        "k": 8,
        "majority_size": 33,
        "quorum_size_2k_minus_1": 15,
        "size_ratio_2k_minus_1_over_N": "15/64"
      },
      {
        "N": 81,
        "grid_intersection_fraction": "1",
        "k": 9,
        "majority_size": 41,
        "quorum_size_2k_minus_1": 17,
        "size_ratio_2k_minus_1_over_N": "17/81"
      },
      {
        "N": 100,
        "grid_intersection_fraction": "1",
        "k": 10,
        "majority_size": 51,
        "quorum_size_2k_minus_1": 19,
        "size_ratio_2k_minus_1_over_N": "19/100"
      }
    ],
    "size_ratio_strictly_decreasing": true
  },
  "G5_determinism": {
    "in_process_double_run": "IDENTICAL",
    "pass": true
  },
  "all_gates_pass": true,
  "feasibility_probe": {
    "closed_form_disjoint_prob": "10925/1472562",
    "closed_form_disjoint_prob_float": 0.007419042458,
    "note": "closed form computed FIRST; thresholds below are what this math meets"
  },
  "head": "grid-quorum-sqrt-intersection",
  "params": {
    "N_main": 36,
    "k_main": 6,
    "k_shift": [
      4,
      5,
      6,
      7,
      8,
      9,
      10
    ],
    "quorum_size_main": 11,
    "t_mc": 2000000
  },
  "seed": 20260717
}
```

`results_sha256: bbc54843f3693815f107f95df069c26d985a3799b2afe2c0f689a38e3659096f` · `in_process_double_run: IDENTICAL` · cross-invocation byte-identical.

## Honest nuance (disclosed)

- The head guarantees intersection (safety), not *availability*: a grid quorum needs a whole row AND a whole column live, so a single failed row can block progress. Grid quorums trade the majority's fault-tolerance for their smaller size — the √N win is on message/latency cost, not on the number of failures survived. The claim proved here is purely the intersection guarantee.
- `2k−1` is the accessible grid construction, not the proven optimum. Maekawa's projective-plane quorums reach ≈√N with each node in equally many quorums; the article covers that optimal √N family, and the grid is the didactic member of it. Both share the identical `Rᵢ ∩ Rⱼ ≠ ∅` property.
- G3's z is large **by construction** (a fixed positive probability against T=2M draws); it certifies the *direction* of the surprise — random same-size sets really can be disjoint — not a delicate effect. The rigorous claim is the exact gate G1.

## Dedup

Grep across ALL `ideas/` lanes (fleet, venture-lab, superbot-games) on 2026-07-20 found no prior quorum, Maekawa, grid-intersection, or mutual-exclusion head. The consistent-hashing / CAP lane returned 0 hits (no consensus/replication head). Distinct from the friendship paradox (P164), the birthday/collision family, and any voting-power head — this is the combinatorial intersection property of quorum *systems*, not a probability paradox.

## Reproduce

`python3 ideas/fleet/grid_quorum_sqrt_intersection.py` — prints the results dict and `results_sha256`. Run twice; the `results_sha256` line is byte-identical.

## Verifier

`ideas/fleet/grid_quorum_sqrt_intersection.py` (stdlib only: `random`, `math`, `fractions`, `hashlib`, `json`, `itertools`; `random.Random(20260717)` local instances only — no global random state).

## Why it matters

The grid quorum is the cleanest counterexample to "consistency needs a majority." It shows that the load-bearing property of a quorum system is a *combinatorial* intersection, and that geometry can enforce it at √N cost — the same insight that underlies real replicated stores' read/write-set sizing and the whole quorum-systems literature (availability, load, and cost trade off against the fixed intersection constraint). The lens — structure, not magnitude, buys the guarantee — generalises well beyond mutual exclusion.

## Model basis

Reasoned and pre-registered by an idea/planning pass; all constants committed before the dry-sim; gates and directions fixed in advance.

## Probe report (v0)

**1. Is the head exactly true or only approximately?**
Exactly. G1 exhaustively enumerates all 630 pairs of the 36 grid quorums (k=6) and finds the intersecting fraction is `Fraction(1)` — every pair shares ≥1 cell, zero exceptions.

**2. Could the surprise be an artifact of the chosen k=6?**
No. G4 sweeps k ∈ {4,…,10}: the grid intersection fraction is exactly 1 for every k, 2k−1 is strictly below the majority ⌊k²/2⌋+1 for every k, and the size ratio (2k−1)/k² strictly decreases (7/16 → 19/100), so the √N advantage grows with N.

**3. Does the ≥3σ signal test a real effect or a tautology?**
It certifies a real direction — two same-size RANDOM subsets are disjoint with a fixed positive probability (0.0074515 observed, z = 122.5352 above zero) — proving intersection is bought by grid STRUCTURE, not by the quorum's size. The z is large by construction; the rigorous claim rests on the exact gate G1, with G2 confirming the MC rate matches the closed form (|z| = 0.5349 < 3).

**4. Is the mechanism reproducible deterministically?**
Yes. `SEED = 20260717` via `random.Random` local instances; in-process double-run IDENTICAL and cross-invocation byte-identical (G5), digest bbc54843f3693815f107f95df069c26d985a3799b2afe2c0f689a38e3659096f.

**5. Is it genuinely unbuilt in the lab?**
Yes. A grep across all `ideas/` lanes on 2026-07-20 found no quorum / Maekawa / grid-intersection head; the consistent-hash / CAP lane was 0 hits.

**6. What breaks the √N-beats-majority claim?**
It is a safety (intersection) claim, not availability: a grid quorum needs a full row and full column live, so it survives fewer failures than a majority. The size/latency win is real; the fault-tolerance trade-off is disclosed. And 2k−1 is the didactic grid size, not the proven √N optimum (projective-plane quorums).

**7. Is the grounding external and specific?**
Yes — a pinned Wikipedia "Maekawa's algorithm" revision (oldid 1306919367, raw-wikitext sha1 894805bd…). It states quorum property #1 `Rᵢ ∩ Rⱼ ≠ ∅` and |Rᵢ| ≥ √(N−1), citing Maekawa's "A √N algorithm". Caveat: the article states the optimal √N quorum family (projective planes) rather than the plain 2k−1 grid row∪column construction the verifier enumerates — same intersection property, the grid being the accessible member of that √N family.

**8. What would a verdict measure?**
Re-run the verifier and confirm G1 fraction == 1 exactly, G2 |z| < 3, G3 z ≥ 3, G4 all-k exact-1 with 2k−1 < majority and strictly decreasing ratio, G5 identical, then recompute the results-dict sha256 and check it matches bbc54843f3693815f107f95df069c26d985a3799b2afe2c0f689a38e3659096f.

**Recommendation: sim-ready**
