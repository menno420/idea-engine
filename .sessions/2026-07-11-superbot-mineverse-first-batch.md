# Session — superbot-mineverse first idea batch (the newborn lane's empty section gets its first honest captures)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-11 ~04:02Z (worker slice, dispatched by the continuous-mode coordinator per Q-0265)

## Scope

The `ideas/superbot-mineverse/` section stub was seeded by PR #66 when the
fleet-manager generated roster became the canonical lane registry and surfaced the
lane born the same window; it has had zero idea coverage since. This slice ships the
first batch: FIVE captures grounded on the live lane state, plus the section index,
per the honesty guard (drops recorded below). Section claimed first —
control/claims/seed-superbot-mineverse-batch-1.md landed on main via fast-lane PR #75
(merged 04:00:16Z) before any build work; no competing claim at HEAD.

## Grounding pins (every load-bearing claim)

- **superbot-mineverse** live HEAD `510fa3e` (`git ls-remote` 2026-07-11T03:59:59Z;
  raw fetches at that pin 04:00:19–21Z; blobless clone for the commit walk). The
  briefing's pin `a2672dc` moved ONE commit before this slice's fetch — the delta is
  only the lane's own heartbeat PR #22 ("deepening slice 2 merged — full field
  coverage"), no capture-changing content; every lane fact below cites `510fa3e`.
  Lane state at the pin: ladder `0 ✓ · (a) ✓ · (b) ✓ · (c) ✓ web-side · (d) PREPARED`
  (live-prod owner-flag-gated), 187 tests green (163→187 at its PR #21), kit v1.8.0 ·
  check green · engaged yes, heartbeat updated 03:58:00Z, micro-polish slice in
  flight. Both bot-lane FLAGs carried verbatim on the heartbeat: FLAG 1 (READ relay —
  `mining_snapshot.v1`, 16 per-miner v1 fields, ~60s push cadence, done = validates
  against schemas/mining_snapshot.v1.schema.json) and FLAG 2 (WRITE endpoint —
  HMAC-signed POST action proposals, closed enum, idempotency by action_id, audit
  every web action, test-guild allowlist, done = tests/test_actions.py shim fixtures
  pass against the real endpoint), both "informational until the manager picks them
  up". Path checks 200 at the pin: docs/mining-data-contract.md,
  schemas/mining_snapshot.v1.schema.json.
- **fleet-manager** live HEAD `dd8dc10` (`git ls-remote` 2026-07-11T03:59:59Z; raw
  fetches at that pin 04:00:21Z + 04:01:23Z). docs/roster.md is STILL generation #4,
  generated-at 2026-07-11T01:58Z — the same generation the briefing pinned at
  `93d3a4d`; the superbot-mineverse row verbatim still reads "stage (a) READ CONTRACT
  v1 + backlog slice in flight … `check: red` … engaged: no", pinned at lane `1120a3b`
  01:57:13Z — now FOUR ladder rungs and ~2h behind the lane heartbeat's 03:58Z
  ladder line. Lane truth wins (README § Idea file grammar freshest-wins rule);
  the drift itself grounds capture 5. docs/proposals/
  games-program-mapping-conformed-2026-07-10.md at the same pin places the
  committed-JSON "mining character-sheet" game-state read feed on the superbot lane
  (surface (a); "contract v1 (family = mining character-sheet on games-web's
  committed consumer schema)") — the second projection demand capture 1 reconciles.
- **games-web / product-forge facts** are cited by relative link to the two
  product-forge captures merged @ PR #71 (this repo, in-tree), never re-derived:
  `ideas/product-forge/games-web-mineverse-scope-seam-2026-07-11.md` +
  `ideas/product-forge/read-projection-fanin-fourth-consumer-2026-07-11.md`.

## The batch (5 captures, ordered per Q-0259 — games completion wave + rebuild pace first)

1. `mining-projection-single-source-2026-07-11.md` (product → superbot) — two
   independently-contracted read projections of the same bot-side mining state are
   now demanded (FLAG 1's push relay + fleet-manager's committed-JSON character-sheet
   feed), written on opposite sides of the lane's birth, neither citing the other;
   ONE bot-side projection module should emit both.
2. `snapshot-field-parity-audit-2026-07-11.md` (product → superbot-mineverse) — audit
   `mining_snapshot.v1` field coverage against games-web's `games-web.character-sheet`
   v1.0.1 BEFORE either contract freezes; additive v1 fields are cheap now.
3. `snapshot-contract-shared-constant-2026-07-11.md` (product → superbot-mineverse) —
   graduates the lane-born card idea: importable `snapshot_contract.py` /
   `REQUIRED_MINER_FIELDS` shared constant, turning FLAG 1 conformance into a CI
   drift gate on both sides.
4. `shim-replay-determinism-harness-2026-07-11.md` (product → superbot-mineverse) —
   graduates the other lane-born card idea: property-based replay-determinism test
   holdable first against the shim, later verbatim against the real FLAG 2 endpoint.
5. `heartbeat-ladder-field-2026-07-11.md` (process → fleet-manager) — a
   machine-parseable `ladder:` heartbeat line so the roster generator can surface
   stage-level drift on fast movers, grounded by THIS lane's four-rung roster lag.

## Honesty-guard drop record (candidates considered and NOT captured)

- **Structured machine-readable FLAG/dependency records** (the heartbeat FLAGs are
  prose a consumer must re-parse every sweep) — cross-cutting kit/heartbeat-grammar
  doctrine, belongs to a substrate-kit or fleet section claim, not this
  section's; noted here so it isn't orphaned, deliberately not captured under a
  superbot-mineverse claim.
- **The remaining 9 ungraduated lane session-card ideas** — left in-lane (harvest
  rule: lane-born ideas are indexed by link, never mass-copied, and the lane's own
  never-idle backlog is their natural home); only the two FLAG-de-risking ideas
  graduated, each linking its source card at the pin.

## Verification (real runs, this tree)

```
$ python3 scripts/check_ideas.py
check_ideas: OK — 296 idea files conform to the README grammar
$ python3 scripts/check_sections.py
check_sections: OK — 13 sections in sync with the lane registry
$ python3 scripts/preflight.py
preflight: OK — all 7 checks green
```

Full `python3 scripts/preflight.py` + `python3 bootstrap.py check --strict` run green
immediately before push (after the heartbeat overwrite). Sibling PR #76
(idle-economy-sim-kernel probe + PROPOSAL 006) landed mid-flight and was merged
origin/main forward-only per the README recipe — clean merge, no conflicts (this
branch had not yet touched control/status.md); the heartbeat overwrite was written
ON the merged tree, keeping both sides' facts. No merge outcome is claimed here for
this slice's own PR — the number is stamped by a follow-up per the #72 precedent.

**📊 Model:** fable-5 · medium · first-batch capture slice (5 idea files + index +
card + claim add/clear + heartbeat; no scripts, no workflows, no proposal —
task-class: bounded section-seeding batch)

## 💡 Session idea

**For kit-native lanes, the richest un-harvested idea surface is `.sessions/`, not
`docs/ideas/`** — this lane's `docs/ideas/` backlog is EMPTY while 11 session cards
each carry an ungraduated `💡 Session idea` (the card contract REQUIRES one per
session, so the surface grows every wake by construction). Both ideas this batch
graduated came from cards, found by hand-reading. A harvest sweep keyed on the 💡
byte-form marker (the same exact-marker discipline `.sessions/README.md` already
enforces) would have found them mechanically — and would generalize to every
kit-adopted lane in the fleet.

## ⟲ Previous-session review

PR #71 (product-forge first batch, squash `767cf1b`) + its #72 stamp follow-up —
claims verified against this tree and the live lanes: all four captures exist as
carded and lint-clean; its two mineverse-grounded captures (the scope seam + the
fourth-consumer fan-in) re-verified still live at the NEW lane pin `510fa3e` — FLAG 1
unchanged verbatim on the heartbeat, the seam still unruled anywhere (neither the
mineverse tree nor fleet-manager @ `dd8dc10` mentions it), so this batch's
cross-links point at premises that still hold. Its handoff aged perfectly: it named
superbot-mineverse "proven rich grounding (163 tests, live contracts, two bot-lane
FLAGs) for a sibling first batch" and suggested a mineverse-section Cross-links row
back to its seam/convergence captures — this slice executed exactly that (both
adopted: the batch + the Cross-links subsection). Two improvements adopted from its
card: claim + born-red card as the earliest commits (early in-flight signal), and its
💡 taken as METHOD — "when a capture touches a lane younger than ~a day, the lane-HEAD
read is where the idea actually comes from" — applied by re-pinning both repos at
fetch time before writing a word (and indeed both HEADs had moved past the dispatch
briefing's pins).

## Handoff → next wake

Inbox: ORDER 001 remains the only order, standing rule re-satisfied by this card
(📊 Model: fable-5); re-read at HEAD anyway. Ripest heads this batch plants: the
**mining-projection single-source** capture is expiry-aware (Sequence: before the
batched read-only-API providing ORDER / games-web phase-2 — both could route any
wake; it shares the product-forge scope-seam head's window and should be probed with
it or right after it), and the two **FLAG-de-risking graduations** (shared constant +
replay harness) are one-file lane slices that only do their job BEFORE the bot lane
starts FLAG 1/FLAG 2 — relay-worthy the moment the manager picks the FLAGs up. All
three empty roster-born stubs are now seeded (product-forge @ #71, superbot-idle @
#73, superbot-mineverse @ this slice). Watch the lane's fast cadence: it moved twice
during the two sibling batch windows (a2672dc → 510fa3e in ~20 min); the self-serve
prior applies with force here — verify-first at lane HEAD before probing anything in
this section. Telemetry residue: this seat's hook-born guard-fires appends left
uncommitted for the telemetry lane per the PR #32/#58/#62 precedent.
