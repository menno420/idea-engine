# Seat boot-verification harness — script the dispatch copilot's §5 row — link index

> **State:** captured
> **Class:** process · **Target:** `menno420/superbot`
> **Grounding:** https://raw.githubusercontent.com/menno420/superbot/655e0fea62dbb64d2d5ec962da7fa5816c180c60/docs/ideas/seat-boot-verification-harness-2026-07-10.md@655e0fe · fetched 2026-07-10T21:38Z

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/seat-boot-verification-harness-2026-07-10.md`](https://github.com/menno420/superbot/blob/655e0fea62dbb64d2d5ec962da7fa5816c180c60/docs/ideas/seat-boot-verification-harness-2026-07-10.md)
— harvested 2026-07-10 by the drift re-harvest slice, pinned @ superbot `655e0fe`
([raw](https://raw.githubusercontent.com/menno420/superbot/655e0fea62dbb64d2d5ec962da7fa5816c180c60/docs/ideas/seat-boot-verification-harness-2026-07-10.md)).

The dispatch copilot's per-seat boot-verification ritual is a four-times-repeated manual sequence (trigger-registry check, raw-fetch of the seat's `control/status.md` heartbeat, inbox/outbox expected-entry check, hand-composed runbook §5 row) with at least three more runs incoming as the games-Project seats boot (Q-0259 r.5). The idea: a small superbot script — `scripts/check_seat.py <repo> [--routine <name>] [--expect-order N] [--expect-outbox N]` — that pulls the trigger registry (or a `list_triggers` JSON dump), parses the kit heartbeat grammar at HEAD, checks expected inbox/outbox numbers, and emits a ready-to-paste §5 row skeleton with every verified fact filled and only the verdict left for judgment. Q-0120-grounded: it reports only transport-verifiable facts and labels self-reported status content as such, so a self-report can never be laundered into a verification. Motivation: hand-composed §5 rows are where transcription drift enters the fleet's boot audit trail.
