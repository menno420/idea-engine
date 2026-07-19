# PROPOSAL 152 — braess-paradox: adding a zero-cost shortcut to a congested network raises everyone's equilibrium travel time (P152 → V165, +13)

> **Status:** `complete`
> 📊 Model: Claude Opus · high · idea/planning

Born-red HOLD: this card lands first with `Status: in-progress` to hold the PR red on the substrate gate; it flips to `complete` as the final commit, after the heartbeat, releasing the landing workflow. A red gate before that flip is the HOLD, not a defect.

## Objective
Author round-35's UNRELATED-slot PROPOSAL 152: a fresh, counterintuitive, quantifiable mechanism outside fleet ops / venture econ / games. Head: Braess's paradox — in the canonical 4-node routing network under stochastic demand, the selfish (Wardrop) equilibrium travel time WITH a zero-cost A→B shortcut is strictly greater than WITHOUT it. Deliver a stdlib-only deterministic verifier (SEED=20260717, ≥3σ gates including a shifted-distribution robustness gate) plus a proposal doc a VERDICT 165 session can check independently.

## Constraints honored
- stdlib-only verifier; SEED pinned 20260717; in-process double-run determinism assert; results dict + sha256 printed (WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY posture).
- +13 offset (P152 → V165). Outbox append-only + dedupe. Status high-water take-max, never regress.
- Grounding cites a reachable real-world source; crossover/caveat disclosed honestly.
- Family model names only; timestamps from `date -u`.

## GROUNDING (verified at HEAD)
- Offset + high-water lineage: https://github.com/menno420/idea-engine/blob/80e432d2682e7b602138a91a8cabb14956f27b1c/control/outbox.md @ ae852cc89f270fbf1e3e5ec8822d5d0a2043bb37 (VERDICT 163 mirror = current tail; proposal high-water P150, +13 offset).
- External phenomenon (reachable): Braess (1968), "Über ein Paradoxon aus der Verkehrsplanung"; documented road removals that improved flow — Seoul Cheonggyecheon expressway (2003), Stuttgart, New York 42nd Street. Wikipedia "Braess's paradox".

## Probe questions
**1.** Is `t_with` the true Wardrop equilibrium, not merely a plausible route? — from the all-shortcut profile a unilateral switch to either fixed route costs `D/CAP + FIXED ≥ 2D/CAP` for `D ≤ FIXED·CAP`, so no driver gains; the piecewise form handles `D > FIXED·CAP`.
**2.** Does the paradox survive random demand, or is it a knife-edge at D=4000? — G1 measures the gap over 20k stochastic-demand trials; G3 re-measures under a shifted demand distribution.
**3.** Where does it FAIL? — below `D = 30·CAP = 3000` the shortcut actually helps (gap<0); disclosed, and the shifted-distribution gate reports `frac_worse < 1` as an honest caveat.
**4.** Real phenomenon or textbook toy? — documented physical road removals (Seoul, Stuttgart, NYC) raised throughput, the field signature of the paradox.

## Outcome
G1 gap_mean +14.983575 (z +572.883357, frac_worse 1.0) · G2 rel_mean +0.229465 (z +347.899519, null 0.10) · G3 shift gap_mean +7.492692 (z +236.126110, frac_worse 0.951250). all_pass=true; results-dict sha256 d0e4e57d3ecb455442d44b59ef09092c1ed3a66425501e3c7b18616384605ad0. Verifier ideas/fleet/braess_paradox.py; doc ideas/fleet/braess-paradox-2026-07-19.md. Outbox PROPOSAL 152 appended; proposal high-water → P152. PR #608. Landing on green.

## ⟲ Previous-session review
Round-35 venture-slot PROPOSAL 150 (founder-dilution liquidation waterfall) → VERDICT 163 APPROVE landed clean (idea-engine #607; sim-lab #237). Verifier posture (whole-dict digest, shifted-distribution robustness gate, honest disclosure) carried forward here. Proposal high-water P150; this slice advances it to P152 (P151 game-slot may land concurrently — take max).

## 💡 Session idea
Round-35 rotation next returns to the fleet slot (P153). Candidate unrelated follow-on: the inspection / waiting-time paradox (length-biased sampling — mean observed gap exceeds the true mean interval), another quantifiable everyday-systems counterintuition with a clean stochastic verifier. Named, not authored.
