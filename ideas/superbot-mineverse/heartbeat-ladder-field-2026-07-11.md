# A machine-parseable ladder line for the roster generator — fast newborn lanes outrun prose rows

> **State:** parked(routed — kit-owned grammar declaration decision; fleet-manager's generator is the first consumer, and the roster went machine-generated between capture and probe, mooting the auto-re-pin third of the payoff)
> **Class:** process · **Target:** `menno420/fleet-manager`
> **Grounding:** https://raw.githubusercontent.com/menno420/fleet-manager/dd8dc10e0a108b4f77a7c7bcd155e4b351aa2881/docs/roster.md@dd8dc10 · fetched 2026-07-11T04:00:21Z
> *(pin annotation: roster still generation #4, generated-at 2026-07-11T01:58Z, at fleet-manager HEAD `dd8dc10` — the same generation the earlier sibling batch pinned at `93d3a4d`)*
> **Grounding:** https://raw.githubusercontent.com/menno420/superbot-mineverse/510fa3e05cdac1244d70e65b71d048b7fdf38dd0/control/status.md@510fa3e · fetched 2026-07-11T04:00:19Z
> **Sequence:** before the roster's row format hardens across more generations

## Problem

Grounded by THIS lane's drift, measured at capture time. The roster gen-#4 row for
superbot-mineverse (@ `dd8dc10`, verbatim): "**LANE BORN THIS WINDOW**
(\"mining-browsergame\"): ORDER 000 walking skeleton merged to main; stage (a) READ
CONTRACT v1 + backlog slice in flight; `check: red` is the pre-existing born-red
unrendered-interview state (engaged: no, flips on slot render)", pinned at lane
`1120a3b` 01:57:13Z. The lane's own heartbeat @ `510fa3e` (updated 03:58:00Z) reads
"LADDER: 0 ✓ · (a) ✓ · (b) ✓ · (c) ✓ web-side · (d) PREPARED ✓" with check green /
engaged yes / 187 tests — FOUR ladder rungs, a check-state flip, and an engagement
flip inside ONE ~2h generation window. The roster already knows fast movers exist
(this exact row carries a "mid-sweep mover, re-pinned" annotation), but stage
progress lives in prose a generator can only carry forward verbatim, so the row is
stale-by-construction the moment a newborn lane moves — and newborn lanes move
fastest precisely while their rows matter most.

## Idea

A machine-parseable `ladder:` line in the kit heartbeat grammar — e.g.
`ladder: 0=done a=done b=done c=done d=prepared` — written by lanes that operate a
staged ladder, so the roster generator can (1) render stage state mechanically
instead of quoting prose, (2) diff it against the previous generation and surface
stage-level drift ("moved N rungs since gen #k"), and (3) re-pin fast movers
automatically when the drift exceeds a threshold, instead of relying on a mid-sweep
human-shaped catch. Seam honesty: the heartbeat format block is kit-owned grammar
(EAP §6.8 — undeclared top-level keys are drift and fold into `phase` in consumers'
parsers, this repo's control/README records the round-4 decision), so the field
becomes real as a KIT grammar addition; fleet-manager's generator is the consumer
that motivates and first exploits it. Until the kit declares it, lanes can carry the
same string inside `phase:` where it is at least grep-able.

**Why now:** the generated roster just became the fleet's canonical lane registry
(this repo's README § Sections re-pointed to it 2026-07-11), every idea-engine
section derivation and manager routing decision now reads these rows, and the fleet
is birthing lanes weekly — the row format is young enough that a grammar field is an
addition, not a migration.

## Probe report (v0, 2026-07-11)

> **Grounding:** https://raw.githubusercontent.com/menno420/fleet-manager/6dedff612cef7f98410575d074a578ab85d6e23c/docs/roster.md@6dedff6 · fetched 2026-07-11T05:51:31Z
> **Grounding:** https://raw.githubusercontent.com/menno420/substrate-kit/941be2e97b97ea8cbd2ab4690204c8580594220d/src/engine/grammar.py@941be2e · fetched 2026-07-11T05:52:12Z

Single-pass battery v0 (no panel trigger: not contested, not high-blast-radius —
a routing question over a docs-only surface). Verify-first at build time
(`git ls-remote` 05:51:08Z): fleet-manager HEAD `6dedff6`, superbot-mineverse HEAD
still `2b1bd0b`, substrate-kit HEAD `941be2e`. **The grounding premise MOVED between
capture and probe:** roster generation #5 (`docs/roster.md` @ `6dedff6`, generated-at
04:28Z) is the FIRST MACHINE GENERATION — `scripts/gen_roster.py` (fleet-manager
PR #62) re-reads every lane heartbeat at an ls-remote-verified HEAD on each manager
wake, so the capture's failure mode ("stage progress lives in prose a generator can
only carry forward verbatim") no longer exists as stated: nothing is carried forward,
and the mineverse row at gen #5 reads its 04:27Z heartbeat at age ~1m. Row staleness
is now bounded by wake cadence (~2h) plus the roster's own >24h kill-switch, not by a
human-shaped mid-sweep catch. What did NOT move: (a) `parse_status()` in
`gen_roster.py` @ `6dedff6` extracts exactly six keys — `("updated", "phase", "kit",
"orders", "health", "lane")` — so an undeclared `ladder:` line is silently IGNORED
there (distinct from websites' hand-kept `/fleet` parser, where undeclared keys fold
into `phase` — this repo's PR #49 measured leak); mineverse's ladder state lives in
heartbeat BODY prose (`LADDER: 0 ✓ · (a) ✓ …` @ `2b1bd0b`), invisible to the parser;
(b) the roster itself prints "the hand generations' 'Deltas vs generation #N-1'
narrative is coordinator judgment and is NOT auto-derived" — the stage-drift diff this
capture asks for is exactly the still-unmechanized half; (c) the kit grammar module
(`src/engine/grammar.py` @ `941be2e`) has no ladder/rung/stage/progress token — the
field does not exist; (d) fleet-manager's inbox @ `6dedff6` ends at ORDER 016
(merge-authority + env audit) — no open ORDER covers a heartbeat grammar field.

**1. What is this really?** Two fused asks with different owners: (i) a kit grammar
declaration — a new machine-parseable heartbeat field — and (ii) a fleet-manager
generator feature (stage-level gen-over-gen diffing + auto re-pin). The auto-re-pin
third of the payoff was mooted between capture and probe: machine generation re-pins
every lane every wake by construction. What survives is structured stage state plus
mechanical drift-diffing — and the declaration half is a decision neither this repo,
nor fleet-manager alone, nor the producing lane can land: the heartbeat format block
is kit-owned grammar (EAP §6.8; writer and enforcer share `src/engine/grammar.py`,
pinned by the kit's `tests/test_grammar.py`).

**2. What is the possibility space?** Ascending: (i) zero-grammar interim — the
producing lane carries the ladder token inside `phase:` (the capture's own fallback),
which is strictly better post-gen-#5 than at capture time: `gen_roster.py` machine-
quotes `phase` (truncated at 160 chars) into the roster cell, so stage state renders
mechanically in every future generation for the cost of moving one string from body
prose into the phase line; (ii) the declared `ladder:` field — kit `grammar.py`
constant + canonical example + `test_grammar.py` case, `gen_roster.py` adds one key to
its parse tuple + one column; (iii) plus gen-over-gen stage diff ("moved N rungs since
gen #k") — the roster file is committed, so the previous generation is already in git
for the generator to diff against; (iv) generalized `progress:` vocabulary for ANY
staged lane (superbot-next runs bands, trading-strategy runs rounds — ladders are not
mineverse-specific, and a `ladder:`-shaped key may be too narrow to declare). Null
alternative: do nothing — machine generation already bounds staleness to a wake
window and stage truth is one heartbeat click away.

**3. What is the most advanced capability reachable by the simplest implementation?**
The zero-grammar interim (i): one heartbeat edit in the producing lane — put the
ladder token inside the first 160 chars of `phase:` — and stage state is mechanically
rendered in every roster generation from then on, with ZERO kit or fleet-manager code
change. The declared field only buys machine diffing and thresholds beyond that, and
those need (iii)'s generator work to pay off.

**4. What breaks it?** (a) The undeclared-key doctrine: a lane unilaterally writing
`ladder:` as a top-level key is exactly the extension-key drift class this repo's
round-4 grooming DECIDED against (PR #59: fold-in over declare, encoded at
control/README § status.md format) — consumers disagree on unknown keys (gen_roster
ignores; websites' parser folds into `phase`, the PR #49 measurement), so the field
must be DECLARED kit-side before any lane writes it. (b) Thin demand: exactly one
lane writes an explicit rung ladder today, and that lane's ladder is FINISHED —
`0/a/b/c ✓ + (d) prepared` with all remaining work externally blocked @ `2b1bd0b` —
so the grounding lane may never move another rung; the general staged-lane case wants
a broader vocabulary than `ladder:` (Q2 iv), which is a grammar-design question, not
a capture. (c) A third of the capture's payoff (auto re-pin) is already delivered by
gen #5's architecture.

**5. What does it unlock?** The roster's remaining hand-work half — machine
gen-over-gen deltas for staged lanes (closing the roster's own self-acknowledged "NOT
auto-derived" gap); manager routing on stage thresholds instead of prose reads; and
machine-visible progress for newborn lanes precisely in the window they move fastest
(the capture's true core, still standing).

**6. What does it depend on?** A substrate-kit grammar declaration (`grammar.py` @
`941be2e` has no such field) + its `test_grammar.py` pin; `gen_roster.py` @ `6dedff6`
adding the key + a delta pass (prior generation available in git); at least one
producing lane with a LIVE ladder (none today — see Q4b); no open fleet-manager ORDER
covers it (inbox @ `6dedff6` ends ORDER 016, unrelated), so the routing surface is
the manager's :30 sweep.

**7. Which lane should build it?** substrate-kit DECLARES (one grammar, one parser —
the same kit heartbeat-grammar seam as the seat-boot and own-heartbeat-parse
cross-links already parked on `ideas/substrate-kit/README.md`, and the "extension-key
declaration story" that README's own-heartbeat entry already names); fleet-manager
CONSUMES (`gen_roster.py` parse key + delta pass). NOT superbot-mineverse (a producer
only — and its zero-grammar interim needs no one's permission), NOT idea-engine.
Cross-linked into `ideas/substrate-kit/README.md` § Cross-links per the PR #29/#40
precedent; fan-in relayed via this repo's heartbeat notes. No sim-lab proposal — a
grammar field is proven by its parser test, there is no simulator question.

**8. What is the smallest shippable slice?** Zero-grammar: ONE producing-lane
heartbeat edit (ladder token into `phase:`) — mechanically rendered at the next
generation, no code anywhere. Declared-field slice, when the kit picks it up: a
`ladder:`/`progress:` constant + canonical example in `src/engine/grammar.py` + one
`tests/test_grammar.py` case (kit side), plus `"ladder"` in `parse_status()`'s key
tuple + one roster column (fleet-manager side) — each side ~10 lines, but it spans
two repos and a grammar-versioning decision, which is why it routes instead of
building here.

**Recommendation: park** — routed: the surviving value (structured stage state + machine drift-diff) is a kit-owned grammar declaration decision with fleet-manager's generator as first consumer (PR #59's fold-in-over-declare rule bars lanes from writing the key undeclared), a third of the capture's payoff was mooted by the machine-generated roster (gen #5 @ `6dedff6`), and the zero-grammar interim (ladder token in `phase:`) is available to any staged lane today.
