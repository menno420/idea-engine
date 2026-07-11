# Session — single-pass probe: venture-lab self-landable-merge-path

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-11 (worker slice, dispatched by the coordinator
> under continuous-chaining mode per Q-0265)

## What this session did

Single-pass probe (battery v0, no panel triggers) of
`ideas/venture-lab/self-landable-merge-path-2026-07-10.md` — the section's LAST
unprobed head (captured in PR #14: at capture the lane's PR self-merge was walled,
0 required checks, no merge-on-green workflow).

Verify-first at live lane HEAD `9b504e8` (ls-remote + raw fetches 06:02–06:06Z):
the head MUTATED, and got CHEAPER. (a) No merge-on-green workflow is live —
`.github/workflows/` carries only `substrate-gate.yml`; five candidate enabler
filenames all 404 at `main`. (b) BUT the kit v1.9.0 STAGED enabler exists in the
lane's own tree (`.substrate/ci/auto-merge-enabler.yml` fetches 200) — the lane
upgraded to kit v1.9.0 since capture, so the committed file the capture priced is
now one `adopt --wire-enforcement` from live; `automerge.branch_patterns` still
the wrong `["claude/*"]` default this repo fixed in PR #55. (c) The classifier
wall DEEPENED: the lane's `docs/PLATFORM-LIMITS.md` @ `9b504e8` records THREE
terminal denials on its PR #15 — REST self-merge AND the auto-merge ARM from a
child seat — with the proven landing path being a coordinator-seat merge under
the owner's genuine user turn; and the owner's 2026-07-11 branch-protection
statement (substrate-gate required + auto-merge) is explicitly UNVERIFIED from
any agent seat.

Verdict: **parked(build-direct — lane wiring slice, owner-click-gated)**. One
venture-lab PR (adopt --wire-enforcement + branch_patterns survey/fix +
PLATFORM-LIMITS annotation) + two verify-or-complete owner toggles ("Allow
auto-merge" ON, substrate-gate required — stated explicitly in the probe for the
fan-in) + one genuine-turn bootstrap merge. NOT park(routed): the kit template
work is already done upstream (v1.8.0 planted the enabler, v1.9.0 validates
required_context); the kit-shaped residue is already captured at
`ideas/substrate-kit/enabler-card-status-guard-upstream-2026-07-11.md`
(cross-linked in the probe). Nothing evidence-shaped for sim-lab; no proposal.

**SECTION MILESTONE: venture-lab 4/4 probed-or-parked** — the FOURTH complete
section (after superbot-games, trading-strategy, and superbot-mineverse @ #107).

Files touched: the idea file (state flip + probe report append),
`ideas/venture-lab/README.md` (index bullet), this card, `control/status.md`
(heartbeat; ⚑ OWNER-ACTION block preserved; venture-lab fan-in updated with the
section milestone + the two-toggle verify ask routed to the lane's surface),
claim `control/claims/probe-venture-lab-self-landable-merge-path.md` deleted per
convention.

Claim: fast-laned first as PR #106 (merged by the enabler in 27s),
`control/claims/` re-read at origin/main HEAD after the merge (one sibling claim
live: fix-stop-hook-telemetry-exemption — disjoint scope, shared-heartbeat
overlap only), claim file deleted in this PR.

**📊 Model:** fable-5 · docs-only (one probe append + state flip + index flip +
heartbeat + card; no code)

## 💡 Session idea

A lane that vendors the kit can have its fix already sitting IN ITS OWN TREE
without knowing it: the staged-vs-live seam (`.substrate/ci/` vs
`.github/workflows/`) means verify-first must probe BOTH paths — the live-path
404 alone would have priced this head as "write the workflow" when the honest
price was "run one adopt command". Staged artifacts are a distinct
verify-first surface class; check them whenever a capture prices committing a
file the kit templates.

## ⟲ Previous-session review

PR #104 (venture-lab revenue-ingestion-owner-relay probe): its handoff named this
exact head ripest-next ("last unprobed head in the section") — the chain held,
the dispatch matched the handoff. Adopted from it: verify-first at live lane HEAD
before probing (re-proven — the head mutated cheaper via the lane's own kit
upgrade), the recommendation-line format `**Recommendation: park** — build-direct
(...)` that the lint's LEGAL_RECOMMENDATION_RE actually accepts (qualifier in the
rationale, never in the token), card complete BEFORE push so the enabler arms at
open, and claim→re-read→build (PR #106 ran clean; one disjoint sibling claim).
Its "expect the mineverse companions heartbeat reconcile" note resolved: sibling
#107 (heartbeat-ladder) landed at this session's setup time and its status
overwrite was the base this slice's heartbeat carried forward.

## Handoff → next wake

venture-lab is CLOSED as a probe surface (4/4) — nothing left but re-harvest when
the lane moves; the manager's sweep now holds both venture-lab asks (ledger slice
ORDER-worthy @ #104's fan-in; the two-toggle verify + wiring slice @ this one).
Ripest elsewhere: the stop-hook telemetry-exemption sibling claim is still live
(its build PR was in flight at dispatch); gba-homebrew's three-head build-direct
queue still races the EAP window (ends 2026-07-14). Watch: if the manager routes
the venture-lab wiring ORDER, the lane's wiring PR should verify the
required-context count live — a zero count with the toggles claimed done is the
first thing to check.
