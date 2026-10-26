# Emergency protocol and persisted budgets — 0.4.6 preview

This preview extends the private 0.4.5 release. Account publication and local activation require separate verification. Defaults preserve manual/opt-in behavior. No existing case, active process, installed cache, Chrome profile, MSIX manifest or URL registration was changed by the development checks.

## State and authority

The queue commit journal remains authoritative for queue jobs. Incident envelopes, immutable diagnostic claims, raw child output files and result envelopes preserve recovery evidence. They are application records, not OS/browser-memory snapshots. A valid hash proves consistency with captured bytes; it does not prove delivery, correct reasoning or successful task execution.

`incident -> budget -> explicit route -> one durable delivery claim -> receiver ACK -> typed proposal -> fresh checkpoint/expiry/budget checks -> bounded read-only observation or one extra output verification -> verified result`. There is no worker-send action in a recovery decision. `UNCERTAIN` worker submissions remain blocked.

`AGENT_ACKNOWLEDGED_*` is diagnostic-message evidence. `OBSERVATION_RETURNED_NOT_TASK_COMPLETION` is metadata observation. `REVIEWED_WITNESS` proves the recorded response/output gates, not task quality. A diagnostic claim or exit code alone proves none of these.

## Exact parameters

| Parameter | Value and unit | Enforcement/meaning |
|---|---|---|
| Incident elapsed budget | 300000 ms | Starts on first recovery use; persisted once; a new decision ID cannot reset it |
| Read-only observation claims | 3 per incident | Durable slots; interrupted owners consume a slot; concurrent/unknown live ownership blocks |
| Extra queue verification | 1 per job | Original three verification attempts remain recorded; extra attempt is committed before observation |
| Verification admission reserve | 45000 ms | Requires this much incident AND decision lifetime; includes up to 10s operation lock, 5s discovery, 10s CDP open, 20s review |
| Decision TTL | At most 300000 ms | Absolute UTC expiry, also checked after observation/output capture; late evidence cannot commit review |
| Diagnostic child timeout | At most 180000 ms | Reduced by remaining incident budget and route lifetime; parent-owned timer is not independent supervision |
| Diagnostic launches | 1 per incident | Claim committed before launch; unknown outcomes never resend automatically |
| Route TTL | At most 86400000 ms | Explicit receiver UUID and authorization reference; expired route cannot start a new send |
| Version/help preflight | 5000 ms per command | Version plus resume JSON/schema/output-file capabilities; does not prove session ownership |
| State/checkpoint size | 2097152 bytes | Browser JSON input; queue checkpoints come from journal excluding lock metadata |
| Incident record size | 4194304 bytes | Hashed immutable envelope limit |
| Reply size | 65536 bytes | Exact incident/checkpoint/delivery/session identity; diagnosis at most 4000 JS string code units |
| Child stdout/stderr | 2097152 bytes each | Direct files; parent monitors every 250 ms; read/reconcile rejects oversized logs |
| JSONL event count | 10000 lines | CLI ACK requires exact session, a terminal turn and final message matching reply file |
| Launcher integrity | SHA-256 of executable and optional JS entrypoint | Absolute real files pinned at setup; rechecked before launch; no shell interpolation |
| Queue/packet hashes | SHA-256 | Checkpoint is exact JSON bytes; envelope integrity uses canonical JSON; hashes have different roles |
| URL/reference rules | Existing handler contract | HTTPS host/path/scope validation and ambiguity checks unchanged; Windows activation is a separate absent adapter |

These are initial bounded safety limits, not measured production-optimal values. Wall-clock regression refuses recovery; forward jumps may exhaust the budget conservatively. PID liveness is conservative and does not establish a process incarnation after PID reuse.

Output file count/size, chunks and content hashes remain governed by the existing output contract/gate. Emergency does not relax those limits. See AUTOMATIC_REVIEW_v0.4.5.md and HANDLER_POLICY_v0.4.5.md.

## When Emergency runs

| Trigger | Current behavior |
|---|---|
| Three automatic response/output verification failures | Persist immutable queue incident; `--auto-emergency` may attempt its configured route |
| Process died after third verification counter commit | Next verification reconstructs the missing incident, without another worker send |
| Endpoint unavailable / ambiguous or missing browser binding | `rcc-recovery incident` records the packet; delivery/recovery is a separate explicit call |
| Missing/corrupt/unreadable current checkpoint | Diagnostic-only send is allowed; schema permits only `decision: null`; no observation or review |
| Current checkpoint differs | Reject old incident before delivery; reconcile current state before a new incident |
| Missing/expired route or changed launcher | No automatic alternative receiver; runner records/escalates handler failure |
| App chat has an active writer | Explicit CLI preacceptance rejection; no writer release or automatic retry |
| Unknown diagnostic outcome, parent died, reply missing | Preserve claim; reconcile durable terminal output when available; never relaunch |
| Invalid ACK, wrong identity, unsafe/expired action | No application; retain evidence. No automatic replacement message |
| Extra queue verification fails or was interrupted | Persistent one-attempt cap prevents re-verification loops; no next worker dispatch |
| Uncertain worker submission | Existing reconciliation gate remains; automatic incident-to-agent wiring for this trigger is not implemented |

## Route setup and execution

Use a fresh, exclusively owned case and a separately authorized diagnostic receiver. Never point to an arbitrary work chat or `--last`. CLI session ownership must be established independently; a UUID and idle status are insufficient.

```text
node bin/rcc-recovery configure-route --root=<workspace> --case=<case> --session=<authorized-uuid> --executable=<absolute-codex.exe> --authorization-ref=<consent-reference> --expires-at=<UTC-ISO-time> [--auto-reobserve] [--allow-non-git]
node bin/rcc-recovery delivery-status --root=<workspace> --incident=<incident-sha256>
node bin/rcc-recovery deliver --root=<workspace> --incident=<incident-sha256>
node bin/rcc-recovery recover --root=<workspace> --incident=<incident-sha256>
```

Route setup sends no model prompt. Browser-state overrides may use `--state`; queue recovery always reads the authoritative queue journal and rejects a CLI override. Status/configuration do not require a state file. `--auto-reobserve` authorizes only the typed read-only action or one queue verification; it does not delegate shell commands or worker resends. Deferred-runner use additionally requires explicit `--auto-emergency` and the existing automatic-review/output contracts.

CLI output writes directly into owned files. After controller death, reconciliation may prove diagnostic ACK from a matching final message, reply file and structured terminal event while process exit remains unproven. Decision expiry still applies. Without that evidence the status stays unknown. Parent-owned timeout/output monitoring may disappear when the parent dies; no independent supervisor or automatic orphan cleanup is installed.

## Executed live findings and release boundary

1. A real Codex CLI resume of the explicitly created diagnostic chat failed before thread persistence: `already has an active writer`. A read-only app inspection showed only the initial READY turn. The first candidate conservatively reported unknown; the new classifier reports this specific preacceptance rejection. It still cannot choose another route or resend automatically.
2. A parent-chat app-tool delivery reached the real agent. Its first JSON reply mistyped the checkpoint hash. The harness rejected it and performed zero loopback observations. This is evidence that identity checks matter even with an otherwise reasonable diagnosis.
3. A distinct second synthetic case returned an exact ACK and checkpoint-bound proposal. The harness called the real read-only recovery module against an owned loopback HTTP fixture, observed an empty target list once and replayed its cached result without another read. The result explicitly says no conversation was open and does not claim Chrome/worker/task recovery.

The app-tool harness is executed by the authorized parent chat. It is not a shipped autonomous Node-to-app adapter. A CLI-only receiver has not been tested with a real agent. Production ChatGPT worker recovery, independent restart supervision, local activation and Windows URL activation remain unverified or absent. The next minimal integration must deliver through the owning host without creating a second writer and preserve request/turn/ACK identity across interruptions.
