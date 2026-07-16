# Session — v096 pipeline: VERDICT 096 (P083, combo grace-budget cliff) via sim-lab → outbox V096 mirror + heartbeat + card flip

> **Status:** `in-progress`
> **Model/time:** opus-class · high · simulation/verification · 2026-07-16 (a
> dispatched session for the coordinator seat — the verify half of PROPOSAL
> 083: run P083 (the round-17 GAME-MECHANICS slot — the combo/streak
> grace-budget cliff, superbot-games `games/mining/core/energy.py` shared-budget
> STRUCTURE transferred onto a proposed combo multiplier and priced against the
> sold forgiving-streak sentence) through sim-lab as VERDICT 096, then mirror
> the verdict into this repo's outbox and close out.)

*(card born in-progress as the designed session-gate hold; flips complete in
this PR's final commit after the pipeline work lands. Task-class
simulation/verification: this session's core work is verifying the sim-lab
verdict landing and mirroring the finalized record — the sim itself runs
sim-lab-side on sim-lab's own PR #168.)*

## Scope

Run the V096 pipeline under standing owner ORDER 003/004 with the EAP frame
(ORDER 015, through 2026-07-21) as the standing context:

1. **VERDICT 096** — run PROPOSAL 083 (combo grace-budget cliff,
   `ideas/superbot-games/combo-grace-budget-cliff-2026-07-16.md`, outbox block
   `## PROPOSAL 083 · 2026-07-16T14:28:18Z · status: sim-ready`, seeds
   20261726–729 with aux 20261729 never read) through sim-lab and register the
   verdict. The sim-lab side lands on its own sim-lab branch/PR (#168); this
   card covers the idea-engine slice. Offset +13 twentieth row (P082 → V095,
   P083 → V096; map in sim-lab docs/current-state.md § Verdict-numbering map —
   "Next expected: PROPOSAL 083 → VERDICT 096" confirmed at sim-lab main
   `35dc520`).
2. **Close-out (this branch)** — V096 mirror appended to `control/outbox.md`
   (append-only, real `date -u`, compact V095-grammar mirror block; proposal
   blocks never edited), close-out heartbeat on `control/status.md` (seed
   baton: P083 consumed 20261726–729, next free block starts 20261730), and
   this card's flip as the deliberate last step. This session's own claim
   `control/claims/2026-07-16-v096-combo-grace-cliff.md` rides this PR's first
   commit and STAYS at close for the successor to prune (the practiced
   prune-by-successor lifecycle; control/claims/README.md HOST-OWNED section).

## Results

**VERDICT 096 = REJECT** — the pre-registered rule fired on all four clauses
(R1 the folk belief made precise — the steady census {ℓ=0 survives; ℓ=1,2,3
break at 11, 6, 4} with the ℓ>G control at step 1; R2 the cliff position —
steady break_step == ⌊B0/ℓ⌋+1 exact; R3 the forgiveness inversion — silent
loss {10,5,3} strictly decreasing in ℓ, max at ℓ=1; R4 the priced repairs —
(a) once per streak at break_step−1 with zero ℓ=0 false positives, (b) R'=1
survives ℓ=1 and moves ℓ=2→10, ℓ=3→5 == closed form); twin evaluators
REJECT/REJECT over the enumerated 64-row boolean input set; APPROVE
arithmetically excluded (ℓ=1 breaks at 11). 35/35 self-checks exit 0 on the
accepted run; byte-identical double run by external diff + sha256 (results.json
`413f4d55b71f5e9f9a71e3090db42268a44201bb22e9bc81cc5a979526c5cf03`, run-stdout
`a0c9ed623167a603078b9d822a3be78c40ca0885d8fd1547daae4fc475cbbfc1`); both
Arm-R class-stream digests reproduced exact (`3bfa073726f7` @ 20261726,
`6f857d0afcf4` @ 20261727). sim-lab PR #168 [MERGE SHA + state filled at flip];
REPORT `sims/verdict-096-combo-grace-budget-cliff/REPORT.md`. This branch:
mirror + heartbeat + claim [SHAs filled at flip]; card flip = the deliberate
last commit.

## Constraints honored

- control/inbox.md untouched (manager-written); newest ORDER is 015 (EAP
  through 2026-07-21) — no `new` ORDER outranks the standing pipeline baton;
  ASK 005 / ASK 006 re-verified still `status: new`, carried.
- control/outbox.md append-only: `## VERDICT 096` collision-grepped clean at
  boot (0 header hits at HEAD b97e97d; the only "VERDICT 096" mentions are
  PREDICTION-class — the P083 heartbeat/card batons and the sim-lab map's
  "next expected" row); nothing above the newest block (PROPOSAL 083) touched.
- No merge actions from this seat: commit + push + report only; landing is the
  repo's CI-side auto-merge-enabler on green after this card's flip.
- No triggers/routines armed, deleted, or audited; no send_later. The failsafe
  cron stays as the coordinator left it (owner rebind pending — the heartbeat
  wakes line, carried verbatim).
- Timestamps real `date -u`; model recorded family-level only; no model
  identifier in any commit/PR text.
- GitHub exclusively via MCP tools; files staged explicitly, never
  `git add -A`/`.`.

## 💡 Session idea

(filled at flip)

## ⟲ Previous-session review

(filled at flip)
