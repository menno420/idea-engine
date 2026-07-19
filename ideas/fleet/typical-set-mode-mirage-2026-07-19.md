# Typical-set "mode mirage": the single most-probable sequence is the one you almost never see

> **State:** sim-ready
> **Class:** counterintuitive-math · information theory (Asymptotic Equipartition Property / typical set)
> **Slot:** round-42 UNRELATED (rotation FLEET P177 → VENTURE P178 → GAME P179 → UNRELATED P180)
> **Target:** sim-lab (VERDICT 193, +13 offset)
> **Grounding:** https://en.wikipedia.org/wiki/Asymptotic_equipartition_property@78b633eddfc34ed73d8a1a7250cc1ceb38bc1d52 · fetched 2026-07-19T18:32:26Z
> **Reference (external, reachable):** https://en.wikipedia.org/wiki/Asymptotic_equipartition_property — Cover & Thomas, *Elements of Information Theory*, ch. 3
> 📊 Model: Claude Opus · high · idea/planning

## The phenomenon
Flip a biased coin (p = 0.7 heads) 1000 times. The single most-probable outcome is all-heads — yet you will essentially never see it; you will see a sequence with ~700 heads whose individual probability is astronomically *smaller* than all-heads.

## The folk belief
"The outcome you observe should be near the most probable one." Intuition equates *typical* with *maximum-probability*. For repeated i.i.d. trials this is false: the mode is a mirage.

## The thesis (reasoned to fuller form — Q-0254 duty)
Shannon's Asymptotic Equipartition Property splits the 2^n possible sequences into a *typical set* of ≈2^{nH(p)} sequences, each of probability ≈2^{−nH(p)}, that together carry ≈all the mass — and everything else, including the maximum-probability mode. Because the typical set is exponentially large while the mode is a single point, an observation lands in the typical set with probability →1. The observed sequence therefore has per-symbol surprisal ≈H(p) = 0.881 bits, strictly greater than the mode's per-symbol surprisal log₂(1/p) = 0.515 bits — i.e. the sequence you see is each ~2^{n·(H−log₂(1/p))} = 2^{~366} times *less* probable than the mode you never see. Probability concentrates away from the probability maximum. This is not large-deviations rareness; it is the generic case.

## The formal model (committed constants)
- Source: i.i.d. Bernoulli(p), n = 1000 symbols/sequence, M = 4000 sequences sampled.
- Empirical entropy-rate of a sequence: ĥ = −(1/n)·log₂P(seq) = −(k·log₂p + (n−k)·log₂(1−p))/n for k ones.
- Mode = the all-majority-symbol string (all-heads for p > ½); its per-symbol surprisal s = log₂(1/max(p,1−p)).
- Base p = 0.7 (H = 0.881291, s = 0.514573); shift p = 0.9 (H = 0.468996, s = 0.152003).
- SEED = 20260717.

## Pre-registered gates (z_gate = 3.0) — identical to the shipped verifier
- **G1 — Typical concentration.** |mean ĥ − H(p)| ≤ 0.10 bits AND in-band fraction (|ĥ−H|≤0.10) ≥ 0.99.
- **G2 — Mode is a mirage (≥3σ).** z_sep = (mean ĥ − s)/se ≥ 3.0 AND the exact modal sequence occurs 0 times in M draws.
- **G3 — Robustness under a shifted distribution (≥3σ).** At p = 0.9: |mean ĥ − H| ≤ 0.10 AND in-band ≥ 0.99 AND z_sep ≥ 3.0 AND modal count 0.

## Pre-registered decision rule
sim-ready iff G1 ∧ G2 ∧ G3 (all_pass = true), the in-process double run is identical, and a cross-invocation re-run reproduces the results-dict sha256 byte-for-byte.

## Dry-sim results (verbatim, SEED = 20260717)
```
{
  "all_pass": true,
  "base_entropy_bits": 0.881291,
  "base_in_band_frac": 1.0,
  "base_mean_hrate_bits": 0.881064,
  "base_mode_count": 0,
  "base_mode_surprisal_bits": 0.514573,
  "base_p": 0.7,
  "base_se_bits": 0.00028,
  "base_z_concentration": 0.811993,
  "base_z_separation": 1308.854386,
  "eps_bits": 0.1,
  "gate_g1_concentration_pass": true,
  "gate_g2_mode_mirage_pass": true,
  "gate_g3_robust_shift_pass": true,
  "head": "typical-set mode mirage: the most-probable sequence is never observed",
  "n_sequences": 4000,
  "n_symbols": 1000,
  "seed": 20260717,
  "shift_entropy_bits": 0.468996,
  "shift_in_band_frac": 0.999,
  "shift_mean_hrate_bits": 0.468904,
  "shift_mode_count": 0,
  "shift_mode_surprisal_bits": 0.152003,
  "shift_p": 0.9,
  "shift_se_bits": 0.000472,
  "shift_z_concentration": 0.193235,
  "shift_z_separation": 671.930225,
  "z_gate": 3.0
}
Results-JSON sha256: 1479479100edba6509b0275d31717a2f44b4504d6051023feffc5f13395b8c36
ALL_PASS: True
```
Cross-invocation double run: IDENTICAL. Results-dict sha256: `1479479100edba6509b0275d31717a2f44b4504d6051023feffc5f13395b8c36`.

Read-out: at p = 0.7 the observed per-symbol surprisal (0.881064 bits) sits **1308.85σ** above the mode's (0.514573 bits) with the mode observed **0** times in 4000 draws; the typical band captures **100%** of draws. Under the p = 0.9 shift the mirage survives — **671.93σ** separation, mode observed **0** times, in-band **99.9%**.

## Verifier
`ideas/fleet/typical-set-mode-mirage-2026-07-19.py` — stdlib-only (`random, math, json, hashlib, sys`), SEED-pinned, in-process double-run assert, WHOLE-DICT/NO-SELF-FIELD/STDOUT-ONLY digest, floats 6 dp.

## Why it matters
Any "most-likely-path" heuristic — Viterbi-style point estimates, modal imputation, "expected" log states — targets the mode, which is exactly the outcome the world does not produce. Reasoning about *typical* behaviour (entropy-rate, the typical set) is not a refinement of "most probable"; for long sequences it is a different and correct target.

## Dedup
Searched ideas/ for entropy / AEP / typical-set / information-theory heads and scanned control/outbox.md. Nearest shipped cousins are distinct: Benford (first-digit law), Cauchy no-averaging (P160), German-tank MVUE, coupon-collector occupancy. None concerns the typical-set-vs-mode split. The AEP typical set has not shipped.

## Model basis (P024 discipline)
Bernoulli i.i.d. AEP; entropy in bits (log₂). No hidden fitting; all constants committed above.

## Probe report (v0)
**1. Does mean ĥ land within 0.10 bits of H(p) at both p = 0.7 and p = 0.9?** → yes (0.881064 vs 0.881291; 0.468904 vs 0.468996).
**2. Is the exact modal sequence observed 0 times at both p?** → yes (0 and 0 of 4000).
**3. Is z_sep ≥ 3σ at both p?** → yes, hugely (1308.85 and 671.93).
**4. Does a cross-invocation re-run reproduce the sha256 byte-for-byte?** → yes (IDENTICAL; sha256 1479479100edba…).
**5. Does the in-process double-run assertion hold?** → yes.
**6. Does the grounding URL resolve live and document the head?** → yes (HTTP 200; the AEP page states individual outcomes can have higher probability than any typical-set member while observations still come from the typical set).
**7. Does the shift gate (p = 0.9) preserve concentration and the mirage?** → yes.
**8. Are these gates identical to the shipped verifier's?** → yes (G1/G2/G3 as coded).

## One-line correction
"Typical" ≠ "most probable": for long i.i.d. sequences the maximum-probability outcome is atypical and essentially never observed.

**Recommendation: sim-ready**
