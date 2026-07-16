# Session — P083 round-17 game-mechanics slot: PROPOSAL 083 (combo/streak grace-budget cliff, superbot-games tap) + ROTATION.md seed + heartbeat

> **Status:** `in-progress`
> **Model/time:** opus-class · 2026-07-16T14:20:17Z → [[fill: flip time]] (Ideas Lab
> worker slice — consume the VERDICT-095 close-out heartbeat's top baton at HEAD
> `96a9f22`: draft PROPOSAL 083, the standing ORDER 003 deliberate-rotation
> round-17 GAME-MECHANICS slot (round 17 opened at fleet backlogs with P081,
> venture served with P082 → VERDICT 095 REJECT), restore the pipeline to
> non-dry, seed the rotation ledger, close out.)

- **📊 Model:** opus-class · high · idea/planning

*(card born in-progress at 2026-07-16T14:20:17Z as the designed session-gate
hold; flips complete in this PR's final commit at [[fill: flip time]], after the
pipeline work lands. Task-class idea/planning: this session's core work is
drafting PROPOSAL 083; VERDICT 096 is deliberately the successor's first slice.)*

## Scope

Serve the VERDICT-095 close-out heartbeat's next-2 baton under standing owner
ORDER 003/004 with the EAP extension to 2026-07-21 (ORDER 015) as the standing
frame:

1. **PROPOSAL 083** — round 17, the GAME-MECHANICS rotation slot (ORDER 004
   rule 3; round 17 opened at fleet backlogs with P081 #448 → V094 REJECT,
   venture served with P082 #450 → V095 REJECT, so game mechanics is next;
   slot spacing …P067, P071, P075, P079 → P083, spacing 4). Harvest source:
   superbot-games, read FIRSTHAND on a public shallow clone. Idea file
   `ideas/superbot-games/combo-grace-budget-cliff-2026-07-16.md`, outbox
   PROPOSAL 083 append (append-only), section README index row, seeds
   20261726–729 (aux 20261729 never read; allocation started at 20261726 per
   the V095 heartbeat baton).
2. **Claim before work** — this session's claim
   `control/claims/2026-07-16-p083-round17-game-mechanics.md` rides this PR
   (claims dir at HEAD holds the README + the unrelated capabilities-classifier
   claim — different scope, no collision; the P082 claim was pruned by the V095
   session per the practiced prune-by-successor lifecycle).
3. **⚑ Self-initiated:** seed `ideas/ROTATION.md` — the O(1) rotation ledger the
   P082 card's 💡 flagged (the rotation table is re-derived by hand O(rounds)
   each slot). One badge-compliant doc, one row per round, linked from a
   reachable index. BONUS: reverted if it reds the gate; the PROPOSAL is the
   must-land.
4. **Close-out (this branch)** — session heartbeat on `control/status.md`
   (pipeline non-dry again: P083 sim-ready, next pull VERDICT 096), the
   guard-fires telemetry delta per the checker's own instruction, and this
   card's flip as the deliberate last commit.

## Results

1. **PROPOSAL 083 — DONE (sim-ready).** Round 17's game-mechanics slot served.
   Grounded FIRSTHAND @ superbot-games `5db902a3` (public shallow clone, fetched
   2026-07-16T14:14:06Z): the shipped SHARED-BUDGET pace surface
   `games/mining/core/energy.py` (`MAX_ENERGY = 60`, `DIG_COST = 1`,
   `REGEN_SECONDS = 10` → the sim-pinned 360-digs/active-hour throttle,
   `RESTORE_VALUES` refills, capped at `MAX_ENERGY`) — a per-action-looking pace
   brake that is actually a shared depleting budget with a cap and passive
   replenishment — plus the in-repo game-mechanics pacing corpus
   (`explore-action-pacing-quest-mint`, `mining-booster-bypass-throttle-seal`).
   P083 is a game-mechanics DESIGN head: it transfers that shipped
   shared-budget structure onto a proposed combo/streak MULTIPLIER surface the
   lane does not yet ship (stated honestly — no combo/streak/grace mechanic
   exists in the tree; the energy budget is the structural precedent). Head:
   a per-action-forgiving grace window (any action ≤ G=3 late "safe forever")
   actually hides one SHARED grace budget (B0=10) whose cumulative depletion
   breaks the streak at a history-determined step. Every registered numeral
   produced live by `draft_p083.py` (scratchpad, stdlib-only): **31/31 checks
   PASS, exit 0** — R1 the folk belief falsified (ℓ∈{1,2,3} break at finite
   steps 11/6/4, only ℓ=0 survives), R2 the cliff at break_step = floor(B0/ℓ)+1
   sim==closed-form exact, R3 the forgiveness inversion (loss = break_step−1 =
   {10,5,3}, strictly DECREASING in ℓ — the smallest lateness ℓ=1 rides longest
   and loses MOST, 10 of M=25), R4 the priced repairs (a grace-low warning
   fires exactly once per streak at break_step−1 with zero false positives on
   the ℓ=0 cohort; within-G replenish R'=1 nets drain (ℓ−1) → ℓ=1 survives,
   ℓ=2 breaks at exactly B0=10, ℓ=3 at 5). Disclosed landing REJECT (all
   within-grace steady patterns break at a finite history-determined step).
   Idea file homed in `ideas/superbot-games/` (the source lane's section per
   the fleet-slot precedent) + section README index row + outbox PROPOSAL 083
   appended (append-only; dedupe-grep 0 prior `## PROPOSAL 083` hits at HEAD
   96a9f22). Seeds 20261726–729, aux 20261729 never read.
2. **Claim — DONE.** This session's claim landed and STAYS at close for the
   successor to prune (the practiced prune-by-successor lifecycle — the P082
   claim was pruned by the V095 session after PR #450 verified merged).
3. **⚑ Self-initiated: ROTATION.md — [[fill: landed | deferred]].** Seeded the
   O(1) rotation ledger the P082 card's 💡 flagged, populated rounds 16–17 from
   the outbox chain (round 16 opener P077 → P078 venture / P079 game / P080
   unrelated; round 17 opener P081 → P082 venture-products / P083 game-mechanics
   = THIS), linked from a reachable index. [[fill: gate result note]]
4. **Close-out — DONE (this branch, PR [[fill: PR number]]).** Heartbeat
   overwritten in the standing grammar: wakes line carried verbatim (failsafe
   cron trig_01FYrWqjWeGVUTLg51arsHFr LIVE, owner rebind pending — no trigger
   touched); ASK 005/006 re-verified `status: new` and carried unchanged;
   pipeline honest: NON-DRY (P083 sim-ready; successor's next pull = VERDICT
   096, offset +13 twentieth row); seed baton next free 20261730; the
   guard-fires telemetry delta committed per the checker's instruction. This
   card's flip is the deliberate last commit.

## Constraints honored

- control/inbox.md untouched (manager-written); newest ORDER 015 (EAP through
  2026-07-21), 001–014 closed — no `new` ORDER outranked the dispatch baton.
- control/outbox.md append-only: `PROPOSAL 083` dedupe-grepped clean before the
  append (0 header hits at HEAD 96a9f22); nothing above the newest block
  (VERDICT 095) touched.
- superbot-games read FIRSTHAND but READ-ONLY (shallow clone in the scratchpad;
  no superbot-games file edited); sim-lab not touched (this repo writes only
  itself — Q-0260); one repo per PR.
- No merge actions from this seat: commit + push + report only; landing is the
  repo's CI-side auto-merge-enabler on green after this card's flip.
- No triggers/routines armed, deleted, or audited; no send_later. The failsafe
  cron stays as the coordinator close-out left it (owner rebind pending — see
  the heartbeat wakes line).
- Timestamps real `date -u`; model recorded family-level only; no model
  identifier in commits or PR text.

## 💡 Session idea

**The disclosed-landing verifier and the sim re-derive the SAME model twice but
share no scaffold — bless a one-file `model.py` the drafter's `draft_pNNN.py`
imports and the sim-lab arm re-implements against, so a drafter/sim disagreement
localizes to the DECISION rule instead of a silent constant typo.** Every
sim-ready proposal in this era ships a scratchpad `draft_pNNN.py` that pins the
model's constants and prints the disclosed `N/N PASS` line; the sim-lab verdict
then RE-DERIVES the same constants from the idea-file prose and must not trust
the drafter's numbers (by design — the independent re-derivation is the value).
But the two live in different repos with the constants transcribed by hand at
each hop (idea file → outbox `done-when` fixture → sim fixture), and a
transcription slip in a single integer (B0, G, the break rule's `<` vs `≤`)
moves several census cells together — exactly the "one misread moves the grid"
failure the NULL axes are pre-registered for. A blessed convention — the drafter
commits `model.py` as a NAMED artifact (not scratchpad-only) with the pinned
constants as module-level names, the idea file cites it by path, and the sim's
Arm B imports NOTHING from it but re-implements against the same named constants
— would turn "did the drafter and the sim pin the same B0?" from archaeology
across three transcriptions into a one-line diff, while preserving the
independent-derivation guarantee (Arm B still writes its own logic). Routing:
this repo owns the drafting convention (the `draft_pNNN.py` scratchpad ritual is
an idea-engine norm); a future opener session can bless it in one PR.
*(Deduped against recent cards: the P082 card's 💡 is the rotation ledger —
BEING BUILT this session as ROTATION.md, so this idea is deliberately DIFFERENT;
the P081 card's the fleet-slot placement rule; the v093 card's the mirror
consumer clause; the v092 card's the mirror grammar gap — none touch the
drafter/sim constant-transcription seam.)*

## ⟲ Previous-session review

Reviewed: the VERDICT-095 close-out session (PR #451, merged @ main 96a9f22,
card `.sessions/2026-07-16-verdict-095-owner-gate-cliff.md` and the coordinator
close-out heartbeat). Its baton was fully consumable as written: the
game-mechanics slot call (round-17, next after P082's venture), the seed baton
(next free 20261726 — confirmed by this session's read: P082's registered set
20261722–725 fully consumed, aux 20261725 never read), the ASK 005/006 status
(both `status: new`, re-verified at HEAD), and the wakes line (the live failsafe
cron, owner rebind pending) all re-verified accurate at HEAD 96a9f22 with zero
re-derivation. The V095 mirror block's discipline of carrying the sim-lab
drafter's numbers VERBATIM (145 matched / 0 mismatched / 7 honest vacancies; the
Arm-R digests e8d8812b3f9c / fc2709073718 reproduced exact) made the
"quote the sim-lab record, never recompute" pattern easy to follow — and it is
exactly the transcription seam this session's own 💡 prices from the drafting
side: the V095 session had to re-key P082's constants from prose to write the
mirror, the same by-hand hop a blessed `model.py` would collapse. One clean
inheritance worth naming: the V095 session pruned the P082 claim after verifying
PR #450 merged live AND deleted its own claim at close (rule 4 — session
terminal), so the claims dir arrived at this session holding only the README and
the unrelated capabilities claim; the practiced prune-by-successor lifecycle the
P082 card committed to `control/claims/README.md` is now running clean across
two consecutive cutovers.
