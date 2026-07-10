# Project capability self-awareness — ask a seat what it can do, get an honest answer — link index

> **State:** sim-ready
> **Class:** process · **Target:** `menno420/superbot`
> **Grounding:** https://raw.githubusercontent.com/menno420/superbot/655e0fea62dbb64d2d5ec962da7fa5816c180c60/docs/ideas/project-capability-self-awareness-2026-07-10.md@655e0fe · fetched 2026-07-10T21:38Z

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/project-capability-self-awareness-2026-07-10.md`](https://github.com/menno420/superbot/blob/655e0fea62dbb64d2d5ec962da7fa5816c180c60/docs/ideas/project-capability-self-awareness-2026-07-10.md)
— harvested 2026-07-10 by the drift re-harvest slice, pinned @ superbot `655e0fe`
([raw](https://raw.githubusercontent.com/menno420/superbot/655e0fea62dbb64d2d5ec962da7fa5816c180c60/docs/ideas/project-capability-self-awareness-2026-07-10.md)).

Owner-raised (verbatim: a Project should be able to answer "what are your abilities?" honestly), prompted by sim-lab's freshly-booted coordinator lacking `create_trigger`/`send_later` while a worker it spawned minutes later had both — the fourth+ occurrence of seat-dependent capability variance across the fleet. Two halves: a platform ask (a first-party queryable per-session capability manifest — routed to the EAP wrap-up email, not buildable here) and a fleet-internal mitigation buildable now — a kit `bootstrap.py capabilities --probe` command that runs the known probe battery (scheduler tools? worker-seat differences? merge path? raw-read reachability?) and regenerates `docs/CAPABILITIES.md` from live results with dates + verbatim errors, so every seat boot can open with a probed, honest self-answer instead of paying the trial-and-refusal discovery tax. Closely related to the already-indexed `session-start-capability-self-probe-2026-07-10.md` (this doc is the owner-raised, fleet-wide restatement with a concrete kit home).

## Probe report (v0, 2026-07-10 — batched with `session-start-capability-self-probe-2026-07-10.md`, the same possibility space per the PR #26 harvest flag; that file carries the pointer disposition, this file carries the primary battery)

> **Grounding:** https://raw.githubusercontent.com/menno420/superbot/9624c5399f5b1a3da293c07ce930e8b0410d79e4/docs/ideas/project-capability-self-awareness-2026-07-10.md@9624c53 · fetched 2026-07-10T22:10Z
> **Sequence:** before the EAP wrap-up email send (window ends 2026-07-14) — the platform half of this idea rides that email as §(d) item 2 (superbot `docs/eap/gen1-wrapup-email-final-candidate.md` @ `9624c53`, SEND-READY, only the owner's Part 1 slot remaining), and the canonical doc says the mitigation's probed output "doubles as EAP evidence" — a verdict after the send misses that ride.

*Timeliness verified live FIRST (the PR #25 lesson). Superbot HEAD
`9624c5399f5b1a3da293c07ce930e8b0410d79e4` transport-verified via `git ls-remote
refs/heads/main` at 22:10Z — ahead of both harvest pins; BOTH canonical docs of this
pair are byte-identical at pin vs HEAD (equal sha256: `4988520…` @ `655e0fe`≡`9624c53`;
`06d3158…` @ `fd638e3`≡`9624c53`), so the header pins stay faithful. Live state of the
named build surfaces: (a) `bootstrap.py capabilities` does NOT exist — kit HEAD is
v1.7.1 (substrate-kit `src/engine/lib/config.py` @ `415c37e`) and its `cli.py`
subcommand table has no `capabilities` entry (the vendored v1.7.0 here agrees:
`python3 bootstrap.py --help` lists 28 subcommands, none capability-shaped); (b) the
LEDGER half already ships — kit `adopt` plants `CAPABILITIES.md.tmpl →
docs/CAPABILITIES.md` (`src/engine/adopt.py:66` @ `415c37e`) with an
OWNER-ACTION↔ledger xref advisory in `check --strict`, and the fleet master copy
(fleet-manager `docs/capabilities.md`, raw 200) is live with 2026-07-10-dated entries;
(c) superbot itself has NO `docs/CAPABILITIES.md` and NO `bootstrap.py` at `9624c53`
(both raw 404) — the dispatch repo is not a kit-adopted seat, so `Target: superbot` on
the header is where the canonical DOC lives, not where the build lands; (d) the owner
ask is OPEN: the platform half sits unsent in the send-candidate email (§(d) item 2,
verbatim owner words), so the fleet-internal mitigation window is live. Probe honest.*

**1. What is this really?**
An owner-raised honesty contract — "ask a project what its abilities are, and it could
answer honestly" (verbatim @ `9624c53`) — split into a platform ask (queryable
per-session capability manifest; routed to the EAP email, unbuildable here) and a
fleet-internal mitigation: turn the hand-maintained `docs/CAPABILITIES.md` ledger into
a re-runnable self-test (`bootstrap.py capabilities --probe` regenerating it from live
probe results with dates + verbatim errors). The founding incident is seat-dependent
variance: sim-lab's coordinator had neither `create_trigger` nor `send_later` while a
worker it spawned minutes later had both (canonical doc; 4th+ occurrence of the class).
PROCESS class; the product is a truthful answer at seat boot instead of the
trial-and-refusal discovery tax.

**2. What is the possibility space?**
Two probe PLANES, not one — this is the load-bearing decomposition of the pair:
- **Subprocess plane (kit command reachable):** everything a Python child process can
  attempt — git push walls (tag/branch-delete 403s), raw-read reachability,
  `api.github.com` blocks, env-token presence, ffmpeg availability. These are exactly
  the planted ledger's seed walls; a `--probe` can re-verify them mechanically.
- **Agent plane (kit command UNREACHABLE):** MCP/session tools — `create_trigger`,
  `send_later`, GitHub MCP, subagent spawn — are model-invoked; a subprocess cannot
  enumerate or call them. The founding incident lives ENTIRELY in this plane. Probing
  it takes an in-session ritual at seat start — which is precisely the sibling idea
  (`session-start-capability-self-probe`, canonical @ `fd638e3` ≡ `9624c53`): the pair
  is one surface, two planes.
- **Escalations:** per-seat-type ledger sections (coordinator vs worker vs CI);
  probe-annotates-never-overwrites (hand-written nuance like "session-dependent"
  survives); fleet roll-up into fleet-manager's master ledger; the platform ask
  obsoleting the whole coping layer from the inside.
- **Degenerate corner:** a probe that overwrites the ledger with one seat's answers —
  a single lucky seat's world laundered into "the repo's abilities" (see Q4).

**3. What is the most advanced capability reachable by the simplest implementation?**
A kit `capabilities --probe` that runs only the SUBPROCESS-plane battery and rewrites
only a fenced `## Probed (generated)` section of the planted ledger — dates + verbatim
errors, hand-written sections untouched — plus a one-line session-start nudge ("run
your toolset checklist, append per-seat") covering the agent plane. That already
converts the ledger's seed walls from prose-that-rots into a re-runnable test in every
kit-adopted repo at once (the adopt/upgrade path ships it fleet-wide for free), and the
regenerated output is EAP-evidence-grade (dated, verbatim, reproducible) before the
2026-07-14 send window closes.

**4. What breaks it?**
- **Per-seat variance (the founding incident, inverted):** capabilities are
  SESSION-properties, the ledger is a REPO-file. A probe run from one seat records that
  seat's world as the repo's answer — the exact laundering class Q-0120 names, now
  automated. Idea-engine's own planted ledger already encodes the counterexample by
  hand: "self-merge classifier … the boundary differs by session kind"
  (`docs/CAPABILITIES.md` @ this repo). Whether file-granularity regeneration can be
  honest AT ALL is the evidence question below.
- **Transient-vs-structural confusion:** a flaky network 403 recorded as a wall, a
  timing-lucky success recorded as a capability — a probe has one sample; the
  hand-written ledger encodes judgment ("don't re-probe; the working route is…").
- **The subprocess wall:** the command physically cannot probe the plane that motivated
  the owner's ask (MCP toolsets) — shipped alone it answers the easy half and may be
  mistaken for the whole answer.
- **Hand-discipline counterfactual is weak too:** this repo's planted append log has
  ZERO entries since adoption (`docs/CAPABILITIES.md` § Append log) — "hand-written
  stays honest" is not the safe default either; both regimes need evidence.
- **Obsolescence race:** if Anthropic ships the §(d)-item-2 platform manifest, the
  probe layer becomes redundant scaffolding (the canonical doc says so: "built from the
  outside until the platform provides it from the inside").

**5. What does it unlock?**
Every seat boot opens with a probed, honest self-answer instead of the discovery tax
(four founding packages carry a worker-seat-retry recipe purely as a workaround —
canonical doc @ `9624c53`); the ledger's DISCOVERY RULE step 1 ("check this file")
becomes trustworthy because the file is re-verified, not remembered; per-seat variance
stops being an incident class and becomes recorded structure; and the probed output
feeds the EAP email as evidence while the window is open. Nothing is hard-blocked
today; the cost of absence is paid per seat boot, and seats are multiplying (three
games-seat boots pending per Q-0259 r.5).

**6. What does it depend on?**
- **substrate-kit** — the only sane build home: it owns `bootstrap.py`, the planted
  ledger template (`adopt.py:66`), the xref advisory, and the adopt/upgrade
  distribution path. A superbot-side script would orphan the fleet (superbot is not
  even kit-adopted — no `bootstrap.py` at `9624c53`).
- **A verdict on the honesty question** (below) — it decides the output schema
  (regenerate-whole-file vs per-seat annotate) BEFORE a fleet-wide command ships wrong.
- **The agent-plane ritual** (sibling idea) for the toolset half — kit `session-start`
  injection is the natural carrier.
- **fleet-manager's master ledger** as the sync target (its header names the relay).
- No unmerged prerequisite: ledger template, seed walls, and probe recipes all exist at
  kit HEAD `415c37e` / fleet-manager HEAD today.

**7. Which lane should build it?**
**substrate-kit builds the command** (one grammar/one-parser logic from the PR #29
seat-boot routing applies verbatim: one ledger template, one prober, kit-versioned —
a second implementation elsewhere is the drift class its `host-checkers-one-gate`
capture tracks); **kit `session-start` carries the agent-plane checklist** (same lane);
**fleet-manager is the standing co-consumer** (master-ledger roll-up at its sweeps);
**sim-lab settles the evidence question first** — it is the lane that LIVED the
founding incident (its coordinator/worker split is the canonical reproduction rig) and
the pipeline's designated evidence gate (Q-0264). Not idea-engine: fleet-wide consumer,
so `park(built-here)` does not apply. Cross-linked into
`ideas/substrate-kit/README.md` § Cross-links (by link, PR #17 rule).

**8. What is the smallest shippable slice?**
For sim-lab (the next pipeline step): ONE reproduction run — execute the two-plane
battery from its two documented seat types (coordinator + spawned worker, the OA-003
pair): agent plane = the sibling idea's toolset checklist (scheduler tools, MCP, spawn,
Bash), subprocess plane = the seed-wall battery (push walls, api.github.com, raw
reach, env tokens); diff the four result sets against each other and against the
hand-maintained ledgers' verified walls; count false walls / false capabilities;
conclude which output schema is honest. For the eventual kit ORDER (after the
verdict): `capabilities --probe` writing only a fenced generated section per the
verdict's schema, plus the session-start agent-plane nudge — one kit slice, distributed
fleet-wide by `upgrade`. What must NOT ship: a whole-file regenerator before the
per-seat honesty question is answered (Q4).

**Recommendation: sim-ready** — a genuine evidence question exists and gates the build:
capabilities are session-properties while the ledger is a repo-file, so whether an
automated probe can regenerate `docs/CAPABILITIES.md` HONESTLY (across seat types,
vs transient noise, vs the hand-maintained baseline) is empirically open — and sim-lab
owns the exact coordinator/worker split that founded the idea; PROPOSAL 005 appended.
