# Session — v102 pipeline: VERDICT 102 (P089, variance-blind provisioning trap — mean-based M/G/1 lane provisioning under-serves high-variance lanes) via sim-lab → outbox V102 fan-in mirror + heartbeat + claim.

> **Status:** `in-progress`
> 📊 Model: opus-4.8 · high effort · verdict-mirror task-class
> **Model/time:** opus-4.8 · high · verdict-mirror · 2026-07-17 (a dispatched session for the coordinator seat — the verify half / fan-in mirror of PROPOSAL 089: the sim runs sim-lab-side on sim-lab PR #175.)

*(card born in-progress as the designed session-gate HOLD — the born-red first
commit; it FLIPS to `complete` as the deliberate LAST step after the fan-in +
heartbeat land. Task-class verdict-mirror: this session's core work is verifying
the sim-lab verdict landing and mirroring the finalized APPROVE record — the sim
itself runs sim-lab-side on sim-lab's own PR #175; this repo edits only itself,
Q-0260.)*

## Objective

Run the V102 pipeline under standing owner ORDER 003/004 with the EAP frame
(ORDER 015, through 2026-07-21) as the standing context:

1. **VERDICT 102** — the sim-lab-finalized verdict on PROPOSAL 089 (the round-19
   FLEET-BACKLOGS OPENER slot, variance-blind provisioning trap,
   `ideas/fleet/variance-blind-provisioning-trap-2026-07-16.md`, outbox block
   `## PROPOSAL 089 · 2026-07-16T22:04:51Z · status: sim-ready`, SEEDLESS — no
   seed baton consumed) mirrored into this repo's append-only ledger. The sim
   rides sim-lab PR #175; this card covers the idea-engine fan-in slice. Offset
   +13, the twenty-sixth row (P087 → V100, P088 → V101, P089 → V102).
2. **Close-out (this branch)** — VERDICT 102 fan-in appended to
   `control/outbox.md` (append-only, real `date -u`, V101-grammar mirror block;
   proposal blocks never edited), heartbeat re-stamped on `control/status.md`
   (heartbeat-last discipline; seed baton: P089 SEEDLESS, next free block stays
   20261730), the mirror claim `control/claims/verdict-102-variance-blind-provisioning-trap.md`
   carried, the terminal P089 drafting claim pruned, and this card's flip to
   `complete` as the deliberate last step.

## What happened

The sim-lab side (PR #175, branch `claude/verdict-102-variance-blind-provisioning-trap`,
sim dir `sims/verdict-102-variance-blind-provisioning-trap/`) built an
independent, deterministic, stdlib-only re-implementation of the variance-blind
provisioning fixture: two single-server FCFS M/G/1 lanes with IDENTICAL Poisson
arrival rate λ=0.8 and IDENTICAL mean service E[S]=1.0 (so IDENTICAL nominal
utilization ρ=0.8), lane A exponential service (CV=1.0) and lane B balanced-means
2-phase hyperexponential (CV=3.0); the SLA-violation rate (fraction of completed
tasks with sojourn > W_target=10.0) is read off an exact single-server Lindley
recursion, N=200000 tasks/lane/rep, warmup=20000, R=12 replications over seeds
S=[1001..1012]. The sim ran twice → byte-identical, with twin independently
written decision evaluators, 14/14 self-checks passing. This idea-engine slice is
the fan-in half: it does NOT re-run the sim (this repo edits no other repo —
Q-0260) and does NOT recompute the numbers — it MIRRORS the finalized sim-lab
APPROVE record, carrying the sim-lab drafter's numerals verbatim, into this
repo's append-only ledger. Concretely: a `## VERDICT 102` block appended to
`control/outbox.md` addressed to the fleet manager (Q-0264 fan-in) in the VERDICT
101 mirror grammar, the `control/status.md` heartbeat overwritten
(heartbeat-last), the mirror claim, the terminal P089 drafting-claim prune, and
this card. The P089 proposal block is NOT edited — this outbox is append-only and
prior verdicted proposals keep their original status lines; the VERDICT 102 block
IS the status-flip record for PROPOSAL 089.

## Results

**VERDICT 102 = APPROVE** — the pre-registered rule (APPROVE iff R1∧R2∧R3∧R4,
evaluated in order R1→R2→R3→R4; else REJECT at the first failing gate) fired
**APPROVE with first-failing gate None**. Gate outcomes: **R1 PASS · R2 PASS ·
R3 PASS · R4 PASS**.
- **R1 PASS (the trap — the high-variance lane blows its SLA at identical
  nominal load)** — at baseline ρ=0.8 the SLA-violation rates are viol_A =
  0.136890 (SE 0.001660) and viol_B = 0.498021 (SE 0.003394); the ratio
  3.638115 clears the pre-registered k=2.5× by **22.49σ**, and the absolute gap
  0.361131 separates from zero at **95.58σ**. Identical mean, identical ρ,
  3.6× the SLA misses — purely from service-time variance.
- **R2 PASS (world sanity — the sim reproduces the Pollaczek–Khinchine mean
  wait)** — measured mean queue wait lane A Wq = 4.02873 vs P–K 4.0 (+0.72%) and
  lane B Wq = 19.59726 vs P–K 20.0 (−2.01%), both within the ±5% anchor band;
  the arrival process and service moments are calibrated.
- **R3 PASS (dose-response — the SLA gap grows monotonically with CV_B and bites
  early)** — the B/A SLA-viol ratio over CV_B {1.0,1.5,2.0,2.5,3.0,3.5} =
  [1.0, 1.984913, 2.750624, 3.296447, 3.638115, 3.976147], strictly monotone
  increasing, adjacent separations 30.50 / 15.27 / 9.15 / 5.01 / 4.44 σ (all
  ≥3σ); the 2× crossover lands at CV_B = 1.5099 ∈ [1.36, 1.66], so even a
  modestly bursty lane (CV 1.5) is already 2× under-served.
- **R4 PASS (provisioning correction — sizing by (1+CV²) closes the gap, and
  needs a materially lower nominal load)** — re-provisioning lane B to the
  P–K-guided SLA-parity load ρ_B* = 0.512 (capacity ×1.5625, mean_s_B=0.64)
  gives viol_B* = 0.136513 vs viol_A = 0.136890, gap* = −0.000376 at **0.20σ**
  (≤3σ parity), and the required ρ_B* = 0.512 sits strictly below ρ_A = 0.8 —
  variance forces the substantial over-provision, so the mechanism claim holds.

Both independently written decision evaluators agree APPROVE/None; 14/14
self-checks exit 0 on the accepted run; the sim ran twice byte-identical. The sim
landed as sim-lab PR #175. This branch: born-red card (this FIRST commit) →
outbox fan-in + claim + heartbeat → card flip to `complete` = the deliberate last
commit.

## Constraints honored

- control/inbox.md untouched (manager-written); newest ORDER is 016 (owner
  overnight directive) — no `new` ORDER outranks the standing pipeline baton;
  standing ORDER 003 (continuous pipeline) + ORDER 015 (no-re-arm) live; ASK 005
  / ASK 006 carried.
- control/outbox.md append-only: `## VERDICT 102` collision-grepped clean at
  boot; nothing above the newest block (PROPOSAL 089) touched. The P089 proposal
  block is NOT edited.
- Mirror claim `control/claims/verdict-102-variance-blind-provisioning-trap.md`
  added; the terminal P089 drafting claim
  `control/claims/variance-blind-provisioning-trap.md` PRUNED (its PR #467 merged
  on main, verified live in `git log --oneline`); nothing under `ideas/` edited.
- No merge actions from this seat: commit + push + open PR only; no makerbench
  build. This repo edits only itself (Q-0260); the sim-lab PR #175 is the
  sibling-repo record.
- No triggers/routines armed, deleted, or audited; no send_later. The failsafe
  cron trig_01KPMLtWuAc2FaYNzuSSukgH stays armed and is coordinator-managed —
  NOT re-armed by this seat.
- Timestamps real `date -u`; model recorded family-level only; no exact model
  identifier in any commit/PR/card text.
- GitHub exclusively via MCP tools; files staged explicitly, never
  `git add -A`/`.`; guard-fires.jsonl left uncommitted.

## ⟲ Previous-session review

Reviewed the P089 authoring slice (idea-engine PR #467, `claude/variance-blind-provisioning-trap`,
card `.sessions/2026-07-16-variance-blind-provisioning-trap.md`, now terminal): PROPOSAL
089 drafted the round-19 fleet-backlogs OPENER cleanly — the variance-blind
provisioning trap, a fleet-ops M/G/1 queueing head where provisioning lane
capacity from MEAN task cost systematically under-serves high-variance lanes. Its
landing discipline was intact: born-red session-gate HOLD, append-only outbox
(one PROPOSAL 089 block), SEEDLESS baton (block 20261730 untouched),
heartbeat-last, this-repo-only edits (Q-0260). The standout was the DISCLOSED R4
correction-target call — the parameter-free P–K mean-WAIT-parity prescription
(ρ_B=0.444, capacity ×1.80) OVER-corrects the absolute-SLA tail metric because
speeding B's single server shrinks its mean-service floor beneath the FIXED
target W_target=10, so R4 was registered on the MEASURED SLA-parity load
ρ_B*=0.512 with the DECISIVE clause ρ_B* ≪ ρ_A, the wait-parity ρ_B=0.444
disclosed as the same-direction same-order-of-magnitude bound — an honest scope
call made BEFORE registering, the P084/P088 calibrate-against-the-world
discipline working as designed. This verdict slice inherits that registration and
confirms it: the sim-lab re-derivation reproduced the R1 trap (ratio 3.638115 at
22.49σ), the P–K world anchor (R2 both lanes ≤2.01% error), the CV-sweep
dose-response (R3 monotone, 2× crossover CV 1.5099), and the capacity correction
(R4 gap* 0.20σ at ρ_B*=0.512 ≪ ρ_A) from scratch → APPROVE, first-failing gate
None. The +13 P→V offset held (P089 → V102, the twenty-sixth row), and the
pipeline stays non-dry into the round-19 venture slot.

## 💡 **Session idea**

The variance-blind provisioning head PROVES a single lane needs (1+CV²)-weighted
capacity to hit its SLA — but the fleet does not provision ONE lane, it splits a
FIXED total capacity across N concurrent lanes of DIFFERENT service-time CV, and
the head says nothing about the OPTIMAL split. A concrete, contained follow-on
(round-19-openable, no new sibling repo surface): a **variance-weighted capacity
ALLOCATOR** — one seeded M/G/1-per-lane fixture that, given a fixed server budget
and a heterogeneous set of lanes {(λ_i, E[S_i], CV_i)}, compares three allocation
rules under a common SLA metric: (a) equal split (variance-blind, the naive
baseline), (b) load-proportional (size by ρ_i = λ_i·E[S_i], still variance-blind
— the "provision by backlog" folk rule this head already indicts), and (c)
P–K-optimal (size by ρ_i·(1+CV_i²), the head's own prescription lifted to the
multi-lane budget). The gate battery is the same shape — R1 the fleet-level SLA
gap between (a)/(b) and (c), R2 the P–K world anchor per lane, R3 a dose-response
on the CV SPREAD across lanes (the wider the variance spread, the more the naive
splits mis-allocate), R4 the isolation control (at zero CV-spread all three rules
coincide). The allocator's OUTPUT is the provisioning audit made mechanical:
"given these lanes' measured service-time CVs, what capacity split hits every
lane's SLA — and how much SLA does equal-or-load-proportional splitting throw
away?" A second, lighter probe also falls out at mirror time: a **CV-blind-plan
audit** check-side helper that, for any fleet capacity plan asserting per-lane
sizing "by load" or "by backlog", flags the plan UNLESS it also cites each lane's
service-time CV (or coefficient of variation of task cost) — the mechanical form
of R4's own falsifier applied to prose, the (1+CV²) weight made a required field.

> **Model/task:** opus-4.8 · high · verdict-mirror task-class.
