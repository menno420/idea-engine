# PROPOSAL 164 — friendship paradox: your friends have more friends than you do, and the gap is exactly the degree variance-to-mean ratio (round-38 UNRELATED slot, P164 -> V177, +13)

> **Status:** `in-progress`
> 📊 Model: Claude Opus · high · proposal authoring

Born-red HOLD: this card lands first with `Status: in-progress` to hold the PR red on the substrate gate; it flips to `complete` as the final commit, after the outbox block + heartbeat, releasing the landing workflow. A red gate before that flip is the HOLD, not a defect.

## Objective
Author round-38's UNRELATED-slot PROPOSAL 164: a fresh, counterintuitive, quantifiable mechanism from network science / social-network sampling. Head: "your friends have more friends than you" (Feld 1991) is a mathematical certainty for any network with degree spread, and the gap is EXACTLY Var(k)/E[k] — the degree variance-to-mean ratio. A random person has mean degree mu; a uniformly random FRIEND (a random edge-endpoint) has mean degree nu = <k^2>/<k> = mu + Var/mu > mu whenever degrees vary, because following a friendship size-biases toward popular people. Deliver a stdlib-only deterministic verifier (SEED pinned, three >=3sigma gates including a heavier-tailed robustness gate) plus a proposal doc a VERDICT session can check independently.

## Constraints honored
- stdlib-only Python 3 verifier (`math, json, hashlib, random`; `random.paretovariate` degree draws, `random.choices` size-biased sampling); SEED=20260717 pinned; deterministic in-process + cross-invocation double-run; results dict + sha256 printed (WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY, pretty indent=2 dump).
- three ordered z-gates (z_gate=3.0): G1 friend-mean-minus-person-mean gap > 0 across R networks (rejects the equal-popularity null), G2 size-biased Monte-Carlo friend-mean matches the closed form <k^2>/<k> (|z|<3 mechanism anchor), G3 robustness under a heavier-tailed distribution (gap survives >=3sigma AND grows).
- Outbox append-only + dedupe; proposal high-water take-max P163->P164, never regress; born-red HOLD; merge-on-green landing.
- Grounding to a reachable real source verified live HTTP 200 this session; crossover/caveat disclosed. Family model names only; timestamps from `date -u`.

## GROUNDING (verified at HEAD)
- External phenomenon (reachable, verified live HTTP 200 this session): Wikipedia, "Friendship paradox" (rev 1358630351) — states "most people have fewer friends than their friends have, on average" and derives the friend-mean as mean + variance/mean via a uniformly random edge-endpoint. Origin: Scott L. Feld (1991), "Why Your Friends Have More Friends Than You Do," American Journal of Sociology 96(6):1464-1477.
- Offset + high-water lineage: `control/outbox.md` at HEAD — verify live before the outbox append; pin +13 to the P164 -> V177 lineage at append time.

## Probe questions
**1.** Is the friend-mean-minus-person-mean gap genuinely > 0 for every sampled network at >= 3 sigma (G1), rejecting the equal-popularity folk null?
**2.** Does a size-biased Monte-Carlo estimate of the friend mean match the closed form <k^2>/<k> within sampling error (G2, |z| < 3), confirming the mechanism IS length-biased sampling?
**3.** Under a heavier-tailed degree distribution does the paradox survive at >= 3 sigma AND does the gap grow (G3), as Var/mean predicts?
**4.** Crossover, not the claim: the same length-bias covers the generalized friendship paradox (co-authors more cited, "your followers have more followers"); disclosed as a crossover, not asserted as the verified claim?

## Outcome
In progress — verifier authored and dry-run green (all three gates pass, results-dict sha256 0df9954e7378ae4c896e892c4614ff2967a117b646276fdde3f21ec874b0bd4f, byte-identical double-run); proposal doc, outbox block, and heartbeat pending; card flips complete LAST.

## ⟲ Previous-session review
Round-38 GAME slot (P163 mana-screw deck-size -> V176, +13) landed clean on three >=3sigma gates with a whole-dict digest and a shifted-distribution robustness gate; that discipline — an exact same-mean/different-spread identity plus a distribution-shift robustness gate — carries forward here into the UNRELATED slot P164 (friendship-paradox gap = Var/mean, robustness under a heavier tail).

## 💡 Session idea
Generalized friendship paradox on a WEIGHTED attribute: any node quality x positively correlated with degree (citations, followers, income) is over-stated among friends by Cov(x,k)/E[k] — so "your friends are richer / more-followed than you" is the same size-bias with a covariance numerator. Named, not authored.
