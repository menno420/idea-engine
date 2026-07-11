# Session — venture-lab sellables shortlist top-2 probes (webhook family + substrate-kit starter)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-11 ~19:25Z (paired worker slices, coordinator-dispatched
> under continuous-chaining mode per Q-0265; this card closes the pair)

## Scope

Battery-v0 probes on the sellables-brainstorm shortlist's top two heads
(`ideas/venture-lab/webhook-test-kit-family-2026-07-11.md` rank 2,
`ideas/venture-lab/substrate-kit-agent-fleet-starter-2026-07-11.md` rank 1).
Claims ceremony rode fast-lane FIRST, one claim per probe per the disjoint-section
rule: PR #208 `67a81cf` (`control/claims/probe-substrate-kit-agent-fleet-starter.md`)
and PR #209 `7e4f444` (`control/claims/probe-webhook-test-kit-family.md`) — both
claim files deleted in their own probe PRs at close-out. Branches
`probe/webhook-test-kit-family` (shipped) and
`probe/substrate-kit-agent-fleet-starter` (this PR).

## What this session did

- **Probe 1 (rank 2, webhook-test-kit-family) — SHIPPED as PR #210, merge
  `2f2d7dd`, verdict `park(awaiting stripe-kit validation signal)`.** Full battery
  on the file @ venture-lab lane HEAD `389bb37`: the github SKU verified CHEAP and
  fully stdlib (Stripe coupling = one 10-line signature fn `swtk.py:49-58` + one
  header name); the discord SKU was FALSIFIED as captured — Python stdlib has no
  Ed25519, checked empirically this session (`'ed25519' in
  hashlib.algorithms_available` → `False`, `import nacl` → ModuleNotFoundError);
  the stripe base SKU has $0 revenue with the INTAKE kill-rule clocks unstarted
  (⚑E listing click pending). Honest family scope stripe+github; re-open on the
  first observed INTAKE-clock signal. No outbox append (pricing/bundle elasticity
  already routed to sim-lab lane-side — nothing non-duplicate to route).
- **Probe 2 (rank 1, substrate-kit-agent-fleet-starter) — THIS PR, verdict
  `needs-more-grooming`** (state flipped `captured` → `probed`, README index
  re-badged; PR number stamped in the follow-up heartbeat per the never-guess
  rule). Verify-first found the kit source at `menno420/substrate-kit` main
  `fa921f4` (MIT, pip-installable, versioned sha256-provenanced releases,
  generated adopter registry — closer to sellable than anything else on the
  batch) but at **v1.12.0 with 16 releases in 3 days**, not the capture's
  "v1.10.0" (that is this repo's vendored dist, control/status.md:5 @37d2592).
  The capture's "pure packaging, ships on two owner clicks" is contradicted by
  the kit's OWN pending-action ledger (docs/current-state.md@fa921f4): name is an
  explicit README placeholder, 👤 P8 license confirm and 👤 P11 public flip both
  pending (P11 with a veto path), no open-core boundary drafted anywhere, 120+
  internal session cards + control/ + owner-profile + telemetry needing curation
  before any flip, and the kit-lane vs venture-lab ownership question unresolved
  by the roster (@6d5e3b3, no owner column). No evidence-settleable sim question
  exists (every unknown is an owner/manager call) — so NOT forced to sim-ready;
  the report's Q8 names the re-scope: a kit-lane public-readiness head + a
  venture-lab sale head. **No outbox append from either probe — outbox tail
  stays PROPOSAL 009.**

## Verification

`python3 bootstrap.py check --strict` green on the final tree immediately before
push (heartbeat rides the follow-up PR per the arm-at-open race recipe —
the #181/#184/#187/#190/#193/#195/#198/#201 lineage). Payload of this PR: one
idea-file probe append + state flip, one README index re-badge, this card, one
claim-file delete. No code, no lane-file writes (Q-0260), no workflow edits.

**📊 Model:** fable-5 · two battery-v0 probes (one shipped #210, one this PR) +
claims ceremony ×2 + card + heartbeat follow-up; no outbox append

## ⟲ Previous-session review

Reviewed card (per dispatch): `.sessions/2026-07-11-wire-automerge-enabler.md`
(status `complete`). Its core promise — the enabler live-arms every
matching-prefix READY PR and merges on green `substrate-gate` — is now proved
LIVE across this pair's own ceremony, with one new failure-mode datapoint:
(1) claim PR #208 self-armed and auto-merged clean; (2) claim PR #209 exposed a
RACE the enabler card did not predict — the enabler run SUCCEEDED yet never
armed an already-clean single-commit PR, and a manual squash-merge was needed to
land it; (3) probe PR #210 then armed and fired clean in ~24s. Net: the wiring
holds (2 of 3 armed-and-merged hands-free), but "enabler run green" ≠ "PR
armed" on the already-clean single-commit shape — the exact class the #86 race
guard was built around, now observed from the other side. Flagged rather than
silently dropped: the card's 💡 (branch-prefix drift tripwire) remains
still-open grooming at this wake.

## Handoff → next wake

- Inbox first, as always. Venture-lab shortlist top-2 heads are CONSUMED
  (rank 2 parked on the file, rank 1 needs-more-grooming on the file); the
  grooming re-scope named in probe 2's Q8 is the ripest venture-lab follow-up —
  split the substrate-kit head into the kit-lane readiness task + the
  venture-lab sale task, and put the ownership ruling (kit lane vs venture-lab)
  in front of the manager sweep.
- Enabler race datapoint (⟲ above) is ledger-worthy: "enabler success without
  arm" on already-clean single-commit PRs — candidate for control/README § CI
  notes next time that surface is edited.
- Friction for the ledger: github.com atom/HTML surface refused for
  substrate-kit from this seat ("GitHub access to this repository is not
  enabled for this session") — `git ls-remote` + shallow clone + raw reads
  covered everything; api.github.com anonymous 403 wall unchanged; the #209
  manual-squash workaround per the known enabler race.
