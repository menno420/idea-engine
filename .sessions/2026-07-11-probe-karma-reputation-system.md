# Session — probe: karma-reputation-system (TOP-5 item 2) — verify-first flips it to built-at-target

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-11 ~16:05Z (worker slice, coordinator-dispatched)

## Scope

The handoff's named ripest work: probe standing TOP-5 item 2,
`ideas/superbot/karma-reputation-system-2026-07-10.md`, applying the #180
card's 💡 first (target-lane decision-ledger grep for karma nouns BEFORE
trusting the capture). Claim landed first via fast-lane PR #182 (claim file
`control/claims/probe-karma-reputation-system.md`, branch
`probe/karma-reputation-system-claim` per the workprefix+`-claim` convention;
claim re-read at HEAD post-merge — sole claim in the dir — then DELETED at
this close-out). Work shipped on branch `probe/karma-reputation-system` (PR
number stamped in-branch after open per the never-guess rule).

## What this session did

- **Inbox FIRST**: read at origin/main HEAD `a2227ed` at wake — still exactly
  ORDER 001 (standing per-session rule, re-satisfied by this card's 📊 Model
  line) + ORDER 002 (done by #158, its Self-review section preserved verbatim
  on the heartbeat). No new orders.
- **Probe shipped — and the verify-first flipped it, harder than #180's**:
  the #180 💡 ledger-grep (superbot-next `docs/decisions.md` for karma nouns)
  hit **D-0037** ("Band 4 slice 2: KARMA — peer reputation on the one-txn
  ledger discipline (INV-K)") — and pulling the thread to the CANONICAL repo
  found karma **shipped at superbot itself on 2026-06-22**, EIGHTEEN days
  before this repo's 2026-07-10 harvest: owner-directed build
  (`.sessions/2026-06-22-karma-build.md` @ S — the owner said "you can
  execute this plan" and the session executed the plan's recommended
  defaults "since the 5 design questions were not individually answered"),
  subsystem folio `docs/subsystems/karma.md` ("Shipped (2026-06-22)" +
  react-to-thank "✅ shipped 2026-07-01 (PR #1620)"), full code tree under
  `disbot/` (cog, service, config, migration `093_karma.sql`, INV-K test,
  8 parity goldens) at live HEAD S=`8214200` (ls-remote 16:03:07Z).
  superbot-next N=`14e5037` ported it verbatim (D-0037, defaults PINNED
  equal to policy constants as a test) and test-hardened it (D-0061 clock
  split + refusal-copy fixes). The "5 owner-stalled questions" were consumed
  by the owner's plan authorization + shipped defaults (1h cooldown /
  10-per-day cap / reaction off-by-default / positive-only / pure
  reputation); ONLY karma-roles + milestone announcements stay deliberately
  owner-gated at the target's own folio. State advanced captured →
  `historical(built at superbot — owner-directed build 2026-06-22 … ported
  at superbot-next D-0037)`; index bullet re-badged with a
  `(state-drift: deliberate — …)` annotation (canonical superbot idea doc
  still reads `ideas` at S — the #161 adoption-record-rot class, now with a
  sharper datapoint: the stale Status line + roadmap gate line misled the
  #180 TOP-5 ranking itself).
- **Batching decision (briefed)**: the pairing with
  audited-score-subsystem-scaffold (#1346, TOP-5 item 4) DISSOLVES rather
  than batches — karma never waited for the scaffold (it hand-stamped the
  six-piece shape and is one of the scaffold idea's three named instances);
  probing karma alone kept the question sharp, and item 4's "the moment
  karma starts" trigger is re-priced as already-fired (its live value is the
  NEXT score subsystem + the rebuild's convention, per D-0037's own "on
  exactly the economy discipline" framing).
- **NO PROPOSAL 009** — the honesty guard outranks feeding sim-lab's empty
  queue, second slice running: the briefed defaults-sweep question (which
  karma parameter set survives adversarial/economy scenarios, sweeping the
  5 owner-stalled knobs) is MOOT — the knobs are shipped canonical constants
  live since 2026-06-22, operator-tunable per guild, test-pinned at N; the
  economy-adversary surface is null by design (pure reputation,
  non-spendable, Q-0190); anti-abuse integrity is already enforced by the
  rebuild's replay goldens + INV-K zero-tolerance reconciliation. Outbox
  tail stays PROPOSAL 008 (verdicted V008); next free number remains 009.
- **Heartbeat overwritten LAST**: TOP-5 updated (item 2 marked
  PROBED→historical this slice; item 4's trigger note re-priced), all
  preserved blocks carried verbatim (the FOUR-decision ≤07-14 ⚑ sitting
  bundle, the ORDER 002 Self-review section, the manager sweep flags,
  the check_sim_gate VALUE-drift note), last-shipped updated.
- Claim file deleted at close-out; guard-fires residue rides this PR per
  precedent (#178/#180 carried the same class).

**📊 Model:** fable-5 · probe slice (one idea-file append + state flip +
index re-badge + card + heartbeat + claim clear; no outbox append — verdict
did not earn one; no product code, Q-0260)

## 💡 Session idea

**Current-state grep is not a build check — folio/tree beats prose.** Two
consecutive TOP-5 rankings priced karma off "zero karma in superbot
current-state@main" — but superbot's `docs/current-state.md` NEVER mentions
karma (built or not), its idea-doc Status line was 18 days stale, and the
truth lived in `docs/subsystems/karma.md` + the `disbot/` tree. The #180 💡
(target-lane decision-ledger grep) caught the PORT; only a canonical-repo
tree/folio check caught the ORIGINAL build. Grooming seed: extend the
verify-first line to "grep the canonical repo's `docs/subsystems/` folio
index AND its code tree (blobless clone ls-tree) for the idea's nouns —
absence from current-state.md is NOT evidence of absence." Also a path
lesson: superbot's code roots at `disbot/`, so bare-path raw probes
(`cogs/…`, `services/…`) 404 on EXISTING files — the PR #141 stem-match rule
generalized to path roots.

## ⟲ Previous-session review

Newest prior card: `.sessions/2026-07-11-rerank-top5-probe-layout-success-sim.md`
(status `complete`; shipped #180, merge `e941ba4`; claim rode #179; heartbeat
stamp landed as #181/`a2227ed`). Spot-checked against the tree at `a2227ed`:
its probe report exists as promised (layout-success idea file — 3 Grounding
pins, 8 questions, `**Recommendation: park**` closing the report, state
`historical(built at superbot-next — D-0020 …)`); its index re-badge with the
state-drift annotation is live (ideas/superbot/README.md:185); its claim file
is gone from `control/claims/` (dir held only README.md at `a2227ed` —
re-verified before this slice claimed); NO PROPOSAL 009 in the outbox exactly
as its card states. Its 💡 (target-lane decision-ledger grep) was applied as
this slice's FIRST verify step and fired exactly as designed — D-0037 surfaced
in one grep — though this slice found the rot ran deeper (the canonical repo
itself had built the idea; see this card's 💡). No reconciliation debt handed
to this slice.

## Handoff → next wake

Inbox first, as always. Standing TOP-5 now has items 1 AND 2 consumed
(both historical, both flipped by verify-first) — **ripest next work: probe
item 3, settle-once-architecture-guard** (double-settlement class recurred a
FIFTH time at superbot-next #133; money leg built #1454; the guard is the
remainder while the rebuild mints new settling paths). Apply BOTH queued
verify-first 💡s before trusting that capture: the #180 ledger grep (D-#
nouns at superbot-next) AND this card's folio/tree check (superbot
`docs/subsystems/` + `disbot/` ls-tree for settle/settlement nouns). Item 4
(audited-score-scaffold) is re-priced by this slice: its karma trigger
already fired in the past — its live question is scaffold value for the NEXT
score subsystem given the rebuild's discipline is already conventional
(D-0037). Manager-side watches unchanged (theme-schema half-fired;
superbot-idle V006 guardrails; #161 adoption-record sweep — now carrying this
slice's sharper karma datapoint; #174 contract-shape attach flag;
effect-arming second-dependent note; check_sim_gate VALUE-drift note). Three
queued 💡s now: the README fan-in parse-rule line (#178), the target-lane
ledger-check line (#180 — VINDICATED live this slice, worth encoding), and
this card's folio/tree-beats-current-state line — all one-liners, foldable
into any control-touching slice.
