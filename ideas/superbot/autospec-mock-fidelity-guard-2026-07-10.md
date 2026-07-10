# Idea — signature-faithful mocks / autospec guard for service+DB facades — link index

> **State:** captured
> **Class:** process · **Target:** `menno420/superbot`

**Canonical idea (stays in superbot — indexed by link, never copied):**
[`menno420/superbot → docs/ideas/autospec-mock-fidelity-guard-2026-06-16.md`](https://github.com/menno420/superbot/blob/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/autospec-mock-fidelity-guard-2026-06-16.md)
— harvested 2026-07-10 by the backlog-harvest slice, pinned @ superbot `fd638e3`
([raw](https://raw.githubusercontent.com/menno420/superbot/fd638e3c0693687a62093aa6bd75954e238fa58d/docs/ideas/autospec-mock-fidelity-guard-2026-06-16.md)).

Require signature-faithful mocks (autospec) for service and DB facades: a production crash shipped green because the only test mocked the DB facade with a bare AsyncMock that accepted a keyword the real function doesn't have.
