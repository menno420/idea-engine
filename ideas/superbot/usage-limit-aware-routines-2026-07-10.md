# Usage-limit-aware routines and orchestrations — link index

> **State:** parked(routed — post-EAP routine posture is an owner decision, needed ≤2026-07-13; mechanical limit-deferred half already superbot's plan @ superbot PR #1845)
> **Class:** process · **Target:** `menno420/superbot`
> **Sequence:** before EAP-window-wrap-2026-07-14

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/usage-limit-aware-routines-2026-07-07.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/usage-limit-aware-routines-2026-07-07.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/usage-limit-aware-routines-2026-07-07.md)).

A 4-agent workflow died silently when the account hit the usage limit and 'completed' with an empty result set; make routines and orchestrations limit-aware (detect, defer to reset, report). Promoted to a superbot plan (PR #1845).

## Probe report (v0, 2026-07-11)

> **Grounding:** https://raw.githubusercontent.com/menno420/superbot/9f46cb7840cb2216a012002fe27feb342d45f480/docs/ideas/usage-limit-aware-routines-2026-07-07.md@9f46cb7 · fetched 2026-07-11T14:19:16Z
> *(pin annotation: superbot live HEAD S = `9f46cb7840cb2216a012002fe27feb342d45f480` by `git ls-remote` 14:19:01Z; the canonical idea still exists at S and still carries its PROMOTED banner pointing at the plan — "PROMOTED → plan (2026-07-08, grooming wave-1 lane C, PR #1845)".)*
> **Grounding:** https://raw.githubusercontent.com/menno420/superbot/9f46cb7840cb2216a012002fe27feb342d45f480/docs/planning/usage-limit-aware-routines-plan-2026-07-08.md@9f46cb7 · fetched 2026-07-11T14:19:17Z
> *(pin annotation: the promoted plan @ S — the limit-deferred / send_later-at-reset pattern is layer 1, verbatim: "schedule a self check-in (`send_later`) at the stated reset time + 2 min, note `limit-deferred` on the run report, and resume there."; the observed failure is in it verbatim too: "all four lanes returned `You've hit your session limit · resets 5:40pm (UTC)` and the workflow completed \"successfully\" with an **empty result set**".)*
> **Grounding:** https://raw.githubusercontent.com/menno420/fleet-manager/7c13be74b8eca2c62cf0118b9473e049ef479b7f/docs/findings/fleet-economics-2026-07.md@7c13be7 · fetched 2026-07-11T14:19:41Z
> *(pin annotation: fm live HEAD F = `7c13be74b8eca2c62cf0118b9473e049ef479b7f` by `git ls-remote` 14:19:01Z; the honest-nulls rule holds at F, verbatim: "Actual CI minutes, token spend, and dollar costs are **NOT visible to agents** from any surface reachable this session — every such cell says \"not measurable\"".)*
> **Grounding:** https://raw.githubusercontent.com/menno420/fleet-manager/7c13be74b8eca2c62cf0118b9473e049ef479b7f/docs/roster.md@7c13be7 · fetched 2026-07-11T14:19:41Z
> *(pin annotation: roster Generation #5 (generated-at 2026-07-11T04:28Z) @ F, trigger-evidence line verbatim: "324-record export, **32 enabled**: 15 standing crons + 2 poke-only + 15 one-shots.")*
> **Grounding:** https://raw.githubusercontent.com/menno420/fleet-manager/7c13be74b8eca2c62cf0118b9473e049ef479b7f/docs/dispatch-log.md@7c13be7 · fetched 2026-07-11T14:19:42Z
> *(pin annotation: dispatch-log line 107 @ F, verbatim: "EAP window **EXTENDED to 2026-07-14** — Anthropic email 2026-07-09 22:29Z".)*

> Single-pass battery (panel not escalated: docs/routing surface, reversible, no
> security/data/spend/public blast radius). Verify-first grounding all live this
> probe (2026-07-11 14:19Z, pins above); ruling-absence check re-run at the LIVE
> heads (both moved since the analysis pass): full-tree greps of shallow clones
> superbot @ `9f46cb7` and fleet-manager @ `7c13be7` (post-EAP / budget-ruling /
> posture-ruling keyword sweeps) found NO owner post-EAP budget ruling — only the
> open question and the Q-0261 boundary, both quoted at Q6. Verdict unchanged:
> parked(routed), not parked(overtaken).

**1. What is this really?**
Two ideas fused. (a) Mechanical resilience: routines/orchestrations that detect
usage-limit death and defer to reset — ALREADY promoted to a superbot plan
(`docs/planning/usage-limit-aware-routines-plan-2026-07-08.md`, PR #1845, pinned
above) prescribing the limit-deferred pattern (`send_later` at reset time + 2 min);
the failure record is verbatim there ("This session's 4-agent adversarial-review
workflow died mid-flight… `You've hit your session limit · resets 5:40pm (UTC)`").
(b) The expiry-bound half: post-EAP usage budgeting — the free EAP window wraps
2026-07-14 (fm dispatch-log pin: "EXTENDED to 2026-07-14 — Anthropic email
2026-07-09 22:29Z"), after which the fleet's standing routines (roster gen #5 pin:
32 enabled triggers = 15 standing crons + 2 poke-only + 15 one-shots) fire on PAID
usage with no ruling on posture.

**2. What is the possibility space?**
Per-lane cadence tiers; wake-on-event over cron; usage-aware self-throttling
(blocked — see Q4); an owner budget dashboard; the limit-deferred retry doctrine
fleet-wide (kit-adopted); cap raises — the Codex cap is a live sibling: idea-engine
PR #143 carries chatgpt-codex-connector[bot] comment 4944145245
(2026-07-11T08:59:32Z), verbatim "You have reached your Codex usage limits. You can
see your limits in the [Codex usage dashboard](https://chatgpt.com/codex/cloud/settings/usage)."
— and the raise-the-cap owner click is ALREADY queued in superbot's round3 brief
(`docs/planning/round3-dispatch-runbook-2026-07-10.md:573` @ `9f46cb7`: "raise the
Codex usage cap"), one ask one surface, not duplicated here.

**3. Most advanced capability reachable by the simplest implementation?**
The limit-deferred self-check-in (`send_later` at reset + 2 min) — already fully
specified in the superbot plan (layer 1 prompt clause + layer 2 failure-class rule
+ layer 3 `limit-deferred` counter); fleet-wide adoption is one doctrine line per
lane's routine prompt, zero new code. Anything smarter ("budget-aware" throttling)
is structurally impossible agent-side today (Q4).

**4. What breaks it?**
Agents are measurably blind to spend — the fm fleet-economics ledger's honest-nulls
rule (pinned above): "Actual CI minutes, token spend, and dollar costs are NOT
visible to agents from any surface reachable this session"; the fm model-matrix
finding line stands behind it (`create_trigger` has no model parameter; Project
config is not agent-visible). So NO agent can implement a budget policy — only
execute an owner-set one. Also: limit errors are opaque and provider-specific
(Anthropic session limits vs the separate Codex cap, Q2's live sibling), so
detection stays string-matching per provider.

**5. What does it unlock?**
The fleet survives the paid period without silent mid-flight workflow deaths and
without unmetered burn-by-inertia; it unblocks the manager's pre-close
trigger-cadence sweep. PROPOSAL 005 dependency status (honest read of
`control/outbox.md` @ HEAD): the status-file TOP-5 line couples this idea's HARD
EXPIRY to "PROPOSAL 005 depends", but PROPOSAL 005's own `depends:` names
substrate-kit as the providing lane — the EAP platform ask ("send window ends
2026-07-14") appears there as a CO-CONSUMER of its probed output, not as a
dependency on this probe. This park therefore neither advances nor blocks
PROPOSAL 005; what they genuinely share is the 2026-07-14 window itself — if
sim-lab verdicts 005 after the window, only the wrap-up-email co-consumer expires,
the proposal's core question survives.

**6. What does it depend on?**
An owner post-EAP posture ruling — VERIFIED ABSENT at the live heads: full-tree
greps of superbot @ `9f46cb7` and fleet-manager @ `7c13be7` this session found
none; only the open question (superbot
`docs/planning/projects-eap-product-review-2026-07-07.md:150`, verbatim: "the
honest cost question is post-EAP pricing of always-on coordination vs our current
zero-idle-cost cron model") and Q-0261's boundary (maintainer-question-router @
`9f46cb7`, core-6 Projects "run indefinitely, at least until the EAP ends").
Plus the existing superbot plan for the mechanical half (pinned above).

**7. Which lane should build it? (honest routing)**
Mechanical half = superbot (its plan, PR #1845) + the kit for fleet doctrine
(the plan's own "Kit portability" section flags exactly this). Budgeting half =
NOBODY builds it — it is an owner policy decision routed via the manager sweep,
deadline-bound: decide ≤2026-07-13, the window wraps 07-14.

**8. Smallest shippable slice?**
The paste-ready structured choice itself, shipped on this heartbeat's ⚑ block —
this slice does exactly that: decision (4) in the ≤07-14 sitting bundle, with a
recommendation first and three alternatives, all one-line pastes.

**Recommendation: park** — routed: the mechanical half already lives as superbot's
plan (PR #1845), and the live half is an owner-only budgeting decision with a hard
07-13 deadline, now paste-ready on the heartbeat; nothing here is sim-shaped
(spend is unmeasurable agent-side per the pinned honest-nulls rule, so no
simulation can settle a pricing/values policy). NO outbox proposal.
