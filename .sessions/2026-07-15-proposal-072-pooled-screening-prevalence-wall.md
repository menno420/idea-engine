# Session — PROPOSAL 072: the pool test is not free — Dorfman batched screening has an exact prevalence wall (p\* = 1 − 3^(−1/3) ≈ 0.3066) above which every batch size loses, and the cautious pair-pool is dominated everywhere (completely-unrelated slot, round 14 closer, group testing)

> **Status:** `complete`
> **Model/time:** fable · 2026-07-15T09:11:03Z (Ideas Lab worker slice — draft the
> round-14 COMPLETELY-UNRELATED-domain rotation slot under standing owner ORDER
> 003/004; round 14 opened at fleet backlogs with P069 (#432), served venture with
> P070 (#434) and game mechanics with P071 (#435, merged 2026-07-15T08:55:30Z by
> github-actions[bot]), so the unrelated slot closes the round per ORDER 004
> rule 3. Slot spacing history confirmed: P056, P060, P064, P068 → P072
> (spacing 4).)

- **📊 Model:** fable-class · high · idea/planning

*(card born in-progress at 2026-07-15T09:11:03Z as the designed session-gate
hold; flipped complete in this PR's final commit. PR #436.)*

## Scope

Draft a genuinely new sim-shaped idea for the COMPLETELY-UNRELATED rotation
slot, round 14 closer, under standing owner ORDER 003 (continuous pipeline) and
ORDER 004 rule 3 ("fleet backlogs → venture's book/product space → game
mechanics → COMPLETELY UNRELATED domains — I want those too"). Domain chosen:
**screening design / combinatorial group testing — Dorfman two-stage pooled
testing**, a FOURTEENTH fleet-external domain, disjoint from the thirteen prior
unrelated-slot occupants (social choice P017, congestion routing P024,
tournament seeding P028, pattern races P032, optimal stopping P036, spatial
self-organization P040, queue discipline P044, stochastic ratchets P048,
occupancy & collection P052, random incidence P056, repeated-game reciprocity
P060, information cascades P064, two-sided matching P068) and deliberately
NON-adjacent to the last two unrelated slots' domains: no signals, no hidden
state, no sequential inference, no herd (vs P064's cascades), no two sides, no
preferences, no market (vs P068's matching) — this head prices a one-shot
TEST-ECONOMY design against prevalence.

Head: **the pooled-screening prevalence wall** — the batching folk belief
("pool the samples, test the pool, drill into positives — batching always
saves, and small pools are the safe hedge") against the exact two-stage cost
law T(n, p) = 1/n + 1 − (1 − p)^n. Three structure theorems, every one RUN
LIVE at drafting by exact enumeration (the V080 lesson): **T1 WALL** — pooling
helps for some n iff q = 1 − p > 3^(−1/3), i.e. p < p\* = 1 − 3^(−1/3) ≈
0.306566, certified purely by integer-power comparisons (3² = 9 > 8 = 2³,
3⁴ = 81 > 64 = 4³, 3⁵ = 243 > 125 = 5³, (n+1)^n < n^(n+1) for n ≥ 3 — and the
exact tie 2⁴ = 4²); above the wall EVERY pool size strictly loses. **T2
PAIR-DOMINANCE** — the exact polynomial identity T(2, q) − T(3, q) =
(q − 2/3)²(q + 1/3) + 1/54: the pair-pool is strictly dominated by the triple
at EVERY prevalence, minimum gap exactly 1/54 attained exactly at q = 2/3
(p = 1/3) — a named knife-edge equality cell. **T3 the 2–4 DEGENERACY** —
T(2, q) − T(4, q) = (q² − 1/2)² exactly: pool 4 weakly dominates pool 2
everywhere with a genuine MARGIN-0 knife-edge at q² = 1/2, where the two
break-even prevalences coincide exactly (because 2⁴ = 4²). Census anchors
computed exact-rational at drafting: n\*(1/100) = 11 with T\* ≈ 0.195571
(≥ 75% saving), n\*(1/10) = 4 with T\* = 5939/10000, last helping grid cell
p = 3/10 (T(3) = 2971/3000 ≈ 0.9903 — a 0.97% saving in the wall's shadow),
and at p = 2/5 the best practical pool (n ∈ {2..8}) still wastes ≥ 5%
(min = 419/375 ≈ 1.1173 at n = 3). The falsifiability world is one deleted
term: drop the pool test's own 1/n cost (the accounting slip the batching
instinct makes) and T̃ = 1 − q^n < 1 everywhere — the wall vanishes and the
verdict flips to APPROVE outright.

Deliverables this slice: this card (born-red first commit), the claim file,
`ideas/fleet/pooled-screening-prevalence-wall-2026-07-15.md` + the
`ideas/fleet/README.md` index row, the `control/outbox.md` PROPOSAL 072 append
(append-only, real `date -u`, status sim-ready), and ONE terminal claim prune
(the P071 drafter — PR #435 verified merged at live GitHub 2026-07-15T08:55:30Z,
merged_by github-actions[bot], this session before deletion). Seeds
20261640–643 — allocated from 20261640 per the coordinator relay (20261630–633
are P071/V084's registered set; the gap 20261634–639 is the disclosed in-flight
buffer). Arm R reporting-only seeded, aux 20261643 never read.

## Constraints honored

- control/inbox.md untouched (manager-written); control/status.md untouched
  (coordinator-only heartbeat). Newest inbox ORDER at HEAD is ORDER 015
  (2026-07-15T03:37:08Z, EAP extended to 2026-07-21) — no ORDER newer than
  015; the continuous-pipeline duty (ORDER 003/004) is the standing authority
  for this slice.
- Outbox: PROPOSAL 072 appended via shell (append-only, real `date -u`); the
  live file is ~116.7 KB pre-append, under the 200KB rollover threshold — no
  roll this append. Both dated archives untouched (rolled, terminal).
- Claim prune is TERMINAL-only: PR #435 verified merged at live GitHub (mcp
  pull_request_read: merged 2026-07-15T08:55:30Z, merged_by
  github-actions[bot]) before deletion; zero open PRs at drafting.
- Numbering verified at HEAD e17ebe7: newest PROPOSAL = 071 (live outbox +
  both dated archives swept); `PROPOSAL 072`/`proposal-072` collision-grepped
  clean (0 hits in live outbox, both archives, ideas/, docs/), zero open PRs.
- Fully hermetic (the P017–P068 unrelated-slot precedent): every model
  constant invented-but-pinned in the idea file, zero repo/network reads in
  the verdict session; grounding pin e17ebe7 is the dedup-sweep HEAD only.
  sim-lab dedup-swept READ-ONLY on a shallow clone @ bf398f91da63133d222c5af
  abcc15ac354e1e72c (VERDICT 083 newest, fetched 2026-07-15T09:08:22Z): zero
  domain hits for group-test/Dorfman/pooled-screen/prevalence terms. Local
  tree sweep at e17ebe7: zero domain hits; one word collision cited (P036's
  "candidate screening" at secretary-rule-cardinal-regret line 331 — a
  search-then-commit selection phrase, not pooled testing). This repo edits
  no other repo (Q-0260).
- Seed sweep boundary-aware at HEAD e17ebe7: genuine in-tree high-water
  20261633 (P071/V084's registered set 20261630–633); sim-lab genuine
  high-water 20261623 (V083's set); the numerals 20261664/20261833/202670087/
  2026964142 match the recorded data-not-seed discrimination rule (Fraction
  numerators and results-JSON digit runs). Allocation starts at 20261640,
  strictly above the registered set and the disclosed gap 20261634–639.
- Drafting-time verification discipline (the V080 lesson, the P068–P071
  norm): every theorem registered below RAN LIVE this session — the twin
  agreement (closed form vs full outcome-tree enumeration, exact-equal on a
  12 × 64 grid), the T1 integer-power wall certificates, the T2 and T3
  polynomial identities verified by exact coefficient match AND on a 101-point
  rational grid plus the q = 2/3 equality cell, all F3 census anchors
  (n\* and exact-rational T\* at nine prevalence cells), the F4 pencil world
  (p = 1/2 pool-2 → 5/4 exactly), the F5 degeneracies (p = 0 → 1/n, p = 1 →
  1 + 1/n, strict monotonicity), the REJECT margins (R1 ×1.0641, R3 ×1.2783,
  R2 floor attained with equality — disclosed), and an Arm-R Monte-Carlo
  preview on seed 20261640 (0.591920 vs exact 0.593900 at p = 1/10, n = 4,
  100,000 items). One structural hazard found at drafting and disclosed in
  the idea file: T(n, p) → 1⁺ as n → ∞ above the wall, so the quantified
  damage clause must be grid-bounded (the strict theorem T > 1 holds for ALL
  n; the ≥ 5% clause holds on the practical grid {2..8} — both registered in
  their honest forms, the n = 64 grid-tail value 1 + 1/64 − (3/5)^64 ≈
  1.015625 named).

## 💡 Session idea

**A drill-down design's entire economics can live in the one term the instinct
rounds to zero — so audit the "cheap" coordination cost FIRST, because it is
the threshold.** The Dorfman law's structure lesson generalizes past testing:
whenever a workflow pays a small per-batch overhead to buy a chance at
clearing the whole batch (a pool test, an aggregate CI leg, a combined lint
pass, one review over a stacked diff), the overhead term — here 1/n, the part
everyone calls "basically free" — is not a correction to the economics, it IS
the wall: delete it and batching wins everywhere at every failure rate; keep
it and there is an exact prevalence p\* above which every batch size loses,
computable by one multiplication. The drafting surprise worth keeping: the
folk belief's two halves fail in opposite styles — "always saves" fails at a
THRESHOLD (a wall you can locate exactly), while "small pools are the safe
hedge" fails EVERYWHERE (an identity with a 1/54 floor — the pair-pool is
never right at any prevalence, so caution expressed as smaller batches is a
theorem violation, not a preference). And the degeneracy rider: near
break-even, batch-of-2 and batch-of-4 tie EXACTLY (2⁴ = 4²), so an A/B test
there measures structural zero — check the family's algebra for exact ties
before spending measurements on a comparison the identity already settled.

## ⟲ Previous-session review

Previous session (the P071 drafter, PR #435 @ `e17ebe7`, merged
2026-07-15T08:55:30Z by github-actions[bot]): a clean game-slot slice whose
recipe this slice consumed and, in three places, extended — (a) the ceremony
carried verbatim (born-red card, three-field 📊 payload, terminal prune with
live merge verification via mcp pull_request_read BEFORE deletion, seed
ledger with the disclosed gap: its 20261630–633 + gap 20261634–639 made this
slice's allocation from 20261640 mechanical); (b) its print-discipline hazard
(exact large-rank rationals exceeding CPython's 4300-digit int-print default)
was INHERITED as pinned practice even though this head's largest numerator is
~23 digits — the fixture gates by in-memory Fraction equality first and
prints second, so the practice survives heads that do not need it; (c) its
live-verification doctrine (run both exact arms at drafting; V080 lesson) was
carried and this slice added a MARGIN LEDGER with registered knife-edges (the
V083 practice P071 cited for its margin disclosures, here extended to a
clause that attains its floor WITH EQUALITY at a named grid point, and a
second identity whose margin-0 cell is certified symbolically) — knife-edges
registered as disclosed structure at drafting rather than left for the
verdict session to discover. No correctness fault found in P071's landing:
its PR #435 merge claim, its seed ledger (numerals 20261630–633 in-tree
exactly where its claim said, nothing ≥ 20261640 anywhere), and its
newest-PROPOSAL = 071 numbering claim were all re-verified live this session
and held. One continuity note for the coordinator: P071's card said "round 14
opened at fleet backlogs with P069 (#432) and served venture with P070
(#434)" — this slice confirms the rotation arithmetic and closes round 14 at
the unrelated slot, so round 15 opens at fleet backlogs.
