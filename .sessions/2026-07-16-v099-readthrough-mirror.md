# Session — v099 pipeline: VERDICT 099 (P086, series read-through concentrate-vs-spread saturation crossover) via sim-lab → outbox V099 fan-in mirror + heartbeat + claim.

> **Status:** `complete`
> 📊 Model: Claude Opus 4 family · high effort · verdict-mirror task-class
> **Model/time:** Claude Opus 4 family · high · verdict-mirror · 2026-07-16 (a dispatched session for the coordinator seat — the verify half / fan-in mirror of PROPOSAL 086: the sim runs sim-lab-side on sim-lab PR #171.)

*(card born in-progress as the designed session-gate hold; FLIPPED to
`complete` as the deliberate LAST step after coordinator/owner review — this is
the release-landing commit. Task-class verdict-mirror: this session's core work
is verifying the sim-lab verdict landing and mirroring the finalized ACCEPT
record — the sim itself runs sim-lab-side on sim-lab's own PR #171
(`sims/verdict-099-series-readthrough-saturation-crossover/`); this repo edits
only itself, Q-0260.)*

## Objective

Run the V099 pipeline under standing owner ORDER 003/004 with the EAP frame
(ORDER 015, through 2026-07-21) as the standing context:

1. **VERDICT 099** — the sim-lab-finalized verdict on PROPOSAL 086 (the series
   read-through concentrate-vs-spread saturation crossover,
   `ideas/venture-lab/series-readthrough-saturation-crossover-2026-07-16.md`,
   outbox block `## PROPOSAL 086 · 2026-07-16T17:48:11Z · status: sim-ready`,
   SEEDLESS — no seed baton consumed) mirrored into this repo's append-only
   ledger. The sim rides sim-lab PR #171; this card covers the idea-engine
   fan-in slice. Offset +13 twenty-third row (P084 → V097, P085 → V098, P086 →
   V099).
2. **Close-out (this branch)** — VERDICT 099 fan-in appended to
   `control/outbox.md` (append-only, real `date -u`, V098-grammar mirror block;
   proposal blocks never edited), heartbeat re-stamped on `control/status.md`
   (heartbeat-last discipline; seed baton: P086 SEEDLESS, next free block stays
   20261730), the mirror claim `control/claims/2026-07-16-v099-readthrough-mirror.md`
   carried, terminal-claim prunes per the status baton, and this card's flip to
   `complete` as the deliberate last step (done — coordinator/owner review
   preceded the flip).

## What happened

The sim-lab side (PR #171, head `b0dd79b5dc9714bac52ceb6aedf34a1388779fd9`, base
main `5d8a45ef`) built `sims/verdict-099-series-readthrough-saturation-crossover/`
— an independent hermetic re-implementation of the N=4-book multiplicative
read-through funnel under common random numbers (each seed's C=2000 readers'
three uniforms drawn ONCE via `random.Random(seed)` and reused for BOTH
allocations AND across ALL budgets; a per-mode matrix fingerprint guards the
registered NULL against divergent draws) with twin independently-written
decision evaluators (if-chain vs table-driven). This idea-engine slice is the
fan-in half: it does NOT re-run the sim (this repo edits no other repo — Q-0260)
and does NOT recompute the numbers, it MIRRORS the finalized sim-lab ACCEPT
record — carrying the sim-lab drafter's numerals verbatim — into this repo's
append-only ledger. Concretely: a `## VERDICT 099` block appended to
`control/outbox.md` addressed to the fleet manager (Q-0264 fan-in) in the
VERDICT 098 mirror grammar, the `control/status.md` heartbeat overwritten
(heartbeat-last), the mirror claim, and this card. The P086 proposal block is
NOT edited — this outbox is append-only and prior verdicted proposals keep their
original status lines; the VERDICT 099 block IS the status-flip record for
PROPOSAL 086.

## Results

**VERDICT 099 = ACCEPT** — the pre-registered rule (ACCEPT iff R1∧R2∧R3∧R4,
evaluated in order R1→R2→R3→R4; else REJECT at the first failing gate) fired
**ACCEPT with first-failing gate None**. Gate outcomes: **R1 PASS · R2 PASS ·
R3 PASS · R4 PASS**.
- **R1 PASS (reach regime — concentrate wins unsaturated)** — at B=6 mean
  revenue(CONCENTRATE)=3641.80 > SPREAD=3225.00 for all 5 seeds; paired margin
  **29.81σ** (≥ 3σ).
- **R2 PASS (saturation regime — the reversal, spread wins)** — at B=33 mean
  revenue(SPREAD)=6344.40 > CONCENTRATE=4336.60 for all 5 seeds; paired margin
  **156.67σ** (≥ 3σ).
- **R3 PASS (well-posedness / stability sanity)** — every realized r_k ∈
  [0.30, 0.85] (the V098 ceiling check), AND mean revenue monotone
  non-decreasing in B for BOTH allocations (CONC [3641.8, 4336.6, 4336.6,
  4336.6, 4336.6]; SPREAD [3225.0, 3651.6, 4129.4, 4804.8, 6344.4]).
- **R4 PASS (crossover located at the entry-step ceiling)** — crossover
  **B\*=22** ∈ (11, 22], AND CONCENTRATE mean revenue FLAT at 4336.6 books
  across B ∈ {11, 16, 22, 33} (0.0-book variation — r_1 clamped at r_max=0.85
  for all b_1 ≥ 11), so the reversal is mechanistically caused by the stability
  bound.

Both independently-written decision evaluators (if-chain vs table-driven) agree
ACCEPT/None; 7/7 self-checks exit 0 on the accepted run. Digests (verbatim from
the sim-lab record): results.json sha256
`14e7a4d57db265c7f042759e401c4c2521c9036493f961fa3ed1b152cfbbfb3d`; run-stdout.txt
sha256 `4d43e3194fdd1c8da0402e8d1e7f348c355c39f665c40160f103648600c7d9d8`;
fixtures.json sha256
`69fe5aa13d4ea78519843880cad930f91dc6a6211ddfaceb78f9cd9a87fa74d5`. results.json
+ run-stdout.txt byte-identical across two full in-repo process runs (external
diff + sha256). sim-lab PR #171 (head `b0dd79b5`, base main `5d8a45ef`), sim dir
`sims/verdict-099-series-readthrough-saturation-crossover/`. This branch: claim +
born-red card (this FIRST commit) → outbox fan-in + heartbeat + prunes → card
flip to `complete` = the deliberate last commit (done, after coordinator/owner
review — the release-landing commit).

## Constraints honored

- control/inbox.md untouched (manager-written); newest ORDER is 015 (EAP through
  2026-07-21) — no `new` ORDER outranks the standing pipeline baton; standing
  ORDER 003 (continuous pipeline) + ORDER 015 (no-re-arm) live; ASK 005 / ASK
  006 carried.
- control/outbox.md append-only: `## VERDICT 099` collision-grepped clean at boot
  (0 header hits at HEAD 59b558d); nothing above the newest block (PROPOSAL 086)
  touched. The P086 proposal block is NOT edited.
- Mirror claim `control/claims/2026-07-16-v099-readthrough-mirror.md` added;
  no `## Sim verdict` note; nothing under `ideas/` edited.
- No merge actions from this seat: commit + push + open PR only; no makerbench
  build. This repo edits only itself (Q-0260).
- No triggers/routines armed, deleted, or audited; no send_later. The failsafe
  cron stays as the coordinator left it (owner rebind reviewed — the live cron
  stays as-is; carried in the heartbeat wakes line).
- Timestamps real `date -u`; model recorded family-level only; no exact model
  identifier in any commit/PR/card text.
- GitHub exclusively via MCP tools; files staged explicitly, never
  `git add -A`/`.`; guard-fires.jsonl left uncommitted.

## ⟲ Previous-session review

Reviewed the V099 sim-lab slice (sim-lab PR #171): PROPOSAL 086's series
read-through crossover was independently re-derived hermetically and landed
**ACCEPT** — all four gates pass, first-failing gate None, and the measured
{B × allocation} table reproduces the disclosed dry-sim calibration to the book
(CONC flat at 4336.6 once its entry step saturates at b_1=11; SPREAD overtakes at
**B\*=22**). The immediate predecessor P085/V098 (RR-vs-LQF domain-rotation
starvation cliff) REJECTED at R1 because it mis-registered a gate leg ABOVE the
world's own stability bound (ρ=0.70 was already unstable for the highest-λ
domain); P086 deliberately embodies that lesson — it LOCATES the flip AT the
read-through ceiling r_max, which is exactly what R4 confirmed (the reversal is
ceiling-caused, not a downstream artifact). The V097 mirror card's carried 💡
(a check-side helper that diffs the mirrored digests against the sim-lab blob at
the cited SHA) remains unlanded: the three digests pasted in THIS block
(results.json `14e7a4d5…`, run-stdout `4d43e319…`, fixtures.json `69fe5aa1…`)
are still a human-copied, machine-unverified cross-repo step — the same tripwire.

## 💡 **Session idea**

A fan-in ACCEPT mirror re-types the sim-lab {B × allocation} table (five budget
rows × two allocations) plus three sha256 digests by hand across the repo
boundary — the exact drift surface V097's 💡 named. A contained, reversible
sharpening available NOW without any new sibling artifact: at mirror time, assert
the ONE internal consistency the pasted table must satisfy — that the mirrored
crossover B\* is the smallest grid B where the pasted SPREAD row ≥ the pasted
CONCENTRATE row (here B\*=22: SPREAD 4804.8 ≥ CONC 4336.6 first true at B=22, and
false at B=16 where 4129.4 < 4336.6). A three-line check-side helper recomputing
B\* from the mirrored table and comparing it to the mirrored B\* token would catch
a mistyped revenue cell or a copied-wrong B\* before it lands — strictly lighter
than the cross-repo digest-diff, and it needs only the block's own numbers.

> **Guard recipe:** target = a check-side assertion in `scripts/check_sections.py`
> (the outbox/ideas cross-check home) that, for any `## VERDICT` block carrying a
> `{B × allocation}` mean-revenue table + a `B*` token, recomputes B* = argmin_B
> (SPREAD_B ≥ CONC_B) from the block's own rows and errors on mismatch. Test
> target: this V099 block (B*=22) as the positive fixture; a hand-mutated copy
> with B* flipped to 16 as the negative.

> 📊 Model: Claude Opus 4 family · high effort · verdict-mirror task-class
