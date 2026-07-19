# PROPOSAL 188 — Population momentum: replacement fertility still grows a population (round-44 UNRELATED slot, P188 → V201, +13)

> **Status:** complete
> 📊 Model: Claude Opus · high · idea/planning

**Born-red HOLD (cleared).** This card landed born-red as `in-progress` to hold the PR red on the first commit; it flips to `complete` here, after the verifier reproduced byte-identical and the gate battery passed green. The HOLD was the sole legitimate red — every other gate red is a real defect.

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

## GROUNDING (verified live)

[Population momentum — Wikipedia](https://en.wikipedia.org/wiki/Population_momentum) — verified reachable 2026-07-19 via WebFetch: "Population momentum explains why a population will continue to grow even if the fertility rate declines... a current increase in fertility rates causes an increase in the number of women of childbearing age roughly twenty-to-forty years later." Documents the specific head (continued growth after fertility reaches replacement, via age structure). Historical origin conventionally Keyfitz (1971), Demography 8(1):71–80 — not cited on the Wikipedia page, so that attribution is unverified from this source.

## Probe questions

**1. Is the growth a coding artifact of the Leslie convention, or a real renewal-equation consequence of NRR = 1 giving intrinsic rate zero?** Real — λ = 1 exactly at NRR = 1 (Euler–Lotka); the growth is the transient of a young structure relaxing to stationary, shown RNG-free by M_det = 1.291976.

**2. Would a seed change or a different N0 flip the sign of the effect?** No — direction is deterministic; z ≈ 1250 above the null. Larger N0 only tightens SE.

**3. What is the simplest version that still bites — does the null contrast (G2) isolate age structure as the cause?** Yes — fertility held at replacement, only the starting structure varies; young grows 29%, stationary stays flat (1.000409).

**4. How large is the momentum for this pinned world, and does it match the Keyfitz direction (M > 1)?** M ≈ 1.292; direction matches Keyfitz and the Wikipedia worked example.

**5. Where could I be fooling myself — is NRR truly 1.000000 post-switch, or is residual fertility hiding?** nrr_repl_check = 1.000000; no residual surplus — the growth is age structure.

**6. Does the effect survive a shifted childbearing schedule (G3)?** Yes — delayed childbearing still gives M = 1.219339 at z ≈ 1116.

**7. What decision does it change for anyone modelling a fertility transition to replacement?** It warns against reading a per-unit equilibrium as an aggregate one: the aggregate overshoots for ~a generation while built-up structure drains.

**8. How will we know it worked — byte-identical digest, all_pass = true, gates in order?** Yes — sha256 fb74854… byte-identical across fresh runs, all_pass = true, G1 → G2 → G3 in order.

## Outcome

Verifier `ideas/fleet/population_momentum.py` reproduced byte-identical across two fresh invocations. results-dict sha256 = `fb74854ebd92a08fe48770136cf4e5645b47176394d1b04a70c2a0cc6ef36f33`; all_pass = true.

- deterministic_momentum M_det = 1.291976 (ultimate size 29.2% above the switch level).
- nrr_repl_check = 1.000000 (post-switch fertility is exact replacement).
- G1 momentum: mean_M = 1.291456, SE = 0.000234, z = 1246.791124 → PASS.
- G2 null contrast: mean_M_null = 1.000409 (inside the 0.02 band), z_contrast = 949.016224, z_null = 2.059462 → PASS.
- G3 robustness (shifted): mean_M_shift = 1.219339, SE = 0.000197, z = 1115.580283 → PASS.

Shipped to sim-lab for VERDICT 201 (P188 → V201, +13). Outbox entry appended `status: sim-ready`; proposal high-water advanced P187 → P188.

## ⟲ Previous-session review

P187 (Glicko RD order-sensitivity, round-44 GAME slot) landed sim-ready targeting V200; results-dict sha256 d4f690a5…. Round-44 rotation FLEET→VENTURE→GAME→UNRELATED: P185 (bufferbloat) → V198, P186 (reserve starvation) → V199 landed, P187 (Glicko) → V200 in flight; this card fills the UNRELATED slot, P188 → V201.

## 💡 Session idea

Companion head: *reproductive-value weighting* — momentum equals the ratio of the initial population's total reproductive value to that of its own stationary equivalent (Keyfitz's v-weighted formula). A follow-on verifier could show the deterministic M_det is reproduced to 6 dp by the reproductive-value inner product ⟨v, n0⟩ / ⟨v, w⟩, turning the stochastic estimate into a closed-form check.
