# Coordinator archive-handoff ceremony — a named close-out ritual, not an ad-hoc derivation

> **State:** captured
> **Class:** process · **Target:** `menno420/substrate-kit` (kit-native ceremony candidate;
> the trigger-disposition half touches coordinator/fleet-manager doctrine)

**Origin:** the 2026-07-11 idea-engine archive close-out (#216 + the archive-ready PR,
this file's own slice). The owner archived the coordinator chat, and the close-out
ceremony had to be DERIVED ad hoc, live, across two PRs: commit chat-only facts →
claims sweep with a bounded wait on in-flight siblings → session enders → a durable
archive-ready note → heartbeat overwrite LAST. Every step existed as scattered doctrine
(heartbeat-last rule, claim etiquette, card markers), but no surface named the SEQUENCE
or the archive-specific duties.

## The idea

A kit-blessed **archive-ready ceremony** — a checklist (docs template or
`bootstrap`-rendered doc, like the claim/heartbeat conventions) any lane runs when its
coordinator chat archives:

1. **Bounded wait, never delete**: poll in-flight sibling claims for a fixed window;
   past the window, PARK the claim on record (heartbeat + archive note line) — another
   session's live claim is never swept.
2. **Sweep**: claims dir down to README, zero open PRs, dangling branches/work items
   each landed/parked/closed with a one-line reason.
3. **Session enders**: complete card (all four kit markers), model-attribution line,
   one GENERATE idea (dedup-grep first).
4. **Durable archive note** (`docs/retro/archive-ready-<date>.md`): true state with
   SHAs, every pending ⚑ owner action mirrored, exact resume steps for the successor,
   unresolved items noted-not-asserted, and a "nothing load-bearing remains chat-only"
   confirmation line.
5. **Trigger disposition table** — the step most likely to be lost in derivation: name
   every scheduled trigger the archiving chat owns (dismantle) vs every sibling
   session's trigger (LEAVE IN PLACE), and the successor's re-arm duty. On 2026-07-11
   this distinction (this coordinator's cron + send_later chain dismantled; sim-lab's
   pacemaker deliberately untouched) existed only in chat until the close-out committed
   it.
6. **Heartbeat overwrite LAST**, phase ARCHIVE-READY, pointing at the note.

## Why it earns a file

The derivation cost two sessions of reconstruction and one near-miss (the Q-0265
continuous-chaining ruling was chat-only until #216's grep caught it). Every fleet lane
with a coordinator chat will eventually archive one; a named ceremony makes the next
archive a checklist run instead of an investigation, and makes "what did the archive
forget?" auditable — the note's confirmation line is the contract.
