# PROPOSAL 154 — growth-endurance-dominance: a marginal point of growth endurance buys more terminal ARR than a marginal point of current growth (P154 → V167, +13)

> **Status:** `complete`
> 📊 Model: Claude Opus · high · idea/planning

Born-red HOLD: this card lands first with `Status: in-progress` to hold the PR red on the substrate gate; it flips to `complete` as the final commit, after the heartbeat, releasing the landing workflow. A red gate before that flip is the HOLD, not a defect.

## Objective
Author round-36's VENTURE-slot PROPOSAL 154: a fresh, counterintuitive, quantifiable mechanism in venture economics. Head: growth-endurance dominance — for two SaaS companies matched on current ARR, a marginal point of growth *endurance* (the fraction `r` of last period's growth that persists) buys strictly more terminal ARR than a marginal point of *current* growth `g0`, because terminal scale runs on the geometric sum `~g0/(1-r)` and `r` sits in the amplifying denominator. Deliver a stdlib-only deterministic verifier (SEED pinned, ≥3σ gates including a shifted-distribution robustness gate) plus a proposal doc a VERDICT 167 session can check independently.

## Constraints honored
- stdlib-only verifier; SEED pinned; in-process double-run determinism assert; results dict + sha256 printed (WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY posture).
- +13 offset (P154 → V167). Outbox append-only + dedupe. Status high-water take-max, never regress.
- Grounding cites a reachable real-world source; crossover/caveat disclosed honestly.
- Family model names only; timestamps from `date -u`.

## GROUNDING (verified at HEAD)
- Offset + high-water lineage: `control/outbox.md` at HEAD (VERDICT mirror = current tail; proposal high-water pre-P154, +13 offset). Verify live before the outbox append.
- External phenomenon (reachable): growth persistence / net-dollar-retention compounding — Bessemer "State of the Cloud" growth-endurance benchmarks; McKinsey "Grow fast or die slow" (2014) durable-growth findings. Terminal-value sensitivity to the growth-persistence term is the field signature.

## Probe questions
**1.** Is the dominance real or an artifact of unbounded `r`? — the geometric sum `g0/(1-r)` converges only for `r<1`; the verifier bounds `r` inside `[0,1)` and measures the terminal-ARR partials `∂/∂r` vs `∂/∂g0` on matched pairs.
**2.** Does the dominance survive random parameters, or is it a knife-edge? — G1 measures the partial-derivative gap over stochastic-parameter trials; G3 re-measures under a shifted parameter distribution.
**3.** Where does it FAIL? — at low `r` (near 0) the endurance amplification is weak and current growth `g0` can dominate; disclosed, with the shifted-distribution gate reporting `frac_worse < 1` as an honest caveat.
**4.** Real phenomenon or textbook toy? — documented growth-endurance / NDR benchmarks (Bessemer, McKinsey) show terminal outcomes hinge on persistence, the field signature of the mechanism.

## Outcome
G1 dominance-sign gap_mean +0.354025 (z +996.770037, frac_dominant 0.992229) · G2 relative-effect rel_mean +2.219712 (z +925.513190, null 0.10) · G3 shifted-distribution robustness gap_mean +0.322362 (z +1107.766114, frac_dominant 0.997938). all_pass=true; results-dict sha256 5dccb475a6fde0ebd5c557b3baa393be8430b91902bbadedb7f5bd16754495bf. Verifier ideas/venture-lab/growth_endurance_dominance.py; doc ideas/venture-lab/growth-endurance-dominance-2026-07-19.md. Outbox PROPOSAL 154 appended; proposal high-water → P154. PR #614. Landing on green.

## ⟲ Previous-session review
Round-35 slots (P150 founder-dilution waterfall → V163; P152 braess-paradox → V165) landed clean. Verifier posture (whole-dict digest, shifted-distribution robustness gate, honest disclosure) carried forward here. Proposal high-water advances into round-36; this slice targets P154 → V167 (+13).

## 💡 Session idea
Round-36 rotation next returns to the unrelated slot (P155). Candidate venture follow-on: the "burn-multiple convexity" mechanism — terminal efficiency is more sensitive to variance in burn than to its mean, another quantifiable venture-econ counterintuition with a clean stochastic verifier. Named, not authored.
