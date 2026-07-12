# Oracle user-copy punctuation-drift sweep — grep rebuild literals against oracle fragments

> **State:** captured
> **Class:** process · **Target:** `menno420/superbot-next`
> **Grounding:** https://github.com/menno420/superbot-next@80464ab39f86d55cede1e38b4780e7b1cc4a1777 · fetched 2026-07-12T01:34:18Z

One cheap sweep: grep the rebuild's user-copy string literals against oracle
`search_code` fragments to catch PUNCTUATION-LEVEL drift in refusal paths the golden
suites don't cover — the class the tournament-entry fix slice hit live and had to leave
out of scope. Live datapoint at the pin, recorded verbatim at the lane heartbeat: the
rebuild's in-memory guard copy in `sb/domain/rps/tournament.py:153` says "You're
already registered." where the oracle says "You're already registered!" —
golden-uncovered, found only because a fix slice happened to reconstruct the oracle
semantics by hand. Source: lane session card
[`.sessions/2026-07-12-tournament-entry-race-fix.md` § "💡 Session idea"](https://github.com/menno420/superbot-next/blob/80464ab39f86d55cede1e38b4780e7b1cc4a1777/.sessions/2026-07-12-tournament-entry-race-fix.md)
(second half) @ `80464ab`
([raw](https://raw.githubusercontent.com/menno420/superbot-next/80464ab39f86d55cede1e38b4780e7b1cc4a1777/.sessions/2026-07-12-tournament-entry-race-fix.md));
the noted-drift datapoint also rides
[`control/status.md`](https://github.com/menno420/superbot-next/blob/80464ab39f86d55cede1e38b4780e7b1cc4a1777/control/status.md)
(the #223 slice's ORACLE SEMANTICS bullet) @ `80464ab`.
