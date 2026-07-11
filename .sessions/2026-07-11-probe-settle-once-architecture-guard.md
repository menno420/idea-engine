# Session — probe: settle-once-architecture-guard (TOP-5 item 3) — verdict sim-ready, PROPOSAL 009 earned

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-11 ~16:40Z (worker slice, coordinator-dispatched)

## Scope

The handoff's named ripest work: probe standing TOP-5 item 3,
`ideas/superbot/settle-once-architecture-guard-2026-07-10.md`, applying BOTH
queued verify-first 💡s first (the #180 D-# ledger grep at superbot-next AND
the #183 folio/tree check at superbot — settle/settlement nouns). Claim landed
first via fast-lane PR #185 (claim file
`control/claims/probe-settle-once-architecture-guard.md`, branch
`probe/settle-once-architecture-guard-claim` per the workprefix+`-claim`
convention; merged by the live auto-merge enabler in 26s, re-read at HEAD
`b2b855b` post-merge — sole claim in the dir — then DELETED at this
close-out). Work shipped on branch `probe/settle-once-architecture-guard`
(PR number stamped post-open per the never-guess rule / #181 recipe).

## What this session did

- **Inbox FIRST**: read at origin/main HEAD `5e8ca13` at wake, re-verified at
  `b2b855b` post-claim — still exactly ORDER 001 (standing per-session rule,
  re-satisfied by this card's 📊 Model line) + ORDER 002 (done by #158, its
  Self-review section preserved verbatim on the heartbeat). No new orders.
- **Probe shipped — the first TOP-5 head that did NOT flip built-at-target,
  and the first PROPOSAL since 008.** Verify-first at live pins S=`8214200`,
  N=`14e5037` (ls-remote 16:20:34Z), reads via raw + blobless clones:
  - **Money leg LIVE at S and wider than briefed**: Rule 6
    `settle_once_adoption` (`scripts/check_consistency.py`, added `fb0c701`
    2026-06-25 promoting this very idea) gained two sinks
    (`payout_tournament`, `update_leaderboard`) via `afec1f1` / PR #1781
    (2026-07-07) after the Gate-V Arm-D live double-write. Still
    **warn-only** (registry `severity="warning"`, :1150) — a finding never
    reds CI (`code-quality.yml:207` strict mode fails on `error` only).
  - **DRIFT FOUND**: the #1781 widening's cogs/-scope half is silently
    INERT — the rule function's default roots + docstring claim `cogs/` in
    scope, but the RULES registry passes `roots=("views/", "services/")`
    (:1151) and `main()` invokes `rule.fn(files, exceptions, rule.roots)`
    (:1185). Latent (the deathmatch `_DuelView` adopts the mixin today,
    `disbot/cogs/deathmatch_cog.py:100/162/243`), but a NEW unguarded
    cogs-layer settle site — the exact Gate-V shape — would ship unscanned.
    Same silent-no-op class as this repo's branch_patterns lesson (PR #55).
  - **No guard at N, where the class last recurred**: `tools/` holds 22
    `check_*` checkers, none settlement-shaped; the discipline is D-0042
    (once() fence + FOR-UPDATE row-consumption) — and superbot-next PR #133
    breached it exactly where no consumable row exists (the
    blackjack-tournament consolation double-payout; fix = check-and-set on
    the atomic row-deletion count, retrofit onto `rps.tournament_payout`;
    quoted at ideas/superbot-next/effect-arming-compensator-checklist-2026-07-10.md:58-61).
    Superbot's own Rule 6 comment names the identical hole class
    (`payout_tournament`'s free-reward leg, check_consistency.py:887-889).
  - **Count correction, evidence-first**: SIX documented instances, not the
    briefed five — BUG-0013 + the three 2026-06-24 sites (#1444/#1445) +
    Gate-V Arm-D (2026-07-06, fixed by #1781) + N #133 (the first recurrence
    IN THE REBUILD).
- **Verdict: sim-ready** — the remainder is a guard-DESIGN fork on a
  money-safety class: S and N answered the same class two different ways
  (caller-side static claim vs row-consumption), each with a documented
  breach or documented false-positive fear, and six reconstructable
  instances exist to measure candidate contracts against. Runtime
  reconciliation cannot see the class (a double-settle writes balance AND
  ledger consistently on both legs — flagged as derivation, not measured).
  **PROPOSAL 009 appended** (outbox tail was 008): the catch-matrix +
  false-positive-count question, three candidate contracts, verdict =
  build spec for a superbot-next `tools/check_*` checker ORDER (warn-first,
  the lane's own Q-0105 posture). Honesty check passed the other way this
  time: the question is genuinely sim-shaped (reproduced-evidence
  measurable), not queue-feeding.
- **State advanced** captured → `sim-ready`; index bullet re-badged with the
  probe summary; forward-only (probe appended, nothing rewritten).
- **current-state staleness re-confirmed (milder form, #161 datapoint)**:
  `docs/current-state.md` at S records the 2026-06-25 money leg (#1454, S3
  sector row) but neither the 2026-07-07 #1781 widening nor the Gate-V
  Arm-D recurrence that forced it; its in-flight section still ends at the
  2026-07-07 program-launch era. Truth lived in the code tree + git log +
  both ledgers — folio/tree/ledger beats current-state grep, again.
- **Heartbeat overwritten LAST**: TOP-5 item 3 marked PROBED→sim-ready with
  PROPOSAL 009; new sweep flag for the Rule 6 registry-roots drift
  (canonical-side one-line fix, superbot's own per Q-0260); all preserved
  blocks carried verbatim (the FOUR-decision ≤07-14 ⚑ sitting bundle, the
  ORDER 002 Self-review section, the standing manager sweep flags).
- Claim file deleted at close-out; guard-fires residue rides this PR per
  precedent (#180/#183 carried the same class).

**📊 Model:** fable-5 · probe slice (one idea-file append + state flip +
index re-badge + outbox PROPOSAL 009 append + card + heartbeat + claim
clear; no product code, no lane-file writes, Q-0260)

## 💡 Session idea

**Body-exists is not body-wired — verify the INVOCATION, not just the rule.**
The Rule 6 cogs/ widening looked shipped from every prose surface (docstring,
sinks, session-card noun greps) and was still inert at the registry — the
`roots=` argument at the call site overrides the widened function default,
so the exact layer the widening was bought for (Gate-V's cogs/ recurrence)
is unscanned. Grooming seed for the verify-first line: when confirming "a
guard/checker exists at target," read the REGISTRATION/invocation site
(registry entry, config key, CI wiring) and confirm the widened parameter
actually flows — the branch_patterns lesson (PR #55) generalized from config
to code. Anchors: check_consistency.py `RULES` registry vs
`rule_settle_once_adoption` defaults; `rule.fn(files, exceptions, rule.roots)`.

## ⟲ Previous-session review

Newest prior card: `.sessions/2026-07-11-probe-karma-reputation-system.md`
(status `complete`; shipped #183, its heartbeat stamp exiled to #184 by the
arm-at-open merge — the #181 recipe, followed again by this slice).
Spot-checked against the tree at `b2b855b`: its probe report exists as
promised (karma idea file — 3 Grounding pins, 8 questions,
`**Recommendation: park**` closing the report, state `historical(built at
superbot …)`); its index re-badge with the state-drift annotation is live;
its claim file is gone from `control/claims/`; NO PROPOSAL from it, exactly
as its card states (outbox tail was 008 at wake). BOTH its queued 💡s were
applied as this slice's first verify steps and BOTH fired: the ledger grep
surfaced D-0042/D-0045 (discipline, no guard decision) and the folio/tree
check surfaced the Rule 6 body + `terminal_guard.py` + four settle-once test
files in one ls-tree — and pulling the invocation thread found the registry
drift its own card's lesson class predicted. Also verified from the
wire-automerge-enabler card (#55): its live-fire promise holds — this
slice's claim PR self-armed and merged in 26s by github-actions, no hand
arming. No reconciliation debt handed to this slice.

## Handoff → next wake

Inbox first, as always. Standing TOP-5: items 1–2 historical, **item 3 now
sim-ready with PROPOSAL 009 pending sim-lab pull** — record the verdict via
the `## Sim verdict` note grammar when it lands (numbering cross: sim-lab
numbers by intake order, likely VERDICT 009 ≠ guaranteed). Ripest next work:
item 4 (audited-score-subsystem-scaffold, #1346) — its re-priced live
question is scaffold value for the NEXT score subsystem; verify that premise
at both trees first (apply this card's 💡: check invocation/registration
sites, not just body greps). Item 5 (wager-flow-map) gains urgency evidence
from this probe: the coin paths it would trace are exactly where the
six-instance corpus lives. NEW manager-sweep item this slice: the Rule 6
registry-roots drift at S (one-line fix, canonical-side, Q-0260 — flagged on
the heartbeat). Standing watches unchanged (theme-schema half-fired;
superbot-idle V006 guardrails; #161 adoption-record sweep — now with this
slice's current-state datapoint; #174 contract-shape attach flag;
effect-arming second-dependent note; check_sim_gate VALUE-drift note). Four
queued 💡s now: the README fan-in parse-rule line (#178), the target-lane
ledger-check line (#180), the folio/tree-beats-current-state line (#183),
and this card's invocation-wiring line — all one-liners, foldable into any
control-touching slice.
