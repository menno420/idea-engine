# Session 2026-07-20 — PROPOSAL 225 balls-into-bins expected collision count E = m(m-1)/(2n) (round-54 FLEET slot)

> **Status:** `in-progress`
>
> Born-red HOLD: this card lands born-red (`in-progress`) on the FIRST commit to hold the PR red until the slice is genuinely done. It flips to `complete` as the deliberate LAST commit — after the idea doc + outbox block land, `python3 bootstrap.py check --strict` goes green in both repos, and the sim-lab verifier reproduces the byte-identical results-dict sha256 with all four gates passing. LEFT RED this session: the coordinator drives the flip + landing after CI.

## 💡 Session idea
Balls-into-bins expected collision count. Throw m balls independently and uniformly into n bins (equivalently: hash m keys into n buckets, or draw m values from a discrete-uniform space of size n). Count a COLLISION for every unordered PAIR of balls that share a bin — X = Σ_bins C(B_k, 2). Then the expected number of colliding pairs is EXACTLY

    E[X] = C(m,2)/n = m(m-1)/(2n)   (fraction-exact)

by linearity of expectation over the C(m,2) pairs — each fixed pair lands in the same bin with probability exactly 1/n, and linearity needs no independence between pairs. The count is quadratic in m: it is the m(m-1)/2 PAIRS that grow, not the m balls, which is why hash-table / shard / nonce collisions arrive far sooner than a per-ball 1/n intuition predicts (the birthday-attack mechanism). The plausible-but-WRONG engineering shortcut E ≈ m²/(2n) (as if a ball could collide with itself) overstates the exact answer by exactly m/(2n) and is REJECTED. Verifier computes E three independent exact ways (a literal Σ Fraction(1,n) over all C(m,2) pairs, a per-bin linearity route, and the closed form), all agreeing; Monte-Carlo (200000 trials) agrees within |z|<3; a robustness sweep over four more (n,m) configs all agree plus an exact-scaling Fraction identity; and the m²/(2n) shortcut is rejected at z=−20.57 (plus the ordered-pair m(m-1)/n impostor at z=−1259.9). Disclosed results-dict sha256 = `874a5b611f327149714d07b841bb4285481bbb223086823a5980b5ae6a31a57a`.

## ⟲ Previous-session review
Round-53 closed FLEET P221 (reservoir sampling → V234), VENTURE P222 (revenue equivalence → V235), GAME P223 (grim-trigger folk-theorem → V236); P224 (Cayley's formula) rides in a sibling session. The rotation is fleet → venture → game → unrelated; this opens round-54 in the FLEET slot as P225 (P225 → V238, +13). DEDUP (tree-wide `rg -i 'balls.into.bins|collision|birthday|occupancy|coupon'` across all lanes, bootstrap.py/.substrate excluded): the coupon-collector n·H_n cover-time identity is already built (P052, `coupon-collector-tail-2026-07-14.md`) and the birthday-problem √N FIRST-collision waiting-time law is already built (`birthday-collision-sqrt-n-2026-07-18.md`) — but NEITHER prices the expected COLLISION-COUNT E = m(m-1)/(2n) (colliding PAIRS by linearity). The birthday doc's object is the √N waiting time to the FIRST repeat; coupon-collector's object is the n·H_n time to cover ALL bins. This head's object — the exact expected number of colliding pairs — is un-built. High-water advance P223 → P225 (union-max; P224 held by a sibling).

## 🫀 Heartbeat
Left to the coordinator per the single-writer rule (control/status.md is coordinator-owned; not touched here). Claim bundled into commit 1: control/claims/2026-07-20-p225-balls-in-bins.md.

> 📊 Model: Claude Opus · high · idea/planning

## Decisions made
- Head: balls-into-bins expected collision count E[colliding pairs] = C(m,2)/n = m(m-1)/(2n), chosen because coupon-collector (n·H_n) is already built (P052) — this is the free fallback, distinct from both P052 and the birthday √N first-collision doc, exactly true, reproducible stdlib-only, and hash/shard-collision flavored.
- 4 pre-registered gates: G1 EXACT identity — E built THREE independent exact ways (literal Σ Fraction(1,n) over all C(m,2) pairs, per-bin linearity n·C(m,2)/n², closed form m(m-1)/(2n)) all equal across configs (365,23)/(256,64)/(1000,100); G2 Monte-Carlo agreement |z|<3 (z=−0.745/−0.988/−1.510, 200000 trials); G3 robustness — sweep over (365,30)/(128,40)/(500,50)/(64,16) all |z|<3 PLUS an exact-scaling Fraction identity E(2m)/E(m) n-independent; G4 falsifiability — the naive m²/(2n) shortcut rejected at z=−20.57 (overstatement exactly m/(2n)=1/8) plus the ordered-pair m(m-1)/n impostor rejected at z=−1259.9.

## Next session should know
P225 → VERDICT 238 (+13 offset). sim-lab verifier staged on the same branch `claude/p225-balls-in-bins`: `sims/verdict-238-balls-into-bins-collisions/balls-into-bins-collision-count.py` (+ run-stdout.txt + probe-report.md). Grounding pins Wikipedia "Birthday problem" oldid 1357361405 (raw-wikitext sha1 d876b4f46b64278277ad0cf4b4bdf2ea0f271be1, 3-way match); caveat scoped — the revision literally states the C(m,2) pair count (23×22/2 = 253) and the Poisson mean C(23,2)/365 = 253/365 ≈ 0.6932 for the number of coincidences and uses linearity of indicator variables, but does NOT state the general exact closed form E = m(m-1)/(2n) as a labeled expected-collision-count formula — that general identity is DERIVED here from the on-page ingredients. This card is LEFT RED (in-progress); the coordinator drives the flip + landing after CI.
