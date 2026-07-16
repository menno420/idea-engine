# The blanket that halves at the border: the catalog-wide impulse-price rejection is exactly right standalone (the bar is twice the price ratio), the royalty function halves exactly at $2.99, and the catalog's own committed series geometry collapses the bar to a mere doubling

> **State:** sim-ready
> **Class:** venture (pipeline rotation — the standing ORDER 003 VENTURE slot, round 16, BOOKS half; harvest source: the vetting packets' own catalog-wide price-band boilerplate — the "No $0.99 impulse price" blanket stamped on 26 packets, its "at any plausible volume ratio" justification, and the complete 3-book series the same catalog commits — priced against the KDP royalty structure the plan itself pins as a verified hard fact)
> **Target:** sim-lab (verification target menno420/sim-lab per the Q-0264 pipeline; routing is the manager's per Q-0260, this repo never edits any other repo)
> **Grounding:** https://github.com/menno420/venture-lab@021cba9422ff838128c3af2c23e4212824173471 · fetched 2026-07-15T23:28:11Z
> (FIRSTHAND: every committed sentence, price, census count, and word count below is read from venture-lab's committed files at that pin and cited file:line; the V049 royalty pin rides as an external-anchor gate from sim-lab @ d212882219c5b9e26d0b13b0457f525b1c5b34e5 · fetched 2026-07-15T23:32:05Z; every MODEL constant — the read-through r, the KU borrow share β, the per-borrow income J, the delivery fee δ — is invented-but-pinned in this file, and the DECISION arms are seedless exact rationals with zero repo/network reads at verdict time — the P017–P077 hermetic precedent)
> **Origin:** standing ORDER 003 (continuous new ideas per repo) under ORDER 004 rule 3 (deliberate lane rotation, "fleet backlogs → venture's book/product space → game mechanics → COMPLETELY UNRELATED domains"); round 16 opened at fleet backlogs with P077 (#442, merged 2026-07-15T23:14:34Z), so the venture slot is next — this head. Half evidence: the slot's own committed alternation (P018 books → P022/P026 trading → P030 books → P034 trading → P038 books → P042 products → P046 books → P050 products → P054 books → P058 products → P062 books → P066 products → P070 books → P074 products) puts round 16 on the BOOKS half.

**Harvest-tap disclosure (slot history):** the books half has tapped the publishing plan's §3/§4 conventions (P038, P054), the KDP keyword map (P046), the derived owner queue (P062), and the committed manuscripts themselves (P070). This head is the half's FIRST tap of the **vetting-packet boilerplate as the decision object**: the catalog-wide price-band checkbox that every packet inherits, the two packets that justify it with an exact-sounding sentence, and the sellable guide that teaches it as transferable procedure. No prior head prices a break-even volume ratio, the 70/35 tier border, or series read-through as a demand channel.

## The committed claims (harvested @ 021cba9)

1. **The royalty structure is a committed verified hard fact.** `docs/publishing/PUBLISHING-PLAN.md` §1 @ 021cba9: "KDP pays **70% only on ebooks priced $2.99–$9.99** (inclusive) … below $2.99 or above $9.99 pays **35%**, and a per-MB delivery fee is deducted from the 70% tier. So a $0.99 YA price earns 35%, not 70% — flag this trade-off when pricing." The trade-off is flagged; no committed sentence ever computes it.
2. **The blanket is stamped catalog-wide.** The line "No $0.99 impulse price recommended (drops to 35%)" (and its NL/`[x]`-checked variants) appears in **26 vetting packets** (measured by script: the exact file list is in the fixture — every adult EN packet, every NL edition packet including all three Night Kiln volumes, weduwenblauw, ultramarine, the-weigh-house, …). It is a checkbox default, not a per-title derivation.
3. **Two packets justify it with a quantified-sounding sentence.** `docs/publishing/vetting/the-twelfth-cake.md:106–107`: "No $0.99 impulse price recommended (drops to 35%) — even in a seasonal spike, **70% of $3.99 beats 35% of $0.99 at any plausible volume ratio**." Inherited verbatim by `de-driekoningentaart.md:106–108` ("holds unchanged in EUR"). The phrase "volume ratio" names the decision variable; "any plausible" is never given a number.
4. **The catalog SELLS the blanket as procedure.** `candidates/ai-novella-production-kit/guide/06-pricing-and-listing.md:9–16` @ 021cba9 teaches: "the explicit rejection of $0.99 impulse pricing because dropping to the 35% tier means 70%-of-$3.99 beats 35%-of-$0.99 at any plausible volume ratio. Whatever your genre's numbers are, the *procedure* transfers" — a paying customer inherits the blanket with the catalog's own authority behind it.
5. **The same catalog commits a complete 3-book series carrying the blanket.** `candidates/adult-novels/the-night-kiln/en/` @ 021cba9 holds `the-night-kiln.md`, `the-morning-door.md`, `the-harvest-rows.md` — measured **16,180 / 16,192 / 23,610 words** (`len(split())`, the `wc -w` rule); `de-morgendeur.md:95–97` pins "**Book Two of a three-book series** — … EN Books 1–3 are complete on `main`. The strongest series home in the catalog"; the series price is committed series-matched at **$4.99 / €4.99** (`the-night-kiln.md:84,145`; `de-morgendeur.md:237`); and the series' own packets carry the blanket checkbox (claim 2's list includes de-nachtoven, de-morgendeur, de-oogstslag).
6. **Exactly one packet concedes the fork — and defers it.** `docs/publishing/vetting/the-marmalade-post.md:93–95`: "No $0.99 impulse price recommended (drops to 35%); **if a later series has 3+ books, a book-1 promo price becomes a real ⚑ owner decision — flagged for then, not now.**" The same packet commits the series comp that makes "then" concrete: "the proven series model is Agatha Frost's Peridale Cafe — 'Peridale Cafe Cozy Mystery (**36 book series**) …'" (§3) and "cozy … earns via KU page-reads and **series read-through**, not single sales" (§3). A 3-book series is already complete on `main` (claim 5) — "then" is now, committed in the same tree.
7. **The external royalty pin already sits in the pipeline.** sim-lab `sims/verdict-049-ku-exclusivity/REPORT.md` @ d212882 pins "roy(0.99) = **693/2000** = $0.3465" — imported HERE as an external-anchor gate, never re-derived by hand.

## The mechanism (reasoned to its fuller form — Q-0254 duty)

The blanket sentence compares two PER-SALE royalties and declares the volume ratio that would equalize them implausible — without ever computing it. The comparison lives on a piecewise royalty function and, for series books, inside a funnel. Three exact structures carry the head, none stated anywhere in the committed docs:

- **T1 — the border halves, exactly.** roy(p) = (7/10)p − δ on [299/100, 999/100], (7/20)p outside (δ = per-MB delivery fee, 70% tier only — claim 1 verbatim). At the $2.99 border the function is discontinuous with jump ratio EXACTLY 2 (= (7/10)/(7/20), price-independent), and the attainable per-sale royalty set over the committed [0.99, 9.99] domain is [693/2000, 2093/2000) ∪ [2093/1000, 6993/1000] — a **forbidden band whose width (2093/2000) exactly equals its own lower edge** (two registered margin-0 contacts). No committed price can earn between $1.0465 and $2.093 per sale; every committed row sits on the upper branch.
- **T2 — the standalone bar law.** For a standalone title the break-even volume ratio is m\* = roy(p)/roy(p₀) = **(70/35) · (p/p₀) — exactly twice the price ratio**, the factor 2 being the tier ratio itself. At the committed pairs: ($3.99, $0.99) → **266/33 ≈ 8.0606**; ($4.99, $0.99) → **998/99 ≈ 10.0808**; (band floor $2.99, $0.99) → **598/99 ≈ 6.0404**. The sentence's home ground is REAL: an eightfold volume response is a fair reading of "implausible". Signed fee lemma: δ > 0 hits the 70% side only (claim 1), so the true bar is strictly BELOW 2·p/p₀ (δ ∈ {1/100, 1/10, 1/2} → 8.0317 / 7.7720 / 6.6176 at $3.99) — the law is an upper bound in a known direction.
- **T3 — the series funnel collapses the bar.** For book 1 of a K-book series with per-boundary read-through r (buyers of book k+1 = r × buyers of book k; downstream books stay at the committed series-matched price under BOTH arms — the promo moves book 1 only, the Marmalade fork's own object), the per-buyer income is I(p₁) = roy(p₁) + Σ_{k=2..K} r^(k−1)·roy(p), and the bar becomes **m\*(K, r) = I(full)/I(promo)** — strictly decreasing in K and in r, with the exact K→∞ closed form m\*_∞(r) = roy(p)/((1−r)·roy(p₀) + r·roy(p)). At the catalog's own committed anchors (series price $4.99; K = 3 the complete Night Kiln; K = 36 the committed Peridale comp): m\*(3, 1/2) = 3493/1695 ≈ 2.0608, **m\*(3, 3/4) = 18463/11271 ≈ 1.6381**, **m\*(36, 3/4) ≈ 1.2907**, m\*(36, 9/10) ≈ 1.1015; the K→∞ curve crosses m\* = 2 at exactly **r\* = 400/899 ≈ 0.4449**. The bar the blanket calls implausible at K = 1 (10.08 at this price) falls to a mere doubling inside the catalog's own committed geometry — and the packets stamp the same checkbox on both worlds.
- **T5 — KU dampens the lever, monotonically.** Under the committed KU posture (claim 6's genre "earns via KU page-reads"; enrollment per-title per V049), a borrow pays page-read income independent of list price, so with borrow share β the bar m\*(K, r, β) is strictly decreasing in β toward 1 — the promo lever's leverage shrinks but its DIRECTION never flips; named cell (K=3, r=1/2, β=1/2, J=roy) = 5489/3691 ≈ 1.4871. V049's roy pin anchors the arithmetic (claim 7).

The decision object is the **blanket's scope**: a catalog-wide checkbox (+ a sellable guide teaching it as genre-independent procedure) whose justifying sentence is exactly true for standalones and exactly false inside the catalog's own committed series geometry. REJECT-first: an unpriced blanket taxes every future series title at its funnel mouth, and the catalog's strongest committed series home already inherits it.

## Pinned model (committed constants @ 021cba9; model constants invented-but-pinned, exact rationals)

- **Royalty:** tiers 7/10 and 7/20; band [299/100, 999/100] inclusive; promo price p₀ = 99/100; delivery fee δ registered at 0 with the signed lemma (δ grid {1/100, 1/10, 1/2} reported); committed prices: 399/100 (Twelfth Cake / Marmalade band floor pick), 499/100 (Night Kiln series-matched, Slow Word), 299/100 (the band floor itself).
- **Series:** K ∈ {1, 3, 36} (standalone; the complete committed Night Kiln; the committed Peridale comp) · read-through r ∈ {1/10, 1/4, 1/2, **3/4**, 9/10} per boundary (geometric attrition — the packets' own "series read-through" channel; no committed measurement exists, hence the grid + the named NULL probe). Promo arm: book 1 at p₀, books 2..K unchanged. Decision cells bold: (K=3, r=3/4) and (K=36, r=3/4) at the committed $4.99.
- **KU mixture (T5):** β ∈ {0, 1/4, 1/2, 3/4} · per-borrow series income J ∈ {roy/2, roy, 2·roy} (relative grid, invented-but-pinned — KENP page counts are uncommitted; T5's decision content is the monotone lemma, not any J cell).
- **Census fixtures (measured at 021cba9, re-measured by the sim from its own pinned copies):** the 26-file blanket list · the 2-file "any plausible volume ratio" list (the-twelfth-cake, de-driekoningentaart) · the 1-file fork list (the-marmalade-post) · the guide sentence · Night Kiln word counts 16,180 / 16,192 / 23,610.
- **Arms:** Arm A seedless exact `fractions.Fraction` closed forms; Arm B independently-structured per-mass ledger walk (book-by-book mass flow — exact-equal required, 15/15 (K, r) cells × full + promo + ratio: typed must-equal contacts C1/C2/C3, plus C4 the geometric-sum identity at (r=1/2, K=36) = 34359738367/34359738368); Arm R seeded finite-cohort MC (N = 10,000), REPORTING-ONLY (seeds 20261700–702; aux 20261703 never read; no statistical gate). **Arm-R draw-order grammar (registered fixture line, the V089 lesson):** for reader i = 0..N−1 ascending, for boundary k = 2..K ascending, draw exactly ONE uniform u = rng.random(); the reader continues to book k iff u < float(r), else break; no other draws are made; one `random.Random(seed)` per trace; the aux seed is never read.
- **Margin-0 ledger (V083):** registered exact contacts — (i) tier jump ratio == 2 exactly; (ii) forbidden-band width == lower edge exactly (2093/2000 == 2093/2000); (iii) m\*(1, r) r-independence across the whole grid. DISCLOSED near-contact, **excluded from decision clauses** (the P070 knife-edge rule): m\*_∞(9/10) = 69860/63567 sits below 11/10 by exactly **91/90810** ≈ 0.001 — no clause may rest on it; the finite-K ordering m\*(36, 9/10) > m\*_∞(9/10) is a gate, the 11/10 comparison is not.

## Pre-registered decision rule (evaluation order: REJECT first)

- **REJECT** the catalog-wide blanket (scope defect, not sentence defect) iff ALL of: **(a)** the standalone home ground is real — m\*(1) ≥ 6 at every committed price pair (the sentence stands where it was born); **(b)** series collapse — m\*(3, r) ≤ 2 for at least one r in the registered grid at the committed $4.99 (a mere doubling of book-1 readers inside the catalog's own complete series); **(c)** comp-scale collapse — m\*(36, 3/4) ≤ 4/3 (at the packet's own committed comp, a 33% lift suffices).
- **INVALID** on any gate failure (below).
- **APPROVE** iff m\*(K, r) > 4 at every committed series cell (K ∈ {3, 36} × the full r grid) — the blanket survives series scope with margin (mutually exclusive with REJECT via clause (b)).
- **NULL** otherwise, on named axes: the **r axis** (no committed read-through measurement exists — the cheapest live probe is the KDP series dashboard's read-through report on the FIRST published pair, zero spend, zero new tooling); the **β/KU axis**; the **δ fee axis**; the **EUR basis** (the NL packets price €3.99/€4.99 and assert "70% band respected" — the EUR band constants are inherited, not re-verified). Every NULL is a finalized, citable finding with its exact tables, never a re-run request.

## Gates (run INVALID on any failure)

- **G1 twin arms:** Arm B (per-mass ledger walk) equals Arm A (closed forms) on every rational at all 15 (K, r) cells — full-price income, promo income, AND their ratio (typed must-equal contacts C1/C2/C3); C4 geometric-sum identity exact.
- **G2 (T1):** jump ratio == 2 exactly; forbidden-band width == lower edge exactly; attainable-set edges == {693/2000, 2093/2000, 2093/1000, 6993/1000}; roy(0.99) == 693/2000 (the V049 external anchor); every committed price in the upper branch.
- **G3 (T2):** m\*(1) == 2·p/p₀ at every committed price (266/33, 998/99, 598/99); the δ lemma strictly lowers the bar at every grid δ.
- **G4 (T3):** m\* strictly decreasing in K and in r across the grid; m\*(1, r) r-free; the K→∞ closed form verified against the ladder (m\*(36, 9/10) > m\*_∞(9/10)); m\*_∞(r\*) == 2 exactly at r\* = 400/899.
- **G5 hand worlds (derived by hand in this file):** p = $4.00 standalone: bar = (7/10·4)/(693/2000) = **800/99** (= 2·4/0.99 — the law, by hand); K = 2, r = 1/2, p = $4.00: I = 2.8 + 1.4 = 4.2, I′ = 0.3465 + 1.4 = 1.7465, m\* = **8400/3493 ≈ 2.4048**.
- **G6 battery:** β-monotonicity strict at every J with β = 0 recovering the sales-only bar; census recount from the fixture's pinned file copies reproduces 26/2/1; Arm R previews within 2% of the exact cohort mean (reporting sanity, no gate on decisions); census anchors (§ Expected landing) reproduced verbatim.

## Expected landing (DISCLOSED per the P048–P077 exact-arm norm)

All 50 drafting checks PASSED live (exit 0, ~0.4 s; twin-arm mismatches: 0). At the registered clauses: **REJECT** — (a) standalone bars 266/33 / 998/99 / 598/99, all ≥ 6 ✓; (b) witness cells m\*(3, 3/4) = 18463/11271 ≈ 1.6381 and m\*(3, 9/10) = 135229/90279 ≈ 1.4979 both ≤ 2 (m\*(3, 1/2) = 3493/1695 ≈ 2.0608 sits ONE grid step above the line — disclosed); (c) m\*(36, 3/4) ≈ 1.2907 ≤ 4/3 ✓ (margin ≈ 0.043, modest, disclosed; the 9/10 cell ≈ 1.1015 is far under). Full m\*(3, r) row: 55389/10439 ≈ 5.3060 · 10479/3287 ≈ 3.1880 · 3493/1695 ≈ 2.0608 · 18463/11271 ≈ 1.6381 · 135229/90279 ≈ 1.4979. Falsifiability is live on both sides: at r ≤ 1/4 every K = 3 cell clears 3 (slow read-through rescues the blanket — clause (b) dies two grid steps left of the witness), and the APPROVE world is real (any committed catalog whose series geometry stays under r\*_∞ = 400/899 at K → ∞ keeps every bar above 2). KU dampening named cell 5489/3691 ≈ 1.4871; the T5 lemma held strict at every J. Arm R previews: seeds 20261700 / 701 / 702 → 80607.96 / 80618.44 / 81041.09 against exact cohort mean 80775.625 (N = 10,000, K = 3, r = 3/4, full-price arm).

## Consequence (pre-registered; routing the manager's per Q-0260 — this repo edits no other repo, nothing here builds/publishes/spends)

- **REJECT →** paste-ready structured choice to the manager for venture-lab's price-band boilerplate, recommendation first per Q-0263.2: **(a, recommended) SCOPE-NARROW the blanket** — the checklist/template line becomes "No $0.99 impulse price for STANDALONE titles (the bar is exactly twice the price ratio ≈ 6–10×); for series book 1 the promo is a per-series ⚑ owner decision read off the committed m\*(K, r) table" — the Marmalade fork sentence (claim 6) is ALREADY the repair text, promoted from one packet to the shared boilerplate; the sellable guide's chapter 6 gains the same one-sentence scope qualifier (a product-correctness fix: paying customers currently inherit the unscoped blanket as "the procedure transfers"); (b) keep the blanket but register the trigger — any series reaching 3 complete books (Night Kiln already qualifies) auto-queues the promo decision row with the m\* table attached; (c) status quo + the named r probe first (the KDP series read-through report on the first published pair — zero spend). No option re-prices any title: the served pricing verdicts (V037/V039/V040/V041 family, V049) set price POINTS and the enrollment fork; this head prices the boilerplate's SCOPE.
- **APPROVE →** the blanket stands catalog-wide, priced; note filed.
- **NULL →** the named r observation (free, arrives with the first published series pair) or the EUR/β/δ re-cut, tables attached.

## Dedup

Nearest priors, argued distinct: **P038 → V049** (books half) priced KU ENROLLMENT vs going wide at a FIXED price per cell — the price never moved inside an arm; its roy(0.99) = 693/2000 pin is imported here as an external-anchor gate (G2), its b\* crossover table composes downstream (T5's β is its borrow channel seen from the pricing side), and no V049 cell computes a break-even volume ratio, a tier-border discontinuity, or a funnel. **P070 → V083** (books half) is the same geometric-attrition FAMILY on a different axis: there survival runs WITHIN one artifact's sample window and the decision is assembly/composition; here attrition runs ACROSS series volumes and the decision is a price-scope rule — zero shared fixtures, zero shared constants. **P074 → V087** (products half, same lane) priced the bundle's PWYW floor lattice — same catalog, different committed sentence, different mechanism (coherence windows vs break-even collapse); its external-anchor-import pattern (V040 numerals as gates) is reused here on V049. **P062 → V073** used geometric survival as a γ-discount in a SCHEDULING objective. **P046** prices the discovery shelf; **P054 → V065** an illustration dollar gate; **P018/P030 → V020/V032** production allocation. The ORDER 005/006 pricing SIM-REQUEST verdicts set per-artifact price points — none touches the 70/35 border structure or a volume-ratio bar. Corpus grep at HEAD `8aa71ba` + sim-lab `d212882`: zero hits for "volume ratio" / "break-even" / "impulse price" / tier-border mechanics in any proposal P001–P077 or verdict V001–V089 (the only royalty-tier hits are V049's own pins, argued above). This is the pipeline's first pricing-scope head and its first tap of the vetting boilerplate as an object.

## Model basis (declared model-dependence — the P024 discipline)

Geometric per-boundary read-through is the pinned funnel model (the packets' own "series read-through" language names the channel; no committed measurement pins r — hence the grid, the exact r\* crossing, and the named zero-spend NULL probe); the promo's demand response m is the SENTENCE'S OWN variable ("volume ratio") — the head prices the bar m\*, never asserts a demand curve; downstream prices held fixed and read-through held promo-independent are declared conventions (a promo that ALSO degrades read-through raises the bar — direction signed, named follow-up); the KU mixture prices only the monotone dampening direction (J is relative-pinned); EUR inheritance and the delivery fee are named NULL axes with signed lemmas. Everything the decision reads is an exact rational.

## Probe report (v0, 2026-07-15)

> Single-pass battery (panel not escalated: self-contained knowledge probe, sim is
> report-only evidence, no spend/publish/irreversible surface — README § probe battery).
> Verify-first ran FIRST, live this slice: (a) **dedup** — the corpus sweep
> `rg -i 'volume ratio|break.even|impulse|promo|royalt|tier'` (bootstrap.py/.substrate
> excluded) at HEAD `8aa71ba` and over the sim-lab clone @ `d212882` returned only
> V049's own royalty pins (imported as anchors, argued in Dedup) and P070's unrelated
> "read-through rt" royalty constant; the distinct-mechanism neighbors
> (V049 enrollment fork, V083 within-artifact attrition, V087 floor lattice,
> V073 γ-discount scheduling) are argued in Dedup. (b) **kill test NOT triggered** —
> no prior proposal P001–P077, idea file, or session-card 💡 prices the blanket's
> scope, the tier border, or a break-even volume ratio; no recorded drop of this
> head exists. (c) **feasibility + arithmetic checked LIVE** — both arms (closed
> forms + per-mass ledger twin) ran at drafting in ~0.4 s stdlib and agreed on every
> rational (15/15 cells, mismatches 0); every committed sentence re-read this session
> at venture-lab origin/main `021cba9` (fetched 2026-07-15T23:28:11Z): the 26-packet
> blanket census, the two "any plausible volume ratio" packets, the guide's
> "the *procedure* transfers", the Marmalade fork + Peridale-36 comp, the Night Kiln
> 3-book completeness (word counts 16,180/16,192/23,610), the plan §1 royalty hard
> fact; expected landing DISCLOSED (REJECT) with its exact drafting values rather
> than hidden, all rulings reachable, the r ≤ 1/4 and r\*_∞ = 400/899 APPROVE-side
> witnesses named, INVALID controls gated. Seeds 20261700–703 swept collision-free
> at HEAD `8aa71ba` (registered prior 20261690–693 P077/V090; 20261694–699 the
> disclosed gap; the lone in-tree "20261700" is the P077 card's next-free-block
> ledger line — a mention, not a seed; 20261833 re-confirmed DATA-not-seed per the
> recorded discrimination rule).

**1. What is this really?** A pre-registered EXACT MEASUREMENT of a committed
catalog-wide pricing rule — the "No $0.99 impulse price … at any plausible volume
ratio" blanket, stamped on 26 vetting packets and sold as procedure in the
AI-novella-production kit — against the exact break-even structure it never
computed, taken at the catalog's own committed constants (the plan's verified
70/35 tiers, the committed $3.99/$4.99 price picks, the complete 3-book Night Kiln
series, the committed 36-book Peridale comp). On exact `fractions.Fraction`
arithmetic the bar law (twice the price ratio), the border halving, the forbidden
royalty band, and the full m\*(K, r) collapse table are exact at every cell, judged
against bands fixed before any code (REJECT first: home-ground bars ≥ 6 AND a
series cell ≤ 2 AND the comp cell ≤ 4/3; APPROVE: every series cell > 4; NULL
otherwise with named axes), byte-identical across two runs, seeded traces demoted
to reporting-only.

**2. What is the possibility space?** (i) Don't run it — the round-16 venture slot
goes unserved and every future series title (and every kit customer) inherits an
unscoped blanket at its funnel mouth. (ii) A prose note "consider series promos" —
retells the direction, measures nothing, misses all three keepers (the bar-law
identity, the exact border halving, the collapse geometry with its r\* crossing).
(iii) Re-price a title — reopens the served V037–V041/V049 verdicts without adding
structure; no price point moves in this head. (iv) An MC-only demand sim — invents
a demand curve the committed docs never state and leaves seed noise on decision
numbers that are exact rationals (the V065/V067 lesson); the sentence's own
variable IS the bar, so the head prices the bar and demands nothing. (v) This
head: exact census as the ruling, REJECT-first bands, INVALID on the G1–G6 gates,
twin-arm verification, falsifiability live on both sides. (vi) Over-scope (real
demand estimation, permafree/price-match mechanics, KENP page modeling,
promo-degraded read-through) — each named as a follow-up, none in scope.

**3. What is the most advanced capability reachable by the simplest
implementation?** One ~130-line stdlib file: a two-branch royalty function, one
geometric-ladder income expression, a per-mass ledger twin, and a grid loop —
yielding the exact bar law verified as a THEOREM CHECK at every committed price,
the border/forbidden-band contacts, the full m\*(K, r) collapse surface with its
exact K→∞ crossing r\* = 400/899, the signed fee and KU lemmas, and the
paste-ready per-series decision table the consequence menu ships — from a sim a
verdict session runs cold in under a second.

**4. What breaks it? (assumptions made explicit)** (a) **r is invented-but-pinned**
— no committed read-through measurement exists; the grid brackets 1/10..9/10, the
witness cells say 3/4, and the named NULL probe is the KDP series dashboard on the
first published pair (free, automatic once anything publishes). REJECT clause (b)
survives at r ∈ {3/4, 9/10} only — disclosed: at r ≤ 1/4 the blanket holds even
at K = 3, and m\*(3, 1/2) misses the 2-line by one grid step (2.0608). (b) **The
funnel model is a choice** — downstream prices fixed, read-through
promo-independent, buyers-only attrition; each named, with the
promo-degrades-read-through direction signed as bar-raising. (c) **The 4/3 and 2
plausibility lines are drafter-registered** — "plausible" is the sentence's own
undefined word; the full exact table ships regardless, so any other reading is a
row lookup, not a re-run. (d) **The knife-edge** — m\*_∞(9/10) vs 11/10 sits
91/90810 apart; excluded from decision clauses by the registered rule. (e) **An
arithmetic slip in the drafter's hand facts** — the sim re-derives everything from
the fixture; theorems are gates AND carry the theorem-failure NULL axis, so a
wrong hand claim becomes a finalized corrected law, not a silent bad gate.

**5. What does it unlock?** The round-16 venture slot (books half) served with the
half's first pricing-scope head; three standalone keepers (the bar law m\* =
tier-ratio × price-ratio — a one-line audit for ANY two-tier royalty border; the
forbidden-band structure — width equals lower edge exactly at a 2× border; the
funnel-collapse geometry with its exact r\* crossing — when a fixed per-unit
argument dies inside its own catalog's series); a paste-ready repair whose text
the catalog has ALREADY written once (the Marmalade fork sentence, promoted to
the shared boilerplate); and a product-correctness fix for a SELLABLE artifact —
the kit currently teaches the unscoped blanket to paying customers as
transferable procedure.

**6. What is the cheapest experiment that decides it?** The whole head IS the
cheapest deciding experiment: Arm A settles every decision number exactly in
milliseconds with no seed. The single cheapest probe if a reader doubts a specific
leg is the two-line hand count: 70% of $3.99 = $2.793, 35% of $0.99 = $0.3465 —
divide: 8.06, exactly 2 × (3.99/0.99); then add ONE downstream book at $4.99 with
r = 3/4 to both sides and divide again — the bar is already under 2.5.

**7. What would make this a mistake to run?** If the exact arithmetic were
unavailable (it is not — the model is closed-form), if the head duplicated a prior
(it does not — the corpus grep is clean; V049/V083/V087/V073 are argued distinct
by decision object and fixtures), or if the disclosed REJECT made the run theater.
It does not: the value is the independent hermetic re-derivation of the bar law,
the border contacts, and the collapse table no doc states — plus both non-REJECT
rulings genuinely reachable (r ≤ 1/4 rescues the blanket at K = 3; any catalog
under r\*_∞ = 400/899 keeps every bar above 2), and the NULL probe is the single
cheapest real observation in the entire books pipeline (one dashboard read).

**8. How will we know it worked?** A committed sim-lab report with: the exact
bar/border/collapse surfaces over the full grid (Fractions + float renderings),
the T1/T2/T3/T5 theorem verifications, the G5 hand worlds, the G6 battery + census
recount, the twin-arm byte-equality note (two process runs identical), Arm R's
seeded cohort traces beside the exact values (reporting-only, grammar as
registered), and the verdict token against the pre-registered bands. A clean run
reproduces the drafter's disclosed values (266/33 · 998/99 · 598/99; jump ratio 2;
band width 2093/2000; m\*(3, 3/4) = 18463/11271; r\* = 400/899; the 26/2/1
census) from scratch, or — the more interesting outcome — DISAGREES and pins the
drafter's error, which the pre-registered rule then rules on honestly (the
theorem-failure NULL axis exists for exactly that).

**Recommendation: sim-ready**
