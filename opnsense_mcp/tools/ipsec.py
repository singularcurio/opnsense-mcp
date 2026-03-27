from __future__ import annotations

import json
from typing import Any

from opnsense_py.models.base import SearchRequest

from opnsense_mcp.context import get_client
from opnsense_mcp.errors import handle_opnsense_errors
from opnsense_mcp.tools.registry import get_module_registrar
mcp = get_module_registrar(__name__)

# ---- Connections -------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def ipsec_search_connections(search_phrase: str = "") -> dict[str, Any]:
    """Search IPsec connections."""
    result = get_client().ipsec.search_connections(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": [r.model_dump(exclude_none=True) for r in result.rows]}


@mcp.tool()
@handle_opnsense_errors
def ipsec_get_connection(uuid: str) -> dict[str, Any]:
    """Get an IPsec connection by UUID."""
    return get_client().ipsec.get_connection(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def ipsec_add_connection(data_json: str) -> dict[str, Any]:
    """Create an IPsec connection. data_json: JSON with connection fields."""
    from opnsense_py.models.ipsec import IPsecConnection
    conn = IPsecConnection.model_validate(json.loads(data_json))
    return get_client().ipsec.add_connection(conn).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def ipsec_del_connection(uuid: str) -> dict[str, Any]:
    """Delete an IPsec connection by UUID. Call ipsec_reconfigure after."""
    return get_client().ipsec.del_connection(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def ipsec_toggle_connection(uuid: str, enabled: bool | None = None) -> dict[str, Any]:
    """Toggle an IPsec connection enabled state. Call ipsec_reconfigure after."""
    return get_client().ipsec.toggle_connection(uuid, enabled).model_dump(exclude_none=True)


# ---- Children ----------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def ipsec_search_children(search_phrase: str = "") -> dict[str, Any]:
    """Search IPsec child SAs."""
    result = get_client().ipsec.search_children(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": [r.model_dump(exclude_none=True) for r in result.rows]}


@mcp.tool()
@handle_opnsense_errors
def ipsec_add_child(data_json: str) -> dict[str, Any]:
    """Create an IPsec child SA. data_json: JSON with child fields."""
    from opnsense_py.models.ipsec import IPsecChild
    child = IPsecChild.model_validate(json.loads(data_json))
    return get_client().ipsec.add_child(child).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def ipsec_del_child(uuid: str) -> dict[str, Any]:
    """Delete an IPsec child SA by UUID."""
    return get_client().ipsec.del_child(uuid).model_dump(exclude_none=True)


# ---- Pools -------------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def ipsec_search_pools(search_phrase: str = "") -> dict[str, Any]:
    """Search IPsec IP pools."""
    result = get_client().ipsec.search_pools(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": [r.model_dump(exclude_none=True) for r in result.rows]}


@mcp.tool()
@handle_opnsense_errors
def ipsec_add_pool(data_json: str) -> dict[str, Any]:
    """Create an IPsec IP pool. data_json: JSON with pool fields."""
    from opnsense_py.models.ipsec import IPsecPool
    pool = IPsecPool.model_validate(json.loads(data_json))
    return get_client().ipsec.add_pool(pool).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def ipsec_del_pool(uuid: str) -> dict[str, Any]:
    """Delete an IPsec pool by UUID."""
    return get_client().ipsec.del_pool(uuid).model_dump(exclude_none=True)


# ---- Sessions ----------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def ipsec_search_sessions_phase1() -> dict[str, Any]:
    """List active IPsec phase 1 sessions."""
    result = get_client().ipsec.search_sessions_phase1()
    return {"total": result.total, "rows": [r.model_dump(exclude_none=True) for r in result.rows]}


@mcp.tool()
@handle_opnsense_errors
def ipsec_search_sessions_phase2() -> dict[str, Any]:
    """List active IPsec phase 2 sessions."""
    return get_client().ipsec.search_sessions_phase2()


@mcp.tool()
@handle_opnsense_errors
def ipsec_connect_session(session_id: str) -> dict[str, Any]:
    """Bring up an IPsec session by session ID."""
    return get_client().ipsec.connect_session(session_id).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def ipsec_disconnect_session(session_id: str) -> dict[str, Any]:
    """Tear down an IPsec session by session ID."""
    return get_client().ipsec.disconnect_session(session_id).model_dump(exclude_none=True)


# ---- Leases ------------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def ipsec_search_leases() -> dict[str, Any]:
    """List active IPsec IP pool leases."""
    result = get_client().ipsec.search_leases()
    return {"total": result.total, "rows": [r.model_dump(exclude_none=True) for r in result.rows]}


# ---- Key pairs ---------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def ipsec_search_key_pairs(search_phrase: str = "") -> dict[str, Any]:
    """Search IPsec key pairs."""
    result = get_client().ipsec.search_key_pairs(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": result.rows}


@mcp.tool()
@handle_opnsense_errors
def ipsec_gen_key_pair(key_type: str, size: str | None = None) -> dict[str, Any]:
    """Generate an IPsec key pair. key_type: RSA, ECDSA, etc."""
    return get_client().ipsec.gen_key_pair(key_type, size)


@mcp.tool()
@handle_opnsense_errors
def ipsec_del_key_pair(uuid: str) -> dict[str, Any]:
    """Delete an IPsec key pair by UUID."""
    return get_client().ipsec.del_key_pair(uuid).model_dump(exclude_none=True)


# ---- Pre-shared keys ---------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def ipsec_search_psks(search_phrase: str = "") -> dict[str, Any]:
    """Search IPsec pre-shared keys."""
    result = get_client().ipsec.search_psks(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": result.rows}


@mcp.tool()
@handle_opnsense_errors
def ipsec_add_psk(data_json: str) -> dict[str, Any]:
    """Create an IPsec pre-shared key. data_json: JSON with psk fields."""
    return get_client().ipsec.add_psk(json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def ipsec_del_psk(uuid: str) -> dict[str, Any]:
    """Delete an IPsec pre-shared key by UUID."""
    return get_client().ipsec.del_psk(uuid).model_dump(exclude_none=True)


# ---- SAD / SPD ---------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def ipsec_search_sad() -> dict[str, Any]:
    """List active IPsec Security Association Database (SAD) entries."""
    return get_client().ipsec.search_sad()


@mcp.tool()
@handle_opnsense_errors
def ipsec_search_spd() -> dict[str, Any]:
    """List active IPsec Security Policy Database (SPD) entries."""
    return get_client().ipsec.search_spd()


# ---- Service -----------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def ipsec_start() -> dict[str, Any]:
    """Start the IPsec service."""
    return get_client().ipsec.start().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def ipsec_stop() -> dict[str, Any]:
    """Stop the IPsec service."""
    return get_client().ipsec.stop().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def ipsec_restart() -> dict[str, Any]:
    """Restart the IPsec service."""
    return get_client().ipsec.restart().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def ipsec_reconfigure() -> dict[str, Any]:
    """Apply pending IPsec configuration changes. Call after any mutation."""
    return get_client().ipsec.reconfigure().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def ipsec_status() -> dict[str, Any]:
    """Get IPsec service status."""
    return get_client().ipsec.status()


@mcp.tool()
@handle_opnsense_errors
def ipsec_legacy_status() -> dict[str, Any]:
    """Get IPsec legacy subsystem status."""
    return get_client().ipsec.legacy_status()
