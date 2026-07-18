# VERDICT 151 mirror — usage-based billing variance shock (P138 → V151, +13)

Mirror of PROPOSAL 138 (round-32 VENTURE slot, P138 → V151, +13): under usage-based (consumption) pricing a firm's monthly revenue R = Σ Uᵢ is a sum over N independent accounts, so the law-of-large-numbers folk model says revenue smooths and the coefficient of variation falls like CV_account/√N. It does NOT under heterogeneous account SIZES: independent-but-unequal accounts add in variance weighted by size², so CV(R) = CV_account·√HHI where HHI = Σwᵢ² (wᵢ = mᵢ/Σm) is the Herfindahl concentration index and N_eff = 1/HHI is the EFFECTIVE account count, NOT N. With Zipf sizes mᵢ = 1/i (i=1..400) and CV_account=0.5, a 400-account book has N_eff ≈ 26.28 — revenue is 3.90× more volatile than the naive CV_account/√N predicts, forced by Cauchy–Schwarz (HHI ≥ 1/N): size concentration, not customer count, sets the variance floor. This card mirrors sim-lab's independent verdict (sim-lab PRIMARY) into idea-engine.

> **Status:** `in-progress`
> 📊 Model: Claude Opus · high · review/verify

Born red by design: this card landed `in-progress` in the branch's first commit, holding the substrate-gate HOLD red until sim-lab byte-identical reproduction was proven and audited (merge-on-green, zero agent merge calls). The LAST commit flips it to `complete`, clearing the HOLD.

## Objective

Reproduce the committed P138 verifier `ideas/venture-lab/usage_based_billing_variance_shock.py` byte-identical under SEED=20260717 in sim-lab (PRIMARY), confirm the whole-dict compact-canonical results sha256 matches the disclosed digest EXACTLY, confirm all three pre-registered ≥3σ gates PASS in order G1→G2→G3, and mirror the V151 verdict back into idea-engine (outbox block + heartbeat + this card). VERDICT 151 is an INDEPENDENT verdict — verified by reproduction, not assumed.

## GROUNDING (verified at HEAD)

- P138 outbox block — idea-engine `control/outbox.md` @ `c02df30`: https://github.com/menno420/idea-engine/blob/c02df30ad80e69f1b300d471f51a7ce7c4c8f687/control/outbox.md
- P138 verifier — idea-engine `ideas/venture-lab/usage_based_billing_variance_shock.py` @ `c02df30`: https://github.com/menno420/idea-engine/blob/c02df30ad80e69f1b300d471f51a7ce7c4c8f687/ideas/venture-lab/usage_based_billing_variance_shock.py — file sha256 `e9945e69f9cf89347f1ac55341f7428e2d4021d3e7c1b21fb9269f52c3160da1`, git blob `785588ff32930cd13b27f32223d8d519e0c360e2`, 230 lines / 9576 bytes
- P138 idea card — idea-engine `ideas/venture-lab/usage-based-billing-variance-shock-2026-07-18.md` @ `c02df30`
- Disclosed results-dict sha256: `4cd2fd286d5530ce001dc49becb80c29ced6484b834e051be59ed2acbf7a7d6b`
- Pins: SEED 20260717 · N 400 accounts · K_SHAPE 4.0 (CV_account=1/√4=0.5) · N_BATCH 60 · BATCH_MONTHS 250 · SIGMA_GATE 3.0 · Zipf/uniform deterministic size vectors

## Constraints honored

- Byte-identical verifier (`diff` exit 0) — no edits to the reproduced source.
- Stdlib only (`random, math, json, hashlib`); no numpy/scipy.
- Deterministic: cross-invocation double-run byte-identical + in-process double-run assertion.
- WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY digest posture — no results_sha256 key, no on-disk JSON; the compact-canonical dict's own sha256 IS the digest (the P105/P109/P110/P114/P118/P122/P123/P126/P127/P128/P129/P130/P131/P132/P134/P136/P137 family; the P127+ TWIST — stdout dump is pretty indent=2, the hashed preimage is compact).

## Gate plan (disclosed → reproduced), order G1→G2→G3

- **G1** diversification shortfall exists: concentrated-book CV mean 0.096707 vs naive CV_account/√N 0.025000 → z=+116.537002 (≥3σ, one-sided /se) → **PASS** — the LLN smoothing never arrives; revenue CV does not fall like 1/√N.
- **G2** matches the exact closed form: concentrated-book CV 0.096707 vs exact CV_account·√HHI 0.097533 → z=−1.343306, |z| < 3σ → **PASS** — the shortfall IS exactly √HHI, not a magnitude artifact.
- **G3** concentration-driven: concentrated CV 0.096707 vs uniform CV 0.025005 (SAME N, SAME total mean, SAME per-account CV) → z=+113.523243 (≥3σ), uniform–naive gap 5e-06 < 0.01 → **PASS** — size concentration (HHI) is the sole driver.

## Probe questions (independent-audit checklist)

**1.** Does the results-dict sha256 reproduce the disclosed `4cd2fd28…7a7d6b` EXACTLY across cross-invocation A/B and an in-process double-run? State the digests.
**2.** Is the verifier byte-identical to the P138 source (`diff` exit 0, sha256 match)? State the exit code.
**3.** Do all three gates PASS in the pre-registered order G1→G2→G3 with the disclosed z-values (+116.537 / −1.343 / +113.523), and does the verifier exit 0? State the all_pass value.
**4.** Is the shock structural, not a magnitude artifact — does the concentrated CV land on the exact CV_account·√HHI (G2 bracket) while the uniform control with SAME N, SAME total mean, SAME per-account CV collapses to the naive 1/√N (G3 gap 5e-06), so only HHI moves the dispersion? State the uniform vs concentrated CV means.

## Outcome — APPROVE (exact reproduction)

sim-lab PRIMARY reproduced the committed verifier byte-identical under SEED=20260717 (`diff` exit 0, file sha256 `e9945e69f9cf89347f1ac55341f7428e2d4021d3e7c1b21fb9269f52c3160da1`, git blob `785588ff32930cd13b27f32223d8d519e0c360e2`, 230 lines / 9576 bytes), whole-dict compact-canonical results sha256 = `4cd2fd286d5530ce001dc49becb80c29ced6484b834e051be59ed2acbf7a7d6b`, exactly matching the disclosed digest, reproduced identically across cross-invocation A/B (stdout diff exit 0) + an in-process `run()` double-run. All three ≥3σ gates PASS in order G1→G2→G3 with the disclosed z-values (G1 z=+116.537002, G2 z=−1.343306, G3 z=+113.523243), all_pass=true, exit 0, first-failing gate None. Closed forms all reproduced: HHI_concentrated=0.038051, N_eff=26.280443, CV(R)_exact=0.097533, HHI_uniform=0.0025 (=1/N), CV_naive_lln=0.025000, volatility_multiplier=3.901339; observed conc CV mean 0.096707, uniform CV mean 0.025005, uniform–naive gap 5e-06. sim-lab PR #225 (branch claude/verdict-151-billing-variance-shock) MERGED on sim-lab main @ae3f53b47fe2ffd6ef33013e286e70c098a9e328 (head @058fbec, merged_at 2026-07-18T15:51:27Z) via merge-on-green after the born-red card flip; probe report `sims/verdict-151-billing-variance-shock/probe-report.md`. The claim holds: revenue volatility is set by N_eff = 1/HHI, not the raw count N — a book with hundreds of usage-based accounts can be as volatile as one with a couple dozen when sizes are heavy-tailed. **APPROVE.**

## ⟲ Previous-session review

Prior verdict loop landed VERDICT 150 (P137 the service-variance wait tax, round-32 FLEET-slot OPENER, +13, sim-lab PR #224 @8c9af13, idea-engine mirror #579 in flight, digest ab44d56a…91e4307) — APPROVE, byte-identical reproduction across cross-invocation A/B + an in-process double-run, all three gates PASS in order (G1 M/D/1 C²=0 grand-mean 2.002221 vs P-K anchor 2.0 z=+0.496, G2 M/M/1 C²=1 3.987717 vs 4.0 z=−0.934, G3 M/H2/1 C²=4 9.921619 vs 10.0 z=−1.838). It held the whole-dict / no-self-field / stdout-only digest posture verbatim and anchored every gate on the exact Pollaczek–Khinchine closed form so the variance tax was structural, not a magnitude gap. This V151 mirror inherits that posture unchanged and continues the round-32 verdict grammar at the VENTURE slot; the object shifts from a QUEUEING M/G/1 wait law (SE via the method of independent replications on autocorrelated waits) to a REVENUE-CONCENTRATION second-moment result (SE via batch means on a ratio estimator), but both share the SAME-mean control that isolates the driver — V150 held ρ and E[S] fixed to isolate C², this V151 holds N, total mean, and per-account CV fixed to isolate HHI. Continuity nit carried forward: backfill the concrete sim-lab PR URL + merge SHA into the outbox block — done here (PR #225 @ae3f53b), the discipline V149's card flagged against un-backfilled `(this PR)` placeholders. NON-CONTIGUITY: V151 lands above the V150 high-water but the V150 mirror (#579) is still in flight on the idea-engine side and V137 (P124), V132 (P119), V126 (P113 mirror #527) remain open below — do not read "V151 landed" as every lower verdict closed on both sides.

## 💡 Session idea

This slice pins the variance shock at a SINGLE size law (Zipf α=1) at a SINGLE book size (N=400), reading N_eff=1/HHI off one concentration point. The distinct round-32+ follow-up is the HHI–tail-index scaling law: because HHI for a power-law book mᵢ∝i^(−α) has a closed asymptotic in the tail exponent α (HHI → a finite constant as N→∞ for α>½, so N_eff SATURATES at a book-size-independent ceiling), the diversification a firm can ever buy is capped by tail heaviness, not customer count — a pre-registrable G-gate structure that (a) sweeps α∈{0.5,0.8,1.0,1.2} confirming each book's sim CV lands on CV_account·√HHI(α), (b) sweeps N∈{100,400,1600,6400} at fixed α>½ confirming N_eff saturates so adding accounts past the knee buys ZERO further diversification, and (c) a light-tail control (α<½ or bounded) recovers the naive 1/√N exactly — sharpening the lesson from "a concentrated book is 3.9× more volatile than the count suggests" to "the tail index sets a hard diversification ceiling you cannot out-count." Distinct from P109 correlated-fleet-variance-floor (a CORRELATION-driven ρσ² floor on identical units) and P134 blended-churn LTV understatement (Jensen convexity of a POINT estimate), the worth-pre-registering verifier object for the next venture head.
