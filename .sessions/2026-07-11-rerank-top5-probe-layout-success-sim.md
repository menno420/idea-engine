# Session — re-rank: standing TOP-5 (fully-consumed shortlist regroomed) + probe: rebuild-layout-success-simulator (new #1)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-11 ~15:40Z (worker slice, coordinator-dispatched,
> two-phase: recon ran separately; this slice = claim + probe + re-rank + ship)

## Scope

The handoff's named ripest work: the standing TOP-5 was FULLY CONSUMED at #178
(items 1–5 all probed/parked/fanned-in), so this slice re-ranked the backlog
into a NEW standing TOP-5 and probed the new #1,
`ideas/superbot/rebuild-layout-success-simulator-2026-07-10.md`. Claim landed
first via fast-lane PR #179 (claim file
`control/claims/probe-layout-success-simulator.md`, branch
`probe/layout-success-simulator-claim` per the workprefix+`-claim` convention,
merged `6b18d61` by the auto-merge enabler on green; claim re-read at the new
HEAD — sole claim in the dir — then DELETED at this close-out). Work shipped on
branch `probe/layout-success-simulator` (PR number stamped in-branch after
open per the never-guess rule).

## What this session did

- **Inbox FIRST**: read at origin/main HEAD `d160d13` at wake and re-verified
  at `6b18d61` post-claim — still exactly ORDER 001 (standing per-session rule,
  re-satisfied by this card's 📊 Model line) + ORDER 002 (done by #158, its
  Self-review section preserved verbatim on the heartbeat). No new orders.
- **Re-rank shipped (the groom half)**: old TOP-5 retired as consumed (ledger
  on the #178 heartbeat); census at re-rank time: **184 captured** ideas (183
  after this slice's one state flip), 8 sim-ready, 55 parked, 52 historical.
  NEW standing TOP-5 (decay reasons one-line each, full text on the
  heartbeat): 1) rebuild-layout-success-simulator — superbot-next composing
  hubs at band-5 pace while 4 bespoke UX sims stay fragmented; owner-proven
  value class (#1617→#1621); every unscored layout freeze raises retrofit
  cost. 2) karma-reputation-system — zero karma at superbot current-state@main;
  its own blocker (cooldown/daily-cap TBD, "S1 Later — blocked on owner
  answers") is the sim-pinnable half. 3) settle-once-architecture-guard —
  double-settlement class recurred a FIFTH time (superbot-next #133
  double-payout race); money leg built (#1454), guard is the remainder while
  the rebuild mints new settling paths. 4) audited-score-subsystem-scaffold —
  partially implemented (#1346); load-bearing the moment karma (item 2) or any
  score subsystem starts; natural batch-pair with item 2.
  5) wager-flow-map — no coin-path tracer at current-state@main; VERDICT 001 +
  V008 green-light loot faucets whose coin paths will be born untraced.
  Named exclusions: mining-exploration-brainstorm DECAYED (mining platform
  batches/gear/vault/forge shipped; exploration carried by PROPOSALs
  003/004/008); rps-tournament-service-refactor DECAYING (rps already
  registers at superbot-next — refactor spend on the live cog loses value as
  parity advances). Websites heads rank below superbot per Q-0259 weighting +
  fm ORDER 012/013 sequencing + lane self-serve risk.
- **Probe shipped (the new #1) — and the verify-first flipped it**: the
  briefed mandatory check (has any superbot-next band already ported or
  consolidated the UX sims?) answered **YES** before the battery ran:
  superbot-next **D-0020** ("Layer-V V-3: sim runner + oracles +
  check_sim_gate", decided **2026-07-08** — two days BEFORE this repo's
  harvest) built `sim/` fresh to design-spec §2.10: one shared runner +
  pluggable oracle registry (navigation = the Q-0235 instruction-driven
  engine — deterministic label-match user, task-success-rate / path-hops /
  wrong-turns; settings_grouping; dense_panel), `sim/apply.py` as the SOLE
  layout-lock writer with mandatory SimRef provenance, `check_sim_gate` in
  CI (sim-gate = one of the six §6 named gates). The #1701 amendments are
  encoded as design: distinct oracles, corpus INDEPENDENT of the NL-router
  eval corpus (the Goodhart caution), AI naive-user leg advisory-only per
  §8 Q9. Consumption evidenced (D-0027 hub layout derived from it; D-0034
  economy hub rows as declared grammar; recurring "ZERO sim-gate/lock churn"
  closes). All pins in the probe report (superbot S=`8214200`, superbot-next
  N=`14e5037`, ls-remote 15:47:08Z). State advanced captured →
  `historical(built at superbot-next — D-0020, 2026-07-08: sim/ shared
  runner + oracle registry + check_sim_gate CI gate)` per the README's
  built precedent; index bullet re-badged with a
  `(state-drift: deliberate — …)` annotation (canonical superbot doc still
  reads `ideas` at S).
- **NO PROPOSAL 009** — the honesty guard outranks feeding sim-lab's empty
  queue: the briefed candidate question (deterministic vs AI user-model
  agreement on layout rankings) is SETTLED BY DESIGN at the target
  (deterministic primary, naive-user advisory-only per §8 Q9; Goodhart
  guardrail encoded), and the framework's records are bit-for-bit
  reproducible inside the target's own CI — an external replay would settle
  nothing a required green gate doesn't already enforce. Outbox tail stays
  PROPOSAL 008 (verdicted V008); next free number remains 009.
- **Heartbeat overwritten LAST**: NEW standing TOP-5 installed (item 1 marked
  PROBED→historical this slice), all preserved blocks carried verbatim (the
  FOUR-decision ≤07-14 ⚑ sitting bundle, the ORDER 002 Self-review section,
  the manager sweep flags), plus one NEW informational sweep note: the
  ledgered `check_sim_gate` VALUE-drift gap at superbot-next (@codex comment
  4947003427, head `47d5cb8`) is that lane's own checker hygiene — named so
  the sweep sees it once, routed nowhere from this seat (Q-0260).
- Claim file deleted at close-out; guard-fires residue rides this PR per
  precedent (#178 carried the same class).

**📊 Model:** fable-5 · re-rank + probe slice (one idea-file append + state
flip + index re-badge + card + heartbeat + claim clear; no outbox append —
verdict did not earn one; no product code, Q-0260)

## 💡 Session idea

**Target-lane decision-ledger check for cross-lane ideas.** This probe found a
capture that was ALREADY BUILT two days before it was harvested — invisible to
every existing freshness tool because the build lives at the TARGET lane
(superbot-next `docs/decisions.md` D-0020), while `check_harvest
--states`/`--re-badge` only read the CANONICAL repo's own status markers
(superbot's doc still says `ideas`). Rule worth one line in the probe-order
section: for any idea whose `**Target:**` differs from its canonical repo,
verify-first MUST include the target lane's decision ledger (grep its
`docs/decisions.md` for the idea's nouns) before ranking it #1 — a
2-day-stale capture cost this slice a full probe that a 30-second ledger grep
would have priced. (The #178 card's queued 💡 — the README fan-in parse-rule
line "quote `ruling:` when present, else `recommendation:`" — stays queued,
foldable into any control-touching slice.)

## ⟲ Previous-session review

Newest prior card: `.sessions/2026-07-11-probe-lean-boot-v008-fanin.md`
(status `complete`; shipped #178, merge `d160d13`; claim rode #177). Spot-
checked against the tree at `6b18d61`: its item-5 park exists as promised
(`ideas/superbot/sector-scoped-lean-boot-for-cheap-models-2026-07-10.md` —
state `parked(routed — kit/fm seat-bootstrap design; behind fm
model-allocation ruling)`, Sequence line present, 3 Grounding pins, park
recommendation closing the report); its V008 fan-in block exists as promised
(`ideas/superbot/mining-grid-encounters-2026-07-10.md` § `## Sim verdict
(2026-07-11)` — bold FINALIZED marker, `= this repo's PROPOSAL 008` numbering
cross, needs-more-evidence + recommendation-quoted form, defaults
threshold=15/20 · chance=0.02 · cooldown=600s with the three guardrails);
its claim file is gone from `control/claims/` (dir held only README.md at
`d160d13` — re-verified before this slice claimed). Its handoff named the
TOP-5 re-rank as the ripest next work and predicted a 009+ comes only from
probing new sim-shaped heads — the re-rank fired this slice; the 009
prediction met the honesty guard instead (new #1 verified already-built at
its target). No reconciliation debt handed to this slice.

## Handoff → next wake

Inbox first, as always. The NEW standing TOP-5 is installed on the heartbeat
with item 1 already consumed (historical this slice) — **ripest next work:
probe item 2, karma-reputation-system**, whose blocker half
(cooldown/daily-cap parameter space, "blocked on owner answers") looked
sim-pinnable at ranking time and could honestly mint PROPOSAL 009 for
sim-lab's still-EMPTY queue; apply this card's 💡 first (grep superbot-next's
decision ledger for karma nouns before trusting the capture). Manager-side
watches unchanged (theme-schema half-fired; superbot-idle V006 guardrails;
#161 adoption-record sweep; #174 contract-shape attach flag; effect-arming
second-dependent note) plus the NEW check_sim_gate VALUE-drift note. Two
queued 💡s now: the README fan-in parse-rule line (from #178) and this card's
target-lane ledger-check line — both one-liners, foldable into any
control-touching slice.
