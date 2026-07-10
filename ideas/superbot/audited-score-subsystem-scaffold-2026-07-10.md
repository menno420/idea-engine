# Idea — "audited per-user score" subsystem scaffold + parity guard — link index

> **State:** captured
> **Class:** process · **Target:** `menno420/superbot`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/audited-score-subsystem-scaffold-2026-06-22.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/audited-score-subsystem-scaffold-2026-06-22.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/audited-score-subsystem-scaffold-2026-06-22.md)).

Economy, XP, and karma are the identical six-piece per-user-score shape (DB seam, audit table, service write seam, catalogue entry, INV test, rank provider); scaffold it plus a parity guard so new score subsystems are stamped out consistently. Partially implemented (superbot PR #1346).
