# `/activity.xml` — Atom feed for the cross-repo activity timeline — link index

> **State:** historical(menno420/websites#41)
> **Class:** product · **Target:** `menno420/websites`
> **Grounding:** https://raw.githubusercontent.com/menno420/websites/144dfced7282806efe778eaacb3565a13e35c2fa/docs/ideas/activity-atom-feed-2026-07-09.md@144dfce · fetched 2026-07-10T22:33Z

**Canonical idea (stays in websites — indexed by link, never copied):**
[`menno420/websites → docs/ideas/activity-atom-feed-2026-07-09.md`](https://github.com/menno420/websites/blob/144dfced7282806efe778eaacb3565a13e35c2fa/docs/ideas/activity-atom-feed-2026-07-09.md)
— harvested 2026-07-10 by the websites lane-backlog harvest slice, pinned @ websites `144dfce`
([raw](https://raw.githubusercontent.com/menno420/websites/144dfced7282806efe778eaacb3565a13e35c2fa/docs/ideas/activity-atom-feed-2026-07-09.md)).

Emit the already-shipped `/activity` cross-repo PR timeline as an Atom 1.0 feed at
`/activity.xml` so the owner subscribes once (any reader, or a webhook pipe) instead
of polling the page — a second serializer over the exact `activity.timeline()` list,
riding the same TTL cache with no new fetch, dependency, or secret. SHIPPED: the lane
records it built (decision D-0025; merge commit `20559c6` "(#41)"; backlog `## Built`
bullet naming this file), with honest degradation (undated PRs omitted, offline
yields a valid single-diagnostic-entry feed) — hence `historical(menno420/websites#41)`
per the outcome-mirroring rule. Front-matter honesty: the doc's `shipped_pr:` field
carries the branch name (`activity-atom-feed`), not a number — the #41 here is
grounded in the merge commit and the backlog Built bullet. The doc stays as the
idea's origin record; source code and binding contracts win over it. Its flagged
follow-up (a per-repo feed variant) is the sibling entry
[`activity-per-repo-filter-2026-07-09.md`](activity-per-repo-filter-2026-07-09.md).
