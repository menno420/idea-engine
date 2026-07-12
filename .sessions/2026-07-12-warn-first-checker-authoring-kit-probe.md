# Session — single-pass probe: superbot warn-first-checker-authoring-kit

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-12 (worker slice, dispatched by the coordinator
> under continuous-chaining mode per Q-0265)

## What this session did

Single-pass probe (battery v0, no panel triggers) of
`ideas/superbot/warn-first-checker-authoring-kit-2026-07-10.md` — TOP-5 #3 on the
fourth ledger (`control/status.md` @ `42f9642`): extract the shared scaffold +
AST/reachability lib so the third warn-first checker doesn't re-duplicate the
plumbing the first two (superbot #1747/#1748) copy-pasted.

Verify-first, live: S = superbot HEAD `1ecc211`, N = superbot-next HEAD
`9b80444` (both `git ls-remote`-resolved; blobless-clone tree scans + raw reads
at the pinned SHAs; canonical doc md5-identical at S HEAD vs the `fd638e3`
harvest pin). The decisive finding: the ledger's fired "third checker" trigger
is a **letter-not-substance fire** — both pending routings are real and still
pending (S `check_plan_staleness.py` unchanged at 127 lines/3 rules, S inbox =
ORDERs 001+002 only, both done; N `parity/parity.yml` has no `recapture:`
section, N inbox = ORDERs 001–013, none recapture) but NEITHER is an AST guard:
#211 adds a regex rule to an existing S text checker (mints nothing), #197's
seat is a yml row-shape validator copying N's own 23-exemplar red-gating fleet
pattern. The kit's actual beneficiary family — S's 4 warn-first AST guards
(audit_seam / deferred_recovery / command_reachability /
settings_reachability, plumbing stem-hits 33/10/21/24) — has no queued fifth
member (rubric backlog consumed/carrier-less per the #211 probe), and both
fleets just grew their newest checker without a kit at ~1-file cost (N
`check_money_race` @ `71af879` between the sibling probe's pin and HEAD).

Verdict: **parked(trigger-misfire — corrected)**, re-arm trigger carried into
the state line and index badge: a NEW AST-shaped guard queued at S, or N's
5-member AST subfamily minting a member that re-implements call-graph/receiver
plumbing. Best implementation if re-armed: lib-only at S
`scripts/lib/astguard.py`, `check_audit_seam.py` as donor, the four existing
ratchet test files as the behavior hold. No sim question (judgment-only —
authoring-time payoff on a family with no queued next member).

Dedup swept: `audit-seam-coverage-checker` + `deferred-action-restart-recovery-checker`
(both historical — the kit's members 1 and 2, no overlap consumed);
`audited-score-subsystem-scaffold` (parked — the `new_subsystem.py` scaffold
precedent, adjacent pattern not duplicate); `ideas/fleet/lint-bundle-2026-07-11.md`
(park built-here — counter-evidence datapoint, cited in Q4);
`substrate-kit/host-checkers-one-gate` (different layer, no overlap). No
duplicate idea file.

**Section-collision flag (dispatch boundary — no claim file):** this slice is
barred from `control/`, so no `control/claims/` entry exists; this card's
born-red first commit carried the `ideas/superbot/` collision flag per the PR
#222/#225/#226/#228 workflow convention.

## Close-out

**Evidence:**

- ideas touched (2): `ideas/superbot/warn-first-checker-authoring-kit-2026-07-10.md`
  (state flip captured→parked(trigger-misfire — …) + probe report v0 append),
  `ideas/superbot/README.md` (index bullet re-badge with the re-arm trigger,
  PR #192 card convention)
- sessions touched (1): `.sessions/2026-07-12-warn-first-checker-authoring-kit-probe.md`
- code touched: none · control touched: none (dispatch boundary; READ-ONLY read
  of `control/status.md` @ `42f9642` for the ledger entry)
- git: branch `probe/warn-first-checker-authoring-kit` off main `3eefb13`,
  born-red card first commit `a3a2a9a`, probe+close-out commit follows; draft
  PR #230 flipped ready on green per dispatch instructions.
- verify: `python3 bootstrap.py check --strict` and `python3 scripts/preflight.py`
  run before push (results in the PR).

**Judgment (the half only the session knows):**

- Decisions made: no D-entry — probe verdict only (park, trigger-misfire,
  re-arm trigger named). One evidence-over-claim call, declared: the fourth
  ledger prices this head as "probe before both re-duplicate plumbing"; the
  live scan showed neither pending routing CAN re-duplicate the kit's plumbing
  (both non-AST), so the park corrects the mint-time claim rather than riding
  it — the trigger grammar fired on "checker" where the kit's premise needs
  "AST guard".
- Next session should know: the re-arm check is one grep per repo — at S, any
  NEW `scripts/check_*.py` that imports `ast` (family today: audit_seam,
  deferred_recovery, command_reachability, settings_reachability); at N, any
  new `tools/check_*.py` importing `ast` that defines call-graph/receiver
  helpers (subfamily today: egress, money_race, config_usage, no_skip,
  symbol_shadowing — only `check_egress.py:55 _receiver_name` overlaps S's
  plumbing today). If either fires, the kit re-prices lib-first at S
  `scripts/lib/` per the probe Q8.

## 💡 Session idea

A trigger badge that keys on an artifact CLASS ("mints a checker") instead of
the idea's load-bearing MECHANISM ("re-duplicates the AST plumbing") will
eventually fire on a class-match/mechanism-miss — this probe is the datapoint.
The cheap fix at mint time: when a TOP-5 trigger names "the Nth X", spell X as
the mechanism the idea de-duplicates, not the artifact family — one clause
("third AST-walking guard", not "third checker") would have re-priced this head
before it earned a slot.

## ⟲ Previous-session review

PR #228 (pil-card-render-contract-guard probe): adopted wholesale — (a) its
live-HEAD-first discipline paid again here (N moved `81b04bc`→`9b80444` since
the sibling pin; the one-file tools/ diff IS the probe's counter-evidence); (b)
the born-red-card collision flag under the dispatch boundary used verbatim; (c)
its "cheapest-carrier, not precondition" honesty pattern echoed as this probe's
"letter-not-substance" trigger correction. Workflow improvement carried: its
card was hand-written from the first commit; this card had to overwrite a
stop-hook auto-draft whose evidence block diffed against the wrong base
(cce4aae, listing 340 untouched files) — auto-draft evidence needs the branch
fork point, not the session's first HEAD.

- **📊 Model:** fable-5 · single-pass battery (no panel triggers) · docs-only
  probe slice (one probe append + state flip + index re-badge + card; no code)

## Handoff → next wake

This consumes TOP-5 #3 of the fourth mint (coordinator-side heartbeat edit —
NOT done here, control/ is coordinator-only). Correction worth carrying to the
heartbeat: the fourth ledger's slot-3 trigger claim should be recorded as
misfired-in-substance (both #197/#211 routings pending AND non-AST at S
`1ecc211` / N `9b80444`). The #197/#211 routings themselves remain
manager-sweep flags (already carried from `fc0bab6`) — unaffected by this park.
Re-arm recipe in this card's "Next session should know".
