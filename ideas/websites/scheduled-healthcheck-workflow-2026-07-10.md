# Scheduled healthcheck workflow — standing liveness verification — link index

> **State:** historical(menno420/websites#69)
> **Class:** process · **Target:** `menno420/websites`
> **Grounding:** https://raw.githubusercontent.com/menno420/websites/144dfced7282806efe778eaacb3565a13e35c2fa/docs/ideas/scheduled-healthcheck-workflow-2026-07-10.md@144dfce · fetched 2026-07-10T22:33Z

**Canonical idea (stays in websites — indexed by link, never copied):**
[`menno420/websites → docs/ideas/scheduled-healthcheck-workflow-2026-07-10.md`](https://github.com/menno420/websites/blob/144dfced7282806efe778eaacb3565a13e35c2fa/docs/ideas/scheduled-healthcheck-workflow-2026-07-10.md)
— harvested 2026-07-10 by the websites lane-backlog harvest slice, pinned @ websites `144dfce`
([raw](https://raw.githubusercontent.com/menno420/websites/144dfced7282806efe778eaacb3565a13e35c2fa/docs/ideas/scheduled-healthcheck-workflow-2026-07-10.md)).

A cron GitHub Actions workflow running the repo's own `scripts/healthcheck.py`
against the three live services and failing loudly on any non-200 — turning liveness
from a thing a session remembers to probe into a thing the repo verifies on its own
clock (Actions cron being the one scheduler agents can arm themselves, per the gen-1
retro's F3 finding; the founding incident was a handover flag "liveness unverified"
that a later session had to close manually). SHIPPED: front-matter records
`state: built · shipped_pr: 69 · merged_date: 2026-07-10`, and the backlog `## Built`
bullet records it live as `.github/workflows/healthcheck.yml` (every 6 h at
minute-17 + `workflow_dispatch`, read-only, no secret, NOT a required check, failure
notifies via the failed-workflow email) — hence `historical(menno420/websites#69)`
per the outcome-mirroring rule; the doc stays as the idea's origin record.
