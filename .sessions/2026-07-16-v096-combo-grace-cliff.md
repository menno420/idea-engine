# Session — v096 pipeline: VERDICT 096 (P083, combo grace-budget cliff) via sim-lab → outbox V096 mirror + heartbeat + card flip

> **Status:** `complete`
> 📊 Model: opus-class · high · simulation/verification
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

**Genuine (this session):** A STANDING/CONTINUOUS ORDER THAT SPAWNS SEQUENTIAL
SLICES NEEDS SLICE-KEYED WORK CLAIMS, NOT ORDER-KEYED ONES. This slice's verify
claim (`control/claims/2026-07-16-v096-combo-grace-cliff.md`) tripped
`claims-order-collision` against the still-terminal P083 DRAFTING claim
(`…p083-round17-game-mechanics.md`) — both name standing ORDER 003 (the
continuous pipeline), and the checker's heuristic treats one order as one
claimant, so it reads a legitimate draft-then-verify handoff as duplicate work.
For a one-shot order that reading is right; for a STANDING order that emits many
sequential work slices (draft P083 → verify P083 → draft P084 → …) two slices
are almost always in flight at once, and the collision fires on every clean
pipeline turn. The durable fix: a work claim for a continuous/standing order
should key its collision identity on the SLICE (the proposal/verdict number or
the draft-vs-verify phase), not the bare order id — so `verify-P083` and
`draft-P083` are distinguishable claimants of ORDER 003, and the warning fires
only on a TRUE duplicate (two `verify-P083` claims). Concretely, the checker
could extract `ORDER NNN` PLUS the nearest proposal/verdict token from the claim
body and collide on the pair. Dedup: V095's card 💡 was doctrine-vs-classifier
CAPABILITIES rows; V094's was the claims-lifecycle rule-4 tension (delete-at-
close vs prune-by-successor — about WHEN a claim dies); the P083 card's was the
O(1) rotation ledger; the P082 card's was drafting-side. None covers the
collision heuristic's GRANULARITY for continuous orders — this is about WHICH
claims count as the same claimant, orthogonal to rule-4's lifecycle question.
Grepped `.sessions/` at b97e97d for "order-collision"/"slice-keyed" — only the
checker's own advisory text, no card states this rule.

## ⟲ Previous-session review

P083 drafting session (PR #453, merged @ main `8143cee`; verifier-count
follow-up #454 @ `b97e97d`): clean handoff, verified in use this session — the
sim-ready P083 block and the idea file carried every registered numeral the
verdict needed (the steady break-step map {∞,11,6,4,1}, the loss map {10,5,3},
both repair maps, both closed-form contacts C1/C2, and the Arm-R seed set
20261726–729 with both preview censuses and both class-stream digests), so the
sim-lab side re-derived the whole battery from the idea file with a single
independently-shaped automaton and reproduced the disclosed 35/35 exactly, zero
back-reference to the drafting scratchpad `draft_p083.py` (which is a scratchpad,
never committed). #454's correction — bumping the disclosed verifier count to
35/35 — was confirmed in use: the independent sim also lands at exactly 35 self-
checks, so the corrected count is the true one. One gap the verify slice hit and
disclosed (see the sim-lab card's 💡, not repeated here): the P083 registration
pinned the Arm-R digest VALUES but not the digest's TOKEN ENCODING, so the verify
side had to reverse-derive the first-character encoding (SURVIVE/SILENT-BREAK →
'S') — the digest reproduced exactly once the encoding was found, with the census
counts carrying the S/S split the digest collapses. Nothing was left pending for
this mirror slice to resolve; the drafting baton ("simulate P083 → V096, disclosed
REJECT") was executable exactly as written and executed here.
