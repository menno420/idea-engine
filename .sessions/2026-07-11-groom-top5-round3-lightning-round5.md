# Session — groom: third standing TOP-5 minted + the queued 💡 one-liners encoded (round 5) + VERDICT 010 fan-in

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-11 ~17:45Z (worker slice, coordinator-dispatched)

## Scope

The #192 handoff's named ripest slice: the second standing TOP-5 was fully
consumed, so this slice (a) verified the consumption ledger and minted the
THIRD standing TOP-5, and (b) folded the queued grooming 💡 one-liners into
the contract docs (grooming round 5; style per rounds 2/3/4 = PRs #21/#50/#59
— minimal in-place amendments, existing voice, one encoding each). No claim:
root contract docs are not a section (PR #21 precedent); no section index or
idea-file STATE was touched (the one idea-file change is a grammar-blessed
`## Sim verdict` note append — see below). Branch
`groom/top5-round3-lightning-round5`.

## Verify-first (the work record)

- **Inbox FIRST** at wake, origin/main HEAD `889ccf3`: still exactly ORDER
  001 (standing per-session rule — re-satisfied by this card's 📊 Model line)
  + ORDER 002 (done by #158, Self-review preserved verbatim on the
  heartbeat). No new orders; nothing in the inbox changes this slice.
- **Second TOP-5 consumption VERIFIED from the five idea files** (not the
  summary — which was slightly off: the briefed "1 historical-at-target, 1
  historical, 3 parked/routed" is actually **2 historical, 1 sim-ready, 2
  parked(routed)**): 1) rebuild-layout-success-simulator →
  `historical(built at superbot-next — D-0020 …)` (#180); 2)
  karma-reputation-system → `historical(built at superbot 2026-06-22 … ported
  at superbot-next D-0037)` (#183); 3) settle-once-architecture-guard →
  `sim-ready` + PROPOSAL 009 (#186); 4) audited-score-subsystem-scaffold →
  `parked(routed — …)` (#189); 5) wager-flow-map → `parked(routed — …)`
  (#192). All five states read from the files this session.
- **PROPOSAL 009 is no longer awaiting intake — VERDICT 010 landed
  mid-window and this slice fanned it in.** sim-lab @ live HEAD
  `87ca0dfb562cb00a3da390c1c155d244fb4bb9b8` (status 17:15:57Z): INTAKE 009
  pulled (triage PR #35 `41b26b5`), **VERDICT 010 · approve** finalized
  (verdict PR #36 `e559a37`) — recommendation: adopt contract (c),
  catch-matrix 6/6; headline negative: (b) row-consumption alone = 1/6,
  already breached by superbot-next #133. Recorded per the README grammar as
  `## Sim verdict (2026-07-11)` on
  `ideas/superbot/settle-once-architecture-guard-2026-07-10.md` (numbering
  cross VERDICT 010 = PROPOSAL 009; `recommendation:` quoted — no `ruling:`
  field, the #178 parse rule applied on its own encoding day). State line
  stays `sim-ready`, untouched, per grammar. The heartbeat's awaiting-intake
  line is RETIRED as consumed; post-verdict routing is the manager's
  (Q-0264).
- **Expiry sweep before ranking**: ZERO captured heads across
  `ideas/superbot/` (175) + `ideas/websites/` (4) + `ideas/fleet/` (0) carry
  a `Sequence:` line — no near-term expiry to rank up (exactly the gap the
  #174 💡, encoded this slice, closes at future harvests).
- **Mint-time ledger check (the #180 💡 applied the day it was encoded)**:
  superbot-next `docs/decisions.md` fetched at live N=`870a16c` and grepped
  for every rebuild-targeted candidate's nouns before ranking. It priced one
  head OUT: rebuild-schema-growth-ledger is BUILT at N (D-0005: "A-2
  schema-growth ledger … + check_schema_growth") — excluded from the TOP-5,
  flagged verify-and-flip. It also demoted two: navigation-completeness
  (A-3 navigation golden landed inside D-0020 — which half remains needs
  pricing first) and amendment-registry (D-0005 S0 re-hosted
  rebuild-amendments.yml + check_amendments.py, rules 1-3 local).

## The third standing TOP-5 (installed on the heartbeat)

Q-0259 weighting (games completion wave + rebuild pace first); one-line
why-now each, full text in `control/status.md` notes:

1. `ideas/superbot/golden-recapture-on-bugfix-2026-07-10.md` — parity flips
   live NOW (D-0019/D-0028; band rows pending D-0050/D-0062), zero recapture
   protocol at N: every live-bot bugfix in the flip window can bake a bug
   into a golden.
2. `ideas/superbot/rebuild-release-testing-loop-2026-07-10.md` — built half:
   test-mode root (D-0049, live-boot 07-09); open half: the in-server
   announce/coverage/approve loop — the bottleneck as Band 7 closes (D-0048)
   and CUT-1 composes. (#189 name-which-half applied at mint.)
3. `ideas/superbot/rebuild-critical-review-checkers-2026-07-10.md` — rubric
   grew classes 11/12/13 with live mechanics (D-0014, ratified D-0033) while
   review enforcement stays manual; checkable classes accumulate at band
   pace.
4. `ideas/superbot/rebuild-design-cite-checker-2026-07-10.md` — zero cite
   validation at N; the fabricated-cite class is documented and the rebuild
   still mints band-pace design docs it can poison.
5. `ideas/superbot/leaderboard-row-avatars-2026-07-10.md` — the games
   completion wave's cheapest visible live-bot win: the Arcane-defining
   per-row avatar visual; every needed piece already exists per the
   canonical doc.

## 💡 encodings — the round-5 map (each → encoded where, or skipped why)

- **#174 Sequence-at-harvest** → ENCODED: README § Idea file grammar,
  Sequence paragraph (stamp at capture time when the source names a hard
  date/event).
- **#178 fan-in parse rule** → ENCODED: README § Idea file grammar,
  Sim-verdict paragraph (quote `ruling:` when present, else
  `recommendation:`) — and APPLIED by this slice's own V010 fan-in.
- **#180 target-lane ledger-check** → ENCODED: README § The probe battery,
  new cross-lane/tree-aware verify-first paragraph — and APPLIED by this
  slice's own mint (it priced schema-growth-ledger out).
- **#183 folio/tree-beats-current-state** → ENCODED: same paragraph
  (absence from current-state.md is not evidence of absence).
- **#186 invocation-wiring** → ENCODED: same paragraph (body-exists is not
  body-wired; read the registration site) — cited with V010's live
  confirmation of the Rule 6 drift.
- **#189 name-which-half** → ENCODED: README § Idea file grammar, badge
  duties (built half + open half, one clause each).
- **#192 trigger-in-the-badge** → ENCODED: same badge-duties sentence
  (carry the canonical text's named trigger into the index badge).
- **#144 standing-order claim grammar** → ENCODED: control/README §
  Claiming an order (a STANDING order's per-wake execution needs no fresh
  claim once its id lives in `done=`); the checker-side carve-out stays
  kit-side, routed via the kit-lane fan-in bundle. NOTE: control/README.md
  is kit-planted — regen-clobber duty applies at the next upgrade, same as
  the round-4 § status.md-format sentence.
- Carried-but-skipped (unchanged from the #144 card's ledger, restated per
  the README § Coordination tracker-reconciliation rule): (a) manifest-row
  Grounding-suffix re-grounding — needs roster verification, not a
  one-liner; (b) park-time-rulings-blackout rider — substrate-kit lane's
  template, rides the kit-lane bundle; (c) the lint-bundle heads (#22 #29
  #33 #36 #59) — build slices, not grooming.

## Verification

Full `python3 scripts/preflight.py` (all 10 checks) + `python3 bootstrap.py
check --strict` green on the final tree immediately before push, run AFTER
the heartbeat overwrite (heartbeat-last rule). PR number stamped post-open
per the never-guess rule, BEFORE arming auto-merge (branch final at arm —
the #86 arm-race guard honored without exiling the stamp).

**📊 Model:** fable-5 · groom slice (7 contract one-liners across 2 root
docs + 1 grammar-blessed verdict-note append + TOP-5 mint on the heartbeat +
card; no code, no outbox append, no state flips, no lane-file writes, Q-0260)

## 💡 Session idea

**A verdict's landing should un-gate its dependents mechanically, not by
re-read.** This slice found VERDICT 010 already finalized only because it
re-checked sim-lab's live status while drafting a "still awaiting intake"
line — the heartbeat's own preserve-list was about to carry a freshly false
fact forward. Grooming seed: any heartbeat line of the shape "awaiting X
from lane Y" should carry the one-command check that retires it (e.g. `curl
raw .../control/status.md | grep 'VERDICT'`), so every wake's preserve-pass
re-verifies instead of re-copies — the preserve-list is the one surface
where verbatim carriage is the failure mode, not the discipline.

## ⟲ Previous-session review

Newest prior card: `.sessions/2026-07-11-probe-wager-flow-map.md` (status
`complete`; shipped #192 `8bababf` + heartbeat stamp #193 `889ccf3`, claim
rode #191 `719cc7f`). Spot-checked against the tree at `889ccf3`: its probe
report exists as promised (wager-flow-map idea file — state
`parked(routed — …)`, `> **Sequence:**` line present, one
`**Recommendation: park**`); its claim file is gone from `control/claims/`
(only README present); the heartbeat carries TOP-5 item 5 = parked(routed)
+ the NEW map-before-faucets sweep flag + all preserved blocks. Its handoff
named this exact slice (groom/re-rank + the six queued 💡s) as ripest —
dispatch matched. One correction made with evidence, not carried: its
"PROPOSAL 009 pending, sim-lab has not intaken" was TRUE at its pins
(sim-lab 15:16:50Z) but expired mid-window — VERDICT 010 finalized
17:15:57Z; this slice's fan-in retires it. Its 💡 (trigger-in-the-badge)
is encoded this slice, closing the six-card 💡 queue it enumerated.

## Handoff → next wake

Inbox first, as always. The THIRD standing TOP-5 is live on the heartbeat —
ripest next work: **probe item 1, golden-recapture-on-bugfix** (apply the
newly-encoded verify-first paragraph: N ledger grep is already done, recheck
at probe-time HEAD). Cheapest micro-slice available first:
**verify-and-flip rebuild-schema-growth-ledger** (built at N per D-0005 —
a 5-minute probe append + state flip + badge re-badge earns a consumed head
for almost nothing). VERDICT 010 is fanned in; the checker ORDER it routes
to superbot-next strengthens the effect-arming third-dependent flag (the
compensator checklist should land BEFORE that lane's arming slice — flag
carried on the heartbeat). The 💡 queue is EMPTY — all eight encoded or
routed; the card-💡 chain restarts with this card's preserve-pass
re-verification seed. Standing watches otherwise unchanged (theme-schema
half-fired; superbot-idle V006 guardrails; #161 adoption-record sweep; #174
contract-shape attach flag; map-before-faucets + RankProvider + Rule 6
manager flags — Rule 6 now sim-confirmed with its catch-matrix delta).
