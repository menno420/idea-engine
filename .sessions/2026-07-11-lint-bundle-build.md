# Session — lint-bundle build (five standing advisory lint heads, one PR)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-11 (dispatched by the continuous-mode coordinator per Q-0265)

## What this session did

The lint-bundle build slice the PR #144 grooming ledger left queued (item (c)): the
five standing advisory lint heads accumulated across session cards, built as ONE
bundle per the park(built-here) shortcut — captured as
`ideas/fleet/lint-bundle-2026-07-11.md` (probe report appended, verdict
park(built-here), no outbox proposal — a contract check is proven by its own
red/green, the #114 precedent). Section claimed first
(`control/claims/build-lint-bundle-2026-07-11.md`, fast-lane PR #146, merged
09:15:39Z by the enabler; the only sibling claim at HEAD `2aa4a4b` is
probe-product-forge-final-two via PR #145 — disjoint section). Each head was re-read
at its SOURCE card and implemented against its own wording, never a heartbeat
summary (the PR #47 discipline):

1. **Step-anchor drift** (PR #36 card 💡,
   `.sessions/2026-07-10-preflight-gate-selfcheck.md`) →
   `scripts/preflight.py --step-anchor-drift`, ninth CHECKS entry, ADVISORY (always
   exit 0). Two legs: a preflight-run-like line (stem-match on
   `scripts/preflight.py`, per the README stem-grep discipline) that does not
   byte-match `PREFLIGHT_RUN` (the FALSE-red-in-waiting class), and the anchored run
   line's step carrying the guard bytes anywhere but its actual `if:` condition (the
   FALSE-green class the binary `--gate-wiring` check cannot see — confirmed in the
   smoke test below). `--gate-file` smoke seam per the `--config` precedent.
2. **Cross-link state-echo** (PR #29 card 💡,
   `.sessions/2026-07-10-seat-boot-harness-probe.md`) → STATE-ECHO pass in
   `scripts/check_ideas.py`, ADVISORY warnings (warn-first per the source card;
   READMEs carry no filename date to gate on). Scans every section README's
   index/cross-link bullet entries (with continuation lines — the fleet-README
   form), takes the FIRST legal state token after the entry's first local `.md`
   link in either blessed position (`— <state> ·` / `· <state>`), and diffs state
   FAMILIES against the linked file's actual `> **State:**` (family = token before
   any `(…)` reason; `park` and `parked` deliberately distinct).
3. **Recommendation-vocabulary** (PR #33 card 💡,
   `.sessions/2026-07-10-capability-pair-probe.md`) → RECOMMENDATION pass in
   `scripts/check_ideas.py`, ADVISORY (warn-first outside probe blocks, per the
   source card): any `^**Recommendation:` line OUTSIDE probe blocks (= before the
   first probe heading, matching the existing block-split semantics) must be in the
   legal vocabulary; the two live outside-block instances (both legal `park`
   pointer dispositions) pass untouched.
4. **`check_harvest --states`** (PR #22 card 💡,
   `.sessions/2026-07-10-harvest-freshness-checker.md`) → the full per-doc
   state-drift depth `--re-badge` deliberately bounded away (the PR #47 card:
   "the full `--states` depth stays unbuilt per the PR #22 card 💡", verbatim):
   flag-gated (batched blobless-clone blobs, the same rationale), BOTH drift
   directions at lifecycle-stage granularity (built/retired/open — raw-token
   compare would false-drift every correctly mirrored entry), suggestion pass,
   report-only, STATE-DRIFT findings count as harvest work.
5. **Undeclared-heartbeat-key tripwire** (PR #59 card 💡,
   `.sessions/2026-07-11-contract-grooming-round-4.md`) →
   `scripts/preflight.py --heartbeat-keys`, tenth CHECKS entry, ADVISORY (the ⚑
   field-check precedent — grammar nags never red). Parses each declared heartbeat
   file's (`substrate.config.json::heartbeat_files`, default `control/status.md`)
   top-level `<key>:` tokens against the control/README format block's documented
   set (`updated phase health kit last-shipped blockers orders ⚑ needs-owner
   notes` — a loud co-edit constant); it would have caught the `routine:` fold-in
   miss at write time (the head's arming case — smoke-verified below).

**Drops: none** — all five heads verified live before building (dedup grep +
read-the-body: recommendation vocabulary checked only INSIDE probe blocks;
check_ideas skips READMEs entirely; `--re-badge` ≠ `--states` per the PR #47 card's
own verbatim deferral; only the binary byte check on gate anchors; zero heartbeat
key checks anywhere — `check --strict --status-only` gates presence/staleness, not
key declaration).

ADVISORY-first held everywhere: every new head warns and never affects any exit
code — stricter than the PR #24 date-gate pattern (which hard-gates new-dated
files) because none of these surfaces carries a filename date to gate on
(READMEs/heartbeats/gate) or the flagged shape is legitimate (outside-block
recommendations). Hermeticity preserved: default runs add ZERO network
(`--states` is flag-gated, wake-time-only like all of check_harvest — still NOT
in preflight or CI); existing exit conventions untouched.

## Live-run findings (full real tree)

`python3 scripts/check_ideas.py` (pre-fix): 6 STATE-ECHO warnings — all genuine
badge rot, all MECHANICALLY FIXED in this PR (echo updated to the linked file's
actual state family, short form):

- `ideas/superbot/README.md:254` — wild-encounters-activity-spawning: `captured` →
  `sim-ready` (PROPOSAL 003 has been in the outbox since 2026-07-10).
- `ideas/superbot-games/README.md:10–13` — all four rows still said `captured`
  while their files were probed to `parked(build-direct)` ×3 /
  `parked(overtaken)` (probes #~128–#134 re-badged files, not this index).
- `ideas/websites/README.md:12` — public-leaderboards-committed-feed: `captured` →
  `parked(routed)`.

Post-fix run: `check_ideas: OK — 301 idea files conform … (3 warning(s), advisory)`
— the 3 are the known deliberate SIM-VERDICT legacy advisories, unchanged.

`python3 scripts/check_harvest.py --states` (wake-time, network — run once for the
smoke + live read, 09:30Z): superbot section 237/237 HEAD unmoved, 0 state-drift;
websites section HEAD MOVED (`d862364` → `6663e6c`) with 1 CHANGED
(`docs/ideas/backlog.md` blob `f1d93e3` → `d130d71`) and 1 REAL state-drift:
`open-pr-awareness-at-wake-2026-07-10.md` — local `parked(build-direct)`,
canonical records `state: built`. JUDGMENT-LADEN, deliberately NOT fixed here: the
2026-07-11 re-pin session already saw the lane self-serve (websites#90), appended
the upstream-outcome note, and ruled "verdict STANDS — forward-only
upstream-outcome note only" (the #~120 card); flipping it to historical(…) would
re-litigate that ruling from a lint line. Reported for the next harvest wake
instead (with the CHANGED backlog.md + moved HEAD, which size that wake's re-pin
rider). This is the suggestion-pass honesty `--re-badge` established, held.

## Smoke tests (planted violations — each head fired, every plant removed)

All plants in the scratchpad or via a temporary in-tree edit reverted the same
session; verbatim key output:

1. step-anchor leg 1 (gate copy, run line reworded `python3` → `python`):
   `step-anchor-drift: DRIFT (advisory) — 1 anchor finding(s) … does not
   byte-match the anchor `run: python3 scripts/preflight.py``; exit 0.
2. step-anchor leg 2 (gate copy, `if: true` + guard bytes moved into a comment):
   `… contains the guard bytes … but NOT on its `if:` condition —
   check_gate_wiring would false-green`; exit 0 — and a direct evaluation of the
   binary check's own predicate on the doctored copy printed
   `GREEN (false-green confirmed)`, proving the leg catches what `--gate-wiring`
   cannot.
3. STATE-ECHO (temp ideas tree via `--ideas-dir`, index says `captured`, file says
   `parked(routed — smoke)`): `warn: STATE-ECHO ideas/testsec/README.md:5: entry
   echoes state 'captured' but the linked … is 'parked(routed — smoke)'`; exit 0.
4. RECOMMENDATION (same temp tree, planted `**Recommendation: ship-it-immediately**`
   outside any probe block): `warn: RECOMMENDATION …: outside-block recommendation
   is not in the legal vocabulary`; exit 0 (advisory — the file otherwise conforms).
5. `--states` (temporary in-tree plant: `activity-atom-feed-2026-07-09.md` state
   flipped `historical(menno420/websites#41)` → `captured`, then reverted via
   `git checkout`): `STATE-DRIFT: docs/ideas/activity-atom-feed-2026-07-09.md —
   local entry says 'captured', canonical records `state: shipped``; exit 0.
6. heartbeat-keys (scratch heartbeat with a planted `routine:` line, via
   `--status-file`): `heartbeat-keys: DRIFT (advisory) — 1 undeclared heartbeat
   key(s) … undeclared top-level key `routine:``; exit 0. The live
   `control/status.md` parses 9/9 declared keys, zero warnings.

## Close-out

**Evidence (verified, this tree):**

- Full `python3 scripts/preflight.py` — ALL TEN checks PASS (the two new advisory
  entries report-only) — and `python3 bootstrap.py check --strict` exit 0,
  run immediately before push after the heartbeat overwrite. Verbatim tails:

  ```
  step-anchor-drift: OK — every preflight-run-like line in .github/workflows/substrate-gate.yml byte-matches the anchor and the guard sits on the step's `if:` condition
  preflight: PASS — step-anchor-drift advisory (report-only, never gates) (exit 0)
  heartbeat-keys: control/status.md — 9 top-level key line(s) parsed
  heartbeat-keys: OK — every top-level heartbeat key is in the documented format-block set
  preflight: PASS — heartbeat-keys advisory (report-only, never gates) (exit 0)
  preflight: OK — all 10 checks green
  ```

  `bootstrap.py check --strict` on the in-progress card correctly reported the
  designed born-red HOLD ("this red is the designed hold, not a defect"); the
  post-flip rerun on this final tree is exit 0 (the flip is this card's last
  edit, per the contract).
- `bootstrap.py reflect --mine` ran at wake (R-0038 mined); ceremony held: inbox
  read FIRST at origin/main HEAD `202b516` and re-read at `2aa4a4b` post-claim
  (ORDER 001 is standing/done per PR #144 — NOT re-claimed; no new orders), claim
  landed on main BEFORE build (PR #146), claims dir re-read at HEAD post-merge.

**Judgment:**

- Decisions made: all five heads ADVISORY (never exit-affecting) — see the
  bundle idea file Q8 for the per-head severity reasoning; family-granular echo
  compare and stage-granular state compare (raw compares false-positive on
  reason detail / vocabulary mismatch); `--states` built as a both-direction
  suggestion pass, never an auto-editor (the open-pr-awareness live case is a
  deliberate local park that a naive auto-fix would have clobbered); six
  mechanical badge fixes taken, one judgment-laden state divergence reported not
  fixed; smoke seams (`--gate-file`, `--status-file`) added matching the
  `--config` precedent.
- Next session should know: `check_harvest --states` belongs to harvest wakes
  (network); the websites section has real drift queued (moved HEAD `6663e6c` +
  CHANGED backlog.md + the open-pr-awareness state-drift line) — the next
  re-harvest slice is sized. The two preflight heads are the reference
  implementations for the substrate-kit routed family
  (`own-heartbeat-parse-self-check` / `host-checkers-one-gate`) — cite them if a
  kit ORDER bundles that fan-in.

**📊 Model:** fable-5 · high · three bounded stdlib script extensions + capture/probe
+ six index-badge fixes + card + heartbeat (no workflows touched, no proposal —
nothing sim-shaped)

## 💡 Session idea

**The suggestion-pass verdict needs a place to stick.** `--states` (and `--re-badge`
before it) reports lifecycle divergence as a suggestion because some divergences are
deliberate (open-pr-awareness: lane built its half, local park verdict STANDS). But
the deliberateness lives in a session card, not on the surface the checker reads —
so every future `--states` run will re-report the same line and every future reader
must re-derive the ruling. One-line grooming seed: bless an optional
`(state-drift: deliberate — <reason/PR>)` annotation on link-index entries that
`--states` reads and reports as ACK'd (distinct from open drift), the same
grammar-blessing move as the pin annotation line (PR #28) — cheap now, noisy after
five deliberate divergences accrete.

## ⟲ Previous-session review

The venture-lab verify-and-park card
(`.sessions/2026-07-11-venture-lab-forecast-verify-park.md`, the newest card at this
wake) holds up on this tree: the check_sections roster migration it shipped
mid-slice is live and green (this slice's every preflight run reports "13 sections
in sync with the lane registry" — its parser survived this window's roster reads),
its three seeded sections exist with README stubs (product-forge already carries
four idea files and a sibling claim this very window — the stub-first rule paid off
within hours), and its claim file is gone at HEAD. Its card's 💡 (verify-and-park
needs a named note shape) remains queued for the next grooming round — not consumed
here (disjoint surface; this slice is a build). One nit its card already
self-flagged and this session confirms: the kit auto-draft named its card
generically and the session renamed it per probe-card precedent — the rename
convention is still discipline-only, which is exactly the class of contract this
bundle turns into tripwires; a card-name lint would be a sixth head for a future
bundle. Its handoff's "three venture-lab captured heads remain" matches the section
index at HEAD (three rows still captured/parked-pending).

## Outcomes

Verdict: **park(built-here)** — all five heads shipped in this PR as advisory
checks; state advances to `historical(<this PR>)` on merge per the README shortcut
grammar. Landed per README § Landing conventions (PR READY; `build/*` matches the
enabler's patterns — auto-merge arms once this card flips complete; REST
merge-on-green as fallback). Claim file deleted in the close-out commit.

## Handoff → next wake

Inbox first. The websites re-harvest is sized and queued (moved HEAD + CHANGED
backlog + one ACK-pending state-drift line — see Live-run findings). The lint
surface is now: 10 preflight checks (2 new advisory), check_ideas with 2 new
advisory categories, check_harvest with the full `--states` depth. Standing
lint-head list from rounds 3–4 is EMPTY (all five built here; the PR #47 card's
`[[fill:` tripwire was already built by #~124's UNFILLED). New seeds: this card's
💡 (deliberate-divergence ACK annotation) + the card-name lint sixth-head note in
the review above.
