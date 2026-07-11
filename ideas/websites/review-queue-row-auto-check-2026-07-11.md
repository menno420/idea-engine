# Review-queue row auto-check for the lane's own PRs — link index

> **State:** parked(build-direct — lane-sized advisory check on websites' own backlog, no simulator question; the append half routes to fleet-manager, the fleet-generic residue to substrate-kit — see probe report)
> **Class:** process · **Target:** `menno420/websites`
> **Grounding:** https://raw.githubusercontent.com/menno420/websites/8c19e930f6dedd8b230538789a579cf1ce337f3c/docs/ideas/backlog.md@8c19e93 · fetched 2026-07-11T01:02Z (manifest row: behind)

**Canonical idea (stays in websites — indexed by link, never copied):**
the "Review-queue row auto-check for this repo's own PRs" bullet under
[`menno420/websites → docs/ideas/backlog.md` § Captured / planned](https://github.com/menno420/websites/blob/8c19e930f6dedd8b230538789a579cf1ce337f3c/docs/ideas/backlog.md#captured--planned-pick-highest-value-buildable-first)
— harvested 2026-07-10 as bullet #8 of the lane-backlog link index
([`lane-backlog-2026-07-10.md`](lane-backlog-2026-07-10.md), PR #37, then pinned @
websites `144dfce`); this sibling entry gives the bullet its own probe home
([raw](https://raw.githubusercontent.com/menno420/websites/8c19e930f6dedd8b230538789a579cf1ce337f3c/docs/ideas/backlog.md)).

A script or advisory `quality`-job step that computes a merged PR's runtime/product
changed-line count against the fleet review-queue's BINDING 50-line rule and prints
"this PR needs a review-queue row" when it qualifies. The documented failure state
(the bullet's source, websites `.sessions/2026-07-10-order-009-reviews.md` 💡 @
`8c19e93`): the rule is binding fleet law but enforcement is memory — 116 merged
PRs / zero rows fleet-wide, and websites' own #67 (+300 runtime lines) and #72 both
qualified unflagged. Row-appending is a fleet-manager write the lane can't do
(Q-0260); KNOWING a row is owed can be mechanical.

## Probe report (v0, 2026-07-11)

> **Grounding:** https://raw.githubusercontent.com/menno420/websites/8c19e930f6dedd8b230538789a579cf1ce337f3c/docs/ideas/backlog.md@8c19e93 · fetched 2026-07-11T01:02Z (manifest row: behind)
> **Grounding:** https://raw.githubusercontent.com/menno420/fleet-manager/dd0eb7f109f8fa39e8d25be160fdeb1175389e04/docs/review-queue.md@dd0eb7f · fetched 2026-07-11T01:04Z
> **Sequence:** before the websites chain's next self-generated backlog pick — the lane ships ~2 slices/hour (slices 5–9 landed 21:40Z–23:48Z) and its 23:57Z heartbeat names OTHER next picks (`?repo=` filter; the PR #9 salvage re-check), so this head is buildable-not-built at probe time

*Timeliness verified live FIRST (the PR #25/#48 lesson — this lane already overtook
one probe by 19 minutes). websites HEAD `8c19e930f6dedd8b230538789a579cf1ce337f3c`
transport-verified via `git ls-remote refs/heads/main` at 2026-07-11T01:01Z, blobless
clone read at that pin: the bullet is STILL `captured` under § Captured / planned
(it did not flip Built or Retired in the 47/31-line backlog churn between the harvest
pin `144dfce` and HEAD — five OTHER bullets flipped; this slice's rider re-pins the
harvest); tree-wide grep at `8c19e93` finds NO review-queue check surface (`scripts/`
holds 4 files, none review-queue; `grep -ril review.queue` hits only the `/reviews`
RENDER path — `app/reviews.py`, `app/templates/reviews.html`, `tests/test_reviews.py`
— which reads the manager's ledger, it never checks the lane's own PRs; neither
`.github/workflows/quality.yml` nor `healthcheck.yml` greps for review/numstat/50).
NOT overtaken — probe proceeds. Mid-probe re-check 01:09Z: websites HEAD moved AGAIN
to `8abfe0a` (lane PR #85); the delta `8c19e93..8abfe0a` is a kit upgrade
v1.7.1 → v1.8.0 only — zero `docs/ideas/`, `scripts/`, or workflow-check changes
(clone-level diff) — so the verdict stands at `8abfe0a` too.*

**1. What is this really?**
A mechanical owed-row detector: fleet law (fleet-manager `docs/review-queue.md` @
`dd0eb7f`) binds that "every PR that adds more than 50 changed lines of
runtime/product code (excluding `docs/`, `control/`, `.sessions/`, and pure test
additions) OR that carries any self-flagged risk … MUST get a row here", appended by
the PR's own session before close — but the ledger is a fleet-manager file, no lane
can write it (Q-0260), and compliance is pure memory. This idea makes the OWED state
computable (a filtered `git diff --numstat` against a threshold) so the flag fires
mechanically; the append itself stays a routed ask. It is the enforcement-side
complement of websites' shipped `/reviews` page (ORDER 009 inc 3, its PR #75): that
page renders rows that EXIST; this check flags rows that are MISSING.

**2. What is the possibility space?**
- **Pre-merge advisory step in `quality` (sharpest):** compute the filtered line
  count on the PR diff itself — the session learns "row owed" BEFORE close, exactly
  when the rule says the row must be appended; zero new network, zero secrets.
- **Post-merge wake script:** sweep recent merged PRs at wake and list owed rows —
  catches history (the existing #67/#72 debt) but fires after the session that owed
  the row is gone.
- **Manager-side owed-row sweep (the only loop-closer):** fleet-manager scans every
  lane's merged PRs against its own rule and appends the rows itself — it is the
  ledger's ONE writer, so it alone can convert "owed" into "exists" without a relay.
- **Fleet-generic floor:** every merge-anyway lane has the identical gap; a
  kit-planted ritual paragraph or advisory `check` finding gives all adopted repos
  the flag at upgrade (the open-pr-awareness routing shape).
- **Degenerate corner (rejected):** a REQUIRED red gate on the 50-line rule — wrong,
  because the rule's second trigger (self-flagged risk) and the "runtime/product"
  boundary are judgment calls; a hard gate would either block honest merges or force
  gaming the classifier. Advisory-only is the honest strength.

**3. What is the most advanced capability reachable by the simplest implementation?**
~40 lines of shell/Python in the lane's existing `quality` workflow: `git diff
--numstat origin/main...HEAD`, drop paths matching the rule's exclusion list, sum,
compare to 50, echo "⚑ this PR owes a fleet review-queue row" (advisory, never
exit-affecting). That single step turns the safety valve that JUSTIFIES the fleet's
merge-anyway doctrine from memory into a per-PR mechanical fact — the documented
116-PRs/zero-rows failure class becomes impossible to not-know, at the exact moment
(pre-close) the law assigns the duty.

**4. What breaks it?**
- **The boundary judgment:** "runtime/product code" is not machine-defined —
  `scripts/`, templates, and config sit in the gray zone. Measured live on THIS
  repo: idea-engine PR #47 changed `scripts/check_harvest.py` by 205 lines
  (187+18, `git show da5c7f3 --numstat`) — non-docs/non-control/non-test — yet
  idea-engine "builds no products"; a naive classifier flags it, a strict-product
  one exempts it, and the ledger @ `dd0eb7f` carries zero idea-engine rows either
  way. Over-flagging spams the ledger (whose 48h-unread rows escalate to the
  manager heartbeat); under-flagging re-creates the memory hole.
- **Threshold copy-drift:** the 50 and the exclusion list live in fleet-manager's
  doc; a hand-copied constant in the lane checker is the KNOWN_KEYS/kit-line drift
  class again — rule edits upstream silently diverge from the enforcement copy.
- **Detection is not appending (measured live):** websites flagged #67/#72 to the
  manager in its heartbeat notes on 2026-07-10 (`.sessions/2026-07-10-order-009-reviews.md`
  close-out), and at fleet-manager HEAD `dd0eb7f` the ledger's 7 open rows STILL
  include no websites row — the relay path itself rots; only the manager-side
  sweep (Q2) closes the loop.
- **Diff-shape edge cases:** squash-merges, force-pushed branches, and renames skew
  `--numstat`; the risk-flag half of the rule (⚑ on card / "risky" in body) needs
  text the CI job has but a wake script must fetch.

**5. What does it unlock?**
The merge-anyway doctrine's honesty: "no PR waits for review" is only defensible
while the post-merge queue actually gets fed, and this makes the feed obligation
visible per-PR. Downstream: owed-vs-appended becomes a trend the manager can read
(the `/reviews` page already renders the ledger — an "owed but missing" count is its
natural companion once detection exists anywhere); the same filtered-numstat helper
is reusable by every lane, including this repo (whose scripts/ slices measurably
cross the naive threshold, Q4); and each flag fired is one fewer silent entry in the
fleet's largest known compliance gap (116/0).

**6. What does it depend on?**
Lane-local slice: nothing new — git history plus the existing `quality` workflow;
the rule text pinned at fleet-manager `docs/review-queue.md` @ `dd0eb7f` (cite the
SHA in the step so drift is checkable). Manager-side sweep: fleet-manager's own
tooling and its sole-writer authority over the ledger. Fleet-generic floor: the
kit-planted `control/README.md` ritual / advisory `check` seam (the same carrier
already routed for open-pr-awareness and the heartbeat-grammar self-check). A
boundary DECISION on "runtime/product" (Q4) precedes any strict variant.

**7. Which lane should build it?**
- **websites builds the lane-local advisory step** — it is the lane's own backlog
  bullet, sourced from its own lived miss (#67/#72), and its never-idle ladder will
  reach it without any ORDER; nothing to route for the build itself.
- **fleet-manager owns the loop-closing half** — an owed-row sweep + self-append
  (it is the ledger's one writer; the measured relay rot in Q4 shows flag-and-ask
  does not feed the queue). Routed via the heartbeat fan-in notes, not an outbox
  proposal (no simulator question).
- **substrate-kit owns the fleet-generic floor** — advisory owed-row finding /
  planted ritual paragraph, same one-grammar/one-source seam family as the
  kit-line and heartbeat-grammar checks (threshold + exclusions read from ONE
  pinned source, never N hand copies) — cross-linked in
  `ideas/substrate-kit/README.md` per the PR #29/#40 precedent.

**8. What is the smallest shippable slice?**
One advisory step appended to websites `.github/workflows/quality.yml` (or a
`scripts/check_review_queue_owed.py` it calls): filtered `git diff --numstat` vs
base, the ledger's exclusion list, threshold 50, a printed ⚑ line naming the rule
@ its SHA when owed — non-required, never red, no network. The step's output line
doubles as the paste-ready heartbeat-notes relay to the manager.

**Recommendation: park** — build-direct: a lane-sized mechanical slice already on
websites' own backlog with no evidence question a simulator could settle (a filtered
diff-count is proven by running it; the two real open questions — the
runtime/product boundary and who appends — are a manager judgment call and a
routing, both carried in the fan-in notes), with the loop-closing append half routed
to fleet-manager and the fleet-generic floor cross-linked to substrate-kit.
