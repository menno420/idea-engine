# Bot self-testing: the command walker + AI eval mode — link index

> **State:** captured
> **Class:** process · **Target:** `menno420/superbot`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/bot-self-test-walker-2026-06-10.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/bot-self-test-walker-2026-06-10.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/bot-self-test-walker-2026-06-10.md)).

Bot self-testing via in-process synthetic invocation: a driver loop walks the command registry calling each callback with a synthetic ctx that captures output, with the EventBus as witness; plus an AI eval mode. Owner idea with two accepted agent adjustments.
