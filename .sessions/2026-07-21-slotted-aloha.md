# PROPOSAL 237 — slotted-ALOHA finite-n throughput ceiling: a fleet of n agents contending for one shared slotted resource tops out at S_max(n) = (1 − 1/n)^(n−1) = (n−1)^(n−1)/n^(n−1), maximised at p* = 1/n, decreasing monotonically to 1/e ≈ 0.367879 — refuting the naive "one expected transmission per slot implies throughput 1"

> **Status:** in-progress

> **📊 Model:** Claude Opus · high · idea/planning
started: 2026-07-21T00:55:32Z

💓 Heartbeat:
- round/slot: fleet · coordination/contention — random-access throughput ceiling (closed-form)
- lane: P237 → V250 (+13 offset)
- branch: claude/proposal-237-slotted-aloha
- verifier: ideas/fleet/verify_237_slotted_aloha.py (stdlib only: json, hashlib, math, random, fractions)
- SEED: 20260717 · results_sha256: fb72d76e05c3e41d3f671f7d324a76dde84ea815a6360be1652508db4fc0cb9a
- determinism: in-process double-run IDENTICAL · separate re-invocation byte-identical
- G1 EXACT optimality identity via fractions.Fraction — for n ∈ {2,3,4,5,8,10,16,32,64,100} the closed form (n−1)^(n−1)/n^(n−1) equals n·p*·(1−p*)^(n−1) at p*=1/n with zero error (rational equality), and p* dominates the 199-point rational grid k/200 — exact argmax, no floats · pass
- G2 MC agreement — 200000 slots per n ∈ {2,3,5,10,25,100}, n independent Bernoulli(1/n) transmitters each; empirical success rate vs S_max(n), all |z|<3, max |z|=2.2817 · pass
- G3 invariance — relabeling agents by a nontrivial seeded permutation leaves the success count byte-identical (bijection-invariant); exact ceiling verified strictly monotone-decreasing across all n and strictly above 1/e · pass
- G4 falsifiability — the pre-registered naive rule "throughput = offered load = 1.0" rejected by the same MC data at min |z|=445.44 (per-n |z| 445–585, far above 6) · pass
- all_pass: true · first_failing_gate: null · decision: PASS

✅ Flip note (born-red → complete): this card committed FIRST with Status: in-progress to hold the PR red behind the substrate-gate; it flips to complete as the deliberate LAST commit, after the idea doc, the verifier, the outbox PROPOSAL 237 block, the full-64 digest match, and all four gates landed. The flip clears the born-red HOLD and releases native squash auto-merge.

## What this proposal does
Adds a fleet PROPOSAL establishing the exact finite-n throughput ceiling for a set of n uncoordinated agents contending for one shared slotted resource — a channel, a lock, a token. In each slot every agent transmits independently with probability p; a slot succeeds iff exactly one agent transmits. The single-slot success throughput S(n,p)=n·p·(1−p)^(n−1) is maximised at p*=1/n, giving the exact rational ceiling S_max(n)=(1−1/n)^(n−1)=(n−1)^(n−1)/n^(n−1), strictly decreasing in n and converging from above to 1/e ≈ 0.367879 (about 36.8%). Ships a stdlib-only firsthand verifier. Fills a confirmed gap: the slotted-ALOHA single-slot success ceiling and p*=1/n are grep-0 across both repos (the finite-n binomial form / "slotted aloha" / "p*=1/n" are untaken).

## Method
Exact optimisation over `fractions.Fraction`. S(n,p)=n·p·(1−p)^(n−1) is the exact binomial probability of exactly one success among n independent Bernoulli(p) trials; its unique interior maximiser is p*=1/n (derivative n(1−p)^(n−2)(1−np)=0), and S_max(n)=(n−1)^(n−1)/n^(n−1) is an exact rational. G1 checks the closed form equals the binomial at p*=1/n with zero error and that p* dominates a 199-point rational grid k/200 (exact argmax). A Monte-Carlo agreement gate simulates n independent Bernoulli(1/n) transmitters per slot and counts "exactly one". An invariance gate relabels the agents by a seeded permutation (success count byte-identical) and verifies the exact ceiling is strictly monotone-decreasing and strictly above 1/e. A falsifiability gate rejects the naive "throughput = offered load = 1.0" rule on the same sample.

## ⟲ Previous-session review
PROPOSAL 236 (necklace / Burnside cyclic-group orbit count, → V249) landed with the born-red + four-gate + full-64-digest choreography; this slice reuses that contract exactly and extends the shipped set into random-access contention throughput, an atom distinct from the shipped combinatorics/probability heads (necklace/Burnside P236, secretary/optimal-stopping P233, airport-Shapley P231, derangement-routing P229, Little's law P213, coupon collector P050, consistent-hashing max-gap P217).

## 💡 Session idea
Next untaken random-access / queueing-contention atoms surfaced in dedup: (a) the continuous unslotted-ALOHA ceiling S=G·e^(−2G) → 1/(2e) ≈ 0.184 (half the slotted ceiling) with its own optimum at G=1/2; (b) the expected number of slots to first success under stabilised backoff (geometric with success prob S_max); (c) the p-persistent CSMA throughput refinement. All grep-checked today.
