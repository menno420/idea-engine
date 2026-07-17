# VERDICT 111 mirror — the referral-bonus value trap: the profit-optimal per-referral bonus b*=4.5 is strictly interior AND strictly below the virality-maximizing bonus b_viral=8.0, so tuning for maximum viral coefficient strictly overspends (P098, +13) — APPROVE

> **Status:** `in-progress`
> 📊 Model: opus-4.8 · high · verdict-mirror

Born in-progress as this session's first commit (born-red HOLD); flips to complete as the deliberate last step after the heartbeat.

## Objective
Fan-in to the fleet-manager (Q-0264) of sim-lab's independent VERDICT 111 verifying idea-engine PROPOSAL 098 (2026-07-17T15:47:53Z, sim-ready), offset +13 (P098 → V111), the round-22 venture slot. On a subcritical Galton–Watson referral cascade with saturating conversion q(b)=q_max·(1−e^(−b/b0)) and a bonus paid per successful referral, the profit-optimal bonus b*=4.5 is strictly interior AND strictly below the viral-coefficient-maximizing bonus b_viral=8.0 — signups scale as S/(1−R0) and the bonus is paid across that amplified referred population, so "tune for maximum virality" strictly overspends. Sim-lab side merged as PR #184 (sim-lab main 85f3948).

## Constraints honored
- Append-only outbox: the PROPOSAL 098 block is NOT edited; this VERDICT 111 mirror block IS its status-flip-to-verdicted record.
- HARD-SYNC to origin HEAD (idea-engine 04774f8) before reading; inbox left untouched (manager-owned).
- `python3 bootstrap.py check --strict` green (exit 0) before the flip push (control/** + .sessions/** ride the control fast-lane).
- Born-red card is the first commit (HOLD); claim + outbox mirror + heartbeat follow; Status→complete is the deliberate last commit. Model lines family-level (ORDER 012).

## Verdict
APPROVE — all three pre-registered gates pass in order R1→R2→R3, verdict never softened (first-failing-gate None).

- R1 branching-anchor match: PASS — |E_sim[T] − S/(1−m(b*))| = |3035.927 − 3039.057|, **|z| = 1.16σ** < 3σ — the simulated mean cohort size reproduces the analytic geometric-series anchor S/(1−m).
- R2 interior optimum: PASS — Π̄(b*)=21197.596 > Π̄(0)=10000.000 at **+757.29σ** AND > Π̄(B_HI=6.0)=19932.238 at **+62.75σ**, each ≥3σ — the profit optimum is strictly interior to the bonus grid.
- R3 value trap / headline: PASS — Π̄(b*)=21197.596 > Π̄(b_viral=8.0)=15575.369 by 5622.227 at **+335.89σ** ≥3σ — the virality-maximizing bonus loses ≈27% of profit versus the profit-optimal bonus.

Derived pinned-world anchors (SEED=20260717, S=1000, K=3, q_max=0.25, b0=2.0, M=10.0, N=2000, grid [0.0..8.0] step 0.1): b*=4.5 (R0=0.670951), b_viral=8.0 (R0=0.736263). Subcritical throughout (K·q_max=0.75<1).

## ⟲ Previous-session review
[[fill: one-line review of the close-out session #488 — added at flip]]

## 💡 Session idea
[[fill: one genuine new session idea — added at flip]]

[[fill: bottom 📊 Model line — added at flip]]
