# Giving FIFO page-replacement more memory can make it fault MORE — Bélády's anomaly — while LRU, a stack algorithm, provably never does

> **State:** sim-ready
> **Class:** fleet (round-49 FLEET slot)
> **Target:** sim-lab (VERDICT 218, +13 offset)
> 📊 Model: Claude Opus · high · idea/planning
> **Grounding:** https://en.wikipedia.org/w/index.php?title=B%C3%A9l%C3%A1dy%27s_anomaly&oldid=1312057235@ffabfee5a2daf46ebc33fca9e3ed94c854e2bd38 · fetched 2026-07-20
> **Reference (external, reachable):** [Bélády's anomaly — Wikipedia](https://en.wikipedia.org/w/index.php?title=B%C3%A9l%C3%A1dy%27s_anomaly&oldid=1312057235) — "In FIFO, the page fault may or may not increase as the page frames increase, but in optimal and stack-based algorithms like Least Recently Used (LRU), as the page frames increase, the page fault decreases." Byte-pinned to the raw-wikitext sha1 of the cited revision.
> **Verifier (firsthand):** ideas/fleet/belady-anomaly-fifo-nonmonotonicity.py · results-dict sha256 e5c3517c9d3408bc76941be37b820d0216fcbe0fb00c2cffaf1d8bf763bf7bff

## The phenomenon (one line)
Give a FIFO page cache one more frame and it can fault MORE, not less — on the textbook string [1,2,3,4,1,2,5,1,2,3,4,5] FIFO takes 9 faults at 3 frames but 10 at 4 — whereas LRU, a stack algorithm, provably never faults more when handed more memory.

## Domain
Operating systems / cache theory — page-replacement algorithms (FIFO vs LRU), the stack-algorithm inclusion property, Bélády's anomaly (Bélády, Nelson & Shedler 1969; Mattson, Gecsei, Slutz & Traiger 1970). Outside fleet-ops, venture, and game: a foundational computer-systems counterintuitive fact.

## The folk belief
"More memory can only help." The universal capacity-planning intuition is that adding a page frame (or a cache slot) either lowers the fault count or leaves it unchanged — never raises it. The Wikipedia article records that this was the standing belief before 1969: "Until Bélády's anomaly was demonstrated, it was believed that an increase in the number of page frames would always result in the same number of, or fewer, page faults."

## The thesis (reasoned to its fuller form — Q-0254 duty)
Model a reference string as a sequence of page requests; a *page-replacement algorithm* keeps a resident set of size `frames` and, on a miss with the set full, evicts one page by its rule. A *page fault* is a miss. Define the fault curve `F_alg(ref, m)` = faults using `m` frames.

1. **FIFO is non-monotone in `m`.** FIFO evicts the oldest-INSERTED page regardless of use. Because a larger FIFO queue reorders *which* page is oldest at each eviction, the resident set at `m+1` frames is NOT guaranteed to contain the resident set at `m` frames. That broken nesting is exactly what lets `F_FIFO(ref, m+1) > F_FIFO(ref, m)` — more memory, more faults. The canonical witness is [1,2,3,4,1,2,5,1,2,3,4,5]: `F_FIFO=9` at 3 frames, `10` at 4 (Δ=+1).
2. **LRU is a stack algorithm, so it is provably immune.** Mattson, Gecsei, Slutz & Traiger (1970) proved the *inclusion property*: for LRU (and OPT), the resident set with `m` frames is always a SUBSET of the resident set with `m+1` frames at every point in the reference string. Nesting sets means every page that is a hit at `m` frames is still a hit at `m+1`, so `F_LRU(ref, m+1) ≤ F_LRU(ref, m)` for every string and every `m`. LRU can never be anomalous — the fault curve is monotone non-increasing.
3. **The distinction is structural, not statistical.** FIFO's anomaly is not a quirk of one string: Bélády, Nelson & Shedler built strings where FIFO faults nearly TWICE as often in the larger memory, and Fornai & Iványi (2010) showed the ratio is unbounded (any fault ratio is constructible). What separates FIFO from LRU is precisely whether the algorithm respects the stack-inclusion property — a *why*, not just a *that*.
4. **The threshold needs ≥5 distinct pages.** FIFO cannot be anomalous when the number of distinct pages is ≤ the larger frame count (with `m+1 ≥ distinct pages`, the whole working set fits and faults are minimal). The classic minimal FIFO anomaly uses 5 distinct pages over a length-12 string. Exhaustively, no length-8 string over 4 pages is FIFO-anomalous.

Fuller form, one sentence: *whether "more memory ⇒ never more faults" holds is decided by the stack-inclusion property — LRU has it and is monotone; FIFO lacks it and is non-monotone (unboundedly so), with the effect requiring at least 5 distinct pages.*

## The formal model / Pinned world (committed constants)
- Object: FIFO (evict oldest-inserted, `set` residency + `deque` insertion order) and LRU (on hit → MRU, on miss evict LRU front) fault counters on integer reference strings.
- Anomaly predicate: `alg_anomalous(ref, Fmax)` = ∃ m∈[1..Fmax−1] with `F_alg(ref, m+1) > F_alg(ref, m)`.
- SEED = 20260717; G3 draws from `random.Random(20260717)`, G4 from `random.Random(20260718)` — two independent seeded streams.
- Committed constants: G1 canonical [1,2,3,4,1,2,5,1,2,3,4,5], frames 1..5; G2 exhaustive A=4, L=8 (4⁸=65536), frames 1..4; G3 N=200000, A=6, L=16, frames 1..6, z-floor 3; G4 N=200000, A=7, L=20, frames 1..7, rate-floor 0.0003, z-floor 3.
- Determinism discipline: raw counts stored as integers; derived rates/z stored as fixed-precision strings; results-dict sha256 is of the WHOLE dict and is not a field of it.

## Pre-registered gates
- **G1 — exactly-true canonical witness (frames 1..5).** FIFO faults == 9 at 3 frames and == 10 at 4 frames, anomaly_delta = +1 (>0); AND LRU faults on the SAME string are monotone non-increasing across frames 1..5. *Direction:* exact integer equality; PASS iff FIFO Δ>0 AND LRU monotone non-increasing.
- **G2 — exhaustive exactly-true (all 4⁸=65536 strings, frames 1..4).** FIFO_anomalous == 0 AND LRU_anomalous == 0, both exact integers. *Direction:* both exactly 0 — exhaustive enumeration matches the closed-form prediction: LRU is immune by the stack/inclusion property, and FIFO cannot be Belady-anomalous with ≤4 distinct pages (this pins the anomaly threshold above 4 pages; it is a statement about all length-8 strings on 4 pages, NOT about all lengths — the classic minimal FIFO anomaly needs 5 distinct pages, length 12).
- **G3 — ≥3σ signal, FIFO vs stack-algorithm LRU (N=200000, A=6, L=16, frames 1..6).** Two-proportion one-sided z-test, H0 p_fifo==p_lru, over uniform-random strings. *Direction:* z ≥ 3 — z clears 3σ because the comparator LRU is provably exactly 0, so even a rare-but-nonzero FIFO anomaly rate is hugely significant against zero; LRU anomaly count must be 0.
- **G4 — robustness / regime-shift (N=200000, A=7, L=20, frames 1..7, independent seed).** FIFO anomaly rate stays ABOVE floor 0.0003 AND the shifted-regime two-proportion z (FIFO vs LRU=0) ≥ 3, while LRU stays exactly 0. *Direction:* the FIFO anomaly persists above the floor across the regime shift while LRU is invariantly 0.

## Pre-registered decision rule
`sim-ready` iff G1 ∧ G2 ∧ G3 ∧ G4 all pass on a deterministic double-run (an in-process rerun and a separate cross-invocation reproduce the identical results-dict sha256). Any gate fail ⇒ `needs-more-grooming`.

## Dry-sim results (SEED=20260717, verbatim from belady-anomaly-fifo-nonmonotonicity.py)
```
{
  "G1_canonical_witness": {
    "anomaly_delta": 1,
    "canonical": [
      1,
      2,
      3,
      4,
      1,
      2,
      5,
      1,
      2,
      3,
      4,
      5
    ],
    "fifo_3": 9,
    "fifo_4": 10,
    "lru_curve_frames_1_to_5": [
      12,
      12,
      10,
      8,
      5
    ],
    "lru_monotone_non_increasing": true,
    "pass": true
  },
  "G2_exhaustive": {
    "A": 4,
    "L": 8,
    "fifo_anomalous": 0,
    "frames_max": 4,
    "lru_anomalous": 0,
    "pass": true,
    "total": 65536
  },
  "G3_signal": {
    "A": 6,
    "L": 16,
    "N": 200000,
    "fifo_anom": 36,
    "frames_max": 6,
    "lru_anom": 0,
    "p_fifo": "0.0001800000",
    "pass": true,
    "z": "6.000270"
  },
  "G4_robustness": {
    "A": 7,
    "L": 20,
    "N": 200000,
    "fifo_anom": 109,
    "fifo_rate": "0.0005450000",
    "floor": "0.0003000000",
    "frames_max": 7,
    "lru_anom": 0,
    "pass": true,
    "z": "10.441729"
  },
  "decision": "sim-ready",
  "gates": {
    "G1": true,
    "G2": true,
    "G3": true,
    "G4": true
  },
  "seed": 20260717
}

in_process_double_run: IDENTICAL
results_sha256: e5c3517c9d3408bc76941be37b820d0216fcbe0fb00c2cffaf1d8bf763bf7bff
decision: sim-ready
```
results-dict sha256: `e5c3517c9d3408bc76941be37b820d0216fcbe0fb00c2cffaf1d8bf763bf7bff`

## Honest nuance (disclosed)
- **The anomaly is real but RARE over uniform-random strings.** The exact measured rates are ~1.8 per ten-thousand (G3: 36/200000 = 0.00018) and ~5.5 per ten-thousand (G4: 109/200000 = 0.000545) — basis points, not "a few percent." G3's z clears 3σ only because the LRU comparator is provably exactly 0; it is significance against a hard zero, not a large effect size. The head's force is the *provable asymmetry* (LRU can never be anomalous), not the frequency.
- **Requires ≥5 distinct pages; G2 pins a threshold, not "all lengths."** Exhaustively, ZERO length-8 strings over 4 pages are FIFO-anomalous (and 4 pages can never be anomalous at any length, since the 4-frame case holds the whole working set). The classic minimal FIFO anomaly is 5 pages, length 12. G2's exhaustive `FIFO_anomalous==0` is a statement about the A=4, L=8 space only, cited as a threshold witness — not a claim that FIFO is never anomalous.
- **Adjacent-but-DISTINCT from Graham's scheduling anomaly (P201).** Graham's anomaly (greedy list scheduling on m machines: adding a machine / shortening jobs / deleting a precedence edge can increase makespan) is a DIFFERENT non-monotonicity in a DIFFERENT domain (scheduling makespan, not page faults). Both are "more resources can hurt," but the mechanisms, objects, and verifiers do not overlap — disclosed, not reused.
- **Grounding caveat:** Wikipedia *describes* the phenomenon (phenomenon-on-page); the verifier *witnesses* it firsthand (exact FIFO 9→10, exhaustive LRU immunity). The byte-pin is to raw wikitext, not the rendered page.

## Dedup
No prior idea keys on Bélády's anomaly, page replacement, page faults, FIFO/LRU caching, or LFU (grep `elady`, `page replacement`, `page fault`, `LFU`, `belady` over `ideas/` on origin/main → the only hits are THIS proposal's own verifier file; LFU zero hits). The nearest neighbor is `ideas/fleet/graham-scheduling-anomaly-2026-07-20.md` (P201 → V214), which is a DIFFERENT non-monotonicity — greedy multiprocessor scheduling makespan, not cache page faults — sharing only the abstract "more resources can hurt" shape. Distinct mechanism (stack-inclusion property vs list-scheduling), distinct object, distinct verifier. Disclosed adjacency, no overlap.

## Reproduce
```
python3 ideas/fleet/belady-anomaly-fifo-nonmonotonicity.py
```
Deterministic: SEED=20260717 (G4 uses the independent stream 20260718), stdlib-only. Prints the results dict and its sha256; the same 64-hex digest appears here, in the session card, and in control/outbox.md's P205 block.

## Verifier
`ideas/fleet/belady-anomaly-fifo-nonmonotonicity.py` — stdlib-only (`json`, `hashlib`, `math`, `random`, `collections.deque`). Implements FIFO and LRU fault counters, the anomaly predicate, and the four gates (G1 exact canonical witness + LRU monotone curve; G2 exhaustive 4⁸ enumeration; G3/G4 seeded Monte-Carlo two-proportion z-tests); asserts an in-process double-run reproduces the identical results-dict before emitting the digest.

## Why it matters
"More resources can only help" is the load-planning intuition behind adding cache slots, replicas, or buffer frames. Bélády's anomaly is the clean, provable counterexample: for a FIFO (or otherwise non-stack) eviction policy, growing the cache can *raise* the miss rate, and the harm is unbounded (Fornai–Iványi). The actionable inverse is equally sharp — choosing a STACK algorithm (LRU, OPT) buys a monotonicity guarantee: more memory is then provably never worse. A verifier that exhibits the anomaly firsthand and pins the LRU immunity exhaustively is a durable anchor for "audit the eviction policy before you assume a bigger cache is safe."

## Model basis (declared model-dependence)
The result depends only on the eviction rule (FIFO evicts oldest-inserted; LRU evicts least-recently-used) and the uniform-random reference-string model for the signal gates. The exact witness (G1) and the LRU immunity (G2, and the general stack-inclusion theorem) are model-free — they hold for every string. The anomaly *rates* (G3/G4) are specific to the uniform-random model and the pinned alphabet/length; under structured or adversarial reference strings the rate rises sharply (Bélády–Nelson–Shedler / Fornai–Iványi), so the scoped rates are conservative lower bounds on how often the anomaly can occur.

## Probe report (v0, 2026-07-20)
**1. What is the precise claim, and which parts are exact vs statistical?** FIFO faults 9 at 3 frames and 10 at 4 on the canonical string (exact, G1, and corroborated verbatim by the cited Wikipedia example), and LRU is monotone non-increasing there and exhaustively never anomalous over all 4⁸ length-8 strings on 4 pages (exact, G1+G2); the FIFO anomaly *rate* over uniform-random strings (G3/G4) is statistical — rare (~1.8–5.5 per ten-thousand) but significant against LRU's hard zero.
**2. Is it counterintuitive in a defensible way?** Yes — the universal "more memory never hurts" belief (explicitly the pre-1969 consensus per the source) is false for FIFO: adding a frame can strictly increase faults, unboundedly so.
**3. Is it deterministic and stdlib-only?** Yes — SEED=20260717 (G4 stream 20260718); `json/hashlib/math/random/collections`; an in-process double-run and a separate cross-invocation both reproduce one 64-hex digest e5c3517c…7bff.
**4. Can an independent re-implementation reproduce it?** Yes — FIFO/LRU rules, the anomaly predicate, and all gate constants and seeds are fully specified; sim-lab reproduces the results-dict sha256 byte-for-byte.
**5. What is the strongest disconfirming check?** G2's exhaustive LRU leg: if ANY of the 65536 strings made LRU anomalous, the stack-inclusion claim (the whole "LRU provably never" half of the head) would be false — zero-tolerance, exact integer.
**6. Where could it silently pass while being wrong?** If the RNG were reseeded/reused across gates, or floats formatted platform-dependently — mitigated by two independent seeded streams and storing every derived float as a fixed-precision string before hashing; and G3's z would be meaningless if LRU were not exactly 0, which G2/G3/G4 all assert explicitly.
**7. Is the grounding external and does it support THIS head?** Yes — Wikipedia "Bélády's anomaly" (byte-pinned raw-wikitext sha1 ffabfee5…bd38, revision 1312057235) states firsthand that FIFO page faults can increase with more frames while "optimal and stack-based algorithms like Least Recently Used (LRU)" see faults decrease, and gives the same 9-faults-at-3-frames, 10-at-4 example; caveat: the page *describes* the phenomenon, the verifier *witnesses* it, and the pin is raw wikitext not the rendered page.
**8. What is the dedup status?** Clear on mechanism (Belady / page replacement / FIFO / LRU / LFU all no-hit on origin/main outside this file); the only adjacency is Graham's scheduling anomaly (P201), a DISTINCT non-monotonicity in scheduling makespan — disclosed in the Dedup and Honest-nuance sections, no overlap.

**Recommendation: sim-ready**
