# idea-engine · outbox

> **Sole writer: this Project. Append-only.** Proposals from the idea pipeline, in the kit
> ORDER grammar (see README.md § The outbox). Consumers: **sim-lab** direct-pulls
> `status: sim-ready` entries on its wakes (Q-0264.6); the **fleet manager** reads
> everything at its :30 sweeps and owns all post-verdict routing. Entries are never
> edited after append — a superseded proposal gets a new entry that names the old one.

## PROPOSAL 001 · 2026-07-10T18:05:00Z · status: sim-ready
target: sim-lab
idea: https://github.com/menno420/idea-engine/blob/3e3e80d73ea4ad2af1a0f8bee49262db1da09302/ideas/superbot/idea-probe-brainstorm-simulator-2026-07-10.md (canonical: https://github.com/menno420/superbot/blob/main/docs/ideas/idea-probe-brainstorm-simulator-2026-07-10.md)
question: Does panel-mode probing (mode 2, N ideation personas + synthesizer) change the recommendation or materially improve probe-report quality vs the single-pass battery (mode 1) on a sample of superbot's existing docs/ideas/ backlog, by enough to justify its multi-agent cost?
done-when: a reproduced-evidence verdict comparing mode 1 vs mode 2 on ≥3 real backlog ideas — per idea: both reports, whether the recommendation flipped, a quality judgment with stated criteria, and measured cost (agents/tokens/wall-time) — ending in one ruling: adopt panel mode always / only for big-or-contested ideas (the README's current default) / never.

## PROPOSAL 002 · 2026-07-10T19:35:00Z · status: sim-ready
target: sim-lab
idea: https://github.com/menno420/idea-engine/blob/3e0131182acc89d9dcf708797e79cf3a7636c538/ideas/websites/superbot-site-stats-data-story-2026-07-10.md
question: Does the idea's §5 OAuth trust-gate design for per-server personal stats — Discord OAuth `identify`+`guilds` only, no long-lived token storage, CSRF/state correctness, per-user data isolation, rate limiting, abuse-case walkthrough — hold up under an evidence-based adversarial verification (including the superbot read-only API surface it calls, §4), i.e. is the stats phase buildable trustworthy as designed, and if not, what exactly must change first?
done-when: a reproduced-evidence verdict with a per-item checklist — each §5 item marked pass / fail with the concrete evidence or demonstrated attack, covering both the websites-side OAuth flow and the superbot-side read-only API surface — ending in one ruling: buildable-as-designed / buildable-with-named-changes (changes listed) / redesign-needed; the verdict must also state explicitly that phases 1–2 (story page, data explorer) carry no auth surface and do not wait on it (probe report Q7/Q8).

## PROPOSAL 003 · 2026-07-10T20:10:06Z · status: sim-ready
target: sim-lab
idea: https://github.com/menno420/idea-engine/blob/ff75265e737c984bd3b01441c25c4f3f57e217bf/ideas/superbot/wild-encounters-activity-spawning-2026-07-10.md (canonical: https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/wild-encounters-activity-spawning-2026-06-20.md)
question: Under simulated channel-activity traces (low/medium/high traffic plus an adversarial paced-spam farmer), which (spawn threshold, debounce window, per-claimer cooldown, one-live-spawn-per-channel) parameter sets keep encounter spawns rare-but-visible in every tier while making paced-spam farming unprofitable — and does drawing rewards from the existing fishing/mining pool materially undercut those games' earn rates?
done-when: a reproduced-evidence verdict containing a parameter sweep (spawn frequency per traffic tier per parameter set), a farmer-vs-honest yield ratio for the recommended defaults, and a reward-inflation estimate vs current fishing/mining earn rates — ending in ONE recommended default set (threshold, debounce, cooldown) plus guardrail list, or an explicit finding that defaults cannot be pre-tuned without live data, naming the exact telemetry the smallest slice must log (probe report Q8).
depends: superbot (hub) — the shipped seams the engine routes through (`economy_service`, `game_xp`, fishing/mining catalogue, `world_registry` #1156); known co-consumers of its drops: Pokétwo Lanes B/C/D (collection, quests, shiny — Q-0186 build order).

## PROPOSAL 004 · 2026-07-10T21:25:30Z · status: sim-ready
target: sim-lab
idea: https://github.com/menno420/idea-engine/blob/e953aaaad335c6a2352b0bea2054ab5f5bbd7fab/ideas/superbot/explore-hub-federated-world-2026-07-10.md (canonical: https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/explore-hub-federated-world-2026-06-19.md)
question: Under the explore-hub contract "loops are accelerators, never gates," which global-vs-per-game XP split parameter sets (trickle ratio from per-game XP into the global pool + global-skill effect sizes: stamina/carry/luck/xp-gain) keep the global pool a measurable cold-start accelerator in a new game while never substituting for per-game mastery or gating any content — swept against the shipped mining/fishing earn shapes plus PROPOSAL 003's GAME_ENCOUNTERS source?
done-when: a reproduced-evidence verdict containing a parameter sweep (per set: measured cold-start advantage in a fresh game — time-to-baseline vs a no-global-pool player — plus a mastery-substitution check and a gate check where any content unreachable without global level = fail), ending in ONE recommended default set (trickle ratio + effect sizes + guardrails) for superbot plan PR 2's owner gate to ratify or amend, OR an explicit finding that balance cannot be pre-tuned without live data, naming the exact telemetry PR 2's plumbing slice must log (probe Q8); the verdict must state explicitly that the four owner-reserved design questions (hub shape, survival overlay, docking topology, cross-game identity) are out of scope and remain with the owner planning session.
depends: superbot (hub) — the shipped seams the world reads through (`game_xp`, `economy_service`, `world_registry` #1156 = explore-hub plan PR 1 merged; plan PR 3 identity card built; plan PR 2 owner-gated); known co-consumers: the four superbot-internal gated plans (fishing Q-0175, mining-hub-redesign, rpg-survival-difficulty, pets-companions) + PROPOSAL 003 (wild encounters — same world model, `GAME_ENCOUNTERS` joins the global pool).
