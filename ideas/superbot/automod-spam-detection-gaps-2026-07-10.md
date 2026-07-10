# Automod's spam rule is rate-only and per-channel — two related detection gaps — link index

> **State:** historical(shipped in superbot same day, 2026-07-07)
> **Class:** product · **Target:** `menno420/superbot`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/automod-spam-detection-gaps-2026-07-07.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/automod-spam-detection-gaps-2026-07-07.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/automod-spam-detection-gaps-2026-07-07.md)).

Automod's spam rule was pure rate-counting per channel — it never read message content, so duplicate/copypasta spam and cross-channel spam were invisible. Owner-raised and shipped the same day.
