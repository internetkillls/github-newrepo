# Technical Guide: MCP Audio Bridge

## Stdio JSON-RPC Protocol Flow
1. Client initializes stdio connection.
2. Client sends `{"method": "tools/list", "id": 1}`. Server returns registered audio tools.
3. Client invokes tool `{"method": "tools/call", "id": 2, "params": {"name": "calculate_safe_margin", "arguments": {...}}}`.
4. Server responds with structured content array.
