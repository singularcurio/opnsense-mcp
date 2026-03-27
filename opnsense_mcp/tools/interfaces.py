from __future__ import annotations

import json
from typing import Any

from opnsense_py.models.base import SearchRequest

from opnsense_mcp.context import get_client
from opnsense_mcp.errors import handle_opnsense_errors
from opnsense_mcp.tools.registry import get_module_registrar
mcp = get_module_registrar(__name__)


# ---- Bridges -----------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def interfaces_search_bridges(search_phrase: str = "") -> dict[str, Any]:
    """Search bridge interface definitions."""
    result = get_client().interfaces.search_bridges(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": list(result.rows)}


@mcp.tool()
@handle_opnsense_errors
def interfaces_get_bridge(uuid: str) -> dict[str, Any]:
    """Get a bridge interface definition by UUID."""
    return get_client().interfaces.get_bridge(uuid)


@mcp.tool()
@handle_opnsense_errors
def interfaces_add_bridge(data_json: str) -> dict[str, Any]:
    """Create a bridge interface. data_json: JSON with bridge fields.
    Call interfaces_reconfigure_bridges after."""
    return get_client().interfaces.add_bridge(json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def interfaces_set_bridge(uuid: str, data_json: str) -> dict[str, Any]:
    """Update a bridge interface. data_json: JSON with bridge fields.
    Call interfaces_reconfigure_bridges after."""
    return get_client().interfaces.set_bridge(uuid, json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def interfaces_del_bridge(uuid: str) -> dict[str, Any]:
    """Delete a bridge interface by UUID. Call interfaces_reconfigure_bridges after."""
    return get_client().interfaces.del_bridge(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def interfaces_reconfigure_bridges() -> dict[str, Any]:
    """Apply pending bridge interface changes."""
    return get_client().interfaces.reconfigure_bridges().model_dump(exclude_none=True)


# ---- GIF ---------------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def interfaces_search_gifs(search_phrase: str = "") -> dict[str, Any]:
    """Search GIF (Generic Tunnel Interface) definitions."""
    result = get_client().interfaces.search_gifs(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": list(result.rows)}


@mcp.tool()
@handle_opnsense_errors
def interfaces_get_gif(uuid: str) -> dict[str, Any]:
    """Get a GIF interface definition by UUID."""
    return get_client().interfaces.get_gif(uuid)


@mcp.tool()
@handle_opnsense_errors
def interfaces_add_gif(data_json: str) -> dict[str, Any]:
    """Create a GIF interface. data_json: JSON with GIF fields.
    Call interfaces_reconfigure_gifs after."""
    return get_client().interfaces.add_gif(json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def interfaces_set_gif(uuid: str, data_json: str) -> dict[str, Any]:
    """Update a GIF interface. data_json: JSON with GIF fields.
    Call interfaces_reconfigure_gifs after."""
    return get_client().interfaces.set_gif(uuid, json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def interfaces_del_gif(uuid: str) -> dict[str, Any]:
    """Delete a GIF interface by UUID. Call interfaces_reconfigure_gifs after."""
    return get_client().interfaces.del_gif(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def interfaces_reconfigure_gifs() -> dict[str, Any]:
    """Apply pending GIF interface changes."""
    return get_client().interfaces.reconfigure_gifs().model_dump(exclude_none=True)


# ---- GRE ---------------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def interfaces_search_gres(search_phrase: str = "") -> dict[str, Any]:
    """Search GRE (Generic Routing Encapsulation) interface definitions."""
    result = get_client().interfaces.search_gres(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": list(result.rows)}


@mcp.tool()
@handle_opnsense_errors
def interfaces_get_gre(uuid: str) -> dict[str, Any]:
    """Get a GRE interface definition by UUID."""
    return get_client().interfaces.get_gre(uuid)


@mcp.tool()
@handle_opnsense_errors
def interfaces_add_gre(data_json: str) -> dict[str, Any]:
    """Create a GRE interface. data_json: JSON with GRE fields.
    Call interfaces_reconfigure_gres after."""
    return get_client().interfaces.add_gre(json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def interfaces_set_gre(uuid: str, data_json: str) -> dict[str, Any]:
    """Update a GRE interface. data_json: JSON with GRE fields.
    Call interfaces_reconfigure_gres after."""
    return get_client().interfaces.set_gre(uuid, json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def interfaces_del_gre(uuid: str) -> dict[str, Any]:
    """Delete a GRE interface by UUID. Call interfaces_reconfigure_gres after."""
    return get_client().interfaces.del_gre(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def interfaces_reconfigure_gres() -> dict[str, Any]:
    """Apply pending GRE interface changes."""
    return get_client().interfaces.reconfigure_gres().model_dump(exclude_none=True)


# ---- LAGG --------------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def interfaces_search_laggs(search_phrase: str = "") -> dict[str, Any]:
    """Search LAGG (Link Aggregation) interface definitions."""
    result = get_client().interfaces.search_laggs(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": list(result.rows)}


@mcp.tool()
@handle_opnsense_errors
def interfaces_get_lagg(uuid: str) -> dict[str, Any]:
    """Get a LAGG interface definition by UUID."""
    return get_client().interfaces.get_lagg(uuid)


@mcp.tool()
@handle_opnsense_errors
def interfaces_add_lagg(data_json: str) -> dict[str, Any]:
    """Create a LAGG interface. data_json: JSON with LAGG fields.
    Call interfaces_reconfigure_laggs after."""
    return get_client().interfaces.add_lagg(json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def interfaces_set_lagg(uuid: str, data_json: str) -> dict[str, Any]:
    """Update a LAGG interface. data_json: JSON with LAGG fields.
    Call interfaces_reconfigure_laggs after."""
    return get_client().interfaces.set_lagg(uuid, json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def interfaces_del_lagg(uuid: str) -> dict[str, Any]:
    """Delete a LAGG interface by UUID. Call interfaces_reconfigure_laggs after."""
    return get_client().interfaces.del_lagg(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def interfaces_reconfigure_laggs() -> dict[str, Any]:
    """Apply pending LAGG interface changes."""
    return get_client().interfaces.reconfigure_laggs().model_dump(exclude_none=True)


# ---- Loopback ----------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def interfaces_search_loopbacks(search_phrase: str = "") -> dict[str, Any]:
    """Search loopback interface definitions."""
    result = get_client().interfaces.search_loopbacks(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": list(result.rows)}


@mcp.tool()
@handle_opnsense_errors
def interfaces_add_loopback(data_json: str) -> dict[str, Any]:
    """Create a loopback interface. data_json: JSON with loopback fields.
    Call interfaces_reconfigure_loopbacks after."""
    return get_client().interfaces.add_loopback(json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def interfaces_set_loopback(uuid: str, data_json: str) -> dict[str, Any]:
    """Update a loopback interface. data_json: JSON with loopback fields.
    Call interfaces_reconfigure_loopbacks after."""
    return get_client().interfaces.set_loopback(uuid, json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def interfaces_del_loopback(uuid: str) -> dict[str, Any]:
    """Delete a loopback interface by UUID. Call interfaces_reconfigure_loopbacks after."""
    return get_client().interfaces.del_loopback(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def interfaces_reconfigure_loopbacks() -> dict[str, Any]:
    """Apply pending loopback interface changes."""
    return get_client().interfaces.reconfigure_loopbacks().model_dump(exclude_none=True)


# ---- Neighbors ---------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def interfaces_search_neighbors(search_phrase: str = "") -> dict[str, Any]:
    """Search static ARP/NDP neighbor definitions."""
    result = get_client().interfaces.search_neighbors(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": list(result.rows)}


@mcp.tool()
@handle_opnsense_errors
def interfaces_add_neighbor(data_json: str) -> dict[str, Any]:
    """Create a static neighbor entry. data_json: JSON with neighbor fields.
    Call interfaces_reconfigure_neighbors after."""
    return get_client().interfaces.add_neighbor(json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def interfaces_set_neighbor(uuid: str, data_json: str) -> dict[str, Any]:
    """Update a static neighbor entry. data_json: JSON with neighbor fields.
    Call interfaces_reconfigure_neighbors after."""
    return get_client().interfaces.set_neighbor(uuid, json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def interfaces_del_neighbor(uuid: str) -> dict[str, Any]:
    """Delete a static neighbor entry by UUID. Call interfaces_reconfigure_neighbors after."""
    return get_client().interfaces.del_neighbor(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def interfaces_reconfigure_neighbors() -> dict[str, Any]:
    """Apply pending neighbor entry changes."""
    return get_client().interfaces.reconfigure_neighbors().model_dump(exclude_none=True)


# ---- VIPs --------------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def interfaces_search_vips(search_phrase: str = "") -> dict[str, Any]:
    """Search Virtual IP (VIP) definitions."""
    result = get_client().interfaces.search_vips(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": list(result.rows)}


@mcp.tool()
@handle_opnsense_errors
def interfaces_get_vip(uuid: str) -> dict[str, Any]:
    """Get a VIP definition by UUID."""
    return get_client().interfaces.get_vip(uuid)


@mcp.tool()
@handle_opnsense_errors
def interfaces_add_vip(data_json: str) -> dict[str, Any]:
    """Create a Virtual IP. data_json: JSON with VIP fields.
    Call interfaces_reconfigure_vips after."""
    return get_client().interfaces.add_vip(json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def interfaces_set_vip(uuid: str, data_json: str) -> dict[str, Any]:
    """Update a Virtual IP. data_json: JSON with VIP fields.
    Call interfaces_reconfigure_vips after."""
    return get_client().interfaces.set_vip(uuid, json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def interfaces_del_vip(uuid: str) -> dict[str, Any]:
    """Delete a VIP by UUID. Call interfaces_reconfigure_vips after."""
    return get_client().interfaces.del_vip(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def interfaces_get_unused_vhid() -> dict[str, Any]:
    """Get the next available VHID for CARP VIPs."""
    return get_client().interfaces.get_unused_vhid()


@mcp.tool()
@handle_opnsense_errors
def interfaces_reconfigure_vips() -> dict[str, Any]:
    """Apply pending VIP changes."""
    return get_client().interfaces.reconfigure_vips().model_dump(exclude_none=True)


# ---- VLANs -------------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def interfaces_search_vlans(search_phrase: str = "") -> dict[str, Any]:
    """Search VLAN definitions."""
    result = get_client().interfaces.search_vlans(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": [r.model_dump(exclude_none=True) for r in result.rows]}


@mcp.tool()
@handle_opnsense_errors
def interfaces_get_vlan(uuid: str) -> dict[str, Any]:
    """Get a VLAN definition by UUID."""
    return get_client().interfaces.get_vlan(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def interfaces_add_vlan(
    if_: str,
    tag: str,
    descr: str | None = None,
    pcp: str | None = None,
) -> dict[str, Any]:
    """Create a VLAN. if_: parent interface. tag: VLAN tag (1-4094).
    Call interfaces_reconfigure_vlans after."""
    from opnsense_py.models.interfaces import Vlan
    vlan = Vlan(if_=if_, tag=int(tag) if tag else None, descr=descr, pcp=pcp)
    return get_client().interfaces.add_vlan(vlan).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def interfaces_set_vlan(
    uuid: str,
    if_: str | None = None,
    tag: str | None = None,
    descr: str | None = None,
    pcp: str | None = None,
) -> dict[str, Any]:
    """Update a VLAN. Call interfaces_reconfigure_vlans after."""
    from opnsense_py.models.interfaces import Vlan
    vlan = Vlan(
        if_=if_,
        tag=int(tag) if tag else None,
        descr=descr,
        pcp=pcp,
    )
    return get_client().interfaces.set_vlan(uuid, vlan).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def interfaces_del_vlan(uuid: str) -> dict[str, Any]:
    """Delete a VLAN by UUID. Call interfaces_reconfigure_vlans after."""
    return get_client().interfaces.del_vlan(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def interfaces_reconfigure_vlans() -> dict[str, Any]:
    """Apply pending VLAN changes."""
    return get_client().interfaces.reconfigure_vlans().model_dump(exclude_none=True)


# ---- VXLANs ------------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def interfaces_search_vxlans(search_phrase: str = "") -> dict[str, Any]:
    """Search VXLAN definitions."""
    result = get_client().interfaces.search_vxlans(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": list(result.rows)}


@mcp.tool()
@handle_opnsense_errors
def interfaces_add_vxlan(data_json: str) -> dict[str, Any]:
    """Create a VXLAN. data_json: JSON with VXLAN fields.
    Call interfaces_reconfigure_vxlans after."""
    return get_client().interfaces.add_vxlan(json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def interfaces_set_vxlan(uuid: str, data_json: str) -> dict[str, Any]:
    """Update a VXLAN. data_json: JSON with VXLAN fields.
    Call interfaces_reconfigure_vxlans after."""
    return get_client().interfaces.set_vxlan(uuid, json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def interfaces_del_vxlan(uuid: str) -> dict[str, Any]:
    """Delete a VXLAN by UUID. Call interfaces_reconfigure_vxlans after."""
    return get_client().interfaces.del_vxlan(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def interfaces_reconfigure_vxlans() -> dict[str, Any]:
    """Apply pending VXLAN changes."""
    return get_client().interfaces.reconfigure_vxlans().model_dump(exclude_none=True)


# ---- Overview ----------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def interfaces_get_interface(iface: str | None = None) -> dict[str, Any]:
    """Get details for a specific interface (e.g. 'em0') or all interfaces."""
    return get_client().interfaces.get_interface(iface)


@mcp.tool()
@handle_opnsense_errors
def interfaces_info(details: bool = False) -> dict[str, Any]:
    """Get overview of all interfaces. details=True includes extra stats."""
    return get_client().interfaces.interfaces_info(details)


@mcp.tool()
@handle_opnsense_errors
def interfaces_export() -> dict[str, Any]:
    """Export all interface configuration."""
    return get_client().interfaces.export_interfaces()
