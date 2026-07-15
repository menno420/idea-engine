# Session — PROPOSAL 066: kill-clock anchor vs owner-gated funnel onset — the T+14 window measures click latency, not viability, once the funnel wires late (venture rotation, round 13 second slot)

> **Status:** `in-progress`
> **Model/time:** fable · 2026-07-15T05:40:25Z (Ideas Lab worker slice — draft the
> round-13 VENTURE rotation slot proposal under standing owner ORDER 003/004;
> round 13 opened at fleet backlogs with P065 (#428, merged 05:06:07Z). Card
> born in-progress as the designed gate hold; flips complete in this PR's
> final commit.)

- **📊 Model:** fable-class · high · idea/planning

## Scope

Draft a genuinely new sim-shaped idea for the VENTURE rotation slot, round 13
SECOND slot, under standing owner ORDER 003 (continuous pipeline) and ORDER
004 rule 3 ("Rotate lanes deliberately: fleet backlogs → venture's
book/product space → game mechanics → COMPLETELY UNRELATED domains (I want
those too)"). Round 13 opened at fleet backlogs with P065 (#428), so the
venture slot is next; the slot's own spacing-4 history (P018, P022, P026,
P030, P034, P038, P042, P046, P050, P054, P058, P062 → P066) confirms, and
the slot's half-alternation read from the actual sequence (P018 books →
P022/P026 trading → P030 books → P034 trading → P038 books → P042 products →
P046 books → P050 products → P054 books → P058 products → P062 books) puts
round 13 on the PRODUCTS half.

Harvest source: venture-lab read FIRSTHAND this session (public shallow
clone, `git log -1` = `520bdfca71ca4f119808d1098cd4ecf7fc6e6732`, fetched
2026-07-15T05:31Z) — the products lane's committed kill-rule measurement
plan, `docs/launch/stripe-webhook-test-kit/LAUNCH-LOG.md`, which commits BOTH
horns of an unpriced incoherence in one document: the kill window is
CALENDAR-ANCHORED ("signal = ≥1 organic sale … within 14 days of the
**listing going live**") while the evidence channel is CLICK-GATED ("BASE
CASE is **0 sales** until a distribution channel is wired … still
owner-gated"). The clock measures owner click latency as much as product
viability. P050 → V061 priced the DIAL (T ∈ {7, 14, 30}) on a stationary
intrinsic-demand model with NO exposure channel, from a SECONDHAND pin (its
venture read was denied that session, verbatim error recorded) — and its own
break-note (a) names "stationarity" as the most-likely flip. This head holds
the dial FIXED at the committed 14 and prices the ANCHOR (listing-live vs
funnel-live vs funnel-live-capped-at-the-committed-30-day-signal-window)
under pinned traffic shapes read off the lane's own committed channel
adjectives (`docs/launch/distribution-channels.md`: "spiky … one shot" /
"long-tail SEO … slow-burn" / "near-zero … but free").

The head: **a calendar-anchored evidence deadline whose evidence channel is
gated on a separate un-synchronized click measures the click, not the
product** — false-kill probability is (1−q)^N with N the funnel visits that
land INSIDE the window, so late wiring truncates N (at the decision cell the
same viable product flips from a 0.145 false-kill risk at τ = 0 to a 0.547
coin flip at τ = 13, and to CERTAIN false kill at τ ≥ 14, the LAUNCH-LOG's
own committed base case) — while anchoring the window at funnel-live and
capping at the lane's OWN committed 30-day signal window (A-CAP30) restores
exact τ-invariance for all τ ≤ 16 with slot occupancy bounded at 30 days,
zero new constants. Three hand-provable structure theorems ride as gates:
ANCHOR INVARIANCE, SPIKE STEP, CAP-30 EQUIVALENCE + BOUNDEDNESS.

Deliverables this slice: this card (born-red first commit), the claim file,
`ideas/venture-lab/kill-clock-anchor-truncated-exposure-2026-07-15.md` + the
`ideas/venture-lab/README.md` index row, the `control/outbox.md` PROPOSAL
066 append, and housekeeping (one terminal claim prune — the P065 drafter,
PR #428 verified merged at live GitHub 2026-07-15T05:06:07Z this session
before deletion). Seeds 20261580–583 — strictly above this tree's high-water
20261570 (P065's registration, re-swept this session at HEAD 85114c5) and
sim-lab's genuine high-water 20261566 (V077's registration, re-swept
READ-ONLY at origin/main 71337e2 this session); the gap 20261571–579 is
deliberately left unallocated as the in-flight VERDICT 078 allocation buffer
(V078 runs sim-lab-side on P065's world and is allocating from 20261571 per
the coordinator relay — not yet visible in either tree at the pins above;
disclosed, not hidden).

## Constraints honored

- control/inbox.md untouched (manager-written); control/status.md untouched
  (no heartbeat housekeeping in this slice's scope).
- control/outbox-archive-2026-07-14.md untouched (rolled archive, terminal).
  Outbox append-only (appended via shell, never loaded into an editor); no
  renumbering; all timestamps from real `date -u`.
- Claim prune is TERMINAL-only: the deleted claim's PR verified merged at
  live GitHub (mcp pull_request_read: #428 merged 2026-07-15T05:06:07Z,
  merged_by github-actions) before deletion; zero open PRs at drafting
  (collision check clean).
- venture-lab and sim-lab READ-ONLY: fresh shallow clones this session
  (venture-lab @ 520bdfc for the FIRSTHAND harvest; sim-lab @ 71337e2 for
  the dedup ledger + seed sweep); nothing there touched — this repo edits
  no other repo (Q-0260).
- Seed sweep boundary-aware at drafting HEAD 85114c5: this tree maxes at
  genuine 20261570 (P065's allocation); sim-lab @ 71337e2 maxes at genuine
  20261566 (V077's registration) — larger standalone numerals (20261833,
  202670087, 2026964142) match the recorded discrimination rule from the
  P065 card's review remark: standalone 2026-prefixed numerals inside
  results-quoting text are data, not seeds.
- The `📊 Model:` line above uses the kit's taught three-field payload
  (the P064 fix, carried forward).

## 💡 Session idea

(placeholder — filled at card flip, per the born-red gate discipline)

## ⟲ Previous-session review

(placeholder — filled at card flip)
