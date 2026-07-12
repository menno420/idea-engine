# Session — capture slice: verdict-inheritance guard for carried heartbeat watches (fleet)

> **Status:** `in-progress`

- **📊 Model:** fable-5 · capture slice (one new `ideas/fleet/` head + index row +
  this card; no code, no probe — capture only, per the PR #244 groom's routing)

**Section-collision flag (dispatch boundary — no claim file):** this slice is
barred from `control/`, so no `control/claims/` entry exists; this card's
born-red first commit carries the `ideas/fleet/` collision flag per the
PR #222/#225/#243/#244 workflow convention. Scope: ONE new head —
`ideas/fleet/carried-watch-verdict-inheritance-guard-2026-07-12.md` — plus the
fleet README index row and this card.

## What this session did

Evaluated the ONE candidate the PR #244 websites lane-backlog groom named but
did not capture (`.sessions/2026-07-12-websites-lane-backlog-groom.md` § 3):
the **verdict-inheritance guard for carried heartbeat watches**, source bullet
at line 158 of websites `docs/ideas/backlog.md` @ blob `e14bb15` (lane commit
`8f97654`; fetch re-verified to the blob SHA by `git hash-object` this slice,
repeating the groom's pin-verify). Decision: **CAPTURE** — the Q-0089 bar met
on all three legs:

1. **Idea-shaped**: the bullet states a mechanism, not a vibe — a
   `watch: <claim> · verified <ISO>` token, writer re-verify-before-copy, and
   a /fleet staleness badge — grounded in a real incident (websites' "never
   delivered" cron verdict rode five heartbeat overwrites after it stopped
   being true).
2. **Fleet-relevant beyond the parked lane**: the live instance is THIS
   repo's own `control/status.md` @ `ce2fab4` — line 10 carries watches by
   pointer and by verbatim copy ("SWEEP NOTES preserved: theme-schema … watch
   (from #157); superbot-idle V006 guardrails watch (from #157)"; "MANAGER
   SWEEP FLAGS carried unchanged from fc0bab6 … not re-copied here"), line 9
   carries standing entries "preserved VERBATIM from the prior overwrite".
   Heartbeat grammar is kit-planted territory (`control/README.md` template +
   status checker) — every adopter inherits the pattern and would inherit the
   guard.
3. **Stateable smallest-testable-version**: the token plus one deterministic
   report-only advisory over `control/status.md` (same always-exit-0 family
   as `--heartbeat-keys` / `--open-work`), demonstrable on this repo today.

Dedup swept (`rg -g '!bootstrap.py' -g '!.substrate'` over all of `ideas/`
for heartbeat/watch/carry/inherit/verdict/stale/handoff/generation) — no
duplicate; eight adjacent heads catalogued as relation notes in the new head,
the closest four:

- `ideas/websites/merge-hold-at-head-2026-07-11.md` — the dispatch-named
  SIBLING failure mode (coordination-file state nothing enforces): spatial
  (a HOLD nothing reads) vs this head's temporal (a watch everything copies);
  relation stated explicitly in the new head.
- `ideas/substrate-kit/parallel-session-heartbeat-reconcile-2026-07-10.md` —
  complementary: concurrent overwrites LOSING facts vs sequential overwrites
  KEEPING them past their evidence; not a dup, same checker surface.
- `ideas/fleet/lint-bundle-2026-07-11.md` (`--heartbeat-keys`) — syntactic
  key-presence tripwire; this adds the semantic-freshness leg.
- `ideas/fleet/coordinator-archive-handoff-ceremony-2026-07-11.md` — names
  the handoff seam and the trigger-disposition precedent but has no watch
  re-validation step; the guard is that missing step.

Also swept, ruled same-family-not-dup: `own-heartbeat-parse-self-check`
(parse, not freshness), `heartbeat-ladder-field` (regen-from-source mooted
verbatim carry at the roster layer), `queue-slice-staleness-age` +
`reconciliation-slot-carry-tracker` (lane-internal carried artifacts).

**Convention deviation, declared:** the dispatch asked for the section's
"`[[...]]` relation-note convention" — no such convention exists in this
tree (every `[[` in `ideas/` is a `[[fill:…]]` auto-draft slot,
`check_ideas.py` UNFILLED class). Relations were stated in the tree's ACTUAL
form: a prose relations subsection with markdown links, per the fleet
exemplars.

Read-only side check for the coordinator: `control/inbox.md` at branch time
(main `ce2fab4`) carries ORDER 001 and ORDER 002 only — no ORDER 003+.

## Close-out

**Evidence:**

- ideas touched (2): `ideas/fleet/carried-watch-verdict-inheritance-guard-2026-07-12.md`
  (NEW — state `captured`, class process, target substrate-kit; Grounding
  pinned to the websites blob `e14bb15` with pin annotation),
  `ideas/fleet/README.md` (index row added, fleet-README entry form)
- sessions touched (1): `.sessions/2026-07-12-verdict-inheritance-guard-capture.md`
- code touched: none · control touched: none (dispatch boundary; READ-ONLY
  reads of `control/status.md` + `control/inbox.md` for grounding/ORDER check)
- git: branch `harvest/verdict-inheritance-guard-capture` off main `ce2fab4`
  (prefix chosen from `substrate.config.json` `automerge.branch_patterns` —
  no `capture/` pattern exists; a capture-from-upstream-doc is harvest-shaped),
  born-red card first commit, capture commit follows; draft PR flipped ready
  on local green — never merged by this slice, auto-merge never armed by this
  slice.
- verify: `python3 bootstrap.py check --strict` and
  `python3 scripts/preflight.py` (expect 10/10) run before each push.

**Judgment (the half only the session knows):**

- Decisions made: no D-entry — capture disposition only. One judgment call,
  declared: the head targets `menno420/substrate-kit` (grammar + checker
  half) with the /fleet badge half noted as manager territory, rather than
  splitting two heads — the groom's own routing read ("heartbeat-grammar
  territory, kit/manager layer") and the merge-hold precedent both treat the
  kit slice as the carrier and the manager surface as a rider.
- Next session should know: the head is `captured`, NOT probed — the probe
  should fetch the kit-planted `control/README.md` template at live kit HEAD
  (does any watch grammar already exist?), pick the checker home (kit-side
  status checker vs per-repo preflight advisory), and price the /fleet badge.
  The merge-hold routed kit slice (four-touch build, PR #243 flags) is a
  natural shared carrier if the manager bundles them.

## 💡 Session idea

Three heads now independently describe "state in coordination files that
nothing re-validates" (merge-hold: nothing reads it; this head: everything
copies it; heartbeat-reconcile: merges drop it) and each was found only by a
manual dedup grep at capture time. The dedup sweep itself is checker-shaped:
a `check_ideas --concept-neighbors` advisory that, for a NEW idea file, greps
the tree for its title's content words and prints the top overlapping heads —
turning the capture-time dedup from a convention someone must remember into a
report the PR diff carries. Cheap v0: stdlib token overlap on `# ` titles +
state lines, report-only.

## ⟲ Previous-session review

The PR #244 groom card held up on every claim this slice depended on: the
blob pin re-verified byte-exact (`e14bb15` by `git hash-object`, same as its
own recorded verify), the bullet is at line 158 as the card's "one candidate
named, not captured" section implies (card said ~154-adjacent region; exact
line recorded here), and its "no routing flag anywhere in the bullet text"
claim confirmed against the quoted bullet — the source names only a lane
session card, no heartbeat/manager routing token. Its judgment call NOT to
capture inside a groom slice (link-index-only rule) was correct separation of
duties; this slice is the capture half it deliberately left. One refinement:
the groom's "heartbeat grammar is kit/manager territory" read was verified
rather than trusted — the kit-planted control/README template is the actual
carrier surface, confirmed via the parallel-session-heartbeat-reconcile
head's routing precedent.

## Handoff → next wake

Facts for the coordinator heartbeat (NOT written here — control/ is
coordinator-only): ONE new fleet head captured
(`carried-watch-verdict-inheritance-guard-2026-07-12.md`, captured, probe
pending — candidate for a future mint slot); the PR #244 groom's named
candidate is now dispositioned, closing its handoff item; inbox still ORDERs
001–002 only at `ce2fab4`; manager-sweep note: the routed merge-hold kit
slice (#243) is a natural shared carrier for this head's advisory if bundled.
