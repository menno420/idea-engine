# Idea — Karma (thanks/upvote reputation) system — link index

> **State:** historical(built at superbot — owner-directed build 2026-06-22 on the plan's recommended defaults + reaction-to-thank PR #1620 2026-07-01; ported at superbot-next D-0037; predates this 2026-07-10 harvest)
> **Class:** product · **Target:** `menno420/superbot`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/karma-reputation-system-2026-06-22.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/karma-reputation-system-2026-06-22.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/karma-reputation-system-2026-06-22.md)).

A peer reputation system: members grant each other karma for being helpful — earned from people, not the bot, measuring community appreciation distinctly from XP (activity) and coins (economy); with a leaderboard.

## Probe report (v0, 2026-07-11)

> **Grounding:** https://raw.githubusercontent.com/menno420/superbot/8214200aa0c00dda4156748617c9482dadc4277a/docs/ideas/karma-reputation-system-2026-06-22.md@8214200 · fetched 2026-07-11T16:03:25Z
> *(pin annotation: superbot live HEAD S = `8214200aa0c00dda4156748617c9482dadc4277a` by `git ls-remote` 16:03:07Z — S has moved past the capture pin `fd638e3`; the canonical doc still exists at S with Status `ideas` and the STALE gate line "Roadmap horizon: `docs/roadmap.md` S1 — **Later** (wants the owner's answers to the 5 questions before PR 1)" — the adoption-record-rot class this repo's #161 sweep flag already names; `docs/roadmap.md` lines 316–321 at S carry the same stale gate. `docs/current-state.md` at S has ZERO "karma" hits (grep 0) — the gap that misled the #180 TOP-5 rationale ("zero karma in superbot current-state@main").)*
> **Grounding:** https://raw.githubusercontent.com/menno420/superbot/8214200aa0c00dda4156748617c9482dadc4277a/docs/subsystems/karma.md@8214200 · fetched 2026-07-11T16:04:22Z
> *(pin annotation: the subsystem folio is unambiguous — "**Last updated:** 2026-06-22 (built — owner-directed…)"; "Current state … **Shipped (2026-06-22):** the command surface (`!thanks`, `!karma`, `/karma`), the audited service + DB seam, the leaderboard category, operator settings"; "**Reaction-grant (react-to-thank)** — ✅ **shipped 2026-07-01 (PR #1620)**". Tree scan via read-only blobless clone at S (the standing capability recipe): `disbot/cogs/karma_cog.py` + `disbot/services/{karma_service,karma_config}.py` + `disbot/utils/db/karma.py` + migration `disbot/migrations/093_karma.sql` + INV-K test `tests/unit/invariants/test_inv_k_karma_service.py` + 8 `parity/goldens/karma/*.json` all EXIST (superbot's code lives under `disbot/` — bare-path probes 404, the stem-match lesson generalized to path roots). Build authority: `.sessions/2026-06-22-karma-build.md` — the owner "explicitly authorized building the Karma plan ('you can execute this plan', 2026-06-22)", executed with the plan's recommended defaults "since the 5 design questions were not individually answered". Shipped defaults, canonical constants in `disbot/services/karma_config.py`: DEFAULT_ENABLED=True · DEFAULT_COOLDOWN_SECONDS=3600 · DEFAULT_DAILY_CAP=10 · DEFAULT_REACTION_EMOJI="" (reaction opt-in, off by default).)*
> **Grounding:** https://raw.githubusercontent.com/menno420/superbot-next/14e503769202e7ca38609c2063366d8db60bf2f0/docs/decisions.md@14e5037 · fetched 2026-07-11T16:03:25Z
> *(pin annotation: superbot-next live HEAD N = `14e503769202e7ca38609c2063366d8db60bf2f0` by `git ls-remote` 16:03:07Z. **D-0037 "Band 4 slice 2: KARMA — peer reputation on the one-txn ledger discipline (INV-K)" · decided** — the shipped surface ported VERBATIM (!thanks / !karma [card] / !karma add / /karma ephemeral) over ONE CompoundOpSpec `karma.give`; stores `karma` + `karma_audit_log` (migration 0015, the anti-abuse source of truth — "NO separate cooldown table, shipped design carried"); "SETTINGS: … SettingSpec defaults PINNED equal to the policy constants (the shipped karma_config no-drift invariant, **now a test**)"; react-to-thank ported (same audited op, source="reaction"); INV-K reconciliation invariant (tolerance 0). **D-0061** (band-4 replay/live testing) found and fixed the karma clock split + refusal-copy envelope — the anti-abuse windows now read the clock they were written with, repeat grants BLOCK in replay. Karma is also a registered leaderboard provider at N (D-0038 manifests: aliases rep/reputation/karmalb).)*

> Single-pass battery (panel not escalated: verify-first is decisive, no ambiguity
> signal, no security/data/spend/public blast radius — README § probe battery). The
> briefed mandatory verify-first — is karma still unbuilt, and are the 5
> owner-stalled questions still open? — answered NO on both at S and N before the
> battery ran: karma SHIPPED at the target 18 days before this repo harvested the
> capture, and the rebuild has already ported and test-hardened it. The battery
> below prices what (if anything) remains. Batching note (briefed): the pairing
> with audited-score-subsystem-scaffold (#1346, TOP-5 item 4) DISSOLVES — karma
> never waited for the scaffold; it hand-stamped the six-piece shape on
> 2026-06-22 and is itself one of the scaffold idea's three named instances, so
> karma is probed alone and item 4 loses its "the moment karma starts" trigger
> (already fired, in the past tense).

**1. What is this really?**
A product idea (canonical superbot doc 2026-06-22, owner's one-word prompt
"Karma") asking for a peer thanks/upvote reputation system — earned from people
not the bot, distinct from XP and coins, with leaderboard and anti-farm rules.
The verify-first read makes it a DONE idea, twice over: superbot built exactly
this on 2026-06-22 — the same day as the plan, owner-directed ("you can execute
this plan"), plan PRs 1+2 in one pass — **18 days before this repo harvested the
capture** (2026-07-10), then deepened it with react-to-thank on 2026-07-01
(PR #1620); superbot-next has since ported the shipped surface verbatim as band-4
slice 2 (D-0037) and test-hardened it (D-0061). The capture premise ("blocked on
owner answers") was a stale-adoption-record artifact, not a live state.

**2. What is the possibility space?**
As-built (command + reaction grant surfaces, audited `karma_service.give` seam,
`karma`/`karma_audit_log` stores, KarmaProvider leaderboard, operator settings);
the owner-gated PR-3 remainder at the target — **karma roles** (auto-assign at
thresholds, e.g. "Trusted Helper" @ 50) and **milestone announcements**
(`karma.milestone` event + log channel), both explicitly "deferred (owner-gated)"
in the folio; a future downvote (the ledger's `delta` is signed, "leaves room");
and hygiene on the RECORDS — the canonical doc's Status line and the roadmap gate
line at S still read pre-build. Every branch is in-lane follow-through at
superbot (or its rebuild), not a new build.

**3. Most advanced capability reachable by the simplest implementation?**
Already reached, at the target, by the target: a farm-resistant peer-reputation
economy-adjacent signal with an append-only audit ledger AS the anti-abuse
source of truth (cooldown and daily cap are reads over `karma_audit_log`, no
separate state table) — and at N the same design upgraded to one-txn discipline
with a zero-tolerance reconciliation invariant (INV-K) and settings no-drift
pinned as a test. Nothing cheaper could deliver more; the shipped design is the
simple version.

**4. What breaks it?**
Nothing left here to break — the idea's own hard part (anti-abuse) shipped as
designed (no self/bot karma, per-pair cooldown, per-giver daily cap,
positive-only), and the rebuild's replay testing already caught and fixed the
one real integrity crack (D-0061: the two-clock split that let a repeat grant
land inside the cooldown window under a pinned clock). What a revival attempt
would break: re-opening the "5 owner questions" as if undecided would fork
authority the owner already exercised — the build ran on his explicit plan
authorization with recommended defaults, and his post-build rulings touch the
shipped surface (`give` banned surface-wide → `!karma add`, question-router).
The one live rot is DOCUMENTARY: stale Status/roadmap lines at S that can
mislead future harvests exactly as they misled this head's #180 ranking.

**5. What does it unlock?**
Already unlocking: the karma leaderboard rides the shared RankProvider registry;
karma is one of the three proven instances (economy/XP/karma) the
audited-score-subsystem-scaffold idea (#1346, TOP-5 item 4) generalizes from —
so this head's closure sharpens item 4's real question (scaffold value for the
NEXT score subsystem, not for karma). Marking it historical also clears the
standing TOP-5's item-2 slot and retires a false "ripest probe" from the queue.

**6. What does it depend on?**
Going forward: nothing — the build consumed the idea's dependency chain (the
economy/XP audited-seam architecture it named, the hardened raw-reaction seam
for react-to-thank). The un-built remainders depend only on the owner's PR-3
go (karma roles + milestones — an owner call at the TARGET's surface, already
ledgered in its folio) and on superbot-next's own band sequencing (parity rows
xp/karma/community stay pending per D-0061 by design).

**7. Which lane should build it? (honest routing)**
Nobody — it is built, by the right lane, at the right layer, twice. NOT
sim-shaped for sim-lab: the briefed candidate question (defaults sweep over the
5 owner-stalled knobs under adversarial/economy scenarios) is MOOT — the knobs
are shipped canonical constants (1h cooldown / 10 daily cap / reaction
off-by-default), live since 2026-06-22, operator-tunable per guild, and pinned
equal to spec defaults BY A TEST at N (D-0037); the economy-adversary surface is
null by design (pure reputation, non-spendable, Q-0190 — karma bridges to no
economic value, so farming it buys nothing an economy sim could price); and the
anti-abuse mechanism's integrity is already enforced by the rebuild's own replay
goldens + INV-K reconciliation. An external sweep would re-derive what shipped
defaults and a green parity gate already answer. NO outbox proposal — the
honesty guard outranks feeding sim-lab's empty queue (the #180 precedent).

**8. Smallest shippable slice?**
None here. The smallest TRUE remainders are both the target's own: (a) the
owner-gated PR-3 rest (karma roles + milestone announcements) — an owner
decision already parked on superbot's own folio, not evidence-shaped; (b) the
stale adoption records at S (idea-doc Status line, roadmap S1 gate line) — 
superbot's own docs, already covered by this repo's standing #161
adoption-record-retirement sweep flag (Q-0260: canonical-side fixes are
superbot's own). Neither is an idea-engine build or a simulation question.

**Recommendation: park** — built-at-target (superbot owner-directed build
2026-06-22 + react-to-thank PR #1620 2026-07-01; ported at superbot-next D-0037
with the defaults test-pinned and D-0061 integrity fixes): the system this idea
asks for shipped at the target 18 days before the harvest and the 5 "owner-
stalled" questions were consumed by the owner's plan authorization + shipped
defaults (karma roles alone stays deliberately owner-gated, at the target); per
the README's built precedent the state advances to `historical(...)`, and
nothing routes to sim-lab.
