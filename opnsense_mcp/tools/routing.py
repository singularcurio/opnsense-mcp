from __future__ import annotations

from typing import Any

from opnsense_py.models.base import SearchRequest
from opnsense_py.models.routing import Gateway

from opnsense_mcp.context import get_client
from opnsense_mcp.errors import handle_opnsense_errors
from opnsense_mcp.tools.registry import get_module_registrar
mcp = get_module_registrar(__name__)


@mcp.tool()
@handle_opnsense_errors
def routing_search_gateways(search_phrase: str = "") -> dict[str, Any]:
    """Search gateway definitions."""
    result = get_client().routing.search_gateways(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": [r.model_dump(exclude_none=True) for r in result.rows]}


@mcp.tool()
@handle_opnsense_errors
def routing_get_gateway(uuid: str) -> dict[str, Any]:
    """Get a gateway definition by UUID."""
    return get_client().routing.get_gateway(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def routing_add_gateway(
    name: str,
    interface: str,
    gateway: str,
    ipprotocol: str = "inet",
    disabled: str | None = None,
    descr: str | None = None,
    defaultgw: str | None = None,
    fargw: str | None = None,
    monitor_disable: str | None = None,
    monitor: str | None = None,
    force_down: str | None = None,
    priority: int | None = None,
    weight: int | None = None,
) -> dict[str, Any]:
    """Create a gateway definition. Call routing_reconfigure after."""
    gw = Gateway(
        name=name, interface=interface, gateway=gateway, ipprotocol=ipprotocol,
        disabled=disabled, descr=descr, defaultgw=defaultgw, fargw=fargw,
        monitor_disable=monitor_disable, monitor=monitor, force_down=force_down,
        priority=priority, weight=weight,
    )
    return get_client().routing.add_gateway(gw).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def routing_set_gateway(
    uuid: str,
    name: str | None = None,
    interface: str | None = None,
    gateway: str | None = None,
    ipprotocol: str | None = None,
    disabled: str | None = None,
    descr: str | None = None,
    defaultgw: str | None = None,
    priority: int | None = None,
    weight: int | None = None,
) -> dict[str, Any]:
    """Update a gateway definition. Call routing_reconfigure after."""
    gw = Gateway(
        name=name, interface=interface, gateway=gateway, ipprotocol=ipprotocol,
        disabled=disabled, descr=descr, defaultgw=defaultgw, priority=priority, weight=weight,
    )
    return get_client().routing.set_gateway(uuid, gw).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def routing_del_gateway(uuid: str) -> dict[str, Any]:
    """Delete a gateway definition by UUID. Call routing_reconfigure after."""
    return get_client().routing.del_gateway(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def routing_toggle_gateway(uuid: str, enabled: bool | None = None) -> dict[str, Any]:
    """Toggle a gateway enabled state. Call routing_reconfigure after."""
    return get_client().routing.toggle_gateway(uuid, enabled).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def routing_reconfigure() -> dict[str, Any]:
    """Apply pending gateway configuration changes. Call after any mutation."""
    return get_client().routing.reconfigure().model_dump(exclude_none=True)
