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
