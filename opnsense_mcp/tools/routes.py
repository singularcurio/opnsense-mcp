from __future__ import annotations

from typing import Any

from opnsense_py.models.base import SearchRequest
from opnsense_py.models.routes import Route

from opnsense_mcp.context import get_client
from opnsense_mcp.errors import handle_opnsense_errors
from opnsense_mcp.tools.registry import get_module_registrar
mcp = get_module_registrar(__name__)


@mcp.tool()
@handle_opnsense_errors
def routes_search_routes(search_phrase: str = "") -> dict[str, Any]:
    """Search static routes."""
    result = get_client().routes.search_routes(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": [r.model_dump(exclude_none=True) for r in result.rows]}


@mcp.tool()
@handle_opnsense_errors
def routes_get_route(uuid: str) -> dict[str, Any]:
    """Get a static route by UUID."""
    return get_client().routes.get_route(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def routes_add_route(
    network: str,
    gateway: str,
    descr: str | None = None,
    disabled: str | None = None,
) -> dict[str, Any]:
    """Create a static route. network: CIDR notation. Call routes_reconfigure after."""
    route = Route(network=network, gateway=gateway, descr=descr, disabled=disabled)
    return get_client().routes.add_route(route).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def routes_set_route(
    uuid: str,
    network: str | None = None,
    gateway: str | None = None,
    descr: str | None = None,
    disabled: str | None = None,
) -> dict[str, Any]:
    """Update a static route. Call routes_reconfigure after."""
    route = Route(network=network, gateway=gateway, descr=descr, disabled=disabled)
    return get_client().routes.set_route(uuid, route).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def routes_del_route(uuid: str) -> dict[str, Any]:
    """Delete a static route by UUID. Call routes_reconfigure after."""
    return get_client().routes.del_route(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def routes_toggle_route(uuid: str, disabled: bool | None = None) -> dict[str, Any]:
    """Toggle a static route. disabled=True disables the route."""
    return get_client().routes.toggle_route(uuid, disabled).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def routes_reconfigure() -> dict[str, Any]:
    """Apply pending route changes. Call after any mutation."""
    return get_client().routes.reconfigure().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def routes_gateway_status() -> dict[str, Any]:
    """Get gateway status (RTT, loss, status for all gateways)."""
    return get_client().routes.gateway_status()
