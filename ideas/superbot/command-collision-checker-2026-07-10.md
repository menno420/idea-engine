# Idea — `check_command_collisions.py`: static guard against duplicate command names — link index

> **State:** historical(implemented in superbot PR #1918, 2026-07-10)
> **Class:** process · **Target:** `menno420/superbot`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/command-collision-checker-2026-06-29.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/command-collision-checker-2026-06-29.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/command-collision-checker-2026-06-29.md)).

A static pre-merge guard against duplicate command names/aliases across cogs — a collision with a dormant since-birth `give` command once crash-looped the bot offline via the strict identity contract.
