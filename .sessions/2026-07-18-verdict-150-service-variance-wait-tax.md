# VERDICT 150 mirror — service-variance wait tax (P137 → V150, +13)

Mirror of PROPOSAL 137 (round-32 FLEET slot OPENER, P137 → V150, +13): for an M/G/1 FIFO queue the Pollaczek–Khinchine mean-value law gives mean queue wait W_q = (ρ/(1−ρ))·E[S]·(1+C²)/2, where C²=Var(S)/E[S]² is the squared coefficient of variation of SERVICE time, so at FIXED utilization ρ=0.8 and FIXED mean service E[S]=1.0 the wait depends ONLY on service-time variance: W_q = 2.0 (M/D/1, C²=0) / 4.0 (M/M/1, C²=1) / 10.0 (M/H2/1, C²=4) — a 1:2:5 (5×) spread at the same load and the same average job, invisible to any utilization/throughput dashboard because the (1+C²)/2 tax is a multiplicative factor capacity math never sees. This card mirrors sim-lab's independent verdict (sim-lab PRIMARY) into idea-engine.

> **Status:** `in-progress`
> 📊 Model: Claude Opus · high · review/verify

Born red by design: this card lands `in-progress` in the branch's first commit, holding the substrate-gate HOLD red until sim-lab byte-identical reproduction is proven and audited (merge-on-green, zero agent merge calls). The LAST commit flips it to `complete`, clearing the HOLD.

## Objective

Reproduce the committed P137 verifier `ideas/fleet/service_variance_wait_tax.py` byte-identical under SEED=20260717 in sim-lab (PRIMARY), confirm the whole-dict compact-canonical results sha256 matches the disclosed digest EXACTLY, confirm all three pre-registered ≥3σ /se gates PASS in order G1→G2→G3, and mirror the V150 verdict back into idea-engine (outbox block + heartbeat + this card + claim). VERDICT 150 is an INDEPENDENT verdict — verified by reproduction, not assumed.

## GROUNDING (verified at HEAD)

- P137 outbox block — idea-engine `control/outbox.md` @ `f008e13`: https://github.com/menno420/idea-engine/blob/f008e130a058b1a62b92d053bb6fd315ec730ac4/control/outbox.md — offset cited verbatim from the P137 depends-ledger: "sim-lab consumes at +13 (PROPOSAL 137 -> VERDICT 150). Offset pinned; authority = this outbox per-block ledger + control/status.md (predecessor P136 -> V149)." (P137 block dated `2026-07-18T15:13:15Z`).
- P137 verifier — idea-engine `ideas/fleet/service_variance_wait_tax.py` @ `f008e13`: https://github.com/menno420/idea-engine/blob/f008e130a058b1a62b92d053bb6fd315ec730ac4/ideas/fleet/service_variance_wait_tax.py — file sha256 `945c0af9bc496522f1b03935afa975a89386a58ab76a246c870a3a2cc6c97974`, git blob `c13e49f78abac8ff39dd62514e37a97413c18624`, 174 lines / 5592 bytes.
- P137 idea card — idea-engine `ideas/fleet/service-variance-wait-tax-2026-07-18.md` @ `f008e13`.
- Disclosed results-dict sha256: `ab44d56a22c24f83c4a2048af56dc3dbdbf462d3aa9990bd19c64426891e4307`.
- Pins: SEED 20260717 · RHO 0.8 · MEAN_SERVICE 1.0 (λ=0.8) · N_JOBS 600000 · WARMUP 150000 · REPLICATIONS 30 · CV2_H2 4.0 · Z_GATE 3.0.
- Domain anchor: Pollaczek–Khinchine mean-value formula, https://en.wikipedia.org/wiki/Pollaczek%E2%80%93Khinchine_formula (Kleinrock, Queueing Systems Vol.1 1975 §5.6).

## Constraints honored

- Byte-identical verifier (`diff` exit 0) — no edits to the reproduced source.
- Stdlib only (`hashlib, json, math, random`); no numpy/scipy.
- Deterministic: cross-invocation double-run byte-identical + an in-process double-run (`run()` ×2, compact-hashed).
- Valid standard errors: the exact single-server FIFO Lindley recursion produces AUTOCORRELATED waits, so the verifier uses the METHOD OF INDEPENDENT REPLICATIONS (30 independent sub-seeded reps, each contributing ONE post-warmup mean) — std/√R is a valid se, naive std/√n would not be.
- WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY digest posture — no results_sha256 key, no on-disk JSON; the compact-canonical dict's own sha256 IS the digest (the P105/P109/P110/P114/P118/P122/P123/P126/P127/P128/P129/P130/P131/P132/P134/P135/P136 family; the P127+ TWIST — stdout dump is pretty indent=2, the hashed preimage is compact).

## Gate plan (disclosed → reproduced), order G1→G2→G3

- **G1** deterministic M/D/1 (C²=0): grand-mean queue wait 2.002221 vs P-K anchor 2.0 → z=+0.496 (se 0.004476), |z| < 3σ → **PASS** — the zero-variance baseline is the pure load term ρ/(1−ρ)·E[S].
- **G2** exponential M/M/1 (C²=1): grand-mean 3.987717 vs P-K anchor 4.0 → z=−0.934 (se 0.013144), |z| < 3σ → **PASS** — DOUBLE the deterministic wait at the SAME ρ and E[S], from service variance alone.
- **G3** hyperexponential M/H2/1 (C²=4): grand-mean 9.921619 vs P-K anchor 10.0 → z=−1.838 (se 0.042648), |z| < 3σ → **PASS** — 5× the deterministic wait, completing the 1:2:5 variance-only spread.

## Outcome

Ruling + card flip deferred to the deliberate LAST commit (born-red HOLD). sim-lab PRIMARY reproduction executed + landed; the flip to `complete` that releases merge-on-green is the final step.

## ⟲ Previous-session review

Prior verdict loop landed VERDICT 149 (P136 the base-rate PPV collapse, round-31 UNRELATED slot CLOSER, +13, sim-lab PR #222 @29c343e2, idea-engine mirror #575, digest 89c4bd02…895faac8) — APPROVE, byte-identical reproduction across cross-invocation A/B + an in-process double-run, all three gates PASS in order (G1 posterior=0.5 z=−0.898, G2 positive-rate z=+0.563, G3 collapse-deepens z=+1.188). It held the whole-dict / no-self-field / stdout-only digest posture verbatim and carried the backfill-discipline nit (fill the concrete sim-lab PR URL + merge SHA into the outbox block once known). This V150 mirror inherits that posture unchanged and OPENS the round-32 verdict grammar at the FLEET slot; its outbox block + this card carry the concrete sim-lab PR #224 URL and merge SHA @8c9af134 inline. Object shift: V149 was a Bayes base-rate / posterior object on a single Monte-Carlo stream; this V150 is a QUEUEING / M/G/1 Lindley-recursion object whose valid standard error demands the method of independent replications (autocorrelated waits) — a different variance-estimation posture than V149's Bernoulli se. NON-CONTIGUITY: V150 advances the high-water above V149 but V137 (P124), V132 (P119), V126 (P113 mirror #527) remain open below — do not read "V150 landed" as every lower verdict closed on both sides. Coordinator-bound routines stay armed and are NOT re-armed by this seat.

## 💡 Session idea

This slice pins the variance tax at a SINGLE utilization (ρ=0.8) across three service distributions (C²=0/1/4), reading the (1+C²)/2 factor off three points. A genuinely distinct NEXT fleet-slot object pins the **variance–utilization interaction surface and the "variance-equivalent utilization" lever**: because P-K factors cleanly into a load term ρ/(1−ρ) and a variance term (1+C²)/2, the two knobs are SEPARABLE and multiplicative, so an operator can trade one for the other — sweep ρ×C² and confirm each cell's wait is the product form within 3σ (separability), solve for the ρ' that makes an M/D/1 queue incur the SAME wait as an M/M/1 at ρ=0.8 (the variance-equivalent utilization — how much spare capacity a variance-halving buys), and a heavy-traffic control (ρ→1) confirming the variance tax stays a bounded multiplicative factor while the load term diverges (so variance reduction and capacity addition are NOT substitutes near saturation). Deliberately distinct from this fixed-ρ P-K wait-law head and from P089 variance-blind-provisioning-trap (which prices the SLA-violation rate + the (1+CV²) CAPACITY-provisioning correction, not the pure wait law).
