# PROPOSAL 163 — mana-screw: deck size (not land ratio) dominates opening-hand consistency via hypergeometric finite-population correction

> **Status:** `in-progress`
> 📊 Model: Claude Opus · high · proposal authoring

Born-red HOLD: this card lands first with `Status: in-progress` to hold the PR red on the substrate gate; it flips to `complete` as the final commit, after the heartbeat, releasing the landing workflow. A red gate before that flip is the HOLD, not a defect.

## Objective
Author round-38's GAME-slot PROPOSAL 163: a fresh, counterintuitive, quantifiable mechanism from tabletop deck-building probability. Head: "mana-screw" consistency is governed by DECK SIZE, not land RATIO. Holding the land fraction fixed, shrinking the deck sharpens opening-hand outcomes because the finite-population (hypergeometric) correction (N−n)/(N−1) shrinks the variance of lands drawn — a 40-card deck at 40% lands is measurably more consistent than a 60-card deck at 40% lands, even though the expected land count per card is identical. Deliver a stdlib-only deterministic verifier (SEED pinned, three ≥3σ gates including a shifted-distribution robustness gate) plus a proposal doc a VERDICT session can check independently. Placeholder card — verifier and doc not yet authored this session.

## Constraints honored
- stdlib-only Python 3 verifier; SEED pinned; deterministic in-process double-run + cross-invocation double-run asserts; results dict + sha256 printed (WHOLE-DICT / NO-SELF-FIELD / STDOUT-ONLY, pretty indent=2 dump). — planned, not yet built.
- three ordered z-gates (z_gate=3.0): G1 opening-hand land-count variance strictly lower for the small deck at matched land fraction (rejects the ratio-only null), G2 measured variance ratio matches the hypergeometric finite-population correction (N−n)/(N−1) closed form, G3 robustness under a shifted (larger deck / wider land-band) distribution.
- Outbox append-only + dedupe; status high-water take-max, never regress; born-red HOLD; merge-on-green landing. — pending.
- Grounding to cite a reachable real-world source; crossover/caveat disclosed honestly. Family model names only; timestamps from `date -u`.

## GROUNDING (verified at HEAD)
- Offset + high-water lineage: `control/outbox.md` at HEAD — verify live before the outbox append; pin the +offset to the P163 → V-target lineage at append time.
- External phenomenon (reachable): hypergeometric draws model card-game opening hands; the finite-population correction (N−n)/(N−1) shrinks the variance of successes drawn as the deck N shrinks at fixed success fraction. To be re-verified live (HTTP 200) this session before the doc lands.

## Probe questions
**1. Is the opening-hand land-count variance genuinely lower for the smaller deck at a matched land fraction?** — G1 to measure, over N paired draws at fixed land fraction, that a 40-card deck yields strictly lower variance in lands drawn than a 60-card deck, with the divergence from the ratio-only null reported at z ≥ 3.
**2. Does the measured variance ratio match the hypergeometric finite-population correction (N−n)/(N−1) exactly?** — G2 to check the small-deck/large-deck variance ratio against the closed-form correction at z ≥ 3.
**3. Does the deck-size dominance survive a shifted distribution (larger decks, wider land bands)?** — G3 to re-run G1 under a shifted regime and confirm the ordering and divergence hold at z ≥ 3.
**4. Crossover, not the claim: the effect generalizes to any "hit a threshold of a card type" opening-hand question (combo pieces, colored sources). Disclosed as a crossover, not asserted as the verified claim?** — to be disclosed as a crossover; the verified claim is the deck-size variance dominance under the hypergeometric opening-hand model.

## Outcome
Placeholder — work in progress. Verifier `ideas/game-lab/mana_screw_deck_size.py` and doc not yet committed. Gates unrun, results-dict digest not yet produced, outbox block not yet appended, high-water not yet advanced. This card lands born-red to hold the gate; the Outcome fills in on the completing commit.

## ⟲ Previous-session review
Round-38 VENTURE slot (P162 option-pool shuffle → V175, +13) landed clean on three ≥3σ gates with a whole-dict digest and a shifted-distribution robustness gate; that verifier discipline — an exact invariance/insensitivity claim plus a distribution-shift robustness gate — carries forward here into the GAME slot P163 (mana-screw deck-size dominance).

## 💡 Session idea
Mulligan-depth invariance: under the London mulligan, the probability of keeping a hand with at least k lands after m mulligans depends on the deck's land fraction and the bottoming rule, but the marginal gain per extra mulligan decays geometrically — so the "one more mulligan" value is nearly constant in deck size at fixed fraction, the opposite face of the deck-size variance result. Named, not authored.
