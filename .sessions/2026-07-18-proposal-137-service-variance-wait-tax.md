# PROPOSAL 137 — service-variance wait tax (round-32 FLEET slot)

> **Status:** `complete`
> 📊 Model: Claude Opus · high · idea/planning

Born-red HOLD released: this card held the PR red from its first commit until the slice was complete and verified; flipping to `complete` here releases the landing workflow.

## Objective

Draft and land round-32 FLEET-slot PROPOSAL 137 — the service-variance wait tax: for an M/G/1 FIFO queue the Pollaczek–Khinchine mean-value law gives mean queue wait W_q = (ρ/(1−ρ))·E[S]·(1+C²)/2 with C²=Var(S)/E[S]² the squared coefficient of variation of SERVICE time, so at FIXED utilization ρ=0.8 and FIXED mean service E[S]=1.0 the wait depends ONLY on service-time variance — W_q = 2.0 (M/D/1, C²=0) / 4.0 (M/M/1, C²=1) / 10.0 (M/H2/1, C²=4), a 1:2:5 spread invisible to any utilization dashboard. Ship a markdown-first card, a committed stdlib verifier (SEED=20260717, exact Lindley recursion + method of independent replications, three ordered ≥3σ /se gates G1→G2→G3, whole-dict sha256), a real dry-sim, an outbox block (P137 → V150, +13), and a heartbeat update. VERDICT 150 (P137 → V150, +13) is the next independent slice, not written here.

## Constraints honored

- Markdown-first card + committed stdlib verifier (hashlib/json/math/random only), SEED=20260717, three ordered ≥3σ gates on the Pollaczek–Khinchine closed-form anchors (W_q = 2.0 / 4.0 / 10.0 exactly).
- Deterministic: byte-identical double run, exit 0, disclosed results-dict sha256 (WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY posture — no results_sha256 key, no on-disk JSON, stdout pretty dump distinct from the compact digest preimage).
- Method of independent replications for valid standard errors (Lindley waits are autocorrelated so naive std/sqrt(n) is invalid): R independent replications per distribution, each a warm-up-discarded run contributing ONE post-warmup mean W_q sample; sub-seeds drawn from a master random.Random(SEED) via getrandbits so no stream couples across reps.
- Born-red first commit → PR READY at once → flip complete last, after the heartbeat.
- Outbox PROPOSAL 137 block appended once per grammar (+13 offset → V150); did NOT write the verdict.
- Deduped against ideas/ + full outbox history — distinct from P089 variance-blind-provisioning-trap (SLA-violation rate + capacity-provisioning correction) and from inspection-paradox / correlated-fleet-variance-floor / checkout-pooling.

## What happened

Synced to origin/main HEAD 8c7d2b5 (round-31 CLOSED on both sides: proposals P133–P136, verdicts V146–V149; origin/main stayed at 8c7d2b5 through the whole slice — no sibling merge needed). Re-scanned control/claims/ and open PRs for a competing P137 — none (the only open PR is #527, VERDICT 126; the "137" hits are VERDICT 137 for P124 forward-references). Claimed P137, branched `claude/proposal-137-service-variance-wait-tax`, opened PR #577 READY on the born-red card (commit afe25ad). Committed the stdlib verifier + idea card + outbox P137 block (commit d8ac8d1): the real dry run passed all three ordered ≥3σ /se gates (G1 M/D/1 W_q measured 2.002221 vs exact 2.0 z=+0.496, G2 M/M/1 3.987717 vs 4.0 z=−0.934, G3 M/H2/1 9.921619 vs 10.0 z=−1.838), byte-identical across two runs, exit 0, results-dict sha256 ab44d56a22c24f83c4a2048af56dc3dbdbf462d3aa9990bd19c64426891e4307 (WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY posture). Authored the fleet-lane card (dedup draws the line vs P089 variance-blind-provisioning-trap: LAW vs the (1+CV²) capacity FIX), appended the outbox PROPOSAL 137 block (+13 → V150, offset cited from the predecessor P136 → V149 row + the status baton), updated the heartbeat (proposal high-water P136 → P137, verdict high-water held at V149, round-32 opens at the FLEET slot; baton → V150 for P137 then round-32 venture-slot P138; routines line unchanged coordinator-bound; commit e225995), then flipped this card to release the landing workflow. `python3 bootstrap.py check --strict` before the flip failed only on the designed born-red HOLD (claims-duplicate / owner-action / seat-digest advisories are never exit-affecting; preflight check_ideas --outbox passes once the outbox block names the card).

## ⟲ Previous-session review

The round-31 UNRELATED-slot CLOSER (P136 base-rate PPV collapse, PR #574; V149 mirror #575) closed round-31 on the proposal side and the +13 offset held unbroken (P133→V146, P134→V147, P135→V148, P136→V149 all landed on both sides). This slice inherits the whole-dict / no-self-field / stdout-only digest posture verbatim and OPENS round-32 by taking the FLEET slot (rotation unrelated→fleet). One continuity note carried forward: the verdict high-water V149 is non-contiguous — V137 for P124, V132 for P119, and V126 for P113 (idea-engine mirror #527) remain open below it, so V149 must not be read as "all lower verdicts closed".

## 💡 Session idea

The service-variance wait tax (P137, the pure P-K queue-WAIT law) and P089's variance-blind-provisioning-trap (the SLA + capacity-correction consequence) are the same (1+C²)/2 factor seen from two ends: P137 states the LAW (wait scales with service-time variance at fixed ρ, E[S]); P089 states the OPERATIONAL FIX (provision by (1+CV²), not the mean). Candidate follow-up: a single "variance-tax" playbook card that chains the law → the tail (M/G/1 sojourn-tail, feeding fan-out P133) → the provisioning correction (P089) → the pooling cure (P044), so a fleet operator reads one thread from "why variance costs wait" to "what capacity/pooling lever removes it".

## GROUNDING

- Verifier (firsthand, ground truth): https://github.com/menno420/idea-engine/blob/main/ideas/fleet/service_variance_wait_tax.py — results-dict sha256 ab44d56a22c24f83c4a2048af56dc3dbdbf462d3aa9990bd19c64426891e4307, SEED=20260717, N_JOBS=600000, WARMUP=150000, REPLICATIONS=30.
- Idea card: https://github.com/menno420/idea-engine/blob/main/ideas/fleet/service-variance-wait-tax-2026-07-18.md
- External reference (reachable): Pollaczek–Khinchine mean-value formula — Kleinrock, Queueing Systems Vol.1 (1975) §5.6; https://en.wikipedia.org/wiki/Pollaczek%E2%80%93Khinchine_formula (M/G/1 mean queue wait explicitly depends on service-time variance) — verified reachable 2026-07-18.
- Grounding commit: https://github.com/menno420/idea-engine@8c7d2b5 · HEAD at start 8c7d2b5d333e97b35b85d754fb64c143c0fdfc37 · fetched 2026-07-18T15:07:28Z. PR: #577.
