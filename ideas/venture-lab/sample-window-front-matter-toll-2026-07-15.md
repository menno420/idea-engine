# The sample is a budget, not a preview: front matter pays an exact exponential toll inside the 10% window, each front page raises the minimum viable book by nine, and the committed short formats sit on or under the cliff

> **State:** sim-ready
> **Class:** venture (pipeline rotation — the standing ORDER 003 VENTURE slot, round 14, BOOKS half; harvest source: venture-lab's COMMITTED MANUSCRIPTS themselves — the assembled Ultramarine novella and its serial episodes, the dormouse picture book, the comet-biscuit format pin — priced against the retail sample window every listing's conversion rides through)
> **Target:** sim-lab (verification target menno420/sim-lab per the Q-0264 pipeline; routing is the manager's per Q-0260, this repo never edits any other repo)
> **Grounding:** https://github.com/menno420/venture-lab@520bdfca71ca4f119808d1098cd4ecf7fc6e6732 · fetched 2026-07-15T07:59:15Z
> (FIRSTHAND: every measured word count, spread count, and format pin below is read from venture-lab's committed files at that pin and cited file@sha; every MODEL constant — the sample fraction α, the survival q, the hook k*, the assembly policies F — is invented-but-pinned in this file, and the DECISION arms are seedless exact rationals with zero repo/network reads at verdict time — the P017–P069 hermetic precedent)
> **Origin:** standing ORDER 003 (continuous new ideas per repo) under ORDER 004 rule 3 (deliberate lane rotation, "fleet backlogs → venture's book/product space → game mechanics → COMPLETELY UNRELATED domains"); round 14 opened at fleet backlogs with P069 (#432, merged 2026-07-15T07:44:03Z), so the venture slot is next — this head. Half evidence: the slot's own committed alternation (P018 books → P022/P026 trading → P030 books → P034 trading → P038 books → P042 products → P046 books → P050 products → P054 books → P058 products → P062 books → P066 products) puts round 14 on the BOOKS half.

**Harvest-tap disclosure (slot history):** the venture slot has tapped the publishing plan's §3/§4 conventions (P038, P054), the KDP keyword map (P046), the derived owner queue (P062), the ideation batches and their rubric (P042, P058), and the products lane's launch log (P050 secondhand, P066 firsthand). This head is the slot's FIRST tap of the committed MANUSCRIPTS themselves — the artifacts' own internal structure as the harvested constants. No prior head reads a word count, a spread count, or an assembly order.

## The committed claims (harvested @ 520bdfc)

1. **The assembled novella carries committed front matter.** `candidates/adult-novels/ultramarine/manuscript/ultramarine.md` @ 520bdfc opens with a title heading, a Status badge, the tagline "*A literary novella of Delft, 1654. ~27,900 words.*", and a content note ending "See README for the full note" — **57 words before the first chapter heading `## 1. Lapis`** (measurement rule: `awk '/^## 1\./{exit} {print}' | wc -w`). The full assembled file is **27,890 words** (`wc -w`). The content note is a committed shipping intention: a warning that "See README" cannot discharge for a retail reader travels WITH the artifact.
2. **The serial format exists as separate committed episode files.** `candidates/adult-novels/ultramarine/manuscript/part-one.md` @ 520bdfc is **8,809 words** (part-two 9,189, part-three 9,850) — the ORDER 005-priced per-episode funnel sells THIS artifact, at roughly a third of the omnibus length, and any produced episode carries its own front matter.
3. **The picture-book bodies are committed at exact lengths.** `candidates/childrens-books/dormouse/dormouse.en.md` @ 520bdfc pins its own body verbatim — "**Word count:** 634 (manuscript body, excluding spread/illustration notes)" — and contains exactly **12 `[Spread N]` blocks** (`grep -c '^\[Spread'`), with a 116-word header block before Spread 1.
4. **The lane's standard picture-book format is committed.** `candidates/childrens-books/comet-biscuit/en/book-1-the-great-jam-wobble.md` @ 520bdfc pins verbatim: "**Format:** 32-page picture book — 15 spreads" and "**Word count:** ~520". 32 pages = 2 pages front matter + 15 spreads × 2 pages: the committed format is internally exact.
5. **Nothing committed prices the sample.** `docs/publishing/CHECKLIST.md`, `PUBLISHING-PLAN.md`, `OWNER-QUEUE.md`, and the vetting packets @ 520bdfc reference "preview/test purchase" as an owner delivery check and cite KDP for AI-art disclosure — no committed sentence anywhere prices what fraction of the artifact a retail sample shows, or what the artifact's own front matter does to it. The assembly order of produced front matter (title, copyright, dedication, TOC, content note) is an unpriced convention defaulting to "everything up front".

## The mechanism (reasoned to its fuller form — Q-0254 duty)

A retail ebook sample (Look-Inside-style) is not a preview of the story — it is a **budget of B = ⌈α·(F + S)⌉ display units** (α ≈ 10%), counted from byte one, that the artifact's own front matter F spends before the story's S units start. A browsing reader survives each unit with probability q (geometric attrition) and converts if they get k* story units (the hook) read INSIDE the budget: **C = q^(F + k\*) · 1[F + k\* ≤ B]**. Three structure theorems carry the head, each an exact gate, none stated anywhere in the committed docs:

- **T1 — the exponential toll.** Within the budget, C(F)/C(0) = q^F exactly: front matter is never an additive nuisance, it is a per-unit multiplicative tax, and log C is affine in F with slope log q. "A couple of pages can't matter" is off by an exact exponential.
- **T2 — the cliff and the 9× lever.** The indicator makes conversion DISCONTINUOUS: at F > B − k* the sample contains no reachable hook and C = 0 for every q. Solving ⌈α(F+S)⌉ ≥ F + k* gives the exact minimum viable story length **S\*(F, k\*, α) = smallest integer S with α(F+S) > F + k\* − 1**; at α = 1/10 this is **S\* = 9F + 10k\* − 9**, so **each unit of front matter raises the minimum viable book by (1−α)/α = 9 units**. A composition choice measured in single pages moves a viability threshold measured in tens of pages.
- **T3 — heterogeneity is signed.** For ANY nondegenerate mixture of reader types q ~ μ, survival S(n) = E[q^n] is strictly log-convex (Cauchy–Schwarz on moment sequences): (a) S(n) > S(1)^n for n ≥ 2 — a single-q model matched on one-unit attrition strictly OVERSTATES the deep toll, so single-q REJECT numbers are conservative in a known direction; (b) the implied per-unit hazard is non-increasing — the FIRST front-matter unit always costs the most; (c) falsifier: any measured per-unit abandonment curve with INCREASING hazard kills the entire mixture-of-geometrics class, not just a calibration.

The decision object is the lane's **assembly convention**: FRONT-LOADED (title + copyright + dedication/content-note + TOC up front — the unpriced default) vs STORY-FIRST (legal-minimum front unit(s), everything else to back matter) vs MID, priced at the committed catalog's own measured lengths.

## Pinned model (measured constants @ 520bdfc; model constants invented-but-pinned, exact rationals)

- **Units:** prose = 250-word screens, ceiling division (NOVELLA 27,890 w → 112 screens; EPISODE 8,809 w → 36 screens); picture books = pages, hook in spreads (1 spread = 2 pages). Quantization is a declared convention; knife-edge cells are named and the decision rule may not rest on one.
- **Committed formats (4):** NOVELLA (S = 112 screens) · EPISODE (S = 36 screens) · PB15 (S = 30 story pages, claim 4's committed pin) · PB12 (S = 24 story pages, dormouse's committed 12-spread body).
- **Assembly policies:** prose F ∈ {1, 2, 3, 4} screens (STORY-FIRST = 1: title/copyright/note merged on one screen; FRONT-LOADED = 4: title, copyright, dedication + content note, TOC); picture book F ∈ {2, 3, 4} pages (legal minimum 2 = title + copyright, per claim 4's own 32 = 2 + 30 arithmetic).
- **Grids:** α ∈ {1/20, **1/10**, 1/5} · q ∈ {4/5, 9/10, **19/20**, 49/50} per unit · hook k* ∈ {2, **3**, 5} screens prose / {**1**, 2} spreads PB · plus the pinned two-point mixture (skimmer q = 3/5 w.p. 1/2, reader q = 49/50 w.p. 1/2) for T3. Decision cell bold. S\*-scan S = 1..400 for the T2 formula gate.
- **Arms:** Arm A seedless exact `fractions.Fraction` closed forms; Arm B independently-written brute unit-walk enumeration twin (exact-equal required); Arm R seeded reader-trace MC, REPORTING-ONLY (seeds 20261620–622; aux 20261623 never read; no statistical gate).

## Pre-registered decision rule (evaluation order: REJECT first)

- **REJECT** the front-loaded assembly default iff, at the decision cell (α = 1/10, q = 19/20, k* = 3 screens / 1 spread): (i) FRONT-LOADED (F = 4 prose / 4 PB) cliffs (C = 0 exactly) on **≥ 3 of the 4 committed formats**, AND (ii) the NOVELLA's front-loaded toll C(STORY-FIRST)/C(FRONT-LOADED) ≥ **11/10**.
- **INVALID** on any gate failure (below).
- **APPROVE** iff zero front-loaded cliffs across all 4 committed formats at α = 1/10 AND the toll ≤ 21/20 (mutually exclusive with REJECT by arithmetic).
- **NULL** otherwise, on named axes: the α axis (the real platform sampler is a model constant here — ONE free observation of an actual Look-Inside cut on any published title settles it, no owner spend); the quantization axis (a knife-edge cell straddling a band); twin-arm disagreement surviving INVALID. Every NULL is a finalized, citable finding with its exact tables, never a re-run request.

## Gates (run INVALID on any failure)

- **G1 twin arms:** Arm B (brute unit walk) equals Arm A (closed form) on every rational at every grid cell.
- **G2 (T1):** within-budget ratio C(F+1)/C(F) = q exactly, constant across F, every format × q.
- **G3 (T2):** cliff indicator flips exactly at F = B − k*; the S\* closed form (S\* = 9F + 10k\* − 9 at α = 1/10; general strict-inequality form at all grid α) matches the brute S = 1..400 scan at every (α, F ∈ 1..5, k* ∈ {1,2,3,5}).
- **G4 (T3):** pinned mixture: strict log-convexity S(n)S(n+2) > S(n+1)² for n ∈ 0..29; S(n) > S(1)^n for n ∈ 2..29; depth-decreasing toll S(n)/S(n+3) strictly decreasing over n ∈ {1, 4, 8, 16} — all exact Fractions.
- **G5 hand worlds (derived by hand in this file):** S = 10 pages, α = 1/2, k* = 2, q = 1/2: F = 1 → B = 6, C = (1/2)³ = **1/8**; F = 5 → B = 8, C = (1/2)⁷ = **1/128**; toll = **16**.
- **G6 battery:** q = 1 ⇒ every within-budget C = 1 and every toll = 1; α = 1 ⇒ no cliff anywhere with S ≥ k*; C monotone non-increasing in F everywhere; census anchors (§ Expected landing) reproduced verbatim.

## Expected landing (DISCLOSED per the P048–P069 exact-arm norm)

Both arms ran live at drafting (twin-arm mismatches: 0; S\* formula-vs-scan mismatches: 0). At the decision cell: **REJECT** — (i) FRONT-LOADED cliffs **3 of 4** committed formats: EPISODE B = 4, story screens in sample = 0; PB15 B = 4, story pages = 0; PB12 B = 3, story pages = 0; NOVELLA survives (B = 12, story 8 ≥ 3); (ii) NOVELLA toll = **8000/6859 ≈ 1.1664 ≥ 11/10**. Census anchors: C(NOVELLA, F=1) = 130321/160000 ≈ 0.8145; C(NOVELLA, F=4) = 893871739/1280000000 ≈ 0.6983; S\*(F=2, k\*=2, α=1/10) = **29 pages** — the committed 15-spread format (30 story pages) clears the threshold by ONE page and one extra front page moves it to S\* = 38 (19 spreads), four spreads past the committed format; PB12 (dormouse, 24 story pages) is **under the cliff even at the legal-minimum F = 2** (B = 3, one story page, hook needs two); EPISODE knife-edges at F = 1 (story screens = 3 = k\* exactly, margin 0 — named fragile cell, excluded from the decision clauses) and cliffs from F = 2. Falsifiability is live on both axes: at **α = 1/5 every committed format clears even front-loaded** (the α probe is the named NULL axis), and at **q = 49/50 the toll is 125000/117649 ≈ 1.0625 < 11/10** — clause (ii) dies one q step away. T3 legs verified exact (log-convex, S(n) > S(1)^n, depth-decreasing toll 1.5019 → 1.0628 from n = 1 to 16).

## Consequence (pre-registered; routing the manager's per Q-0260 — this repo edits no other repo, nothing here builds/publishes/spends)

- **REJECT →** paste-ready structured choice to the manager for venture-lab's assembly convention, recommendation first per Q-0263.2: **(a, recommended) STORY-FIRST assembly rule** — legal-minimum front unit (title + copyright + the committed content note merged on one screen; the note is a values-surface, keeping it front is the recommended default and costs exactly one unit by T1), dedication/TOC/series pages to back matter, PLUS the S\* table (9F + 10k\* − 9) added to the vetting checklist as a per-format publishability gate (a 12-spread body is under the 10%-window cliff under ANY assembly — a format decision, not an assembly one); (b) keep front-loaded assembly but hold every short format to S ≥ S\*(4, k\*) (19+ spreads / 57+ screens); (c) status quo + the one-observation α probe first. Composes with, never reopens, the served pricing verdicts: they price the PRICE of the funnel (ORDER 005/006, V037/V039/V040/V041 family), this prices the WINDOW the funnel's first click lands in — the Ultramarine free-first-episode funnel in particular sells an 8,809-word artifact whose 10% sample is 4 screens: its conversion rides clause (i) directly.
- **APPROVE →** the front-loaded convention stands, priced; note filed.
- **NULL →** the named α observation (free, no owner spend) or the quantization re-cut, tables attached.

## Dedup

Nearest priors, argued distinct: **P062 → V073** (books half) uses geometric survival as the γ-discount LEG of an owner-attention scheduling objective — there survival weights job completion indices and the decision is a SEQUENCING policy over 44 jobs; here survival IS the demand channel, the decision is artifact COMPOSITION against a platform-truncated budget, and the theorems (exponential toll, viability cliff, mixture log-convexity) have no scheduling analogue — zero shared fixtures. **P066 → (in flight)** truncates CALENDAR exposure by funnel onset τ against a kill deadline (decision object: the anchor of a clock); here the truncation is WITHIN-ARTIFACT position by the sampler (decision object: an assembly rule) — kinship is the word "truncation" only. **P046** prices the discovery SHELF (keyword tiling — where the title is found, nothing inside the artifact); **P038 → V049** prices KU revenue mixture (its "read-through rt" is a ROYALTY fraction, not position survival); **P054 → V065** prices an illustration dollar gate (VOI); **P018/P030 → V020/V032** allocate production tokens; **P058 → V069** prices a scoring instrument. The pricing SIM-REQUEST verdicts (ORDER 005/006 batch: serial per-episode/bundle/free-first, photo packs, ship-it bundle, cookbook PWYW) set PRICE POINTS — price never appears in this head's model, and the verdicts compose. Corpus grep at HEAD 10533ae: zero hits for front matter / look-inside / sample-window mechanics in any proposal or verdict P001–P069, V001–V082 (the only "read-through" hits are P038's royalty constant). This is the pipeline's first within-artifact composition head.

## Model basis (declared model-dependence — the P024 discipline)

Geometric (memoryless) per-unit abandonment is the pinned reader model, with T3 pricing the heterogeneity direction exactly; the sample fraction α = 1/10 is an invented-but-pinned platform constant (the committed KDP citations @ 520bdfc cover AI-art disclosure, NOT the sampler — no committed source pins it; hence the α grid and the named one-observation NULL probe); the hook model (convert iff k* story units read in-window) and unit quantization are declared conventions with the knife-edge exclusion rule; conversion is priced up to a positive constant (browse-to-sample rate) that cancels from every ratio and indicator the decision reads.

## Probe report (v0, 2026-07-15)

> Single-pass battery (panel not escalated: self-contained knowledge probe, sim is
> report-only evidence, no spend/publish/irreversible surface — README § probe battery).
> Verify-first ran FIRST, live this slice: (a) **dedup** — the corpus sweep
> `rg -i 'front.matter|look.inside|read.through|attrition|page.turn|free sample'`
> (bootstrap.py/.substrate excluded) at HEAD `10533ae` returned only P038's KU
> royalty constant ("read-through rt" — a revenue fraction, not position survival)
> and unrelated websites-lane "attrition" hits; the distinct-mechanism neighbors
> (P062 γ-discount scheduling, P066 calendar-exposure truncation, P046 shelf tiling,
> P054 dollar VOI) are argued in Dedup. (b) **kill test NOT triggered** — no prior
> proposal P001–P069, idea file, or session-card 💡 prices sample composition,
> front matter, or a truncated preview budget; no recorded drop of this head exists.
> (c) **feasibility + arithmetic checked LIVE** — both arms (closed form + brute
> unit-walk twin) ran at drafting in < 1 s stdlib and agreed on every rational
> (mismatches 0; S\* formula vs S = 1..400 scan mismatches 0); every measured
> constant re-read this session at venture-lab origin/main `520bdfc` (fetched
> 2026-07-15T07:59:15Z): 27,890 / 8,809 words (`wc -w`), the 57-word and 116-word
> front blocks (awk rule), 12 `[Spread` blocks, the verbatim "32-page picture book
> — 15 spreads" and "Word count: 634" pins; expected landing DISCLOSED (REJECT)
> with its exact drafting values rather than hidden, all rulings reachable, the
> α = 1/5 and q = 49/50 APPROVE-side witnesses named, INVALID controls gated.
> Seeds 20261620–623 swept collision-free at HEAD `10533ae` (registered priors
> 20261600–603 P068/V081 and 20261610–613 P069/V082; 20261614–619 the disclosed
> gap; standalone data numerals 20261664/20261833 per the recorded discrimination
> rule).

**1. What is this really?** A pre-registered EXACT MEASUREMENT of an unpriced
committed convention — the assembly order of front matter in venture-lab's produced
books — against the retail sample window it silently spends, taken at the committed
catalog's own measured lengths (novella, episode, two picture-book formats @
`520bdfc`). On exact `fractions.Fraction` arithmetic the conversion surfaces, the
toll ratios, the cliff census, and the S\* viability table are exact at every grid
cell, judged against bands fixed before any code (REJECT first: ≥ 3-of-4 committed
front-loaded cliffs AND toll ≥ 11/10; APPROVE: zero cliffs AND toll ≤ 21/20; NULL
otherwise with named axes), byte-identical across two runs, seeded traces demoted
to reporting-only.

**2. What is the possibility space?** (i) Don't run it — the round-14 venture slot
goes unserved and every future title inherits an unpriced assembly default. (ii) A
prose note "keep front matter short" — retells the direction, measures nothing,
misses all three keepers (the exponential form, the exact 9-pages-per-front-page
lever, the signed heterogeneity bound). (iii) Price the funnel again — reopens the
served pricing verdicts without adding structure; price never appears in this head.
(iv) An MC-only reader sim — leaves seed noise on decision numbers that are exact
rationals (the V065/V067 lesson); MC is demoted to Arm R. (v) This head: exact
census as the ruling, REJECT-first bands, INVALID on the G1–G6 gates, twin-arm
verification, falsifiability live on two named axes. (vi) Over-scope (real platform
sampler measurement, per-unit partial-credit hooks, back-matter read-through
economics) — each named as a follow-up, none in scope.

**3. What is the most advanced capability reachable by the simplest
implementation?** One ~120-line stdlib file: a budget formula, one closed-form
conversion expression, a brute unit-walk twin, and a grid loop — yielding the exact
conversion/toll/cliff surfaces, the S\* viability law verified as a THEOREM CHECK
against a 400-point scan, the mixture direction bound, and the per-format
publishability table the consequence menu ships — from a sim a verdict session runs
cold in under a second.

**4. What breaks it? (assumptions made explicit)** (a) **α is invented-but-pinned**
— no committed source pins the real sampler; the grid brackets 1/20..1/5, the
decision cell says 1/10, and the named NULL probe is ONE free observation of a real
Look-Inside cut. The REJECT's strongest clause (PB12 under the cliff at legal
minimum) survives α = 1/10 ± one grid step on the low side only — disclosed: at
α = 1/5 everything clears. (b) **Memoryless attrition is a choice** — T3 prices the
direction exactly: any nondegenerate mixture makes the single-q deep toll an
OVERSTATEMENT bound, and increasing measured hazard falsifies the class outright —
the boundary is signed, not hand-waved. (c) **Quantization** — 250-word screens and
page-granular sampling are declared conventions; the knife-edge exclusion rule bars
the EPISODE F = 1 margin-0 cell from decision clauses, and every headline clause
carries ≥ 2 units of margin (EPISODE/PB15/PB12 front-loaded at story = 0 vs need
2–3). (d) **The hook model** (convert iff k\* story units read in-window) is
declared; partial credit is a named follow-up — note T1 and S\* are hook-model-free
within budget. (e) **An arithmetic slip in the drafter's hand facts** — the sim
re-derives everything; theorems are gates AND carry the theorem-failure NULL axis,
so a wrong hand claim becomes a finalized corrected law, not a silent bad gate.

**5. What does it unlock?** The round-14 venture slot (books half) served with the
slot's first within-artifact composition head; three standalone keepers (the
exponential toll law; the S\* = 9F + 10k\* − 9 viability lever — each front page
costs nine pages of minimum viable length; the log-convexity direction bound that
signs every single-q calibration in this family); a paste-ready assembly rule +
publishability gate for the committed catalog (dormouse's 12-spread body is under
the 10%-window cliff under ANY assembly — a format decision nobody has surfaced);
and the window-side complement to the served pricing verdicts — the free-first-
episode funnel's first click lands in a 4-screen sample that front-loaded assembly
zeroes out.

**6. What is the cheapest experiment that decides it?** The whole head IS the
cheapest deciding experiment: Arm A settles every decision number exactly in
milliseconds with no seed. The single cheapest probe if a reader doubts a specific
leg is the PB15 pencil count: 32-page book, 10% window ⇒ ⌈3.4⌉ = 4 sample pages;
title + copyright + dedication + half-title = 4 pages ⇒ the sample ends before
spread one — a two-line hand count that anchors the whole cliff machinery.

**7. What would make this a mistake to run?** If the exact arithmetic were
unavailable (it is not — the model is closed-form), if the head duplicated a prior
(it does not — the corpus grep is clean; P062/P066/P046/P038/P054 are argued
distinct by decision object and fixtures), or if the disclosed REJECT made the run
theater. It does not: the value is the independent hermetic re-derivation of the
three theorems PLUS the census no doc states — the exact 3-of-4 cliff table at the
committed formats, the one-page margin of the committed 15-spread pin, the 8000/6859
toll — and both non-REJECT rulings are genuinely reachable (α = 1/5 clears every
format; q = 49/50 kills the toll clause one grid step from the decision cell).

**8. How will we know it worked?** A committed sim-lab report with: the exact
conversion/toll/cliff/S\* surfaces over the full grid (Fractions + float
renderings), the T1/T2/T3 theorem verifications, the G5 hand worlds, the G6
battery, the twin-arm byte-equality note (two process runs identical), Arm R's
seeded reader traces beside the exact values (reporting-only), and the verdict
token against the pre-registered bands. A clean run reproduces the drafter's
disclosed values (toll 8000/6859; C(NOV, F=1) = 130321/160000; S\* = 29/38 pages,
30/39/57 screens; the 3-of-4 cliff census with PB12 cliffed at F = 2) from scratch,
or — the more interesting outcome — DISAGREES and pins the drafter's error, which
the pre-registered rule then rules on honestly (the theorem-failure NULL axis
exists for exactly that).

**Recommendation: sim-ready**
