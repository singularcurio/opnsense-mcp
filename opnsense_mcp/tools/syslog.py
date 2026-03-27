from __future__ import annotations

from typing import Any

from opnsense_py.models.base import SearchRequest
from opnsense_py.models.syslog import SyslogDestination

from opnsense_mcp.context import get_client
from opnsense_mcp.errors import handle_opnsense_errors
from opnsense_mcp.tools.registry import get_module_registrar
mcp = get_module_registrar(__name__)


@mcp.tool()
@handle_opnsense_errors
def syslog_search_destinations(search_phrase: str = "") -> dict[str, Any]:
    """Search remote syslog destinations."""
    result = get_client().syslog.search_destinations(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": [r.model_dump(exclude_none=True) for r in result.rows]}


@mcp.tool()
@handle_opnsense_errors
def syslog_get_destination(uuid: str) -> dict[str, Any]:
    """Get a syslog destination by UUID."""
    return get_client().syslog.get_destination(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def syslog_add_destination(
    hostname: str,
    port: str = "514",
    transport: str | None = None,
    program: str | None = None,
    level: str | None = None,
    facility: str | None = None,
    certificate: str | None = None,
    rfc5424: str | None = None,
    enabled: str = "1",
    description: str | None = None,
) -> dict[str, Any]:
    """Create a remote syslog destination. Call syslog_reconfigure after."""
    dest = SyslogDestination(
        hostname=hostname, port=port, transport=transport, program=program,
        level=level, facility=facility, certificate=certificate, rfc5424=rfc5424,
        enabled=enabled, description=description,
    )
    return get_client().syslog.add_destination(dest).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def syslog_set_destination(
    uuid: str,
    hostname: str | None = None,
    port: str | None = None,
    transport: str | None = None,
    program: str | None = None,
    level: str | None = None,
    facility: str | None = None,
    certificate: str | None = None,
    rfc5424: str | None = None,
    enabled: str | None = None,
    description: str | None = None,
) -> dict[str, Any]:
    """Update a remote syslog destination. Call syslog_reconfigure after."""
    dest = SyslogDestination(
        hostname=hostname, port=port, transport=transport, program=program,
        level=level, facility=facility, certificate=certificate, rfc5424=rfc5424,
        enabled=enabled, description=description,
    )
    return get_client().syslog.set_destination(uuid, dest).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def syslog_del_destination(uuid: str) -> dict[str, Any]:
    """Delete a syslog destination by UUID. Call syslog_reconfigure after."""
    return get_client().syslog.del_destination(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def syslog_toggle_destination(uuid: str, enabled: bool | None = None) -> dict[str, Any]:
    """Toggle a syslog destination enabled state. Call syslog_reconfigure after."""
    return get_client().syslog.toggle_destination(uuid, enabled).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def syslog_stats() -> dict[str, Any]:
    """Get syslog statistics."""
    return get_client().syslog.stats()


@mcp.tool()
@handle_opnsense_errors
def syslog_start() -> dict[str, Any]:
    """Start the syslog service."""
    return get_client().syslog.start().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def syslog_stop() -> dict[str, Any]:
    """Stop the syslog service."""
    return get_client().syslog.stop().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def syslog_restart() -> dict[str, Any]:
    """Restart the syslog service."""
    return get_client().syslog.restart().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def syslog_reconfigure() -> dict[str, Any]:
    """Apply pending syslog configuration changes. Call after any mutation."""
    return get_client().syslog.reconfigure().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def syslog_status() -> dict[str, Any]:
    """Get syslog service status."""
    return get_client().syslog.status()
