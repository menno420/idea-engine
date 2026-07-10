# Host-seam conformance stub — an executable stand-in for the in-flight plugin contract

> **State:** captured
> **Class:** product · **Target:** `menno420/superbot-games` (cross-lane dependency:
> `menno420/superbot-next` plugin/manifest contract, its inbox ORDER 002)

## Problem

The lane README @ `adb5f9b` is explicit: games ship as plugin packages consumed by
`superbot-next` via a manifest/plugin contract that "is in flight there (superbot-next's
inbox ORDER 002); until it lands, all work here stays plugin-side … with the host-facing
seams left open." Today those open seams exist only as prose in two founding plans. Two
autonomous Projects building against prose seams for weeks means the seams drift apart,
and the eventual cutover to the real contract becomes an archaeology job instead of a
diff — while superbot-next itself is still mid-mission (manifest: gen-1 band 5, ORDERs
008/009 pending), so the wait is not short.

## Idea

A tiny **stub host** under `games/shared/` (claim-first path per `docs/lanes.md`): one
module that fake-implements each open host-facing seam (registration/manifest handshake,
command surface mount, persistence handle, audited reward routing) plus a conformance
test both lanes run — "my package loads, mounts, and round-trips against the stub."
The stub is the seam's single executable definition; when superbot-next's real contract
lands, cutover = point the conformance test at the real contract and fix exactly the
failures it prints. Interface changes announce in both lane status files per lanes.md.

## Grounding

- `https://raw.githubusercontent.com/menno420/superbot-games/main/README.md` @ `adb5f9b`
  (contract-in-flight paragraph, quoted above) and `docs/lanes.md` @ `adb5f9b`
  (`games/shared/**` claim-first; both-status-files interface rule).
- Fleet manifest superbot-next row (`https://raw.githubusercontent.com/menno420/superbot/main/docs/eap/fleet-manifest.md`,
  fetched 2026-07-10): mid-mission, self-arm ORDER unexecuted — the contract's ETA is
  genuinely uncertain.

**Why now:** both gen-1 lanes just closed green — gen-2's first plugin work starts
against these seams, and a stub is cheapest before either lane has code shaped around a
private guess.
