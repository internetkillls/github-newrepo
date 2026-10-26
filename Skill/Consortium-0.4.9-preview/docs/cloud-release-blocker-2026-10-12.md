> Historical issue affecting ONLY plugin ID `plugins_6ac4c3fb114881919f3f0a9c9ddf5706` (v0.2.0). Do not infer that the later separately owned v0.2.3 ID is affected.

# Cloud release blocker (2026-10-12)

Target plugin ID: `plugins_6ac4c3fb114881919f3f0a9c9ddf5706` (USER / PRIVATE).
Last observed cloud release: `pluginrel_6ac4cc035f748191ad876c8e48e024b5`, semantic version `0.2.0`.
Cloud releases returned only `0.1.0` and `0.2.0`; duplicate cloud *release numbers* were not confirmed.

Four guarded `update_plugin` attempts to publish the `0.3.0` local candidate failed **before action invocation** with HTTP 400 `Plugin archive must contain exactly one plugin, not a marketplace`. They tested: full package with compatibility manifest, single manifest packaged under one root folder, flat single-manifest ZIP, and a minimal manifest/skill overlay. `get_plugin_files` on the existing cloud plugin also failed with HTTP 409 and the same archive-classification text. `get_plugin_metadata` remained `0.2.0` following attempts.

No cloud update took place. Do **not** create another plugin as a workaround, delete old release IDs, or claim a fix. Backend inspection of current release package parser is the remaining blocker; the URI-backed archive retrieval exposes a download URL but was not inspected locally. Verify current archive packaging against a single-plugin schema or obtain Plugin Creator backend support. After repair, publish through `update_plugin` with a new `expected_release_id` and verify metadata/source readback. Keep original audience and ID.
