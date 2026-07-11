# `?repo=` filter on the activity views — link index

> **State:** historical(menno420/websites#86)
> **Class:** product · **Target:** `menno420/websites`
> **Grounding:** https://raw.githubusercontent.com/menno420/websites/144dfced7282806efe778eaacb3565a13e35c2fa/docs/ideas/activity-per-repo-filter-2026-07-09.md@144dfce · fetched 2026-07-10T22:33Z

**Canonical idea (stays in websites — indexed by link, never copied):**
[`menno420/websites → docs/ideas/activity-per-repo-filter-2026-07-09.md`](https://github.com/menno420/websites/blob/144dfced7282806efe778eaacb3565a13e35c2fa/docs/ideas/activity-per-repo-filter-2026-07-09.md)
— harvested 2026-07-10 by the websites lane-backlog harvest slice, pinned @ websites `144dfce`
([raw](https://raw.githubusercontent.com/menno420/websites/144dfced7282806efe778eaacb3565a13e35c2fa/docs/ideas/activity-per-repo-filter-2026-07-09.md)).

Accept an optional `?repo=<name>` query on `/activity`, `/activity.json`, and
`/activity.xml` so the owner can watch — or subscribe to — a single lane's PR stream
instead of the whole fleet: the per-repo Atom variant the shipped feed (D-0025)
explicitly flagged as its natural follow-up. Cheap because `activity.timeline()`
already tags every item with its `repo`: a one-line post-filter over the cached list,
validated against `config.REPOS`, threaded through the three existing routes with no
new fetch. Its own open considerations are honesty-shaped: unknown `?repo=` must be
an honest empty/404 (never a silent full-fleet fallback that misleads a subscriber),
and the feed `id`/`self` link must differ per filter so readers treat per-repo feeds
as distinct subscriptions. State `captured` at the pin (front-matter `outcome: open`);
also backlog bullet #3, which names this file as the idea's one home.

## Upstream outcome (2026-07-11 re-pin)

> **Grounding:** https://raw.githubusercontent.com/menno420/websites/d8623642cabf068125dccb69ac775f2de0311104/docs/ideas/activity-per-repo-filter-2026-07-09.md@d862364 · fetched 2026-07-11T06:47Z

SHIPPED by the lane itself — the +4/-4 drift since pin `8c19e93` is FRONT-MATTER
ONLY, the outcome flip: `state: built · shipped_repo: menno420/websites ·
merged_date: 2026-07-11 · outcome: shipped` (quoted from the canonical doc at the
pin; `shipped_pr:` stays `null` there). The state badge above mirrors it as
`historical(menno420/websites#86)` — the PR number is NOT in the front-matter: it
is inferred from the slice-10 squash-commit subject `580f5e0` "`?repo=` per-lane
filter on the activity views (/activity, .json, .xml) (#86)" in the blobless
clone's `git log` at `d862364`, corroborated by the backlog's Built bullet
("continuous-mode slice 10; decision stamped in `docs/site.md` § 2 + the decision
ledger"). Shipped shape matches the capture: filtered case fetches only that
repo, the Atom feed becomes a per-lane subscription with the repo in its title,
unknown repo = honest empty state.
