# PROPOSAL 151 — St. Petersburg cap-collapse: a doubling press-your-luck jackpot has INFINITE expected value, yet capping the payout at 2^M coins collapses its fair ticket price to exactly M/2 + 1

> **Status:** `in-progress`
> 📊 Model: Claude Opus · high · idea/planning

Born-red HOLD: this card is the session's FIRST content commit (alongside the claim), born `in-progress` to hold the `substrate-gate` RED so the PR cannot merge before the deliberate `complete` flip. The flip (the deliberate LAST commit, after the verifier + idea doc + outbox P151 block + heartbeat) releases the merge-on-green backstop. A red gate AFTER this flip is a real defect, not the HOLD.

## Objective

Draft and land round-35 GAME-slot PROPOSAL 151 — St. Petersburg cap-collapse: a doubling "press-your-luck" jackpot (flip a fair coin, the pot doubles on heads, bank on the first tails) has INFINITE uncapped expected value, yet once the house caps the payout at 2^M coins its fair ticket price collapses to exactly M/2 + 1 coins and grows only LOGARITHMICALLY in the cap — doubling the bankroll (M→M+1) adds half a coin, not double the payout. Ship a markdown-first card, a committed stdlib-only deterministic verifier (SEED=20260717, ≥3σ /se gates, disclosed results-dict sha256), a deterministic double-run, an outbox block (P151 → V164, +13), and a heartbeat update. VERDICT 164 (P151 → V164, +13) is the next independent slice, NOT authored here.

## Constraints honored

- Round-35 GAME slot (rotation fleet→venture→game→unrelated; round-35 FLEET P149→V162, VENTURE P150→V163, this GAME slot P151→V164). Offset +13 (P151 → V164) — the verdict is NOT authored here. Offset authority = this repo's control/outbox.md P151 depends-ledger + control/status.md.
- Digest posture: WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY (the P105…P150 family) with the P127+ TWIST (compact canonical hashed preimage, pretty indent=2 stdout dump, floats rounded 6 dp, no on-disk JSON, in-process double-run byte-identity assertion).
- Stdlib-only verifier (hashlib, json, math, random); pinned SEED=20260717; /se z convention (z=(mean−H0)/se); ordered ≥3σ gates G1 finite-price-collapse → G2 sublinear-scaling → G3 robustness-under-shifted-coin.
- Outbox `## PROPOSAL 151 · … · status: sim-ready` block appended once (append-only, deduped).
- Status heartbeat: proposal high-water P150 → P151 (union-max, no regress); verdict high-water kept (this is a PROPOSAL slice, no verdict authored); routines line UNCHANGED (coordinator-bound).
- Born-red first commit (card in-progress + claim) → verifier → idea doc + outbox + heartbeat → flip complete LAST.

## GROUNDING

Round-35 GAME-slot of the superbot-games proposal→verdict pipeline. Pinned world: SEED=20260717, N_SAMPLES=400000, ≥3σ /se gates, disclosed results-dict sha256. Verifier (firsthand, ground truth): `ideas/superbot-games/st_petersburg_cap_collapse.py` — stdlib-only (hashlib, json, math, random); results-dict sha256 `e1919f49d20df0b50121864b8e35f78be0637e4eeb812799e9f0d8af535ef078`. Pinned constants: classic continue-prob p=0.5 / multiplier r=2 (critical curve p·r=1), nominal cap 2^12=4096, slope caps {2^6,2^8,2^10,2^12}, N_SAMPLES=400000, SIGMA_GATE=3.0; shifted-coin robustness p=0.4 / r=2.5 (still p·r=1) cap 2.5^10. Closed form (firsthand anchor): EV_cap(p,r,M) = (1−p)·((pr)^M−1)/(pr−1) + (pr)^M, reducing on the critical curve pr=1 to (1−p)·M+1 = M/2+1 for fair doubling. External reference (reachable): St. Petersburg paradox — https://en.wikipedia.org/wiki/St._Petersburg_paradox (permanent revision 1359513006, fetched 2026-07-19T02:41:04Z). Grounding branch-point: idea-engine main @80e432d; verifier + idea doc committed on branch claude/proposal-151-st-petersburg-cap-collapse.

## Probe questions

**1. Is the mechanism genuinely new against the game backlog?** Yes — a grep of ideas/ and control/ at HEAD for `petersburg|doubling jackpot|bounded bankroll|infinite expected value` returned NONE. Every prior game-lane head is an equilibrium / economy / matchmaking / tournament / gacha result; NONE model a divergent-EV lottery or a bounded-bankroll price collapse. Nearest relatives: shop-reroll-ruin (optimal stopping on a finite reroll budget) and the fleet gamblers-ruin-edge-asymmetry (bounded random walk) — both are bounded-bankroll gambling, but neither has a DIVERGENT expected value or the log-of-cap fair-price law; this is the FIRST St. Petersburg / infinite-EV-jackpot card in any lane.

**2. Do all pre-registered gates PASS in order on the /se margin?** Yes — all three PASS in order at SEED=20260717: G1 finite-price-collapse z=+16496.525875 (fair price 7.067918 ≪ half-cap 2048); G2 sublinear-scaling z=+1998.187697 (cap 2^6→2^12 raises the price by 3.069885, not the 251.876047 a cap-proportional intuition predicts; log-rule anchor z=+0.561254); G3 robustness-under-shifted-coin z=−1.000661 (|z|≤3 anchor: shifted p=0.4/r=2.5 price 6.828497 matches the generalized closed form 7.0). all_pass=true, first_failing_gate=null, exit 0.

**3. Does the digest reproduce EXACTLY and deterministically?** Yes — both a CLI cross-invocation double-run and the in-process double-run assertion produce results-dict sha256 `e1919f49d20df0b50121864b8e35f78be0637e4eeb812799e9f0d8af535ef078`, byte-identical; floats rounded 6dp, one random.Random(SEED) stream, no on-disk JSON, exit 0.

**4. Does the proposal advance the proposal high-water without regressing anything?** Yes — proposal high-water ADVANCES P150 → P151 (round-35 GAME slot, union-max, no regress); verdict high-water STAYS (this is a PROPOSAL slice — no verdict authored). Baton: round-35 FLEET P149→V162 + VENTURE P150→V163 CLOSED; this GAME slot P151→V164; next the round-35 UNRELATED slot P152.

## Outcome

sim-ready. On the pinned world (SEED=20260717, fair doubling p=0.5/r=2, N_SAMPLES=400000), the doubling jackpot's uncapped expected value diverges, yet the capped fair price is a small finite number set by the BITS of bankroll: at cap 2^12=4096 the Monte-Carlo fair price is 7.067918 coins (closed form M/2+1 = 7.0), ≈290× below half the maximum payout (2048), z=+16496.525875. Raising the cap from 2^6 to 2^12 (a 64× larger jackpot) lifts the fair price by only 3.069885 coins — the +½-per-bit log rule (predicted +3.0) — which is z=+1998.187697 below the +251.876047 a cap-proportional intuition predicts; doubling the max jackpot does not double the price. The finite-log-price law survives a shifted distribution (biased coin p=0.4, multiplier r=2.5 held on the critical curve p·r=1): the capped fair price stays finite at 6.828497 and matches the generalized closed form (1−p)·M+1 = 7.0 within noise (z=−1.000661), with the log-rule slope tracking (1−p)=0.6 rather than 0.5. Fair-price-vs-cap ladder (MC / closed form): 2^6 3.998032/4.0 · 2^8 4.952937/5.0 · 2^10 6.121433/6.0 · 2^12 7.067918/7.0. All three ≥3σ /se gates PASS in order; all_pass=true, first_failing_gate=null, exit 0; results-dict sha256 e1919f49…f078 reproduced EXACT across a deterministic double-run. Transferable rule (Q-0264): price a divergent-EV "double-or-bank" gamble feature by the closed form of the CAPPED game — set by the log of the bankroll, not the headline jackpot — because the uncapped sample mean never converges and a bigger advertised max payout barely moves the fair price. Shipped to sim-lab for VERDICT 164 (P151 → V164, +13).

## ⟲ Previous-session review

Newest OTHER complete session card: `.sessions/2026-07-19-proposal-150-founder-dilution-waterfall.md` (PROPOSAL 150 — founder-dilution liquidation waterfall, round-35 VENTURE slot, sim-ready, digest bf4042bd… EXACT, born-red HOLD released on the deliberate complete flip). Baton picked up: round-35 FLEET P149→V162 and VENTURE P150→V163 CLOSED; this slice takes the round-35 GAME slot with P151. Carry-forwards honored: digest posture WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY with the P127+ compact-canonical twist (verified against the script text, not assumed); SEED pinned 20260717; born-red HOLD held from the first content commit to the deliberate complete flip (merge-on-green released there, no agent merge call); proposal high-water advanced by UNION (P150 → P151), verdict high-water kept; routines line UNCHANGED (coordinator-bound).

## 💡 Session idea

round-35 UNRELATED-slot P152 is the next independent slice (rotation fleet→venture→game→unrelated). A clean FOLLOW-ON to THIS head (named, not authored here): the BOUNDED-UTILITY resolution — re-run the jackpot with a concave utility u(x)=log(x) instead of a payout cap and locate the certainty-equivalent ticket price; the prediction is that log-utility yields a finite price EVEN WITHOUT a cap (Bernoulli's original 1738 resolution), and that the cap and the utility bound give the SAME log-scaling law, so "cap the payout" and "bound the utility" are interchangeable price-tamers. Deduped: distinct from the payout-cap collapse shipped here and from every prior game head.
