# PROPOSAL 123 — the hard-close snipe clearing leak (round-28 GAME slot, P123 → V136, +13)

> **Status:** `in-progress`
> 📊 Model: opus · high · idea/planning

Born in-progress as this session's first commit (born-red HOLD); flips to complete as the deliberate last step after the heartbeat, releasing the landing workflow.

## Objective
Draft and land the round-28 GAME-slot proposal (P123): one genuinely new, counterintuitive, stdlib-simulable game-domain pure-mechanism head, distinct from the prior game heads P099 (shop-reroll-ruin), P103 (streak-shield regression), P107 (energy-cap overflow), P111 (matchmaking win-rate mirage), P115 (compounding-reward inequality), P119 (PRD proc-rate compression), P091 (gacha pity), P095 (rubber-band controller). Domain: game auction-house economics / market microstructure — the anti-snipe timer as an economic mechanism: a hard-close auction's second-price clear leaks value below the true v_(2) because last-instant snipes fail to transmit (rate q), while a soft-close (auto-extend) auction restores the full-field clear. With pre-registered ≥3σ /se gates, a paired common-random-numbers design, a dose-response leg, a placebo (q=0) specificity leg, and a binomial-mixture closed-form anchor. Fanned to sim-lab as VERDICT 136 (+13). This slice does NOT write the verdict.

## Constraints honored
- HARD-SYNC to origin HEAD (idea-engine 4098509) before reading; sibling union taken IN if origin/main advances mid-slice.
- Claim filed FIRST; born-red card is the first commit (HOLD); branch pushed; PR opened READY; heartbeat before flip; Status→complete is the last commit.
- Round-28 rotation fleet→venture→game→unrelated: P121 opened at fleet, P122 took venture, this takes the GAME slot. P123 is the next unused number (P122 high-water, confirmed against control/outbox.md per-block ledger).
- Monte Carlo pinned SEED=20260717, ≥3σ gates on the /se margin (z on an estimated statistic, se=std/√TRIALS — the P104…P122 convention). Stdlib-only verifier (random, math, json, hashlib), no third-party. Model line family-level, PL-004 task class idea/planning.

## What happened
- Idea: the anti-snipe (auto-extend) timer in a game auction house is usually read as UX politeness — "so you don't lose to a last-second bid." Reasoned to its fuller form (Q-0254), it is an ECONOMIC mechanism. In a HARD-CLOSE (fixed-deadline) auction, bidders who wait to snipe submit last-instant sealed bids that must TRANSMIT through the server tick; each fails with probability q (latency, rate limits, tick granularity). A second-price clear over only the TRANSMITTED bids thins the effective field, so the winner pays the second-highest of a random subset — BELOW the true competitive second-highest valuation v_(2). A SOFT-CLOSE auction auto-extends on late action, letting the full field respond, and clears at v_(2). The gap leak = P_soft − P_hard ≥ 0 is a silent transfer from the seller (and, via the AH cut, a gold-sink leak) to the best-connected bidder, and it SCALES with q. Anchor: Roth & Ockenfels, "Last-Minute Bidding and the Rules for Ending Second-Price Auctions", AER 92(4), 2002.
- Pinned world SEED=20260717, TRIALS=100000, K=8, valuations iid Uniform(0,1), q∈{0.0,0.05,0.15,0.25}, second-price over the transmitted subset (reserve 0 if <2 transmit), SIGMA_GATE=3.0. Soft-close clears at v_(2)=second-highest of all K; E[v_(2)]=(K−1)/(K+1)=7/9. Paired common-random-numbers: the same valuation draws and the same transmission draws feed every q level, coupling the estimators for a low-variance dose-response.
- Gates use the P104…P122 /se convention: G1 existence — mean leak @q*=0.15 > 0 with z=mean/se ≥ 3; G2 dose-response — mean(leak(0.25) − leak(0.05)) > 0 with z ≥ 3 (paired, coupled, low-variance); G3 specificity/placebo — at q=0 the two rules coincide, per-auction leak EXACTLY 0.0 for every trial (max|placebo| == 0.0). Plus a binomial-mixture closed-form E_hard anchor cross-checking the sim.
- Dry-sim results — filled in STEP 4 from the committed verifier (exit 0, two runs byte-identical, results-dict sha256 disclosed).
- Concurrency: origin/main synced at 4098509 before this slice; if origin/main advances mid-slice a UNION merge is taken (outbox both blocks chronologically, status highest P/V high-water per line, routines line UNCHANGED coordinator-bound).
- Files: ideas/superbot-games/snipe-clearing-leak-2026-07-18.md (State: sim-ready) + committed reference verifier ideas/superbot-games/snipe_clearing_leak.py; PROPOSAL 123 block appended to control/outbox.md (P123 ↔ V136, +13); claim control/claims/proposal-123-snipe-clearing-leak.md filed; heartbeat control/status.md updated (proposal high-water → P123). Branch pushed; PR opened READY, born-red until this card flips.

## ⟲ Previous-session review
Filled in STEP 4 (read the P122 session card, carry one thing forward).

## 💡 Session idea
Filled in STEP 4.

## GROUNDING
Filled in STEP 4 with a real reachable URL (idea-engine@HEAD + the Roth-Ockenfels AER 2002 anchor).
