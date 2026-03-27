from __future__ import annotations

import os
from typing import Any

from mcp.server.fastmcp import Context

from opnsense_mcp.server import mcp
from opnsense_mcp.tools.registry import MODULE_DESCRIPTIONS, _catalog


def _is_readonly_mode() -> bool:
    return os.environ.get("OPNSENSE_MCP_READONLY", "").lower() in ("1", "true", "yes")


def _loadable(entry_readonly: bool) -> bool:
    """Return True if this entry can be loaded given the current mode."""
    return entry_readonly or not _is_readonly_mode()


def preload_modules(module_names: list[str]) -> None:
    """Register tools for the given modules with FastMCP at startup.

    Called before any session exists, so no send_tool_list_changed() is needed.
    Respects read-only mode — mutating tools are skipped when OPNSENSE_MCP_READONLY=1.
    """
    for module in module_names:
        for entry in sorted(_catalog.values(), key=lambda e: e.name):
            if entry.module == module and _loadable(entry.readonly):
                mcp.add_tool(entry.fn, name=entry.name, description=entry.description)


@mcp.tool()
def list_modules() -> dict[str, Any]:
    """List all available OPNsense modules with descriptions and tool counts.
    In read-only mode, only read-only tools are loadable — counts reflect that.
    Call this first, then describe_module(), then load_module() or load_tool()."""
    readonly_mode = _is_readonly_mode()
    counts: dict[str, int] = {}
    readonly_counts: dict[str, int] = {}
    for entry in _catalog.values():
        counts[entry.module] = counts.get(entry.module, 0) + 1
        if entry.readonly:
            readonly_counts[entry.module] = readonly_counts.get(entry.module, 0) + 1

    modules = [
        {
            "name": name,
            "description": MODULE_DESCRIPTIONS.get(name, ""),
            "tool_count": readonly_counts.get(name, 0) if readonly_mode else counts.get(name, 0),
            "readonly_tool_count": readonly_counts.get(name, 0),
        }
        for name in sorted(set(counts) | set(MODULE_DESCRIPTIONS))
        if counts.get(name, 0) > 0
    ]
    return {"modules": modules, "readonly_mode": readonly_mode}


@mcp.tool()
def describe_module(module: str) -> dict[str, Any]:
    """List all tools in a module with names, descriptions, and read-only status.
    In read-only mode, mutating tools are shown but marked as unavailable.

    Args:
        module: Module name (e.g. 'cron', 'firewall'). Get names from list_modules().
    """
    readonly_mode = _is_readonly_mode()
    entries = [e for e in sorted(_catalog.values(), key=lambda e: e.name) if e.module == module]
    if not entries:
        known = sorted({e.module for e in _catalog.values()})
        raise ValueError(f"Module '{module}' not found. Known modules: {', '.join(known)}")

    tools = [
        {
            "name": e.name,
            "description": e.description.split("\n")[0],
            "readonly": e.readonly,
            "loadable": _loadable(e.readonly),
        }
        for e in entries
    ]
    return {
        "module": module,
        "description": MODULE_DESCRIPTIONS.get(module, ""),
        "readonly_mode": readonly_mode,
        "tools": tools,
    }


@mcp.tool()
async def load_tool(tool_name: str, ctx: Context[Any, Any, Any]) -> dict[str, Any]:
    """Load a single tool into the active session so it can be called.
    Mutating tools cannot be loaded when the server is in read-only mode.

    Args:
        tool_name: Exact tool name (e.g. 'cron_search_jobs'). Get names from describe_module().
    """
    entry = _catalog.get(tool_name)
    if entry is None:
        raise ValueError(
            f"Tool '{tool_name}' not found in catalog. "
            "Use list_modules() and describe_module() to find available tool names."
        )

    if not _loadable(entry.readonly):
        raise ValueError(
            f"Tool '{tool_name}' is a mutating operation and cannot be loaded "
            "while the server is in read-only mode (OPNSENSE_MCP_READONLY=1)."
        )

    already_loaded = {t.name for t in mcp._tool_manager.list_tools()}
    if tool_name in already_loaded:
        return {"status": "already_loaded", "tool": tool_name, "module": entry.module, "readonly": entry.readonly}

    mcp.add_tool(entry.fn, name=entry.name, description=entry.description)
    await ctx.request_context.session.send_tool_list_changed()
    return {"status": "loaded", "tool": tool_name, "module": entry.module, "readonly": entry.readonly}


@mcp.tool()
async def load_module(module: str, ctx: Context[Any, Any, Any]) -> dict[str, Any]:
    """Load all tools in a module into the active session at once.
    In read-only mode, only read-only tools in the module are loaded.

    Args:
        module: Module name (e.g. 'cron', 'firewall'). Get names from list_modules().
    """
    all_entries = [e for e in _catalog.values() if e.module == module]
    if not all_entries:
        known = sorted({e.module for e in _catalog.values()})
        raise ValueError(f"Module '{module}' not found. Known modules: {', '.join(known)}")

    entries = [e for e in all_entries if _loadable(e.readonly)]
    skipped_readonly = [e.name for e in all_entries if not _loadable(e.readonly)]

    already_loaded = {t.name for t in mcp._tool_manager.list_tools()}
    loaded: list[str] = []
    skipped_duplicate: list[str] = []

    for entry in sorted(entries, key=lambda e: e.name):
        if entry.name in already_loaded:
            skipped_duplicate.append(entry.name)
        else:
            mcp.add_tool(entry.fn, name=entry.name, description=entry.description)
            loaded.append(entry.name)

    if loaded:
        await ctx.request_context.session.send_tool_list_changed()

    result: dict[str, Any] = {
        "module": module,
        "loaded": loaded,
        "already_loaded": skipped_duplicate,
        "total_loaded": len(loaded),
    }
    if skipped_readonly:
        result["skipped_mutating"] = skipped_readonly
    return result
