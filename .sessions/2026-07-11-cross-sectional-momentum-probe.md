# Session — cross-sectional momentum family probe (trading-strategy): battery v0

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-11 (dispatched by the continuous-mode coordinator per Q-0265)

## What this session did

Probed `ideas/trading-strategy/cross-sectional-momentum-family-2026-07-10.md` (seeded
by PR #10 as the first post-holdout hypothesis class) through battery v0 — single-pass
per the README panel default (sim-lab VERDICT 002): no ambiguity signal, no
irreversible surface. Section claimed first
(`claims/probe-cross-sectional-momentum-family.md`), claim cleared in the close-out
commit. Probe order was expiry-aware by the book: the capture's "Why now" named a
window ("the lane goes idle the day P5 completes"), so live-state recon ran FIRST.

Live verification decided the verdict, again. Lane HEAD `6799a4c` (ls-remote
2026-07-11T01:08:54Z, ahead of the capture pin `e713abb`): the lane did NOT go idle
after spending the holdout — on the same day (2026-07-10) it pre-registered Research
Round 2 (lane PR #46, `8d0270f`, BINDING, merged before any Round 2 number existed)
and executed the capture's exact hypothesis class as R3 `xsec_momentum` (lane PR #49,
merge `9b13b8a`): first portfolio-level lane, rank-by-trailing-return top-k
equal-weight over the 9 cached daily instruments, rebalance 21 bars, vs equal-weight
basket B&H — 3 KEEP (dev-candidates only: L=63/k=2 Sharpe 1.627, L=63/k=3 1.631,
L=252/k=3 1.277, basket 1.147) / 3 KILL (L=126 both arms, L=252/k=2), then closed the
round (PR #50). Promotion is CLOSED by the round's own banner: any path past
dev-candidate is a NEW owner-gated pre-registered protocol on post-2026 data —
"agents may flag it as a proposal but must not schedule, initiate, or run it."
P5 holdout outcome confirmed at the same pin: SPENT 2026-07-10 (run stamps
2026-07-10T1647Z), 0 of 13 clears the ORDER 007 significance bar (primary
donchian×AAPL t = 0.02 → RULE-PASS candidate, NOT a finding); ORDERs 001–008 all done,
no order newer than 008. Manifest row @ superbot `4ccb631` still says "PARKED GREEN …
holdout SEALED … ORDER 007 in flight; kit v1.1.0" — staleness datapoint 13; freshest
wins, all citations from the lane's own tree.

**📊 Model:** fable-5 · high · docs-only (probe report + header lines on the idea
file, 1 README index row, card, heartbeat; no code)

## 💡 Session idea

**The lane-self-served pre-probe check has now fired twice in ~24 h and deserves its
round-4 encoding.** Websites built bullet #11 ~19 min after harvest (PR #49 card);
here trading-strategy pre-registered AND executed a captured hypothesis class within
hours of its capture merging (capture PR #10 ~20:0xZ; lane pre-reg + R3 same day).
The convergent shape: the most competent lanes consume their own obvious next moves
faster than the capture→probe cycle turns, so a capture aimed at a LIVE lane's
next-step slot should be probed with the presumption of self-serve — the round-4 seed
(PR #49 card 💡) is confirmed by a second, independent, cross-section datapoint. Note
the silver lining worth keeping in the encoding: independent convergence (capture
predicted exactly what the lane then did) is evidence the capture heuristic aims
true, not wasted work.

## ⟲ Previous-session review

The round-3 grooming slice (PR #50, merge `097267c`) holds up in live use — this
probe exercised three of its seven freshly-encoded rules and all three earned their
place: expiry-aware probe ordering put the lane-HEAD check first (and it flipped the
verdict), freshest-wins resolved the manifest-vs-lane divergence cleanly (row a full
program-phase-plus stale — datapoint 13 on the same trading-strategy row as
datapoints 5–6), and the producer-reachability bullet gave Q4 its sharpest line (the
missing producer for the residual OOS question is time itself plus an owner
signature). One honest observation: the round card's skip list deferred the
lane-self-served pre-probe check to round 4 as a harvest-side twin of expiry-aware
ordering — this session shows it is not harvest-specific (this was a seeded capture,
not a harvested bullet); the round-4 encoding should cover both arrival paths. Claim
discipline inherited unchanged (claim first commit, cleared at close-out); PR #50
itself needed no claim per the PR #21 root-docs precedent, correctly.

## Outcomes

Verdict: **park** (state `parked(overtaken-by-events — …)`) — the lane pre-registered
(`8d0270f`) and executed (`9b13b8a`) the exact family before this probe ran; every
path beyond dev-candidate is an owner-gated new protocol on post-2026 data. NO
proposal appended — outbox tail verified at PROPOSAL 005; Q7 rules the evidence path
is the lane's OWN pre-registered research/paper machinery, not sim-lab (a sim-lab
re-backtest of the same dev bars would carry weaker provenance than the lane's
pre-registration, and the open question is owner-reserved — routing it would
route around an explicit OWNER-ACTION). Blessed header lines added forward-only:
Grounding @ trading-strategy `6799a4c` (manifest row: behind) + pin annotation
(capture pin `e713abb`; manifest divergence detail) + Sequence (constraint met,
slot consumed). Section index row updated. Preflight (6 checks) +
`python3 bootstrap.py check --strict` green before push; landed per README § Landing
conventions (PR READY, merge-on-green). Sibling in flight at dispatch time: websites
review-queue probe — status.md conflict, if any, reconciled forward-only keeping both
sides' facts.

## Handoff → next wake

Inbox first (verified empty at origin/main `097267c` at branch time).
trading-strategy section state after this slice: post-holdout-reseal
parked(overtaken) @ #25 · cross-sectional-momentum parked(overtaken) @ this PR ·
remaining captured heads: wake-resilience-fresh-session-rebind (gated on the lane's
⚑ (b) env setup-script click — check the ⚑ list at probe time; it was still open @
`6799a4c`) and kit-upgrade-oldest-pin (likely MOOT: lane heartbeat @ `6799a4c` reads
"kit: substrate-kit v1.7.1 — upgraded from v1.7.0 via PR #44" vs the capture's
v1.1.0 premise — probe it next for the cheap park, same self-served shape). For the
manager: trading-strategy needs NO providing ORDER — the lane self-serves; the only
live owner surface is its own standing note (follow-on research = owner-gated
proposal) and its ⚑ (b)/(c)/(d) items. Round-4 grooming seed strengthened: the
lane-self-served pre-probe check now has two datapoints across two sections and two
arrival paths (harvested bullet, seeded capture).
