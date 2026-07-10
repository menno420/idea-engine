# Public server leaderboards on the committed feed — the zero-auth slice of the stats ask

> **State:** captured
> **Class:** product · **Target:** `menno420/websites` (one small cross-lane dependency on `menno420/superbot`: a new contracted export family — same class as PROPOSAL 002 phase 2's, NOT the read-only API)
> **Grounding:** https://raw.githubusercontent.com/menno420/idea-engine/698fd93869f8a05200f26fde45bbd71596323e6a/ideas/websites/superbot-site-stats-data-story-2026-07-10.md@698fd93 · fetched 2026-07-10T22:08Z
> **Grounding:** https://raw.githubusercontent.com/menno420/superbot/9624c5399f5b1a3da293c07ce930e8b0410d79e4/docs/eap/fleet-manifest.md@9624c53 · fetched 2026-07-10T22:08Z
> **Sequence:** before the PROPOSAL 002 stats phase — it deliberately front-runs the OAuth sim verdict and the unrouted superbot read-only API by shipping only what needs neither

## Problem

The owner's stats ask ("clearly see your stats for the bot, per server", idea §1)
is double-blocked: the OAuth trust gate awaits a sim-lab verdict (PROPOSAL 002,
still queued behind INTAKEs 001–002), and the superbot read-only API it needs is
an unrouted cross-lane ORDER with two waiting consumers (probe Q4: "unrouted,
phase 3 deadlocks regardless of the sim verdict"). Meanwhile a large slice of
that value is not personal at all: leaderboards — top miners, depth records, XP
ranks per server — which the bot already displays publicly in-channel to anyone
who types the command.

## Idea

Ship the trust-free slice first: a new contracted export family `leaderboards`
(top-N per game per server: XP/level, coins, mining depth, fishing, creature
game — small, bounded rows), produced by superbot's existing exporter per the
PR #1920 versioned fail-closed pattern, rendered by websites over the exact raw
fetch path `dashboard/data_source.py` uses today. Zero OAuth, zero backend, zero
new server surface — per-user *private* views stay behind the sim gate where they
belong. One real design point, named honestly: publishing in-server display names
on the open web is wider exposure than in-channel display, so the family should
carry a per-server opt-out and/or name masking — a data-shape decision, not an
auth surface. Bonus: this is the same family-extension muscle the phase-2
explorer needs (probe Q4: "B's real cost is contract extension, not UI") —
exercised once on the smallest family.

**Why now:** the stats phase's two blockers have no ETA, and the manifest row
confirms the lane is live and hungry (3 services on Railway, 4-hourly wake
verified) — this converts the stats ask's demonstrable 80% into routable
phases-1–2-class work instead of leaving ALL stats value parked behind the
slowest dependency.
