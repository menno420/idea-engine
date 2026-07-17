# PROPOSAL 097 — the long chain: one secondary skill per lane, wired as a single ring, ≈ fully cross-trained lanes (round-22 fleet opener, P097 → V110, +13)

> **Status:** `in-progress`
> 📊 Model: opus-4.8 · high · idea/planning

Born in-progress as this session's first commit (born-red HOLD); flips to complete as the deliberate last step after the heartbeat, releasing the installed merge-on-green workflow to land the PR.

## Objective
Draft and fan in the round-22 FLEET-opener PROPOSAL 097 — "the long chain." Reason the process-flexibility result to its fuller form and register it as a pinned-world, pre-registered-gate proposal to sim-lab (P097 → V110, +13): give each of K=12 specialized lanes exactly ONE secondary category (a fixed 2-skills/lane budget); wired as a single long chain (lane i also covers cat i+1, closing the loop) the fleet recovers ~95% of the FULLFLEX−DEDICATED throughput gap — nearly all of full flexibility — while the SAME budget wired as disjoint buddy-pairs recovers only ~41%. Topology, not amount, is what matters.

## Constraints honored
- Append-only outbox: the PROPOSAL 097 block is appended newest-last; no prior block edited.
- Claim placed before the mirror/authoring work (control/claims/proposal-097-long-chain.md); the terminal VERDICT 109 claim (idea-engine PR #484 merged, verified live) is pruned in this slice.
- Neutral heartbeat; no cross-seat inbox edits.
- Born-red: this card is the session's first commit at `in-progress` and flips to `complete` last, after the heartbeat — the PR stays red until the flip, then the installed merge-on-green workflow lands it (this session casts ZERO merge verbs).

## What happened
Round-22 fleet opener P097 "the long chain" DRAFTED + fanned to sim-lab (P097 → V110). Idea filed at ideas/fleet/long-chain-flexibility-2026-07-17.md (`> **State:** sim-ready`); outbox PROPOSAL 097 block appended; claim placed. Harvest source read firsthand: Simchi-Levi & Wei 2012, Operations Research (INFORMS), plus Jordan & Graves 1995 (secondary) for the ≈-full-flexibility half.

Pre-registered gates (deterministic Edmonds-Karp max-flow dry-sim, all ≥3σ, APPROVE in order R1→R2→R3→R4):
- R1 (chain ≈ full): chain_recovery = (LONGCHAIN−DEDICATED)/(FULLFLEX−DEDICATED) ≥ 0.90. Dry-sim 0.9460, +52.76σ.
- R2 (real gap): FULLFLEX−DEDICATED served-fraction ≥ 0.02. Dry-sim 0.0992, +300.63σ.
- R3 (topology > budget): LONGCHAIN−BUDDYPAIRS ≥ 0.01 (identical 2-skill budget). Dry-sim 0.0528, +210.98σ.
- R4 (moderate-CV robustness): min chain_recovery over sd∈{0.30,0.35,0.40} ≥ 0.90. Dry-sim min 0.9155 (at sd 0.40), +14.79σ.

Pinned world: K=12 categories / K=12 lanes, lane capacity 1.0, per-category demand max(0, N(1.0,0.35)) i.i.d., served = Edmonds-Karp max-flow, N_REPS=20000, SEED=20260717. Dry-sim results-dict sha256 505321acb9ec94075a8f027ea1df27f50db84fcf31df56ea3a9586cf2f8c94ab. Disclosed sensitivity: at sd=0.50 recovery falls to 0.8537 (claim bounded to CV ≤ 0.40).

## ⟲ Previous-session review
The prior slice mirrored VERDICT 109 (friendship-paradox epidemic sensors, P096 → V109 APPROVE) and closed round-21 entirely (fleet P093→V106, venture P094→V107, game P095→V108, unrelated P096→V109); idea-engine PR #484 born-red HOLD held correctly and merged. This session opens round-22 at the FLEET slot (ORDER 004 rotation restarts at fleet): PROPOSAL 097 "the long chain" drafted + fanned to sim-lab as V110. The baton rolls to sim-lab VERDICT 110; the next proposal slot after fleet is the venture opener (P098).

## 💡 Session idea
The long chain is a runtime provisioning knob for the fleet's own lanes: when adding cross-training, wire each lane's one secondary skill as a single ring across the whole fleet rather than buddy-pairs — same training budget, ~2.3× the recovered throughput under balanced-but-random per-lane demand. The named follow-up (b), a CV-monitor that widens flexibility 2→3 skills only when per-category demand CV crosses ~0.45, gives the fleet manager a cheap trigger for when the sparse ring stops sufficing — the boundary the disclosed sd=0.50 degradation (0.8537) marks.

📊 Model: opus-4.8 · high · idea/planning
