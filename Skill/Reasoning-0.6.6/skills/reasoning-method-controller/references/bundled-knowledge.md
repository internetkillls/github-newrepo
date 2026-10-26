# Bundled Knowledge — v0.5 quarantine policy

This release inherits many binary/text assets from v0.3/v0.4 because Plugin Creator updates are overlays and cannot delete files. Their physical presence is NOT permission to load them by default.

## Runtime rule

A legacy asset may be consulted only when BOTH conditions hold:
1. the current operator/object independently requires it; and
2. `references/reference-registry-v0.5.md` or task-specific provenance establishes its role.

Otherwise legacy assets are `QUARANTINED-INHERITED`.

Availability never sets research priority. Named authors in old corpus filenames MUST NOT determine the theme, question, ontology, formalism, or literature map.

New v0.5 research intentionally distinguishes:
- `BUNDLED` inherited legitimate/user-supplied texts;
- `PUBLIC-OA` texts that may be fetched from a legal open/public source when needed;
- `PUBLIC-ACCESS` stable public records/expositions;
- `METADATA-ONLY` records.

This release does not claim that every `PUBLIC-OA` source was physically copied into the archive.
