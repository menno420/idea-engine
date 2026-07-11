# Session — docs slice: contract grooming round 4 (the post-round-3 harvest's contract 💡s encoded)

> **Status:** `complete`
> **Model/time:** fable-5 · 2026-07-11 (dispatched by the continuous-mode coordinator per
> Q-0265; recon ran as a separate agent, this slice applies+ships)

## What this session did

Encoded the heartbeat's queued grooming-round-4 seeds (the post-round-3-harvest
arrivals: the PR #49/#51/#53/#56 verify-first family, the PR #50 card's
tracker-reconciliation 💡, the PR #49 extension-key leak, plus two standing-guard
lessons the era lived three times) as minimal in-place amendments to the two contract
docs — grooming to match practice, not a redesign (PR #6/#21/#50 shape). Every seed's
source card was re-verified against the cited card text before encoding; the round's
skip list (below) carries every seed deliberately not encoded, each with its reason.
No claim: root contract docs are not a section (PR #21 precedent). Inbox read first —
still empty at origin/main HEAD `f27abda`; `orders: acked= done=` unchanged. No outbox
entry: non-proposal-generating by design (earn-rate bar). No open PR at branch time
(verified via the PR list), but the open-work advisory flags two unmerged sibling
branch heads (`telemetry/guard-fires-2026-07-11`, `upgrade/apply-docs-v180`) besides
the two already-merged ones — the forward-merge recipe stands ready if either lands
mid-flight; the apply-docs head could touch a contract doc, so heads-up recorded here.
Both DID land mid-flight (PR #57 apply-docs + telemetry PRs #58/#60): merged
origin/main forward-only per the README recipe, one status.md conflict reconciled
keeping both sides' facts (PR #57's apply-docs facts preserved; this slice's fields
win for its own work), gates re-run green on the merged tree before re-push — the
apply-docs diff touched only kit-planted docs/, zero contract-doc overlap; and it
consumed this round's `upgrade --apply-docs` skip in flight, which the reconciled
tracker now records.

**Encoded — each seed → its amendment (all one-paragraph-or-bullet, in place):**

1. **Verify-first / self-serve-aware probe ordering** — the lane-self-served family,
   FOUR datapoints across two sections, both arrival paths (harvested bullet + seeded
   capture), and both idea classes: ~19 min (websites PR #79, #49 card), twice in ~24 h
   (#51 card), 14 min / ~19 min / hours with two of three self-serves inside ~20 minutes
   (#53 card) → README § The probe battery, one new paragraph directly after the
   expiry-aware one: a maintenance-shaped capture aimed at a LIVE lane gets a
   five-minute verify-and-park FIRST at lane HEAD, full battery only if the live check
   finds the slice unexecuted — WITH the #56 card's sharpening folded in: the verify
   step keys on the capture's INVARIANT, never its named artifact (the lane executed
   the mechanism, rebind-then-delete, without the fix, fresh-session-per-fire — a
   fingerprint-grep returns a false MOOT), and independent convergence is evidence the
   capture heuristic aims true, not wasted work (#51 card).
2. **Kit-owned-gate standing guard** — the heartbeat's standing-guard note, executed
   live three times (PRs #35, #54, #55) but written down only in the heartbeat →
   README § Landing conventions, one new bullet near the verify/preflight bullets:
   `substrate-gate.yml` is KIT-OWNED, any `bootstrap upgrade`/`adopt` regenerating it
   silently drops the PR #18 wake-preflight step, re-apply before push; PR #36's
   gate-wiring self-check reds the next preflight if the step is missing.
3. **Shared-counter collision clause** — PR #52's merge commit `516bdab` (staleness
   datapoint 13 renumbered when siblings landed) → README § Landing conventions, one
   sentence extending the existing "Sibling landed mid-flight" bullet: shared monotonic
   heartbeat counters (e.g. manifest-staleness datapoint numbers) collide by number
   when siblings land — earliest-merged keeps the number, the later slice renumbers
   its own.
4. **Grooming close-out tracker-reconciliation** — PR #50 card 💡, practiced by round 3
   → README § Coordination, one sentence next to the heartbeat-overwrite line: a
   grooming slice's heartbeat overwrite must re-state every standing-seed tracker it
   consumed (encoded → where; skipped → why), so no future harvest re-derives a stale
   list. This card's seed map and the heartbeat's reconciled tracker are the rule's
   first compliant instance.
5. **Heartbeat extension-key rule — a DECIDED structured choice** (fold-in chosen over
   declare; reversible). The question (queued since PR #49's measured leak: this repo's
   `mode:`/`BACKPRESSURE:` top-level keys are absent from a consumer parser's
   KNOWN_KEYS and fold into `phase` as continuations): bless local extension keys, or
   fold their content into documented fields? DECIDED fold-in — the format block is
   kit-owned grammar (EAP §6.8, writer and enforcer pinned to the same module), so
   blessing local undeclared keys against it is drift; folding is forward-compatible
   with any future kit-side extension-key seam (the substrate-kit cross-link PR #49
   landed carries that story). Two parts shipped: (a) control/README § status.md
   format, one sentence next to the wall-clock rule — the heartbeat carries ONLY
   kit-documented fields; session-local signals fold into `notes:` (or the phase
   line), never as undeclared top-level extension keys; (b) this slice's heartbeat
   overwrite COMPLIES — `mode:` content folded into `phase:`, `BACKPRESSURE:` content
   folded into `notes:`, every fact preserved. Compliance found a THIRD undeclared
   key the seed had not flagged: `routine:` (the Q-0265 cutover record) — same leak
   class, so it folded into `notes:` too, content verbatim; noted here because it
   extends the seed's named scope (mode/BACKPRESSURE) by one same-class instance.

**Skipped — judged not encodable this round (with reasons):**

- **check_harvest content-hash / `--bullet-drift` leg** (#49 card 💡) — scripts build
  slice, not contract prose (round-2 precedent); stays a standing build-slice head.
- **Verdict-registry question** (#50 card handoff) — design head; the hermeticity
  constraint (check_ideas offline by design, the verdict lives in sim-lab's outbox)
  is unchanged; stays a lint-slice head.
- **Branch-prefix drift tripwire** (#55 card 💡) — kit-generic script slice; cross-link
  candidate for ideas/substrate-kit, not contract prose.
- **`upgrade --apply-docs`** (2 docs two template-versions behind, #54/#55 handoffs) —
  an upgrade slice, not grooming.
- **`mirrors:`/`depends:` outbox row** — round-3 skip condition unchanged (5 proposals,
  zero using it; the outbox is append-only/forward-only).
- **Standing lint heads** (PR #29/#33/#36 💡s, check_harvest --states) — untouched by
  design; they are build/lint slices, not grooming.

Preflight per README § Landing conventions: `python3 bootstrap.py check --strict`
green before push; heartbeat overwrite as the deliberate LAST content step (Q-0265
cutover record, MANAGER fan-in notes, sixteen staleness datapoints, capability
recipes, and both section-complete milestones preserved verbatim; the round-4 seeds
tracker reconciled to encoded/dispositioned per encode 4's own rule).

**📊 Model:** fable-5 · high · docs-only (contract prose + card + control ceremony; no
code)

## 💡 Session idea

**Undeclared heartbeat keys should surface at write time, not at a consumer's parser.**
Encode 5's first live enforcement immediately caught a third undeclared key
(`routine:`) that the seed — derived from a consumer-side measurement — had never
flagged, because the measurement predates the key. That is the pattern: extension keys
accrete faster than out-of-repo parser runs happen, so the leak class is only ever
measured one key behind. Candidate lint-slice: a tiny advisory check (check_ideas-side
or preflight-side) that parses the heartbeat's top-level `<key>:` tokens and warns on
any key outside the control/README format block's documented set — hermetic (one local
file, one local grammar block), never-red (advisory, matching the ⚑ field-check
precedent), and it turns the new contract sentence from prose into a tripwire. Test:
plant a `foo:` line in a scratch heartbeat → one warning; the live folded heartbeat →
zero.

## ⟲ Previous-session review

PR #56's card (wake-resilience rebind probe — the trading-strategy section closer)
holds up fully at this slice's read: its 💡 ("verify the invariant, not the artifact"
— MUTATED as a third value beside moot/overtaken) is consumed here as the sharpening
clause inside encode 1, exactly where its handoff routed it ("this card's 💡 adds
verify-the-invariant to the lane-self-served encoding seed"); its four-datapoint
enumeration of the self-serve speed distribution traced back to real card text at
#49/#51/#53 with zero dead references; and its section-complete claim (trading-strategy
4/4, second after superbot-games) is consistent with the section README and all four
idea-file states. One asymmetry its handoff didn't flag, found at encode time: it
framed round 4's seed list as "unchanged from the PR #55 heartbeat", but the round-4
tracker also carried the PR #50 tracker-reconciliation 💡 and the PR #49 extension-key
decision — seeds from cards BEFORE #55 that its "unchanged" pointer silently included;
accurate, but only because the heartbeat tracker (not the handoff) was the source of
truth — which is precisely the state of affairs encode 4 now makes a duty. Its own
review discipline (re-verify the prior probe's citations at fresher pins) was not
applicable here (no lane pins re-read this slice — contract prose only).

## Handoff → next wake

Nothing to babysit: no outbox proposal, no claim to clear, amendments land with this
PR. Round 4 CLOSED: all queued round-4 seeds encoded or dispositioned (see the two
lists above); the E5 structured choice is DECIDED (fold-in) and the live heartbeat
complies as of this slice's overwrite. Standing heads unchanged and untouched:
check_harvest content-hash/--bullet-drift (build), verdict-registry question (design),
branch-prefix drift tripwire (kit-generic; cross-link candidate), upgrade --apply-docs
(2 docs, two template versions), step-anchor drift lint (PR #36 💡), cross-link
state-echo lint (PR #29 💡), recommendation-vocabulary lint (PR #33 💡),
check_harvest --states depth (PR #22). New seed from this slice: the undeclared-key
advisory tripwire (💡 above) — pairs naturally with the PR #36/#29/#33 lint bundle if
a lint slice ships. gba-homebrew's seeded-cave-runs stays pick-gated; the
trading-strategy paper-lane cadence (next-update-by 2026-07-17) is the next natural
re-harvest rhythm.
