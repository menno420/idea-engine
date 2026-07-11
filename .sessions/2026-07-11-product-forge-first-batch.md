# Session — product-forge first idea batch (the empty roster-born section gets its first honest captures)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-11 ~03:38Z (worker slice, dispatched by the continuous-mode coordinator per Q-0265)

## Scope

The `ideas/product-forge/` section stub was seeded by PR #66 when the fleet-manager
generated roster became the canonical lane registry and surfaced the lane; it has had
zero idea coverage since. This slice ships the first batch: FOUR captures grounded on
the live lane state, plus the section index, per the honesty guard (Q-0089: only ideas
genuinely believed from grounding actually read; drops recorded below).

## Grounding pins (every load-bearing claim)

- **fleet-manager roster** @ `93d3a4d` (gen #4, generated-at 01:58Z — fresh, inside
  its own >24h kill-switch) · raw fetch 2026-07-11T03:31:30Z. product-forge row:
  WATCH — stalest live-lane heartbeat (~3h36m), HEAD "unmoved since 22:46Z",
  kit v1.7.0 straggler, acked/done 001.
- **product-forge** live HEAD `0a6efe9` (`git ls-remote` 03:31Z; raw fetches +
  read-only blobless clone at that pin, 03:31–03:34Z). Freshest-wins divergence vs
  the roster row: HEAD moved past the row's `77f5231` — but the delta is ONLY the
  manager's ORDER 002 model-attribution relay commit (#16); the lane's own last work
  is still the 22:46Z a11y merge, so the roster's WATCH stands. Read: README,
  control/inbox.md (ORDER 001 games-web + NEW ORDER 002 relay @ 03:26:18Z),
  control/status.md (heartbeat 22:22Z — ORDER 001 done, build ladder fully ticked +
  extensions, PRs #1–#13 merged, owner merge-grant verbatim, Pages deploy dark on
  OA-003, phase-2 blocked on the superbot read-only API),
  products/games-web/docs/phase2-data-api-proposal.md,
  products/games-web/data/schema/game-state.schema.json (v1.0.1, 8 fixed gear slots).
- **superbot-mineverse** live HEAD `01a8b85` (`git ls-remote` 03:34:14Z; raw fetches
  at that pin). Freshest-wins divergence vs the roster row (which says "walking
  skeleton, stage (a) in flight" @ `1120a3b`): the lane is at stages 0/a/b/c DONE,
  (d) prepared, 163 tests, heartbeat 03:25:30Z — read-views deepening merged (9-slot
  gear panel with wear, vault, leaderboards) and ⚑ FLAG 1 asks the bot lane for a
  `mining_snapshot.v1` read relay. The roster row is ~90 minutes stale against a
  fast-moving newborn lane; every mineverse fact in the batch cites the lane HEAD.

## The batch (4 captures, ranked per Q-0259 — games wave + rebuild pace first)

1. `games-web-mineverse-scope-seam-2026-07-11.md` — ORDER 001's "no owning lane"
   premise moved: mineverse now renders the same miner state; probe the seam
   (specialize / reconcile / fold) before phase-2 builds a second live-data path.
2. `read-projection-fanin-fourth-consumer-2026-07-11.md` — cross-links (never
   duplicates) the canonical read-only-API fan-in (status.md note + PR #45 two-rung
   probe) and adds ONLY the two newly-visible facts: mineverse FLAG 1 = a fourth
   convergent consumer; games-web's fallback-to-mock transport makes it a RUNG-1
   committed-feed consumer (its HTTP-endpoint ask can be re-scoped). Concrete
   divergence datapoint: 8 fixed gear slots (games-web contract) vs 9-slot gear
   panel (mineverse) over one dataset.
3. `games-web-live-preview-review-surface-2026-07-11.md` — the owner's review-after
   merge grant makes the dark Pages preview the review surface; post-deploy smoke +
   README preview line, waiting ready for OA-003. Self-serve-class caveat written
   into the capture (verify the INVARIANT at lane HEAD first).
4. `games-web-concept-evidence-pass-2026-07-11.md` — the owner's deferred sim-lab
   evidence pass on the full comic-RPG concept, captured so it never orphans;
   Sequence: after the seam probe, which sharpens its ONE question.

## Honesty-guard drop record (candidates considered and NOT captured)

- **kit v1.7.0 → v1.8.0 straggler upgrade** — maintenance-shaped on a LIVE lane with
  FIVE lane-self-served datapoints behind the verify-first rule; the roster already
  tracks the straggler. A capture would predictably verify-and-park.
- **model-attribution relay** — already ORDER 002 in the lane's own inbox @
  `0a6efe9`; an idea would shadow the manager's own relay.
- **heartbeat-lag / WATCH escalation** — the roster's own gen-#5 escalation path
  covers it; manager surface, not a lane idea.
- **games-web next-surface option board (fishing/market comic-RPG sheets)** — gated
  by the scope-seam ruling (moot under fold/specialize), and the surface inventory
  (fishing/market state shape) is unmeasured from here — "not measured" beats
  invention.

## ORDER 001 (this repo's inbox — model-attribution relay, P3)

Read FIRST per the ritual; arrived mid-setup (manager append `2d9648f`, 03:27:41Z;
forward-merged). Executed in-slice — its three items are verification + a standing
rule, not separate build work, and execution is idempotent per session: (1) template
CONFIRMED already carrying the line — the kit's auto-draft card template
(`bootstrap.py`) emits `📊 Model:` and `.sessions/README.md` lists it among the
required byte-form markers; nothing to add. (2) This session's committed card carries
the real family-level line (below; harness self-report: fable-5). (3) Standing rule
kept. done-when satisfied by this card. Reported `acked=001 done=001` in the
heartbeat.

## Verification (real runs, this tree)

```
$ python3 scripts/check_ideas.py
check_ideas: OK — 288 idea files conform to the README grammar
$ python3 scripts/check_sections.py
check_sections: OK — 13 sections in sync with the lane registry
```

Full `python3 scripts/preflight.py` + `python3 bootstrap.py check --strict` run green
immediately before push (after the heartbeat overwrite). No merge outcome is claimed
here for this slice's own PR — the number is stamped by a follow-up per the #64/#65
precedent.

**📊 Model:** fable-5 · medium · first-batch capture slice (4 idea files + index +
card + claim add/clear + heartbeat; no scripts, no workflows, no proposal —
task-class: bounded section-seeding batch)

## 💡 Session idea

**A newborn lane outruns the registry faster than anything else in the fleet** — the
roster row for superbot-mineverse ("walking skeleton, stage (a) in flight") was ~90
minutes old and FOUR STAGES behind the lane's live HEAD; the same generation's
product-forge row was directionally fine. Freshest-wins already covers the rule, but
the *prioritization* seed is new: when a capture involves any lane younger than ~a
day, the lane-HEAD read is not optional diligence, it is where the idea actually
comes from (both load-bearing captures in this batch — the seam and the fourth
consumer — exist ONLY in the delta between the roster row and the newborn's HEAD).

## ⟲ Previous-session review

PR #68 (sections re-point REMAINDER; squash `78333fb`) + its #69 stamp follow-up —
claims verified against this tree: the superbot-idle `## Cross-links` entry exists as
carded; README § Sections says "registry →" (the one-word fix is live); its
"13 sections in sync" claim re-verified by this session's own check_sections run
(still 13, now with product-forge non-empty). Its handoff aged perfectly: it named
the three empty stubs as first-batch candidates and this slice executed exactly that
for product-forge. One improvement adopted from its card: the dispatched-count-is-a-
hypothesis lesson generalized here — this slice treated the dispatched fan-in
consumer count (three) as a hypothesis too, and the lane-HEAD read falsified it
(four). Workflow improvement carried forward: claim + born-red card pushed as the
FIRST commit (early in-flight signal), which #68's race with #66 showed is worth
doing before any content work.

## Handoff → next wake

Inbox: ORDER 001 acked+done this slice (see above); re-read at HEAD anyway. Ripest
heads this batch plants: the **scope-seam probe** (expiry-aware — it should run
before the manager routes the batched providing ORDER or games-web phase-2; both
could move any wake) and the **fourth-consumer fan-in fact**, which the :30 sweep
should relay into the batched-ORDER routing decision. superbot-idle and
superbot-mineverse sections are still empty stubs — mineverse especially is now
proven rich grounding (163 tests, live contracts, two bot-lane FLAGs) for a sibling
first batch; consider adding a mineverse-section Cross-links row back to this batch's
seam/convergence captures when that section seeds (by-link, PR #17 grammar).
Telemetry residue: this seat's hook-born guard-fires appends left uncommitted for the
telemetry lane per the PR #32/#58/#62 precedent.
