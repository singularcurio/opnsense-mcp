from __future__ import annotations

from typing import Any

from opnsense_py.models.base import SearchRequest
from opnsense_py.models.dhcrelay import DHCRelayDestination, DHCRelayRelay

from opnsense_mcp.context import get_client
from opnsense_mcp.errors import handle_opnsense_errors
from opnsense_mcp.tools.registry import get_module_registrar
mcp = get_module_registrar(__name__)

# ---- Destinations ------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def dhcrelay_search_destinations(search_phrase: str = "") -> dict[str, Any]:
    """Search DHCP relay destinations."""
    result = get_client().dhcrelay.search_destinations(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": [r.model_dump(exclude_none=True) for r in result.rows]}


@mcp.tool()
@handle_opnsense_errors
def dhcrelay_get_destination(uuid: str) -> dict[str, Any]:
    """Get a DHCP relay destination by UUID."""
    return get_client().dhcrelay.get_destination(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def dhcrelay_add_destination(data_json: str) -> dict[str, Any]:
    """Create a DHCP relay destination. data_json: JSON with destination fields.
    Call dhcrelay_reconfigure after."""
    dest = DHCRelayDestination.model_validate(__import__("json").loads(data_json))
    return get_client().dhcrelay.add_destination(dest).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def dhcrelay_del_destination(uuid: str) -> dict[str, Any]:
    """Delete a DHCP relay destination by UUID. Call dhcrelay_reconfigure after."""
    return get_client().dhcrelay.del_destination(uuid).model_dump(exclude_none=True)


# ---- Relays ------------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def dhcrelay_search_relays(search_phrase: str = "") -> dict[str, Any]:
    """Search DHCP relays."""
    result = get_client().dhcrelay.search_relays(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": [r.model_dump(exclude_none=True) for r in result.rows]}


@mcp.tool()
@handle_opnsense_errors
def dhcrelay_add_relay(data_json: str) -> dict[str, Any]:
    """Create a DHCP relay. data_json: JSON with relay fields. Call dhcrelay_reconfigure after."""
    relay = DHCRelayRelay.model_validate(__import__("json").loads(data_json))
    return get_client().dhcrelay.add_relay(relay).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def dhcrelay_del_relay(uuid: str) -> dict[str, Any]:
    """Delete a DHCP relay by UUID. Call dhcrelay_reconfigure after."""
    return get_client().dhcrelay.del_relay(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def dhcrelay_toggle_relay(uuid: str, enabled: bool | None = None) -> dict[str, Any]:
    """Toggle a DHCP relay enabled state. Call dhcrelay_reconfigure after."""
    return get_client().dhcrelay.toggle_relay(uuid, enabled).model_dump(exclude_none=True)


# ---- Service -----------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def dhcrelay_reconfigure() -> dict[str, Any]:
    """Apply pending DHCP relay configuration changes. Call after any mutation."""
    return get_client().dhcrelay.reconfigure().model_dump(exclude_none=True)
