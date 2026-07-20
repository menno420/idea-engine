# PROPOSAL 096 — friendship-paradox epidemic sensors: watch a random FRIEND, not a random person, and you see the wave first — the head-start equals the degree variance Var[k]/E[k] (round-21 UNRELATED-domain closer, P096 → V109, +13)

> **Status:** `complete`
> 📊 Model: agent · effort high · task-class proposal-draft

Born in-progress as this session's first commit (born-red HOLD); flips to complete as the deliberate last step after the heartbeat, releasing the landing workflow.

## Objective
Close round 21 of the ORDER 003 pipeline at the UNRELATED-domain slot (rotation fleet→venture→game→unrelated; the round-21 fleet opener was P093, the venture slice P094, the game slot P095, so the completely-unrelated closer is next per ORDER 004 rule 3). Draft one genuinely new, counterintuitive, stdlib-simulable head outside fleet/venture/game — network epidemiology / size-biased sampling (the friendship paradox as a free early-warning sensor) — ground it firsthand, pre-register four gates on a committed pinned world with a disclosed stdlib verifier spec, dry-sim to calibrated margins, and route it sim-ready to sim-lab as VERDICT 109 (+13 offset).

## Constraints honored
- Append-only outbox: `## PROPOSAL 096` appended once; no prior entry edited.
- Claim placed before the work (control/claims/friendship-paradox-sensor.md); no collision on this slug/scope (existing claims are bt-controller-plan and verdict-108-rubber-band-controller).
- Idea head placed in ideas/fleet/ per the check_sections cross-cutting carve-out for pure-mechanism heads (the P076/P080/P084/P088/P092 unrelated-closer precedent).
- Grounded firsthand on the Feld 1991 friendship-paradox formula and the Christakis & Fowler 2010 social-network-sensor result (fetched 2026-07-17T13:11:31Z); model-dependence disclosed (P024 discipline) — the pinned world is a committed construction, the verdict tests the size-biased-reach mechanism.
- Gates pre-registered on a seeded deterministic dry-sim; corrections disclosed (SI vs SIR, θ/interpolation, β raised 0.02→0.08 for a robust operating point, configuration-model stub-drop).
- Neutral heartbeat; no cross-seat inbox edits; guard-fires.jsonl left uncommitted (classifier wall).

## What happened
Drafted PROPOSAL 096 (idea file + outbox block) at the round-21 UNRELATED slot: monitoring a random FRIEND of a random person (a degree-biased sample needing no network map) detects a spreading contagion earlier than an equal-size random sample, with the expected head-start equal to the degree variance Var[k]/E[k] (Feld 1991). Pinned world: Barabási–Albert graph (n=10000, m=3, seed 20260717, committed moments E[k]=5.9988 / E[k²]=110.253 / Var[k]=74.267 / max degree 378) as the signal world W1, plus a degree-matched random 6-regular graph as the negative control W0; discrete-time SI diffusion (β=0.08), size-S=100 friendship-paradox (half-edge) vs random sensor groups, θ=0.30 detection threshold, T=200 trials. Four pre-registered gates: R1 (analytic anchor, FP mean sensor degree = E[k²]/E[k]=18.379 within 2% — dry-sim 18.399, relerr 0.11%); R2 (BA mean lead > 0 at ≥3σ — dry-sim +1.052 steps, 18.4σ, frac(lead>0)=0.76); R3 (regular-graph lead NOT ≥3σ — dry-sim +0.052 steps, 0.75σ); R4 (pinned-moment/sanity consistency, exact). Dry-sim APPROVE. Routed sim-ready to sim-lab for VERDICT 109 (+13 offset).

## ⟲ Previous-session review
Previous-session review: the prior slice closed the round-21 GAME loop P095 → VERDICT 108 (catch-up rubber-band as a proportional feedback controller, APPROVE; sim-lab PR #181 merged head 6ecb0de, idea-engine VERDICT 108 mirror landed to the fleet manager) and rolled the baton to the round-21 UNRELATED closer P096. That card's 💡 named an N-racer field head and a nonlinear/saturating-boost head as game-lane follow-ups; per the fleet→venture→game→unrelated rotation (ORDER 004 rule 3) this session instead opens the UNRELATED slot with a mechanistically distinct head — the first proposal where a sampling bias is a FEATURE to exploit (a free map-less sensor) rather than an artifact to correct (P084 Simpson's / P088 Berkson). Records were clean at HEAD f3473eb; the failsafe cron stays armed (coordinator-managed, no re-arm).

## 💡 Session idea
Next baton after V109: the three named follow-ups this head opens — (F1) sweep β and network family (configuration-model power-law, small-world) to map lead-time vs Var[k]/E[k]; (F2) test the field nomination method (random neighbour of a random node) against the exact half-edge draw to quantify the degree-correlation penalty; (F3) an SIR variant with recovery to check robustness under waning. All three reuse the same pinned-world diffusion kernel and are the named follow-ups in the P096 outbox block. Round 22 restarts the rotation at the fleet opener.

📊 Model: agent · effort high · task-class proposal-draft
