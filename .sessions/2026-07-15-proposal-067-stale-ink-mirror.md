# Session — PROPOSAL 067: the stale-ink mirror — Wickroad's "bet on your own stale information" is a rigged coin under its own 12-day closed-form law (game-mechanics rotation, round 13 third slot)

> **Status:** `complete`
> **Model/time:** fable · 2026-07-15T06:18:07Z (Ideas Lab worker slice — draft the
> round-13 GAME-MECHANICS rotation slot proposal under standing owner ORDER
> 003/004; round 13 opened at fleet backlogs with P065 (#428) and served
> venture with P066 (#429, merged 05:52:20Z). Card born in-progress as the
> designed gate hold; flipped complete in this PR's final commit at
> 2026-07-15T06:33Z. PR #430)

- **📊 Model:** fable-class · high · idea/planning

## Scope

Draft a genuinely new sim-shaped idea for the GAME-MECHANICS rotation slot,
round 13 THIRD slot, under standing owner ORDER 003 (continuous pipeline) and
ORDER 004 rule 3 ("fleet backlogs → venture's book/product space → game
mechanics → COMPLETELY UNRELATED domains"). Round 13 opened at fleet backlogs
with P065 (#428) and served venture with P066 (#429), so game mechanics is
next; the slot's own spacing history (P020, P023, P027, P031, P035, P039,
P043, P047, P051, P055, P059, P063 → P067) confirms. Source rotation inside
the slot (the P063 record): gba-homebrew ×2 (r6/r7), superbot ×2 (r8/r9),
superbot-mineverse (r10), superbot-idle (r11), superbot-games (r12) — so
round 13 returns to **gba-homebrew**, undrawn since round 7 (P043), with
pokemon-mod-lab (the only never-drawn games lane) excluded DARK/private per
the standing Q-0260 rule-3 carve-out.

Harvest source: gba-homebrew read FIRSTHAND this session (public shallow
clone, `git log -1` = `c0c688210bcb3db0004102e6c5b899943533f816`, "wickroad:
growth cut 3 — the road itself (v0.4) (#144)", fetched 2026-07-15T06:02:44Z)
— **Wickroad**, the lane's newest game (breadth game #11, v0.4 merged this
morning), whose committed concept sells ONE hook in its own words: "You
navigate an economy you remember, not one you see; every trip is a bet on
your own stale information" — while the same tree commits a price law that
is a CLOSED FORM of the day (12-day integer triangle wave, fixed seed
0x5749434B, "The SAME world every run"). The head: the committed law makes
the committed hook's bet a rigged coin — ink of age 12 is exactly fresh
(period), ink of age 6 is exactly INVERTED (tri12(m+6) = −tri12(m), and the
shipped map's longest natural round trip is exactly 6 days), and two
consecutive mornings in a town decode its entire price track forever (the
12 consecutive-value pairs of the triangle are pairwise distinct). Measured
at drafting: the lag-6 inversion census is 300/300 — clamps included — and a
law-inferring planner collapses the oracle gap to 1201/1309 ≈ 0.917 on the
shipped world under a shared greedy scaffold.

Deliverables this slice: this card (born-red first commit), the claim file,
`ideas/gba-homebrew/wickroad-stale-ink-mirror-2026-07-15.md` + the
`ideas/gba-homebrew/README.md` index row, the `control/outbox.md` PROPOSAL
067 append, ONE terminal claim prune (the P066 drafter — PR #429 verified
merged at live GitHub 2026-07-15T05:52:20Z, merged_by github-actions[bot],
this session before deletion), and — the threshold having tripped — the
ROLLOVER 002 outbox roll per the committed convention (see Constraints).
Seeds 20261590–593 — strictly above this tree's genuine high-water 20261583
(P066's registration, re-swept this session at HEAD 848d6de) and sim-lab's
genuine high-water 20261570 (V078's reserved aux, re-swept READ-ONLY at
origin/main b7a6859 this session); 20261580–583 are P066/V079's registered
set, and the gap **20261584–589 is deliberately left unallocated** as the
in-flight VERDICT 079 allocation buffer per the coordinator relay
(disclosed, not hidden).

## Constraints honored

- control/inbox.md untouched (manager-written); control/status.md untouched
  (no heartbeat housekeeping in this slice's scope).
- Outbox: PROPOSAL 067 appended via shell (append-only, real `date -u`);
  then — the file having crossed the committed 200KB threshold with this
  append (198,699 B before; the P066-era size the coordinator flagged) —
  ROLLOVER 002 executed per the committed convention (fm
  `docs/conventions/outbox-rollover.md` as relayed by inbox ORDER 010 and
  quoted verbatim in the ROLLOVER 001 receipt: 200KB threshold ·
  terminal-blocks-only · dated archive files · mandatory pointer stubs ·
  content-stable numbering), byte-faithful per block (sha256-verified at
  roll time) to `control/outbox-archive-2026-07-15.md`, exactly the
  2026-07-14 precedent's shape. Terminal set verified FIRSTHAND sim-lab-side
  this session: PROPOSAL 058–065 (verdicts V069–V078 ALL finalized at
  sim-lab origin/main b7a6859 — offset +11 through P063→V074, V075/076 =
  simreq-010/011, +13 from P064), ACK 001 (posted), CLOSE-OUT 001 (posted).
  Non-terminal stayed live: ASK 005 (open, awaits fm) and PROPOSAL 066
  (V079 not yet registered sim-lab-side at b7a6859).
- control/outbox-archive-2026-07-14.md untouched (rolled archive, terminal).
- Claim prune is TERMINAL-only: PR #429 verified merged at live GitHub (mcp
  pull_request_read: merged 2026-07-15T05:52:20Z, merged_by
  github-actions[bot]) before deletion; zero open PRs at drafting
  (collision check clean; `PROPOSAL 067`/`proposal-067`/`VERDICT 080`
  grepped clean repo-wide at HEAD 848d6de).
- gba-homebrew and sim-lab READ-ONLY: fresh shallow clones this session
  (gba-homebrew @ c0c6882 for the FIRSTHAND harvest; sim-lab @ b7a6859 for
  the verdict ledger + dedup + seed sweep); nothing there touched — this
  repo edits no other repo (Q-0260).
- Seed sweep boundary-aware at drafting HEAD 848d6de: this tree maxes at
  genuine 20261583; larger standalone numerals (20261664, 20261833,
  202670087, and results-quoting digit runs) match the recorded
  discrimination rule — standalone 2026-prefixed numerals inside
  results-quoting text are data, not seeds.
- The `📊 Model:` line above uses the kit's taught three-field payload
  (the P064 fix, carried forward).

## 💡 Session idea

**Memory quality is a property of the (memory, process) pair — before
pricing "staleness risk", ask what the underlying process IS, because
against a deterministic periodic process memory does not decay, it
ROTATES.** Drafting held two genuine surprises. First, the inversion is
not merely "possible at bad lags" — it is a perfect staircase (0, 60, 120,
180, 240)/240 across lags 1–5 and TOTAL (300/300) at lag 6, clamps
included, and the shipped map geometry puts its own flagship round trip
exactly on the anti-phase: nothing in the concept chose that, it fell out
of period 12 meeting a 5-town line — a reminder that two independently
reasonable constants (a 12-day market cycle, a 4-leg map) can compose into
a rigged mechanic neither author intended. The transferable audit: any
"fog of war"/memory read over a deterministic engine (idle offline
projections, cached dashboards, replay-from-memory) should be priced at
the system's natural revisit lags FIRST — the worst lag is computable, and
the UI may be shipping it as the default cadence. Second, the greedy
scaffold showed better beliefs are NOT monotone in outcome (SCRYER out-
earned ORACLE 1496 vs 1237 on the decks-OFF drafting row): when a planner
is held fixed and only beliefs vary, information value can overshoot
through plan-selection luck — so a "more information ≥ more gold" band
must pre-register its overshoot axis or it will misread its own evidence.
Kin to P066's "price the (deadline, shape) pair, not the dial" — same
moral, new axis: there a rule against an arrival process, here a memory
against a price process.

## ⟲ Previous-session review

Previous session (the P066 drafter, PR #429 @ `848d6de`): the strongest
card of the round so far, and this slice consumed it directly three ways —
(a) the born-red card / three-field 📊 payload / terminal-prune-with-live-
verification recipe carried verbatim (this slice's P066-claim prune
followed its own recorded recipe: #429 verified merged at live GitHub
05:52:20Z before deletion); (b) its seed-ledger discipline (registered set
+ explicitly disclosed buffer gap 20261571–579) made this session's
allocation trivially safe — the gap convention is doing real work and was
re-used here (20261584–589 left as the V079 buffer); (c) its "price the
PAIR, not the dial" framing seeded this head's process-pair lens. One nit,
with a lived consequence this session: the P066 claim bullet and card
pinned sim-lab's high-water via "V078 in flight, allocating from 20261571
per the coordinator relay" — but V078 had FINALIZED (05:37:45Z) nine
minutes before the claim was written (05:46:46Z), so this session's sweep
first re-derived a stale picture and had to reconcile against the live
ledger at b7a6859. The relay was honest about its source ("not yet visible
in either tree at the pins above; disclosed, not hidden") — the nit is
only that a claim written AFTER a fact lands should re-pin the fact, not
the relay: prefer one fresh `git log`/ledger read over a cached relay
whenever the claim is about another repo's moving state.
