# Open-PR awareness at wake — sibling-session collision check — link index

> **State:** parked(build-direct — websites wake-ritual doc edit, lane-sized, relayed via manager fan-in; fleet-generic convention cross-linked to substrate-kit — see probe report)
> **Class:** process · **Target:** `menno420/websites`
> **Grounding:** https://raw.githubusercontent.com/menno420/websites/144dfced7282806efe778eaacb3565a13e35c2fa/docs/ideas/open-pr-awareness-at-wake-2026-07-10.md@144dfce · fetched 2026-07-10T22:33Z

**Canonical idea (stays in websites — indexed by link, never copied):**
[`menno420/websites → docs/ideas/open-pr-awareness-at-wake-2026-07-10.md`](https://github.com/menno420/websites/blob/144dfced7282806efe778eaacb3565a13e35c2fa/docs/ideas/open-pr-awareness-at-wake-2026-07-10.md)
— harvested 2026-07-10 by the websites lane-backlog harvest slice, pinned @ websites `144dfce`
([raw](https://raw.githubusercontent.com/menno420/websites/144dfced7282806efe778eaacb3565a13e35c2fa/docs/ideas/open-pr-awareness-at-wake-2026-07-10.md)).

Add one step to the lane's wake ritual: list open PRs plus PR-less unmerged
`claude/*` branches BEFORE picking a work rung, classifying each into three states —
PR open (leave it to its session), branch pushed PR-less (rescue candidate), or
merged-stale (ledger drift to fix). Grounded in two same-day lived failures: a wake
that started ~6 minutes after a sibling pushed PR #63 and only an ad-hoc `ls-remote`
prevented a merge conflict on a shared doc, and a committed ledger still calling a
merged branch "not yet merged" hours after it landed — the live PR list never lies
where committed state goes stale. Deduped by the doc itself against heartbeat
enrichment's `landing:` line, which covers a session's OWN branch only; nothing
covers discovering OTHER sessions' in-flight code. The same failure class
idea-engine's claims ritual fixes for sections, applied to branches — and one of the
lane's ripest sim-worthy heads (mechanical scope, concurrent sessions now the norm).

## Probe report (v0, 2026-07-10)

> **Grounding:** https://raw.githubusercontent.com/menno420/websites/8dc5ec2f2c28904423ab046e5eaff17870c194b5/docs/ideas/open-pr-awareness-at-wake-2026-07-10.md@8dc5ec2f · fetched 2026-07-10T23:04Z
> **Sequence:** after the two lived failures it cites (websites #63 near-collision, the stale "Not yet merged" ledger) — probed while concurrent sessions are the fleet norm (Q-0265 continuous mode)

*Timeliness verified live FIRST (the PR #25 lesson). websites HEAD
`8dc5ec2f2c28904423ab046e5eaff17870c194b5` transport-verified via `git ls-remote
refs/heads/main` at probe time (23:04Z) — AHEAD of the harvest pin `144dfce`; the
canonical doc is byte-identical at both SHAs (equal sha256, `d4e4c2a6…`), so the header
pin above stays faithful. At websites HEAD `8dc5ec2f`: (a) the wake ritual still has NO
open-PR step — `docs/project/routine-prompt.md` (WAKE line) reads `control/inbox.md`
only, and `docs/project/project-instructions.md` § ROUTINE-FIRED protocol sweeps orders
and landing tools, never sibling branches; (b) both cited failures are transport-real:
PR #63's merge commit `507be5a` is in main history, and the stale "Not yet merged"
ledger passage is recoverable verbatim at `docs/planning/queue-state-2026-07-09-winddown.md@507be5a`
with its 20:00Z correction (PR #64) at HEAD; (c) the gap is live: `git ls-remote` at
probe time shows three `claude/*` branches plus `manager/control-plant` all carrying
commits not on main, and commit-count alone cannot say which are squash-merge leftovers
vs rescue candidates. The window is real, not stale.*

**1. What is this really?**
The claims ritual, applied to code. This repo's bus already covers ORDERS (inbox +
claim-first-on-main) and SECTIONS (`claims/` per-file, the measured ≈0%-conflict
ritual); NOTHING covers in-flight BRANCHES and PRs — the exact surface where two
same-day websites failures happened. The idea is one wake-ritual read step plus a
three-state classifier (PR open → leave it to its session · pushed PR-less → rescue
candidate for the stranded-work protocol · merged-stale → ledger drift to fix). PROCESS
class; the product is collision-free concurrency, not a script. One honesty note the
canonical doc softens: in failure (b) the committed ledger was wrong in BOTH directions
— it said "not yet merged" after the work landed as PR #59, and its "the branch is
pushed" claim was also false (the push had never landed; the work needed rescue). A
live sweep catches state overstated and understated alike — committed ledgers go stale
the moment a sibling acts; the remote never lies.

**2. What is the possibility space?**
- **Minimal:** one documented wake-ritual line — `git ls-remote --heads origin` plus a
  PR list where the seat carries PR tooling — classified by eye against the three-state
  table.
- **Script:** the canonical doc's own `scripts/open-work.py` printing the three-state
  table (a `check_harvest.py`-sized stdlib build).
- **Heartbeat dual:** the kit heartbeat's `landing:` line covers a session's OWN branch;
  this is its OTHER-sessions dual — deliberately a live READ step, not a new committed
  surface (no new writer, no staleness).
- **Kit-planted convention:** the same step in the kit-planted `control/README.md` wake
  ritual — every kit-adopted lane inherits it at its next `upgrade`, orders → sections →
  branches completing the bus.
- **Kit hook carrier (rejected):** the kit's `session-start` injection is the obvious
  hook, but its evidence sources are deliberately zero-network/zero-subprocess (the
  session anchor reads `.git` by pure file parsing; `bootstrap.py` has zero remote
  awareness today) — a live `ls-remote` belongs in the documented ritual the hook points
  at, not in the hook.
- **Degenerate corner:** a classifier trusted without PR data — commit-count alone
  misclassifies squash-merge leftovers as rescue candidates (live example: the three
  `claude/*` branches right now), manufacturing the false "needs rescue" alarms the idea
  exists to kill.

**3. What is the most advanced capability reachable by the simplest implementation?**
Fleet-grade collision avoidance from a one-paragraph doc edit. The documented two-command
sweep plus the three-state table is the branches/PRs analogue of this repo's per-file
claims ritual, whose measured result (superbot Q-0195) was ≈0% merge-conflict rate vs
~98% for the shared-ledger alternative. The most advanced reachable capability is not
the websites script — it is the CONVENTION: the same paragraph in the kit-planted
`control/README.md` makes every current and future lane's concurrency safe for the cost
of one template edit; `open-work.py` is an optional convenience on top, not the load-bearing part.

**4. What breaks it?**
- **Seat capability variance (the decisive one):** listing PRs needs tooling many seats
  lack — websites' own PR #59 incident was a no-PR-tooling seat, and this probe's seat
  could not count websites' open PRs (MCP scoped to idea-engine; anonymous api.github.com
  is walled). `ls-remote` is universal; PR state is not. The step must degrade honestly:
  branch sweep always, PR sweep when the seat can, and "not classifiable from this seat"
  said out loud (Q-0120 — never launder a guess into a verification). This is the same
  per-seat honesty problem PROPOSAL 005 already has queued at sim-lab (INTAKE 005).
- **Squash-merge ambiguity:** unmerged-by-commit-count ≠ unmerged-by-content; without PR
  data the three-state classifier cannot separate leftovers from rescue candidates.
- **Ritual bloat:** wake rituals accrete; the canonical doc's own char-budget caveat is
  real — this must stay one line plus a table, not a ceremony.
- **Staleness inversion:** if the sweep's OUTPUT ever gets committed (an "open work"
  ledger), it goes stale exactly like the ledger it fixes. The step is a live read,
  never a committed artifact.

**5. What does it unlock?**
Duplicate-build and shared-file-conflict prevention wherever sessions run concurrently —
which since Q-0265 is everywhere; false "needs rescue" alarms die; the stranded-work
protocol gains its missing discovery half (today `landing:` self-reports, nothing
discovers); and the kit-planted version hands all of it to every lane — including the
≥3 games seats now booting (Q-0259 r.5) — at their next kit upgrade, for free.

**6. What does it depend on?**
`git ls-remote` reachability of origin (universal — every session already pushes); PR
tooling where the seat has it (degradation documented, Q4); the lane's existing
stranded-work protocol as the "rescue candidate" sink; and for the fleet-generic half,
the kit-planted `control/README.md` template (substrate-kit owns it). No unmerged
prerequisite anywhere; build size is a doc edit (websites) plus a template paragraph
(kit).

**7. Which lane should build it?**
A split, PR #29-shaped but with the weight on the lane:
- **websites builds its own step, build-direct.** The lane owns
  `docs/project/routine-prompt.md` and `project-instructions.md`; the canonical doc —
  already sitting in the lane's own backlog — names the exact files and even the char
  budget. Lane-sized, zero dependencies, and the ad-hoc version already worked once
  (it is what caught #63). Idea-engine writes only this repo, so the routing is a
  MANAGER relay note on `control/status.md` for the :30 sweep fan-in; the lane can
  equally self-serve at its next wake.
- **substrate-kit owns the fleet-generic convention.** The planted `control/README.md`
  already carries the order-claim re-read and the `landing:` line; the open-work sweep
  is the missing third leg (orders → sections → branches) — one grammar, one template,
  every adopter inherits. NOT the `session-start` hook (zero-network doctrine, Q2).
  Routed as a Cross-links entry in `ideas/substrate-kit/README.md` (PR #17 rule),
  this slice.
- Not idea-engine: `park(built-here)` is for repo-internal tooling, and this build's
  consumers are other lanes — though this repo should itself adopt the sweep (its own
  sibling PR #38 was discovered by exactly this ad-hoc `ls-remote` during this probe),
  which is a separate one-line capture, not this build.

**8. What is the smallest shippable slice?**
One websites PR: add the sweep step — one line plus the three-state table, with the
graceful-degradation sentence (branch sweep always; PR sweep when the seat carries the
tooling; unclassifiable = say so) — to the WAKE preamble in
`docs/project/routine-prompt.md` and the ROUTINE-FIRED protocol in
`docs/project/project-instructions.md`. `scripts/open-work.py` is a legitimate SECOND
slice, not the first — the doc step alone already prevented the #63 collision when done
ad-hoc. What must NOT ship: a committed open-work ledger (Q4's staleness inversion) or
a label-free classifier that guesses PR state it cannot see.

**Recommendation: park** — no simulator question exists (a wake-ritual read step is
proven by lived usage and one golden classifier table, not by reproduced simulation;
the one genuinely open question — per-seat PR-tooling variance — is already PROPOSAL
005's battery, queued at sim-lab as INTAKE 005), and the build belongs to lanes this
repo does not write: websites build-direct for its own ritual step (manager fan-in
relay via the heartbeat) plus substrate-kit for the fleet-generic planted
`control/README.md` convention (Cross-links entry landed this slice).
