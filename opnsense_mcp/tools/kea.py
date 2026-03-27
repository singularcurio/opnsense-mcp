from __future__ import annotations

import json
from typing import Any

from opnsense_py.models.base import SearchRequest

from opnsense_mcp.context import get_client
from opnsense_mcp.errors import handle_opnsense_errors
from opnsense_mcp.tools.registry import get_module_registrar
mcp = get_module_registrar(__name__)

# ---- DHCPv4 subnets ----------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def kea_search_v4_subnets(search_phrase: str = "") -> dict[str, Any]:
    """Search Kea DHCPv4 subnets."""
    result = get_client().kea.search_v4_subnets(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": [r.model_dump(exclude_none=True) for r in result.rows]}


@mcp.tool()
@handle_opnsense_errors
def kea_get_v4_subnet(uuid: str) -> dict[str, Any]:
    """Get a Kea DHCPv4 subnet by UUID."""
    return get_client().kea.get_v4_subnet(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def kea_add_v4_subnet(data_json: str) -> dict[str, Any]:
    """Create a Kea DHCPv4 subnet. data_json: JSON with subnet fields.
    Call kea_reconfigure after."""
    from opnsense_py.models.kea import KeaSubnet4
    subnet = KeaSubnet4.model_validate(json.loads(data_json))
    return get_client().kea.add_v4_subnet(subnet).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def kea_del_v4_subnet(uuid: str) -> dict[str, Any]:
    """Delete a Kea DHCPv4 subnet by UUID. Call kea_reconfigure after."""
    return get_client().kea.del_v4_subnet(uuid).model_dump(exclude_none=True)


# ---- DHCPv4 reservations -----------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def kea_search_v4_reservations(search_phrase: str = "") -> dict[str, Any]:
    """Search Kea DHCPv4 host reservations."""
    result = get_client().kea.search_v4_reservations(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": [r.model_dump(exclude_none=True) for r in result.rows]}


@mcp.tool()
@handle_opnsense_errors
def kea_add_v4_reservation(data_json: str) -> dict[str, Any]:
    """Create a Kea DHCPv4 host reservation. data_json: JSON with reservation fields
    (hw-address, ip-address, hostname, subnet_id). Call kea_reconfigure after."""
    from opnsense_py.models.kea import KeaReservation4
    res = KeaReservation4.model_validate(json.loads(data_json))
    return get_client().kea.add_v4_reservation(res).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def kea_del_v4_reservation(uuid: str) -> dict[str, Any]:
    """Delete a Kea DHCPv4 reservation by UUID. Call kea_reconfigure after."""
    return get_client().kea.del_v4_reservation(uuid).model_dump(exclude_none=True)


# ---- DHCPv6 subnets ----------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def kea_search_v6_subnets(search_phrase: str = "") -> dict[str, Any]:
    """Search Kea DHCPv6 subnets."""
    result = get_client().kea.search_v6_subnets(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": result.rows}


@mcp.tool()
@handle_opnsense_errors
def kea_add_v6_subnet(data_json: str) -> dict[str, Any]:
    """Create a Kea DHCPv6 subnet. data_json: JSON with subnet fields.
    Call kea_reconfigure after."""
    return get_client().kea.add_v6_subnet(json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def kea_del_v6_subnet(uuid: str) -> dict[str, Any]:
    """Delete a Kea DHCPv6 subnet by UUID. Call kea_reconfigure after."""
    return get_client().kea.del_v6_subnet(uuid).model_dump(exclude_none=True)


# ---- Leases ------------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def kea_search_leases() -> dict[str, Any]:
    """List all current Kea DHCP leases (requires OPNsense with the kea/leases API)."""
    from opnsense_py.exceptions import OPNsenseNotFoundError
    try:
        return get_client().kea.search_leases()
    except OPNsenseNotFoundError:
        raise ValueError(
            "kea/leases/search endpoint not found (HTTP 404). "
            "This endpoint is not available on this OPNsense version. "
            "Use kea_search_v4_reservations to list static reservations instead."
        )


# ---- Service -----------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def kea_start() -> dict[str, Any]:
    """Start the Kea DHCP service."""
    return get_client().kea.start().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def kea_stop() -> dict[str, Any]:
    """Stop the Kea DHCP service."""
    return get_client().kea.stop().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def kea_restart() -> dict[str, Any]:
    """Restart the Kea DHCP service."""
    return get_client().kea.restart().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def kea_reconfigure() -> dict[str, Any]:
    """Apply pending Kea DHCP configuration changes. Call after any mutation."""
    return get_client().kea.reconfigure().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def kea_status() -> dict[str, Any]:
    """Get Kea DHCP service status."""
    return get_client().kea.status()
