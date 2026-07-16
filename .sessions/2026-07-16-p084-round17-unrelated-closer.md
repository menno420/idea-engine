# Session — P084 round-17 unrelated-domain CLOSER slot: PROPOSAL 084 (Simpson's-paradox aggregation-reversal trap, statistics/causal-inference tap) + heartbeat

> **Status:** `complete`
> **Model/time:** opus-class · 2026-07-16T15:17:03Z → 2026-07-16T15:31:23Z (Ideas Lab
> worker slice — consume the VERDICT-096 close-out heartbeat's top baton at HEAD
> `b119a62`: draft PROPOSAL 084, the standing ORDER 003 deliberate-rotation
> round-17 COMPLETELY-UNRELATED-domain CLOSER slot (round 17 opened at fleet
> backlogs with P081 → V094 REJECT, venture with P082 → V095 REJECT, game
> mechanics with P083 → V096 REJECT), keep the pipeline non-dry, close out.)

- **📊 Model:** opus-class · high · idea/planning

*(card born in-progress at 2026-07-16T15:17:03Z as the designed session-gate
hold; flipped complete in this PR's final commit at 2026-07-16T15:31:23Z, after the
pipeline work landed. Task-class idea/planning: this session's core work is
drafting PROPOSAL 084; VERDICT 097 is deliberately the successor's first slice.)*

## Scope

Serve the VERDICT-096 close-out heartbeat's next-2 baton under standing owner
ORDER 003/004 with the EAP extension to 2026-07-21 (ORDER 015) as the standing
frame:

1. **PROPOSAL 084** — round 17, the COMPLETELY-UNRELATED-domain CLOSER slot
   (ORDER 004 rule 3; round 17 opened at fleet backlogs with P081 #448 → V094
   REJECT, venture with P082 #450 → V095 REJECT, game mechanics with P083 #453 →
   V096 REJECT, so the unrelated closer is next; slot spacing …P068, P072, P076,
   P080 → P084, spacing 4). Fleet-external pure-mechanism head homed in
   `ideas/fleet/` (the cross-cutting home per the P080 precedent). Idea file
   `ideas/fleet/simpsons-paradox-aggregation-reversal-2026-07-16.md`, outbox
   PROPOSAL 084 append (append-only), fleet README index row.
2. **Claim before work** — this session's claim
   `control/claims/2026-07-16-p084-round17-unrelated-closer.md` rides this PR
   (claims dir at HEAD holds the README + the P083 drafting claim, the V096
   verify claim, and the unrelated capabilities-classifier claim — all different
   scope, no SAME-scope collision; the draft-vs-verify claims-order advisory is
   expected/non-blocking).
3. **Domain switch (decide-and-flag).** The task named IRV/social-choice as the
   primary domain and the transit inspection paradox as the fallback. BOTH are
   already occupied: IRV monotonicity is P017
   (`ideas/fleet/irv-monotonicity-close-races-2026-07-13.md` — "how often does
   raising the winner make it lose") and the inspection paradox is P056
   (`ideas/fleet/inspection-paradox-wait-inflation-2026-07-14.md`). The rotation
   ledger counts DISTINCT fleet-external domains, so re-using either breaks the
   coverage claim. Switched to **Simpson's paradox** (statistics / causal
   inference — the aggregation/reversal paradox), tree-wide clean (0 hits), the
   fresh SEVENTEENTH domain — flagged here, in the idea file's Dedup, and in the
   report.
4. **Close-out (this branch)** — session heartbeat on `control/status.md`
   (pipeline non-dry again: P084 sim-ready, next pull VERDICT 097), the
   guard-fires telemetry delta per the checker's own instruction if it appends,
   and this card's flip as the deliberate last commit.

## Results

1. **PROPOSAL 084 — DONE (sim-ready).** Round 17's unrelated CLOSER slot served
   with a fresh SEVENTEENTH fleet-external domain: STATISTICS / CAUSAL INFERENCE
   — Simpson's paradox (the aggregation/reversal paradox). Pure social-choice-
   distant math head; NO external repo surface — grounded FIRSTHAND in the
   reasoning + the canonical Charig et al. (1986) kidney-stone table, HONEST per
   the TRUTH bar (no repo claimed). Head: the folk belief "if treatment A beats
   treatment B in EVERY subgroup, A beats B overall" is FALSE the moment the
   subgroup allocation is confounded with the subgroup baseline — the pooled rate
   is a SIZE-WEIGHTED mean of stratum rates, and A can win every stratum yet lose
   the pool. Every registered numeral produced live by `draft_p084.py`
   (scratchpad, stdlib-only): **25/25 checks PASS, exit 0** (deterministic
   integer/Fraction arithmetic, byte-identical across two process runs) — R1 the
   folk belief falsified (A 0.931>0.867 Small, 0.730>0.688 Large, yet pooled A
   39/50=0.780 < B 289/350≈0.826, B wins the pool by ≈0.046), R2 the reversal
   pivot (A loads the HARD stratum — 75.1% of A's cases are Large, base 0.720 —
   while B loads the EASY one — 77.1% Small, base 0.882; give A B's size-mix and A
   wins the pool 0.885>0.826, so the pivot is the ALLOCATION, not the treatment),
   R3 the cliff (holding A's stratum rates fixed and sweeping x = #A-in-hard-
   stratum, pooled_A(x) is strictly decreasing with exactly ONE crossing — the
   single-threshold cliff at **x\*=184**; the real table x=263 sits past it), R4
   the priced repair (direct standardization to the pooled size distribution
   restores A>B — std A≈0.8325 > B≈0.7789 — and the fix is WEIGHT-INVARIANT here,
   A>B under A-mix/B-mix/50-50/pool; priced: it REQUIRES recording the confounder
   — the subgroup — and the honest NULL axis is that adjusted direction can in
   general depend on the estimand weights, here it does not). Disclosed landing
   REJECT (a reversing table exists; APPROVE arithmetically excluded). Idea file
   homed in `ideas/fleet/` (fleet-external cross-cutting home per P080) with a
   `> **State:**` line so `check_ideas`' grammar scan passes + fleet README index
   row + outbox PROPOSAL 084 appended (append-only; dedupe-grep 0 prior
   `## PROPOSAL 084` hits at HEAD b119a62).
2. **Claim — DONE.** This session's claim landed and STAYS at close for the
   successor to prune (the practiced prune-by-successor lifecycle).
3. **Domain switch — DONE + FLAGGED.** IRV (P017) and inspection paradox (P056)
   both confirmed hard duplicates firsthand (`rg` sweeps + reading both files);
   Simpson's paradox confirmed tree-wide clean; the switch is disclosed in the
   idea file's Dedup, this card's Scope, and the report.
4. **Close-out — DONE (this branch, PR #456).** Heartbeat overwritten in
   the standing grammar: wakes line carried verbatim (failsafe cron
   trig_01FYrWqjWeGVUTLg51arsHFr LIVE, owner rebind pending — no trigger
   touched); ASK 005/006 re-verified `status: new` and carried unchanged;
   pipeline honest: NON-DRY (P084 sim-ready; successor's next pull = VERDICT 097,
   offset +13); the guard-fires telemetry delta committed per the checker's
   instruction if it appended. This card's flip is the deliberate last commit.

## Constraints honored

- control/inbox.md untouched (manager-written); newest ORDER 015 (EAP through
  2026-07-21), 001–014 closed — no `new` ORDER outranked the dispatch baton.
- control/outbox.md append-only: `PROPOSAL 084` dedupe-grepped clean before the
  append (0 header hits at HEAD b119a62); nothing above the newest block
  (VERDICT 096) touched.
- No external repo cloned or read — this is a pure-math head grounded in its own
  reasoning + a cited standard result (HONEST scope: no repo surface claimed);
  sim-lab not touched (this repo writes only itself — Q-0260); one repo per PR.
- No merge actions from this seat: commit + push + report only; landing is the
  repo's CI-side auto-merge-enabler on green after this card's flip.
- No triggers/routines armed, deleted, or audited; no send_later. The failsafe
  cron stays as the coordinator close-out left it (owner rebind pending — see
  the heartbeat wakes line).
- Timestamps real `date -u`; model recorded family-level only; no model
  identifier in commits or PR text.

## 💡 Session idea

**The unrelated-domain rotation has no COVERAGE LEDGER, so a slot can silently
re-tap a domain it already served — this session's own task named two domains
(IRV, inspection paradox) that were BOTH already occupied (P017, P056), caught
only by a hand `rg` sweep of every prior fleet file. Bless a one-line
machine-checkable `domain:` tag in each unrelated head's front matter (a
controlled vocabulary — `social-choice`, `renewal-theory`, `causal-inference`,
…) and a `check_ideas` advisory that reds a DUPLICATE `domain:` across the
`ideas/fleet/` unrelated-rotation heads.** The rotation's whole value is DISTINCT
fleet-external domain coverage (P080's file enumerates "the fifteen prior
occupants" by hand), yet the only thing standing between the pipeline and a
silent re-tap is a drafter remembering to grep — and this slice is the existence
proof that the grep can be skipped by an upstream spec (the task confidently
named IRV as "maximally distant," unaware it was the rotation's FIRST occupant).
A `domain:` token turns "is this domain fresh?" from an O(rounds) hand sweep that
a busy drafter can shortcut into an O(1) checker assertion that CANNOT be
shortcut: the drafter still picks the domain and writes the head, but a
duplicate token reds the gate before the PR can go green, exactly where the
current process has no tripwire at all. Routing: this repo owns the ideas-grammar
checker (`scripts/check_ideas.py`), so a future opener session can bless the
token + the advisory in one PR; the controlled vocabulary seeds from P080's
hand-enumerated fifteen + this head's seventeenth.
*(Deduped against recent cards: the P083 card's 💡 is the drafter/sim
`model.py` constant-transcription seam; the P082 card's is the O(1) rotation
LEDGER (round bookkeeping — WHICH slot-type is next); the V096 card's is
slice-keyed work claims (the `claims-order-collision` heuristic's GRANULARITY —
WHICH claims count as the same claimant for a continuous order). THIS idea is
adjacent to all three but distinct: not "which slot-type is next" (P082's round
ledger), not "which claims are the same claimant" (V096's collision granularity),
but "has this DOMAIN been used before" — a domain-coverage/dedup tripwire on the
`ideas/fleet/` unrelated heads that no round ledger and no claim heuristic
provides, surfaced by this session's own double-collision on two already-spent
domains.)*

## ⟲ Previous-session review

Reviewed: the VERDICT-096 close-out session (PR #455, sim-lab #168 merged @
34ff0c9, card `.sessions/2026-07-16-v096-combo-grace-cliff.md` and the
coordinator close-out heartbeat at main b119a62). Its baton was fully consumable
as written: the unrelated-CLOSER slot call (round-17, next after P083's game
mechanics), the +13 offset (V097 ↔ P084), the ASK 005/006 status (both
`status: new`, re-verified at HEAD), and the wakes line (the live failsafe cron,
owner rebind pending) all re-verified accurate at HEAD b119a62 with zero
re-derivation. The V096 mirror block's discipline of carrying the sim-lab
drafter's numbers VERBATIM (35/35 self-checks, both Arm-R digests 3bfa073726f7 /
6f857d0afcf4 reproduced, results sha 413f4d55…) made the "quote the sim-lab
record, never recompute" pattern easy to follow. One caveat worth naming for the
successor: the heartbeat baton pointed at the unrelated CLOSER but did NOT name a
domain — and the DISPATCH spec that did name one (IRV) named a domain the
rotation had already spent at P017, and its fallback (inspection paradox) one
spent at P056; the baton's silence on domain was correct (domain is the
drafter's decide-and-flag), but it is exactly the coverage-tripwire gap this
session's 💡 prices. The claims dir arrived holding the README, the P083 drafting
claim (PR #453 merged — prunable), the V096 verify claim (STAYS for its
successor), and the unrelated capabilities claim; per the practiced
prune-by-successor lifecycle those are left for the successor baton, and this
session adds its own P084 claim to that set.
