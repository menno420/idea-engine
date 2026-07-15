# Session — PROPOSAL 076: the check digit's exact blind spot — no position-wise mod-10 scheme catches every adjacent swap (the floor is exactly 2 of 90 ordered pairs, proven over all 3,628,800 digit-map quotients, and Luhn attains it on precisely 09↔90), and the ISBN-10 → EAN-13 migration strictly WEAKENED transposition detection (0 → 10/90 adjacent, 0 → 90/90 at distance 2) (unrelated slot, round 15 CLOSER, check-digit design)

> **Status:** `in-progress`
> **Model/time:** fable · 2026-07-15T11:27:28Z (Ideas Lab worker slice — draft the
> round-15 COMPLETELY-UNRELATED-domain rotation slot under standing owner ORDER
> 003/004; round 15 opened at fleet backlogs with P073 (#437, merged
> 2026-07-15T09:59:51Z), served venture with P074 (#438, merged
> 2026-07-15T10:32:39Z) and game mechanics with P075 (#439, merged
> 2026-07-15T11:09:44Z by github-actions[bot]), so the UNRELATED slot closes the
> round per ORDER 004 rule 3. Slot spacing history confirmed: P017/P020, P024,
> P028, P032, P036, P040, P044, P048, P052, P056, P060, P064, P068, P072 → P076
> (spacing 4).)

- **📊 Model:** fable-class · high · idea/planning

*(card born in-progress at 2026-07-15T11:27:28Z as the designed session-gate
hold; flipped complete in this PR's final commit.)*

## Scope

Draft a genuinely new sim-shaped idea for the COMPLETELY-UNRELATED-domain
rotation slot, round 15 closer, under standing owner ORDER 003 (continuous
pipeline) and ORDER 004 rule 3 ("COMPLETELY UNRELATED domains — I want those
too"). Prior unrelated-slot domains re-read this session (all fourteen): social
choice (P017), congestion routing (P024), tournament seeding (P028), pattern
races (P032), optimal stopping (P036), spatial self-organization (P040), queue
discipline (P044), stochastic ratchets (P048), occupancy & collection (P052),
random incidence (P056), repeated-game reciprocity (P060), information cascades
(P064), two-sided matching (P068), group testing / screening design (P072). The
FIFTEENTH domain: **algebraic error detection — check-digit design over decimal
identifiers** (Luhn / weighted mod-10 / ISBN-10 mod-11 / the Damm quasigroup),
deliberately non-adjacent to the last three occupants: no signals, no beliefs,
no sequential inference (vs P064's cascades); no sides, no preferences, no
market (vs P068's matching); no probability, no prevalence, no subset queries
(vs P072's group testing — that head priced a STOCHASTIC screening economy;
this one is deterministic algebra on a single codeword).

Head: **the transposition floor.** Any position-wise decimal check equation
Σ σ_i(d_i) ≡ 0 mod 10 (each σ_i a digit permutation — Luhn's doubling fold is
the i odd case, plain weights are the linear case) detects an adjacent swap at
boundary i iff y ↦ σ_i(y) − σ_{i+1}(y) mod 10 is injective. It never is: the
ten values sum to 0 mod 10, a permutation's values sum to 45 ≡ 5 — the
one-line certificate. Drafting enumerated ALL 3,628,800 quotient permutations
(scratchpad `draft_p076.py`, 50/50 checks PASS, exit 0): min undetected
ordered pairs per boundary = 2, attained by 46,400 quotients, Luhn among them
(its miss set exactly {(0,9),(9,0)}); every all-singles LINEAR cell (the 16
unit-weight pairs) misses 10 (off-diagonal, 12 cells) or 90 (diagonal, 4
cells) — nonlinearity buys 5×, never zero. ISBN-10 (mod 11): 0 undetected
substitutions AND 0 undetected transpositions at EVERY distance; EAN-13
(alternating 1,3): 10/90 per adjacent boundary and 90/90 at distance 2 — the
2007 book-number migration strictly weakened detection in both transposition
classes. The Damm quasigroup table (pinned, verified live: rows/columns
permutations, zero diagonal) achieves 0/900 on the same 10 symbols — the
barrier is the abelian-linear algebra, not the alphabet.

Deliverables this slice: this card (born-red first commit), the claim file,
`ideas/fleet/check-digit-transposition-floor-2026-07-15.md` + the
`ideas/fleet/README.md` index row, the `control/outbox.md` PROPOSAL 076 append
(append-only, real `date -u`, status sim-ready), and ONE terminal claim prune
(the P075 drafter — PR #439 verified merged at live GitHub 2026-07-15T11:09:44Z,
merged_by github-actions[bot], this session before deletion). Seeds
20261680–683 — allocated from 20261680 per the coordinator relay (20261670–673
are P075's registered set; the gap 20261674–679 is the disclosed in-flight
buffer). Arm R reporting-only seeded 20261680/681/682, aux 20261683 never read.

## Constraints honored

- control/inbox.md untouched (manager-written); control/status.md untouched
  (coordinator-only heartbeat). Newest inbox ORDER at HEAD is ORDER 015
  (2026-07-15T03:37:08Z, EAP extended to 2026-07-21) — no ORDER newer than 015
  (checked at sync, 2026-07-15T11:15:03Z); the continuous-pipeline duty
  (ORDER 003/004) is the standing authority for this slice.
- Outbox: PROPOSAL 076 appended via shell (append-only, real `date -u`); the
  live file was 166,054 B pre-append — under the 200KB rollover threshold, no
  roll this append. Both dated archives untouched (rolled, terminal).
- Claim prune is TERMINAL-only: PR #439 verified merged at live GitHub (mcp
  pull_request_read: merged 2026-07-15T11:09:44Z, merged_by github-actions[bot])
  before deletion; zero open PRs at drafting (list_pull_requests state=open →
  []).
- Numbering verified at HEAD 87bbb39: newest PROPOSAL = 075 (live outbox tail +
  both dated archives swept); `PROPOSAL 076`/`proposal-076` collision-grepped
  clean; zero open PRs; the only claim on file was P075's (pruned this PR after
  live merge verification).
- Grounding: this head is FULLY HERMETIC (the P017–P072 unrelated-slot
  precedent) — every model constant is invented-but-pinned in the idea file,
  zero repo/network reads at verdict time; the grounding pin is the dedup-sweep
  HEAD of this repo only. sim-lab dedup-swept READ-ONLY on a shallow clone @
  d6610dc (fetched 2026-07-15T11:22:09Z, newest VERDICT 087): zero domain hits
  for check digits / Luhn / Damm / ISBN / quasigroups; word collisions cited in
  the idea file's Dedup (verdict-050's game save-file checksum mirror,
  verdict-073's exchange-argument "transpositions"). This repo edits no other
  repo (Q-0260).
- Seed sweep boundary-aware at HEAD 87bbb39: genuine in-tree high-water
  20261673 (P075's registered set 20261670–673); the sim-lab clone's genuine
  high-water 20261663 (V087's set) with 20261664 re-confirmed DATA-not-seed by
  the recorded discrimination rule (as are 20261833 / 202670087 / 2026964142).
  Allocation starts at 20261680 per the coordinator relay, strictly above the
  registered set and the disclosed gap 20261674–679.
- Drafting-time verification discipline (V080 live-verify + V084
  NO-DERIVED-LITERALS): every numeral registered in the idea file was PRODUCED
  by the drafting script this session (`draft_p076.py`, 50/50 PASS, exit 0,
  stdlib-only, ~10 s): the full 10! census (min 2 / 46,400 minimizers / max 90
  on exactly the 10 rotations / histogram total 3,628,800 / no zero), the
  sum-certificate, the 16-cell linear grid {4×90, 12×10}, the ISBN-10 0/0 and
  the 11-ary length-4 full enumeration (1331 valid, 0/0), the EAN censuses
  {10/90, 90/90, 120, 990} and its length-4 word-level {1000, 0, 300, 1800},
  the Luhn censuses {2, (0,9)/(9,0), 1000, 0, 60}, the Damm verifications
  {rows/cols/diagonal, 0/900, 0/900, 958/9000 reporting, 1000/0/0}, the
  degeneracy controls {90, 90}, the pencil worlds, and the Arm-R preview (seed
  20261680: 412/17954, 1948/18026, 17966/17966, 600,000 draws counted). One
  drafting-run hand-fact correction disclosed in the idea file (the
  ordered-vs-unordered word-level contact factor). Zero hand-derived or scaled
  numerals anywhere in the registered set.
