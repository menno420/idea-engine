# PROPOSAL 101 — the winner's curse in a common-value task auction: when N agents bid to claim a task by their own noisy estimate, the winner is the one who most overestimated, so naive commitment systematically loses (round-23 fleet opener, P101 → V114, +13)

> **Status:** `complete`
> 📊 Model: opus-4.8 · high · idea/planning

Born in-progress as this session's first commit (born-red HOLD); flips to complete as the deliberate last step after the heartbeat, releasing the installed merge-on-green workflow to land the PR.

## Objective
Draft and fan in the round-23 FLEET-opener PROPOSAL 101 — "the winner's curse in a common-value task auction." Reason the common-value-auction result to its fuller form and register it as a pinned-world, pre-registered-gate proposal to sim-lab (P101 → V114, +13): N agents each get an unbiased-but-noisy private signal of a task's common value and the highest signal wins the claim; because winning is itself evidence that your estimate was the most upward-biased of the N, an agent that commits resources sized to its own signal earns NEGATIVE expected profit (the curse), and the cure is an N-dependent order-statistic shading of the bid.

## Constraints honored
- Append-only outbox: the PROPOSAL 101 block is appended newest-last; no prior block edited.
- Claim placed before the authoring work (control/claims/proposal-101-winners-curse-task-auction.md).
- Neutral heartbeat; no cross-seat inbox edits (ORDER 018 is appended as the inbox's writer only, per this slice's task).
- Born-red: this card is the session's first commit at `in-progress` and flips to `complete` last, after the heartbeat — the PR stays red until the flip, then the installed merge-on-green workflow lands it (this session casts ZERO merge verbs).

## What happened
Round-23 FLEET opener P101 "the winner's curse in a common-value task auction" DRAFTED + fanned to sim-lab (P101 → V114, +13). Idea filed at ideas/fleet/winners-curse-task-auction-2026-07-17.md (`> **State:** sim-ready`); committed stdlib-only reference verifier ideas/fleet/winners_curse_task_auction.py (random, math, json, hashlib); outbox PROPOSAL 101 block appended (append-only); claim placed. Also landed ORDER 018 (owner's 2026-07-17 overnight continue-working directive, captured VERBATIM — the classifier-declined summary problem of ORDER 016 did not recur here) on the inbox bus, and updated the heartbeat.

Pre-registered gates (deterministic Monte-Carlo dry-sim, all ≥3σ, APPROVE iff G1 ∧ G2 ∧ G3):
- G1 (winner's curse): naive own-signal commitment yields NEGATIVE mean winner profit at ≥3σ. Dry-sim mean_naive = −0.778285 (se 0.000443), z = −1755.27 — PASS.
- G2 (order-statistic shading cures it): shaded policy (bid − w·(N−1)/(N+1)) beats naive by ≥3σ AND not significantly negative. Dry-sim mean_shaded = −0.000250 (break-even), z_vs_naive = 1238.54 — PASS.
- G3 (analytic-anchor match): sim naive mean profit vs closed form −w·(N−1)/(N+1) = −0.777778, |z| < 3. Dry-sim |z| = 1.14 — PASS.

Pinned world: N_BIDDERS=8, W_NOISE=1.0, V_TRUE=10.0, N_AUCTIONS=200000, sweep N∈{2,4,8,16}, SEED=20260717; derived shade* = w·(N−1)/(N+1) = 0.777778. Descriptive sweep confirms the curse deepens monotonically with rival count: N=2 → −0.333, N=4 → −0.600, N=8 → −0.778, N=16 → −0.883, each matching its closed form. Verifier exit 0; **results-dict sha256 = df79ddf35990ae250d096ada20a7f10d1e5320b2f83f49fc551d97415b98eb54** (verified deterministic — byte-identical digest across repeated invocations). Source read firsthand: Capen, Clapp & Campbell 1971 (JPT) + Milgrom & Weber 1982 (Econometrica).

## ⟲ Previous-session review
Previous-session review: the prior slice drafted the round-22 UNRELATED closer P100 (Kelly overbet ruin) and it LANDED — PR #492 is the current origin/main HEAD (9e8cd78) — closing round-22 on the proposal side (fleet P097↔V110, venture P098↔V111, game P099↔V112, unrelated P100↔V113). The baton recorded next = VERDICT 113 for P100 (a sibling session has claimed V113 via the open PR #493), then round-23 reopening at the FLEET slot with P101; this slice picked up that fleet opener with zero re-derivation. Records were clean at HEAD 9e8cd78 (git ls-remote origin main matched). Carried friction: a stale claim control/claims/proposal-099-shop-reroll-ruin.md is unparseable (check_claims advisory) — pre-existing, not this slice's, flagged for a successor prune; my own claim parsed clean (no new duplicate-scan warning). The failsafe cron stays armed and coordinator-bound (no re-arm from this seat); this slice recorded the failsafe id correction (N-variant → K-variant) and the owner-ordered deletion of the old-seat duplicate failsafe trig_01DQu7LbHvP8ZqC31douQTAe in the heartbeat.

## 💡 Session idea
The winner's curse is a runtime discipline for the fleet's OWN selection rules, not just a betting-desk anecdote: any time the fleet hands a common-value resource to the EXTREME of many noisy-but-unbiased estimates — dispatching a task to the seat that bid it cheapest, routing a lead to the most-confident agent, letting the highest-confidence model win an ensemble vote — the selected estimate is optimistic by an order-statistic gap that widens with the number of RIVALS, so shade the winning commitment by ≈E[max noise over N rivals] (or set a reserve / require independent corroboration), scaling the correction with rival count rather than own-estimate quality. Named follow-ups (out of scope here): (a) wire a concrete claim-shading rule into a lane's dispatch/auction with the shade tied to live rival-count; (b) a heterogeneous-signal-quality variant (bidders with different noise widths — does the curse concentrate on the noisiest bidder, and does that make it the systematic winner?); (c) an affiliated/correlated-value variant (Milgrom-Weber) where signals aren't independent, testing whether correlation deepens or softens the curse. Dedup: distinct from P100 Kelly (single-agent multiplicative compounding, ensemble-vs-time gap) and P096 friendship-paradox (degree-biased sampling on a static graph) — this is a single-shot MULTI-agent order-statistic SELECTION bias in a common-value auction.

## Grounding
TRUTH bar: every gate margin is measured from the committed dry-sim (SEED=20260717), not asserted; grounding cites idea-engine@9e8cd78 · fetched 2026-07-17T22:51:57Z. Outbox append-only; idea file append-only (no rewrites). Claim staked before content. This repo edits no sim-lab files (routing is the manager's per Q-0260). Prior fleet/unrelated heads (P100 Kelly, P099 shop-reroll, P096 friendship-paradox, P092 Braess, P097 long-chain) checked for non-adjacency — no prior prices a common-value auction / winner's curse / order-statistic bid-shading.

📊 Model: opus-4.8 · high · idea/planning
