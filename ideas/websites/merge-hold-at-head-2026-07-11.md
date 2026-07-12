# Merge holds announced in a file at HEAD — link index

> **State:** captured
> **Class:** process · **Target:** `menno420/websites`
> **Grounding:** https://raw.githubusercontent.com/menno420/websites/8f9765483a7df57ce426e7d11d200f10b5495ed7/docs/ideas/merge-hold-at-head-2026-07-11.md@8f97654 · fetched 2026-07-12T01:47Z

**Canonical idea (stays in websites — indexed by link, never copied):**
[`menno420/websites → docs/ideas/merge-hold-at-head-2026-07-11.md`](https://github.com/menno420/websites/blob/8f9765483a7df57ce426e7d11d200f10b5495ed7/docs/ideas/merge-hold-at-head-2026-07-11.md)
— harvested 2026-07-12 by the websites fourth re-harvest slice, pinned @ websites `8f97654`
([raw](https://raw.githubusercontent.com/menno420/websites/8f9765483a7df57ce426e7d11d200f10b5495ed7/docs/ideas/merge-hold-at-head-2026-07-11.md)).

Announce a repo-wide merge hold as a file **at origin/main HEAD** — one
`control/claims/HOLD-<scope>.md` per hold (created when the hold starts, deleted
when it lifts; weaker fallback: a `hold:` heartbeat line) — so every session's
mandatory session-start pull sees the hold mechanically, instead of coordinating
holds by session messages, which only reach sessions alive at send time. The
canonical doc grounds it in a MEASURED failure, not vibes: the 2026-07-11 hold
protecting websites PR #141 failed twice — routine-fired 4-hourly wakes boot with
zero chat context, and websites #143/#146 were merged mid-hold by sessions that
never saw it (websites PR #148's body records #141 knocked to
`mergeable_state: behind` by exactly those merges). Same insight that makes
`control/claims/` work for work-claims, and the claim checker's existing
parse/stale machinery could nag on a stale HOLD file for free. Routing half named
in the canonical doc: the convention belongs to the kit/manager layer — one
fleet-wide shape, not per-repo forks (born in the lane's archive-prep capture,
websites #154; source retro: websites `docs/retro/archive-ready-2026-07-11.md`
§3). Dedup at capture: zero prior hold-coordination capture anywhere in this
repo's `ideas/` tree (nearest misses are the kit's `session-card-hold` gate
mechanics and superbot-idle's sim-hold queue states — different objects).
