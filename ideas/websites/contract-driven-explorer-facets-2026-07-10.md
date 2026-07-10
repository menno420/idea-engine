# Contract-driven explorer facets — the game-data explorer derives its UI from the versioned contract

> **State:** captured
> **Class:** product · **Target:** `menno420/websites`
> **Grounding:** https://raw.githubusercontent.com/menno420/idea-engine/698fd93869f8a05200f26fde45bbd71596323e6a/ideas/websites/superbot-site-stats-data-story-2026-07-10.md@698fd93 · fetched 2026-07-10T22:08Z
> **Grounding:** https://raw.githubusercontent.com/menno420/websites/0cd08d2da1580fffff1595a6f4119b6d98a8b4b3/dashboard/data_source.py@0cd08d2 · fetched 2026-07-10T22:08Z

## Problem

PROPOSAL 002's phase-2 explorer rides the live committed-feed pattern, but the
probe's Q4 names its real break: only families `meta`+`bugs` are contracted at
version 1, the game corpora (BTD6 towers/upgrades/bosses, mining items/recipes,
fish, creatures) are not contracted families at all, and "an explorer built on
un-contracted exports inherits the BUG-0022 silent-desync class … B's real cost
is contract extension, not UI." Built the obvious way, every new family costs
TWICE: a superbot-side contract/export extension AND a websites-side hand-built
facet/column/search UI — two lanes paying per family, forever, with the UI copy
free to drift from the contract it renders.

## Idea

Make the contract the explorer's only UI source of truth: the explorer reads the
versioned contract file itself (family list, field names/types, which dimensions
are facetable) and *generates* its browse facets, table columns, and search
fields from it — fail-closed on an unknown schema version, exactly the checker
doctrine the feed already lives by ("never fake data", honest-unavailable
banners, `dashboard/data_source.py`). Result: when superbot contracts a new
family, the family appears in the explorer with ZERO websites diff — the
per-family cost halves to one lane, the UI *cannot* desync from the contract,
and the probe's Q5 flywheel ("forces the #1920 contract to grow
family-by-family — hardening every other consumer of the same feed for free")
spins without a websites session per turn. The `leaderboards` family (sibling
capture, this section) would be its first zero-diff arrival if both land.

**Why now:** phase 2 is routable now without the sim verdict (probe
recommendation), and schema-driven vs hardcoded is a first-commit fork —
retrofitting generation under two or three hand-built family UIs is the
expensive path, choosing it before UI #1 exists is nearly free.
