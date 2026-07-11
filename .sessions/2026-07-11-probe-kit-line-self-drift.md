# Session — single-pass probe: substrate-kit kit-line-self-drift-local-check

> **Status:** `in-progress`
> **Model/time:** fable-5 · 2026-07-11 (worker slice, dispatched by the coordinator
> under continuous-chaining mode per Q-0265)

## What this session did

Single-pass probe (battery v0, no panel triggers — not contested, no
irreversible surface; a routing decision over a docs-only diff) of
`ideas/substrate-kit/kit-line-self-drift-local-check-2026-07-10.md` — the
section's LAST unprobed head (captured in PR #19 off the fleet scanner's first
run; the other four substrate-kit heads stay `captured`, section NOT complete).

**Verify-first finding (expiry-aware — the capture was one day old and a
release wave landed overnight):** the class is not moot, it REGENERATED.
Upstream shipped v1.9.0 TODAY (`CHANGELOG.md` @ kit HEAD `7122aca`, ls-remote
06:24:11Z: `## [1.9.0] - 2026-07-11`, the model-attribution retrofit band) and
ran a fresh fleet scan at 2026-07-11T05:33:10Z (`docs/adopters.md` @ `7122aca`,
fetched 06:24:27Z): 10 rows, 6 DRIFT rows carrying 7 drift-report lines, of
which FIVE repos are again the exact self-report-lag class — websites v1.8.0,
gba-homebrew v1.8.0, superbot-games v1.7.1 (both lane heartbeats),
trading-strategy v1.7.1, fleet-manager v1.7.0, all claimed over v1.9.0 trees.
vs the capture's scan (@`7e600c6`, 20:36:19Z yesterday): only superbot-next
flipped clean; trading-strategy JOINED. Live HEAD spot-checks this session
(raw fetches 06:25:03–06:25:11Z: websites `7da9fbf` · gba-homebrew `31c8672` ·
fleet-manager `6dedff6`) confirm dist header 1.9.0 + config pin 1.9.0 +
heartbeat `kit:` v1.8.0/v1.8.0/v1.7.0 — DRIFT at HEAD right now, not a
stale-scan artifact. And NO local check exists: vendored v1.8.0 `bootstrap.py`
(`cmd_check` line 12364) and the upstream v1.9.0 dist (`cmd_check` line 12909)
run the same checker list with no version-consistency checker;
`_check_one_status` (line 2287) never parses the `kit:` version; zero
`self-drift`/`check_kit_version` symbols in either dist.

Verdict: **parked(routed — substrate-kit lane build)**. The check belongs in
the kit's own `cmd_check` — a zero-network `check --strict` finding (advisory
first wave, strict next) comparing the repo's three committed version
artifacts across all declared `heartbeat_files`, plus `upgrade` printing the
paste-ready line via the existing, currently call-site-less
`kit_line_example()` (dist line 752). Near-composition of already-vendored
v1.8.0+ pieces: `parse_kit_line`/`KIT_LINE_RE` (grammar, writer↔enforcer
pinned by kit tests) + `KIT_VERSION` + the config-pin loader +
`config.heartbeat_files`; `RepoCurrency.drifts()` (line 10751) is already the
pure three-artifact comparison. Advisory-first because consumer #0 is born-red:
the kit's OWN row is tree-internal DRIFT (config pin 1.0.0 vs dist 1.9.0, both
scans). No sim-lab proposal — a contract check is proven by its own red/green;
no simulator question.

Files touched: the idea file (probe report append + state flip forward
captured→parked(routed)), `ideas/substrate-kit/README.md` (index bullet — this
head only; the other four stay captured), this card, `control/status.md`
(heartbeat; ⚑ OWNER-ACTION Lumen Drift block and notes tail preserved
byte-for-byte), claim `control/claims/probe-substrate-kit-kit-line-self-drift.md`
deleted per convention.

Claim: fast-laned first as PR #112 (control-only, merged 06:14:59Z), branch
recreated fresh from origin/main after the squash-merge, claims dir re-read at
HEAD `c2d22cf` (only the superbot-idle sibling's disjoint claim live), claim
file deleted in this PR.

**📊 Model:** fable-5 · docs-only (one probe append + state flip + index flip +
heartbeat + card + claim clear; no code)

## 💡 Session idea

A drift class that a scanner measures and a doc contract forbids will regrow on
every release wave until the check runs at the surface that COMMITS the drift —
here, the adopter's own gate on the upgrade PR itself. The general pattern: when
N committed artifacts must agree, the consistency check belongs in the tool that
writes any one of them (and it should print the paste-ready fix), not in a
cross-repo auditor that reads them later; the auditor's job is then anomalies,
not the steady-state class.

## ⟲ Previous-session review

PR #108 (`fix/stop-hook-telemetry-exemption`, the stop-hook telemetry-loop
exemption): verified against the tree — patcher `scripts/patch-stop-hook-git-check.sh`
+ `.claude/settings.json` SessionStart wiring live, idea file
park(built-here), both README touches present, card `complete` with the Model
line, claim cleared. Its prediction held: this session accrued NO telemetry
nag (the exemption's first probe-slice beneficiary). Adopted from it: prove
claims with verbatim command output on the card, and flip the card complete
before the final push so the #86 enabler guard arms on the card-flip
synchronize. Its handoff's "expect telemetry PRs to STOP" is confirmed two
sessions on (#109 was the deliberate flush, not a treadmill entry).

## Handoff → next wake

- substrate-kit section: 1/5 probed (this head); the other four
  (`parallel-session-heartbeat-reconcile`, `behind-stall-auto-updater`,
  `host-checkers-one-gate`, `enabler-card-status-guard-upstream`) remain
  captured — NOT section-complete.
- KIT v1.9.0 RELEASED UPSTREAM: this repo still runs v1.8.0 with all three
  artifacts in sync — an upgrade slice is a natural next head (and, per this
  probe, the exact moment the routed check would first pay off here).
- The routing fact rides the heartbeat notes for the manager's :30 sweep; the
  superbot-idle theme-heads sibling claim was live at dispatch — expect its PR
  in flight.
