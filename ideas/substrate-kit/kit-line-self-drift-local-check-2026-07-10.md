# Local `kit:` self-drift check — kill the dominant DRIFT class at its source

> **State:** parked(routed — substrate-kit lane build: a zero-network three-artifact self-drift finding in the kit's own `cmd_check` (advisory first wave, strict next) + `upgrade` printing the paste-ready `kit:` line; DRIFT class re-verified LIVE at v1.9.0 — see probe report)
> **Class:** product · **Target:** `menno420/substrate-kit`

## Problem

The kit's brand-new fleet scanner (`bootstrap currency`, shipped kit-lab PR #133)
just measured the fleet's version truth for the first time — and **7 of 10 registry
rows are DRIFT**, of which **5 are the exact same class**: the repo's heartbeat
`kit:` self-report lags its own tree after an upgrade (superbot-next, websites, and
gba-homebrew all claim v1.6.0 over a v1.7.0 tree; fleet-manager claims v1.4.0;
superbot-games' lane heartbeats claim v1.2.0). The contract already says "update it
in the same session as every `bootstrap upgrade`" (planted `control/README.md`,
§ status format) — it is hortatory, and measurably not happening. The fleet scan
catches it, but only agent-side, only on kit-lab's cadence, and only *after* the
stale claim has misled a manifest re-stamp or a coordinator read.

## Idea

Give every adopter a **zero-network local drift check**: a `check --strict` finding
(or Stop-hook advisory first, strict later) that compares the repo's OWN three
version artifacts against each other — vendored `bootstrap.py` stamped header
(primary truth), `substrate.config.json` `kit_version` pin, and the `kit: v<X.Y.Z>`
line in each declared heartbeat file. All three already exist in the committed tree
(`adopt` plants all of them — kit-lab's own finding, its 18:40Z heartbeat note 2),
so the check needs no fetch and runs under the same gate that already validates the
heartbeat. `bootstrap upgrade` completes the loop by printing the exact heartbeat
line to paste. The fleet scanner stays the cross-repo auditor; this makes the
dominant drift class impossible to *commit* rather than merely visible after the
fact.

## Grounding

- Generated registry + drift report (5 self-report-lag rows of 7 DRIFT) @
  [`7e600c6`](https://raw.githubusercontent.com/menno420/substrate-kit/7e600c6f4b9e0e685d7d5a11aed37d435d009dae/docs/adopters.md)
  (fetched 2026-07-10 ~20:55Z; scan generated 20:36:19Z the same day).
- The three-artifact finding + scanner design (tree = truth, self-report = claim) @
  [`7e600c6`](https://raw.githubusercontent.com/menno420/substrate-kit/7e600c6f4b9e0e685d7d5a11aed37d435d009dae/control/status.md)
  (kit-lab §6.3 close heartbeat, notes 2–3).
- The hortatory contract this would make enforcing: this repo's planted
  `control/README.md` § `status.md` format ("update it in the same session as every
  `bootstrap upgrade`") — and this repo's own in-sync `kit: v1.7.0` line as the
  existence proof that the check is satisfiable (`control/status.md`,
  `substrate.config.json`).

**Why now:** the currency checker made the class visible fleet-wide *today* — the
cheapest moment to close the loop is while the drift report is one slice old and
five repos would flip clean on their very next upgrade session.

## Probe report (v0, 2026-07-11)

> **Grounding:** https://raw.githubusercontent.com/menno420/substrate-kit/7122aca08135906c200a975286ed0a669ea59a1f/docs/adopters.md@7122aca · fetched 2026-07-11T06:24:27Z
> **Grounding:** https://raw.githubusercontent.com/menno420/substrate-kit/7122aca08135906c200a975286ed0a669ea59a1f/dist/bootstrap.py@7122aca · fetched 2026-07-11T06:25:44Z

Single-pass battery v0 (no panel trigger: not contested, not
high-blast-radius — a routing decision over a docs-only diff).

*Verify-first, expiry-aware (the PR #48/#25 discipline — the capture was one
day old and a release wave landed overnight): the class is not moot, it
REGENERATED. Upstream shipped v1.9.0 TODAY (`CHANGELOG.md` @ kit HEAD
`7122aca`, ls-remote 2026-07-11T06:24:11Z: `## [1.9.0] - 2026-07-11`, the
model-attribution retrofit band; v1.8.0 is also dated 2026-07-11 and v1.7.1
2026-07-10 — three releases inside ~36h) and ran a fresh fleet scan at
2026-07-11T05:33:10Z (`docs/adopters.md` @ `7122aca`, fetched 06:24:27Z):
10 registry rows, 6 DRIFT rows carrying 7 drift-report lines, of which FIVE
repos are again the exact self-report-lag class the capture names — websites
v1.8.0, gba-homebrew v1.8.0, superbot-games v1.7.1 (BOTH lane heartbeats,
`status-mining.md` + `status-exploration.md`), trading-strategy v1.7.1,
fleet-manager v1.7.0 — every one a heartbeat claim over a v1.9.0 tree. vs the
capture's scan (@`7e600c6`, generated 2026-07-10T20:36:19Z): only
superbot-next flipped clean (it updated all three artifacts);
trading-strategy JOINED the class. Not a stale-scan artifact: live HEAD
spot-checks this session (raw fetches 06:25:03–06:25:11Z) confirm websites
@`7da9fbf`, gba-homebrew @`31c8672`, and fleet-manager @`6dedff6` each carry
dist header `KIT_VERSION = "1.9.0"` + config pin `"kit_version": "1.9.0"` but
heartbeat `kit:` lines v1.8.0 / v1.8.0 / v1.7.0 — DRIFT at HEAD right now.
And still NO local check anywhere: the vendored v1.8.0 `bootstrap.py` here
(`cmd_check`, line 12364) and the upstream v1.9.0 dist (`cmd_check`, line
12909) run the same checker list with no version-consistency checker;
`_check_one_status` (line 2287) emits only status-missing /
status-no-heartbeat / status-stale and never parses the `kit:` version; zero
`self-drift` / `check_kit_version` symbols in either dist; empirically, this
repo's own `check --strict` passes green with no such finding class
(preflight run 06:24Z this session). No release since the capture shipped one:
v1.7.1 was upgrade hardening (the currency SCANNER rode kit-lab #133
alongside), v1.8.0 was the claims convention + `grammar.py` + the staged
enabler, v1.9.0 is the model-attribution retrofit — the scanner (cross-repo,
agent-side, network) remains the only surface, exactly the "only after the
fact" gap the capture names.*

**1. What is this really?** An enforcement move: it turns the hortatory
contract "update it in the same session as every `bootstrap upgrade`" (the
kit-planted `control/README.md` § status format — measurably failing on both
scans, 5 repos each) into a zero-network `check --strict` finding that
compares the three version artifacts already committed in every adopter's own
tree: vendored dist header (primary truth) · `substrate.config.json`
`kit_version` pin · the `kit: v<X.Y.Z>` line in each declared heartbeat file.
The fleet scanner made the class VISIBLE after the fact, on kit-lab's cadence,
agent-side over the network; this makes the class impossible to COMMIT, at the
adopter's own gate, with no fetch. Same-class sibling of the
heartbeat-grammar self-check and branch-prefix-tripwire routings already on
this section's README — config-vs-reality checks belong to the lane that
plants both sides.

**2. What is the possibility space?** Ascending: (i) Stop-hook advisory — a
session-end nudge when the `kit:` line disagrees with the tree (softest,
catches the drift the session that made it); (ii) a `check --strict` finding
in `cmd_check` — the gate on every PR, including the upgrade PR that commits
the drift (the capture's core); (iii) `upgrade` prints — or offers to
auto-edit — the paste-ready heartbeat line: `kit_line_example()` already
exists (dist line 752) but has ZERO call sites in the v1.9.0 dist, so today
`upgrade` never tells the session what to paste; (iv) generalized N-artifact
version truth — the same comparison extended to cross-repo claims about this
repo (manifest row, adopters row), which stays scanner-side by construction
(those artifacts live in other repos). Negative space: the status quo doc
contract (measured failing on two consecutive scans — twice is a pattern, not
an accident); a CI-side cross-repo gate (the currency scanner already IS the
cross-repo auditor, deliberately agent-side because kit CI cannot auth to
sibling repos — its own header says so).

**3. What is the most advanced capability reachable by the simplest
implementation?** One new checker inside `cmd_check`, composed entirely of
pieces the v1.8.0+ dist already vendors into every adopter: `parse_kit_line` /
`KIT_LINE_RE` (the kit-owned grammar module — writer and enforcer agreement
already pinned by the kit's `tests/test_grammar.py`; lenient parse proven on
decorated live heartbeats) + `KIT_VERSION` (line 90, the dist's own header
truth) + the config-pin loader + a loop over `config.heartbeat_files` (line
279). `RepoCurrency.drifts()` (line 10751) is ALREADY the pure three-artifact
comparison, fetcher-injectable — pointing it at a filesystem fetcher instead
of the network makes it local. ~Tens of lines of composition, no new parsing,
no new grammar — and it kills the fleet's dominant DRIFT class (5 of 6 DRIFT
rows today) at every adopter's next upgrade, because the check rides the same
`check --strict` the planted gate already runs.

**4. What breaks it?** (a) **Consumer #0 is born-red:** substrate-kit's OWN
registry row is tree-internal DRIFT — config pin 1.0.0 vs dist 1.9.0, on BOTH
scans (@`7e600c6` and @`7122aca`) — so a strict-from-day-one check reds the
kit repo itself the moment it ships; advisory-first (or fixing the kit's own
pin in the same slice) is a correctness requirement, not politeness.
(b) **Multi-lane heartbeats:** the checker must iterate ALL declared
`heartbeat_files`, or SHARED repos escape — superbot-games drifts per-lane
(v1.2.0 claims at capture, v1.7.1 in both lane files today); checking only
`control/status.md` would pass it while both lanes lie. (c) **Decorated
lines:** live heartbeats decorate parsed fields — gba-homebrew @`31c8672`
reads `check: green (full --strict exit 0 at close)` and parses fine under the
lenient grammar — so the finding must compare the VERSION TOKEN only, never
byte-match the line against `kit_line_example()`. (d) **Wrong-surface risk is
already solved:** the drift is committed BY the upgrade PR itself, and the
planted gate runs `check --strict` on exactly that tree — the check fires at
the moment of the crime; pairing it with `upgrade` printing the paste-ready
line (Q2 iii) closes the loop so the finding almost never fires red in
practice.

**5. What does it unlock?** Trustworthy `kit:` input for every downstream
reader: fleet-manager's machine-generated roster (`gen_roster.py` re-reads
lane heartbeats each wake — fleet-manager itself claims v1.7.0 over a v1.9.0
tree today) and the manager's staleness math stop consuming known-stale
self-reports; the scanner's DRIFT column becomes SIGNAL (genuine anomalies —
tree-internal pin drift, no-heartbeat rows) instead of re-measuring the same
lag class every wave; and it pattern-completes the config-vs-reality check
family already routed to this seam (heartbeat-grammar self-check,
branch-prefix tripwire — see this section README's Cross-links).

**6. What does it depend on?** The v1.8.0+ grammar module in the adopter's
vendored dist (`parse_kit_line` — already fleet-wide: every adopted row on the
05:33:10Z scan runs a v1.9.0 tree except superbot's pin-only row); the planted
`substrate.config.json` `kit_version` pin and `heartbeat_files` declaration
(both planted by `adopt`, per the capture's kit-lab finding); resolution of
the kit's own 1.0.0 pin before any strict wave (Q4a); nothing else — zero
network by construction, all three artifacts live in the committed tree.

**7. Which lane should build it?** substrate-kit, unambiguously: the check
ships inside the kit's own `cmd_check` (every adopter inherits it at their
next `upgrade` — the same distribution mechanism that regenerates the drift
today ships the cure); the grammar and the drift logic are kit-owned modules
(`grammar.py` `parse_kit_line`, `RepoCurrency.drifts()`), so building it
anywhere else re-creates the second-parser-copy rot the seat-boot probe's Q4
already ruled decisive — same one-grammar/one-parser routing as the seat-boot
and heartbeat-grammar siblings on this README. Fleet-political fit: kit-lab's
own heartbeat says version truth "now defers to the generated
docs/adopters.md … pending owner's §7 ruling" — a LOCAL check complements the
scanner rather than competing with it (the capture's own framing: the scanner
stays the cross-repo auditor). Not idea-engine (this repo writes only itself);
routing = this section README's index + the heartbeat notes for the manager's
:30 sweep.

**8. What is the smallest shippable slice?** One kit PR: a self-drift checker
in `cmd_check` — advisory first wave, strict next — comparing dist header vs
config pin vs the `kit:` version token across ALL declared `heartbeat_files`
(kit's own pin fixed in the same slice, or the advisory posture carries it),
plus `upgrade` printing the paste-ready line via the existing, call-site-less
`kit_line_example(KIT_VERSION)`. Red/green reference exists in the wild today:
any of the five live-drifted repos (websites `7da9fbf` / gba-homebrew
`31c8672` / fleet-manager `6dedff6` red; this repo — v1.8.0 all-three-in-sync
— green).

**Recommendation: park** — routed (substrate-kit lane build): the class re-verified LIVE at v1.9.0 (today's 05:33:10Z scan: the same 5-repo self-report-lag class regenerated by the release wave, confirmed at live HEADs 06:25Z; NO local check in v1.8.0 or v1.9.0 `cmd_check`), and the natural builder is the kit lane — kit-owned grammar + `cmd_check` seam, a near-composition of already-vendored pieces every adopter inherits at next upgrade; no sim-lab proposal (no simulator question — a contract check is proven by its own red/green).
