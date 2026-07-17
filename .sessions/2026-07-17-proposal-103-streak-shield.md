# PROPOSAL 103 — streak-shield variance amplification (round-23 game slot, P103 → V116, +13)

> **Status:** `complete`
> 📊 Model: opus-4.8 · high · idea/planning

Born in-progress as this session's first commit (born-red HOLD); flipped to complete as the deliberate last step after the heartbeat, releasing the landing workflow.

## Objective
Draft and land the round-23 GAME-slot proposal (P103): one genuinely new, counterintuitive, stdlib-simulable competitive-game-mechanics idea with pre-registered ≥3σ gates, fanned to sim-lab as VERDICT 116 (+13). Executes ORDER 018 (owner's live overnight generate→verify loop directive).

## Constraints honored
- HARD-SYNC to origin HEAD (idea-engine dc75cb3) before reading; control/inbox.md@HEAD confirms ORDER 018 (owner overnight directive, verbatim) is the governing order for this slice.
- Claim filed before work; born-red card is the first commit (HOLD); PR opened READY immediately; heartbeat before flip; Status→complete is the last commit.
- `python3 bootstrap.py check --strict` green (exit 0) before push.
- Paired Monte Carlo (same per-game outcomes scored with and without the shield) with a pinned SEED=20260717 and a ≥3σ gate; stdlib-only verifier (random, math, json, hashlib), no third-party. Model line family-level (ORDER 012 / PL-004 idea/planning class).

## What happened
- Idea: a competitive game grants a "streak shield" — after W=3 consecutive true wins a player banks a shield that negates their next loss (the loss is scored as a WIN, a +2 rating swing). It is sold as anti-tilt PROTECTION for struggling players, but it is REGRESSIVE: because the frequency of completing a length-W win run is monotone increasing in per-game win probability p, an already-high-skill cohort (p=0.55) banks and spends more shields than the low-skill cohort (p=0.45) it is marketed to protect, so the "protection" flows uphill. Shield supply, not loss availability, is the binding constraint on uplift, and supply is skill-monotone.
- Pinned world SEED=20260717, N_PER_COHORT=10000, GAMES=200, STREAK_W=3, LOW_P=0.45, HIGH_P=0.55, SIGMA_GATE=3.0. Paired Monte Carlo: each player's iid Bernoulli(p) outcome sequence is scored TWICE (shield-on / shield-off) on the SAME draws; uplift = shield-on net rating − shield-off net rating; cohort uplift = mean over 10000 players.
- Dry-sim (stdlib verifier, exit 0, two runs byte-identical): low_uplift_mean +21.6436 (se 0.05745), high_uplift_mean +35.313 (se 0.068073), gap +13.6694 (~1.63× more protection to the high cohort). G1 regressive-amplification uplift_gap_sigma=153.4585 ≥3σ PASS; G2 both-positive/strict-ordering (low +21.64>0 AND high>low) PASS; passed=true. Disclosed results-dict sha256 0294f75799989decfe6c0166136691509239a91ac8eaba75d1932074022c09b4.
- One-line design fix (pre-registered): grant shields on LOSS streaks, not win streaks — funds the safety net from the cold-run distress signal it targets, making the protection progressive.
- Files: ideas/superbot-games/streak-shield-regression-2026-07-17.md (State: sim-ready) + committed reference verifier ideas/superbot-games/streak_shield_regression.py; PROPOSAL 103 block appended to control/outbox.md (P103 ↔ V116, +13); claim control/claims/proposal-103-streak-shield.md filed; heartbeat updated (proposal high-water → P103, baton → V116 then P104). PR #498. `python3 bootstrap.py check --strict`: the only exit-1 finding was the born-red HOLD (in-progress card), cleared by this flip; the preflight content legs (check_ideas + outbox↔ideas cross-check) pass.

## ⟲ Previous-session review
Immediate predecessor P102 (round-23 VENTURE slot, the growth cash-trough trap) drafted sim-ready by the parallel slice (idea-engine #497), awaiting VERDICT 115 — offset ledger (+13) and baton confirmed intact before extending the rotation to the game slot. Game-lane predecessor P099 (the shop-reroll ruin value trap) landed APPROVE as V112 (idea-engine #495-era slice). P103 continues the round-23 rotation (fleet→venture→game→unrelated) at the game slot with a DISTINCT mechanism (regressive incidence of a win-streak-gated protection resource, measured by a paired-difference cohort contrast — not an interior optimum on a spend lever like P099, not a gacha-pity counter like P091, not a PID/rubber-band controller like P095).

## 💡 Session idea
Regressive-incidence is a reusable audit template for any "help the weak" mechanic: audit a protection/subsidy by its COHORT-CONDITIONAL benefit, not its average benefit — if the resource that funds the safety net is gated on a SUCCESS signal (win streak, high MMR, spend, tenure), the benefit is monotone in the very trait it claims to offset, so it flows uphill and widens the gap it claims to close. The general fix is to gate the resource on the DISTRESS signal it targets (loss streak, low MMR, new-account status). Candidate future proposals: MMR-decay dampers (gated on rank → protects the ranked, not the churning), loss-forgiveness tokens earned by playtime (protects the engaged, not the frustrated), and referral/loyalty rebates scaled by spend (subsidize the whales, not the price-sensitive) — each a success-gated-protection regressivity claim with its own cohort-contrast σ.

## GROUNDING
idea-engine@dc75cb3 (HEAD at sync, verified via `git ls-remote origin main` == local `git rev-parse HEAD`). The regressive-amplification result is verified firsthand by the committed stdlib verifier ideas/superbot-games/streak_shield_regression.py — two byte-identical runs, exit 0, paired Monte Carlo under SEED=20260717; disclosed results-dict sha256 0294f75799989decfe6c0166136691509239a91ac8eaba75d1932074022c09b4 (high uplift +35.313 vs low +21.6436, gap +13.6694 at 153.4585σ). Mechanism grounded in the shield-supply argument (length-W win-run rate is monotone in p), not a fabricated external fetch.

📊 Model: opus-4.8 · high · idea/planning
