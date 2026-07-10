# EFFECT-arming compensator checklist — turn the #105→#111 lineage into a precondition

> **State:** captured
> **Class:** process · **Target:** `menno420/superbot-next`

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
