# Claude Code Projects (EAP) as the rebuild coordinator — link index

> **State:** parked(overtaken — adopted 2026-07-07 and operating: the owner stood up the "SuperBot" Project the same day the canonical doc was written (superbot `docs/planning/projects-eap-coordinator-kickoff-2026-07-07.md` §1 @ `c77ee0d` — Project exists, screenshots verified, both repos connected) and directed the rebuild through it that evening (activation-plan supersession note, same pin); by probe time the WHOLE FLEET — this repo included — runs on Claude Code Projects (fm roster gen #5 @ `3150f0e`: 18 seats on per-lane wake triggers; superbot-next at 26/49 parity through parallel Project lanes @ `f87ffb0`) — probe report below)
> **Class:** process · **Target:** `menno420/superbot-next`
> **Grounding:** https://raw.githubusercontent.com/menno420/superbot/c77ee0d662aeaff892623c445297c5f2952de34d/docs/ideas/claude-code-projects-for-the-rebuild-2026-07-07.md@c77ee0d · fetched 2026-07-11T10:55Z
> *(pin annotation: probe-time re-fetch at live superbot HEAD (ls-remote ~10:54Z) — byte-identical to the harvest pin `fd638e3` (sha256 `5057ea4e…` both, diffed this probe), so the canonical link below stays valid unchanged.)*

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/claude-code-projects-for-the-rebuild-2026-07-07.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/claude-code-projects-for-the-rebuild-2026-07-07.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/claude-code-projects-for-the-rebuild-2026-07-07.md)).

Use the Claude Code Projects EAP as the orchestration layer for the SuperBot rebuild: prove it on reversible work in the current repo first, then let it coordinate building superbot-next (kernel, port bands, cutover).

## Probe report (v0, 2026-07-11)

*Single-pass battery per the README panel default (sim-lab VERDICT 002): the head is an
adoption question whose answer is an observable operational fact — no irreversible
surface is reachable from this repo, and the verify-first sweep did not disagree with
itself (every layer read said the same thing: adopted). Every load-bearing claim below
was fetched live this probe (2026-07-11 ~10:54–10:58Z): superbot HEAD `c77ee0d`
(ls-remote; canonical doc byte-identical from the harvest pin `fd638e3`, sha256
`5057ea4e…` both, diffed), superbot-next HEAD `f87ffb0` (ls-remote; heartbeat
`updated: 2026-07-11T10:25Z` read raw at that pin), fleet-manager roster gen #5 @
`3150f0e`, websites `92c3dc6` (unchanged since the #159 probe's clone ~10:35Z). One
evidence class is new for this battery: THIS REPO'S OWN OPERATION — idea-engine is
itself one lane of a Claude Code Projects fleet and this probe session is a
Project-dispatched child session (README.md § Coordination, Q-0265 cadence), cited
below as operating evidence, not a wish.*

### Verify-first ledger — the canonical doc's asks vs what already happened

| Canonical item (superbot doc @ `c77ee0d`) | Status | Where it lives now (live-pin citation) |
|---|---|---|
| "Next lifecycle step": owner accepts the EAP invite, stands up one Project | **CONSUMED 2026-07-07** | The doc's own same-day update: "access went live". Then superbot `docs/planning/projects-eap-coordinator-kickoff-2026-07-07.md` §1 @ `c77ee0d`: Project **"SuperBot" exists** (owner-created, "screenshots verified"), **both** `menno420/superbot` and `menno420/superbot-next` connected in Settings → Repositories. |
| "Prove it on reversible work first, then let it coordinate building superbot-next" | **CONSUMED — and exceeded** | The activation plan's §2 supersession note @ `c77ee0d`: *"Superseded 2026-07-07 evening, owner-directed: the rebuild DOES run through the Project."* Live result at probe time: superbot-next heartbeat @ `f87ffb0` — **26/49 subsystems ported, 168/168 goldens green at `8b55d95`**, five named parallel lanes (parity flips, band-6 games, band-7 builder, kit, codex-triage) chaining slices in continuous mode per Q-0265. The kernel/port-bands/cutover program the doc wanted Projects to coordinate is being coordinated exactly that way. |
| Open consideration 1 — memory location (keep repo docs the source of truth, Project memory = working cache) | **CONSUMED as prescribed** | The fleet's coordination record is committed files, not cloud memory: `control/` bus + heartbeats + session cards + per-file claims (this repo's `control/README.md`: "Projects cannot talk to each other directly — committed git files are the only shared medium"). The doc's repo-as-truth rule held fleet-wide. |
| Open consideration 2 — tooling overlap (evaluate retiring claim files / PR babysitting / cron triggers) | **CONSUMED by evolution — opposite verdict** | The fleet KEPT and extended the committed machinery rather than retiring it: per-file claims (measured 0% conflict, `control/claims/README.md`), roster generated from the live trigger registry (fm `docs/roster.md` gen #5 @ `3150f0e`, 32 enabled triggers), auto-merge enablers. Reason the doc could not see in 2026-07-07: native Project features are per-Project, and the fleet became MANY Projects — cross-Project coordination still needs a committed medium. |
| Open consideration 3 — repo scope (superbot now, add superbot-next when created) | **CONSUMED** | Kickoff doc §1 @ `c77ee0d`: superbot-next created (owner, deliberately public) and connected alongside superbot. |
| "If accepted, this promotes to a short `docs/planning/` note" | **CONSUMED** | Three planning docs supersede it @ `c77ee0d`: product review, activation plan, coordinator kickoff (each cross-linked; the activation plan's header says it "supersedes the 'next lifecycle step'" of this very doc). |
| EAP feedback as a byproduct | **Lives superbot-side** | Canonical email doc `docs/planning/projects-eap-anthropic-email-2026-07-08.md` (pointed to by the activation plan §4 @ `c77ee0d`). Superbot's duty on superbot's surface — not this repo's residue. |
| The window (EAP "free only through Friday 2026-07-10"; this repo's shortlist pressure "probe before the next rebuild wave") | **FIRED — with the idea adopted** | The rebuild wave ran THROUGH Projects (rows above; websites rebuilt + dark-launched @ `92c3dc6` by its own Project lane, per the #159 probe). Post-EAP commercial terms: **not measured** from this seat — but no operational wall is in evidence: every pin in this report is dated 2026-07-11, the day after the free window closed, including this session itself. |

**1. What is this really?**
A 2026-07-07 adoption proposal whose decision fired the same day it was written: the
owner accepted the EAP, stood up the "SuperBot" Project, and directed the rebuild
through it that evening. By harvest time (2026-07-10) it was operating doctrine; by
probe time the entire fleet — including the repo probing it — runs on Claude Code
Projects. The head is a historical adoption record wearing a `captured` badge, not an
open question.

**2. What is the possibility space?**
Dispositions only — the adoption is fact, not hypothesis: (a) park(overtaken) with the
consumption ledger above, so no future battery re-derives it; (b) leave captured —
invites exactly that re-derivation (the stale-grounding trap); (c) sim-ready — needs a
reproduced-evidence question and none survives: you cannot simulate your way to a fact
the production system already demonstrates daily; (d) needs-more-grooming — nothing
ungroomed: superbot's own planning layer superseded the doc twice over (activation plan
→ kickoff protocol); (e) reject — wrong: the idea was right, and it won. Collapses to (a).

**3. What is the most advanced capability reachable by the simplest implementation?**
This report's marginal value is the ledger plus one delta no surface records: the doc
imagined ONE Project coordinating the rebuild; reality scaled to MANY Projects — one
per lane, 18 seats on the fm roster — coordinated through committed git files, an
architecture the doc's open consideration 1 (repo-as-truth) anticipated but did not
predict. The simplest implementation was the one taken: adopt, then let the committed
bus carry cross-Project coordination the product does not natively provide.

**4. What breaks it?**
- **Mistaking "overtaken" for "verdicted":** superbot-side the doc's Status is still
  `ideas` at `c77ee0d` — no ruling formally retired it. Mitigation: the supersession
  note is owner-directed and in-tree, and the operating fleet is the strongest
  available evidence class; this park cites both rather than inventing a ruling.
- **Post-EAP economics:** the free window ended 2026-07-10. If pricing/limits later
  change fleet economics, that is a NEW head (spend doctrine, owner court), not a
  revival of this one — deliberately not speculated here (not measured).
- **Ledger rot:** superbot/superbot-next HEADs move fast (superbot-next moved twice
  during the #159 probe's window alone); every row above pins its SHA.

**5. What does it unlock?**
Closes the #155 superbot ripe shortlist — this was its last remainder, so the section's
groomed state survives without a dangling time-pressured head; frees future wakes from
re-deriving the EAP adoption history (this file now carries the ledger); and records
the one-Project→many-Projects delta for any future Projects-tooling head to build on.

**6. What does it depend on?**
Nothing buildable — an overtaken park has no build dependencies. Freshness depends on
the pins above staying true: superbot `c77ee0d` (doc + planning layer), superbot-next
`f87ffb0` (rebuild mid-parity through Project lanes), fm roster `3150f0e` (fleet
shape), and this repo's own committed operating contract (README.md § Coordination @
this PR's HEAD). No layer disagreed this probe — freshest-wins was never needed.

**7. Which lane should build it?**
None — there is nothing to build: adoption is operating fact fleet-wide. The residual
duties already live where they belong: the EAP feedback email superbot-side (its
planning docs), Projects-tooling evolution kit-side (e.g. the enabler/trigger
machinery). Not sim-lab: no reproduced-evidence question survives. **No owner ask:**
the doc's one owner decision (accept + stand up the Project) was made 2026-07-07
(kickoff §1, screenshots verified) — routing it again would violate the stale-ask
hygiene (`control/README.md` § ⚑ needs-owner).

**8. What is the smallest shippable slice?**
This PR: this report + the state flip + the Grounding pin + the section-README
re-badge + the heartbeat. Explicitly NOT in the slice: any outbox entry (nothing
sim-ready), any ⚑ owner ask (the decision was made 2026-07-07 and asking again is
drift), any superbot/planning write (Q-0260 — this repo writes only itself).

**Recommendation: park** — overtaken(adopted): the owner stood up the Project and
routed the rebuild through it the day the doc was written (superbot kickoff doc +
activation-plan supersession note @ `c77ee0d`), and by probe time the whole fleet —
this session included — operates on Claude Code Projects (fm roster gen #5 @
`3150f0e`; superbot-next 26/49 parity via parallel Project lanes @ `f87ffb0`), so the
question is consumed and nothing is simulable or askable.
