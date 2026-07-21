# PROPOSAL 241 — Erlang-C delay probability: for an M/M/c pool of c parallel agents (Poisson arrivals λ, exp service μ, offered load a=λ/μ<c, utilization ρ=a/c) the probability an arriving task must WAIT (finds all c agents busy) is exactly the Erlang-C formula C(c,a) — C(2,1)=1/3, C(10,6)=1458/14393 — refuting both the "delay = utilization ρ=1/2" foil and the "delay = Erlang-B blocking = 1/5" foil

> **Status:** complete

> **📊 Model:** Claude Opus · high · idea/planning
started: 2026-07-21T05:10:00Z

💓 Heartbeat:
- round/slot: fleet · queueing / teletraffic — the M/M/c delay (Erlang-C) probability, distinct from the M/M/c/c loss (Erlang-B) head and the asymptotic √-staffing law
- lane: P241 → V254 (+13 offset)
- branch: claude/proposal-241-erlang-c-delay
- verifier: ideas/fleet/verify_241_erlang_c_delay.py (stdlib only: json, hashlib, math, random, fractions)
- SEED: 20260717 · results_sha256: 4d382264df161dcd033abc0592afc58a84173b58aaf061449d6c7d72d832dc39
- determinism: in-process double-run IDENTICAL · --selfcheck byte-identical · separate re-invocation byte-identical
- G1 EXACT identity (direct == from_b == stationary, exact via fractions.Fraction) — over the panel {(2,1),(3,2),(5,3),(10,6),(10,17/2),(20,15)} the three independent routes to C(c,a) agree bit-for-bit; C(2,1)=1/3, C(10,6)=1458/14393; error_count=0 · pass
- G2 MC agreement (PASTA) — correct FIFO discrete-event M/M/c simulator, warm-up 10000 discarded then MC_N=200000 measured arrivals thinned every THIN=50 to keep the binomial SE honest under queue autocorrelation; (c=2,λ=1,μ=1→a=1, expect 1/3) z=−0.2355896857; (c=10,λ=6,μ=1→a=6, expect 1458/14393) z=0.8459716886; both |z|<3 [Z_ACCEPT=3.0] · pass
- G3 invariance — time-scale invariance C=f(c,a) only: (i) EXACT C for (λ,μ)∈{(1,1),(3,3),(7,7)} all a=1,c=2 are the identical Fraction 1/3 (exact_identical=True, mismatch_count=0); (ii) MC DES at (3,3) and (7,7) both agree with 1/3 at z=−0.2355896857 and z=−0.2355896857 (byte-identical to the (1,1) run — at a=1 the sample path scales by 1/λ, so event ordering and every wait decision are unchanged); both |z|<3 · pass
- G4 falsifiability — SAME (c=2,a=1) MC sample: naive "delay=ρ=1/2" REJECTED at z_naive_rho=−149.2933145858 (|z|≥6, Z_REJECT=6.0); naive "Erlang-C=Erlang-B" — exactly 1/3≠1/5=B(2,1) (exact_distinct=True) and z_naive_b=148.7935533928 REJECTED · pass
- all_pass: true · first_failing_gate: null · decision: PASS

✅ Flip note (born-red → complete): this card commits FIRST with Status: in-progress to hold the PR red behind the substrate-gate; it flips to complete as the deliberate LAST commit, after the idea doc, the verifier, the outbox PROPOSAL 241 block, the full-64 digest match, and all four gates landed. The flip clears the born-red HOLD and releases native squash auto-merge. FLIPPED: idea doc + verifier (results_sha256=4d382264df161dcd033abc0592afc58a84173b58aaf061449d6c7d72d832dc39, all four gates PASS) + outbox PROPOSAL 241 block landed in commit 1; this commit flips Status in-progress → complete to release merge-on-green.

## What this proposal does
Adds a fleet PROPOSAL establishing the exact delay probability for a pool of c parallel agents modelled as an M/M/c queue. With Poisson arrivals at rate λ, exponential service at rate μ per agent, offered load a=λ/μ Erlangs (a<c for stability) and utilization ρ=a/c, the probability that an arriving task must WAIT — it finds all c agents busy — is exactly the Erlang-C formula C(c,a)=[a^c/c!·c/(c−a)] / [Σ_{k=0}^{c−1}a^k/k! + a^c/c!·c/(c−a)]: C(2,1)=1/3, C(10,6)=1458/14393. Ships a stdlib-only firsthand verifier that computes C three exact ways (direct sum, Erlang-B bridge, birth-death stationary), runs a correct discrete-event M/M/c simulator to confirm it by PASTA, checks time-scale invariance, and falsifies the "delay=utilization ρ=1/2" and "delay=Erlang-B blocking=1/5" naive beliefs. Fills a confirmed gap: the M/M/c DELAY probability is grep-0 across both repos and is distinct from the shipped Erlang-B M/M/c/c LOSS head (verdict-154) and the asymptotic √-safety-staffing law (P169/verdict-182).

## Method
Exact closed form + a correct DES. C(c,a) via: (a) direct Erlang-C sum, tail=a^c/c!·c/(c−a), S=Σ_{k=0}^{c−1}a^k/k!, C=tail/(S+tail); (b) the Erlang-B recursion B(0,a)=1, B(k,a)=a·B(k−1,a)/(k+a·B(k−1,a)) with the loss→delay bridge C=B/(1−ρ(1−B)); (c) the M/M/c birth-death stationary distribution (weights a^n/n! for n≤c, geometric tail a^c/c!·1/(1−ρ)), P(wait)=P(n≥c). All in fractions.Fraction, a passed as a Fraction, a<c required. G1 asserts the three routes agree exactly across the panel. G2 runs a FIFO discrete-event M/M/c simulator (departure-time heap for the c servers, a FIFO wait queue; interarrivals ~Exp(λ), services ~Exp(μ) assigned at service start), recording by PASTA whether each arrival finds ≥c in system, thinned every 50th post-warmup arrival so the binomial SE is honest, for (c=2,a=1) and (c=10,a=6). G3 checks C depends only on (c,a=λ/μ), exactly and via the DES at rescaled (λ,μ). G4 rejects delay=ρ=1/2 (z≈−149) and shows 1/3≠1/5=B(2,1) on the same sample.

## ⟲ Previous-session review
PROPOSAL 240 (Catalan numbers count non-crossing handshakes: a uniformly random perfect matching of 2n circle points is non-crossing with probability exactly C_n/(2n−1)!!, → V253) landed with the born-red + four-gate + full-64-digest choreography; this slice reuses that contract exactly and returns to the fleet queueing lane. It is distinct from the shipped queueing heads: the Erlang-B M/M/c/c LOSS head (blocking probability, calls dropped, no queue — verdict-154) and the √-safety-staffing / Halfin–Whitt asymptotic law (P169/verdict-182); this is the M/M/c DELAY probability — a queue forms, nothing is dropped, and the object is the exact finite-(c,a) probability an arriving task waits. The P240 Catalan head was enumerative combinatorics; this returns to teletraffic with a fresh, orthogonal object.

## 💡 Session idea
Next untaken queueing/teletraffic atoms surfaced in dedup: (a) the exact mean wait in queue W_q = C(c,a)/(cμ−λ) (the Erlang-C delay coupled to the wait TIME, a clean companion to this all-or-nothing wait PROBABILITY); (b) the M/M/c/K finite-buffer blocking probability interpolating Erlang-B and Erlang-C; (c) the pooling/economy-of-scale statement that C(c,a) at fixed ρ falls as c grows (the delay-side analogue of the shipped Erlang-B trunking-efficiency head). All grep-checked today.
