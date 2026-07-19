# PROPOSAL 181 — more hash functions make Bloom-filter false positives worse past the optimum k* = (m/n)·ln2, and no tuning beats the bits-per-element floor ≈ 0.6185^(m/n) (round-43 FLEET slot, P181 → V194, +13)

> **Status:** `in-progress`
> 📊 Model: Claude Opus · high · idea/planning

**Born-red HOLD.** This card lands on the FIRST commit with `Status: in-progress`, holding the substrate-gate red while the verifier and proposal doc are authored and proven. The final commit flips it to `complete` — after the outbox block and heartbeat — releasing the landing workflow. A red gate before that flip is the born-red HOLD, not a defect.

## Objective
round-43 FLEET-slot PROPOSAL 181 — Bloom-filter optimal-k / false-positive-floor head. Show with a deterministic stdlib verifier (SEED = 20260717) that a Bloom filter's false-positive rate is U-shaped in the number of hash functions k — minimized at k* = (m/n)·ln2 — so adding hashes past k* makes false positives WORSE, and that the achievable minimum is floored at φ = (½)^{(m/n)·ln2} ≈ 0.6185^{(m/n)} by bits-per-element alone (no choice of k crosses it). ≥3σ gates including a robustness gate under a shifted bits-per-element config, targeting sim-lab VERDICT 194 (+13).

## Constraints honored
- PR opens READY (not draft); landing handled by the repository CI workflow.
- stdlib-only (`hashlib, json, math`); Python 3.
- SEED = 20260717 pinned; fully deterministic; in-process double-run asserted; cross-invocation identical.
- WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY digest: sha256 of the compact-canonical results dict IS the digest; pretty dump to stdout, floats 6 dp; no on-disk JSON.
- Grounding URL verified live this session (HTTP 200, content-hash pinned).
- No model version identifiers in artifacts; family names only. Timestamps from `date -u`.

## Gate-plan (pre-registered — must match the shipped verifier)
Base config: bits-per-element c = m/n = 8, n = 1500 inserted, Q = 1500 absent queries, R = 150 trials; k ∈ {1, k*, 2k*} with k* = round(c·ln2) = 6. Shifted (robustness) config: c = 12, k* = 8, k ∈ {1, 8, 16}. Hash indices by Kirsch–Mitzenmacher double hashing. z_gate = 3.0, floor tolerance TOL = 0.20.
- **G1 — optimum dominance (c = 8).** Empirical FPR at k = 1 and at k = 2k* each strictly exceed FPR at k*, both with z ≥ 3 — both ends of the k-sweep are worse than the optimum.
- **G2 — more-hashes-hurt (the head) + floor.** The past-optimum penalty FPR(2k*) − FPR(k*) > 0 with z ≥ 3 (adding hashes past k* strictly raises the FPR), AND the achieved optimum sits at the bits-per-element floor φ = (½)^{c·ln2}: |FPR(k*) − φ| ≤ TOL·φ and no tested k beats φ by more than TOL — tuning cannot cross the memory floor.
- **G3 — robustness under a shifted config (c = 12).** Dominance (both ends worse than k* at z ≥ 3) and the past-optimum penalty (z ≥ 3) persist, and the optimum again matches its floor φ(12).

all_pass = G1 ∧ G2 ∧ G3.

## GROUNDING (verified at HEAD)
Bloom filter optimal-k / false-positive tradeoff (Bloom 1970; Wikipedia "Bloom filter"): the page states verbatim that "the value of k that minimizes the false positive probability is k = m/n ln 2" and gives ε = (1 − e^{−kn/m})^k, and documents Kirsch–Mitzenmacher double hashing for deriving the k indices. Verified live 2026-07-19T19:05:56Z (HTTP 200): https://en.wikipedia.org/wiki/Bloom_filter@15d7f16cabd1b2e9f33543aa383f4aee8a81896b — content-hash pin (sha256 of the fetched page, first 40 hex; drifts on later fetches, per the same discipline as prior heads). Honest caveat: the page states the *minimizing* k (which mathematically makes FPR(k) convex — the U-shape and the past-optimum penalty follow directly) but does not spell out "too many hash functions is counterproductive" in prose; the verifier demonstrates that consequence firsthand.

## Probe questions
**1.** Does empirical FPR at k = 1 and at k = 2k* both strictly exceed FPR at k* with z ≥ 3 at c = 8?
**2.** Is the past-optimum penalty FPR(2k*) − FPR(k*) > 0 at ≥ 3σ — i.e., do extra hashes past k* measurably raise false positives?
**3.** Does the achieved optimum FPR(k*) match the bits-per-element floor φ = (½)^{c·ln2} within TOL, and does no tested k beat that floor?
**4.** Do dominance and the penalty persist under the shifted config c = 12 (k* = 8) at ≥ 3σ?
**5.** Does the in-process double-run assertion hold, and does a cross-invocation re-run reproduce the results-dict sha256 byte-for-byte under SEED = 20260717?
**6.** Does the grounding URL resolve live (HTTP 200) and document the specific optimal-k / FPR-formula head?
**7.** Is the empirical FPR(k*) consistent with the closed-form predicted (1 − e^{−k*n/m})^{k*}?
**8.** Are the pre-registered gates here identical to the gates the verifier ships?

## Outcome
_Filled at flip._ Verifier `ideas/fleet/bloom-optimal-k-fpr-floor-2026-07-19.py`; results-dict sha256, per-gate z, PR #, target sim-lab VERDICT 194 (+13) recorded on the final commit.

## ⟲ Previous-session review
PROPOSAL 180 (typical-set "mode mirage", round-42 UNRELATED slot, sim-ready, targets V193, PR #676): clean information-theory head — the single most-probable i.i.d. sequence is atypical and essentially never observed while observations concentrate at the entropy rate; gates pre-registered at z_gate = 3.0, +13 offset consistent, grounding (AEP) verified live. No blocker seen. This P181 opens round-43 on the FLEET slot (rotation FLEET → VENTURE → GAME → UNRELATED).

## 💡 Session idea
Companion FLEET head for a later slot: **the counting-Bloom-filter deletion tax** — supporting deletes turns each bit into a small saturating counter, so the false-positive floor rises by the counter-overflow probability, and a fixed memory budget spent on counter width is memory *not* spent on more slots; quantify the crossover where a plain Bloom + periodic rebuild beats a counting Bloom at equal bytes, gated at ≥3σ. Clean, groundable (counting Bloom filters), stdlib-checkable.
