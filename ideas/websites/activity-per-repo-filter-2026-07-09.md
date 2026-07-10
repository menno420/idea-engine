# `?repo=` filter on the activity views — link index

> **State:** captured
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
