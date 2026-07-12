# KNOWN_RISKS→fix coupling as checker doctrine — ledgered bugs whose rows the fixing PR must delete

> **State:** captured
> **Class:** process · **Target:** `menno420/superbot-next`
> **Grounding:** https://github.com/menno420/superbot-next@80464ab39f86d55cede1e38b4780e7b1cc4a1777 · fetched 2026-07-12T01:34:18Z

Generalize the lane's just-proven #221→#223 pattern into standing checker doctrine: any
"suspected real bug" a committed checker surfaces lands as a loud KNOWN_RISKS ledger
row (reported on every run, never called safe) whose DELETION is mechanically coupled
to the fixing PR by a stale-row guard — fix-without-delete reds the checker — so
checker findings can't silently rot. Live proof at the pin: `tools/check_money_race.py`
(PR #221) ledgered the tournament-entry race as its single KNOWN_RISKS row, and the
stale-row guard forced the fixing PR #223 to ship fix + row deletion in one PR ("worked
exactly as designed", the fix session's own words). Adjacent but distinct in scope to
[`ideas/superbot/warn-first-checker-authoring-kit-2026-07-10.md`](../superbot/warn-first-checker-authoring-kit-2026-07-10.md)
(superbot-side checker AUTHORING ergonomics; this head is the finding-LIFECYCLE
coupling rule for this lane's checker fleet). Source: lane session card
[`.sessions/2026-07-12-tournament-entry-race-fix.md` § "💡 Session idea"](https://github.com/menno420/superbot-next/blob/80464ab39f86d55cede1e38b4780e7b1cc4a1777/.sessions/2026-07-12-tournament-entry-race-fix.md)
@ `80464ab` ([raw](https://raw.githubusercontent.com/menno420/superbot-next/80464ab39f86d55cede1e38b4780e7b1cc4a1777/.sessions/2026-07-12-tournament-entry-race-fix.md));
the pattern is also described at the lane heartbeat,
[`control/status.md`](https://github.com/menno420/superbot-next/blob/80464ab39f86d55cede1e38b4780e7b1cc4a1777/control/status.md)
(the #223 and #221 slice records) @ `80464ab`.
