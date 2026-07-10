# No-transcript secret plumbing — moving secrets without ever printing them (2026-07-02) — link index

> **State:** captured
> **Class:** process · **Target:** `menno420/superbot`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/no-transcript-secret-plumbing-2026-07-02.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/no-transcript-secret-plumbing-2026-07-02.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/no-transcript-secret-plumbing-2026-07-02.md)).

Secret moves between stores (Railway URL → GitHub secret, webhook URLs) currently rely on discipline not to echo values into transcripts; build a plumbing pattern that moves secrets without ever printing them.
