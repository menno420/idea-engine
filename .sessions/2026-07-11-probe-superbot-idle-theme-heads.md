# Session — batched probe: superbot-idle theme heads (section close)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-11 (worker slice, dispatched by the coordinator
> under continuous-chaining mode per Q-0265)

## What this session did

Batched single-pass probe (battery v0, no panel triggers on either head) of the
section's two LAST unprobed heads, both captured in the #73 first batch at lane pin
`f11c71a`:

- `ideas/superbot-idle/theme-catalog-gallery-read-contract-2026-07-11.md`
- `ideas/superbot-idle/theme-schema-plugin-contract-promotion-2026-07-11.md`

Verify-first ran FIRST, both sides of every seam (expiry-aware per README § probe
order: the catalog head carries a `before` Sequence; the promotion head's arming
event is owner-click-distance from firing). One sweep served both heads — four
remote pins:

- **Producer lane** superbot-idle: HEAD moved `f11c71a` → `1b3a211` since capture;
  the delta (lane PRs #47–#49) is ORDER-001 model-attribution only — zero product
  change. Full ls-tree @ `1b3a211`: no `themes/catalog*.json`, no export tool beyond
  `gen_setup_vectors.py` + `theme_gate.py`; promotion tracker still ABSENT (the
  lane's `control/status.md` tracks PLUG-001 — the ADAPTER — not the promotion).
  BOTH capture premises HOLD at the live pin.
- **superbot-next** @ `4c8c5b0`: ORDER 002 `status: new`, acked-NOT-done (done =
  003,005,…,011), blocker verbatim "ORDER 002 done-when still hangs ONLY on the
  owner-created separate repo"; all four candidate contract-doc paths 404. The
  promotion's arming event has NOT fired — but is one owner click away.
- **websites** @ `7da9fbf`: zero hits for `IDLE1-|superbot-idle|theme gallery|setup
  code` — the gallery consumer is NOT started (supersedes the capture's `d4ed380`
  read). The catalog head's Sequence window is verified OPEN.
- **sim-lab** @ `d89303e`: VERDICT 006 = PROPOSAL 006 landed APPROVE, finalized
  2026-07-11T05:09:53Z — lifts the lane's SIM-001 economy hold; a seam-adjacent
  NON-event for both theme heads (themes carry no economy numbers). The
  `## Sim verdict` fan-in note on `idle-economy-sim-kernel-2026-07-11.md` is still
  OWED by a future slice — named best-next-slice in the handoff below.

Verdicts (one line each):

- theme-catalog-gallery-read-contract → **parked(build-direct)** — a one-PR lane
  export slice (loader-generated `themes/catalog.v1.json` + regenerate-or-red test)
  whose correctness is settled by the lane's own CI, leaving no empirical question a
  sim can settle; the sole open point (gallery ordering) is a product decision. No
  outbox proposal — the head stays indexed for the sweep / lane pickup (the
  mineverse snapshot-contract shape).
- theme-schema-plugin-contract-promotion → **parked(awaiting-arming-event)** — the
  promotion is already DECIDED (superbot `41899e1` §4/§7 item 3) and its evidence
  already exists, so nothing is sim-shaped; un-park keyed on the EVENT, never the
  404 path list: a published plugin/manifest contract doc fetchable anywhere in
  superbot-next OR ORDER 002 reaching done → relay the adopt-with-evidence
  promotion to the manager.

**SECTION MILESTONE: superbot-idle 4/4 probed-or-parked** — the FIFTH complete
section (after superbot-games, trading-strategy, superbot-mineverse @ #107, and
venture-lab @ #110): idle-economy-sim-kernel sim-ready @ #76 (PROPOSAL 006, now
verdicted approve), both theme heads parked this slice, and the cross-linked
directive head's probe-shaped kernel carried by the #76 probe.

No sim-ready outputs this slice → **NO outbox entry** (both verdicts are parks;
the outbox stays at 6 proposals, nothing pending relay from here).

Files touched: the two idea files (state flips + probe report appends),
`ideas/superbot-idle/README.md` (both index bullets flipped), this card,
`control/status.md` (heartbeat; ⚑ OWNER-ACTION block preserved verbatim;
superbot-idle milestone + VERDICT 006 routing note prepended to notes), claim
`control/claims/probe-superbot-idle-theme-heads.md` deleted per convention.

Claim: fast-laned first as PR #111 (control-only, merged 06:13:51Z by the enabler),
branch cut from origin/main `80a024b` (post-#113); claims dir re-read at that HEAD
— two sibling claims live (kit-line-self-drift probe @ #112, check_harvest
content-identity build @ #113), disjoint scopes, shared-heartbeat overlap only.

**📊 Model:** fable-5 · docs-only (two probe appends + two state flips + two index
flips + heartbeat + card; no code)

## 💡 Session idea

Batch probes by SHARED SEAMS, not just by section: these two heads needed four
remote pins between them (lane, superbot-next, websites, sim-lab) and every pin
served both reports — one verify-first sweep amortized across two verdicts. The
section boundary made the batch legible, but the cost win came from the seam
overlap; two same-section heads with disjoint seams would have batched in name
only. When picking the next batch, grep the captures' Grounding/Sequence lines
first and batch the heads whose pins coincide.

## ⟲ Previous-session review

PR #110 (venture-lab self-landable-merge-path probe, the FOURTH section close):
its heartbeat discipline transferred whole — ⚑ needs-owner preserved verbatim,
prior-slice PR number stamped at demotion per the #72/#79 precedent, last-shipped
citing the branch (never a guessed number) — and its recommendation byte-form
(`**Recommendation: park** — qualifier in the rationale, never in the token`) is
what both of this slice's reports use. Its 💡 (staged-vs-live is a distinct
verify-first surface class) did NOT bite here — these heads are doc/tracker-shaped
with no staged-artifact seam — but its generalization did: verify the INVARIANT,
not the named artifact, is exactly why the promotion head's un-park condition is
keyed on the event rather than the four 404 paths. Its handoff named the stop-hook
sibling and the gba-homebrew EAP race as ripest elsewhere; the coordinator instead
dispatched this section close — consistent with the handoff's own "venture-lab is
CLOSED" logic (the next probe surface with a live claim was this one). Its watch
item (manager routing the venture-lab wiring ORDER) remains pending — nothing in
this slice's inbox re-read moved it.

## Handoff → next wake

superbot-idle is CLOSED as a probe surface (4/4) — new heads arrive by capture or
harvest when the lane moves. Best-next-slice, named: the `## Sim verdict
(2026-07-11)` fan-in note on
`ideas/superbot-idle/idle-economy-sim-kernel-2026-07-11.md` — VERDICT 006 =
PROPOSAL 006 approve @ sim-lab `d89303e` (finalized 05:09:53Z) is verdicted but
NOT yet fanned in; per the V005 precedent (#80) the note carries the numbering
cross + the ruling summary, and the idea's state stays sim-ready→historical per
grammar. Watch: superbot-next ORDER 002 — one owner click fires the promotion
head's un-park (relay adopt-with-evidence via the manager, never re-design); and
the two live sibling claims (#112 kit-line-self-drift probe, #113 check_harvest
content-identity build) may land heartbeat edits — forward-merge, never rebase.
