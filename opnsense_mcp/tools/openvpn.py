from __future__ import annotations

import json
from typing import Any

from opnsense_py.models.base import SearchRequest

from opnsense_mcp.context import get_client
from opnsense_mcp.errors import handle_opnsense_errors
from opnsense_mcp.tools.registry import get_module_registrar
mcp = get_module_registrar(__name__)

# ---- Instances ---------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def openvpn_search_instances(search_phrase: str = "") -> dict[str, Any]:
    """Search OpenVPN instances (servers and clients)."""
    result = get_client().openvpn.search_instances(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": [r.model_dump(exclude_none=True) for r in result.rows]}


@mcp.tool()
@handle_opnsense_errors
def openvpn_get_instance(uuid: str) -> dict[str, Any]:
    """Get an OpenVPN instance by UUID."""
    return get_client().openvpn.get_instance(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def openvpn_add_instance(data_json: str) -> dict[str, Any]:
    """Create an OpenVPN instance. data_json: JSON with instance fields."""
    from opnsense_py.models.openvpn import OpenVPNInstance
    instance = OpenVPNInstance.model_validate(json.loads(data_json))
    return get_client().openvpn.add_instance(instance).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def openvpn_del_instance(uuid: str) -> dict[str, Any]:
    """Delete an OpenVPN instance by UUID. Call openvpn_reconfigure after."""
    return get_client().openvpn.del_instance(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def openvpn_toggle_instance(uuid: str, enabled: bool | None = None) -> dict[str, Any]:
    """Toggle an OpenVPN instance enabled state. Call openvpn_reconfigure after."""
    return get_client().openvpn.toggle_instance(uuid, enabled).model_dump(exclude_none=True)


# ---- Static keys -------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def openvpn_search_static_keys(search_phrase: str = "") -> dict[str, Any]:
    """Search OpenVPN static keys."""
    result = get_client().openvpn.search_static_keys(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": [r.model_dump(exclude_none=True) for r in result.rows]}


@mcp.tool()
@handle_opnsense_errors
def openvpn_gen_key(key_type: str = "secret") -> dict[str, Any]:
    """Generate an OpenVPN static key. key_type: secret (default) or tls-auth."""
    return get_client().openvpn.gen_key(key_type)


# ---- Client overwrites -------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def openvpn_search_client_overwrites(search_phrase: str = "") -> dict[str, Any]:
    """Search OpenVPN client-specific configuration overwrites."""
    result = get_client().openvpn.search_client_overwrites(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": [r.model_dump(exclude_none=True) for r in result.rows]}


@mcp.tool()
@handle_opnsense_errors
def openvpn_add_client_overwrite(data_json: str) -> dict[str, Any]:
    """Create an OpenVPN client overwrite. data_json: JSON with overwrite fields."""
    from opnsense_py.models.openvpn import OpenVPNOverwrite
    overwrite = OpenVPNOverwrite.model_validate(json.loads(data_json))
    return get_client().openvpn.add_client_overwrite(overwrite).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def openvpn_del_client_overwrite(uuid: str) -> dict[str, Any]:
    """Delete an OpenVPN client overwrite by UUID."""
    return get_client().openvpn.del_client_overwrite(uuid).model_dump(exclude_none=True)


# ---- Sessions / routes -------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def openvpn_search_sessions() -> dict[str, Any]:
    """List active OpenVPN client sessions."""
    return get_client().openvpn.search_sessions()


@mcp.tool()
@handle_opnsense_errors
def openvpn_search_routes() -> dict[str, Any]:
    """List OpenVPN routing table entries."""
    return get_client().openvpn.search_routes()


@mcp.tool()
@handle_opnsense_errors
def openvpn_kill_session(data_json: str = "{}") -> dict[str, Any]:
    """Kill an OpenVPN client session. data_json: JSON with session filter."""
    return get_client().openvpn.kill_session(json.loads(data_json)).model_dump(exclude_none=True)


# ---- Service -----------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def openvpn_reconfigure() -> dict[str, Any]:
    """Apply pending OpenVPN configuration changes. Call after any mutation."""
    return get_client().openvpn.reconfigure().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def openvpn_start_service(service_id: str | None = None) -> dict[str, Any]:
    """Start an OpenVPN instance service. service_id: optional specific instance."""
    return get_client().openvpn.start_service(service_id).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def openvpn_stop_service(service_id: str | None = None) -> dict[str, Any]:
    """Stop an OpenVPN instance service."""
    return get_client().openvpn.stop_service(service_id).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def openvpn_restart_service(service_id: str | None = None) -> dict[str, Any]:
    """Restart an OpenVPN instance service."""
    return get_client().openvpn.restart_service(service_id).model_dump(exclude_none=True)
