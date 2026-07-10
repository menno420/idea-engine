# Idea probe / brainstorming simulator — link index + probe

> **State:** sim-ready
> **Class:** process · **Target:** `menno420/idea-engine` (battery + probe flow — see report Q7; the idea doc predates Q-0264 and named superbot)

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/idea-probe-brainstorm-simulator-2026-07-10.md`](https://github.com/menno420/superbot/blob/main/docs/ideas/idea-probe-brainstorm-simulator-2026-07-10.md)
— owner-raised 2026-07-10, status `ideas`, gate `ready`. Three modes: (1) question-battery
probe, (2) panel simulation (persona stress-test), (3) forward simulation (stretch).

## Probe report (v0, 2026-07-10)

*The battery probing itself — this report is also probe battery v0's reference example
(README § The probe battery). Everything below is grounded in the canonical doc linked
above, this repo's README, and `.sessions/2026-07-10-seed.md`; where something has not
been tried or measured, it says so.*

**1. What is this really?**
A reusable interrogation engine for ideas: a fixed question battery run against one idea,
emitting "the filled-in picture + a recommended way forward" (canonical doc §"The idea").
Its real substance is turning the Q-0254 understand-and-reflect *habit* into a *tool* so
"promotion quality stops depending on which agent happens to groom" (doc §"Why it's worth
having"). Modes 2–3 (panel, forward-sim) are depth extensions of the same engine, not
separate products.

**2. What is the possibility space?**
Three axes, all present in the doc: **depth** (single-pass battery → N-persona panel →
forward simulation of month 1); **surface** (internal idea grooming vs the public
suggestion-copilot skin — doc: "one engine, two skins", pointing at superbot's
`website-suggestion-copilot-2026-07-10.md`); **automation** (agent follows prose → skill
with battery-as-data → routine-invoked flow with parallel per-question-group agents, per
the doc's §"Sketch"). Adjacent and unclaimed by the doc: versioning the battery itself
(v0 → v1) so the method can evolve against evidence of which questions earn their keep.

**3. What is the most advanced capability reachable by the simplest implementation?**
Mode 1 as pure prose: the eight questions embedded as a numbered list in the consuming
repo's pipeline contract, executed by any agent in one pass, output appended to the idea
file. Zero code, no skill, no personas — yet it already produces the pipeline's core
artifact: a probe report ending in one routed recommendation. This document is the
existence proof: mode 1 shipped as ~15 lines of README (README § The probe battery) and
ran to completion on its first idea.

**4. What breaks it?**
- **Confident padding.** The battery asks; nothing checks answers against reality. A
  "filled-in picture" of invented specifics is worse than a blank — the format rewards
  fluent fabrication unless the honesty norm ("not measured" beats invention) is enforced
  by review, which in this pipeline happens only downstream (sim-lab / manager).
- **Battery drift.** The doc sketches the battery living in superbot; it now also lives
  in this repo's README. Two prose copies of a convention diverge without a checker
  (the drift class named in `.sessions/2026-07-10-seed.md`, superbot #880→#882).
- **Unmeasured mode escalation.** Panel mode multiplies agent/token cost; no evidence yet
  that it changes verdicts (not measured — that is exactly the sim question below).
  Forward-sim narrates fiction by design; without a "labelled-speculation" rule it can
  launder invented operational detail into evidence.

**5. What does it unlock?**
The whole idea-engine pipeline downstream of capture: every sim-ready outbox proposal is
the residue of a probe, so the outbox → sim-lab → manager flow (README §Pipeline position)
only carries traffic once this runs. Secondarily, per the doc: the suggestion-copilot
public skin reuses the same battery as its interview flow — build the question engine
once, expose it twice.

**6. What does it depend on?**
- A canonical battery text with one home — currently this repo's README § The probe
  battery (v0).
- Idea files following the idea grammar (README § Idea file grammar) so reports can be
  appended and states move forward.
- For panel mode: the fleet's judge-panel workflow pattern (doc §"Sketch": "the existing
  Workflow judge-panel pattern with ideation personas").
- For routine invocation: this repo's standing wake (armed at this boot — see
  `control/status.md`).

**7. Which lane should build it?**
The doc (written the morning of round-3 planning, before owner ruling Q-0264 created this
repo) says "Home: superbot (where docs/ideas/ lives), invoked by the Idea Engine's
routine." Q-0264 moved the ideation seat here, so the split is now: **idea-engine** owns
the battery and probe flow (mode 1 already lives in its README; mode 2 would be run by its
sessions); superbot builds nothing new for this; the public suggestion-copilot skin, if it
survives its own probe, targets the websites lane per its own idea file.

**8. What is the smallest shippable slice?**
Mode 1 over exactly one real idea: report appended to the idea's file, ending in one
recommendation, landed through the full merge path. That slice is this PR — shipped.

**Recommendation: sim-ready** — mode 1 is proven-by-use in this very report; the one open
question worth reproduced evidence is whether panel mode (mode 2) changes verdicts or
materially improves report quality enough to justify its multi-agent cost, and sim-lab can
settle that by running battery-only vs panel over a sample of superbot's existing backlog.
