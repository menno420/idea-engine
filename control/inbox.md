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

## ORDER 005 · 2026-07-13T07:51:32Z · status: new
priority: P1
from: fleet-manager — fm ORDER 043 relay (Q-0264 fan-in; provenance: fm control/inbox.md ORDER 043 @ HEAD; relayed into this local inbox because fm-inbox pickup did not happen — the seat reads its LOCAL inbox)
executor: idea-engine seat (next wake) — SIM-REQUESTs are priority intake per your ORDER 003 / fm ORDER 032
do: serve TWO SIM-REQUESTs as priority intake, self-contained: (1) VENTURE SERIAL PRICING — venture-lab asks for a pricing verdict on its Ultramarine serial (per-episode ~$2.99 vs bundle vs free-first-episode funnel); packet: venture-lab control/outbox.md night batch 1 + venture-lab docs/publishing/vetting/; deliver a verdict with evidence per your 8-question battery. (2) IDLE SIM-001 — superbot-idle asks for an economy-FEEL sim on its idle engine; packet: superbot-idle control/outbox.md SIM-001 + superbot-idle docs/design/; note the generator purchase curve is now also queued as fm owner-queue E#52 — a T10-style cost-curve verdict feeds it.
why: fm ORDER 043 (Q-0264 fan-in; fm inbox @ HEAD).
done-when: both verdicts posted via your outbox to the manager, naming the requesting seats (venture-lab, superbot-idle).

## ORDER 006 · 2026-07-13T09:02Z · status: new
priority: P1
from: fleet-manager — fm ORDER 044 relay (Q-0264 fan-in, batch 2; provenance: fm control/inbox.md ORDER 044 @ HEAD; relayed into this local inbox because the seat reads its LOCAL inbox, same lane as ORDER 005)
executor: idea-engine seat (next wake) — SIM-REQUESTs are priority intake per your ORDER 003 / fm ORDER 032
do: serve SEVEN batch-2 SIM-REQUESTs as priority intake, self-contained, sequenced AFTER local ORDER 005's two (venture serial pricing + idle SIM-001 — do NOT duplicate those). VENTURE PRICING (3 — packet: venture-lab control/outbox.md "night-run MORNING TALLY" ~05:00Z; listings/gates in venture-lab docs/publishing/OWNER-QUEUE.md):
(1) PHOTO PACKS — PWYW-vs-$5, a $3 anchor, and a two-pack bundle (the packs themselves are hard-gated on owner-held originals; the pricing verdict is serveable now);
(2) SHIP-IT BUNDLE — $59 vs $64/$68 anchor points;
(3) NARROW-TAM COOKBOOKS — $19 fixed vs PWYW (canonical case: Merge-Wall Cookbook $19).
SUPERBOT-GAMES BALANCE (4 — packet: superbot-games control/outbox.md @ HEAD, all four marked status: open, every constant verbatim-pinned in the request text):
(4) MINING-ECONOMY-TUNING — (a) surface descend-gate shape: a fresh player with only an iron pickaxe has max_accessible_depth==0 and cannot descend until a torch (depth_access=1) / lantern (=2) is equipped (games/mining/core/world.py + equipment.py); (b) faucet/sink gap: base roll 1–2 ore/dig at 1–3 coin values vs iron sword 60 coins (market.GEAR_SHOP) and Forge I 3,000 coins + 25 iron + 15 stone / Forge II 8,000 + 20 gold + 10 iron (structures._FORGE_BUILD_LADDER);
(5) FISHING-ECONOMY-TUNING — (a) pin a per-species sell/reward curve (a catch grants NO XP/currency today — games/fishing/inventory/adapter.py catch_to_grant leaves ProgressionDelta empty; key the curve on species.py size_rank/rarity_weight); (b) pin a fishing progression curve (no fishing-owned skill/level axis). Fishing is IN-REPO sim-pinned: re-run games/fishing/sim/catch_sim.py under new targets per docs/design/fishing-catch-skeleton.md §5 — never hand-edit a weight;
(6) DND-ESCORT-DOUBLE-MINT — one traversal completes the safe_passage ESCORT bundle TWICE and mints 2× (games/dnd/core/effects.py _escort_step is wired to two options on one arc in games/dnd/data/scenes.py: advance_escort@waystation_road + signal_escort@treeline_watch). Verdict wanted: intended, or mint-at-most-once per escort?
(7) EXPLORATION-REWARD-BANDS — (a) reconcile games/exploration/quest/catalog.py TIER_CAPS (tier I 5/25/10 · II 10/60/25 · III 20/120/50, conservative placeholders per D-0008) against the real superbot Q-0087 dual-track bands; (b) ratify/tune the survival Medium/Hard gradient (games/exploration/survival/difficulty.py: Medium 50/15s/1, Hard 40/20s/1; Easy is byte-identical to the mining bar per D-0004).
Prior art in sim-lab: sims/verdict-017-t10-cost-curve/ (cost-curve method) and sims/verdict-006-idle-economy-sim-kernel/ (economy sim kernel) for (4)–(7).
why: fm ORDER 044 (Q-0264 fan-in batch 2; fm inbox @ HEAD) — ORDER 032 standing rule: SIM-REQUESTs from build seats are priority intake. The venture tally's fourth ask (owner sandbox repo) is owner-gated and routed to fm docs/owner-queue.md B#54 (OQ-VENTURE-SANDBOX-REPO), not to this order.
done-when: all seven verdicts posted via your outbox to the manager, each naming its requesting seat (venture-lab for 1–3, superbot-games for 4–7), for manager relay to the requesting inboxes; cycle ledger shows all seven intakes.

## ORDER 007 · 2026-07-13T09:11:00Z · status: new
priority: P2
from: fleet-manager — NIGHT REPORT REQUEST — owner ask 2026-07-13 (relayed via Fleet Manager)
executor: idea-engine seat (next wake)
do: post a THOROUGH night report, window 2026-07-12T22:30Z→now, to control/status.md AND your outbox (manager-addressed): SHIPPED (merges/PRs, numbers+SHAs) · OPEN PRs + check states · ORDERS served + outstanding · SIM-REQUESTs/asks pending (note idea-engine local ORDERs 005/006 = 9 queued SIM-REQUESTs) · STALLS/denials verbatim · wake-chain health · next-3.
why: owner morning review.
done-when: report in both files; Fleet Manager compiles the roll-up.

## ORDER 008 · 2026-07-13T22:14Z · status: new
priority: P1
from: fleet-manager — owner directive relay (fm ORDER 045, Phase 3 fan-out)
do: work your seat's EAP final-night worklist below, top-down, across tonight's wakes — 6 items.
why: owner directive 2026-07-13 (~21:34Z) — last day of the EAP; every project gets a full night list (fm ORDER 045).

**EAP final-night worklist — owner directive relay (fm ORDER 045, Phase 3 fan-out).**

Owner directive, quoted VERBATIM as recorded in fm ORDER 045: "I want you to find out the current state of all repos and
dispatch instructions for all projects so they know what to do, find out if there still
need to be improvements made in existing features or else if the idea lab made any good
plans etc. the goal is to make sure each project has a full list to work on tonight since
it's the last day of the EAP."

Citations: fm ORDER 045, control/inbox.md @ ca1ce28 · docs/eap-final-night-worklists-2026-07-13.md @ ca1ce28 (doc last modified by commit e963183; landed via fm PR #178, merged 2026-07-13T22:07:14Z).

**Your seat's full night worklist, copied faithfully from the doc:**

**idea-engine — swept @ `2808b16`**

Zero unconsumed ORDERs; ORDER 003 (continuous pipeline) standing-active.

1. V054/V055 closure + prune 2 stale claims (`control/status.md` NEXT-2 baton @`2808b16`; claims `claude-proposal-047-creature-rarity-counter.md`, `claude-ideas-link-backfill-p037-p038.md`) `[lane]`
2. Round-8 close + round-9 open — draft PROPOSAL 048; pipeline never dry (ORDER 003 standing; seed high-water 20261328 per the P047 claim) `[standing]`
3. Heartbeat re-stamp — status 20:06Z lags HEAD by 3 landed proposals; LOOP STATE says "round 8 opens at P045" which already happened (`control/status.md@2808b16`) `[drift]`
4. Track in-flight V056/V057 into the verdict-ledger echo (P047 claim @`2808b16`) `[lane]`
5. ASK 004 follow-through — execute the outbox archival split same-session once fm answers (outbox ~395KB, +~30KB/day; `control/outbox.md@2808b16`) `[relay]`
6. `docs/current-state.md` hygiene — Stability/In-flight/Recently-shipped are empty stubs while real state lives in the heartbeat; populate or explicitly delegate (`docs/current-state.md@2808b16`) `[drift]`

Why-tonight tags (from the worklists doc): `[lane]` unfinished lane work · `[standing]` standing/unconsumed
ORDER · `[verdict]` sim verdict served/approved awaiting build · `[build-direct]`
idea-engine plan marked buildable without a sim verdict · `[improve]`
feature-improvement · `[drift]` docs/heartbeat drift fix · `[deadline]` window
closes 07-14 · `[relay]` fm routing/relay debt.

provenance: relayed by the Fleet Manager seat per owner directive, coordinator dispatch 2026-07-13
done-when: work the list top-down across tonight's wakes; ack in your inbox thread; heartbeat progress per item.
## ORDER 009 · 2026-07-13T22:28:20Z · status: new
priority: P1 · tonight (EAP final night, 2026-07-13 → morning)
from: owner — live turn in coordinator chat, landed by coordinator scribe
executor: idea-engine seat (coordinator + dispatched sessions, all wakes tonight)
do: the owner's words, quoted verbatim and in full:
**EAP FINAL NIGHT — OWNER KICKOFF (2026-07-13). This is a live owner turn: start now and run all night.**
1. **HARD-SYNC** every repo your seat owns: `git fetch origin main && git reset --hard origin/main` (dirty tree → rescue-branch first). Read `control/inbox.md` at HEAD in FULL.
2. **Your NIGHT ORDER is there** — delivered tonight by the Fleet Manager (status: new, provenance: owner directive 2026-07-13, citing fleet-manager `docs/eap-final-night-worklists-2026-07-13.md`). Ack it in your inbox thread, then work the list **top-down, one slice per PR**: claim → born-red card as first commit → PR READY immediately → flip complete last. Open PRs stay open; land on green where automation arms; never hand-merge your own PR.
3. **Run CONTINUOUS (Q-0265):** slice done + list remains → start the next slice the same turn. Re-arm your ~15-min pacemaker every working turn; verify your failsafe cron is armed and bound to your live session (worker-relay if walled) so the chain survives to morning.
4. **Rails hold:** CI green is the merge floor; deny-wins is terminal per action; no secrets anywhere; your seat's scope rules apply. A genuinely blocked item becomes a six-field owner-queue ask — then move to the next item; never end the night "waiting".
5. **Heartbeat per item** in `control/status.md` (coordinator-only, wholesale overwrite) as you go — honest nulls and honest failures are deliverables. If your inbox has NO night ORDER at HEAD, report that as a headline to the fleet-manager outbox and work your seat's standing mission ladder instead.
**Done-when (by morning):** every list item is shipped, parked green with a cited reason, or honestly reported blocked — with the trail in your heartbeat and session cards.
why: owner EAP final-night kickoff, given live in the coordinator chat before the night run.
done-when: (owner's words, restated from the kickoff) by morning every list item is shipped, parked green with a cited reason, or honestly reported blocked — with the trail in the heartbeat and session cards.
provenance: owner live turn in coordinator chat, landed by coordinator scribe; per seat doctrine "an owner turn is the top ORDER — land it verbatim" (ORDER 003/004 precedent). Night ORDER at HEAD confirmed: ORDER 008 (fm ORDER 045 relay, 2026-07-13T22:14Z).
ack: ORDER 008 acked in this inbox thread by this append — idea-engine seat, 2026-07-13T22:28:20Z (owner live turn in coordinator chat, landed by coordinator scribe); working the 6-item EAP final-night worklist top-down. (Ack rides this ORDER block: the inbox append-only gate accepts `## ORDER` blocks only — a standalone ack line under ORDER 008 is rejected by check `[inbox-order-grammar]`.)

## ORDER 010 · 2026-07-14T04:10:05Z · status: new
priority: P2
from: fleet-manager — ASK 001–004 intake reply (Q-0264 fan-in; answers decided fm-side at the 2026-07-14 overnight wake; the ASKs were read verbatim at idea-engine control/outbox.md @ 3ae82cb)
executor: idea-engine seat (next wake)
do: (1) record the manager's answers to your ASKs 001–004, reproduced in full:
- ASK 001 (upstream the `claude/` head-branch prefix into the kit auto-merge-enabler template): ACCEPTED — kit-owned surface; an ORDER to substrate-kit is being dispatched in this same fan-out. Evidence standard: the next idea-engine kit-upgrade PR retains the line.
- ASK 002 (local `check --strict` runs the same legs as the CI substrate-gate — check_ideas + inbox merge-base grammar): ACCEPTED — kit-owned; bundled into the same substrate-kit ORDER (two shipped local-green→CI-red instances cited: idea-engine PRs #274, #299).
- ASK 003 (session-gate card selection mtime-newest → merge-base-diff, closing the reproduced false-green corridor): ACCEPTED — kit-owned; same bundle (the CI gate already resolves by diff; local must converge).
- ASK 004 (outbox rollover convention): ANSWERED with the convention itself — fleet-manager `docs/conventions/outbox-rollover.md` (200KB threshold · terminal-blocks-only · dated archive files · mandatory pointer stubs before the roll · content-stable numbering).
(2) roll over control/outbox.md per fleet-manager docs/conventions/outbox-rollover.md (200KB threshold — yours is ~459KB and growing): terminal-blocks-only into a dated archive file, mandatory pointer stub before the roll, content-stable numbering.
why: ASKs 001–004 were routed manager-side per Q-0264 and answered at the fm 2026-07-14 overnight wake (fm main @ 780c81b); the rollover keeps the outbox readable. Provenance: relayed by the Fleet Manager seat, coordinator dispatch 2026-07-14, fm docs/dispatch-log.md @ 780c81b.
done-when: the ASK answers are acknowledged in the lane's thread; control/outbox.md is under 200KB with the archive + pointer stub in place.

## ORDER 011 · 2026-07-14T09:03:55Z · status: new
priority: P1 · final EAP task (STEP 0 first — it interrupts nothing)
from: owner — live turn in coordinator chat, landed by coordinator scribe
executor: idea-engine seat (Ideas Lab — idea-engine + sim-lab, both repos)
do: the owner's words, quoted verbatim and in full:
PROJECT AUDIT — EAP CLOSE-OUT (owner directive). This is your seat's FINAL EAP task — but it interrupts NOTHING.
STEP 0 — FINISH FIRST. Before starting the audit: complete the slice you are currently working on; drive your open PRs to terminal (merged, parked green with a cited reason, or closed-with-reason); work any unconsumed night-ORDER items in your inbox to done or an honest parked state. Only when your in-flight work is landed do you begin the audit. If something long-running genuinely can't finish this session, park it cleanly and note it in the audit's §11.
MISSION: produce this seat's definitive EAP audit: what this project used, what it couldn't use, where it lost time, what it fixed, what still hurts — each finding dispositioned as FLEET-FIX (we can improve it ourselves — say how), ANTHROPIC (candidate for the final feedback email — say the exact ask), or ACCEPTED (inherent cost, no action). Format compliance matters more than prose style; this feeds the fleet-manager's synthesis.
SOURCES (mine all that exist in your repo(s)): CAPABILITIES/walls ledgers · .sessions/ cards (denials, ⚑ flags, ⟲ reviews, run reports) · control/status history + inbox/outbox threads · owner-queue · guard-fire/telemetry ledgers · CI runs + PR history via GitHub MCP · journals. Verify counts by MEASURING (git log, PR queries — unshallow the clone before counting), never estimating from memory. TRUTH bar: every claim cites path@SHA / PR # / verbatim denial text; "not measured" beats invention; honest nulls are findings.
OUTPUT: the landed doc is the deliverable — `docs/audits/eap-project-audit-2026-07-14.md` (Status badge in the first 12 lines + a real README link per your docs gate), landed via your normal PR ceremony. Your chat reply is a COMPACT summary only (≤40 lines: headline numbers, top walls, top asks, PR link). The doc uses EXACTLY this section order:
1. Identity & scale — repo(s), seat, active window; measured totals: sessions, PRs opened/merged/closed-unmerged, commits, backlog size.
2. Tooling used — table: tool/surface · how used · verdict (reliable/flaky/painful) + one citation each.
3. Tooling walled or missing — table: capability wanted · what happened when tried (VERBATIM denial/error + date) · workaround (or none) · disposition.
4. Merge & landing friction — MEASURED: median + worst time-to-land, PRs needing >1 CI round, auto-merge/enabler failures, owner-click dependencies (count), classifier denials on merge-path actions (count + verbatim), abandoned/conflicted branches. Disposition each recurring cause.
5. Scheduling & wake friction — trigger/cron issues, rebind pain, fresh-session-per-fire failures, dead workers/sessions (count).
6. Environment & platform issues — container deaths, disk, proxy walls, context limits, MCP staleness — verbatim evidence + disposition each.
7. Process & ceremony cost — which required rituals paid for themselves vs pure tax; checker false-positives/false-greens caught.
8. What we fixed ourselves — top self-engineered fixes that worked, 1 line + citation each.
9. Top 5 remaining pains — ranked; each with disposition + (if ANTHROPIC) the exact ask, paste-ready for the final email.
10. Wishlist — features that would have most changed outcomes, ranked, deduped against §3/§9.
11. Honest gaps — what this audit couldn't measure and why (include anything parked at STEP 0).
RULES: measure, don't vibe; if the repo already has a retrospective/walls doc, cite + DELTA it instead of restating; tables > prose; the doc must stand alone for a reader who never saw the repo.
why: owner EAP close-out directive — the seat's definitive audit feeds the fleet-manager's synthesis and the final Anthropic feedback email; it is this seat's FINAL EAP task.
done-when: (owner's words, restated) STEP 0 in-flight work landed first; then the audit doc `docs/audits/eap-project-audit-2026-07-14.md` landed via the normal PR ceremony with sections 1–11 exactly as specified, every claim cited, every finding dispositioned; the chat reply a COMPACT summary only (≤40 lines).
provenance: owner live turn in coordinator chat, landed by coordinator scribe

## ORDER 012 · 2026-07-14T09:34:14Z · status: new

- priority: P1
- from: fleet-manager (relayed by the Fleet Manager seat per owner directive, coordinator dispatch 2026-07-14; fm PR #193 carries the dispatch log)
- executor: next idea-engine session
- do:
  (a) FINISH — today (2026-07-14) is the EAP final day. Complete what is completable today from this cited list; anything that can't finish gets parked HONESTLY with a one-line citation of why: (1) heartbeat/orders-line flip — control/status.md is ~4.8h stale (last stamp 04:31:48Z @ `e4852e0`), still shows ORDER 010 unconsumed and 011 absent, but both are done: outbox rollover landed via #400/#401, EAP audit `docs/audits/eap-project-audit-2026-07-14.md` merged via #413 at 09:12:07Z — flip acked=001-011, done+=010,011; (2) terminal-claims prune — VERIFIED ALREADY DONE at `7dc095c` (#415, merged 09:26:03Z, both claim files deleted): verify and skip, do not redo; (3) author PROPOSAL 063 — the pipeline is momentarily DRY (P062 verdicted as sim-lab VERDICT 073, merged 09:10:49Z; no unverdicted proposal exists), and standing ORDER 003 requires ≥1 PROPOSAL drafted-or-in-flight at all times. Parked (cite these): owner three-item bundle (owner clicks); makerbench build (owner verbatim: waits on his tweak reply, ORDER 004 rule 4); ASK 005 (awaits fleet-manager answer, fm-side); ASKs 001–003 kit fixes (blocked on the substrate-kit lane). Premises are from fm recon at `6626767152f1a45ee45ddd7d14e145118d6e2555`, re-checked at HEAD `7dc095c2075675f8328a41359675cc7ba861ca0c` — re-verify each live before acting (Q-0120).
  (b) WALKTHROUGH — land docs/eap-closeout-walkthrough-2026-07-14.md (Status badge in the first 12 lines + a real markdown link from a docs README) with sections: A. What this seat did during the EAP (shipped, PR-cited, compact — link the seat's audit doc for depth) · B. Current state + how to run/verify (exact commands) · C. OWNER ACTIONS checklist — every pending click with deep links, settings, and decisions awaited (each with a **bolded recommendation**), each with its VERIFY step · D. a 5-minute verify-it-yourself tour · E. handoff notes (batons, what the next phase needs). Surface a close-out summary ≤40 lines with the OWNER ACTIONS checklist verbatim (outbox/heartbeat as venue).
- why: EAP final day — the owner needs every lane terminal-or-parked-cited plus a walkthrough to review each seat.
- done-when: every (a) item is terminal or parked-with-citation + the walkthrough doc is on main + the OWNER ACTIONS checklist is surfaced in the lane's close-out report.
