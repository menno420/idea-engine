# Session — v101 pipeline: VERDICT 101 (P088, Berkson admission-collider anticorrelation trap — a disjunctive selection gate induces a spurious novelty–rigor tradeoff) via sim-lab → outbox V101 fan-in mirror + heartbeat + claim.

> **Status:** `in-progress`
> 📊 Model: opus-class · high effort · verdict-mirror task-class
> **Model/time:** opus-class · high · verdict-mirror · 2026-07-16 (a dispatched session for the coordinator seat — the verify half / fan-in mirror of PROPOSAL 088: the sim runs sim-lab-side on sim-lab PR #173.)

*(card born in-progress as the designed session-gate HOLD — the born-red first
commit; it FLIPS to `complete` as the deliberate LAST step after the fan-in +
heartbeat land. Task-class verdict-mirror: this session's core work is verifying
the sim-lab verdict landing and mirroring the finalized APPROVE record — the sim
itself runs sim-lab-side on sim-lab's own PR #173; this repo edits only itself,
Q-0260.)*

## Objective

Run the V101 pipeline under standing owner ORDER 003/004 with the EAP frame
(ORDER 015, through 2026-07-21) as the standing context:

1. **VERDICT 101** — the sim-lab-finalized verdict on PROPOSAL 088 (the round-18
   COMPLETELY-UNRELATED-domain CLOSER slot, Berkson admission-collider
   anticorrelation trap, `ideas/fleet/berkson-admission-collider-2026-07-16.md`,
   outbox block `## PROPOSAL 088 · status: sim-ready`, SEEDLESS — no seed baton
   consumed) mirrored into this repo's append-only ledger. The sim rides sim-lab
   PR #173; this card covers the idea-engine fan-in slice. Offset +13
   twenty-fourth-plus row (P086 → V099, P087 → V100, P088 → V101).
2. **Close-out (this branch)** — VERDICT 101 fan-in appended to
   `control/outbox.md` (append-only, real `date -u`, V100-grammar mirror block;
   proposal blocks never edited), heartbeat re-stamped on `control/status.md`
   (heartbeat-last discipline; seed baton: P088 SEEDLESS, next free block stays
   20261730), the mirror claim `control/claims/v101-berkson-mirror.md` carried,
   and this card's flip to `complete` as the deliberate last step.

## What happened

The sim-lab side (PR #173, merged) built an independent, deterministic,
stdlib-only re-implementation of the Berkson admission-collider fixture: each
candidate item carries two INDEPENDENT latent quality axes — novelty N and rigor
R, each drawn iid ~ Normal(0,1) from SEPARATE PRNG streams (a per-axis +10000
offset) so corr(N,R) = 0 by construction; admission uses a DISJUNCTIVE collider
gate (admit iff N ≥ a OR R ≥ b), and the induced correlation is read OFF the
admitted cohort. The sim ran twice → byte-identical, with twin independently
written decision evaluators. This idea-engine slice is the fan-in half: it does
NOT re-run the sim (this repo edits no other repo — Q-0260) and does NOT
recompute the numbers — it MIRRORS the finalized sim-lab APPROVE record, carrying
the sim-lab drafter's numerals verbatim, into this repo's append-only ledger.
Concretely: a `## VERDICT 101` block appended to `control/outbox.md` addressed to
the fleet manager (Q-0264 fan-in) in the VERDICT 100 mirror grammar, the
`control/status.md` heartbeat overwritten (heartbeat-last), the mirror claim, and
this card. The P088 proposal block is NOT edited — this outbox is append-only and
prior verdicted proposals keep their original status lines; the VERDICT 101 block
IS the status-flip record for PROPOSAL 088.

## Results

**VERDICT 101 = APPROVE** — the pre-registered rule (APPROVE iff R1∧R2∧R3∧R4,
evaluated in order R1→R2→R3→R4; else REJECT at the first failing gate) fired
**APPROVE with first-failing gate None**. Gate outcomes: **R1 PASS · R2 PASS ·
R3 PASS · R4 PASS**.
- **R1 PASS (null anchor — the two axes are independent by construction)** — the
  full-population pooled correlation ρ_full = +0.000251 ± 0.004738 sits inside
  the registered null band (|mean| + 3·SE = 0.0145 ≤ 0.03). No correlation exists
  before selection.
- **R2 PASS (the trap — the disjunctive collider induces a spurious NEGATIVE
  correlation among the admitted)** — at the 25% admission stringency
  ρ_OR@25% = −0.587329 ± 0.006550, clearing the pre-registered ρ* = −0.45 by
  **20.97σ**. Selecting on "at least one strong axis" manufactures an illusory
  novelty–rigor tradeoff.
- **R3 PASS (dose-response — the collider anticorrelation strengthens
  monotonically as admission TIGHTENS)** — ρ_OR over {50%, 25%, 10%} =
  [−0.457816, −0.587329, −0.685281], strictly more negative at each tightening;
  adjacent separations 14.34σ (50%↔25%) and 8.92σ (25%↔10%).
- **R4 PASS (mechanism-isolation — the DISJUNCTION is the sole cause)** — the
  single-gate control (admit on N ≥ a ALONE) shows ρ_single@25% = −0.013478 ±
  0.011502, within the null band and statistically indistinguishable from zero;
  the separation from the disjunctive gate |ρ_OR − ρ_single| = 0.5739 clears at
  **43.35σ**. Removing the OR removes the effect.

Both independently written decision evaluators agree APPROVE/None; self-checks
exit 0 on the accepted run; the sim ran twice byte-identical. The sim landed as
sim-lab PR #173 (merged). This branch: claim + born-red card (this FIRST commit)
→ outbox fan-in + heartbeat → card flip to `complete` = the deliberate last
commit.

## Constraints honored

- control/inbox.md untouched (manager-written); newest ORDER is 015 (EAP through
  2026-07-21) — no `new` ORDER outranks the standing pipeline baton; standing
  ORDER 003 (continuous pipeline) + ORDER 015 (no-re-arm) live; ASK 005 / ASK
  006 carried.
- control/outbox.md append-only: `## VERDICT 101` collision-grepped clean at
  boot; nothing above the newest block (PROPOSAL 088) touched. The P088 proposal
  block is NOT edited.
- Mirror claim `control/claims/v101-berkson-mirror.md` added; nothing under
  `ideas/` edited.
- No merge actions from this seat: commit + push + open PR only; no makerbench
  build. This repo edits only itself (Q-0260); the sim-lab PR #173 is the
  sibling-repo record, merged sim-lab-side.
- No triggers/routines armed, deleted, or audited; no send_later.
- Timestamps real `date -u`; model recorded family-level only; no exact model
  identifier in any commit/PR/card text.
- GitHub exclusively via MCP tools; files staged explicitly, never
  `git add -A`/`.`; guard-fires.jsonl left uncommitted.

<!-- TODO(flip): ⟲ Previous-session review — fill on the completion commit (the P088 → sim-lab #173 landing slice) when the card flips to `complete`. -->

<!-- TODO(flip): 💡 Session idea — fill on the completion commit; carry the family-level `📊 Model:` footer line at flip. -->
