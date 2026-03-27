from __future__ import annotations

import json
from typing import Any

from opnsense_mcp.context import get_client
from opnsense_mcp.errors import handle_opnsense_errors
from opnsense_mcp.tools.registry import get_module_registrar
mcp = get_module_registrar(__name__)


@mcp.tool()
@handle_opnsense_errors
def hostdiscovery_get_settings() -> dict[str, Any]:
    """Get host discovery settings (scan interval, interface, etc.)."""
    return get_client().hostdiscovery.get()


@mcp.tool()
@handle_opnsense_errors
def hostdiscovery_set_settings(data_json: str) -> dict[str, Any]:
    """Update host discovery settings. data_json: JSON with settings fields.
    Call hostdiscovery_reconfigure after."""
    return get_client().hostdiscovery.set(json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def hostdiscovery_search() -> dict[str, Any]:
    """Search/list discovered hosts."""
    return get_client().hostdiscovery.search()


@mcp.tool()
@handle_opnsense_errors
def hostdiscovery_start() -> dict[str, Any]:
    """Start the host discovery service."""
    return get_client().hostdiscovery.start().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def hostdiscovery_stop() -> dict[str, Any]:
    """Stop the host discovery service."""
    return get_client().hostdiscovery.stop().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def hostdiscovery_restart() -> dict[str, Any]:
    """Restart the host discovery service."""
    return get_client().hostdiscovery.restart().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def hostdiscovery_reconfigure() -> dict[str, Any]:
    """Apply pending host discovery configuration changes. Call after any mutation."""
    return get_client().hostdiscovery.reconfigure().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def hostdiscovery_status() -> dict[str, Any]:
    """Get host discovery service status."""
    return get_client().hostdiscovery.status()
