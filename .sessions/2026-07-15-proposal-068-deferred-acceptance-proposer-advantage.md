# Session — PROPOSAL 068: who asks, wins — the deferred-acceptance proposer advantage is not a tie-break, it is a market-size-born rank tax the receiving side pays (COMPLETELY-UNRELATED-domain rotation, round 13 closer)

> **Status:** `complete`
> **Model/time:** fable · 2026-07-15T06:40:20Z (Ideas Lab worker slice — draft the
> round-13 COMPLETELY-UNRELATED-domain rotation closer under standing owner
> ORDER 003/004; round 13 order so far: P065 fleet-backlogs (#428) → P066
> venture (#429) → P067 game (#430, merged 06:26:58Z), so the UNRELATED slot is
> next. Card born in-progress as the designed session-gate hold; flipped
> complete in this PR's final commit at 2026-07-15T06:47Z. PR #431.)

- **📊 Model:** fable-class · high · idea/planning

## Scope

Draft a genuinely new sim-shaped idea for the COMPLETELY-UNRELATED-domain
rotation slot, round 13 CLOSER, under standing owner ORDER 003 (continuous
pipeline) and ORDER 004 rule 3 ("fleet backlogs → venture's book/product
space → game mechanics → COMPLETELY UNRELATED domains — I want those too").
Round 13 served fleet backlogs with P065 (#428), venture with P066 (#429),
and game mechanics with P067 (#430, merged 2026-07-15T06:26:58Z), so the
unrelated slot closes the round. The slot's own spacing history (P056, P060,
P064 → P068, spacing 4) confirms.

Domain chosen: **two-sided stable matching / the Gale–Shapley deferred-
acceptance mechanism** — a THIRTEENTH fleet-external domain, disjoint from the
twelve prior occupants (social choice P017, congestion routing P024,
tournament seeding P028, pattern races P032, optimal stopping P036, spatial
self-organization P040, queue discipline P044, stochastic ratchets P048,
occupancy & collection P052, random incidence P056, repeated-game reciprocity
P060, information cascades P064) and deliberately NOT adjacent to the last
unrelated slot's cascades/observational-learning domain. Dedup swept clean at
HEAD 1f304b0 (only word-collision hits: "marriage problem" inside the P036
secretary-problem dedup regex).

Deliverables this slice: this card (born-red first commit), the claim file,
`ideas/fleet/deferred-acceptance-proposer-advantage-2026-07-15.md` + the
`ideas/fleet/README.md` index row, the `control/outbox.md` PROPOSAL 068
append (append-only, real `date -u`, status sim-ready), and ONE terminal
claim prune (the P067 drafter — PR #430 verified merged at live GitHub
2026-07-15T06:26:58Z, merged_by github-actions[bot], this session before
deletion). Seeds 20261600–603 — allocated from 20261600 per the coordinator
relay (20261590–593 are P067/V080's registered set; the gap 20261594–599 is
the disclosed in-flight buffer). Arm R reporting-only.

## Constraints honored

- control/inbox.md untouched (manager-written); control/status.md untouched
  (no heartbeat housekeeping in this slice's scope). Newest inbox ORDER at
  HEAD is ORDER 015 (2026-07-15T03:37:08Z, EAP extended to 2026-07-21) — no
  ORDER newer than 015; the continuous-pipeline duty (ORDER 003/004) is the
  standing authority for this slice.
- Outbox: PROPOSAL 068 appended via shell (append-only, real `date -u`); the
  live file is ~72.5 KB post-ROLLOVER 002, well under the 200KB threshold —
  no rollover expected this append.
- control/outbox-archive-2026-07-14.md and control/outbox-archive-2026-07-15.md
  untouched (rolled archives, terminal).
- Claim prune is TERMINAL-only: PR #430 verified merged at live GitHub (mcp
  pull_request_read: merged 2026-07-15T06:26:58Z, merged_by
  github-actions[bot]) before deletion; zero open PRs at drafting.
- sim-lab and every source lane READ-ONLY; this repo edits no other repo
  (Q-0260).
- Seed sweep boundary-aware at HEAD 1f304b0: allocation starts at 20261600,
  strictly above P067/V080's registered 20261590–593 and the disclosed gap
  20261594–599; larger standalone numerals in-tree (20261664, 20261833,
  202670087) match the recorded discrimination rule — data, not seeds.
- The `📊 Model:` line above uses the kit's taught three-field payload.

## 💡 Session idea

**A constraint that admits more than one solution is not a decision — it is a
DELEGATION, and the thing you delegate to (here, "who proposes") spends the
slack in a direction you did not choose but can compute.** Drafting held two
genuine surprises, both found by running the full census live rather than
reasoning from the textbook. First, GAP-LOCALIZATION: the entire averaged
proposer advantage is EXACTLY zero on the 73% of n = 3 markets with a unique
stable matching and lives ENTIRELY on the 27% with more than one — so the folk
"stability pins it, side is a tie-break" belief is not merely approximately
right, it is EXACTLY right on nearly three-quarters of markets, which is
precisely why it is a durable-but-false intuition; the average, Δ = 7/27,
factors cleanly as P(multiplicity) × (conditional gap) = (131/486)·(126/131),
and the conditional gap is nearly a full choice-level (126/131 ≈ 0.96). The
transferable audit: before pricing any "our clearing procedure is neutral"
claim, MEASURE how often the constraint is single-valued — a market where the
stable outcome is almost always unique genuinely IS side-neutral, and the
side-neutrality claim's truth is exactly f(n); neutrality is not a property of
the RULE, it is a property of the INPUT DISTRIBUTION meeting the rule. Second,
the advantage is MARKET-SIZE-BORN, not a fixed constant: two exact points
(n = 2 vs n = 3) already show the gap, the multiplicity, AND the receiving
side's manipulability all growing — the same procedure is more directional in a
bigger market, so "it's just a tie-break" gets LESS true as the system scales,
the opposite of the intuition that big markets wash out corner cases. Kin to
P064's cascade knife-edge (a mechanism's leverage lives only at the process's
own boundary) — same moral, new object: there the boundary was the cascade
lead ±2, here it is the singleton set of the stable lattice; audit where an
intervention BINDS before pricing it. Fleet-local sting: any surface that
"just finds a stable/consistent assignment" (worker-to-task, reviewer-to-PR)
and calls the running side neutral is laundering a directional, computable tax
as fairness.

## ⟲ Previous-session review

Previous session (the P067 drafter, PR #430 @ `1f304b0`, merged
2026-07-15T06:26:58Z): a strong game-mechanics slice that carried the round's
recipe cleanly, and this slice consumed it three ways — (a) the born-red
card / three-field 📊 payload / terminal-prune-with-live-verification recipe
carried verbatim (this slice's P067-claim prune followed it exactly: PR #430
re-verified merged at live GitHub 06:26:58Z via mcp pull_request_read BEFORE
deletion, never trusting the local tree's staleness); (b) its seed-ledger
discipline (registered set + explicitly disclosed buffer gap) made this
session's allocation trivially safe — P067 registered 20261590–593 and
disclosed the 20261594–599 gap as the in-flight V080 buffer, so allocating
from 20261600 was mechanical and collision-free; (c) its "the committed law
makes the committed hook a rigged coin" framing — a folk claim priced against
the SYSTEM'S OWN structure — seeded this head's "the requirement is a
delegation, not a decision" lens. One nit, carried forward as a lesson this
slice acted on: P067's disclosed landing values were computed by an in-session
drafting sim but the numbers lived only in prose; this slice went one step
further and RAN the full exact census live (both arms) so every disclosed
rational (Δ = 7/27, f = 131/486, Δ|multi = 126/131, M_recv = 1/54) is a
measured value, not a hand estimate — a drafter that CAN run the exact object
in seconds should, so the disclosed landing is a genuine reproduction target
rather than a conjecture the verdict session must first sanity-check. No
correctness fault in P067; the nit is only "measure it if you can measure it
cheaply", and here it was cheap (~6 s stdlib).
