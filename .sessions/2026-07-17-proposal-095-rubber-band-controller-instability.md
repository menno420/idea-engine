# PROPOSAL 095 — the catch-up rubber-band is a feedback controller, not a fairness dial: a boost proportional to the leader's gap has an INTERIOR-optimal strength, going unstable past the exact discrete-control stability boundary where outcomes decouple from skill (round-21 game slot, P095 → V108, +13)

> **Status:** `complete`
> 📊 Model: opus-4.8 · high · proposal-draft

Born in-progress as this session's first commit (born-red HOLD); flips to complete as the deliberate last step after the heartbeat, releasing the landing workflow.

## Objective
Open round 21 of the ORDER 003 pipeline at the GAME slot (rotation fleet→venture→game→unrelated; the round-21 fleet opener was P093 and the venture slice was P094, so this is the game slot per ORDER 004 rule 3). Draft a genuinely new, counterintuitive, stdlib-simulable game-mechanics idea and land it sim-ready for sim-lab VERDICT 108 (+13): a catch-up rubber-band boost proportional to the leader's gap is a discrete-time proportional feedback controller — engagement is NON-monotone in the gain k, peaking at an interior k* because a weak band lets the intrinsically faster racer open a persistent lead (decided-early boredom) while past the exact discrete-control stability boundary k=2 the loop goes unstable, the gap oscillates with diverging amplitude, and the winner decouples from skill (no-agency churn). The folk "stronger catch-up is strictly closer and strictly better" optimizes the visible steady-state lead g*=F/k and walks straight off the instability cliff.

## Constraints honored
- Append-only outbox: `## PROPOSAL 095` appended once; no prior entry edited.
- Claim placed before the work (control/claims/proposal-095-rubber-band-controller-instability.md); the terminal VERDICT 107 refund-window claim (idea-engine PR #479 + sim-lab PR #180 both merged, verified live) is pruned in this slice (housekeeping rider).
- SEEDLESS: pins a private SEED=20260719; the shared seed-ledger block 20261730 left untouched (P089–P094 precedent).
- Grounded firsthand on the game-mechanics idea tree (idea-engine@0e9f261, fetched this session); model-dependence disclosed (P024 discipline) — the dynamics are committed design choices, the verdict tests the internal control logic, not empirical magnitudes.
- Gates pre-registered on a seeded deterministic dry-sim, byte-identical double-run; one correction disclosed (the R4b stabilizer sign — velocity damping β=+0.5 DEstabilizes this recurrence, the correctly-signed lead term is β=−0.5, so R4b was re-registered as a cliff-relocation test before landing).
- Neutral heartbeat; no cross-seat inbox edits; guard-fires.jsonl left uncommitted (classifier wall).

## What happened
Drafted PROPOSAL 095 (idea file + outbox block) at the round-21 GAME slot and calibrated four pre-registered gates on a stdlib-only deterministic dry-sim (byte-identical double-run, results-dict sha256 573fa714ab524e11fa1b57a12d6083f135d80d47c147add62442297152c7b563, all five gate flags pass). Dry-sim APPROVE: R1 — the interior gain k*=1.4 dominates the weak endpoint k=0.2 by 1397.3σ and the past-instability endpoint k=2.2 by 1527.8σ; R2 — every k>2 diverges and the last stable gain k=1.95 outsells the first unstable k=2.05 by 239.9σ, with measured Var(g) matching the closed form σ²/(k(2−k)) to 0.5115% (the control-theory stability boundary made visible); R3 — sensor delay d=1 drops the Jury boundary to k=1 (argmax 0.7, divergence onset at k=1) and the optimum stays interior across s∈{0.3,0.5,0.7} (argmax [1.0,1.4,1.6]); R4 — dual control: s=0 collapses E to max|E|=0.00086 (skill-fidelity arm removed → interior peak gone), and the stabilizer boundary k_crit=2−2β is confirmed by the empirical divergence onsets [2.2,3.2,1.2] for β∈{0,−0.5,+0.5}. Twin evaluators agree APPROVE/None. One correction disclosed (R4b stabilizer sign). Housekeeping rider: pruned the terminal VERDICT 107 refund-window claim (idea-engine PR #479 + sim-lab PR #180 both verified merged live).

## ⟲ Previous-session review
The prior slice closed the P094→V107 loop (refund-window abuse-threshold, APPROVE; sim-lab PR #180 merged head f5c2df5, mirrored into this repo's ledger via idea-engine PR #479 at HEAD 0e9f261) and rolled the baton to the round-21 GAME slot. That card's 💡 suggested a refund-window × price joint optimizer and a heterogeneous-wardrobe-threshold head as the next venture-lane follow-ups; per the fleet→venture→game rotation (ORDER 004 rule 3) this session instead opens the GAME slot with a mechanistically distinct head — the first game idea to model a competitive-balance mechanic as a feedback control loop rather than a reward schedule (P091), a shared streak budget (P083), or a damage distribution (P087). The venture follow-ups remain available as named venture-lane heads.

## 💡 Session idea
Next baton after V108: an N-racer field head — does the pairwise instability boundary k=2 survive a pack of N>2 racers where every trailing racer is boosted (do the coupled loops destabilize earlier)? Plus a nonlinear/saturating boost head — does a soft cap on the catch-up boost round the k=2 cliff into an interior ridge (graceful degradation instead of divergence)? Both reuse the same delay-difference kernel and are the named follow-ups in the P095 outbox block.

📊 Model: opus-4.8 · high · proposal-draft
