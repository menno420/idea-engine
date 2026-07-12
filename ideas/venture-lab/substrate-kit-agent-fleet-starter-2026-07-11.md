# substrate-kit as a product — agent-fleet starter kit

> **State:** parked(owner-gated — behind kit public-readiness: settled name + P8 + P11/P13 + curation; re-open on public flip under a settled name, or on a manager ownership ruling)
> **Class:** venture · **Target:** menno420/venture-lab
> **Grounding:** https://raw.githubusercontent.com/menno420/fleet-manager/main/docs/roster.md@6d5e3b3 · fetched 2026-07-11T18:54Z
> **Sequence:** behind substrate-kit public-readiness gates (settled name · P8 license confirm · P11 public flip or P13 veto path — kit docs/current-state.md@8a544a6)
> **Shortlist rank:** 1 of 5 · sellables brainstorm 2026-07-11 · [batch](sellables-brainstorm-batch-2026-07-11.md)

## What it is

Package substrate-kit — the bootstrap that turns any repo into an agent-operated project — as a public product: an "agent-fleet starter kit". The kit already exists at v1.10.0 in this repo and carries the full operating ceremony as working machinery: section claims in `control/claims/`, coordinator heartbeats, the `bootstrap.py check --strict` gate, and the merge-on-green landing path (auto-merge enabler + required substrate-gate check). The product is the same kit plus packaging: a public landing README, a docs page built on the websites lane's static machinery, and a sponsor/license split. Sell channel is GitHub sponsorware — public repo with sponsor-gated support and extras — plus a Gumroad one-time license for a pro docs/templates bundle.

## Why shortlisted

Biggest asymmetric upside on the list. The asset already exists at v1.10.0 and is proven by this very fleet — every claim, heartbeat, and merge-on-green landing in this repo's history is a live demonstration that the product works. That makes the product-build cost effectively zero: this is pure packaging, not construction. The doctrine docs the pro bundle would ship are already written across the fleet. And because agent-orchestration tooling is a live topic in 2026, the story ("the kit an actual autonomous agent fleet runs on") is plausible enough to earn attention without inventing anything.

## Smallest shippable slice

A public landing README + one docs page (websites-lane machinery) with a sponsor link. No kit code changes at all — the slice is entirely presentation. This can ship as soon as the owner clicks the two gates: making the repo public and creating the sponsor account.

## Honest effort / plausibility

Docs-heavy, low code effort — the cheapest build-to-value ratio here, but the revenue expectation must stay conservative per Q-0259 r.4: interest in agent-orchestration tooling is plausible in 2026, revenue is not. Without promotion, tens of dollars/month of sponsorship at best. The binding constraint is distribution, not the product — which is exactly why the batch's cross-cutting note pairs this with the playbook (rank 5) and the devlog sponsorware (batch #12) as a mutually-reinforcing distribution stack. Owner clicks required before any money can move: repo public + sponsor account.

## Open questions

- Open-core boundary: what stays sponsor-gated (support, pro templates, upgrade guides?) versus free in the public repo — the split determines whether sponsorship has any pull.
- Ownership: does fleet-manager or venture-lab own the productization? The kit is fleet infrastructure; the sale is a venture. The boundary needs deciding before the landing page names a maintainer.

## Probe report (v0, 2026-07-11)

> **Grounding:** https://raw.githubusercontent.com/menno420/substrate-kit/main/README.md@fa921f4 · fetched 2026-07-11T19:08Z

Verify-first pass (read-only worker, this session): substrate-kit main pinned at `fa921f43fa1002c4769b6903acb7a057bb750030` (`git ls-remote` + shallow clone; README, pyproject, LICENSE, CHANGELOG, docs/current-state.md, docs/adopters.md, release machinery all read at that ref); fleet-manager roster pinned at `6d5e3b3` (matches the capture's grounding, re-confirmed still HEAD via ls-remote); idea-engine local refs cited @ `37d2592`. The github.com atom feed for substrate-kit is session-walled from this seat ("GitHub access to this repository is not enabled for this session") — git transport + raw covered everything.

**1. What is this really?** A repackage-for-sale of an already-extracted asset — NOT packaging work still to be done inside this repo. The kit source verifiably lives at `menno420/substrate-kit` as its own repo AND its own fleet lane (roster@6d5e3b3: "kit-dev lane, coordinator-dispatched worker", `v1.12.0-WAVE SLICE CLOSED`): `src/engine/` source-of-truth, `src/build_bootstrap.py`, `dist/bootstrap.py` matching this repo's vendored header. The capture's "exists at v1.10.0 in this repo" conflates the vendored dist (control/status.md:5 @37d2592) with the product: kit HEAD is **v1.12.0** (pyproject.toml@fa921f4), with 16 releases in 3 days (CHANGELOG: v1.0.0 2026-07-09 → v1.12.0 2026-07-11, non-empty `[Unreleased]`) — a fast-moving dependency, not a frozen artifact. The batch line itself scoped the claim honestly ("v1.10.0 **here**", sellables-brainstorm-batch-2026-07-11.md:22); the capture dropped the "here".

**2. What is the possibility space?** Channel shapes: sponsorware as captured; GitHub Releases distribution (machinery already LIVE at fa921f4 — `.github/workflows/release.yml`, `docs/operations/release-runbook.md`, each tag ships `bootstrap.py` + sha256 + release.json); pip (pyproject exists but states "do not publish to PyPI from here"); Gumroad pro bundle; plus the batch's own distribution stack (playbook rank 5 + devlog #12). Every shape funnels through the same owner gates recorded in the KIT's own `docs/current-state.md`@fa921f4: 👤 P8 "confirm the MIT license" (applied as the flagged ⚑ default at KL-1, still pending) and 👤 P11 "flip the repo public" (KF-10, pending, with a veto path → 👤 P13 read-only PAT) — plus the README's verbatim "`substrate-kit` is a placeholder name — the published name is the owner's call at extraction". And the open-core split (this file's own open question 1) exists NOWHERE in either tree — until it is drafted, a sponsor link has no gated tier behind it to sell.

**3. What is the most advanced capability reachable by the simplest implementation?** The asset is unusually close to sellable for a fleet artifact: MIT LICENSE file present ("Copyright (c) 2026 Menno van Hattum"), pip-installable pyproject, versioned sha256-provenanced GitHub Releases, a public-facing 7.2KB README (what-it-does, one-step adopt, staged-learning contract, daily loop, layout), and `docs/adopters.md` — a GENERATED adopter registry that is machine-made social proof ("the kit an actual autonomous fleet runs on" is literally auto-documented). The repo also appears likely already public (differential raw test: substrate-kit README 200 where a known-private adopter repo 404s through the same anonymous-behaving proxy path) — though P11's pending status contradicts this, so public-status is UNSETTLED, not confirmed. Simplest real move: a curated public cut + landing copy, not a flip of the working repo as-is.

**4. What breaks it?** The capture's core costing. "Pure packaging, product-build cost effectively zero … can ship as soon as the owner clicks the two gates" is contradicted in scope: (a) THREE decision gates, not two clicks — name placeholder + P8 license confirm + P11 public flip are all pending owner actions in the kit's own current-state.md@fa921f4 (the sponsor account is a fourth); (b) the repo carries fleet-internal material a product repo must triage before publicity — 120+ `.sessions/` cards, `control/` (inbox/status/claims), `docs/owner-profile.md`, planning/gen2/retro/succession trees, `telemetry/`, `bench/`; (c) no quickstart, no `examples/`, no docs page, no sponsor link exist anywhere (`rg -il 'quickstart|installation|getting started'` across docs/ + README → zero hits); (d) 16 releases in 3 days means packaging pins a moving target — this repo's own history shows live upstream-fix churn (kit #176 verified on a lane's v1.10.0, ideas/websites/lane-backlog-2026-07-10.md:193 @37d2592) and documented kit-machinery failure modes (docs/CAPABILITIES.md:71). "No kit code changes" verifies — the understatement is entirely on the presentation/gating side.

**5. What does it unlock?** The first revenue channel for the fleet's own infrastructure, with the adopter registry and this repo's merge-on-green history as zero-cost marketing evidence. Drafting the open-core boundary would also settle, once, what stays private for every future public-facing kit surface. It anchors the batch's mutually-reinforcing distribution stack (playbook + devlog) — the capture's pairing logic survives the probe.

**6. What does it depend on?** (1) The three kit-side owner gates (name, P8, P11) plus the sponsor-account click; (2) an open-core boundary decision — an owner/design call with no draft to react to yet; (3) internal-material curation of the kit repo — kit-lane work; (4) the ownership ruling (Q7); (5) distribution, the batch's own named binding constraint (revenue expectation conservative per Q-0259 r.4).

**7. Which lane should build it?** Unresolved — and this is the grooming gap. The roster @6d5e3b3 has no owner column; the productization prerequisites (P8/P11/name) are tracked KIT-lane-side as pending owner actions, while the SALE framing exists only in venture-lab; the kit lane self-describes as "kit-dev … coordinator-dispatched", and its founding constraint KF-2 ("the lab never writes to consumers", docs/adopters.md@fa921f4) bounds it against adopter repos, not against its own packaging. This file's open question 2 names exactly this split and no surface answers it.

**8. What is the smallest shippable slice?** Not the captured one. "Landing README + docs page + sponsor link, ships on two clicks" cannot ship as scoped: the landing copy would market a placeholder name, the sponsor link has no gated tier behind it (no open-core boundary drafted anywhere), and the public flip is explicitly held as pending owner action WITH a veto path (P11 → P13). The honest smallest slice is a re-scope, not a build: split this head into (a) a kit-lane public-readiness task — name decision relay + P8/P11 + internal-material curation, three of which the kit already tracks as its own pending actions — and (b) a venture-lab sale task — landing copy, docs page on the websites-lane machinery, and an open-core/sponsor-tier DRAFT presented as a paste-ready owner choice — sequenced behind (a), with the Q7 ownership ruling flagged for the manager sweep. No sim question exists to route: every open unknown (name, license confirm, public flip, boundary, ownership) is an owner or manager call with no parameter space, no corpus, and no evidence-settleable form — inventing one would duplicate the owner-queue surface, and the family-probe precedent (pricing elasticity, PROPOSAL-routed lane-side) has no analogue here. Rationale for the verdict: the asset is real and closer to sellable than anything else on the batch, but the capture's premise ("pure packaging", "two gates") is contradicted by the kit's own pending-action ledger and missing boundary — the file needs re-scoping into the two properly-owned heads above before any forward disposition.

**Recommendation: needs-more-grooming**

## Grooming pass (2026-07-12)

> **Grounding:** https://raw.githubusercontent.com/menno420/substrate-kit/main/docs/current-state.md@8a544a6 · fetched 2026-07-12T00:32Z

Follow-through on the probe's `needs-more-grooming`: the probe named the re-scope
("split this head into a kit-lane public-readiness task and a venture-lab sale task")
but left the gaps open. This pass closes them one by one, against a FRESH kit pin —
`git ls-remote` 2026-07-12 puts substrate-kit main at
`8a544a63d9b98bab41ac3ba0e31f8863216b7582` (v1.12.1 per pyproject.toml@8a544a6, one
release since the probe's fa921f4/v1.12.0), and the pending-owner-action ledger
re-read at that ref (current-state.md@8a544a6, items 6–7 + the pyproject name
comment) confirms ALL THREE kit-side gates still open: distribution name still the
"one-place-swappable placeholder", 👤 P8 (confirm MIT) still pending, 👤 P11 (public
flip, or veto → 👤 P13 read-only PAT) still pending.

**Gap 1 — the costing premise ("pure packaging … two clicks").** Closed by
replacement. Retired from this file's claims; the honest gate ledger is FOUR owner
decisions (settled name · P8 license confirm · P11 public-flip-or-P13-veto · sponsor
account) plus one kit-lane internal-material curation slice (120+ `.sessions/`
cards, `control/`, owner-profile/planning/telemetry/bench trees) plus a
venture-lab presentation build (quickstart/examples/docs page/sponsor link — all
verified absent by the probe). Revenue expectation unchanged and conservative per
Q-0259 r.4: tens of dollars/month without distribution.

**Gap 2 — the open-core boundary (open question 1) existed nowhere.** Closed by
drafting it, paste-ready (structured choice, recommendation first, per Q-0263.2):

- **(a) RECOMMENDED — kit free, service and extras gated.** Free: the entire
  working kit (MIT `bootstrap.py`, adopt path, README, versioned sha256-provenanced
  releases, the generated adopter registry — the registry is the marketing asset
  and must stay public). Sponsor-gated: support/answers, upgrade guides, extra
  host-check/template packs. Gumroad one-time: a pro doctrine bundle (operating-
  ceremony templates + worked examples as FILES) — kept explicitly disjoint from
  the rank-5 playbook e-book, which sells the NARRATIVE (cannibalization guard,
  new finding of this pass's dedup sweep).
- (b) Kit + all docs free, sponsor = support only — cheapest, weakest pull.
- (c) `bootstrap.py` free, docs gated — rejected: cripples adoption and kills the
  "an actual autonomous fleet runs on it" story.

Rationale for (a): sponsorship needs a durable artifact behind the link, not
goodwill; gating the kit itself contradicts both the MIT default and the proof-by-
adoption story.

**Gap 3 — ownership (open question 2 / probe Q7).** Closed by a recommended split,
flagged for the manager sweep: the **substrate-kit lane owns public-readiness**
(name-decision relay, P8, P11-or-P13, internal-material curation — three of the
four are ALREADY its own tracked pending owner actions at 8a544a6, so no new
surface is invented), and **venture-lab owns the sale head** (landing copy, docs
page on the websites-lane static machinery, sponsor tiers, Gumroad listing),
sequenced strictly behind. KF-2 ("the lab never writes to consumers",
docs/adopters.md) bounds the kit lane against ADOPTER repos, not against packaging
its own tree — no constraint blocks the split. This slice writes nothing under
`control/` (dispatch boundary): the flag rides this file + the session card for
the coordinator's next heartbeat, not a heartbeat line.

**Gap 4 — the smallest shippable slice was wrong.** Re-scoped. The captured slice
(landing README + docs page + sponsor link, "ships on two clicks") cannot ship:
the copy would market a placeholder name, the sponsor link has no gated tier, and
P11 is held WITH a veto path. The honest smallest slice shippable with ZERO owner
gates is the open-core boundary draft as a paste-ready owner choice — gap 2 above
IS that slice, so it no longer blocks. Next slice after the gates flip: venture-lab
landing copy pinned to a tagged kit release (gap 5's rule).

**Gap 5 — version conflation / moving target.** Closed by a pinning rule: the sale
surface never markets kit HEAD — it pins the newest tagged release (release.yml
ships `bootstrap.py` + sha256 + release.json per tag) and names that tag in the
landing copy. Cadence datapoint at re-pin: fa921f4/v1.12.0 (2026-07-11) →
8a544a6/v1.12.1 (2026-07-12) — still roughly a release a day; the rule is
load-bearing, not hygiene.

**Gap 6 — public-status unsettled (probe Q3's differential-raw anomaly).** Routed,
not resolved: whether the repo is de-facto public already is the kit-lane head's
verification, not a venture-lab premise. This pass re-confirms only that P11 is
still on the pending ledger at 8a544a6; the sale head's entry condition is
"verifiably public under a settled name".

**Dedup sweep (2026-07-12, `rg -g '!bootstrap.py' -g '!.substrate'` across
ideas/):** no true duplicate found.

- [`sellables-brainstorm-batch-2026-07-11.md`](sellables-brainstorm-batch-2026-07-11.md) — the parent batch (this head is its rank 1), source not duplicate.
- [`agent-fleet-playbook-ebook-2026-07-11.md`](agent-fleet-playbook-ebook-2026-07-11.md) — the rank-5 distribution-stack sibling; NEW overlap surfaced: its Gumroad e-book and this head's Gumroad doctrine bundle sell adjacent doctrine — boundary drawn in gap 2(a), files-vs-narrative.
- [`gba-homebrew-starter-kit-2026-07-11.md`](gba-homebrew-starter-kit-2026-07-11.md) — "starter kit" naming overlap only; different asset, different lane machinery.
- `ideas/substrate-kit/` (6 heads) — kit MACHINERY process/product heads (drift checks, auto-updater, gate seams); zero sale/productization overlap.
- `ideas/superbot/` kit-adjacent heads (`portable-agent-memory-package`, `kit-seed-command-fleet-repo-bootstrap`, `multi-repo-program-kit-lab-trading`) — zero sell-channel overlap.
- `ideas/product-forge/` — zero hits for sponsor/open-core/productization/sellable.

**Honest read after grooming:** weaker than the capture sold it, exactly as the
probe warned — the "biggest asymmetric upside" framing survives only as "cheapest
asset-to-story ratio". Correctly priced, the head is four owner decisions and a
kit-lane curation slice deep before the first sponsor link can exist, with
conservative revenue and distribution still the binding constraint. What grooming
genuinely improved: the boundary draft (gap 2) removes the one blocker that was
agent-shaped, and the ownership split (gap 3) makes the rest routable. Nothing
further is buildable from this repo until the kit-side gates flip — every
remaining unknown is an owner or manager call with no evidence-settleable form
(probe Q8's finding, re-confirmed at the fresh pin).

**Next step: park(owner-gated — behind kit public-readiness: settled name + P8 +
P11/P13 + curation)** — re-open trigger: the kit repo verifiably public under a
settled name, or a manager ownership ruling that re-scopes the gap-3 split.
