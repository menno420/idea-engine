# Golden recapture on current-bot bug fix — a protocol so parity never preserves a bug — link index

> **State:** parked(routed — superbot-next protocol/CI slice: recapture-disposition ledger + warn-first checker on the parity corpus source pin; the superbot-side checklist half manager-routed per Q-0260; no sim question — a protocol contract is proven by its own red/green)
> **Class:** process · **Target:** `menno420/superbot-next`
> **Sequence:** before superbot-next CUT-1 (recapture is only honest while the frozen live-bot reference stays runnable under the capture harness)

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/golden-recapture-on-bugfix-2026-07-03.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/golden-recapture-on-bugfix-2026-07-03.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/golden-recapture-on-bugfix-2026-07-03.md)).

A protocol so rebuild parity goldens never preserve a bug: when a current-bot bug is fixed after goldens were captured, re-capture the affected goldens in the same PR.

## Probe report (v0, 2026-07-11)

> **Grounding:** https://github.com/menno420/superbot-next@2f4b2c3dcf4a13f32dd1e758908a886cc5b1d704 · fetched 2026-07-11T17:57:33Z
> *(pin annotation: N = superbot-next live HEAD by `git ls-remote` at 17:57Z; per-file
> raw reads at N: `docs/decisions.md` (D-0019 :140-144 corpus import + reviewed-change
> rule; D-0028 :205-212 replay adapter, "parity flips stay at zero honestly";
> D-0050 :375 + D-0062 :462 band-1/band-5 parity rows still pending; D-0071 :545 —
> gate 220/220 across **37 ported** subsystems, corpus 467 = 465 imported + 2 MINTED
> by the new bot's own capture_case); `parity/parity.yml` (source pin
> `menno420/superbot @ 7f7628e12f3b89c5c2a1fbdcfb039787df269e20`, `goldens: 465`,
> `minted_goldens: 2`; flip = the port PR's deliberate last commit, one-way door);
> `parity/README.md:24-32` § "The integrity rule". Greps for `recapture|re-capture`
> over the fetched decisions.md, parity.yml, and parity/README.md: the README's one
> hit is the harness-normalization clause ("re-captured verbatim"), decisions.md and
> parity.yml carry ZERO — no bugfix-recapture protocol exists at N.)*
> **Grounding:** https://github.com/menno420/superbot@2c7d2de770fee76008b4561ef8165f1d97d78a52 · fetched 2026-07-11T18:05Z
> *(pin annotation: S = superbot live HEAD by `git ls-remote`, cited as the drift
> clock only — the consumed corpus is pinned at `7f7628e1` while S has moved past it
> (merge=deploy cadence), so the flip window's drift is real, not hypothetical.
> Canonical idea doc re-read whole at the harvest pin `fd638e3` (raw): the collision,
> the six routed live bugs (two money bugs), and the one-line durable fix are as the
> capture states.)*

> Single-pass battery (panel not escalated: process/protocol head, reversible
> park/route decision, no security/data/spend/public blast radius). Third TOP-5
> item 1 (PR #194 mint — "parity flips are live NOW … zero recapture protocol at
> N: every current-bot bugfix in the flip window can silently bake a bug into a
> golden"); mint-time ledger grep re-verified at probe-time HEAD per the README
> battery's cross-lane verify-first paragraph.

**1. What is this really?**
The missing HALF of an integrity rule that already exists. The target's parity
corpus is the rebuild's acceptance oracle, and its integrity rule
(`parity/README.md:24-32` at N) already LEGALIZES a golden change whose reason is
"the current bot's behavior changed deliberately in PR #N" — permission without
detection: nothing notices that a live-bot bugfix invalidated a golden, nothing
demands the recapture-or-record decision the canonical doc named. The capture's
collision is now live, not hypothetical: flips are real (37 subsystems `ported`,
gate 220/220 at D-0071; the D-0028 adapter made flips possible; band rows still
pending at D-0050/D-0062 mean the window is still open), the corpus is frozen at
superbot `7f7628e1` while the live bot has moved to `2c7d2de`, and the target's
decision ledger + parity manifest carry zero recapture protocol. A bug fixed on the
live bot after capture leaves its golden encoding the BUGGY behavior — the rebuild
faithfully reproduces the bug and parity goes green on it.

**2. What is the possibility space?**
(i) Do nothing — every behavior-changing live-bot fix in the flip window silently
converts a golden into a bug-preservation contract; invisible precisely because
parity stays green. (ii) Checklist-only discipline at superbot (the canonical doc's
one-liner) — exhortation; the target lane's own enforce-don't-exhort doctrine
(Q-0132, cited on the A-2 ledger it ships) argues this alone under-delivers.
(iii) A recapture-DISPOSITION ledger at superbot-next: a committed section keyed on
superbot PRs/shas past the source pin, each row carrying one disposition —
`re-captured @ PR #N` / `pre-capture, no golden yet` / `behavior-neutral` — plus a
checker over the rows. (iv) Full recapture automation — re-run the capture harness
per fix and re-import; heavyweight, cross-repo write, disproportionate.
(v) Per-flip staleness review — fold "which fixes landed on this subsystem since
the pin?" into the A-16 flip review as a judgment step; catches drift late but at
the moment it matters most.

**3. What is the most advanced capability reachable by the simplest implementation?**
Oracle-drift accounting for one ledger section and one small checker: the corpus
source pin is already machine-readable (`parity/parity.yml` `source.sha`), and the
lane already ships the EXACT pattern this needs — the A-2 schema-growth ledger
(D-0005: same-PR ledger entry + a stdlib checker diffing reality against the
ledger, verified live at N by this PR's twin item). Copying that shape onto golden
drift (disposition rows + a `tools/check_*` seat in the existing 19-checker fleet)
buys "parity green means parity with the INTENDED behavior" for roughly one file
and one checker.

**4. What breaks it?**
(a) Cross-repo detection: superbot-next CI checks out only its own tree, so a
hermetic checker can verify dispositions are well-formed and current, but cannot
itself enumerate superbot's commit stream — the drift ENUMERATION (git log
`7f7628e1..HEAD` scoped to captured-surface paths) is wake-time/protocol work, the
same hermetic/non-hermetic split this repo's own check_harvest uses. (b) The
recapture half needs the OLD capture harness against the live bot (it lives at
superbot, `parity/harness/`), and stays honest only while the frozen reference is
runnable — the window closes toward cutover (hence the Sequence line). (c)
Normalization drift: a re-captured golden carries today's harness normalization
and can diff on noise against the 465 imported — D-0071's two minted goldens
already had to strip kernel-spine surfaces for exactly this class. (d) Volume:
most superbot commits don't touch captured behavior; an unscoped disposition duty
becomes a treadmill — the rule must key on captured subsystems' paths.

**5. What does it unlock?**
Parity green becomes trustworthy through the whole flip window and into cutover:
the six routed live-bot bug fixes (two money bugs) can land without silently
poisoning the oracle; each A-16 flip review gets a staleness answer instead of an
assumption; CUT-1..CUT-3 inherit a documented drift ledger instead of an
archaeology pass; and the corpus-change machinery D-0071 built for MINTING new
goldens gains its inverse — a rule for when existing goldens must change.

**6. What does it depend on?**
(a) The machine-readable source pin (`parity/parity.yml` `source.sha` — exists).
(b) The capture harness at superbot staying runnable against the live bot
(pre-cutover window — the Sequence constraint). (c) A disposition home + checker
seat, both target-owned (parity.yml or a sibling ledger; the `tools/check_*`
fleet). (d) The superbot-side half — recording "pre-capture, no golden yet" at
fix time — is a one-line checklist duty on the OTHER repo, manager-routed
(Q-0260: this repo writes nothing lane-side). (e) Nothing owner-shaped.

**7. Which lane should build it?**
`menno420/superbot-next` — it owns the consumed corpus copy, `parity/parity.yml`,
the checker fleet, the A-16 flip review, and the A-2 ledger pattern to copy;
superbot's half is one checklist line the manager routes alongside. NOT sim-lab:
no distinct evidence question survives that a simulator could settle — which fixes
landed since `7f7628e1` is a git-log fact, whether a disposition rule catches
drift is proven by the checker's own red/green (the #114 precedent: a contract
check is its own evidence), and the only judgment call (the disposition
vocabulary) is lane design-review material, not simulation.

**8. What is the smallest shippable slice?**
Lane-side: a `recapture:` disposition section in `parity/parity.yml` (rows keyed
on superbot sha/PR past `source.sha`, disposition ∈ {re-captured @ PR,
pre-capture, behavior-neutral}) + a warn-first checker in the existing fleet
validating row shape and that the newest disposition is not older than the source
pin — with the wake-time drift enumeration documented as the non-hermetic half.
This-repo-side: this probe + park (nothing else to build here, Q-0260).

**Recommendation: park** — routed: the recapture protocol is superbot-next lane
protocol/CI work (the lane owns the corpus, the manifest, the checker fleet, and
ships the exact ledger+checker pattern to copy at D-0005); no sim-shaped evidence
question survives — drift enumeration is a git-log fact and the protocol is
proven by its own red/green. NO outbox proposal; the superbot-side checklist half
and the lane routing ride the manager sweep (Q-0260/Q-0264).
