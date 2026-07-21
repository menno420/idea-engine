# idea-engine — Project Closeout

> **Status:** `historical`
>
> Permanent closeout record for the autonomous generate-and-verify idea loop.
> Written at the close of the run; the repositories go read-only after this
> lands. Read it as the definitive final state — verify any live claim against
> `control/outbox.md` and `control/status.md` on `main`.

This document is written for two readers who start from zero: the project
owner, and any future Claude session that opens this repository cold. It
describes what the project was, everything it produced, the exact state it
was left in, and how to pick the work back up.

---

## 1. What this project is & what it accomplished

**idea-engine** (canonical) and **sim-lab** (reproduction mirror) together ran
an **autonomous generate-and-verify loop**: a series of autonomous agent
sessions that repeatedly (1) generated a self-contained mathematical or
algorithmic *claim* — a "PROPOSAL" — each paired with a small stdlib-only
Python verifier, then (2) had an independent session *reproduce and adjudicate*
that claim — a "VERDICT" — by re-deriving the result from scratch, re-running
the verifier to a reproducible digest, and ruling `APPROVE` / `QUALIFIED` /
`REJECT`. Everything is markdown-first and records-only: no product code and no
deployment live here. The ledger is the product.

The two repositories divide the labour:

- **`menno420/idea-engine`** — the canonical record. `control/outbox.md` is the
  append-only ledger of every PROPOSAL and every VERDICT; `ideas/**` holds the
  idea documents and their verifiers; `control/status.md` is the live heartbeat.
- **`menno420/sim-lab`** — the reproduction mirror. Each landed proposal is
  independently re-run here as a "reproduction mirror" commit, an extra layer of
  confirmation that a verifier reproduces its claimed digest on a clean checkout.

**Scale of the run.** The ledger spans **PROPOSAL 001 through PROPOSAL 261**
(261 contiguous proposals) with matching **VERDICTs through V274**. Proposals map
to verdicts by a fixed **+13 offset** (proposal *n* → verdict *n+13*), so on the
order of ~260 distinct ideas were each independently reproduced and adjudicated.
`control/outbox.md` in this repo records verdicts **V092–V274**; the earlier
verdicts live in sim-lab's canonical ledger. Each verdict re-derived its claim
with an independent oracle (not the proposal's own functions), reproduced the
proposal's full 64-hex results digest firsthand, and evaluated four verification
gates — an exact check, a Monte-Carlo agreement check, an invariance check, and
a falsifiability check against a deliberately-wrong "foil."

**The most recent landed heads** (verified on `main`, newest first — cite the
merge SHA and PR for each):

| Proposal | Idea | Merge (proposal / verdict) |
|---|---|---|
| P261 / V274 | Morris approximate counting — unbiased streaming counter, N̂ = 2^C − 1 | [`9483353`](https://github.com/menno420/idea-engine/commit/9483353) ([#896](https://github.com/menno420/idea-engine/pull/896)) / [`cbd964a`](https://github.com/menno420/idea-engine/commit/cbd964a) ([#897](https://github.com/menno420/idea-engine/pull/897)) |
| P260 / V273 | Wilson's theorem — (n−1)! ≡ −1 (mod n) iff n prime | [`b40d9ae`](https://github.com/menno420/idea-engine/commit/b40d9ae) ([#894](https://github.com/menno420/idea-engine/pull/894)) / [`5bbe366`](https://github.com/menno420/idea-engine/commit/5bbe366) ([#895](https://github.com/menno420/idea-engine/pull/895)) |
| P259 / V272 | Moore's Nim (Nim_k) — P-position iff every binary column-sum ≡ 0 (mod k+1) | [`a904fdd`](https://github.com/menno420/idea-engine/commit/a904fdd) ([#892](https://github.com/menno420/idea-engine/pull/892)) / [`5bacb3a`](https://github.com/menno420/idea-engine/commit/5bacb3a) ([#893](https://github.com/menno420/idea-engine/pull/893)) |
| P258 / V271 | Prophet inequality — single threshold τ = E[max]/2 guarantees E[ALG] ≥ ½·E[max] | [`1120a19`](https://github.com/menno420/idea-engine/commit/1120a19) ([#890](https://github.com/menno420/idea-engine/pull/890)) / [`ad17eb5`](https://github.com/menno420/idea-engine/commit/ad17eb5) ([#891](https://github.com/menno420/idea-engine/pull/891)) |
| P257 / V270 | Valiant two-phase hypercube routing — randomized load balancing | [`f74988b`](https://github.com/menno420/idea-engine/commit/f74988b) ([#888](https://github.com/menno420/idea-engine/pull/888)) / [`bc87a02`](https://github.com/menno420/idea-engine/commit/bc87a02) ([#889](https://github.com/menno420/idea-engine/pull/889)) |

The full ledger of all 261 proposals and their verdicts is
[`control/outbox.md`](../control/outbox.md).

---

## 2. Current true state (verified live on `main`)

- **Canonical HEAD:** `cbd964a` (idea-engine `main`).
- **Proposal high-water:** **PROPOSAL 261** — Morris approximate counting, status
  `sim-ready`.
- **Verdict high-water:** **VERDICT 274** — `ruled APPROVE`, verifying P261.
- **The loop is caught up / at rest.** The newest proposal (P261) already carries
  its verdict (V274). There is **no un-verdicted proposal pending** on `main`.
- **PROPOSAL 262 / VERDICT 275 do not exist.** They were never written. (A
  Vickrey second-price auction idea, if you go looking for one, already shipped
  earlier in the run as **P199 → V212**, with a multi-unit VCG generalization as
  **P250** — those are done and merged, not pending.)
- **Open PRs:**
  - idea-engine: **none**.
  - sim-lab: **one** — [#344](https://github.com/menno420/sim-lab/pull/344),
    "PROPOSAL 246 reproduction mirror: Gordon growth" (non-draft). A lagging
    reproduction mirror; see Continuation.
- **Gate is green:** `python3 bootstrap.py check --strict` exits `0` on `main`.

---

## 3. Continuation (priority order, exact resume instructions)

If the run is ever revived, do the work in this order.

### #1 — Draft & verify the next idea (PROPOSAL 262 → VERDICT 275)

The loop is at rest at P261/V274, so the next pull is a **fresh proposal**, not a
pending verification. The mechanical recipe below is the one every verdict
followed; it is written against the last landed pair (P261 → V274) so you have a
concrete, reproducible template to copy.

**If a new un-verdicted proposal has since landed on `main`, verify it like this:**

1. `git fetch origin main && git reset --hard origin/main`.
2. **Stop-if-absent guard:** confirm the `## PROPOSAL <n>` block is literally
   present in `control/outbox.md` on `main` before ruling. (A sim-lab mirror
   alone is not enough — it omits grounding.)
3. **Byte-identical verifier copy:** copy the proposal's verifier, `diff` it
   against the original, require exit `0` (unmodified). For P261 the verifier is
   [`ideas/fleet/verify_261_approximate_counting.py`](../ideas/fleet/verify_261_approximate_counting.py)
   (file sha256 `fdc06e07bbce31a877e56e00ddc78cb5232142656878a7fd1b1a09b82765f71e`).
4. **Reproduce the full 64-hex results digest** firsthand (fresh run + a separate
   re-invocation must be byte-identical). For P261: `results_sha256`
   `ade24bf035bcc213d144494660998ed207ddae62b00e0a36879643b5a98239e6`
   (`SEED=20260721`, stdlib only).
5. **Evaluate the four gates**, each in its own direction, with an independent
   from-scratch oracle (never reuse the proposal's own functions): exact,
   Monte-Carlo agreement, invariance, falsifiability-against-a-foil.
6. **Grounding check:** grep the pinned Wikipedia revision *both* ways — what the
   proposal QUOTES from the page vs. what it DERIVES beyond the page. For P261 the
   pin is "Approximate counting algorithm" **oldid 1356953469**, raw-wikitext
   **sha1 `f2de0cd8da297f8e039b8d8f57128382529490a3`** (5705 bytes).
7. **Rule** `APPROVE` / `QUALIFIED` / `REJECT`, then in **one combined
   control-only commit**: append the `## VERDICT <n+13>` block to
   `control/outbox.md`, advance the verdict high-water, and refresh the prose in
   `control/status.md`. Open a PR, mark it ready-for-review, let it auto-merge on
   green (see §5).

### #2 — sim-lab open PR [#344](https://github.com/menno420/sim-lab/pull/344)

A P246 Gordon-growth reproduction mirror, non-draft, still open. Decide: land it
(it auto-merges on green) or close it. It is a lagging mirror, not a blocker.

### #3 — sim-lab `control/status.md` is stale

sim-lab's heartbeat still reads high-water P225/V237, but reproduction mirrors
have since landed through P261 on its `main`. If the mirror work continues,
re-stamp it; otherwise leave it as the historical record.

---

## 4. Owner walkthrough (plain language)

Everything of value, with a link and what it's for:

- **The canonical repository — [menno420/idea-engine](https://github.com/menno420/idea-engine).**
  The record of the whole run.
- **The idea ledger — [`control/outbox.md`](../control/outbox.md).** Append-only.
  Every idea (PROPOSAL) and every independent verification (VERDICT), in order.
  This is the heart of the project. Search it for a topic; each block cites its
  verifier file, its reproducible digest, and its grounding source.
- **The docs index — [`docs/current-state.md`](current-state.md).** The map of
  the documentation; this closeout is linked from it.
- **The live heartbeat — [`control/status.md`](../control/status.md).** The
  single most current status line.
- **The reproduction mirror — [menno420/sim-lab](https://github.com/menno420/sim-lab).**
  Independent re-runs confirming each verifier reproduces its digest on a clean
  checkout.

**How to clone and reproduce a verifier yourself** (nothing but Python 3 stdlib
is needed):

```
git clone https://github.com/menno420/idea-engine.git
cd idea-engine
python3 ideas/fleet/verify_261_approximate_counting.py
```

That runs the most recent idea's verifier and prints its results — the same
digest recorded in the ledger. Every proposal's verifier under `ideas/**` runs
the same way.

**Owner checklist** (quickest first):

1. **sim-lab PR [#344](https://github.com/menno420/sim-lab/pull/344)** — one open
   mirror PR. Land it or close it, your call; it changes nothing canonical.

That is the only open item that involves you. The loop is caught up, the ledger
is complete and green, and the canonical record needs nothing further.

---

## 5. Working this repo with a fresh session

**Boot order.** Land on origin first, then read the short boot set:

1. `git fetch origin main && git reset --hard origin/main` — a warm clone can lag
   origin by dozens of commits and read stale state.
2. [`.claude/CLAUDE.md`](../.claude/CLAUDE.md) — the working agreement.
3. [`control/status.md`](../control/status.md) — the live heartbeat (source of
   truth for current state).
4. [`docs/current-state.md`](current-state.md) — the docs index.

**Verify a change.** One command, run before every push:

```
python3 bootstrap.py check --strict
```

Exit `0` is green. This is exactly what the required CI check (`substrate-gate`)
enforces on every PR. A diff touching only `control/**` takes a fast lane through
the gate.

**How PRs land.** Native GitHub squash **auto-merge**, armed by the
`auto-merge-enabler.yml` workflow the moment a PR opens (or is marked
ready-for-review), and held red by the required `substrate-gate` check until it
goes green. Merging by hand is unnecessary here — open a PR, mark it
**ready-for-review**, keep CI green, and it merges itself on the all-green head
SHA.

**Gotchas a newcomer must know:**

- **Draft PRs do not arm auto-merge.** Open the PR, then immediately mark it
  ready-for-review, or it will sit green and unmerged.
- **The sim-lab mirror often merges before the canonical idea-engine block.**
  Always verify the actual PROPOSAL/VERDICT block is on **idea-engine** `main`
  before treating it as landed — a mirror alone is reproduction-only.
- **Born-red card convention.** A session's first commit lands a
  `.sessions/YYYY-MM-DD-<slug>.md` card marked in-progress, which holds the PR
  red until the session flips it complete at the end. That red is intended, not
  a defect.
- **The outbox is append-only**, and proposals map to verdicts by a **+13
  offset** (proposal *n* → verdict *n+13*).
- **Cross-check live GitHub before landing** — cached PR/ledger reads can lag the
  true state by tens of minutes.
