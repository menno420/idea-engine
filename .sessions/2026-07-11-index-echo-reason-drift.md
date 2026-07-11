# Session — build: index-echo reason-presence drift check (STATE-ECHO extension)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-11 (worker slice, dispatched by the coordinator
> under continuous-chaining mode per Q-0265)

## Scope — the slice plan

The PR #161 card's 💡 executed: extend the STATE-ECHO pass in
`scripts/check_ideas.py` so a section-README bullet's state token that disagrees
with its idea file's `> **State:**` line on REASON PRESENCE warns — the exact
drift class PR #161 hand-fixed 3 instances of (bare `parked` bullets whose files
already carried full terminal `parked(<reason>)` states).

Verify-first overlap check (mandatory, done before writing code): PR #149's
STATE-ECHO pass (`.sessions/2026-07-11-lint-bundle-build.md` head 2) already
compares state FAMILIES — `parked` echo vs `parked(routed)` file counts as a
MATCH, so the #161 class passes silently. The lint-bundle idea's Q4 names this
deliberately ("family-compare blindness … reason-detail drift is judgment
territory") and the #161 card's 💡 carves the fix precisely: "`parked` vs
`parked(...)` counts as agreement only bare-vs-bare". Verdict: PARTIALLY covered
— EXTEND the existing pass with a reason-PRESENCE leg (never reason-DETAIL:
abbreviated echoes stay blessed per the #160 line-59 format precedent), no
parallel check.

Claim ritual honored: `control/claims/build-index-echo-reason-drift.md`
fast-laned FIRST as PR #162 (merged c3682dd by the enabler within the minute),
claims dir re-read at HEAD post-merge — empty except README.md and this claim.
Claim file deleted in this PR's close-out.

## What this session did

- **`scripts/check_ideas.py` — STATE-ECHO reason-presence leg** (stdlib, same
  pass, same ADVISORY severity — extend-not-duplicate per the overlap verdict
  above): when echo and file-state FAMILIES agree, a BARE echo against a file
  state that carries a `(<reason>)` now warns. Bare-vs-bare stays agreement; an
  echo with ANY parenthetical passes (abbreviated echoes blessed, the #160
  index-row precedent); reason-DETAIL drift stays deliberately unchecked
  (lint-bundle Q4 — judgment territory). The `STATE_ECHO_RE` constant grew an
  optional `(\()` group that must sit IMMEDIATELY after the token — a
  space-separated parenthetical is prose, not a state reason. Severity note:
  advisory-only, NOT date-gated hard — the script's date-gate pattern (PR #24)
  keys on the linted FILE's filename date, and READMEs carry no filename date
  (the exact reasoning the PR #149 card recorded for the family leg; held).
- **41 mechanical exact-echo re-badges in `ideas/superbot/README.md`** — the
  live run's full yield (list below). Judgment basis: that README's own line-18
  convention spells the form `historical(...)`, every OTHER section README
  echoes historical WITH its reason (`historical(#62)`,
  `historical(menno420/websites#41)`, fleet README `historical(#2)` …), and
  the #161 card's exact-echo precedent covers the fix form. Zero non-historical
  hits (the 3 parked-class instances were already fixed by #161 itself).
- **Extension note appended to `ideas/fleet/lint-bundle-2026-07-11.md`** (the
  idea behind PR #149's STATE-ECHO head) per the extending-shipped-ideas
  precedent (probe-report-lint's PR #13/#24 notes lineage) — probe report and
  state untouched.
- **Zero wiring change**: preflight CHECKS entry 2 already runs this checker —
  `scripts/preflight.py`, both workflows, and the outbox mode untouched.

**📊 Model:** fable-5 · one checker-leg extension + 41 index re-badges + docs
(idea-file extension note, card, heartbeat, claim clear)

## Live-run findings (full real tree)

`python3 scripts/check_ideas.py` (pre-fix): 41 new STATE-ECHO reason-presence
warnings — ALL bare `historical` echoes in `ideas/superbot/README.md`, all
genuine badge rot vs that README's own convention, all exact-echo re-badged in
this PR (README line numbers pre-fix; every echo now carries the linked file's
full state reason verbatim):

33 audit-seam-coverage-checker · 35 automod-spam-detection-gaps ·
38 backup-integrity-check · 40 band-pr-merge-status-helper ·
49 btd6-shorthand-corpus-eval · 56 ci-dropped-synchronize-auto-retrigger ·
57 claim-remote-visibility-scan · 61 codex-automated-pr-review ·
69 command-collision-checker · 78 control-plane-single-source-pointer ·
80 coordinator-self-review-against-1901 · 81 creature-pvp-rematch-button ·
82 creature-sim-engine-constant-parity-guard · 83 cross-agent-trust-ledger ·
88 deferred-action-restart-recovery-checker ·
93 diagnostic-cog-platform-group-extraction · 96 dispatch-resolution-json-hermes ·
104 fishing-bait-crafting · 105 fishing-gear-stats ·
106 fleet-manifest-freshness-checker · 113 games-economy-faucet-sink-diagnostic ·
116 generated-artifact-freshness-umbrella · 119 governance-files-presence-guard ·
122 help-nav-attachment-seam · 127 idea-subsystem-tag-on-ideas ·
129 idle-game-offline-summary · 137 ledger-checker-print-pr-subjects ·
138 ledger-checker-range-scope · 139 ledger-dedup-linter ·
141 ledger-guard-benign-lag-vs-drift · 142 ledger-guard-exempt-reconciliation-prs ·
143 ledger-window-scale-to-marker · 155 no-dead-end-terminal-view-guard ·
163 permission-overlap-guard · 166 plan-homing-guard ·
173 public-data-contract-field-snapshot · 190 recently-shipped-auto-trim-helper ·
201 reconcile-trigger-band-consistency-guard · 206 repo-manageability ·
208 review-unit-tagging · 239 supersede-banner-integrity-checker
(all `-2026-07-10.md` files).

Post-fix run: `check_ideas: OK — 301 idea files conform to the README grammar
(3 warning(s), advisory)` — the 3 are the known deliberate SIM-VERDICT legacy
advisories, unchanged. Outbox mode unaffected (`check_ideas --outbox` OK, part
of the preflight below).

## Smoke tests (planted violations — fired, plants removed)

Temp tree via `--ideas-dir` (the PR #149 smoke-3 seam), three bullets in one
planted `ideas/testsec/README.md` — verbatim key output:

```
warn: STATE-ECHO ideas/testsec/README.md:3: entry echoes bare 'parked' but the linked bare-echo-drift-2026-07-11.md is 'parked(routed — smoke)' — echo the reason (abbreviated is fine)
warn: STATE-ECHO ideas/testsec/README.md:5: entry echoes state 'captured' but the linked family-drift-2026-07-11.md is 'parked(overtaken — smoke)' — re-badge the index line
check_ideas: OK — 3 idea files conform to the README grammar (3 warning(s), advisory)
exit=0
```

— line 3 = the NEW leg fires on the exact #161 class (bare `parked` vs
`parked(routed — smoke)`); line 4 (an abbreviated `parked(routed)` echo of a
longer reason) correctly SILENT; line 5 = the existing family leg regression
intact; exit 0 = advisory held. In-tree plant (one fixed bullet flipped back to
bare `historical`, then reverted byte-exact the same run):

```
warn: STATE-ECHO ideas/superbot/README.md:35: entry echoes bare 'historical' but the linked automod-spam-detection-gaps-2026-07-10.md is 'historical(shipped in superbot same day, 2026-07-07)' — echo the reason (abbreviated is fine)
```

Post-revert run: back to exactly the 3 legacy advisories, exit 0.

## Close-out

**Evidence (verified, this tree):** full `python3 scripts/preflight.py` — ALL
TEN checks PASS — and `python3 bootstrap.py check --strict` exit 0, run
immediately before push after the heartbeat overwrite (verbatim tails on the
final tree in the session transcript). Ceremony held: `bootstrap.py reflect
--mine` ran at wake (R-0042 mined); inbox read FIRST at origin/main HEAD
00002cd and re-read at c3682dd post-claim (ORDER 001 standing rule satisfied by
this card's 📊 Model line; ORDER 002 done by #158 — no new orders, nothing
re-claimed); claim landed on main BEFORE build (PR #162); claims dir re-read at
HEAD post-merge; claim file deleted in this close-out.

**Judgment:**

- Decisions made: EXTEND over duplicate (the overlap verdict); reason-PRESENCE
  only, never reason-DETAIL (Q4 held); advisory severity (no filename date to
  gate on — the #149 reasoning held, stricter hard-gating declined); 41
  exact-echo fixes taken as mechanical (three independent convention witnesses,
  above) rather than exempting the `historical` family — an exemption would
  have encoded the drifted form as a convention.
- Next session should know: guard recipe — the leg lives in
  `check_state_echoes()` + the `STATE_ECHO_RE` optional `(\()` group in
  `scripts/check_ideas.py` (the `# Cross-link state-echo constants` loud
  co-edit block); test = the temp-tree smoke on this card.

## 💡 Session idea

The 41-hit yield is a WRITER bug surfacing as reader-side lint: the harvest
index writer minted bare `historical` uniformly while every hand-written
section echoed reasons — the checker now catches the rot after commit, but the
next 237-doc harvest or `--emit-entries` pass can re-plant it wholesale. Cheap
seed: the harvest/emit path that mints index bullets should echo the linked
file's exact state line at write time (co-edit anchors: `check_harvest.py`
emit/re-badge path, the mirroring sentence at `ideas/superbot/README.md:18`) —
then the lint leg only ever fires on true post-write advances, and
advisory-fatigue risk (lint-bundle Q4) stays near zero.

## ⟲ Previous-session review

PR #161 (`.sessions/2026-07-11-groom-superbot-supersession-rebadge.md`, squash
`00002cd`, the newest card at this wake) holds up on this tree: its 3 parked
index-echo re-badges are live in `ideas/superbot/README.md` (rebuild-websites-
cutover-role · competitive-teardown · wire-level-live-bot-loop — this slice's
live run found ZERO parked-class hits, confirming its sweep was complete for
that family), the #158 Self-review section and the standing ⚑ survived verbatim
on the heartbeat, and its claim is gone at HEAD. Its number-less
`last-shipped: this slice` is stamped #161 by THIS slice's heartbeat overwrite
(the #72/#79 precedent). Adopted from it directly: its 💡 IS this slice — and
its "exact echo" / "abbreviated echo per the #160 line-59 precedent" wording
became the new leg's agreement semantics verbatim. One extension beyond its
scope, flagged honestly: it verified the self-historical pair as "historical
both sides, leave alone" under FAMILY eyes; this slice's reason-presence eyes
re-classified bare `historical` as the same rot class (three convention
witnesses on the card) and re-badged all 41, the pair included.

## Outcomes

Verdict: the lint-bundle idea's head 2 extended in place —
`ideas/fleet/lint-bundle-2026-07-11.md` state stays `park(built-here — …)`
(extension notes never advance state, the probe-report-lint lineage). Landed
per README § Landing conventions (PR READY; `build/*` matches the enabler's
patterns — auto-merge arms once this card flips complete; REST merge-on-green
as fallback). Claim file deleted in this close-out commit.

## Handoff → next wake

- The reason-presence leg is live in preflight from this merge (CHECKS entry 2
  — no wiring change). Index bullets whose linked file carries a reasoned
  state must echo SOME parenthetical; bare echoes only for bare states
  (captured/probed/sim-ready).
- The 💡 above (writer-side exact-state echo at harvest/emit time) is the
  natural next lint-adjacent slice — reader-side is now covered, writer-side
  re-plant is the remaining hole.
- Standing ripest unchanged from the #161 heartbeat: websites re-harvest queue
  (moved HEAD + CHANGED backlog + one ACK-pending state-drift line, sized by
  the #149 card) and the manager sweep flags on the heartbeat notes line.
