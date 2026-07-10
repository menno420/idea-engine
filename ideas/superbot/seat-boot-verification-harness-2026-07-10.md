# Seat boot-verification harness — script the dispatch copilot's §5 row — link index

> **State:** parked(routed — no simulator question; the build is real but belongs to lanes: kit-side heartbeat-parser seam (substrate-kit) + operator-side wrapper (superbot `scripts/`), relayed to the manager via the heartbeat notes + a substrate-kit section cross-link — see probe report)
> **Class:** process · **Target:** `menno420/superbot`
> **Grounding:** https://raw.githubusercontent.com/menno420/superbot/655e0fea62dbb64d2d5ec962da7fa5816c180c60/docs/ideas/seat-boot-verification-harness-2026-07-10.md@655e0fe · fetched 2026-07-10T21:38Z

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/seat-boot-verification-harness-2026-07-10.md`](https://github.com/menno420/superbot/blob/655e0fea62dbb64d2d5ec962da7fa5816c180c60/docs/ideas/seat-boot-verification-harness-2026-07-10.md)
— harvested 2026-07-10 by the drift re-harvest slice, pinned @ superbot `655e0fe`
([raw](https://raw.githubusercontent.com/menno420/superbot/655e0fea62dbb64d2d5ec962da7fa5816c180c60/docs/ideas/seat-boot-verification-harness-2026-07-10.md)).

The dispatch copilot's per-seat boot-verification ritual is a four-times-repeated manual sequence (trigger-registry check, raw-fetch of the seat's `control/status.md` heartbeat, inbox/outbox expected-entry check, hand-composed runbook §5 row) with at least three more runs incoming as the games-Project seats boot (Q-0259 r.5). The idea: a small superbot script — `scripts/check_seat.py <repo> [--routine <name>] [--expect-order N] [--expect-outbox N]` — that pulls the trigger registry (or a `list_triggers` JSON dump), parses the kit heartbeat grammar at HEAD, checks expected inbox/outbox numbers, and emits a ready-to-paste §5 row skeleton with every verified fact filled and only the verdict left for judgment. Q-0120-grounded: it reports only transport-verifiable facts and labels self-reported status content as such, so a self-report can never be laundered into a verification. Motivation: hand-composed §5 rows are where transcription drift enters the fleet's boot audit trail.

## Probe report (v0, 2026-07-10)

> **Grounding:** https://raw.githubusercontent.com/menno420/superbot/afbaea73cda998d0f31994efdd4cf959b2f38505/docs/planning/round3-dispatch-runbook-2026-07-10.md@afbaea7 · fetched 2026-07-10T21:5xZ (superbot HEAD `afbaea73cda998d0f31994efdd4cf959b2f38505` transport-verified via `git ls-remote refs/heads/main` at probe time — AHEAD of the harvest pin `655e0fe`; the canonical idea doc is byte-identical at both SHAs, sha256 `eab12561…`)
> **Sequence:** after superbot `655e0fe` (harvest pin, PR #26) · **before** the ≥3 games-Project seat boots (Q-0259 r.5) — at `afbaea7` the manifest's three games lanes (games-plugins, pokemon-mod-lab, gba-homebrew) all show "Routine cadence: none" with pending self-arm ORDERs, i.e. their seat boots (and §5 rows) are still ahead.

*Timeliness verified live FIRST (the PR #25 lesson). At superbot HEAD `afbaea7`: (a) the
runbook §5 "Boot verification log" now carries **seven** hand-composed data rows
(fleet-manager, substrate-kit, Idea Engine, Product Forge, Simulator, Trading, Builder) —
the repetition the idea observed at four has grown by three since harvest, live and
compounding; (b) `scripts/check_seat.py` does NOT exist (raw fetch → 404; a GitHub tree
listing of superbot `scripts/` shows 100+ checkers, none seat/boot-shaped) — nobody built
it while the idea sat; (c) the demand window is open per (Sequence). The window is real,
not stale.*

**1. What is this really?**
A transcription-drift guard for the fleet's boot audit trail, disguised as a convenience
script. The §5 rows are where the program's "is this seat actually alive?" facts are
recorded; today each row is hand-composed from a manual four-step ritual (trigger
registry → raw heartbeat fetch → inbox/outbox expected-entry check → row prose), and
hand-composition is exactly where state errors entered before (the runbook's own
six-vs-seven lesson was a hand-composed state error, resolved in a dated correction
block @ `afbaea7`). The idea mechanizes the transport-verifiable ~80% of the ritual and
leaves only the verdict cell to judgment, with the Q-0120 line load-bearing: facts the
tool verified over transport (registry, git @ HEAD) are labeled apart from facts a seat
self-reported (status content), so a self-report can never be laundered into a
verification. PROCESS class; the product is trustworthy rows, not saved minutes.

**2. What is the possibility space?**
- **Minimal:** an operator-run script taking a repo name + a pasted `list_triggers` JSON
  dump, raw-fetching `control/{status*,inbox,outbox}.md` at HEAD, emitting a §5 row
  skeleton with provenance labels and `[[fill: verdict]]`.
- **Live-registry mode:** the same run from a seat with the claude-code-remote MCP,
  pulling the registry itself (the canonical doc's mode 1).
- **Standing re-verification:** the canonical doc's own escalation — the "every-wake
  re-verification (brief §2.4 class)" becomes cheap enough to actually happen; the fleet
  manager's sweeps get per-seat rows for free (its ~15:1xZ archive-readiness sweep @
  `afbaea7` did claim-by-claim heartbeat/registry checking entirely by hand).
- **Roster convergence:** run over ALL manifest rows this is the verify pass of the
  manager's generated-roster-from-heartbeats proposal (fleet-manager ORDER 009, named in
  the manifest header @ `afbaea7`) — same fetch+parse core, different output shape.
- **Kit-native:** a `bootstrap`-side seam ("parse this heartbeat text / this fetched
  control dir") — the kit already owns and parses the heartbeat grammar in every repo.
- **Degenerate corner:** an over-trusted harness whose emitted rows get pasted without
  the provenance labels — worse than the manual ritual it replaced (see Q4).

**3. What is the most advanced capability reachable by the simplest implementation?**
A stdlib-only script (repo name + `--triggers-dump <json>`; no MCP, no API auth — public
raw + a pasted dump) that raw-fetches three control files, parses the kit heartbeat
grammar, matches the seat's routine in the dump, and prints a ready-to-paste §5 row with
every cell tagged `[registry]` / `[git@HEAD]` / `[self-reported]` plus `[[fill:
verdict]]`. That one artifact already covers the mechanical content of all seven
existing §5 rows AND the manager's hand-done sweep verification — the most advanced
reachable capability is not row-writing but **fleet-wide seat liveness checking as a
one-command habit**, reached by a script of roughly `check_harvest.py`'s size (this
repo's analogue: ~200 lines, stdlib, built in one slice as PR #22).

**4. What breaks it?**
- **Grammar drift (the decisive one):** the heartbeat grammar is kit-owned and moving
  (v1.7.0; the multi-lane `status-<lane>.md` extension in `control/README.md` here is
  already newer than some lanes' pinned kits). A second parser copy in superbot
  `scripts/` silently rots against kit releases — the exact drift class two
  substrate-kit section captures already track (`kit-line-self-drift-local-check`,
  `host-checkers-one-gate`). This is why Q7 splits the build.
- **Registry access wall:** `list_triggers` is callable only from seats with the MCP
  (capability noted seat-dependent in the §5 idea-engine row @ `afbaea7`); the dump-input
  mode is the mitigation, but a stale pasted dump re-imports the transcription-drift
  the tool exists to kill — the dump's age must be printed on the row.
- **Private lanes:** pokemon-mod-lab is PRIVATE (manifest @ `afbaea7`); its raw path
  404s. The harness must report "unreadable (private — manifest-relay only, Q-0260 rule
  3)" rather than "seat dark", or it manufactures false alarms on one of the three
  incoming boots.
- **Laundering regression:** any future edit that auto-fills the verdict cell or drops
  the `[self-reported]` labels turns it into an authority-laundering machine (Q-0120) —
  the labels need a test, not a comment.
- **Obsolescence race:** if fleet-manager ORDER 009 (generated roster) ships first, the
  fetch+parse core belongs there and a superbot twin becomes duplicate work — the
  routing below deliberately puts the manager, who owns both, in the loop.

**5. What does it unlock?**
The ≥3 incoming games-seat boots (Q-0259 r.5) get drift-free §5 rows; the every-wake
re-verification class (brief §2.4) becomes cheap enough to be a habit instead of an
event; the manager's sweep verification and the ORDER 009 roster share one verified
fetch+parse core instead of three hand-rituals; and — if the core lands kit-side — the
kit gains a remote-tree heartbeat-parsing seam that other captured cross-repo checkers
(e.g. this section's `fleet-manifest-freshness-checker`) also need. Nothing is blocked
today by its absence; the cost of not building it is paid in drift risk per boot, and
the boot count is about to grow.

**6. What does it depend on?**
- The kit heartbeat grammar (substrate-kit v1.7.0) — ideally as an exposed parser seam;
  failing that, a ported regex set with an explicit "copied from kit vX.Y.Z" marker a
  drift check can later gate.
- A trigger-registry path: the MCP from a privileged seat, or a fresh `list_triggers`
  JSON dump with its age labeled.
- Public-raw readability of target lanes' `control/` (fails to manifest-relay on
  private lanes, per Q4).
- No unmerged prerequisite anywhere: every input (raw path, registry dump, grammar)
  exists today. Build size ≈ one lane slice (measured analogue: `check_harvest.py`,
  PR #22, one slice).

**7. Which lane should build it?**
Not idea-engine: the consumer is fleet-wide (dispatch copilot, fleet manager, every
future seat boot), so the `park(built-here)` shortcut — legitimate only for
repo-internal PROCESS tooling — does not apply. The honest answer is a split:
- **substrate-kit owns the parsing core.** It owns the grammar being parsed, already
  ships the in-repo status checker, and Q4's drift argument is decisive: one grammar,
  one parser, kit-versioned. A remote-tree/heartbeat-parse seam is proposal-shaped for
  that lane and rhymes with its existing `host-checkers-one-gate` capture.
- **superbot hosts the thin operator wrapper** (registry-dump matching + §5 row
  emission), per the canonical doc — that is where the dispatch copilot works and where
  the runbook lives; **fleet-manager is the standing co-consumer** (sweeps + ORDER 009
  roster, which the manager should be free to absorb this into).
Idea-engine writes only this repo, so the routing is: a Cross-links index line in
`ideas/substrate-kit/README.md` (PR #17 rule — by link, never copied) + a MANAGER relay
note on `control/status.md` for the :30 sweep. The build ORDER is the manager's call.

**8. What is the smallest shippable slice?**
One superbot PR: stdlib `scripts/check_seat.py <repo> --triggers-dump <json>` doing the
three raw fetches + dump match and printing the labeled §5 row skeleton, plus one golden
test replaying an already-verified seat (e.g. the idea-engine row's mechanical cells @
`afbaea7`) asserting the emitted facts match the recorded row — with the heartbeat
regexes carried under an explicit "ported from kit v1.7.0" marker so the kit-seam
extraction can follow as a second, independent slice (kit-side: expose the parser;
superbot-side: delete the port). If the manager prefers ORDER-009-first, the same slice
inverts: the fetch+parse core lands in the roster generator and `check_seat.py` becomes
its single-seat CLI face. Either order is one-slice-sized; what must NOT ship is a
label-free row emitter (Q4).

**Recommendation: park** — no simulator question exists (a deterministic
transport-checking harness is proven by one golden replay against a recorded §5 row, not
by reproduced simulation), and the build — real, timely, one-slice-sized, wanted before
the ≥3 incoming games-seat boots (Q-0259 r.5) — belongs to lanes this repo does not
write: routed to the manager (heartbeat MANAGER note + `ideas/substrate-kit/` cross-link)
for a build ORDER splitting kit-side parser seam from superbot-side wrapper.
