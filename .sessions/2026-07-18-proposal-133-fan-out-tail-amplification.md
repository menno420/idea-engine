# PROPOSAL 133 — fan-out tail amplification (round-31 FLEET slot)

> **Status:** `complete`
> 📊 Model: Claude Opus · high · idea/planning

Born-red HOLD released: this card held the PR red from its first commit until the slice was complete and verified; flipping to `complete` here releases the landing workflow.

## Objective

Draft and land round-31 FLEET-slot PROPOSAL 133 — fan-out tail amplification: a scatter-gather request that waits for all N independent leaves inherits slow-tail probability P_slow(N) = 1 − (1−p)^N, so a 1%-per-leaf tail makes the median of a ~69-way fan-out slow (crossover N* = ln2/(−ln(1−p)) ≈ 0.693/p). Ship a markdown-first card, a committed stdlib verifier, three pre-registered ≥3σ gates, and a disclosed results-dict sha256. VERDICT 146 (P133 → V146, +13) is the next independent slice, not written here.

## Constraints honored

- Markdown-first card + committed stdlib verifier (hashlib/json/math/random only), SEED=20260717, ≥3σ gates on independently-computed closed forms.
- Deterministic: byte-identical double run, exit 0, disclosed results-dict sha256 `4b3de50…31c42d` (WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY posture).
- Born-red first commit → PR #568 READY at once → flip complete last, after the heartbeat.
- Outbox PROPOSAL 133 block appended once per grammar (+13 offset → V146); did NOT write the verdict.
- Deduped against all ideas/ cards + full outbox history — distinct from [[hedged-request-tail-cure]] (the cure).

## What happened

Synced to origin/main HEAD 2671e47 (round-30 complete: P129–P132 / V142–V145). Claimed P133, branched `claude/proposal-133-fan-out-tail-amplification`, opened PR #568 READY on the born-red card. Committed the verifier; the dry run passed all three gates (G1 z=−0.336, G2 z=−0.015 with N*=69 bracketed, G3 z=+0.055), N*=69, sha256 4b3de50…31c42d identical across two runs. Authored the fleet card, appended the outbox block, updated the heartbeat (proposal HW → P133; baton → V146 then round-31 VENTURE-slot P134), then flipped this card to release the landing workflow.

## ⟲ Previous-session review

The round-30 closer (P132 birthday-collision √N, PR #565; V145 mirror #566) landed clean on the whole-dict / no-self-field / stdout-only digest posture and the +13 offset held unbroken (P131→V144, P132→V145). This slice inherits that posture verbatim and continues the rotation into the round-31 FLEET slot. No regressions observed; the born-red HOLD behaved exactly as designed — substrate-gate stayed red until the flip.

## 💡 Session idea

The crossover formula N* ≈ 0.693/p is a ready-made **provisioning tripwire**: for any wait-for-all fan-out, the moment N approaches 0.693/p the request-level median crosses into "slow" — a one-line guard (`warn if shard_count × per_leaf_tail > 0.5`) catches the degradation before p50 moves. Candidate follow-up: pair this phenomenon with the hedged-request cure into a single "fan-out tail budget" playbook card.

## GROUNDING

- Verifier (firsthand, ground truth): https://github.com/menno420/idea-engine/blob/main/ideas/fleet/fan_out_tail_amplification.py — results-dict sha256 4b3de5012a6cedc99de8e446c3fdd0aa79b1988fd0594c3cbb9e33702131c42d, SEED=20260717.
- External reference (reachable): Dean & Barroso, "The Tail at Scale," Communications of the ACM 56(2):74–80, 2013 — https://web.archive.org/web/https://dl.acm.org/doi/10.1145/2408776.2408794.
- HEAD at start: 2671e4703b34e9c90d12d41a4f324a8024a8a273. PR: #568.
