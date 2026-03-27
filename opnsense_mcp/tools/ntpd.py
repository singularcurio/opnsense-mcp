from __future__ import annotations

from typing import Any

from opnsense_mcp.context import get_client
from opnsense_mcp.errors import handle_opnsense_errors
from opnsense_mcp.tools.registry import get_module_registrar
mcp = get_module_registrar(__name__)


@mcp.tool()
@handle_opnsense_errors
def ntpd_gps() -> dict[str, Any]:
    """Get NTPd GPS source information."""
    return get_client().ntpd.gps()


@mcp.tool()
@handle_opnsense_errors
def ntpd_meta() -> dict[str, Any]:
    """Get NTPd server metadata (peers, status)."""
    return get_client().ntpd.meta()


@mcp.tool()
@handle_opnsense_errors
def ntpd_status() -> dict[str, Any]:
    """Get NTPd service status."""
    return get_client().ntpd.status()
