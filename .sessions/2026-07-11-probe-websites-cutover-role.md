# Session — probe: rebuild-websites-cutover-role (superbot section, #155 shortlist item 2)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-11 (worker slice, dispatched by the coordinator
> under continuous-chaining mode per Q-0265)

## What this session did

Probe battery v0 on `ideas/superbot/rebuild-websites-cutover-role-2026-07-10.md`
(#2 on the #155 groom's ripe shortlist) — verdict **parked(routed)**. Verify-first
at four live pins (all fetched this probe, ~10:35–10:45Z): superbot `c77ee0d`
(canonical doc byte-identical from the harvest pin `fd638e3`, sha256 `4e75226…`
both, diffed), websites `92c3dc6` (depth-1 clone + its 10:28Z heartbeat),
superbot-next `dc32367` (blobless clone + its 10:25Z heartbeat), fleet-manager
roster gen #5 @ `3150f0e`.

The finding: the doc's rebuild-disposition ask is **CONSUMED by practice** at the
websites lane — both sites rebuilt + dark-launched (websites PRs #7/#8), the
producer question resolved read-only (rework-plan Q7: consume superbot's committed
artifacts; console feed on a pinned v1 cross-repo contract, superbot PR #1884),
hosting/cadence settled (own Railway project, deploy-state drift cell, healthcheck
cron; deploy verified all three services at `1ff77e4`). What survives is exactly
the CUTOVER-ROLE CALL — an owner architecture decision, unruled at live HEAD,
already tracked click-level on the lane's own owner surface (websites
`docs/owner/OWNER-ACTIONS.md` rows 1/4/6: "Do not port without an owner call" /
"Deferred to cutover" / "Gated: needs your go"). Not simulable — routed as ONE
structured-choice ⚑ OWNER-ACTION on this slice's heartbeat (recommendation first,
paste-ready, per Q-0263.2), fanning the lane's three rows into one sitting while
the canonical rows stay on the lane's surface (fewer-clearer-asks hygiene).

Separability insight recorded in the report (no other surface carried it): SITE
cutover and BOT cutover are independent events — the new sites mirror the OLD
bot's data, which stays correct while the old bot IS production; the producer
repoint keys to the BOT cutover, and its target already exists committed
(superbot-next `manifest.snapshot.json` + `manifest/layout/*.lock.json` @
`dc32367`, parity 26/49 mid-flight) — so the site-cutover go needs zero waiting
on the parity march.

Slice contents: probe report append + state flip (captured → parked(routed)) +
Grounding pin added (doc re-fetched at live `c77ee0d`) + one section-README
index-echo re-badge (captured → parked) + this card + claim add/clear + the
heartbeat. No outbox entry (nothing sim-ready), no code, no workflow edits, no
websites-lane write (Q-0260). Claim rode this branch's first commit per the #157
precedent (claims dir re-read at origin/main `42d60b7` — empty of live claims;
the ORDER-002 sibling's scope was control-only, disjoint) and is deleted in the
close-out commit. Sibling #158 (ORDER 002 self-review) landed mid-flight — merged
`origin/main` forward-only (never rebased) per the README recipe; its Self-review
section is preserved VERBATIM at the foot of the heartbeat overwrite.

**📊 Model:** fable-5 · docs-only probe slice (one idea-file append + re-badge +
card + heartbeat; no code)

## 💡 Session idea

The websites OWNER-ACTIONS doc is exactly the six-field-adjacent owner surface
this repo's ⚑ grammar formalizes, but its rows are table-shaped and un-bundled —
three of its six open rows (1/4/6) are really ONE decision. If more lanes adopt
the kit's OWNER-ACTIONS pattern, propose (via the manager) a `sitting:` grouping
key on owner-action rows so any consumer (fm owner-queue, this repo's fan-in ⚑,
the :30 sweep) can mechanically bundle rows that must be decided together —
today that bundling is re-derived by hand at every fan-in (this slice did it for
websites; the #148/#150 gba pick + Lumen Drift + pokemon verdicts bundle on this
heartbeat did it for the ≤07-14 EAP sitting).

## ⟲ Previous-session review

`.sessions/2026-07-11-self-review-order-002.md` (#158, merged `48bbac4`) —
verified against this tree at my merge of origin/main: the dated Self-review
section sits at the foot of `control/status.md` exactly as its done-when
required, the orders line correctly moved 002 into `done=` and dropped the
sibling claim annotation per the control/README ritual, and its honesty line
(one briefed went-wrong candidate verified NOT-FOUND and recorded as such rather
than repeated) is the norm this probe reused — the idea file's own premise ("the
call should precede more build-out") was verified INVERTED at live HEAD rather
than copied forward, the same claim-vs-tree discipline. Its ⚑ mirror bundling
(three decisions, one ≤07-14 sitting) directly shaped this slice's fan-in ⚑
(one structured choice instead of three rows). No reconciliation debt handed to
this slice: its overwrite preserved the #157 standing entries verbatim, so this
slice's overwrite only had to append, not repair.

## Handoff → next wake

The #155 superbot ripe shortlist has ONE remainder:
`claude-code-projects-for-the-rebuild-2026-07-10.md` (explicit before-event
pressure — probe it before the next rebuild wave spins up lanes). The cutover
⚑ is owner-court: on the owner's reply, the WEBSITES lane executes (plan steps
3/5) and nothing returns here except closing the loop if the manager routes a
confirmation. The producer-repoint capture stays deliberately UN-captured — its
arming event is the BOT cutover (D-3/CUT-3); capturing early would race
superbot-next's own CUT-3 planning. Watch item continued from #157: superbot-idle
consuming the VERDICT 006 lift with both guardrails.
