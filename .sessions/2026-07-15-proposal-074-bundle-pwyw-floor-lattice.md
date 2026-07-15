# Session — PROPOSAL 074: one field decides the lattice — the queued template-pack publish click leaves the PWYW minimum "owner's choice" with no committed value, and that single unpinned floor is what decides whether the committed Ship-It Bundle triple ($49 kit + $19-suggested PWYW pack vs $59 bundle, "saves $9") is coherent pricing or a $10 strategic surcharge (venture slot, round 15, PRODUCTS half, venture-lab)

> **Status:** `in-progress`
> **Model/time:** fable · 2026-07-15T10:23:28Z (Ideas Lab worker slice — draft the
> round-15 VENTURE rotation slot under standing owner ORDER 003/004; round 15
> opened at fleet backlogs with P073 (#437, merged 2026-07-15T09:59:51Z by
> github-actions[bot]), so the venture slot is next per ORDER 004 rule 3.
> Half-alternation puts round 15 on the PRODUCTS half (P070 was BOOKS); slot
> spacing history confirmed: P062, P066, P070 → P074 (spacing 4). The P073
> drafter's baton says the same and was consumed.)

- **📊 Model:** fable-class · high · idea/planning

*(card born in-progress at 2026-07-15T10:23:28Z as the designed session-gate
hold; flips complete in this PR's final commit.)*

## Scope

Draft a genuinely new sim-shaped idea for the VENTURE rotation slot, round
15, PRODUCTS half, under standing owner ORDER 003 (continuous pipeline) and
ORDER 004 rule 3. Products-half priors re-read this session: P042 (channel
allocation), P050 (kill-clock dial), P058 (rubric weight robustness), P066
(kill-clock anchor / exposure truncation) — plus the four served pricing
verdicts V037/V039/V040/V041 swept READ-ONLY at sim-lab `2370855`.

Head: **the bundle/PWYW floor-coherence lattice.** The committed catalog
ships a fixed $49 kit (`candidates/membership-kit/LISTING.md:46`), a
$19-suggested PWYW pack (`candidates/template-packs/LISTING.md:61`), and a
$59 fixed bundle whose committed copy claims "it saves $9 and one checkout"
(`candidates/BUNDLE-LISTING.md:73-74`) — all @ venture-lab `520bdfc`. The
pack's PWYW MINIMUM is the one unpinned field: the queued ⚑D publish click
commits "price set ($19 pay-what-you-want suggested (default); minimum
owner's choice)" (`docs/publishing/OWNER-QUEUE.md:162`), and sim-lab V040's
own gap register G2 records verbatim that "the PWYW minimum is an owner
choice with NO committed value". Three exact structure theorems, every
registered numeral RAN live by the drafting script this session (V084
NO-DERIVED-LITERALS lesson; closed forms + independently-written
integer-cent brute-force twins, exact agreement): **T1 BASIS GAP** —
advertised saving minus achievable saving = s − f exactly, independent of
both the kit price and the bundle price (at the f = 0 default the committed
"$9" copy overstates the achievable saving by exactly $19 = s, the
achievable saving being −$10: a strategic surcharge); **T2 COHERENCE
WINDOW** — a fixed bundle over {fixed a, PWYW floor f} is lattice-coherent
iff p ∈ [a, a + f], so f*(p) = p − a: the committed $59 needs f ≥ 10
(strictly more than half the suggested price, ratio 20/19), V040's parked
$64 needs f ≥ 15, and V040's banned $68 needs f ≥ 19 = s EXACTLY — the
banned anchor coheres only when the PWYW knob is dead ink (margin-0
contact, an independent lattice re-derivation of V040's ban); **T3 FEE
INVARIANT** — under the committed affine fee schedule (net(P) = 0.871·P −
0.80, `candidates/photo-packs/MARKET-PLAN.md:17-19`, V040's committed
reading) the seller nets exactly +$9.51 per both-buyer routed to the bundle
at f = 0 while that buyer pays $10 over their achievable path, the ONLY
f-independent genuine saving in the system is the second $0.80 fixed fee
(accruing to the SELLER — "one checkout" is worth exactly $0.80 and not to
the buyer), and the f = s cell reproduces V040's committed $7.039 nudge
cost exactly (Δ(19) = −7039/1000).

Deliverables this slice: this card (born-red first commit), the claim file,
`ideas/venture-lab/bundle-pwyw-floor-lattice-2026-07-15.md` + the
`ideas/venture-lab/README.md` index row, the `control/outbox.md` PROPOSAL
074 append (append-only, real `date -u`, status sim-ready), and ONE
terminal claim prune (the P073 drafter — PR #437 verified merged at live
GitHub 2026-07-15T09:59:51Z, merged_by github-actions[bot], this session
before deletion). Seeds 20261660–663 — allocated from 20261660 (20261650–653
are P073/V086's registered set; the gap 20261654–659 is the disclosed
in-flight buffer). Arm R reporting-only seeded 20261660/661/662, aux
20261663 never read.

## Constraints honored

- control/inbox.md untouched (manager-written); control/status.md untouched
  (coordinator-only heartbeat). Newest inbox ORDER at HEAD is ORDER 015
  (2026-07-15T03:37:08Z, EAP extended to 2026-07-21) — no ORDER newer than
  015 (checked at sync, 2026-07-15T10:11:20Z); the continuous-pipeline duty
  (ORDER 003/004) is the standing authority for this slice.
- Outbox: PROPOSAL 074 appended via shell (append-only, real `date -u`); the
  live file is ~152 KB pre-append, under the 200KB rollover threshold — no
  roll this append. Both dated archives untouched (rolled, terminal).
- Claim prune is TERMINAL-only: PR #437 verified merged at live GitHub (mcp
  pull_request_read: merged 2026-07-15T09:59:51Z, merged_by
  github-actions[bot]) before deletion; zero open PRs at drafting
  (list_pull_requests state=open → []).
- Numbering verified at HEAD 63c75cf: newest PROPOSAL = 073 (live outbox +
  both dated archives swept, rc=1 on `PROPOSAL 074` in the archives);
  `PROPOSAL 074`/`proposal-074` collision-grepped clean (0 hits in
  control/, ideas/, docs/), zero open PRs.
- Grounding FIRSTHAND (Q-0272 git transport): venture-lab shallow clone at
  live HEAD 520bdfca71ca4f119808d1098cd4ecf7fc6e6732 (fetched
  2026-07-15T10:13:36Z — the SAME pin P066/P070 grounded at; the lane has
  not moved, so the pin is current, and this head reads three documents
  neither prior tapped for its decision object) — every harvested constant
  quoted verbatim with file:line in the idea file. The verdict session is
  fully hermetic: every constant pinned in the idea file, zero repo/network
  reads at verdict time (the P017–P073 precedent). This repo edits no other
  repo (Q-0260).
- sim-lab dedup-swept READ-ONLY on a shallow clone @
  23708552a730d61fbe7fce82610ac0afc54484e2 (fetched 2026-07-15T10:17:34Z):
  the four pricing verdicts read in full — V040 priced the bundle ANCHOR
  {59, 64, 68} holding the pack at its suggested $19 and registered the
  PWYW minimum as unserved gap G2 verbatim; V039 priced a SAME-product
  two-pack seller-net band (its floor $3 is committed, the family's one
  pinned-floor world); V041 priced single-product $19-vs-PWYW mode with
  min-0 taker mechanics; V037 serial pricing. No verdict and no proposal
  prices the CROSS-product dominance lattice or the floor knob — argued in
  the idea file's Relations section.
- Seed sweep boundary-aware at HEAD 63c75cf: genuine in-tree high-water
  20261653 (P073/V086's registered set 20261650–653); the numerals
  20261664/20261833 match the recorded data-not-seed discrimination rule
  (Fraction numerators and results-JSON digit runs, disclosed in prior
  cards). Allocation starts at 20261660, strictly above the registered set
  and the disclosed gap 20261654–659.
- Drafting-time verification discipline (the V080 live-verify rule + the
  V084 NO-DERIVED-LITERALS lesson): every numeral registered in the idea
  file was PRODUCED by the drafting script this session (scratchpad
  `draft_p074.py`, ALL PASS, exit 0) — the f* table {10, 15, 19}, the
  margin ratios 20/19 and 10/9, the census table over the full floor grid
  (coherence, achievable saving, premium, basis gap, seller delta per
  cell), the V040 external-anchor reproductions (nets 50589/1000,
  41879/1000, 54944/1000 = 6868/125, 58428/1000 = 14607/250; the +$0.80
  row; the retention bar 50589/54944; the nudge cost −7039/1000), the f = 1
  mirror knife-edge (premium 9 = the advertised saving exactly), the pencil
  world (a=3, s=2, p=4), and the Arm-R previews (seed 20261660: 19878
  bundle-takes of 50,000, exact expectation 2/5; seed 20261661: 15946 of
  20,000, exact expectation 4/5; exact mean outlays 53 and 57). Zero
  hand-derived or scaled numerals anywhere in the registered set.
