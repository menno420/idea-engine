# PROPOSAL 202 — Condorcet jury theorem for committees: a below-average committee gets steadily WORSE as you add members (round-48 VENTURE slot, P202 → V215, +13; pivoted from the shipped secretary-problem head)

> **Status:** complete
> 📊 Model: Claude Opus · high · idea/planning

**Born-red HOLD (cleared).** This card landed `in-progress` on the FIRST commit to hold the proposal PR red on the born-red convention; it flips to `complete` here on the deliberate LAST commit, after the verifier reproduces byte-identical (results-dict sha256 e37537a46ae122d030e858f1f21015b2f528ab84d567a5b13227cf1905eaf1df across an in-process double-run and separate cross-invocations) and the G1/G2/G3 battery passes green (all_pass=true, first_failing_gate=null). Merge-on-green is the only merge path — this session issues zero merge calls.

## 💡 Session idea
The assigned head — the secretary problem / 37% optimal-stopping rule — is ALREADY SHIPPED (ideas/fleet/secretary-rule-cardinal-regret-2026-07-13.md, PROPOSAL 036 → sim-lab VERDICT 047), so this slice pivoted to the first fallback: the Condorcet jury theorem for committees. The counterintuitive head is the DARK SIDE. A majority vote of n independent members each correct with probability p is right with probability M(n,p)=Σ_{k>n/2}C(n,k)p^k(1−p)^{n−k}; for p>1/2 this rises monotonically to 1 as the committee grows, but for p<1/2 it FALLS monotonically to 0 — a 101-member committee of 40%-competent members is right only ≈2% of the time, worse than a single such member, and the optimal jury of below-average members is one voter. Committee SIZE amplifies whichever side of the coin-flip line the individual competence sits on; only at p=1/2 is M=1/2 for every size. The governance lever: vet member competence past 1/2 BEFORE enlarging the panel, never after. Distinct in mechanism from the shipped condorcet-jury-correlation-floor head (→V142), which models a latent-Gaussian error-correlation ceiling A_∞=Φ(Φ⁻¹(p)/√ρ) for p>1/2 members and never touches the p<1/2 dark side; this head is the exact independent binomial-tail theorem, Fraction-exact, no Gaussian.

## ⟲ Previous-session review
P201 (Graham's multiprocessing timing anomaly — greedy list scheduling is non-monotone; adding a machine can increase the makespan, yet greedy ≤ (2−1/m)·OPT; round-48 FLEET opener, lane fleet) landed via claim + born-red proposal PR and is queued P201 → V214 (+13) on the outbox ledger; its verifier reproduced byte-identical (results_sha256 2f81534216b6d8dee3d99446a0e451bde7cd64019d5f10b7de59a01921129eef) with G1 remove-edge z=77.58, G2 add-machine z=8.49 & shorten z=9.22, G3 (2−1/m) bound 0 violations over 20000 exact instances. The round-48 rotation (fleet→venture→game→unrelated) advances to the VENTURE slot; this session opens P202 → V215 (+13). Claim (control fast-lane) bundles into the born-red proposal commit.

## Objective
Author + land PROPOSAL 202 → VERDICT 215 (+13): the Condorcet jury theorem for committees (majority accuracy climbs to 1 for above-half competence but collapses to 0 for below-half — the optimal below-average jury is a single voter), with a stdlib deterministic verifier (SEED=20260717) carrying a ≥3σ statistical-agreement gate, an exactly-true 2^n-enumeration + sign-of-(p−1/2) monotonicity gate, and a distribution-free-shift robustness gate.

## Constraints honored
- stdlib-only verifier (hashlib, json, math, random, fractions); SEED=20260717; byte-identical across in-process double-run + separate invocation.
- PR opens READY; merge-on-green only (zero agent merge calls); born-red HOLD via this card.
- No model version identifiers; timestamps from `date -u`; external grounding pinned live (Wikipedia "Condorcet's jury theorem" raw-wikitext rev sha1, byte-exact to a local recompute).
- DEDUP: assigned head (secretary/37%) shipped → pivoted to first fallback (Condorcet). Second fallback (Simpson's paradox) also hard-collided. Pivot disclosed in the doc, the claim, and here.

## Pinned world (committed constants, SEED=20260717)
Homogeneous binary competence p as exact Fractions: P_above=3/5 (0.60, above the coin-flip line), P_below=2/5 (0.40, below it), P_half=1/2 (knife edge). Closed form M(n,p)=Σ_{k=(n+1)/2}^{n}C(n,k)p^k(1−p)^{n−k} as exact Fraction; enumeration leg re-derives M by summing p^c(1−p)^{n−c} over ALL 2^n vote patterns with c>n/2. Z_GATE=3.0; Monte-Carlo T=200000; N_mc=101 (odd); N_enum={1,3,5,7,9}. Fresh `random.Random(20260717)` at the top of every full run. Digest posture: WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY.

## Gate-plan (pre-registered — frozen, z_gate = 3.0)
- **G1 statistical agreement (≥3σ band):** at N_mc=101 the Monte-Carlo majority-correct rate matches the exact closed form M(101,p) within 3 standard errors, for BOTH p=0.60 and p=0.40. Direction: |empirical − closed_form| ≤ 3·stderr (small z is PASS).
- **G2 exactly-true enumeration + monotonicity:** exhaustive 2^n enumeration EQUALS the closed-form Fraction for every n∈{1,3,5,7,9} and every case (exact Fraction equality), AND the sign-of-(p−1/2) monotonicity holds — p=3/5 strictly increasing toward 1, p=2/5 strictly decreasing toward 0, p=1/2 flat at 1/2.
- **G3 robustness / distribution-free shift:** (a) EXACT — a monotone (exp) transform of the same uniform draw with a matched threshold gives BIT-IDENTICAL votes to a Bernoulli pass over the same stream (rate diff = 0); (b) STATISTICAL — an independent heavy-tailed (Cauchy) latent stream calibrated to the same competence p yields a majority rate within 3σ of the closed form.
- all_pass = G1 ∧ G2 ∧ G3.

## GROUNDING (verified live)
Wikipedia "Condorcet's jury theorem" (oldid 1364571286) fetched live this session (action=raw), 12161-byte raw wikitext; MediaWiki revision sha1 1e6130332a53f4c8b92aa3872a25019b5f871ded is byte-identical to a locally recomputed sha1 of those bytes (self-certifying pin). The article carries all three head claims verbatim: the p>1/2 monotone-to-1 result, the binomial-sum closed form, and the dark side — "if p is less than 1/2 … adding more voters makes things worse: the optimal jury consists of a single voter."

## Probe questions
**1. Is the head crisp and falsifiable?** Yes — a single closed form M(n,p) with an exact 2^n enumeration witness and a byte-pinned verifier; falsified if enumeration ≠ closed form for any (n,p), or the sign-of-(p−1/2) monotonicity fails, or the MC rate leaves the 3σ band.
**2. Is it counterintuitive-but-true?** Yes — "more heads are better than one" is exactly wrong below the coin-flip line: a 101-member 40%-competent committee is right only ≈2% of the time (worse than one member) and worsens with size; the optimal below-average jury is one voter.
**3. Is the model clean and fully pinned?** Yes — homogeneous binary competence as exact Fractions (3/5, 2/5, 1/2), odd sizes, SEED committed, T/N pinned, nothing tunable post-hoc.
**4. Is there an exactly-true gate?** Yes — G2: the 2^n enumeration equals the binomial-tail closed form as exact Fractions for every (n,p), plus the exact-equality leg of G3 (bit-identical votes under a monotone value transform), no sampling.
**5. Is it deterministic and reproducible?** Yes — fresh random.Random(20260717) per run, in-process double-run asserted canonical-identical before hashing, whole-dict sha256 e37537a4…eaf1df byte-identical across two invocations.
**6. Is the grounding real and external?** Yes — Wikipedia "Condorcet's jury theorem" oldid 1364571286 pinned by rev sha1 (byte-exact to a local recompute), carrying the monotone-to-1 result, the binomial-sum form, and the p<1/2 dark side verbatim.
**7. Could it collide with a shipped proposal?** It pivoted BECAUSE of a collision (secretary problem, P036→V047, shipped). Its nearest live neighbour condorcet-jury-correlation-floor (→V142) is a DIFFERENT mechanism (latent-Gaussian correlation ceiling, p>1/2 only); this is the exact independent binomial-tail theorem with the p<1/2 dark side. No verifier overlap; disclosed in the doc.
**8. What would make sim-lab reject it?** A non-reproducible digest, the enumeration disagreeing with the closed form under reimplementation, the monotonicity direction failing, or the grounding not resolving.
