# Queue journal — 0.4.5-preview

Each queue save now commits a flushed, hash-linked snapshot under `<case>/queue-journal/00000001.json` before updating `queue.json`. These records contain the existing queue metadata and job transition history; they do not store raw prompt text. The queue lock remains the only dispatch owner. The journal is not a second dispatcher.

The journal is authoritative for this runtime. A verified stale compatibility projection may be read at the latest committed state without rewinding DISPATCHING to PENDING. Missing queue.json can be reconstructed for reads from a valid journal. Invalid JSON in an existing projection, conflicting edits, broken hashes, unknown projection history and schema/case mismatches fail closed. Records use canonical sorted-key hashes; this detects accidental corruption, not adversarial rewriting of the whole history.

Crash boundaries:
- Before committed hard-link creation: temp files are ignored; prior projection remains valid.
- After committed hard-link creation, before queue.json projection: readers recover the committed queue revision.
- During transport: committed DISPATCHING blocks automatic dispatch after restart. Existing recovery changes it to UNCERTAIN, never PENDING.
- After response return but before recording outcome: still DISPATCHING/uncertain; transport return is not inferred.

Legacy queues bootstrap the journal on their next normal save. Do not allow older runtimes or manual scripts to edit the same case after adoption: they do not understand the authoritative journal. Keep one runtime/dispatch path per case. An unexpected newer projection or same-revision edit is a conflict requiring reconciliation, not permission to discard history.

Executed tests include real child-process termination after journal commit before projection, real dispatch process termination, no-resend assertions, legacy queue migration, missing projection, torn temporary file, corruption and projection conflicts, plus existing queue/handoff guards. These are local runtime tests with fixture transport; they do not send ChatGPT messages or kill Chrome.

Limits: append-only snapshots retain all queue metadata and have a 10,000-record read limit pending an explicit archival design. No unbounded log compaction is performed. Complete file contents are fsynced before exclusive hard-link creation; unsupported filesystems fail closed, and Windows power-loss durability and directory metadata flushing are not proven. Automatic dead-owner lock takeover, worker/session registry transactions, browser restart, autonomous completion review and diagnostic-message delivery remain separate work.

This implementation is part of the 0.4.5-preview package. Saving the account release does not establish activation in existing local processes or their workspaces.
