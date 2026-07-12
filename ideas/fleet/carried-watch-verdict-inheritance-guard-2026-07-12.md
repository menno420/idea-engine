# Carried-watch verdict-inheritance guard — a watch must not outlive the verdict that justified it

> **State:** captured
> **Class:** process · **Target:** `menno420/substrate-kit` (heartbeat-grammar + status-checker
> half is kit-planted territory every adopter inherits; the fleet-surface badge half is
> manager `/fleet` territory)
> **Grounding:** https://raw.githubusercontent.com/menno420/websites/8f9765483a7df57ce426e7d11d200f10b5495ed7/docs/ideas/backlog.md@e14bb15 · fetched 2026-07-12T02:57Z
> *(pin annotation: source bullet at line 158 of the pinned backlog — the fetch re-verified
> to blob `e14bb15408b1f45de14eae72efe990024f0e548c` by `git hash-object` this slice, the
> same pin-verify the PR #244 groom ran. The bullet's own canonical source is the websites
> chain-closeout card 💡 (`.sessions/2026-07-11-chain-closeout.md`, websites repo). Captured
> here because the PR #244 lane-backlog groom named it the ONE new bullet of eleven with no
> routing flag anywhere (`.sessions/2026-07-12-websites-lane-backlog-groom.md` § 3) and the
> websites lane chain is PARKED at `8f97654` — lane self-serve never comes.)*

**Origin:** websites backlog bullet (quoted verbatim): *"a watch claim copied across N
heartbeat overwrites (the 'never delivered' cron verdict rode five) should carry a
last-verified timestamp (`watch: <claim> · verified <ISO>`) so readers see staleness and
writers re-verify before copying; /fleet could badge watches whose verified-stamp lags the
heartbeat. Worth having because inheritance is how this chain's one durable wrong claim
propagated."*

## The idea

A **carried watch** is a heartbeat line one coordinator generation inherits from the
previous — copied verbatim or carried by pointer at each overwrite. This repo's own
`control/status.md` @ `ce2fab4` is a live gallery of the pattern: "SWEEP NOTES preserved:
theme-schema promotion park HALF-FIRED watch (from #157); superbot-idle V006 guardrails
watch (from #157 …)" and "MANAGER SWEEP FLAGS carried unchanged from fc0bab6 … full text at
fc0bab6 control/status.md notes, not re-copied here" (line 10), plus line 9's standing
entries "preserved VERBATIM from the prior overwrite". The failure mode is that inheritance
is *textual, not evidential*: every overwrite renews the file's `updated:` stamp, but the
watch's justifying verdict or evidence is never re-checked — a watch records where it came
from ("from #157") but nothing distinguishes *re-verified this wake* from *copied N times
since anyone last looked*, so an expired or wrong claim propagates exactly as durably as a
true one. That is not hypothetical: the websites chain's one durable wrong claim (a "never
delivered" cron verdict that had stopped being true) rode five overwrites on precisely this
mechanism, and the risk peaks at **generation handoff**, where a fresh coordinator inherits
the whole watch set by ceremony with zero context to doubt any line of it.

The guard puts teeth on the inheritance step, cheapest first. **Grammar:** a carried watch
names its justifying pointer and a last-verified stamp — the source's token,
`watch: <claim> · verified <ISO>`, generalized with a `· per <verdict/PR/sha>` evidence
half. **Carrier duty:** at each overwrite (and mandatorily at generation handoff) the
writer either re-verifies the claim and refreshes the stamp, or carries it with the OLD
stamp intact — visible staleness instead of silent renewal; what the guard forbids is a
watch whose apparent freshness is the heartbeat's, not its own. **Check:** a report-only
advisory in the existing status-checker/preflight family (always exit 0, like
`--heartbeat-keys` and `--open-work`) flagging watch-class lines with no `verified` stamp
or a stamp lagging the heartbeat by more than N overwrites/days; the manager's `/fleet`
badge is the same finding rendered fleet-wide. **Smallest testable version:** the token
plus one deterministic grep-shaped advisory over `control/status.md` — stdlib, no network,
demonstrable on this repo's own carried watches today. Expiry action is a probe question,
not a given: auto-drop is probably wrong (the merge-hold head's `claims-stale` "delete it"
lesson — stale advice that would kill a legitimate hold), so v0 nags and a human retires.

## Relations (adjacent heads — deliberately links, not duplication)

- [`../websites/merge-hold-at-head-2026-07-11.md`](../websites/merge-hold-at-head-2026-07-11.md)
  — **sibling failure mode, stated explicitly per the dispatch**: state written into
  coordination files that no automation enforces or re-validates. The hold's finding is
  spatial (a HOLD nothing *reads*, so armed auto-merge fires through it); this guard's is
  temporal (a watch everything *copies*, so staleness compounds). Same doctrine, two axes —
  a kit slice carrying its check_claims carve-out is a natural carrier for this advisory too.
- [`../substrate-kit/parallel-session-heartbeat-reconcile-2026-07-10.md`](../substrate-kit/parallel-session-heartbeat-reconcile-2026-07-10.md)
  — the complementary heartbeat hazard: concurrent overwrites LOSING sibling facts vs
  sequential overwrites KEEPING facts past their evidence; both land as advisories on the
  same kit status-checker surface.
- [`lint-bundle-2026-07-11.md`](lint-bundle-2026-07-11.md) — `--heartbeat-keys` is the
  syntactic leg (declared key-set presence); this adds the semantic-freshness leg in the
  same always-exit-0 family.
- [`coordinator-archive-handoff-ceremony-2026-07-11.md`](coordinator-archive-handoff-ceremony-2026-07-11.md)
  — the guard is the missing re-affirm step at exactly the seam that ceremony names; its
  trigger-disposition table (every carried trigger dispositioned, none inherited silently)
  is the precedent shape, applied to watches.
- Not dups, same family: `../websites/own-heartbeat-parse-self-check-2026-07-11.md`
  (parseability, not freshness), `../superbot-mineverse/heartbeat-ladder-field-2026-07-11.md`
  (whose probe found machine *regeneration-from-source* mooted verbatim carry at the manager
  roster — the strong-form fix this guard's stamp is the cheap form of),
  `../superbot/queue-slice-staleness-age-2026-07-10.md` and
  `../superbot/reconciliation-slot-carry-tracker-2026-07-10.md` (staleness-age for carried
  lane-internal artifacts, not fleet heartbeat grammar).

Captured awaiting probe — the claim here is the mechanism and its live instances, not a
verdict. Probe should verify what watch grammar (if any) the kit-planted `control/README.md`
prescribes at live kit HEAD, pick the checker's home (kit-side vs per-repo preflight), and
price the /fleet badge half.
