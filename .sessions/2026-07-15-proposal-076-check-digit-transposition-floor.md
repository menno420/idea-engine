# Session — PROPOSAL 076: the check digit's exact blind spot — no position-wise mod-10 scheme catches every adjacent swap (the floor is exactly 2 of 90 ordered pairs, proven over all 3,628,800 digit-map quotients, and Luhn attains it on precisely 09↔90), and the ISBN-10 → EAN-13 migration strictly WEAKENED transposition detection (0 → 10/90 adjacent, 0 → 90/90 at distance 2) (unrelated slot, round 15 CLOSER, check-digit design)

> **Status:** `complete`
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
hold; flipped complete in this PR's final commit. PR #440.)*

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

## 💡 Session idea

**When a claimed impossibility has a small finite scope, don't cite it — EXHAUST
it: a complete census of the whole function space costs seconds, upgrades the
theorem from "known" to "counted", and hands the verdict session a
falsifiable object (the histogram) instead of an authority.** The floor-2
theorem is classical folklore; what drafting added is that all 3,628,800
quotient permutations were counted live, which simultaneously (a) proved the
one-line certificate against its own exhaustive confirmation, (b) named the
attaining set (46,400 — Luhn is not just good, it is ON the floor, so every
"improved mod-10" pitch is refutable by census), and (c) surfaced structure
nobody asked for (the histogram's even-only support with gaps above 44). The
drafting surprise worth keeping: the enumeration CAUGHT A REAL DRAFTER ERROR —
the hand-derived word-level contacts were the unordered counts (30/150/900),
off by exactly the two directions of a swap; the full enumeration returned
60/300/1800 and the corrected multiplicity law became a typed must-equal gate
plus its own pre-registered NULL axis. Transferable audit, one sentence: when
a detection/validation instrument is adopted ("it has a check digit", "CI
covers that"), ask for its miss SET, not its existence — the miss sets here
are tiny, structured, and named (Luhn = {09↔90}; EAN-13 = five twin pairs
adjacent plus EVERYTHING at distance 2), and a named miss set is actionable
where "mostly works" is not. Pattern name for the battery: EXHAUST-THE-SCOPE
census (complete function-space enumeration as the gate on a cited theorem).

## ⟲ Previous-session review

Previous session (the P075 drafter, PR #439 @ `87bbb39`, merged
2026-07-15T11:09:44Z by github-actions[bot]): a clean game-slot landing whose
recipe this slice consumed and, in two places, extended — (a) the ceremony
carried verbatim (born-red card, three-field 📊 payload, terminal prune with
live merge verification via mcp pull_request_read BEFORE deletion, seed ledger
with the disclosed gap: its 20261670–673 + gap 20261674–679 made this slice's
allocation from 20261680 mechanical); (b) its disclosed-drafting-correction
practice (P075's ghost-law `elif` hand-fact fixed by enumeration) recurred
here in a stronger form — this slice's ordered/unordered contact error was not
only disclosed but PRE-REGISTERED as its own NULL axis, upgrading "the drafter
corrected himself" into "the verdict session can rule on exactly this error
class"; and (c) its HINT-DOMINATION audit pattern (diff the absence-branch
against the presence-branch) has a sibling here — diff the ADVERTISED coverage
against the ENUMERATED census. No correctness fault found in P075's landing:
its PR #439 merge claim, its seed ledger (20261670–673 in-tree exactly where
its claim said, nothing ≥ 20261680 anywhere), its newest-PROPOSAL = 075
numbering, and its round-15 baton ("the UNRELATED slot (P076) closes the round
per ORDER 004 rule 3") were all re-verified live this session and held — this
slice consumed that baton. Continuity notes for the coordinator: round 15 is
now FULLY SERVED (P073 fleet #437, P074 venture #438, P075 game #439, P076
unrelated #440) — round 16 opens at the fleet-backlogs slot with P077 per
ORDER 004 rule 3; the game slot's source-rotation record still reads gba
r6/r7, superbot r8/r9, mineverse r10, idle r11, games r12, gba r13, superbot
hub r14, mineverse r15, so round 16's game tap (P079) falls due on
SUPERBOT-IDLE by least-recently-drawn (P075's baton, unchanged); the
unrelated-slot domain ledger now holds FIFTEEN entries ending …cascades →
matching → group testing → algebraic error detection, and the next unrelated
closer (P080) must argue non-adjacency against at least the last three
(matching, group testing, error detection); seed high-water after this PR:
20261683 (P076's registered set 20261680–683), next free block 20261690 if
the in-flight-buffer convention holds (gap 20261684–689 to disclose).
