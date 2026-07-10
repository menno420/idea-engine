# Patch-only egress doctrine — encode why the repo went private, before anything leaves it

> **State:** captured
> **Class:** process · **Target:** `menno420/pokemon-mod-lab`

## Problem

The repo was flipped private **urgently** on 2026-07-10 — the manifest row records it
as "PRIVATE ✅ (API-verified ~15:12Z — the URGENT flip happened)". The urgency is the
tell: this lane's tree contains Nintendo-derived content that must not sit on a public
surface, in explicit contrast to gba-homebrew's "public-by-design (no Nintendo-derived
content)" row. The privacy flip fixed the *repo* surface, but the failure class —
IP-bearing bytes crossing to a public surface — re-arms every time the lane ships
anything outward: the pending owner playtest artifact, release assets, future public
docs. Nothing visible today encodes the boundary as doctrine; it lives only as the
memory of one urgent flip.

## Idea

One short lane PR that makes the boundary structural: (1) a **doctrine paragraph** in
the lane README — everything that leaves this repo (release artifact, playtest kit,
attachment, screenshot policy) is **patch-format only** (BPS/UPS/IPS against a named
clean base the owner supplies), never a ROM, never extracted assets; the repo itself
stays private indefinitely; (2) a **CI tripwire** — a check that fails on binary blobs
above a size threshold or known ROM extensions in the tree and in release-bound paths,
so the guard survives session turnover instead of relying on each agent remembering the
flip; (3) a one-line note that venture-class monetization is permanently out of scope
for this lane's outputs (derived IP), so no future venture sweep wastes a probe on it.

## Grounding

- Manifest pokemon-mod-lab row (URGENT private flip, API-verified ~15:12Z) and
  gba-homebrew row (public-by-design contrast) @
  [`53fb5ef`](https://raw.githubusercontent.com/menno420/superbot/53fb5ef9a294ab304b679dedd44ead55849295d5/docs/eap/fleet-manifest.md)
  (fetched 2026-07-10 ~20:35Z).
- Q-0260 rule 3 @ [`53fb5ef`](https://raw.githubusercontent.com/menno420/superbot/53fb5ef9a294ab304b679dedd44ead55849295d5/docs/owner/maintainer-question-router.md):
  "pokemon-mod-lab went private 2026-07-10" is already fleet-visible doctrine on the
  *read* side; this capture is its missing *egress* half.
- Verified live this session: raw-read of the lane 404s; only patch-shaped, clean
  artifacts could ever be fleet-shareable from here.

**Why now:** the post-EAP playtest (window closes 2026-07-14) is the first planned
egress event since the flip — the doctrine should exist before the first artifact
leaves, not be reconstructed after a second urgent fix.
