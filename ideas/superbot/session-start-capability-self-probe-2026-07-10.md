# Idea — session-start capability self-probe (know your own toolset before you plan) — link index

> **State:** parked(folded — probed 2026-07-10 jointly with `project-capability-self-awareness-2026-07-10.md` (one possibility space, flagged at harvest by PR #26): this is the AGENT-plane half of the same capability-self-awareness surface — see the pointer disposition below and the primary battery there)
> **Class:** process · **Target:** `menno420/superbot`
> **Sequence:** behind project-capability-self-awareness-2026-07-10.md (the owner-raised fleet-wide restatement with the concrete kit home — the pair was probed as one surface, primary battery on that file)

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/session-start-capability-self-probe-2026-07-08.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/session-start-capability-self-probe-2026-07-08.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/session-start-capability-self-probe-2026-07-08.md)).

A session-start capability self-probe: multiple EAP findings came from sessions not knowing their own toolset (a coordinator without Bash, a documented-but-absent send_later) until after they had planned around it.

## Probe disposition (2026-07-10 — pointer, not a battery)

> **Grounding:** https://raw.githubusercontent.com/menno420/superbot/9624c5399f5b1a3da293c07ce930e8b0410d79e4/docs/ideas/session-start-capability-self-probe-2026-07-08.md@9624c53 · fetched 2026-07-10T22:10Z

Probed 2026-07-10 as one half of the batched capability pair; the full battery-v0
report lives on [`project-capability-self-awareness-2026-07-10.md`](project-capability-self-awareness-2026-07-10.md)
(this PR), whose Q2 decomposes the shared surface into two probe planes. This idea IS
the **agent plane**: an in-session, session-start toolset checklist (scheduler tools,
GitHub MCP, Bash, subagent spawn) — the plane a kit `bootstrap.py` subprocess
physically cannot reach (MCP tools are model-invoked), and the plane where the founding
incident lives (sim-lab's coordinator/worker `create_trigger`/`send_later` split; the
canonical doc's own Bash-less-coordinator and phantom-`send_later` findings). It is not
superseded by the newer owner-raised restatement — it is that idea's complementary
half, so it folds rather than probes separately: same routing (substrate-kit owns the
carrier — the kit `session-start` injection is the natural home for the checklist,
per primary Q6/Q7), same evidence question (is a recorded capability answer honest
across seat types — PROPOSAL 005, whose done-when names this checklist as the
agent-plane battery for sim-lab's two-seat reproduction), no second proposal earned.
Canonical doc byte-identical at pin `fd638e3` vs superbot HEAD `9624c53` (equal
sha256 `06d3158…`, verified 22:10Z) — the harvest gist above stays faithful.

**Recommendation: park** — folded into the primary: it is the agent-plane half of one
surface, carried forward by PROPOSAL 005's done-when (the sim reproduction runs this
checklist) and the same substrate-kit routing; a separate battery would duplicate the
primary's report, and a separate proposal would double-bill sim-lab for one question.
