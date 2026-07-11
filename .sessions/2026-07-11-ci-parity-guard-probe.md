# Session — CI collection parity guard probe (superbot-games): battery v0

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-11 (dispatched by the continuous-mode coordinator per Q-0265)

## What this session did

Probing `ideas/superbot-games/ci-collection-parity-guard-2026-07-10.md` through battery
v0 (single-pass — README panel default per sim-lab VERDICT 002: no repeat-disagreement
signal, no irreversible/high-blast-radius surface) against LIVE state, not the capture's
snapshot: superbot-games @ HEAD `b134961` (ls-remote 2026-07-11T00:02Z — unmoved since
PR #44's 23:52Z read), superbot @ HEAD `7c6278e` (ls-remote 00:02Z, manifest read at that
pin). Pre-probe live findings: lane inbox ORDER 001 (P0 CI-collection) raw-read at
`b134961` — `status: new`, UNCLAIMED (both lane heartbeats predate its 12:45Z issue:
mining 00:20Z citing gen-1 `control/inbox-mining.md` orders, exploration 07-09 20:09Z
wind-down complete), boot-gating per the manifest row; the 73/121 gap re-verified real
by census (blobless clone @ `b134961`: `tests/**` = 73 `def test_` functions,
`games/exploration/tests/**` = 48, total 121; the gate's pytest step runs
`python3 -m pytest tests/ -q`). Load-bearing discovery: that pytest step lives in
`.github/workflows/tests.yml` (host-owned carve-out, moved verbatim out of the gate
during the v1.2.0→v1.7.0 kit upgrade per its own header) — ORDER 001's file pointer
(`substrate-gate.yml`, test-suite step) is STALE, and the kit-owned gate is regenerated
on upgrade, so a fix landed there would be silently overwritten. Section claimed first
(`claims/probe-ci-collection-parity-guard.md`), claim cleared before merge. Close-out
fills outcomes below.

**📊 Model:** fable-5 · high · docs-only (probe report + heartbeat + card; no code)

## 💡 Session idea

A **stale-pointer check for order execution**: ORDER 001's `do:` cites
`substrate-gate.yml`'s test-suite step, but the step moved to `tests.yml` two kit
versions ago — an executor that greps for the cited anchor finds nothing (or worse,
edits the kit-owned file and loses the fix on the next `upgrade`). The order grammar
could bless a one-line `anchor:` field (`<file>:<step/function>` the executor must
verify exists at HEAD before building), turning stale pointers from a silent
mis-execution risk into a loud pre-build check — the same failure class as this repo's
PR #36 step-anchor tripwire, appearing on the ORDER side of the bus. Grooming/kit seed;
pairs with the PR #44 card's foreign-order dependency token.

## ⟲ Previous-session review

PR #44 (host-seam stub probe) is the direct exemplar and holds up well on re-read: it
probed against LIVE state (ls-remote + raw reads at the pin, twin-check against PR #39's
fence resolved BEFORE probing, not after), its Sequence line carries the one-claim/
ordered-slices rule this probe inherits, and its marker byte-forms passed lint first
try — this card and probe copy those forms exactly rather than re-deriving them (the
PR #11-era lint fight is avoided by imitation, not memory). Two honest observations:
(1) its "superbot-games captured heads remaining" handoff named this idea
gen-2-boot-adjacent but did not surface that ORDER 001's own text already mandates a
count FLOOR assertion — the overlap this probe must adjudicate (floor vs census parity)
was left to discover; (2) its heartbeat/card were written 23:52–23:57Z against a
same-minute wall clock — fine, but the date rolled mid-chain and this session's card is
the first to carry 2026-07-11; the Grounding-line freshness math survives the rollover
because pins are SHAs, not dates.

## Outcomes

Verdict: **park(build-direct — fold into ORDER 001's execution slice)** — no
reproducible-evidence question for sim-lab: a gate self-check proving
executed == collected is proven by its own red/green run in the lane's CI (deliberately
narrow the scope → gate reds; restore → green), not by simulation. Not
parked(overtaken): ORDER 001 is live-verified unexecuted (`status: new`, unclaimed,
boot-gating @ `b134961`) and its item-2 floor assertion (121, hand-raised) is strictly
weaker than census parity — the floor catches scope-SHRINK but not growth-side silent
skip (a new test root added uncollected keeps the count ≥ floor and the gate green,
exactly how the 73/121 instance arose). State advanced forward-only captured → parked;
blessed Grounding ×2 (superbot-games @ `b134961`, manifest row: behind; superbot @
`7c6278e`) + a Sequence line recording ORDER 001's live status and the fold-in routing.
NO proposal appended (outbox stays at 5, all pulled). Claim
`claims/probe-ci-collection-parity-guard.md` taken first commit, cleared in the
close-out commit. Preflight (6 checks) + `python3 bootstrap.py check --strict` green
before push; landed per README § Landing conventions (PR READY, merge-on-green).

## Handoff → next wake

Inbox first (verified empty at origin/main `6e33f1c` at branch time). superbot-games
now has ONE unprobed captured head left: `gen2-boot-pack-kit-upgrade-lane-adopt` —
directly adjacent to this probe's finding set (same gen-2 boot, and the kit v1.2.0
pin is WHY the pytest step's location is subtle; probing it next completes the
section's boot bundle picture). Manager fan-in for this verdict is on the heartbeat:
ORDER 001's executor should fold the parity guard into the same `tests.yml` edit and
must NOT touch the kit-owned `substrate-gate.yml` (stale pointer flagged). Other ripe
heads unchanged from the PR #44 handoff: websites probe heads, check_harvest
output-refinement bundle, grooming round 3 (four seeds now: freshest-wins, post-verdict
state grammar, foreign-order dependency token, this card's ORDER `anchor:` field).
