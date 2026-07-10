# The wire-level live-bot loop — Galaxy Bot dissolves the [needs-live-bot] gate (2026-07-02) — link index

> **State:** parked(contradicted-in-part by superbot canonical-plan F-4, PR #1770 — do not build as written)
> **Class:** process · **Target:** `menno420/superbot`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/wire-level-live-bot-loop-2026-07-02.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/wire-level-live-bot-loop-2026-07-02.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/wire-level-live-bot-loop-2026-07-02.md)).

Use the test-bot token to drive the live bot over the real Discord gateway from a second connection as a black-box loop; source check later showed a second BOT connection cannot drive message commands (discord.py drops bot-authored messages), so the design needs re-scoping.
