# Session — single-pass probe: pokemon-mod-lab patch-only-egress-doctrine (section closer)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-11 ~08:25Z (worker slice, dispatched by the
> continuous-mode coordinator per Q-0265)

## Scope

The #134 card's handoff named this exact head "the section closer":
`ideas/pokemon-mod-lab/patch-only-egress-doctrine-2026-07-10.md` — the section's LAST
open head, window-adjacent to the 2026-07-14 sitting. Single-pass battery v0 (no panel:
the slice is one doctrine paragraph + an advisory-first lint, reversible; the
high-blast-radius event it governs — actual IP egress — is what the doctrine defers, so
the panel trigger reads on the egress decision, not on encoding the ban). Section
claimed first — `control/claims/probe-pokemon-mod-lab-patch-only-egress.md` landed on
main via fast-lane PR #135 (merged 08:08:29Z by the enabler) before any build work;
claims dir re-read at the recut: ONE sibling claim live
(`probe-substrate-kit-heartbeat-behind-pair`, PR #136 — disjoint section,
shared-heartbeat overlap only). Claim deleted in this PR.

## Verify-first record (DARK-lane recipe, three layers, one pin each)

- **The lane is DARK** — the standing wall, verified three ways same-day by the #131
  probe (raw 404 ×2, `git ls-remote` auth wall, MCP scoped here;
  `.sessions/2026-07-11-pokemon-playtest-kit-probe.md`), not re-paid per
  docs/CAPABILITIES.md. All lane facts roster/manager-relayed.
- **fleet-manager pinned at `1afca50e171a33591f8481f0ac837b989c280425`** (ls-remote
  2026-07-11T08:08:14Z — the SAME pin the #131/#134 probes read, third consecutive
  read; blobless clone, `git show HEAD:<path>` per file). Surfaces: playbook R22 ·
  capabilities visibility recipe · dispatch-log visibility-saga (flip → re-public for
  the auto-merge toggle → counter → re-flip; "private repos cannot enable the
  auto-merge toggle at all" on this plan) · fm status line 698 ("pokemon-mod-lab:
  ORDER 003 (visibility verify) landed 12:56Z … unconsumed" at roster gen #1) ·
  owner-queue items 3–4 (item 4 cites **Q-0262.7 correctly** — the mislabel is on
  roster/status/parallel-run only) · review-queue pokemon#8 (sha1 chain
  `eec6d6af` → … → `805aeaee` manager-verified; lane CI = `rom-builds.yml` prints
  sha1, asserts nothing) · night-review Q16 + remediation item 1 ·
  `docs/proposals/instructions/game-lab.md` (IP RAILS — header verbatim "PROPOSED,
  not deployed").
- **superbot router live at HEAD `58040c6`** (raw fetch): Q-0260 rule 3 verbatim
  ("pokemon-mod-lab went private 2026-07-10" — read-side doctrine) and Q-0262.7
  verbatim ("Pokemon concept pick = QoL+ … takes effect when the games program boots
  post-core"); the #134 Q-0266-mislabel caution honored — this probe cites Q-0262.7.
- **substrate-kit CHANGELOG at live HEAD `be72c09`**: the night-review's prescribed
  repo.private gate step ("Builder: the substrate-kit lane … ships in v1.8.0") is
  NOT shipped through v1.10.0 — zero visibility-guard or IP-lint entries.

## Verdict

`patch-only-egress-doctrine` → **parked(build-direct — lane doctrine slice)**. The
capture's core premise ("nothing visible encodes the boundary as doctrine") is
THREE-QUARTERS OVERTAKEN — read-side (Q-0260.3), verification-side (R22 + lane ORDER
003), and the lane's own pre-flip "no exceptions PRIVATE / never publish" rail all
exist readable — and ONE QUARTER INTACT: the egress PROTOCOL (patch-only BPS/UPS
against a named clean base) is encoded nowhere deployed, and the machine guard is a
verified kit-side debt. Sharpest scope correction from grounding: the tripwire must be
EGRESS-SCOPED, never tree-wide — the tree carries the vendored decomp by design
(night-review Q16), so the game-lab draft's tree-wide blob lint is born-red here.
Egress-planning premise honestly WEAKENED: the planned playtest is IN-REPO (owner-queue
item 3's WHERE is the private repo; no bytes leave), no release path exists by design —
the 2026-07-14 sitting matters as the event most likely to GENERATE the first share
ask, in the same sitting that publishes Lumen Drift publicly. One lane PR: README
egress paragraph (citing Q-0262.7 + the flip) + `repo.private == true` CI assert
(makes ORDER 003's per-session duty structural) + egress-scoped ROM/blob lint. Routed
via the heartbeat fan-in with the 2026-07-14 owner-sitting bundle — same routing
decision as the playtest-kit park; one manager ORDER could carry both. No outbox
proposal (nothing sim-shaped — doctrine text and a lint are proven by their own
red/green).

## SECTION MILESTONE — pokemon-mod-lab complete

All 4 heads probed-or-parked: post-eap-playtest-kit parked(build-direct) @ #131 ·
qol-plus-wave-2-option-board + ruling-sync-first-boot parked(overtaken-by-events) @
#134 · patch-only-egress-doctrine parked(build-direct) this PR — the **SIXTH fully
probed-or-parked section** (after superbot-games / trading-strategy /
superbot-mineverse @ #107 / venture-lab @ #110 / superbot-idle @ #116).

## Verification (real runs, this tree)

Full `python3 scripts/preflight.py` (all 8 checks) + `python3 bootstrap.py check
--strict` run green immediately before push, after the heartbeat overwrite (outputs
quoted in the PR). Telemetry residue: this seat's hook-born `.substrate/` appends left
uncommitted for the telemetry lane per the PR #32/#58/#62 precedent.

**📊 Model:** fable-5 · docs-only single-pass probe (probe append + state flip +
Grounding/Sequence headers + section index re-badge + card + heartbeat + claim
add via #135/clear via this PR; no scripts, no workflows, no proposal)

## 💡 Session idea

**A capture aimed at a catastrophic-failure class should be probed against the
LESSON'S full encoding map, not just its own premise:** this head believed nothing
encoded the private-flip lesson; grounding found the lesson already encoded in three
of four layers (ruling, playbook rule + lane order, lane rail) with only the egress
protocol missing — and found the prescribed MACHINE guard silently unshipped two kit
releases after its "ships in v1.8.0" commitment (night-review remediation item 1 vs
kit CHANGELOG @ `be72c09`). Cheap convention: when a remediation list assigns a
builder + release ("ships in vX"), the assignee's CHANGELOG is the verify surface —
a one-line check any later probe can run; unshipped commitments should surface as
loudly as unconsumed ORDERs. Natural home: fm's night-review follow-up sweep;
evidence pinned in this probe's report.

## ⟲ Previous-session review

Reviewed: `.sessions/2026-07-11-pokemon-verify-park-pair.md` (PR #134, squash
`454a1db`) — the actual newest card at my read, and the dispatch briefing agreed this
time (no briefing-lag; the #131/#134 pattern of aging handoffs did not recur).
Verified against the tree: both verify-and-park notes exist with
`parked(overtaken-by-events)` state lines, the section README rows are re-badged, its
claim file is gone from control/claims/, and its heartbeat landed with the ⚑ block's
BOTH 2026-07-14 items preserved. Adopted from it: (a) the Q-0262.7/Q-0266 mislabel
caution — this probe cites Q-0262.7 and found corroboration (fm owner-queue item 4
labels the pick Q-0262.7 CORRECTLY; the mislabel is confined to roster/status/
parallel-run); (b) same-pin evidence carry-over (fm unmoved at `1afca50` across
#131 → #134 → this slice — three probes, one pin, zero re-derivation); (c) its
handoff's exact next-head call ("probe patch-only-egress before the sitting; after
it, the section is fully probed-or-parked — would be the SIXTH complete section") —
executed as specified, milestone confirmed real.

## Handoff → next wake

- **Routing watch:** the pokemon-mod-lab fan-in now carries TWO build-direct parks on
  the SAME 2026-07-14 sitting bundle (playtest kit + egress doctrine) — one manager
  ORDER could carry both; if the :30 sweep declines, re-probe the routing, not the
  ideas.
- **Kit-lane evidence line (small, rides the existing bundle):** the night-review's
  repo.private gate is a verified unshipped kit commitment (CHANGELOG @ `be72c09`) —
  a fifth line for the SAME kit-lane ORDER the #132/#134 slices already flagged;
  evidence pinned in this probe's report, do not re-derive.
- **Section state:** pokemon-mod-lab is COMPLETE (6/13 sections fully
  probed-or-parked). The sibling substrate-kit heartbeat-behind pair (claim PR #136)
  was in flight at this write — expect its heartbeat reconcile; merge ⚑ items, never
  clobber.
- Guard recipe: DARK-lane verify path unchanged (blobless clone fm, read at ONE
  pinned HEAD, cite fm@sha per fact; anonymous api.github.com 403s via the proxy —
  MCP or git transport only); for egress-class heads, the verify surface set is
  ruling layer (router) + rule layer (fm playbook/dispatch-log) + machine layer (kit
  CHANGELOG) — three one-file reads.
