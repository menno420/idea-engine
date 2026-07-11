# EFFECT-arming compensator checklist — turn the #105→#111 lineage into a precondition

> **State:** parked(routed — lane build-direct: a one-doc pre-arming slice writing the four-point arming checklist into `docs/collaboration-model.md` beside the ORDER-010 @codex rule, sequenced BEFORE the role/proof_channel arming slice — probed 2026-07-11: the trigger the capture named is the literal next queued item ("Still queued: role/proof_channel live EFFECT action ports (GuildRoleActions, ChannelPermActions still unarmed)" verbatim at the lane heartbeat @ `910c44e`), no arming-checklist doc exists (grep zero), the lessons are demonstrably still re-litigated per-PR (#133 settle-once double-payout race caught mid-flight · #138 render-once · #163 ad-hoc effect-leg sequencing) while the compensator allowlist stays deliberately EMPTY (re-asserted #145/#160/#163), and MORE armings are queued behind the first (the modal-arming slice, dispatched at the pin; the owner-key-gated live-NL leg, OWNER-ACTION 5); nothing sim-shaped)
> **Class:** process · **Target:** `menno420/superbot-next`
> **Grounding:** https://github.com/menno420/superbot-next@910c44ebeb85c0d0db2bd6e5455176d52a023dcc · fetched 2026-07-11T08:13:45Z
> *(pin annotation: probe-time re-check pin — capture pin was `ec2bcf2` (2026-07-10); lane live HEAD via `git ls-remote` 2026-07-11T08:13:45Z = `910c44e`, re-confirmed UNMOVED 08:42:15Z at authoring time; tree reads via read-only blobless clone at the pin; the shared verify-first sweep for this section's four heads lives in [`composition-parity-registration-diff-2026-07-10.md`](composition-parity-registration-diff-2026-07-10.md)'s pin annotation — only the facts SPECIFIC to this head are restated below)*

## Problem

The named next lane arms live EFFECT actions: "role/proof_channel live EFFECT action
ports (GuildRoleActions, ChannelPermActions still unarmed)" — and band-6 games will arm
more. The compensation lessons were bought across three PRs (#105→#108→#111) plus the
audit's canonical failure case: compensators must delete **if-match** (winner_id +
unlock_at — a permanent grant compensates nothing), every declared compensator ref must
resolve to a registered leg (the #111 invariant test), and an EFFECT leg without
oracle-aligned failure handling yields phantom DB rows when Discord refuses (ORDER 004
item 1's warn-escalation regression: escalation history written pre-effect, count wiped,
where the oracle keeps the count and reports `escalation_blocked=True`). Nothing makes
those lessons a *precondition* for arming the next action — each arming re-litigates
them from memory, and the lineage shows memory loses (#108's symmetric twin had to be
folded in by #111).

## Idea

A one-page arming checklist in the doctrine doc, binding for every newly armed EFFECT
action: (a) an if-match compensator, or a written compensates-nothing ruling in the PR;
(b) coverage under the existing compensator-invariant test (extend it where the new
action declares refs it can't see); (c) oracle alignment on the refusal path — what the
old bot does when Discord says no, matched or ledgered; (d) a live-drive proof of the
armed action plus golden classification of its failure copy. The invariant test already
exists to hang (b) on; the rest is doc + PR discipline, enforced the same way the
ORDER-010 @codex rule is.

## Grounding

- Lane status @ [`ec2bcf2`](https://raw.githubusercontent.com/menno420/superbot-next/ec2bcf21d7517284df33f56d1082db0c8dcb9007/control/status.md)
  (fetched 2026-07-10): phase line — the #111 fold-in ("`_compensate_lock` deletes
  IF-MATCH … a permanent grant compensates nothing" + "the extended
  compensator-invariant test"); "▶ NEXT LANE: … role/proof_channel live EFFECT action
  ports (GuildRoleActions, ChannelPermActions still unarmed)"; notes — the #105/#108
  compensator lineage "fully closed by #111's delete-if-match fold-in".
- Lane inbox @ [`ec2bcf2`](https://raw.githubusercontent.com/menno420/superbot-next/ec2bcf21d7517284df33f56d1082db0c8dcb9007/control/inbox.md):
  ORDER 004 item 1 — the phantom-rows/wiped-count regression that defines the failure
  mode class (a) and (c) guard against.

**Why now:** the next arming (role/proof_channel) is already queued as the next lane —
the checklist costs a page today and a compensator-lineage repeat later.

## Probe report (v0, 2026-07-11)

Single-pass battery v0 (no panel trigger: routing decision, docs-only diff lane-side).
**Verify-first, this head's specifics at `910c44e`:** the trigger the capture named is
**still the literal next queued item** — the lane heartbeat carries verbatim "Still
queued: role/proof_channel live EFFECT action ports (GuildRoleActions,
ChannelPermActions still unarmed)". **No arming-checklist doc exists** (grep zero hits
for any arming checklist/precondition across docs/, sb/, tests/ at the pin;
`docs/collaboration-model.md` carries only the ORDER-010 @codex rule). The lessons are
**demonstrably still re-litigated per-PR**: #133 caught the blackjack-tournament
settle-once double-payout race mid-flight ("no escrow rows to consume — two racing
champion resolutions could both pay the consolation"; fixed as check-and-set keyed on
the atomic row-deletion count, retrofit onto `rps.tournament_payout` too), #138 added
the render-once guard, and #163's moderation flip hand-derived "call-Discord-first
record-leg sequencing for the timeout half-applied golden … the kick effect leg
carries compensate_kick" — each a fresh in-flight derivation of the same lesson
family. The **compensator allowlist stays deliberately EMPTY**, re-asserted at
#145/#160/#163 ("the compensator allowlist stays EMPTY" verbatim in the #163 wave-6
record). And **more armings are queued behind the first**: the modal-arming slice
(dispatched at the pin's heartbeat — "no PR/branch visible yet; unblocks the
#160-parked text/number modals") and the owner-key-gated live-NL leg (OWNER-ACTION 5);
even non-arming work is hitting effect-precondition walls (the quicksetup park: "a
create-channel EFFECT with no capture twin and no compensator ruling; D-0030 names
channel-ops as the successor slice"). **Not overtaken — the gap is fully open and its
trigger is imminent.**

**1. What is this really?** A pre-arming gate for a lesson family the lane keeps
re-buying at retail. The #105→#111 compensator lineage produced four durable rules
(if-match compensation or a written compensates-nothing ruling · invariant-test
coverage · oracle-aligned refusal path · live-drive proof + failure-copy
classification), and the lane demonstrably APPLIES them — but from memory, per-PR,
with the derivation cost paid each time (#133's race was caught mid-flight, not
pre-empted; #163's sequencing was hand-derived at the flip). The checklist converts a
recurring in-flight derivation into a boot-time read. The battery's crux: where does
it live, and must it land before the next arming?

**2. What is the possibility space?** (i) Do nothing — each arming re-derives; the
lineage's own record shows memory loses (#108's symmetric twin had to be folded in by
#111). (ii) The captured one-page checklist in `docs/collaboration-model.md` beside
the @codex rule — the same home the (separately probed) band-binding encoding routes
to, enforced the same way (PR discipline + citation), landing BEFORE the
role/proof_channel slice. (iii) Mechanize instead: extend the #114-family invariant
tests to force per-arming coverage — partially real (item (b) already hangs on the
existing compensator-invariant test) but items (a)/(c)/(d) are judgment calls a test
cannot see (a compensates-nothing RULING, oracle alignment on refusals, live-drive
proof); over-mechanizing repeats the mistake the allowlist-stays-EMPTY discipline
guards against. (iv) Fold it into each ORDER's text — the exact inbox-rotation
fragility ORDER 010 already condemned. The value peak is (ii).

**3. What is the most advanced capability reachable by the simplest implementation?**
One doc page makes every future arming — role/proof_channel, the modal slice, the
owner-key-gated live-NL leg, band-9's remainder — boot from the full paid-for lesson
set: the arming PR opens with four checkboxes instead of a memory scan, the reviewer
(and the standing @codex question) gets a named contract to review against, and the
compensator allowlist's EMPTY discipline gets its written rationale (why EMPTY is a
choice, not an omission) — the single highest-leverage page per queued-arming in the
lane's backlog.

**4. What breaks it?** Sequencing, above all: the role/proof_channel slice is the
literal next queued item and the lane merges ~50 commits/day — if the arming lands
before the checklist, the head's marginal value drops to the NEXT arming (still
real: modal + live-NL are queued, band-9 follows). A checklist written but not
cited is shelf-ware: it needs the same PR-discipline hook as the @codex rule (the
arming PR cites the section). And a checklist that hardens into bureaucracy for
non-EFFECT work would be over-reach — its scope line must bind newly ARMED live
EFFECT actions only.

**5. What does it unlock?** The role/proof_channel arming (GuildRoleActions,
ChannelPermActions) ships against a written precondition instead of institutional
memory; every subsequent arming inherits it free; the #133-class mid-flight saves
stop being the safety net; and the compensator lineage (#105→#108→#111) graduates
from war story to doctrine.

**6. What does it depend on?** The doctrine doc as the real boot surface (verified —
same home as the @codex rule); the existing compensator-invariant test (item (b)'s
enforcement seam, live since #111/#114); the lane's PR discipline (proven — the
@codex rule rides it); nothing external, no owner action, nothing sim-shaped — a
checklist is proven by the next arming PR citing it and shipping without a
mid-flight compensator save.

**7. Which lane should build it?** `menno420/superbot-next` — build-direct: it owns
the doc, the invariant test, the queued armings, and the lessons. Not idea-engine
(this repo writes only itself); no sim-lab question (nothing to simulate in writing
down rules the lane already enforces by hand). Routing = this section README's index
+ the heartbeat notes for the manager's :30 sweep — pairs with the band-binding
encoding head (same doc, same sweep, could ride ONE lane ORDER), with THIS head
carrying the sequencing constraint: before the role/proof_channel slice if the lane's
cadence allows.

**8. What is the smallest shippable slice?** One lane doc-only PR:
`docs/collaboration-model.md` gains an "EFFECT-arming checklist (standing)" section
beside the @codex rule — binding for every newly armed live EFFECT action: (a)
if-match compensator or a written compensates-nothing ruling in the PR; (b) coverage
under the compensator-invariant test, extended where the action declares refs it
can't see; (c) oracle-aligned refusal path (what the old bot does when Discord says
no — matched or ledgered); (d) live-drive proof of the armed action + golden
classification of its failure copy — plus one line requiring arming PRs to cite the
section, and one sentence recording WHY the compensator allowlist stays EMPTY.
Red/green reference: the role/proof_channel arming PR (or the first arming after
landing) opening with the four checkboxes and merging without a mid-flight
compensator derivation.

**Recommendation: park** — routed (lane build-direct, sequencing-constrained): a
one-doc pre-arming slice in `docs/collaboration-model.md`, ideally landed BEFORE the
role/proof_channel arming (the capture's named trigger, still the literal next
queued item at `910c44e`); if the lane's cadence outruns the relay, the slice keeps
full value for the queued modal/live-NL/band-9 armings; nothing sim-shaped — the
checklist is proven by the next arming PR citing it.
