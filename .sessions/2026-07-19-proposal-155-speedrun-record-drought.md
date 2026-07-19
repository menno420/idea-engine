# PROPOSAL 155 — speedrun-record-drought: lifetime record count follows the harmonic number, so records slow logarithmically and distribution-free (P155 → V168, +13)

> **Status:** `in-progress`
> 📊 Model: Claude Opus · high · idea/planning

Born-red HOLD: this card lands first with `Status: in-progress` to hold the PR red on the substrate gate; it flips to `complete` as the final commit, after the outbox block, releasing the landing workflow. A red gate before that flip is the HOLD, not a defect.

## Objective
Author round-36's GAME-slot PROPOSAL 155: a fresh, counterintuitive, quantifiable mechanism in game/play statistics. Head: in any i.i.d. sequence of attempts the k-th attempt is a new record with probability exactly 1/k, independent of the value distribution, so after N attempts the expected number of personal-best records is the harmonic number H_N ≈ ln N + γ. Consequence for speedrunning: records accumulate only logarithmically — to DOUBLE a lifetime record count you must roughly SQUARE the attempt count, and the drought between PBs grows without bound. The late-run "wall" is not a skill plateau; it is the arithmetic of running extrema, and it is identical whether attempt times are Gaussian, exponential, or heavy-tailed. Deliver a stdlib-only deterministic verifier (SEED pinned, ≥3σ gates including a distribution-free robustness gate) plus a proposal doc a VERDICT 168 session can check independently.

## Constraints honored
- stdlib-only verifier; SEED pinned; in-process double-run determinism assert; results dict + sha256 printed (WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY posture, floats 6 dp).
- +13 offset (P155 → V168). Outbox append-only + dedupe. Proposal high-water take-max, never regress.
- Grounding cites a reachable real-world source; distribution-free/caveat disclosed honestly.
- Family model names only; timestamps from `date -u`.

## GROUNDING (verified at HEAD)
- Offset + high-water lineage: `control/outbox.md` at HEAD (PROPOSAL 154 = current tail; proposal high-water pre-P155, +13 offset). Verify live before the outbox append.
- External phenomenon (reachable): theory of records — the probability that the n-th i.i.d. observation is a record is 1/n and E[records] = H_n (Renyi 1962; Glick 1978, "Breaking Records and Breaking Boards," American Mathematical Monthly; Arnold-Balakrishnan-Nagaraja 1998, "Records"). Speedrun world-record attrition is the field signature.

## Probe questions
**1.** Is the harmonic law real or an artifact of the chosen distribution? — record indicators are Bernoulli(1/k) by exchangeability of i.i.d. ranks; the verifier draws actual attempt times and detects running-minimum records, gating the MC record count against H_N.
**2.** Is the log-slowdown a knife-edge or robust? — G2 compares a small horizon n1 and n2 = n1 squared; the linear-accumulation null (records proportional to attempts) is rejected at >=3 sigma while the observed ratio matches H_{n2}/H_{n1} ~ 2.
**3.** Does skill-distribution shape matter? — G3 re-measures the record count under a different base distribution (heavy-tailed) and gates it against the SAME H_N, confirming record cadence is a rank property, not a value property.
**4.** Real phenomenon or textbook toy? — documented record theory plus speedrun record attrition; the log-cadence is observed wherever i.i.d. attempts chase a running best.

## Outcome
Landing on green — verifier + doc committed; gate z-scores, results-dict sha256, and PR number recorded on the complete-flip commit. Verifier ideas/superbot-games/speedrun_record_drought.py; doc ideas/superbot-games/speedrun-record-drought-2026-07-19.md.

## ⟲ Previous-session review
Round-36 FLEET-slot P153 (Kleinrock conservation law → V166) and VENTURE-slot P154 (growth-endurance dominance → V167) landed clean. Verifier posture (whole-dict digest, distribution robustness gate, honest disclosure) carried forward here. This slice fills round-36's GAME slot: P155 → V168 (+13); the rotation's UNRELATED slot (P156) follows.

## 💡 Session idea
Named, not authored: a records follow-on — the "record-value gap" mechanism (the expected IMPROVEMENT at each new record shrinks, and for heavy-tailed attempt distributions the gaps need not shrink at all), a distinct quantifiable record-statistics counterintuition with a clean stochastic verifier.
