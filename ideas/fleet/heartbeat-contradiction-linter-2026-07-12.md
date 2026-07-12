# Heartbeat single-home rule + intra-file contradiction linter — one fact, one home, and a flag when duplicates disagree

> **State:** sim-ready
> **Class:** process · **Target:** `menno420/sim-lab` (verification target per the Q-0264
> pipeline; the buildable artifact the verdict specs is substrate-kit territory — a
> grammar rule in the planted `control/README.md` plus an advisory in the kit
> status-checker family)
> **Grounding:** https://github.com/menno420/idea-engine/blob/c77563c92342be7ef56f0e927d572bf22d552729/control/status.md@c77563c · fetched 2026-07-12T21:59Z
> *(pin annotation: the live specimen revision — `c77563c` (#270, session-1 close-out)
> carries BOTH "failsafe cron trig_01T83UuVthszGBcENYwrTrm7 … STILL ENABLED and LEFT
> ARMED deliberately as the successor's dead-man bridge" (line 3, phase block) AND "The
> archiving coordinator's failsafe cron trigger AND its 15-minute send_later chain are
> being DISMANTLED with the chat archive" (line 9, ⚑ block) — the same trigger, one file
> revision, two dispositions. Read locally from this repo's own history this slice;
> corpus size verified: 22 committed revisions of `control/status.md`,
> `git log --follow`, `fc0bab6` → `0cfe15e`.)*

**Origin:** the session-2 boot card's 💡
(`.sessions/2026-07-12-ideas-lab-session2-boot.md`) — the booting coordinator had to
adjudicate the specimen contradiction by live trigger enumeration before it could trust
its own heartbeat, resolved in favor of ARMED (correct: the cron was live and became the
successor bridge). Promoted to a full idea + PROPOSAL 013 by this slice.

## The idea (reasoned to its fuller form — Q-0254 duty)

A heartbeat overwrite is a partial rewrite: each writer updates the blocks it owns and
carries the rest — often verbatim, sometimes by pointer. When the SAME fact lives in two
blocks (the failsafe trigger's disposition lived in both the phase line's
routine-disposition block and the ⚑ archive-handoff paragraph), one update plus one
carry manufactures a contradiction inside a single revision: at `c77563c` the file
simultaneously said LEFT ARMED and being DISMANTLED about `trig_01T83UuVthszGBcENYwrTrm7`.
Every successor then pays an adjudication tax — the session-2 boot resolved it only by
enumerating 956 live triggers — and the fix it applied was itself the missing rule,
declared ad hoc in prose at `e66c78a`: "routine state now lives ONLY in the phase line's
routine-disposition block". That rule exists nowhere in the kit grammar (kill test, run
this slice: `control/README.md` § status format prescribes nine fields and a file-level
`updated:` stamp; no single-home rule, no duplicate-fact check; "single" appears only
about inbox writers).

Two halves, cheapest first. **Single-home rule (structural prevention):** the planted
`control/README.md` gains one paragraph — a fact class with a canonical block (routine
disposition → the phase line's disposition block) appears there and ONLY there; other
blocks reference the home ("routine state: see phase line"), never restate it.
**Contradiction linter (mechanical detection):** an always-exit-0 advisory in the kit
status-checker family (`--heartbeat-keys` / `--open-work` lineage) that extracts keyed
facts (trigger ids `trig_…`, PR numbers, named routines) from ONE revision and flags the
key when two statements about it disagree on disposition class (armed/enabled/live vs
dismantled/deleted/disabled/paused). Whether the linter half is honest is exactly what
the sim must settle: heartbeat prose quotes and negates its own history (the `e66c78a`
carry line QUOTES "being dismantled" while DROPPING it as superseded — a naive
co-occurrence check flags the fix itself), so the detector's false-positive floor on
real heartbeat prose is an empirical question, not a design one.

**The sim (a measured spec sweep, the PROPOSAL 010/011 grammar, on a corpus neither
touched):** replay every detector cell over all 22 real committed revisions of this
repo's `control/status.md`. Axes: **fact-key extraction grammar** (trigger-id tokens
only / +PR numbers / +quoted routine names) × **disposition-vocabulary normalization**
(raw antonym co-occurrence / antonym classes with per-key attribution / +quotation- and
negation-span exclusion) × **comparison scope** (whole file / cross-block only). Scored
per cell: true catches (the `c77563c` specimen MUST be re-found), false positives on the
other 21 revisions (the `e66c78a` quotation-negation carry MUST NOT flag; nor may
same-class-different-key statements collide — `c77563c` line 3 legitimately says one
cron LEFT ARMED and eighteen `send_later` one-shots self-disabled), and recall on
planted contradictions (seeded disposition flips of real keyed lines, breaking the n=1
true-positive dependence). Deterministic, stdlib, no network: the corpus is `git show`
over this repo's own history.

## Relations (adjacent heads — deliberately links, not duplication)

- [`carried-watch-verdict-inheritance-guard-2026-07-12.md`](carried-watch-verdict-inheritance-guard-2026-07-12.md)
  — the temporal sibling, and the boot card's own named nearest neighbor: watches going
  STALE across overwrites (both copies agree; the evidence expired). This head is
  duplicate statements DISAGREEING within one revision — prevented structurally
  (single home) and caught mechanically (contradiction flag on shared keys). A watch
  can be perfectly stamped and still contradict its duplicate; a single-homed fact can
  still be stale. Orthogonal checks, same kit checker surface.
- [`lint-bundle-2026-07-11.md`](lint-bundle-2026-07-11.md) — head 5 (`--heartbeat-keys`)
  is syntactic (declared key-set presence); this is semantic (fact consistency across
  blocks), same always-exit-0 family.
- [`../substrate-kit/parallel-session-heartbeat-reconcile-2026-07-10.md`](../substrate-kit/parallel-session-heartbeat-reconcile-2026-07-10.md)
  — concurrent overwrites LOSING sibling facts; this is a sequential overwrite KEEPING
  two copies of one fact that disagree.
- `../websites/own-heartbeat-parse-self-check-2026-07-11.md` — parseability, not
  consistency; [`verdict-registry-2026-07-11.md`](verdict-registry-2026-07-11.md) —
  idea-file sim-verdict notes, not heartbeat blocks.
- vs the outbox: PROPOSAL 012 consumed the SAME corpus for a different question (wake
  economics — when the heartbeat is written); this asks whether its content is
  self-consistent. PROPOSALs 010/011 are the checker-spec-sweep precedent (doc cites;
  oracle copy drift) on different corpora and failure classes; no proposal touches
  heartbeat/coordination-file integrity.

## Probe report (v0, 2026-07-12)

> Single-pass battery (panel not escalated: process/lint head, report-only advisory,
> reversible, no security/data/spend/public blast radius — README § probe battery).
> Verify-first, run live this slice: (a) **specimen** — the contradiction is real and
> quoted byte-exact above (`git show c77563c:control/status.md`, lines 3 vs 9, same
> trigger id); (b) **corpus** — 22 committed revisions, `git log --follow --
> control/status.md`, `fc0bab6` (#220, first wake) → `0cfe15e` (#273), every revision
> locally replayable; (c) **the hard FP case exists** — `e66c78a` line 9 quotes the
> stale claim while negating it ("the stale Q-0265 'must re-arm both / being
> dismantled' paragraph is DROPPED as superseded"), carried verbatim again at
> `0cfe15e`; (d) **kill test NOT triggered** — `control/README.md` § status format
> (lines 117–130): nine fields, file-level staleness only, zero single-home or
> duplicate-fact grammar; the carried-watch probe's kit-side pin (template blob
> `71c9ce4` @ kit `8a544a6`) found the planted template identical on this point.

**1. What is this really?** A consistency invariant for coordination files: one fact,
one home — and where duplication happens anyway, a mechanical flag instead of a
successor's adjudication session. Consumers: overwriting coordinators (told at write
time they restated a homed fact), booting successors (the specimen cost the session-2
boot a 956-trigger enumeration to trust one line), and the manager sweep (a heartbeat
that disagrees with itself is worse than dark — it is confidently ambiguous).

**2. What is the possibility space?** (i) Do nothing — the next carry+update seam
manufactures the next contradiction, and each is adjudicated by hand against live
state. (ii) Single-home rule only — one grammar paragraph; prevention without
detection; violations surface only when a human notices. (iii) Linter only — detection
without prevention; the flag fires forever on a grammar that keeps inviting
duplication. (iv) Both halves, rule + advisory — prevention plus a tripwire for the
carries the rule cannot reach (quoted history, ⚑ prose). The sweep prices whether
(iii)/(iv)'s detector is honest at real-prose false-positive rates; if it is not, the
verdict downgrades the ship to (ii) — a legitimate, evidenced outcome.

**3. What is the most advanced capability reachable by the simplest implementation?**
A fleet-wide answer to "can coordination prose be consistency-checked mechanically at
all?" from one stdlib sweep over one repo's committed history. The winning cell (if
one exists) is directly the spec for a kit `--fact-consistency` advisory every adopter
inherits at `bootstrap upgrade`; a negative result is equally load-bearing — it pins
that heartbeat consistency must be structural (single-home grammar), not detected,
before the fleet invests in NLP-shaped lint anywhere else.

**4. What breaks it? (assumptions made explicit)** (a) **n=1 known true positive** —
the real corpus carries one verified contradiction; planted-flip recall is
load-bearing, not decoration, and the verdict must report real-TC and planted-recall
separately. (b) **The FP floor may be irreducible** — heartbeat prose quotes,
negates, and narrates its own history; if every normalization tier still flags
legitimate carries, single-home-only is the ruling (stated in the done-when as a
first-class outcome). (c) **Keyed facts only** — the detector reads shared tokens
(trigger ids, PR numbers); a contradiction stated in pure prose with no shared key is
out of scope by design, and the verdict must state that boundary. (d) **Consistency,
not truth** — two agreeing copies of a wrong fact pass this check; evidence freshness
is the carried-watch head's axis, deliberately not duplicated here.

**5. What does it unlock?** Successors trust the heartbeat's disposition facts without
re-enumerating live state (the specimen's exact tax); the kit checker family gains its
first semantic-consistency leg with a measured spec instead of a guessed one; the
`e66c78a` ad-hoc fix ("routine state lives ONLY in the phase line") graduates from
one-repo prose to planted grammar; and the fleet learns cheaply whether
contradiction-lint on coordination prose is viable before any lane builds one blind.

**6. What does it depend on? (cheapest confirm/kill, priced)** Nothing unshipped: the
corpus is this repo's committed history (verified, 22 revisions), the specimen and the
hard FP case are byte-pinned above, and the runtime is stdlib `git show` + regex.
Cheapest confirm evidence — already in hand this probe: one real contradiction born at
a carry+update seam, one real quotation-negation carry that must not flag, and a
documented adjudication cost (the boot's live-enumeration detour). Kill test, run
live: a kit grammar that already single-homes facts or checks duplicates — NOT
triggered (§ verify-first (d)). Sim-worthy or judgment-only: sim-worthy, and the
carried-watch probe's own boundary proves the distinction — that head was judgment-only
because its check is a deterministic grep for a token's PRESENCE; this one's open
question is a measured TC/FP tradeoff across a spec grid on real prose, exactly what
PROPOSALs 010/011 sent to sim-lab.

**7. Which lane should build it — and what does it displace or duplicate?** sim-lab
runs the sweep (deterministic, seeded, swept, falsifiable one-question output);
substrate-kit builds what the verdict specs (grammar paragraph + advisory in the
status-checker family — the same surfaces as the carried-watch fifth-touch rider, so
the manager may bundle them); the manager consumes the ruling. Duplicates nothing,
swept by name this slice (rg over ideas/ for contradiction/single/duplicate/heartbeat/
consistency, bootstrap.py and .substrate excluded): the four nearest neighbors and
their distinctions are stated in § Relations above; the only prior "contradiction" hit
in the tree is a design tension inside one superbot idea, not a checker.

**8. What is the smallest shippable slice?** One stdlib Python file (~150 lines) in a
sim-lab intake dir: enumerate `control/status.md` revisions from a local clone
(`git log --follow` + `git show`), extract keyed disposition statements per cell of
the (extraction grammar × normalization tier × scope) grid, plant seeded flips, emit
one table {cell → real-TC, FP count + flagged lines, planted recall} and a one-line
ruling. No network, reproducible from the seed and the repo.

**Recommendation: sim-ready** — the corpus is real and committed, the specimen and the
hard FP case are byte-pinned, and the output changes what the kit ships (rule alone vs
rule + measured linter) in a way neither intuition nor a grep can. THE ONE QUESTION
for the simulator: *Over the 22 committed revisions of idea-engine
`control/status.md` (`fc0bab6` → `0cfe15e`, `git log --follow`), which (fact-key
extraction grammar × disposition-vocabulary normalization × comparison scope) cell
catches the one known live intra-file contradiction — `c77563c` line 3 "STILL ENABLED
and LEFT ARMED deliberately" vs line 9 "being DISMANTLED with the chat archive", both
about `trig_01T83UuVthszGBcENYwrTrm7` — plus planted disposition-flip contradictions,
at near-zero false positives on the other 21 revisions (in particular NOT flagging
`e66c78a`'s quotation-negation carry "the stale Q-0265 … paragraph is DROPPED as
superseded"), and does the winning cell's TC/FP profile justify shipping a kit
advisory contradiction linter alongside the single-home grammar rule, or the rule
alone?* Done-when: the per-cell {real-TC, FP, planted-recall} table on the real
corpus, the winning cell's grammar/normalization/scope stated machine-readably, the
`c77563c` instance caught and the `e66c78a` carry un-flagged by the winning cell —
ending in ONE ruling: rule + linter (advisory spec named for the kit status-checker
family) / single-home rule only (FP floor too high on real heartbeat prose, stated
with the measured floor) / neither (the missing evidence named).
