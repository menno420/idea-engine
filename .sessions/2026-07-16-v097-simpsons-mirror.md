# Session — v097 pipeline: VERDICT 097 (P084, Simpson's-paradox aggregation-reversal trap) via sim-lab → outbox V097 mirror + heartbeat + card flip

> **Status:** `complete`
> 📊 Model: opus-class · high · simulation/verification
> **Model/time:** opus-class · high · simulation/verification · 2026-07-16 (a
> dispatched session for the coordinator seat — the verify half of PROPOSAL
> 084: run P084 (the round-17 COMPLETELY-UNRELATED-domain CLOSER slot — the
> Simpson's-paradox aggregation-reversal trap, the canonical Charig et al.
> (1986) kidney-stone table carried as a WITNESS and priced as an exact
> size-weighted-mean reversal with a single-cliff allocation threshold and a
> weight-invariant standardization repair) through sim-lab as VERDICT 097,
> then mirror the verdict into this repo's outbox and close out.)

*(card born in-progress as the designed session-gate hold; flips complete in
this PR's final commit after the pipeline work lands. Task-class
simulation/verification: this session's core work is verifying the sim-lab
verdict landing and mirroring the finalized record — the sim itself runs
sim-lab-side on sim-lab's own PR #169.)*

## Objective

Run the V097 pipeline under standing owner ORDER 003/004 with the EAP frame
(ORDER 015, through 2026-07-21) as the standing context:

1. **VERDICT 097** — run PROPOSAL 084 (Simpson's-paradox aggregation-reversal
   trap, `ideas/fleet/simpsons-paradox-aggregation-reversal-2026-07-16.md`,
   outbox block `## PROPOSAL 084 · 2026-07-16T15:25:14Z · status: sim-ready`,
   SEEDLESS — no Arm R, no seed baton consumed) through sim-lab and register
   the verdict. The sim-lab side lands on its own sim-lab branch/PR (#169);
   this card covers the idea-engine slice. Offset +13 twenty-first row (P083 →
   V096, P084 → V097).
2. **Close-out (this branch)** — V097 mirror appended to `control/outbox.md`
   (append-only, real `date -u`, compact V096-grammar mirror block; proposal
   blocks never edited), close-out heartbeat on `control/status.md` (seed
   baton: P084 SEEDLESS, next free block stays 20261730), and this card's flip
   as the deliberate last step. This session's own claim
   `control/claims/2026-07-16-v097-simpsons-mirror.md` rides this PR's first
   commit and STAYS at close for the successor to prune (the practiced
   prune-by-successor lifecycle; control/claims/README.md HOST-OWNED section).

## What happened

The sim-lab side (PR #169, merge commit `51567b4`) built and landed
`sims/verdict-097-simpsons-paradox-aggregation-reversal/` — the hermetic
exact-arm + twin-evaluator pre-registered discipline (the P028/P032/P036/P076
SEEDLESS fully-exact-census precedent, reused as machinery on a new object: a
size-weighted-mean reversal with a single-cliff allocation threshold and a
weight-invariant standardization repair confined to the same-sign case). This
idea-engine slice is the fan-in half: it does NOT re-run the sim (this repo
edits no other repo — Q-0260) and does NOT recompute the numbers, it MIRRORS
the finalized sim-lab record — carrying the sim-lab drafter's numerals verbatim
— into this repo's append-only ledger. Concretely: a `## VERDICT 097` block
appended to `control/outbox.md` addressed to the fleet manager (Q-0264 fan-in)
in the VERDICT 096 mirror grammar, the `control/status.md` heartbeat overwritten
(heartbeat-last discipline), this card, and this session's claim. The proposal
block for P084 is NOT edited — this outbox is append-only and prior verdicted
proposals keep their original status lines; the VERDICT 097 block IS the
status-flip record for PROPOSAL 084.

## Results

**VERDICT 097 = REJECT** — the pre-registered rule fired in the registered order
(REJECT → INVALID → APPROVE → NULL) on all four clauses: R1 the reversal (A beats
B in BOTH strata by cross-multiplication — small 81·270=21,870>234·87=20,358,
large 192·80=15,360>55·263=14,465 — while pooled B beats A: 289/350 > 273/350,
the reversal margin exactly 16/350=8/175≈0.046); R2 the pivot (A loads the HARD
large stratum 263/350=75.1% vs B's 80/350=22.9%, base_S=315/357 > base_L=247/343,
and A under B's size-mix wins the pool ≈0.8851>0.8257 — the reversal lives
entirely in the ALLOCATION, the treatment ranking never moved); R3 the cliff
(pooled_A(x) strictly decreasing with EXACTLY ONE crossing of 289/350 at x\*=184,
boundary x=183 above / x=184 below, real table x=263 past it — a single-threshold
step function); R4 the priced repair (standardization to the pooled marginal
357/343/700 gives std_A=634983/762700≈0.8325 > std_B=6231/8000≈0.7789, A
restored, weight-invariant over the four common-weight mixes {A-mix, B-mix,
50/50, pool} because A wins every stratum). APPROVE is arithmetically excluded
(the single exhibited reversal refutes "a uniform stratum ordering always
survives aggregation"), so REJECT. Twin evaluators agree REJECT/REJECT.
**33/33 self-checks exit 0** on the accepted run; results.json + run-stdout.txt
byte-identical across two full in-repo process runs by external diff + sha256
(results.json `7abe38549d01bc2abb30f535c351eabd40d02ad2200b58cdecfb187698c7eeee`,
run-stdout `62686fc03de7b6a212979db8a2a0cf324328344b5651759ac320ada37ec2926a`).
sim-lab PR #169, merge commit `51567b4`, sim dir
`sims/verdict-097-simpsons-paradox-aggregation-reversal/`; REPORT
`sims/verdict-097-simpsons-paradox-aggregation-reversal/REPORT.md`. This branch:
mirror + heartbeat + claim (born-red card) → card flip = the deliberate last
commit.

## Constraints honored

- control/inbox.md untouched (manager-written); newest ORDER is 015 (EAP
  through 2026-07-21) — no `new` ORDER outranks the standing pipeline baton;
  ASK 005 / ASK 006 carried.
- control/outbox.md append-only: `## VERDICT 097` collision-grepped clean at
  boot (0 header hits at HEAD 4b9db80); nothing above the newest block
  (PROPOSAL 084) touched. The P084 proposal block is NOT edited.
- No merge actions from this seat: commit + push + report only; landing is the
  repo's CI-side auto-merge-enabler on green after this card's flip.
- No triggers/routines armed, deleted, or audited; no send_later. The failsafe
  cron stays as the coordinator left it (owner rebind pending — carried in the
  heartbeat wakes line).
- Timestamps real `date -u`; model recorded family-level only; no model
  identifier in any commit/PR text.
- GitHub exclusively via MCP tools; files staged explicitly, never
  `git add -A`/`.`.

## ⟲ Previous-session review

P084 drafting session (PR #456, card
`.sessions/2026-07-16-p084-round17-unrelated-closer.md`, merged @ main
`4b9db80`): a clean, fully-consumable handoff — verified in use this session.
The sim-ready P084 block and the idea file carried every registered numeral the
verdict needed (the pinned Charig table A·S=(81,87)/A·L=(192,263)/B·S=(234,270)/
B·L=(55,80), the pooled fractions 39/50 & 289/350, the reversal gap 16/350, the
baselines 315/357 & 247/343, the shares 263/350 & 80/350, the cliff x\*=184 with
the x=183/184 boundary, the standardized 634983/762700 & 6231/8000, and the
three typed must-equal contacts C1/C2/C3), so the sim-lab side re-derived the
whole battery from the idea file with an independently-shaped automaton and
reproduced the disclosed gates exactly, with zero back-reference to the drafting
scratchpad `draft_p084.py` (never committed). The drafter's decide-and-flag
domain switch — the dispatch spec named IRV (already P017) and the inspection
paradox (already P056), so the slice served the fresh SEVENTEENTH domain,
Simpson's paradox — was disclosed in the idea file's Dedup, the card, and the
report, and held up firsthand this session (both prior domains confirmed spent).
One honest caveat carried forward: the P084 registration pinned the SEEDLESS
exact-census discipline, so the verify side had no digest-encoding ambiguity to
reverse (unlike the V096 Arm-R token-encoding gap) — the arithmetic reproduced
directly. Nothing was left pending for this mirror slice to resolve; the drafting
baton ("simulate P084 → V097, disclosed REJECT") was executable exactly as
written and executed here.

## 💡 **Session idea**

**A MIRROR SLICE THAT CARRIES DIGESTS VERBATIM FROM A SIBLING REPO HAS NO
MACHINE CHECK THAT THE DIGEST IT PASTED IS THE DIGEST THE SIBLING PR ACTUALLY
LANDED — the fan-in trusts a human-copied sha256 across a repo boundary.** This
slice pastes the sim-lab results.json sha `7abe3854…` and run-stdout sha
`62686fc0…` into both this repo's outbox block and this card, copied from the
sim-lab record; nothing in idea-engine's own `check --strict` can confirm those
64 hex chars match what sim-lab PR #169 merged, because the sim artifacts live
in the OTHER repo and this repo (correctly) never reads it. A silent
transcription slip — one hex nibble — would land a WRONG provenance digest that
reads authoritative forever, and the append-only rule means it can never be
edited out, only superseded by a correction block. The durable fix is a
cross-repo provenance manifest: sim-lab, on merge, writes the (verdict-number →
merge-sha, results-sha, stdout-sha, self-check-count) tuple into a tiny
machine-readable ledger (e.g. sim-lab `docs/verdict-provenance.json`), and
idea-engine's `check_ideas` grows an OPTIONAL advisory that, when the sibling
ledger is present in a co-checkout, asserts the outbox VERDICT block's pasted
digests EQUAL the ledger's — turning "did I copy the sha right?" from an
unverifiable human step into an O(1) checker assertion at the exact boundary the
current process leaves unguarded. Dedup: the P084 card's 💡 is the `domain:`
coverage tripwire (WHICH domain, drafting-side); the V096 card's is slice-keyed
work claims (WHICH claims collide); the P082 card's is the O(1) rotation ledger
(WHICH slot-type is next). None touches VERIFICATION of a cross-repo pasted
digest — this is about the fan-in's provenance integrity, orthogonal to all
three. Grepped `.sessions/` at HEAD 4b9db80 for "provenance"/"digest-check" —
only the checker's own advisory text, no card states this rule.

> 📊 Model: opus-class · high · simulation/verification
