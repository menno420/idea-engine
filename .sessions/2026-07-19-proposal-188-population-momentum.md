# PROPOSAL 188 — Population momentum: replacement fertility still grows a population (round-44 UNRELATED slot, P188 → V201, +13)

> **Status:** in-progress
> 📊 Model: Claude Opus · high · idea/planning

**Born-red HOLD.** This card lands born-red on the first in-progress commit to hold the PR red; it flips to `complete` only after the verifier reproduces byte-identical and the gate battery passes green. The HOLD is the sole legitimate red — every other gate red is a real defect.

## Objective

Show, with a stdlib-only deterministic verifier, that a population whose fertility instantly drops to exact replacement (NRR = 1.000) keeps growing for roughly a generation — the demographic *population momentum* of Keyfitz (1971) — and that the growth is driven solely by the young age structure inherited from the prior growth regime, not by any residual per-cohort surplus.

## Constraints honored

- stdlib-only (Leslie-matrix power iteration + binomial survival / Poisson births, Gaussian-approximated for large counts); SEED=20260717 pinned; deterministic in-process double-run with an equality assert.
- WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY digest: the compact-canonical results dict's own sha256 IS the digest; no self-referential field; stdout pretty dump (indent=2, sort_keys), floats 6 dp; no on-disk JSON.
- Pre-registered gates frozen BELOW before any run; thresholds not tuned to force a pass.

## Pinned world (committed constants)

- SEED = 20260717
- Age classes: 17 five-year bins (ages 0–84); childbearing classes 3–8 (ages 15–44).
- Per-step (5-year) survival s = 0.96 for classes 0–15; class 16 is terminal.
- Base fertility shape F_base (classes 0–8) = [0, 0, 0, 0.30, 0.90, 1.00, 0.70, 0.35, 0.10].
- Growth regime NRR = 1.50; replacement regime NRR = 1.00 (same shape, rescaled).
- Initial total N0 = 300000; stochastic replicates K = 1500; projection horizon T = 50 steps (250 years).
- Robustness shift: childbearing shape shifted +1 class later (delayed childbearing), NRR re-pinned to 1.50 → 1.00.
- G2 null band = 0.02; Z_GATE = 3.0.

## Gate-plan (pre-registered — frozen, z_gate = 3.0)

- **G1 — momentum is real.** Starting from the growth-regime stable age structure and switching to replacement fertility (NRR = 1.000), mean momentum M = final/initial over K replicates satisfies z1 = (mean_M − 1)/SE ≥ 3.0 with mean_M > 1.
- **G2 — age structure is the sole cause (null contrast).** A control starting from the replacement-regime stationary structure (identical replacement fertility) shows no material growth: |mean_M_null − 1| < 0.02; and the contrast z_contrast = (mean_M − mean_M_null)/√(SE1²+SE_null²) ≥ 3.0. Same fertility, only the starting age structure differs.
- **G3 — robustness under a shifted vital-rate distribution.** Under the delayed-childbearing fertility shape, momentum from the growth-regime structure still satisfies z3 = (mean_M_shift − 1)/SE ≥ 3.0.
- all_pass = G1 ∧ G2 ∧ G3.

## GROUNDING (to be verified live before flip)

Keyfitz, N. (1971), "On the momentum of population growth"; reference article: Population momentum (Wikipedia). Verified reachable at flip; specific head — growth continues after replacement fertility because of the young age structure — quoted verbatim in the doc.

## Probe questions

**1.** Is the growth a coding artifact of the Leslie convention, or a real renewal-equation consequence of NRR = 1 giving intrinsic rate zero?
**2.** Would a seed change or a different N0 flip the sign of the effect?
**3.** What is the simplest version that still bites — does the null contrast (G2) isolate age structure as the cause?
**4.** How large is the momentum for this pinned world, and does it match the Keyfitz direction (M > 1)?
**5.** Where could I be fooling myself — is NRR truly 1.000000 post-switch, or is residual fertility hiding?
**6.** Does the effect survive a shifted childbearing schedule (G3)?
**7.** What decision does it change for anyone modelling a fertility transition to replacement?
**8.** How will we know it worked — byte-identical digest, all_pass = true, gates in order?

## Outcome

_Pending — filled at flip with results-dict sha256, per-gate z-stats, deterministic momentum M_det, and all_pass._

## ⟲ Previous-session review

P187 (Glicko RD order-sensitivity, round-44 GAME slot) landed sim-ready targeting V200; results-dict sha256 d4f690a5…. Round-44 rotation FLEET→VENTURE→GAME→UNRELATED: P185 (bufferbloat) → V198, P186 (reserve starvation) → V199 landed, P187 (Glicko) → V200 in flight; this card fills the UNRELATED slot, P188 → V201.

## 💡 Session idea

Companion head: *reproductive-value weighting* — momentum equals the ratio of the initial population's total reproductive value to that of its own stationary equivalent (Keyfitz's v-weighted formula). A follow-on verifier could show the deterministic M_det is reproduced to 6 dp by the reproductive-value inner product ⟨v, n0⟩ / ⟨v, w⟩, turning the stochastic estimate into a closed-form check.
