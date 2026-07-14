# Session — EAP close-out walkthrough: the seat-level walkthrough doc (both repos), terminal-claim prune, outbox CLOSE-OUT report

> **Status:** `in-progress`
> **Model/time:** fable · 2026-07-14T12:37:21Z (Ideas Lab worker slice — land
> the seat's EAP close-out walkthrough under inbox ORDER 012 item (b) /
> ORDER 013 STEP 2. Card born in-progress as the designed gate hold; flips
> complete in this PR's final commit)

**📊 Model:** fable-family · content-only slice (walkthrough doc, docs index
row, terminal-claim deletion, outbox CLOSE-OUT append, this card; no
scripts/, no control/status.md or control/inbox.md writes; nothing in
sim-lab)

## Scope

Land `docs/eap-closeout-walkthrough-2026-07-14.md` — the seat-level EAP
close-out walkthrough covering BOTH repos (idea-engine + sim-lab), sections
A–E exactly per inbox ORDER 012 (b) / ORDER 013 STEP 2: A. what this seat
did (PR-cited, audit-linked) · B. current state + exact verify commands ·
C. OWNER ACTIONS checklist (deep link first, bolded recommendation, VERIFY
step each) · D. 5-minute tour · E. handoff. Same PR: (i) delete the
now-terminal claim `control/claims/claude-proposal-063-menu-width-leverage-
inversion.md` (its PR #419 merged at 6d6735f — claims/ ends the EAP empty);
(ii) append a CLOSE-OUT REPORT block to `control/outbox.md` (target:
fleet-manager) carrying the ≤40-line close-out summary with the OWNER
ACTIONS checklist verbatim (ORDER 012's "outbox/heartbeat as venue" —
the heartbeat is coordinator-only, so the outbox is the venue).

## Constraints honored

- control/status.md and control/inbox.md untouched (coordinator/manager-only;
  the proposed next heartbeat stamp is WRITTEN OUT in the walkthrough §E for
  the coordinator to apply, never applied from here).
- control/outbox-archive-2026-07-14.md untouched (rolled archive, terminal).
- sim-lab untouched entirely (its own walkthrough lands via a parallel
  sim-lab PR); all sim-lab facts cited from today's verified ledger and
  re-checked read-only via GitHub MCP where restated.
- Outbox append-only (appended via shell, never loaded into an editor); no
  renumbering; all timestamps from real `date -u`.
- Claim deletion is the terminal-claim prune class (PRs #414/#415 precedent):
  the P063 claim's PR #419 merged at 6d6735f, so the claim is terminal.
- No new seeds allocated (doc-only slice; fleet seed high-water stays
  20261562, sim-lab V076 registration).
