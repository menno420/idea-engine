# PROPOSAL 150 — founder-dilution waterfall: a higher headline valuation with participating + a liquidation multiple pays founders LESS at exit

> **Status:** `complete`
> 📊 Model: Claude Opus · high · idea/planning

Born-red HOLD: this card was the session's FIRST content commit (alongside the claim), born `in-progress` to hold the `substrate-gate` RED so the PR could not merge before this deliberate `complete` flip. The flip (the deliberate LAST commit, after the verifier + idea doc + outbox P150 block + heartbeat) releases the merge-on-green backstop. A red gate AFTER this flip is a real defect, not the HOLD.

## Objective

Draft and land round-35 VENTURE-slot PROPOSAL 150 — the founder-dilution liquidation waterfall: between two term sheets raising the SAME amount for the SAME company, the one with the HIGHER headline pre-money valuation can leave founders with LESS money at exit across a strict MAJORITY of realistic outcomes, because it carries a PARTICIPATING preferred with a liquidation MULTIPLE whose participation drag dominates the founder-friendly effect of the lower investor ownership fraction the higher valuation buys — everywhere except the extreme upside tail. Ship a markdown-first card, a committed stdlib-only deterministic verifier (SEED=20260717, ≥3σ /se gates, disclosed results-dict sha256), a deterministic double-run, an outbox block (P150 → V163, +13), and a heartbeat update. VERDICT 163 (P150 → V163, +13) is the next independent slice, NOT authored here.

## Constraints honored

- Round-35 VENTURE slot (rotation fleet→venture→game→unrelated; round-35 opened at the FLEET slot with P149, this is the VENTURE slot P150). Offset +13 (P150 → V163) — the verdict is NOT authored here. Offset authority = this repo's control/outbox.md P150 depends-ledger + control/status.md.
- Digest posture: WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY (the P105…P149 family) with the P127+ TWIST (compact canonical hashed preimage, pretty indent=2 stdout dump, floats rounded 6 dp, no on-disk JSON, in-process double-run byte-identity assertion).
- Stdlib-only verifier (hashlib, json, math, random); pinned SEED=20260717; /se z convention (z=(mean−H0)/se); ordered ≥3σ gates G1 majority-inversion → G2 typical-outcome gap → G3 robustness.
- Outbox `## PROPOSAL 150 · … · status: sim-ready` block appended once (append-only, deduped).
- Status heartbeat: proposal high-water P149 → P150 (union-max, no regress); verdict high-water kept V161 (this is a PROPOSAL slice, no verdict authored); routines line UNCHANGED (coordinator-bound).
- Born-red first commit (card in-progress + claim) → verifier → idea doc + outbox + heartbeat → flip complete LAST.

## GROUNDING

Round-35 VENTURE-slot of the venture-lab proposal→verdict pipeline. Pinned world: SEED=20260717, ≥3σ /se gates, disclosed results-dict sha256. Verifier (firsthand, ground truth): https://github.com/menno420/idea-engine/blob/ed22c62f259264149568ec798ffbaa7b330ca642/ideas/venture-lab/founder_dilution_waterfall.py — git blob 2bb413badfe75bdbed32298179a9340cd43ee348, file sha256 daad631413974ffcbf0eb6951c35bdf64ec970f6c0ce1be7140a88d532026100, 287 lines / 12093 bytes, stdlib-only (hashlib, json, math, random). Pinned constants: RAISE=10, Offer A pre=30 / 1x non-participating (f_A=0.25), Offer B pre=50 / 2x participating uncapped (f_B=1/6), X_CROSS=200; exit LogNormal Dist A (median 80, sigma 1.0) primary + Dist B (median 120, sigma 1.3) robustness; M_TRIALS=20000; SIGMA=3.0. Analytic anchor: founder_A(X)=X−max(10,0.25X), founder_B(X)=(1−1/6)(X−20); equal at 0.75X=0.8333(X−20) → X*=200 exactly (below it A>B). External reference (reachable): liquidation-preference / participating-preferred waterfall — https://en.wikipedia.org/wiki/Liquidation_preference + https://en.wikipedia.org/wiki/Preferred_stock. Grounding branch-point: idea-engine main; verifier + idea doc committed on branch claude/proposal-150-founder-dilution-waterfall.

## Probe questions

**1. Is the mechanism genuinely new against the venture backlog?** Yes — a grep of ideas/venture-lab/ and control/ at HEAD shows every prior venture head is an operating-metric / growth / revenue / cash / sales-ops result; NONE touch the cap table or the exit waterfall. This is the FIRST liquidation-preference / founder-vs-investor exit-economics card in the venture lane. Nearest relative P146 (quota-cliff bunching) is sales-comp deal-timing — a different actor, object, and mechanism.

**2. Do all pre-registered gates PASS in order on the /se margin?** Yes — all three PASS in order at SEED=20260717: G1 majority-inversion win_rate=0.7983 z=+105.128721; G2 typical-outcome gap gap_mean=+8.787216 z=+300.536834 (frac_below_cross 0.8153); G3 robustness (Dist B) win_rate=0.62305 z=+35.907274, gap=+8.22916 z=+234.981636 — all ≥3σ; all_pass=true, first_failing_gate=null, exit 0.

**3. Does the digest reproduce EXACTLY and deterministically?** Yes — both the CLI double-run and the in-process double-run assertion produce results-dict sha256 bf4042bdc18bf2c5ff3d1530a97ad2a7ead43038407f095ff2b5304df4f3b7c1, byte-identical; floats rounded 6dp, one random.Random(SEED) single stream (Dist A then Dist B), no on-disk JSON, exit 0.

**4. Does the proposal advance the proposal high-water without regressing anything?** Yes — proposal high-water ADVANCES P149 → P150 (round-35 VENTURE slot, union-max, no regress); verdict high-water STAYS V161 (this is a PROPOSAL slice — no verdict authored). Baton: round-35 fleet-slot P149 + venture-slot P150 DRAFTED; next: V162 for P149, V163 for P150; then round-35 game-slot P151.

## Outcome

sim-ready. On the pinned world (SEED=20260717, RAISE=10, Offer A pre=30/1x-non-participating, Offer B pre=50/2x-participating, X_CROSS=200, exit LogNormal, M_TRIALS=20000), the higher-valuation participating-multiple sheet (Offer B) leaves founders with LESS at exit than the lower-valuation clean sheet (Offer A) across a strict majority of realistic outcomes: win_rate=0.7983 (z=+105.128721) and, conditional on a non-moonshot exit (X<200, 81.53% of draws), founders net +$8.787216M MORE under Offer A (z=+300.536834); the median founder proceeds are 60.243238 (A) vs 50.270264 (B). The effect survives a heavier-tailed exit calibration (Dist B: win_rate 0.62305 z=+35.907274, below-crossover gap +8.22916 z=+234.981636). Honest crossover (disclosed): above X*=200 Offer B wins, and under the moonshot-heavy Dist B the raw full-distribution MEAN even flips to B (207.803124 vs 215.568532) — the head is a body/typical-exit claim, not a universal one. All three ≥3σ gates PASS in order; all_pass=true, first_failing_gate=null, exit 0; results-dict sha256 bf4042bdc18bf2c5ff3d1530a97ad2a7ead43038407f095ff2b5304df4f3b7c1 reproduced EXACT across a deterministic double-run. Transferable rule (Q-0264): price a term sheet on the liquidation-preference WATERFALL, not the headline valuation — a participating multiple is a large first-order founder haircut while a headline-valuation bump is a small tail-only credit, so trade valuation down for clean 1x non-participating terms unless the exit is a near-certain moonshot. Shipped to sim-lab for VERDICT 163 (P150 → V163, +13).

## ⟲ Previous-session review

Newest OTHER complete session card: `.sessions/2026-07-19-proposal-149-coordinated-omission.md` (PROPOSAL 149 — coordinated omission, round-35 FLEET slot, sim-ready, digest 12d3ce4f… EXACT, born-red HOLD released on the deliberate complete flip). Baton picked up: round-35 opened at the FLEET slot with P149; this slice takes the round-35 VENTURE slot with P150. Carry-forwards honored: digest posture WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY with the P127+ compact-canonical twist (verified against the script text, not assumed); SEED pinned 20260717; born-red HOLD held from the first content commit to this deliberate complete flip (merge-on-green released here, no agent merge call); proposal high-water advanced by UNION (P149 → P150), verdict high-water kept (V161); routines line UNCHANGED (coordinator-bound).

## 💡 Session idea

round-35 game-slot P151 is the next independent slice (rotation fleet→venture→game→unrelated). A clean cap-table FOLLOW-ON to THIS head (named, not authored here): the PARTICIPATION-CAP crossover — re-run the waterfall with Offer B's participation CAPPED at 3x (the common real term) and locate the exit value where the cap binds and B's tail-win disappears; the prediction is that a cap moves the crossover UP and shrinks B's moonshot advantage, so "higher valuation + capped participation" is a strictly worse founder deal than uncapped in the tail while still losing in the body. Deduped: distinct from the uncapped waterfall shipped here and from every prior venture head.
