# CLAUDE.md

This file provides guidance to Claude Code when working with code in this repository.

## Commands

```bash
# Install dependencies
uv sync

# Run tests
uv run pytest

# Run a single test file
uv run pytest tests/tools/test_cron.py

# Run a single test
uv run pytest tests/tools/test_cron.py::test_search_jobs_empty

# Lint
uv run ruff check .

# Type check
uv run mypy opnsense_mcp/

# Run MCP dev server (stdio, for testing with Claude Desktop)
uv run opnsense-mcp

# Run MCP SSE server (homelab persistent mode)
OPNSENSE_MCP_TRANSPORT=sse OPNSENSE_MCP_HOST=0.0.0.0 OPNSENSE_MCP_PORT=8000 uv run opnsense-mcp

# Inspect available tools interactively
mcp dev opnsense_mcp/server.py
```

## Architecture

**opnsense-mcp** is an MCP (Model Context Protocol) server that wraps the `opnsense-py` client library and exposes all OPNsense management capabilities as MCP tools.

### Layers

1. **`server.py`** — creates the single `FastMCP` instance (`mcp`) and imports all tool modules at startup to trigger `@mcp.tool()` registration. The `main()` entry point selects between stdio (default) and SSE transport via `OPNSENSE_MCP_TRANSPORT`.

2. **`context.py`** — lazy singleton `OPNsenseClient`. `get_client()` builds the client on first call and reuses the httpx connection pool. Config is resolved from env vars (`OPNSENSE_HOST`, `OPNSENSE_API_KEY`, `OPNSENSE_API_SECRET`, `OPNSENSE_VERIFY_SSL`, `OPNSENSE_HTTPS`) then from `~/.config/opnsense-py/config.toml`. `reset_client()` is used in tests.

3. **`errors.py`** — `@handle_opnsense_errors` decorator that wraps the opnsense-py exception hierarchy and converts all errors to `ValueError` with human-readable messages. Always applied inside `@mcp.tool()`.

4. **`tools/`** — one file per OPNsense subsystem. Each file imports `mcp` from `server.py` and `get_client` from `context.py`. Tools return `dict[str, Any]`. Search results are returned as `{"total": N, "rows": [...]}`.

### Transport modes

- **stdio** (default): Claude Desktop spawns the server as a subprocess. Set `OPNSENSE_MCP_TRANSPORT=stdio` or omit the env var.
- **SSE** (homelab): A persistent HTTP server. Set `OPNSENSE_MCP_TRANSPORT=sse`. Optionally set `OPNSENSE_MCP_HOST` (default `127.0.0.1`) and `OPNSENSE_MCP_PORT` (default `8000`).

### Connection configuration

Priority order (highest first):
1. Environment variables: `OPNSENSE_HOST`, `OPNSENSE_API_KEY`, `OPNSENSE_API_SECRET`, `OPNSENSE_VERIFY_SSL`, `OPNSENSE_HTTPS`
2. Config file: `~/.config/opnsense-py/config.toml` (shared with the `opn` CLI)

### Tool naming convention

`{module}_{action}`, e.g. `cron_search_jobs`, `firewall_add_alias`, `unbound_reconfigure`.

### Input strategy

- **Flat typed params**: used for modules with well-defined Pydantic models (cron, routes, routing, syslog, etc.). The LLM sees individual named fields.
- **`data_json: str`**: used for complex/nested models (WireGuard, OpenVPN, HAProxy, interfaces, etc.). Pass a JSON string; the tool deserializes it.

### Reconfigure pattern

Most mutation tools (add/set/del/toggle) stage changes but do not apply them. Always call the corresponding `*_reconfigure` tool after mutations, e.g.:

```
cron_add_job(...) → cron_reconfigure()
firewall_add_alias(...) → firewall_reconfigure()
```

### Testing approach

Tests use `respx` to mock `httpx` at the transport level (same as opnsense-py). The `mcp_client` fixture in `tests/conftest.py` monkeypatches `opnsense_mcp.context._client` with a pre-built `OPNsenseClient` pointed at `opnsense.test`. The `reset_client_singleton` autouse fixture ensures test isolation.

### Adding a new tool module

1. Create `opnsense_mcp/tools/<name>.py` with `@mcp.tool()` / `@handle_opnsense_errors` decorated functions.
2. Import the module in `server.py` to register the tools.
3. Add tests in `tests/tools/test_<name>.py`.
