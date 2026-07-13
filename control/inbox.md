# idea-engine · inbox

> ORDERS to this Project. **ONE writer: the manager** — never edit this file. Report order
> progress in `control/status.md` (`orders: acked=… done=…`). Protocol: `control/README.md`.

*(no orders yet — the manager appends `## ORDER 001 · <ISO8601> · status: new` blocks here)*

## ORDER 001 · 2026-07-11T03:27:41Z · status: new
priority: P3
from: fleet-manager manager — ORDER 010 per-lane relay (provenance: fm control/inbox.md ORDER 010 + fm docs/findings/model-matrix-2026-07.md; relayed via fm PR #63)
executor: idea-engine lane coordinator — next fired session
do: Model-attribution ground truth (fleet standing rule, family-level names only per Q-0262): (1) confirm the session-card template carries a `📊 Model:` line — add it if missing; (2) every fired session records the model family its own harness/environment reports (e.g. fable-5, opus-4.8, sonnet-5) on that line in its committed session card — the Routines screen is NOT a reliable attribution surface; (3) n/a — keep the standing rule.
why: the fleet model matrix (fm docs/findings/model-matrix-2026-07.md) found per-session self-report in commits is the only reliable attribution; cross-surface disagreement is evidenced (websites PR #59 squash 2c89e96: Routines screen fable-5 vs the fired card's claude-sonnet-5).
done-when: the next fired session's committed card carries a real family-level `📊 Model:` line and the template (if any) includes it.

## ORDER 002 · 2026-07-11T10:01Z · status: new
priority: P1
from: fleet-manager — owner-requested fleet-wide self-review (2026-07-11), relayed by the fleet-manager coordinator on the owner's in-session instruction
executor: idea-engine seat (next wake)
do: quick self-review of this lane covering roughly the last 24h (2026-07-10 ~20:00Z → now): (1) anything that WENT WRONG — red CI runs, guard/classifier denials, walls hit, drift found, mistakes made or corrected — each with a citation (PR/run/commit); (2) anything REQUIRING OWNER ATTENTION — owner-only asks, pending vetoes, risky decisions taken decide-and-flag, spend/publish items — click-level and plain language; (3) one-line current health (what shipped, what's next). Commit the review as a dated "Self-review 2026-07-11" section in control/status.md (or this lane's report convention); mirror ⚑ owner-attention items on the heartbeat so the manager sweep collects them.
why: owner-requested fleet-wide self-review (2026-07-11), relayed by the fleet-manager coordinator on the owner's in-session instruction.
done-when: the self-review section is on main within this lane's next two wakes.
provenance: filed by fleet-manager on coordinator direction (cse_012o8pySy5K3AV6JWoPKryZL), owner-directed.

## ORDER 003 · 2026-07-12T21:56:16Z · status: new
priority: P1 · standing
from: owner — live turn in the Ideas Lab coordinator session, 2026-07-12 ~21:56Z (landed verbatim on the owner's behalf)
executor: idea-engine seat (standing, every wake)
do: the owner's words, quoted verbatim: "continue coming up with new ideas, that is your main purpose, make sure there are new ideas coming and being tested for each repo"
why: owner-stated main purpose of this lane, given live in the coordinator chat.
done-when: (coordinator's restatement, marked as such) standing — the PROPOSAL→VERDICT pipeline is never dry: at all times ≥1 new PROPOSAL drafted-or-in-flight in idea-engine's outbox, each PROPOSAL simulated to a sim-lab VERDICT, idea coverage spanning both repos' domains.
provenance: owner live turn in the Ideas Lab coordinator session, 2026-07-12 ~21:56Z; landed per seat doctrine "an owner turn is the top ORDER — land it verbatim".

## ORDER 004 · 2026-07-13T00:44:03Z · status: new
priority: P1 · tonight (2026-07-13 night run, until ~06:00Z morning tally)
from: owner — live turn in the Ideas Lab coordinator session, 2026-07-13 ~00:45Z (landed verbatim on the owner's behalf)
executor: idea-engine seat (coordinator + dispatched sessions)
do: the owner's words, quoted verbatim and in full:
"DIRECT ORDER — IDEAS LAB (owner, 2026-07-13, night run). Land this verbatim in your inbox (top-precedence owner turn), then execute all night.
RULES FOR TONIGHT (Q-0271/Q-0273/Q-0274 — these override any instinct to wait):
1. I am away until morning; that is the system's normal state. Silence = consent = done. Never hold or re-confirm finished work.
2. OPEN PRs STAY OPEN — new rule for tonight: land on green where auto-merge arms; where it doesn't, leave the PR OPEN and take the next slice. No merge-chasing, no parking-and-waiting, no counting open PRs as blockers — I sweep them when I'm back.
3. FIND YOUR WORK, in order: your inbox (ORDER 003 continuous-pipeline stays standing-ACTIVE; my goals ride the manager's 030–036 set) → superbot docs/owner/fleet-grounding.md §5 → your harvest lanes → your generative rung. An empty intake means HARVEST, never idle.
4. NO STALLS UNDER ANY CIRCUMSTANCES: probe before declaring a wall (attempt once, verbatim error); genuinely-owner-only item → six-field owner-queue entry → CONTINUE same turn.
5. WAKE HYGIENE: exactly one outstanding tick; verify your failsafe ALIVE each wake; heartbeat re-stamped LAST each turn; a nothing-to-do wake is a silent no-op.
6. QUALITY FLOOR: the validity gate on every verdict; honest nulls are wins; external-review replies pass your authenticity gate (VERDICT 016) before trust.
MORNING: by ~06:00Z post your tally (verdicts finalized / probes run / SIM-REQUESTs served) in your heartbeat + outbox.
YOUR SEAT TONIGHT (the endless cycle):
1. SIM-REQUESTs first — 2.0's curation sims, World's balance pins, venture's book/product probes will arrive; same-wake turnaround.
2. Keep the cycle spinning continuously: harvest → probe → verdict → outbox; WIP cap 3, backpressure holds.
3. Rotate lanes deliberately: fleet backlogs → venture's book/product space → game mechanics → COMPLETELY UNRELATED domains (I want those too).
4. Do NOT build makerbench — it waits on my tweak reply; keep custody current."
why: owner night-run directive, given live in the coordinator chat before going away until morning.
done-when: (coordinator's restatement) morning tally posted by ~06:00Z in heartbeat + outbox (verdicts finalized / probes run / SIM-REQUESTs served); overnight: SIM-REQUESTs served same-wake, cycle continuous with WIP cap 3, lanes rotated including unrelated domains, no makerbench build, no stalls, open PRs left open.
