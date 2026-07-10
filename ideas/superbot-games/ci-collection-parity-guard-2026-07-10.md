# CI collection parity guard — make the 73/121 class of gap impossible to recur

> **State:** captured
> **Class:** process · **Target:** `menno420/superbot-games`

## Problem

The lane's merge gate currently **collects only 73 of 121 tests** — 48 tests exist in the
tree but never run in CI, so a green gate silently under-verifies. The manager already
filed the P0 fix for the *instance* (games inbox ORDER 001, boot-gating, per the
manifest row). But the failure *class* — collection drifting below the tree's real test
census without turning anything red — stays open after that fix: the same misconfigured
testpath/marker/import-error that caused this can recur on the next plugin package, and
nothing would notice.

## Idea

A small guard step in the gate, landed in the same era as the ORDER 001 fix: run
`pytest --collect-only -q` over the whole tree, compare the census against the count the
gate actually executed, and go RED on any shortfall (collection errors count as
shortfall — they are how tests silently vanish). No pinned magic number to maintain:
the tree's own census is the reference, so the guard never goes stale as tests are added.

## Grounding

- Fleet manifest games-plugins row (`https://raw.githubusercontent.com/menno420/superbot/main/docs/eap/fleet-manifest.md`,
  fetched 2026-07-10): "**ORDER 001 (P0 CI-collection: gate collects 73/121 tests)
  pending — boot-gating**".
- Complements, does not duplicate, ORDER 001: that order repairs today's 48-test gap;
  this guard makes the repaired state self-checking. (Same warn-first/checker doctrine
  the hub already applies — cf. the harvested checker family in `ideas/superbot/`.)

**Why now:** the moment ORDER 001 lands, the gate will be trusted again — that trust is
only honest if the collection census is checked on every run, not once.
