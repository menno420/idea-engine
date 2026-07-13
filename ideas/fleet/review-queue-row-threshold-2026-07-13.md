# Review-queue row-trigger threshold priced — size-arm defect miss vs drain saturation (fleet-manager N = 50)

> **State:** sim-ready
> **Class:** process (pipeline rotation — the standing ORDER 003 FLEET-BACKLOGS
> slot, round 6; harvest source: the fleet-manager's own backlog, a FIFTH repo for
> this slot — rounds 1–5 were P019 websites → V021 approve, P021 superbot → V023
> reject, P025 kit claims doctrine → V027 reject, P029 lease-renewal → V031 null,
> P033 assign-at-merge queue tax → V035 null) ·
> **Target:** `menno420/sim-lab` (verification target per the Q-0264 pipeline; the
> deliverable is a committed stdlib sim + a citable measured verdict — no lane build)
> **Grounding:** https://github.com/menno420/idea-engine@2b43de296e15c64b3b04f6380d88f97c5f2936e6 · fetched 2026-07-13T15:50:00Z
> (this repo's own tree at backfill HEAD — the pin under which the P037 outbox
> block was re-read verbatim; the harvest source itself is pinned inside that
> block at fleet-manager `06ce3cc`)

**Origin + provenance (backfill, disclosed):** PROPOSAL 037 was drafted as a
control-only fast-lane slice (PR #315, merged 2026-07-13T15:10:59Z) whose block
disclosed "no local idea file is committed, a disclosed deviation from the
P017–P036 idea-file precedent". That deviation left `scripts/check_ideas.py
--outbox` RED at main HEAD `2b43de2` (LINK: "PROPOSAL 037: `idea:` carries no
menno420/idea-engine ideas/ link") — a latent gate any next non-control PR would
inherit. This file backfills the convention: the **full probe/summary/question/
done-when text rides the P037 block in `control/outbox.md` verbatim and stays
the source of truth**; this doc condenses it so the outbox↔ideas link contract
holds. A correction `idea:` line inside the P037 block links here.

## The idea (condensed from the P037 block)

The fleet-manager's binding review-queue auto-append rule
(`docs/review-queue.md:12–17` @ `06ce3cc`) rows every PR adding more than
**N = 50** changed lines of runtime/product code OR carrying any self-flagged
risk. N = 50 was seeded decide-and-flag ("the owner may re-tune") on zero data,
with both failure directions named qualitatively by the doctrine itself (a lower
N drowns the queue in ceremony rows nobody drains; a higher N lets exactly the
mid-size logic changes through) and the stakes already realized once ("116
merged PRs / zero rows was the state that voided it"). The head prices that
invented constant under a pinned hermetic fleet-merge-stream model: a
three-class PR-size mixture (docs-only / tweak / feature), a per-line defect
model (q₁ = 1/400, invented, pinned, the disclosed weakest joint), a self-flag
OR-arm (r = 3/10), N swept over {0, 10, 25, 50, 100, 200} with both exact
controls in-grid, and rows draining in 6-h wake batches at drain-to-merge tiers
d ∈ {1/5, 2/5, 4/5} — the harvest item's own fork (wake-step drain vs a
dedicated reviewer lane) made a decision axis. Decision metrics per (cell, N):
REL(N) — the size-arm defect miss share — and ρ(N) — drain utilization, the
doctrine's own "drowns the queue" axis — computed in BOTH an exact closed-form
Fraction arm (all 54 decision points, zero sampling error) and a seeded
event-driven MC arm (seeds 20261285–88, strictly above the fleet high-water
20261284), with pre-registered bands: REJECT first (Feas(cell) = ∅ in ≥ 5/9
cells → descope threshold re-tuning, route the risk-signal redesign), APPROVE
(one fleet-wide N† feasible in ≥ 8/9 cells → pin it with its drain tier), else
NULL (the conditional per-tier/per-mix rule ships + three named zero-tooling
live probes).

## Probe report (v0, 2026-07-13 — backfill condensation)

> The probe rode the P037 outbox block itself (the fast-lane deviation, stated
> there); this section condenses it into the battery form so the idea grammar
> holds. Every claim below is sourced from the block @ `2b43de2`.

**1. What is this really?** A pre-registered repricing of a doctrine constant
seeded by vibes: the fleet-manager review-queue rule's N = 50 row-trigger,
priced on its own two named failure axes (defect miss vs drain saturation)
under a fully hermetic, dual-arm (exact Fractions + seeded MC) policy-grid sim
— the exact P025 shape (reprice a flagged-revisable invented constant by a
pre-registered grid).

**2. What is the possibility space?** Leave N = 50 unmeasured (the standing
latent risk the doctrine itself names); re-tune it by owner intuition (repeats
the original sin); measure it live first (the NULL branch's probes — but the
model brackets the space at zero fleet-data cost today); or this head: price
the threshold family hermetically, with the drain-capacity fork as a decision
axis and live probes pre-named for NULL.

**3. Most advanced capability from the simplest implementation?** One stdlib
sim + fixture JSON: 54 closed-form decision points (geometric partial sums, all
exact Fractions) cross-gated against an event-driven MC of the 6-h batch-drain
queue — a citable per-tier/per-mix feasibility table for the whole trigger
family, from minutes of compute.

**4. What breaks it?** The per-line defect model — q₁ = 1/400 is invented and
NO fleet datapoint on defect rates exists (disclosed weakest joint; sweeps
bracket scale, not shape). Miss ≠ harm (REL prices the loss of the safety
valve, not total harm). d is quota-bracketed, not measured. PR-splitting to
duck the threshold is out of scope (cooperative lanes, the V027 registration
inherited). All stated in the block's done-when boundaries.

**5. What does it unlock?** An evidence row for (or against) the one constant
every enabled repo's row-append ritual inherits; on REJECT, descoping doctrine
churn BEFORE it is spent and routing the risk-signal redesign with the
infeasibility table attached; on NULL, three zero-tooling live probes (numstat
census, ⚑-flag census, drain-tempo count) that turn the question from modeling
into measurement.

**6. What does it depend on?** Nothing at verdict time — fully hermetic, every
fixture a pinned constant committed with the sim, doctrine quotes pinned
verbatim @ fleet-manager `06ce3cc`. Consumers: fleet-manager owns the rule
(routing is the manager's per Q-0260 — this repo never edits fleet-manager
files); co-consumers named in the block's `depends:`.

**7. Which lane should build it?** sim-lab (method provider — the hermetic
dual-arm pre-registered discipline is the PROPOSAL 017–036 committed
precedent); the verdict consumer is fleet-manager via the manager sweep. Dedup
ran at drafting (block @ `2b43de2`): no proposal 001–036 and no verdict
V001–V046 touches PR-size distributions, review-row triggers, defect-escape
shares, or post-merge review capacity; nearest neighbors (P019/V021 by shape,
P025+P029/V027+V031 by move, P033/V035 by method) are disjoint on
queue/metric/consumer, argued line-by-line in the block.

**8. What is the smallest shippable slice?** The committed stdlib sim + fixture
JSON reproducing the full {REL, ρ, ESC, p95 age, ≤72 h share} × (cell, N) table
byte-identically per the block's done-when — already fully specified there;
this file adds no scope.

**Recommendation: sim-ready** — the proposal is already on the sim-lab pull
surface as PROPOSAL 037 (outbox @ `2b43de2`, drafted via PR #315); this
backfill restores the idea-file convention behind it so the outbox↔ideas LINK
gate holds. State advances to `historical(…)` on the verdict's arrival per the
forward-only rule.
