# The fail-safe with one eye: the owner-gate parser's both-marks asymmetry ("a stray checkbox edit can only ever RE-QUEUE an owner action, never silently drop one" — the sold GOTCHAS.md #4 sentence) is real on its own disposition grid and inverted everywhere else — recognition is an unguarded four-way conjunction (⚑-prefix ∧ literal `**Owner:**` ∧ `- [ ]` shape ∧ flush-left position) where 18 of 26 registered single-edit cells silently drop an owner click, an owner decision, or a kill-clock checkpoint, the strict lint passes every one of them clean (every lint check fires only AFTER recognition — the guard and the hazard share one predicate), and one lost asterisk on the DONE row disarms both armed kill-clock checkpoints in the same silent edit

> **State:** sim-ready
> **Class:** venture (pipeline rotation — the standing ORDER 003 VENTURE slot,
> round 17, PRODUCTS half on the slot's own half-alternation read from the
> actual sequence: P018 books → P022/P026 trading → P030 books → P034 trading
> → P038 books → P042 products → P046 books → P050 products → P054 books →
> P058 products → P062 books → P066 products → P070 books → P074 products →
> P078 books, so r17 = PRODUCTS due; round 17 opened at fleet backlogs with
> P081 (#448 → VERDICT 094 REJECT), so the venture slot is next per ORDER 004
> rule 3, confirmed against the slot's own spacing history (…P066, P070,
> P074, P078 → P082, spacing 4).)
> **Target:** `menno420/sim-lab` (verification target per the Q-0264 pipeline; the
> deliverable is a committed stdlib sim + a citable measured verdict — no lane build).
> Verdict consumer: menno420/venture-lab — the lane owns both parser copies, the
> derived owner queue, the kill-clock checker that imports the same parser, and the
> $19 product whose zip sells the sentence.
> **Grounding:** https://github.com/menno420/venture-lab@95e18469aedad37f37f74a69eed17dd7dc002bcf · fetched 2026-07-16T08:23:04Z
> (FIRSTHAND pin, public shallow clone read this session — the P058/P062/P066/P074/P078
> precedent; every quoted parser behavior lives in this tree TWICE:
> `candidates/owner-click-queue-kit/ocq.py` (the sold copy) and
> `scripts/derive_owner_queue.py` (the production copy — recognition predicate
> verbatim-identical at its lines 215/221), plus `scripts/check_kill_clocks.py`
> which imports `parse_packet` from the production copy. The sim itself is fully
> hermetic: zero repo/network reads at verdict time, every fixture constructed
> in-sim from the pinned constants and the registered corpus in this file.)

**Origin:** drafted this slice under the standing owner ORDER 003 (continuous
pipeline) and ORDER 004 rule 3's rotation — round 17 opened at the
fleet-backlogs slot (PROPOSAL 081, PR #448), so this slice serves the VENTURE
slot, products half. The harvested object is the products lane's own control
surface: the OWNER-GATE grammar and its tolerant-derive + strict-lint parser
pair, distilled into the sellable Owner-Click Queue Kit ($19, BUILD #2 of the
2026-07-13 ideation batch) and running in production as
`scripts/derive_owner_queue.py` → `docs/publishing/OWNER-QUEUE.md` (26 vetting
packets ride it; the OCQK packet's own §7 block is parsed by the same script —
"recursion as evidence", `docs/publishing/vetting/owner-click-queue-kit.md` §1).

## The folk belief

The kit's own GOTCHAS.md #4, sold in the buyer zip and titled "The DONE flip
needs BOTH marks — the asymmetry is the feature", verbatim: "That is the
correct direction of failure: a stray checkbox edit (agents reflow markdown
all the time) can only ever RE-QUEUE an owner action, never silently drop
one." The same claim ships in the code twice — ocq.py's regex comment ("BOTH
marks are required — a checked box without DONE still queues, and an unchecked
box carrying DONE text still queues") and the parse-site comment ("still
QUEUES in derive (fail-safe: never silently drop an owner action)") — and the
vetting packet's §1 sells the evidence: a 38-test suite "covering … lint (all
strict failures incl. half-flipped DONE rows …) and hostile inputs". The
load-bearing corollary, uninspected: that the strict `lint` — the mode "you
gate a pull request on" — sees what the tolerant `derive` drops. It cannot:
every lint error class fires on rows the parser has already RECOGNIZED (or on
a whole file with no gate section), so an edit that breaks recognition rather
than disposition is invisible to both modes at once. The both-marks asymmetry
guards the two DISPOSITION bits; recognition is a four-way conjunction —
flag-first ∧ literal-bold-token ∧ checkbox-shape ∧ flush-left — and every
conjunct is a single stray-edit away from a silent drop, in exactly the "agents
reflow markdown all the time" world the sentence itself invokes.

## The mechanism (reasoned to its fuller form — Q-0254 duty)

The shipped parser, pinned verbatim from the harvested source (five named
behaviors): **(i) recognition** — an owner row is a folded checkbox item whose
text satisfies `text.lstrip().startswith("⚑") and "**Owner:**" in text`
(ocq.py `is_owner_row`; derive_owner_queue.py lines 215/221 identical);
**(ii) row shape** — `^- \[[ xX]\]\s+` at line start (bullet `-`, one space,
single-char state, `]`, whitespace); **(iii) fold rule** — indented non-empty
lines fold into the OPEN item of the same regex class, a non-matching
flush-left line closes the item, and an indented line with NO open item is
invisible; **(iv) disposition** — `[—–-]\s*DONE\s+\d{4}-\d{2}-\d{2}`
(case-sensitive) on CHECKED rows only moves a row to Live; the half-flipped
cells still queue AND lint red (the both-marks rule); **(v) section + arming**
— the gate section runs from the first h2 matching `^##\s.*OWNER-GATE`
(case-insensitive) to the next h2; `^KILL-CHECK:` heads the checkpoint line;
checkpoints ARM only when the group has ≥ 1 recognized DONE row ("a kill clock
only ticks once live" — check_kill_clocks.py's stated rule, inherited by
import). Model: a registered canonical gate file C0 (pinned verbatim in the
fixture; modeled on the OCQK packet's own §7: 3 numbered steps of which 1 is a
⚑ decision with a marked default, 4 pending ⚑ **Owner:** rows of which one
carries an indented continuation with the word "(blocking)", 1 checked DONE
row, 1 non-owner seat row — excluded BY DESIGN, the
`test_only_owner_rows_become_clicks` contract — and 1 KILL-CHECK line with 2
⏲ checkpoints), two variant corpora (C1 = C0 minus the DONE row; C2 = C0 with
a second flagged decision), and a 26-cell registered single-edit mutation grid
(14 operators × named targets). EVERY registered numeral below was produced by
the drafting script this session (V080 live-verify + V084 NO-DERIVED-LITERALS,
scratchpad `draft_p082.py`, **119/119 checks PASS, exit 0, ~15 s**), twin-verified
(Arm A regex-faithful replay == Arm B independently-written character-level
classifier + explicit fold walk, exact on every observable of every cell).
**Baseline (C0):** 3 steps · 1 decision · 4 pending · 1 done · 1 non-owner ·
2 checkpoints parsed, 2 armed · blocked=True · lint 0 · manual 0; conservation
4+1+1 == the file's 6 checkbox rows. **The census:** of the 26 cells, exactly
**18 land SILENT-LOSSY** (a pending click, a decision, a DONE row, or an armed
checkpoint is LOST with lint == 0 AND manual == 0), 3 ALARMED-LOSSY, 4
ALARMED-SAFE, 1 SILENT-REGRADE. The silent eighteen: one lost asterisk
(`**Owner:**` → `*Owner:**`, OP1) drops the row at all 5 targets; bolding the
flag (`⚑ **Owner:**` → `**⚑ Owner:**`, OP2) drops all 5; one leading space
(OP3) makes the row vanish when the line above is closed (pending 4→3) or MERGE
into the click above when it is open (pending 4→3 with the neighbor's WHAT
text swallowing the lost click — both position cells registered); a bullet
swap `- [` → `* [` (OP4) drops all 3 targets; bracket damage `- [ ]` → `- []`
(OP5) drops; deleting the ⚑ from the decision step (OP6) silently deletes the
DECISION from queue §1; and `KILL-CHECK:` → `KILL CHECK:` (OP12) silently
disarms BOTH checkpoints. **The cascade:** the three silent cells that hit the
DONE row (OP1@r5, OP2@r5, OP4@r5) each land done 0 · armed 0 · lint 0 — one
character on one row disarms every kill-clock checkpoint of the launch,
because arming is gated on a recognized DONE row (the once-live rule; C1
registers the rule directly: 2 parsed, 0 armed). check_kill_clocks.py reads
checkpoints through this exact parser, so the T+7/T+30 clocks go dark in the
same silent edit. **The true sentence survives:** the disposition 2×2 the
GOTCHA actually describes is exactly fail-safe — (unchecked, no DONE) NO-OP ·
(checked, no DONE) still queues + lint 1 · (unchecked, DONE) still queues +
lint 1 · (checked, valid DONE) retires to Live with lint 0 — zero silent cells
on the sentence's own grid, and lowercase `done` (OP11) re-queues the CLICK
exactly as promised (pending 4→5, lint 1) while silently disarming the clock
it rode (done 0, armed 0). **The granularity inversion:** breaking the file
(heading demote `##` → `###`, OP13) is GUARDED — manual 1, lint 1, the whole
file lands in Manual review; breaking a ROW is silent. The parser fails safe
at file granularity and fails open at row granularity, and the lint — sold as
the strict half — is blind at exactly the row grain because it shares the
deriver's recognition predicate. **The repair is one function:** a
conservation lint that counts a LOOSER net (any bullet-ish or ⚑ line whose
markup-stripped text contains "owner:"; any numbered step containing
"(default"; any ⏲ line containing "kill") and errors when strict recognition
counts fewer — measured on the registered grid it catches **18/18 SILENT-LOSSY
cells** plus 2 of the 3 alarmed-lossy, with **0 false positives on all three
clean corpora**, and misses only the one SILENT-REGRADE cell (deleting the
word "(blocking)" silently un-gates the ordering — a semantic edit no net
predicate sees; disclosed open).

## Pinned model (committed constants — all pinned)

- Source behaviors, verbatim from the harvested surface (both copies): the five
  named behaviors (i)–(v) above; the regexes `^- \[[ xX]\]\s+(.*)$`,
  `[—–-]\s*DONE\s+(\d{4}-\d{2}-\d{2})`, `^KILL-CHECK:\s*(.*)$`,
  `^##\s.*OWNER-GATE` (IGNORECASE); the predicate
  `text.lstrip().startswith(FLAG) and "**Owner:**" in text`; the once-live
  arming rule; lint's error classes (half-flips both directions, invalid DONE
  date, defaultless flagged decision, no-H1, no-gate-section, no-rows,
  malformed KILL-CHECK token) — every class conditioned on recognition.
- Corpus C0: the 21-line canonical gate file, pinned VERBATIM in the fixture
  (registered baseline tuple above); C1 = C0 minus line 18 (the DONE row);
  C2 = C0 with step 1 flagged + a `**…** (default)` marker (baseline: 2
  decisions, lint 0).
- The 26-cell grid: OP1 star-loss ×5 rows · OP2 flag-fold ×5 · OP3 indent ×
  {r1, r2, r5} · OP4 bullet-swap × {r1, r3, r5} · OP5 bracket-damage @r1 ·
  OP6 step-flag-removal @step2 · OP7 default-marker-damage @step2 · OP8
  check-without-DONE @r1 · OP9 DONE-on-unchecked @r2 · OP10 invalid-DONE-date
  @r5 · OP11 DONE-case-flip @r5 · OP12 KILL-CHECK-prefix @kill · OP13
  heading-demote @heading · OP14 blocking-word-deletion @cont4. Every operator
  is a deterministic single edit; a cell must differ from its corpus (the
  real-edit sentinel).
- Registered census anchors (F3): class totals **{SILENT-LOSSY 18,
  ALARMED-LOSSY 3, ALARMED-SAFE 4, SILENT-REGRADE 1}**; the SILENT-LOSSY list
  verbatim {OP1@r1–r5, OP2@r1–r5, OP3@r1, OP3@r2, OP4@r1, OP4@r3, OP4@r5,
  OP5@r1, OP6@step2, OP12@kill}; key cell tuples — OP1@r1 (pending 3, done 1,
  armed 2, lint 0) · OP1@r5/OP2@r5/OP4@r5 (pending 4, done 0, armed 0, lint 0)
  · OP3@r1 vanish and OP3@r2 merge (both pending 3; the merged WHAT contains
  both clicks' text — containment asserted) · OP3@r5 (pending 4, done 0,
  armed 0, lint 1 — the merged unchecked row carries DONE text, the half-flip
  lint fires) · OP11@r5 (pending 5, done 0, armed 0, lint 1) · OP12 (parsed 0,
  armed 0, lint 0) · OP13 (pending 0, manual 1, lint 1) · OP10 (done 1,
  armed 2, lint 1); the 2×2 tuple row (NO-OP · queue+lint 1 · queue+lint 1 ·
  RETIRE-LIVE pending 3/done 2/lint 0); repair census 18/18 caught + {OP3@r5,
  OP13} + 0 false positives on {C0, C1, C2} + missed {OP14}; C1 once-live
  (parsed 2, armed 0).
- Arm A (DECISION, seedless): the faithful replay of behaviors (i)–(v),
  regex-ported. Arm B (twin, seedless, INDEPENDENTLY-WRITTEN): character-level
  line classification (no row regexes) + an explicit index fold walk — must
  equal Arm A on the full observable tuple (steps, decisions,
  decisions-no-default, pending, done, non-owner, parsed, armed, blocked,
  manual, lint, pending texts, done dates) on every baseline, every grid cell,
  every 2×2 cell, and every Arm-R trace.
- Arm R (seeded, REPORTING-ONLY): random cells — per trace EXACTLY 3
  `rng.randint` draws in registered order (corpus ∈ [0,2], grid cell ∈ [1,26],
  salt ∈ [1,1000] drawn-and-logged), one `random.Random` per seed;
  inapplicable/no-edit cells counted honestly as their own classes. N = 20,000
  on seed **20261722** (drafting preview census: SILENT-LOSSY **12,856** ·
  ALARMED-SAFE 2,770 · ALARMED-LOSSY 1,820 · SILENT-REGRADE 1,293 · NO-EDIT
  1,004 · INAPPLICABLE 257; draws exactly **60,000**; class-stream digest
  `e8d8812b3f9c`), stability N = 8,000 on **20261723** (preview: 5,203 / 1,095
  / 694 / 516 / 407 / 85; draws **24,000**; digest `fc2709073718`),
  presentation shuffle **20261724** (presentation legs only). NO statistical
  gate rides Arm R — its gates are the 3N draw sentinel and exact
  reproducibility.
- Aux seed: **20261725**, reserved, NEVER read by any leg (the P054–P081 aux
  convention). Seeds 20261722–725 allocated from 20261722 per the V094
  heartbeat baton (20261718–721 are P081/V094's registered set); boundary-aware
  sweep — regex `(^|[^0-9])2026[0-9]{4,6}([^0-9]|$)` over this tree at the
  grounding HEAD maxes at genuine 20261721; the only ≥ 20261722 hits are the
  V094 heartbeat's own "next free block 20261722" baton lines and this
  session's card/claim (self-hits, this allocation).
- Typed must-equal contacts: **C1** — Arm B == Arm A on the three baseline
  tuples. **C2** — Arm B == Arm A on all 26 grid cells and all four 2×2 cells.
  **C3** — the two independently-written decision evaluators emit the same
  ruling token. **C4** — Arm R: A == B on every trace, draw counters == 3N
  exactly (60,000 / 24,000), and the class-stream digests reproduce.
- Runtime disclosure: the whole drafting battery (three baselines, 26 cells,
  the 2×2, the repair census, N = 28,000 seeded traces, twin everything) runs
  in ~15 s; every decision leg is deterministic parsing and counting.

## Pre-registered decision rule (evaluation order: REJECT first)

- **REJECT** — "the fail-safe sentence is wrong as doctrine: the both-marks
  asymmetry protects DISPOSITION only — recognition is an unguarded
  conjunction where stray edits fail silent, in the drop direction, on both
  shipped copies, and the strict lint is blind there by construction because
  it shares the deriver's recognition predicate": **(R1, the true sentence
  survives)** the disposition 2×2 exact — NO-OP / still-queues + lint /
  still-queues + lint / RETIRE-LIVE, zero silent cells on the sentence's own
  grid; **(R2, the recognition cliff)** the 26-cell census exact at the
  registered class totals {18, 3, 4, 1} with the SILENT-LOSSY list verbatim
  AND the lint-downstream law (every SILENT cell lands lint == 0 AND
  manual == 0); **(R3, the cascade + once-live)** OP1@r5, OP2@r5, OP4@r5 each
  land done 0 · armed 0 · lint 0, AND C1 lands parsed 2 / armed 0 (single
  silent edits disarm every checkpoint of a live launch, and the checker that
  owns the clocks reads through the same parser); **(R4, the granularity
  inversion + priced repair)** OP13 is guarded (manual ≥ 1, lint ≥ 1) while
  the row-level breaks of R2 are silent, AND the conservation-lint repair arm
  reproduces its registered catch census (18/18 SILENT-LOSSY, 0 false
  positives on all three corpora, missed set exactly {OP14}). (Checked FIRST
  because the costly direction is a dropped owner action: the production
  queue is the owner's single entry point to every publish/price/account
  click — a silently dropped click is a launch that never happens and a
  silently disarmed KILL-CHECK is a kill rule that never fires, and both
  failure modes leave a GREEN lint behind them.)
- **INVALID** (controls misbehaving — report, no ruling): any F1–F6 gate
  failure below.
- **APPROVE** — "the sentence holds as doctrine: no single registered stray
  edit can silently drop an owner action": zero SILENT-LOSSY cells on the
  registered grid — arithmetically excluded by the OP1@r1 cell (`**Owner:**`
  is not a substring of `*Owner:**` — F4a, pencil); mutually exclusive with
  REJECT.
- **NULL** — anything else; pre-registered axes: **source-semantics mismatch**
  (the verdict session's own read of the pinned source contradicts one of the
  five behaviors — the fold-closure rule, the checked-only DONE rule, the
  substring-vs-token recognition, the once-live arming, or the lint error
  classes; the corrected behavior + re-derived censuses are the finding, and
  this axis is genuinely LIVE: the behaviors were pinned by reading ~340 lines
  of parser source across two copies, and one misread moves several census
  cells together); **corpus-convention axis** (the registered corpus is
  SYNTHETIC-canonical — modeled on the OCQK packet's own §7 block, not copied
  from it; if a registered cell census fails under the corpus exactly as
  pinned, the corrected cell ships with the finding); **twin-fidelity
  mismatch** (Arm A and Arm B disagree on a registered observable and the
  INVALID diagnosis does not localize it — the corrected census is the
  finding).

GATE POWER, computed at registration for a correct implementation (the
V065/V067 lesson): the sim is FULLY DETERMINISTIC in every decision leg —
every clause is an exact census over a finite registered grid; the only seeded
arm is reporting-only with NO statistical gate (its sole gates are the 3N draw
sentinel and exact reproducibility, pass probability 1 for a correct
implementation); JOINT pass probability across all gates for a correct
implementation = 1 EXACTLY (the P059–P081 no-stochastic-gate precedent).
MARGIN LEDGER, disclosed (the V083 practice): every REJECT clause is an exact
census equality — the registered equality surfaces are the class totals
{18, 3, 4, 1}, the SILENT-LOSSY membership list, the eight key-cell tuples,
the 2×2 row, the cascade triple, the once-live pair (2, 0), the repair catch
census (18/18, +2, 0 FP, miss {OP14}), and the Arm-R draw sentinels; the one
strict inequality (SILENT-LOSSY ≥ 15 in the evaluator) carries margin 3 below
the registered 18. A census landing anywhere off these exact values is
INVALID-or-NULL by the pre-registered axes, never a "close enough".

## Gates (run INVALID on any failure)

- **F1 — model identities:** conservation pending + done + non-owner == 6
  checkbox rows on C0 and every cell that destroys no checkbox head (merged
  and vanished rows accounted explicitly); every grid cell differs from its
  corpus (real-edit sentinel); baseline tuples echo the registered values;
  Arm-R draw counter == 3N exactly.
- **F2 — the structure results, exact:** (a) the 26-cell census twin-verified
  cell-by-cell (C2 contact); (b) the disposition 2×2 (R1); (c) the cascade
  triple + the once-live pair (R3); (d) the position law — OP3@r1 vanish vs
  OP3@r2 merge with the merged-text containment assertion; (e) the
  lint-downstream law on every SILENT cell; (f) the granularity inversion
  (OP13 guarded).
- **F3 — census anchors (reference values, exact):** the registered anchors of
  the Pinned-model block, verbatim — class totals, the SILENT-LOSSY list, the
  key-cell tuples, the 2×2 row, the repair census, the C1 pair, the Arm-R
  previews and digests.
- **F4 — the hand worlds (pencil):** (a) `**Owner:**` is not a substring of
  `*Owner:**` — one lost asterisk defeats a literal-token conjunct; (b)
  `**⚑ Owner:**`.lstrip() starts with `*`, not ⚑ — bolding defeats the prefix
  conjunct; (c) `- []` fails the single-char bracket shape by inspection; (d)
  lowercase `— done 2026-07-13` is unmatched by the case-sensitive DONE regex,
  so the row re-queues — the fail-safe direction, by inspection.
- **F5 — degeneracy/convention controls:** C1 (no-DONE) reproduces the
  once-live rule with everything else unchanged; C2 (two decisions) parses
  lint-clean (the grid's decision cells are not an artifact of
  single-decision files); the repair arm fires on ZERO unmutated corpora; the
  Arm-R INAPPLICABLE and NO-EDIT classes are counted, never silently skipped;
  the classify taxonomy is total on all 26 cells.
- **F6 — battery:** Arm B == Arm A through the four typed contacts on every
  registered surface; twin independently-written decision evaluators agree on
  the ruling token; Arm-R draw sentinels (exactly 60,000 / 24,000) and exact
  reproducibility with the registered class-stream digests; presentation seed
  20261724 read by presentation legs only; aux seed 20261725 never read;
  stdout + results.json byte-identical across two process runs (Arms A/B pure
  deterministic parsing, platform-independent; Arm R pinned to a stated
  CPython minor).

## Expected landing (DISCLOSED per the P048–P081 exact-arm norm)

REJECT on all four conjuncts, at the drafter's exact values (the sim
re-derives everything from scratch and must not trust these; every number was
computed live at drafting — draft_p082.py, 119/119 checks PASS, exit 0,
~15 s, twin evaluators REJECT/REJECT): **R1** — the 2×2 lands NO-OP /
queue+lint / queue+lint / RETIRE-LIVE; **R2** — 18 of 26 cells SILENT-LOSSY,
every one with lint 0 and manual 0; **R3** — the cascade triple at (4, 0, 0,
0) and C1 at (2, 0); **R4** — OP13 guarded while rows fail silent, repair
18/18 with 0 false positives. Falsifiability is real and named on three axes:
(i) the **source-semantics world** — one misread of the fold-closure rule,
the checked-only DONE rule, or the substring recognition moves the position
cells, the cascade cells, and the 2×2 together, and the source-semantics NULL
prices exactly that; (ii) the **guarded world** — if lint in fact carries a
recognition-independent error class the drafter missed (a conservation check
already present anywhere in the lint path), the SILENT census collapses and
APPROVE's zero-silent condition comes live — one real code path away; (iii)
the **corpus world** — a registered census that fails under the corpus
exactly as pinned ships the corrected cell (the corpus-convention NULL).
Disclosed sharpenings, reporting-only: the Arm-R previews (the 26-cell grid
sampled 20,000× lands SILENT-LOSSY 12,856 ≈ 64%, digest `e8d8812b3f9c`); and
the production color — the real derived queue (docs/publishing/OWNER-QUEUE.md
@ the grounding HEAD) is generated from 26 vetting packets by the production
copy of this parser, the OCQK packet's §7 rides it with 5 pending ⚑ owner
rows and a KILL-CHECK due T+7/T+30 after its publish click, and GOTCHAS #2's
own union re-derive race (PR #150) is the documented mechanism by which
stray reflow edits reach gate files — quoted per the P019/P029 realized-probe
precedent as color, never a fixture.

## Consequence (pre-registered; routing the manager's per Q-0260 — this repo edits no other repo, nothing here builds/publishes/spends)

Verdict consumer: venture-lab — the lane owns both parser copies, the derived
queue, the kill-clock checker, the GOTCHAS.md sentence, and the $19 listing
whose copy sells the 38-test evidence. REJECT → paste-ready structured
choice, recommendation first per Q-0263.2: **(a, recommended)** the
conservation lint, zero recognition change: one function per lint path
(ocq.py `cmd_lint` + scripts/lint_owner_gates.py) counting the LOOSER net
(bullet-ish or ⚑ line whose stripped text contains "owner:"; numbered step
containing "(default"; ⏲ line containing "kill") and erroring when strict
recognition counts fewer — priced on the registered grid: 18/18 silent cells
caught, 0 false positives on all three corpora, the one semantic-regrade cell
disclosed as out of reach; plus replace the GOTCHAS #4 sentence with the
two-sided disclosure (disposition fail-safe TRUE / recognition unguarded —
three sentences). **(b)** recognition-weakening — accept unbolded `Owner:`,
the flag anywhere before the token, `*` bullets, one-space indents: shrinks
the silent space at the price of false-positive recognition, and the seat-row
exclusion is BY DESIGN (`test_only_owner_rows_become_clicks` pins it; a
weakened predicate can queue seat rows — the exclusion-vs-recognition tension
is why (a) dominates); **(c)** status quo + document: amend GOTCHAS #4 and the
packet's §1 test claim with the boundary sentence, and kill-clock consumers
add their own checkpoint-count check. Known co-consumers of the verdict:
check_kill_clocks.py (the T+7/T+30 clocks the kill-clock verdict pair priced
are READ through this parser — a silent disarm is upstream of every law they
measured), the OCQK buyer population (the zip ships the sentence and the
parser together), idea-engine's own scripts/check_sections.py (ASK 005's
roster breakage is the same failure class — recognition drift in a consumer
parser — and the repair transfers: a second, looser net + a conservation
check), and — the transferable audit — every tolerant-derive + strict-lint
pair in the fleet: a lint that shares the deriver's recognition predicate can
never see recognition loss; conservation checks need a predicate the deriver
does NOT use.

## Dedup

Tree-wide `rg -i 'recognition|tolerant.pars|owner-gate|derive_owner_queue|ocq\.py|silently drop'`
(bootstrap.py/.substrate excluded) at the grounding HEAD: the owner-queue hits
are P062's attention-order head and its consumers; "silently drop" appears in
workflow prose and in the harvested GOTCHA itself; no idea file or proposal
prices a parser, a grammar, a mutation census, or a lint blind spot. Nearest
priors argued distinct: **P062 → V073 (owner-queue-attention-order)** — the
SAME document family, zero shared machinery: it priced the ORDER the derived
queue is served in (scheduling, completion indices, attention discount),
taking the parse as given; this head prices whether a row SURVIVES parsing at
all — the verdicts compose (an attention-optimal queue can still silently
lose rows); **P058 → V069 (rubric weights)** — scoring robustness, not
parsing; **the kill-clock pair (kill-clock-horizon-2026-07-13.md → P050;
kill-clock-anchor-truncated-exposure-2026-07-15.md → P066)** — both price the
CLOCK (horizon length, anchor onset) assuming the checkpoint is read; this
head prices the reader: a silent disarm is upstream of every clock law, and
the OP12/cascade cells are exactly the checkpoints those heads assumed
present; **P074/P078** — pricing lattices on committed constants, no parser
surface; **P081 → V094 (guard-fires dedupe)** — the method kin: a shipped
~150-line mechanism priced against its own comfort comment with the
true-sentence-survives move; different object class entirely (a windowed
dedupe's TEMPORAL orbits vs a parser's single-edit recognition census — no
dynamics here, pure finite enumeration), different lane (substrate-kit vs
venture-lab), and this head's blind-lint law has no analogue there. No
proposal P001–P081 and no verdict V001–V094 prices a grammar parser, a
mutation census, a recognition predicate, or a lint/derive contract pair.
This head's own additions to the battery: a MUTATION CENSUS over a pinned
grammar as the decision object, a LINT-DOWNSTREAM law (the guard and the
hazard sharing one predicate, priced as its own REJECT clause), a
position-dependent fold law (vanish-vs-merge), and a repair arm priced by its
exact catch census inside the same registered grid.

## Model basis (declared model-dependence — the P024 discipline)

Four modeling commitments carry the verdict, each pinned and directional:
(1) the SEMANTICS are the harvested source's, pinned at the grounding HEAD as
five named behaviors — each carried with a control or a NULL axis, and the
source-semantics NULL exists because pinning by reading ~340 lines across two
copies is fallible; (2) the MUTATION SPACE is a registered 26-cell grid of
single edits, chosen to exercise each recognition conjunct and each
disposition bit once per relevant target — it is a WITNESS space, not a
measure space: the claim is existential (silent-drop cells EXIST and lint is
blind on all of them), so grid choice can overstate prevalence but cannot
manufacture a witness, and Arm R's random sampling is demoted to
reporting-only for exactly that reason; (3) the CORPUS is synthetic-canonical
(pinned verbatim, modeled on the packet's own §7 block) — cell censuses are
corpus-relative, the corpus-convention NULL prices a corpus-driven failure,
and the two variant corpora control the two structural toggles (a DONE row's
presence; decision multiplicity); (4) the CONSEQUENCE model treats a
dropped-from-queue row as a lost owner action — true on the committed
workflow (the queue is the owner's single entry point, GOTCHAS #7: agents
write, only the human executes, and the gate file itself is not re-read at
click time), and the head says so rather than assuming silent readers of raw
gate files. The comfort sentence is priced against its own best
formalization: the disposition grid where it is TRUE is registered as R1, so
the head cannot be read as a straw man.

## Probe report (v0, 2026-07-16)

> Single-pass battery (panel not escalated: self-contained mechanism probe, sim is
> report-only evidence, no spend/publish/irreversible surface — README § probe battery).
> Verify-first ran FIRST, live this slice: (a) **dedup** — the tree-wide sweep and the
> sim-lab READ-ONLY dedup posture above returned P062's attention-order head (parse
> taken as given) and the harvested GOTCHA's own prose as the only collisions; no
> prior head prices a parser or a mutation census. (b) **kill test NOT triggered** —
> no recorded drop of this mechanism exists on any card; P062's head explicitly
> priced a DIFFERENT object over the same document. (c) **feasibility + liveness
> arithmetic checked LIVE** — every registered numeral ran this session
> (draft_p082.py, 119/119 PASS, exit 0, ~15 s): the three baselines, all 26 cells
> twin-verified, the 2×2, the cascade triple, the once-live pair, the position law,
> the repair catch census, and the seeded Arm-R previews with their 3N sentinels;
> expected landing DISCLOSED (REJECT), all rulings reachable, the source-semantics /
> guarded-world / corpus falsifiability worlds named.

**1. What is this really?** A pre-registered EXACT MEASUREMENT of a sold
fail-safe claim — "a stray checkbox edit can only ever RE-QUEUE an owner
action, never silently drop one" — taken on the claim's own shipped parser
(both copies, verbatim-identical predicate): a 26-cell single-edit mutation
census over a pinned canonical gate file, with the disposition grid where the
claim is TRUE registered beside the recognition space where it inverts, and
the lint's structural blindness (every error class downstream of the same
recognition predicate) priced as its own clause.

**2. What is the possibility space?** (i) Don't run it — the round-17 venture
slot goes unserved. (ii) A pricing head instead — the products-half pricing
surfaces (ladder, bundle, floors) are verdicted through V094's era; the
lane's CONTROL surface (the queue every click rides) has one priced verdict
(P062, ordering) and zero on integrity. (iii) File a bug report ("the parser
drops rows") — states a symptom without the laws; the exact treatment gives
the regime map: WHICH conjuncts drop silently, which cells the lint sees, the
cascade to the kill clocks, and a repair priced by its catch census. (iv) A
fuzzing run — random mutation without registration finds witnesses but proves
no census and gates nothing; here every decision cell is registered and the
random arm is demoted to reporting. (v) This head. (vi) Over-scope (mutate
the render layer, the discovery walk, the union re-derive race of GOTCHAS #2)
— each named as a follow-up, none in scope.

**3. What is the most advanced capability reachable by the simplest
implementation?** One ~200-line stdlib file: two parser replays (regex-faithful
and character-level), one mutation library (14 single-edit operators), and
integer counters — that single kernel yields the full census, the 2×2, the
cascade, the position law, the repair pricing, and the seeded traces; a
verdict session runs it cold in seconds.

**4. What breaks it? (assumptions made explicit)** (a) **The semantics are
read, not executed** — the model replays five pinned behaviors, not the
function objects; one misread moves several censuses together, and the
source-semantics NULL prices exactly that. (b) **The grid is a witness space**
— prevalence claims ride only the registered cells (and the reporting-only
Arm R); the decision claim is existential and the census is exact on its own
grid, stated as such. (c) **The corpus is synthetic-canonical** — registered
verbatim; the corpus-convention NULL prices a corpus-driven miss.
(d) **Band placement could cherry-pick** — every band is an exact census
committed before the sim, the expected landing is DISCLOSED, and the TRUE
cells (the 2×2, OP11's re-queue, OP13's guarded file break, OP10's caught bad
date) are registered as prominently as the silent ones.

**5. What does it unlock?** The venture lane's first integrity verdict on its
own control surface (the queue every publish click rides); the kill-clock
verdicts' missing precondition (the checkpoint reader itself); a priced,
one-function repair (the conservation lint) with its catch census attached;
the OCQK product-copy fix (the sold sentence made true); and the transferable
audit for every tolerant-derive + strict-lint pair in the fleet — a lint that
shares the deriver's recognition predicate can never see recognition loss
(idea-engine's ASK 005 roster breakage is the same class, and the second-net
repair transfers).

**6. What is the cheapest experiment that decides it?** The whole head IS the
cheapest deciding experiment: 26 deterministic parses of a 21-line file. The
single cheapest probe if a reader doubts it is pencil: `**Owner:**` is not a
substring of `*Owner:**`, so one lost asterisk un-recognizes the row; every
lint error class begins `if is_owner_row(b)…`, so the same lost asterisk
silences the lint — two lines of source, no computer.

**7. What would make this a mistake to run?** If the exact treatment were
unavailable (it is not — every decision quantity is a finite parse census),
if the object duplicated a prior head (it does not — P062 priced ordering
over the same document with the parse taken as given; zero mechanism
collisions in both trees), or if the disclosed REJECT made the run theater.
It does not: the value is the independent hermetic re-derivation (Arm B's
character-level replay exists because regex-reading is exactly where a
misread hides), the five source pins re-read by fresh eyes, and both
non-REJECT rulings genuinely reachable (APPROVE is one overlooked
conservation check away; the corpus and source-semantics NULLs are one real
misread away).

**8. How will we know it worked?** A committed sim-lab report with: the three
baseline tuples, the 26-cell census table (class + observable tuple + repair
catch per cell), the disposition 2×2, the cascade triple and once-live pair,
the position-law pair, the repair catch census, the F1–F6 gate results, the
verdict token against the pre-registered bands, Arm R's measured class
censuses beside the exact grid (reporting-only, 3N draws asserted), and a
byte-identity note. A clean run reproduces the drafter's disclosed values
(class totals {18, 3, 4, 1}; the cascade at (4, 0, 0, 0); repair 18/18 with 0
false positives) from scratch, or — the more interesting outcome — DISAGREES
and pins the drafter's misread, which the pre-registered rule then rules on
honestly (the source-semantics, corpus-convention, and twin-fidelity NULL
axes exist for exactly that).

**Recommendation: sim-ready**
