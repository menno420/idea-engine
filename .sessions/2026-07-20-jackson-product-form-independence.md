# PROPOSAL 197 — Jackson product-form independence: coupled M/M/1 stations that feed each other (with feedback routing) carry provably non-Poisson internal flow yet an EXACT product of independent M/M/1 marginals with zero equal-time correlation (round-47 FLEET slot; P197 → V210, +13)

> **Status:** `in-progress`
> 📊 Model: Claude Opus · high · idea/planning
> heartbeat: 2026-07-20T04:40:15Z — born-red HOLD: this card is PROPOSAL 197's FIRST commit, born `in-progress` to hold the `substrate-gate` RED so the PR cannot merge before the deliberate `complete` flip. Flipping to `complete` (the LAST commit, after the doc + verifier + outbox block) releases the merge-on-green enabler. A red gate AFTER the flip is a real defect, not the HOLD.

## 💡 Session idea
Jackson product-form as a fleet capacity-planning lens — size each station independently as M/M/1 even under feedback routing: once the linear traffic equations are solved for the effective per-station rate λᵢ, the joint stationary backlog law is EXACTLY the product ∏ᵢ(1−ρᵢ)ρᵢ^{nᵢ}, so per-station provisioning at ρᵢ = λᵢ/μᵢ is exact rather than an approximation, and the equal-time backlogs are uncorrelated — a station-by-station sizing rule for feedback pipelines, bounded by the exponential/BCMP conditions and equal-time (not lagged) independence.

## ⟲ Previous-session review
Prior session landed round-46 UNRELATED-slot PROPOSAL 196 (Bertrand's paradox / non-uniqueness of "random chord": three equally natural "uniform" mechanisms give exactly 1/3, 1/2, 1/4) sim-ready → sim-lab VERDICT 209 (+13), via idea-engine PR #729 (merge 3f309a5): doc + verifier bertrand_paradox_chord.py (results-dict sha256 ab79371c9908f7b16f9478d41969e224eb4c95c19d237a2773df693173b5c3cb), born-red HOLD released on the complete flip. That P196 closed the round-46 rotation at the UNRELATED slot; this P197 OPENS round-47 at the FLEET slot (rotation fleet→venture→game→unrelated). Neutral: V209 not yet ruled at this card's birth; no regress claimed against it.

## Objective
Author and land round-47 FLEET-slot PROPOSAL 197 (Jackson product-form independence) as sim-ready: idea doc + stdlib verifier + outbox block + this card, born-red HOLD released on the complete flip, landing on green via merge-on-green (zero agent merge calls). Target sim-lab VERDICT 210 (+13 offset).

## Constraints honored
- Offset +13 (P197 → V210), cited from the outbox per-block ledger + status.md (predecessor P196 → V209).
- Digest posture WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY: compact-canonical sha256 over the results dict IS the digest; no self field; floats 6 dp; no on-disk JSON; SEED=20260717; in-process double-run + separate cross-invocation byte-identical.
- Born-red first commit (this card `in-progress`) → doc + verifier → outbox block → flip `complete` LAST; enabler lands on green (merge-on-green), zero agent merge calls.
- External content grounding (Wikipedia "Jackson network", byte-pinned raw-wikitext sha1), NOT a house self-reference. Grounding pin is a 40-hex wikitext sha1, not a 64-char sha256.

## Pinned world + gates
3 single-server exponential (M/M/1) stations, external Poisson arrivals, Markov routing with a feedback cycle. **Set 1** (strong feedback 3→1 w.p. 3/4): λ0=(1,0,0), μ=(8,7,6) → λ=(4,4,4), ρ=(1/2,4/7,2/3). **Set 2** (partial 3-cycle, each station also exits): λ0=(1,0,0), μ=(2,6/7,4/7) → λ=(8/7,4/7,2/7), ρ=(4/7,2/3,1/2). SEED=20260717, 800000 events, 50000 warmup, 30 batches/set. Gates: **EXACTLY-TRUE** — product measure solves the CTMC global balance with fractions.Fraction `exact_balance_max_abs_residual = 0/1` over 64 interior states both sets (traffic-equation residual 0); **≥3σ non-Poisson-internal** — Set-1 station-1 merged stream CV²=1.404111 (se 0.019995) → z_nonpoisson=20.210254 ≥ 3; **product-form-holds** (|z|<3) — Set-1 marginal-mean z {0.133253, 0.575864, 0.983478}, correlation z {0.233043, 0.336708, 0.455705}; Set-2 mean z {1.224147, 1.098711, 0.591916}, correlation z {0.677484, 0.424487, 0.395371}; **robustness** — Set 2 re-passes exact + product-form gates; **determinism** — in-process double-run + cross-invocation byte-identical, exit 0.

## GROUNDING
English Wikipedia "Jackson network" oldid 1358616430, raw wikitext self-computed sha1 `2bb20c407ea3d109bc936dabc7039de2f671b7cb` byte-matches MediaWiki's own reported revision sha1 (clean byte-pin), fetched live 2026-07-20. The article states the product form verbatim: π(k₁,…,k_m) = ∏ᵢ ρᵢ^{kᵢ}(1−ρᵢ), and the adjacent theorem states the queue independence. Caveat: the sha1 pins the raw wikitext (not rendered HTML) and the product form sits in `<math>` LaTeX markup. External content citation, not a house pin.

## Disclosed digest
results-dict sha256 `29d55fa57612782046831e792beb1584cb5c688bc181b6363d12774b56cae258` (full 64 hex), exit 0, byte-identical across in-process double-run and separate cross-invocation.
