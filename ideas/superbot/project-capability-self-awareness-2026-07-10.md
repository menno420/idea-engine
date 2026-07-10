# Project capability self-awareness — ask a seat what it can do, get an honest answer — link index

> **State:** captured
> **Class:** process · **Target:** `menno420/superbot`
> **Grounding:** https://raw.githubusercontent.com/menno420/superbot/655e0fea62dbb64d2d5ec962da7fa5816c180c60/docs/ideas/project-capability-self-awareness-2026-07-10.md@655e0fe · fetched 2026-07-10T21:38Z

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/project-capability-self-awareness-2026-07-10.md`](https://github.com/menno420/superbot/blob/655e0fea62dbb64d2d5ec962da7fa5816c180c60/docs/ideas/project-capability-self-awareness-2026-07-10.md)
— harvested 2026-07-10 by the drift re-harvest slice, pinned @ superbot `655e0fe`
([raw](https://raw.githubusercontent.com/menno420/superbot/655e0fea62dbb64d2d5ec962da7fa5816c180c60/docs/ideas/project-capability-self-awareness-2026-07-10.md)).

Owner-raised (verbatim: a Project should be able to answer "what are your abilities?" honestly), prompted by sim-lab's freshly-booted coordinator lacking `create_trigger`/`send_later` while a worker it spawned minutes later had both — the fourth+ occurrence of seat-dependent capability variance across the fleet. Two halves: a platform ask (a first-party queryable per-session capability manifest — routed to the EAP wrap-up email, not buildable here) and a fleet-internal mitigation buildable now — a kit `bootstrap.py capabilities --probe` command that runs the known probe battery (scheduler tools? worker-seat differences? merge path? raw-read reachability?) and regenerates `docs/CAPABILITIES.md` from live results with dates + verbatim errors, so every seat boot can open with a probed, honest self-answer instead of paying the trial-and-refusal discovery tax. Closely related to the already-indexed `session-start-capability-self-probe-2026-07-10.md` (this doc is the owner-raised, fleet-wide restatement with a concrete kit home).
