# Python transducer: local venv, ChatGPT sandbox, and cloud MCP are different

## 1. Tested local Python runtime

From extracted `vibecode-transducer/` root:

```bash
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows PowerShell:
# .\.venv\Scripts\Activate.ps1
python -m unittest discover -s skills/vibecode-engineer/tests -v
python skills/vibecode-engineer/runtime/vibe_transducer.py --spec skills/vibecode-engineer/examples/duplicate_selection.json
```

Core analyzer and local patch tool use Python 3.11+ standard library. Input schema: `task_kind`, `goal`, optionally `expected_behavior`, `observed_behavior`, `files` (relative path → UTF-8 text), `target_file`, `events`, `trace_complete` (caller claim), `dependencies`, `measurements`, and `edits` for preview. `decision_gate` is evidence-dependent; a CLI exit code 0 is not target code PASS.

## 2. ChatGPT Python sandbox

If the ChatGPT session has a Python execution tool, it can run the script **when source files are actually available to that runtime**. This venv is separate from the plugin package and may be ephemeral, isolated, and not persisted or reachable by other chats. Installing a skill does not mount a local project or spin up a persistent process. Do not say a Python transducer is running in ChatGPT unless the tool emitted a real execution receipt.

## 3. Cloud-hosted Python MCP (requires user host + account permissions)

Install optional SDK 2.x **in the actual Python server environment**:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install 'mcp>=2,<3'
python skills/vibecode-engineer/runtime/mcp_server.py
```

The program binds `127.0.0.1:8765/mcp`, uses **official MCP SDK v2** `from mcp.server import MCPServer`, and exposes `vibecode_status` and `vibecode_transduce` as read-only tools. The latter accepts **explicit source texts**, not an arbitrary repository path; it performs no code execution or mutations. It has no generic `python_eval` or shell tool. No SDK pip installation/MCP network handshake was performed in the initial offline sandbox unless a later verification record specifically says so.

For a **private** MCP connection from an eligible ChatGPT account/workspace, configure an OpenAI Secure MCP Tunnel with an authenticated Platform organization and an explicitly authorized ChatGPT workspace. Follow current docs: https://developers.openai.com/api/docs/guides/secure-mcp-tunnels . For a public HTTPS endpoint, deploy behind a competent OAuth/authentication and ingress layer; the server itself ships **without OAuth/multi-user isolation** and MUST NOT be exposed to the public internet directly. Do not change host to `0.0.0.0` on an unprotected dev server.

In ChatGPT web, use the current Plugins → Add custom MCP server flow only if the workspace/account has that entitlement. Verify `vibecode_status` through an actual ChatGPT-origin tool call before reporting `CHATGPT_CONNECTED`. As of 2026-10-23, complete custom MCP/write support remains subject to Business/Enterprise/Edu eligibility and permissions; do not assume the user's plan can create/write custom MCP plugins. Source: https://help.openai.com/en/articles/12584461-connecting-custom-mcp-servers-in-chatgpt .

## 4. Local patch transaction (not through cloud MCP)

The optional `runtime/local_apply.py` is a **separate owner-invoked local command** requiring both `--approve` and `--enable-writes`, SHA-256 source pins, exactly one matching old span, and owner-selected allowlisted Python test argv. On non-green/zero/inconclusive receipts it rolls back unless another process has modified the edited file, in which case it reports `MANUAL_CONFLICT`. This is not a process sandbox; test code can execute arbitrary project code, so use a disposable Git checkout and do not run unknown dependencies. The bridge does not solve all TOCTOU races or support cross-run idempotent multi-user transactions.

## Product-honesty matrix

- `LOCAL_STATIC_TESTED`: evidenced only by current sandbox unittest/CLI run.
- `SDK_IMPORT_VERIFIED`: needs dependency installed and import executed.
- `MCP_HANDSHAKE_VERIFIED`: needs actual client connection and tools/list/call.
- `CHATGPT_CONNECTED`: needs ChatGPT-origin tool call in eligible account.
- `PATCH_APPLIED_TEST_RECEIPT`: owner-run tool receipt with matching file revisions.
- `TARGET_FEATURE_VERIFIED`: independent runtime/UX/integration observation.

The attached plugin ZIP does **not** confer these higher statuses automatically.
