# PROPOSAL 098 — the referral-bonus value trap (round-22 venture slot, P098 → V111, +13)

> **Status:** `complete`
> 📊 Model: opus-4.8 · high · proposal-draft

Born in-progress as this session's first commit (born-red HOLD); flips to complete as the deliberate last step after the heartbeat, releasing the landing workflow.

## Objective
Draft and land the round-22 VENTURE-slot proposal (P098): one genuinely new, counterintuitive, stdlib-simulable venture-economics idea with an analytic anchor and pre-registered ≥3σ gates, fanned to sim-lab as VERDICT 111 (+13).

## Constraints honored
- HARD-SYNC both repos to origin HEAD (idea-engine 4de68f4, sim-lab 991edec) before reading; inbox@HEAD read in both — no new order outranks this task (ORDER 016 = this backlog; 017 owner-review-parked; sim-lab ORDER-010(c) parked).
- `python3 bootstrap.py check --strict` green (exit 0) before work.
- Claim filed before work; born-red card is the first commit (HOLD); PR READY immediately; heartbeat before flip; Status→complete is the last commit.
- Analytic anchor (branching-process geometric series) + dry-sim-calibrated gates at ≥3σ; correction disclosed (near-critical variance blow-up → subcritical cap). Model lines family-level (ORDER 012).

## What happened
- Idea: the referral bonus that maximizes viral coefficient R0 is strictly larger than the profit-maximizing bonus — "tune for maximum virality" overspends because signups scale as S/(1−R0) and you pay the bonus to the exploding referred population.
- Subcritical Galton–Watson model; pinned world SEED=20260717, S=1000, K=3, q_max=0.25, b0=2.0, M=10.0, N=2000; b*=4.5 (R0=0.671) vs b_viral=8.0 (R0=0.736), ~27% profit lost at virality-max.
- Dry-sim (stdlib-only verifier, exit 0): R1 anchor |z|=1.16σ, R2 interior z=757.29σ/62.75σ, R3 value-trap z=335.89σ — all PASS. Results sha256 5438482c51479370e2a80aef0a01d3fe7f5617dcc1d30a622c9e74e1c8436786.
- Idea file ideas/venture-lab/referral-bonus-value-trap-2026-07-17.md (State: sim-ready) + committed reference verifier; PROPOSAL 098 appended to control/outbox.md; claim filed; heartbeat updated.

## ⟲ Previous-session review
Round-22 FLEET opener P097 "the long chain" DRAFTED + VERDICTED APPROVE (P097 → V110, +13, idea-engine #486 / sim-lab #183) — the 9th consecutive APPROVE. Verified terminal-merged before pruning its claim. P098 continues the rotation at the venture slot.

## 💡 Session idea
The 1/(1−R0) branching amplifier is a double-edged lever: the same factor that multiplies your cascade multiplies your per-referral bonus bill. A reusable "value trap" template — any growth lever with a saturating response and a per-unit cost paid across an amplified population has a profit optimum strictly inside the metric-maximizing setting. Candidate future proposals: paid-acquisition bid caps under LTV amplification, affiliate-commission tiers.

📊 Model: opus-4.8 · high · proposal-draft
