# idea-engine · outbox

> **Sole writer: this Project. Append-only.** Proposals from the idea pipeline, in the kit
> ORDER grammar (see README.md § The outbox). Consumers: **sim-lab** direct-pulls
> `status: sim-ready` entries on its wakes (Q-0264.6); the **fleet manager** reads
> everything at its :30 sweeps and owns all post-verdict routing. Entries are never
> edited after append — a superseded proposal gets a new entry that names the old one.
