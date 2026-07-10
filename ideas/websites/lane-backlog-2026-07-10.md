# websites ideas backlog — the lane's single never-idle list — link index

> **State:** captured
> **Class:** process · **Target:** `menno420/websites`
> **Grounding:** https://raw.githubusercontent.com/menno420/websites/144dfced7282806efe778eaacb3565a13e35c2fa/docs/ideas/backlog.md@144dfce · fetched 2026-07-10T22:33Z

**Canonical idea (stays in websites — indexed by link, never copied):**
[`menno420/websites → docs/ideas/backlog.md`](https://github.com/menno420/websites/blob/144dfced7282806efe778eaacb3565a13e35c2fa/docs/ideas/backlog.md)
— harvested 2026-07-10 by the websites lane-backlog harvest slice, pinned @ websites `144dfce`
([raw](https://raw.githubusercontent.com/menno420/websites/144dfced7282806efe778eaacb3565a13e35c2fa/docs/ideas/backlog.md)).

The websites lane's single backlog list — rung 3 of its never-idle work ladder
(`docs/project/project-instructions.md`), one bullet per idea with lifecycle states
`captured → planned → built → retired` per its `docs/ideas/README.md`, seeded
2026-07-10 from ideas previously scattered across session cards, the queue-state NEXT
list, and the retros, every bullet source-cited. At the pin it holds **13 captured
bullets, 6 built, 0 retired**; a substantial idea additionally gets one standalone
file in `docs/ideas/` ("one home per idea"), and four such files exist — each indexed
as its own sibling entry in this section.

**Captured bullets @ pin (indexed by link, one line each)** — all under the backlog's
[`## Captured / planned` heading](https://github.com/menno420/websites/blob/144dfced7282806efe778eaacb3565a13e35c2fa/docs/ideas/backlog.md#captured--planned-pick-highest-value-buildable-first):

1. `/fleet` manifest-parse freshness badge — surface manifest-sourced vs fallback (and its age) on the page itself, a likely template tweak.
2. Re-check closed-unmerged PR #9 branch — diff the still-live `claude/rework-dashboard` against `main`, salvage or retire its hardening explicitly.
3. Per-repo `?repo=` filter on the activity views — narrow the three `/activity` routes to one lane's stream over the cached timeline (own doc, sibling entry).
4. kit-version rollup on `/fleet` — summary header plus per-card badge over the already-parsed `kit:` line, pure presentation.
5. "Unseen orders?" badge on `/fleet` — flag a lane whose inbox last-commit is newer than its heartbeat `updated:` stamp.
6. `/queue.json` + manager round-trip check — a JSON owner-queue variant so a filed ask is machine-verifiable write → poll → confirm.
7. `scripts/wait-deploy.py` — post-merge sha-convergence poller turning the manual "merge = deploy" check into a deterministic PASS/FAIL.
8. Review-queue row auto-check — mechanically flag a merged PR whose runtime changed-line count owes a fleet review-queue row under the binding 50-line rule.
9. Stalled-claim aging on `/orders` — badge a claimed order whose `claimed-by:` stamp is older than the claim ritual's ~24h expiry.
10. `meta.md` state-line convention — ask the manager to standardize one `deployed:` line format in the forming `projects/` registry.
11. Own-heartbeat parse self-check in `quality` — run the repo's own `control/status.md` through the `/fleet` parsers at PR time so a malformed heartbeat fails before it renders wrong.
12. Ladder-rung telemetry — one `rung:` token per wake so orders-vs-self-generated work and backlog dryness become trends the manager can read.
13. Open-PR awareness at wake — list open PRs + PR-less unmerged `claude/*` branches before picking a work rung (own doc, sibling entry).

**Honesty note (the sim-worthy count claim):** the lane heartbeat @ the pin claims
"Q-0264 sim-worthy candidates now seven, all in docs/ideas/backlog.md (newest:
stalled-claim aging on /orders)" — @ `0cd08d2`/`b30b4f1` the same claim said six —
but no heartbeat write ever enumerates the full set. The four it once enumerated
(@ `44a9fa6`) included "healthcheck-failure auto-files an issue," which has NO
backlog bullet at the pin (grep for issue/alert: zero hits). This entry indexes the
count claim verbatim and does not assert a specific six (or seven).

**Cross-links (by link, never duplicated):** backlog #1 and #4 touch the same
`/fleet` surface named as a future sparkline consumer in
[`fleet-program-pulse-feed-2026-07-10.md`](fleet-program-pulse-feed-2026-07-10.md);
backlog #3 plus the shipped Atom feed relate to the `/activity` "living epilogue"
folded into that same pulse-feed capture; backlog #13 is the same failure class as
idea-engine's own claims ritual (`claims/README.md`) — the order-claim fix applied
to branches.
