from __future__ import annotations

import json
from typing import Any

from opnsense_py.models.base import SearchRequest

from opnsense_mcp.context import get_client
from opnsense_mcp.errors import handle_opnsense_errors
from opnsense_mcp.tools.registry import get_module_registrar
mcp = get_module_registrar(__name__)

# ---- Servers -----------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def wireguard_search_servers(search_phrase: str = "") -> dict[str, Any]:
    """Search WireGuard server instances."""
    result = get_client().wireguard.search_servers(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": [r.model_dump(exclude_none=True) for r in result.rows]}


@mcp.tool()
@handle_opnsense_errors
def wireguard_get_server(uuid: str) -> dict[str, Any]:
    """Get a WireGuard server by UUID."""
    return get_client().wireguard.get_server(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def wireguard_add_server(data_json: str) -> dict[str, Any]:
    """Create a WireGuard server. data_json: JSON with server fields.
    Use wireguard_key_pair to generate key material first."""
    from opnsense_py.models.wireguard import WireguardServer
    server = WireguardServer.model_validate(json.loads(data_json))
    return get_client().wireguard.add_server(server).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def wireguard_set_server(uuid: str, data_json: str) -> dict[str, Any]:
    """Update a WireGuard server. data_json: JSON with server fields."""
    from opnsense_py.models.wireguard import WireguardServer
    server = WireguardServer.model_validate(json.loads(data_json))
    return get_client().wireguard.set_server(uuid, server).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def wireguard_del_server(uuid: str) -> dict[str, Any]:
    """Delete a WireGuard server by UUID."""
    return get_client().wireguard.del_server(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def wireguard_toggle_server(uuid: str) -> dict[str, Any]:
    """Toggle a WireGuard server enabled state."""
    return get_client().wireguard.toggle_server(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def wireguard_key_pair() -> dict[str, Any]:
    """Generate a new WireGuard key pair (public + private key)."""
    return get_client().wireguard.key_pair()


# ---- Clients / Peers ---------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def wireguard_search_clients(search_phrase: str = "") -> dict[str, Any]:
    """Search WireGuard peers (clients)."""
    result = get_client().wireguard.search_clients(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": [r.model_dump(exclude_none=True) for r in result.rows]}


@mcp.tool()
@handle_opnsense_errors
def wireguard_get_client(uuid: str) -> dict[str, Any]:
    """Get a WireGuard peer by UUID."""
    return get_client().wireguard.get_client(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def wireguard_add_client_builder(data_json: str) -> dict[str, Any]:
    """Create a WireGuard peer using the builder endpoint.
    data_json: JSON with peer fields including public_key, tunnel_address, servers."""
    from opnsense_py.models.wireguard import WireguardPeer
    peer = WireguardPeer.model_validate(json.loads(data_json))
    return get_client().wireguard.add_client_builder(peer).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def wireguard_set_client(uuid: str, data_json: str) -> dict[str, Any]:
    """Update a WireGuard peer. data_json: JSON with peer fields."""
    from opnsense_py.models.wireguard import WireguardPeer
    peer = WireguardPeer.model_validate(json.loads(data_json))
    return get_client().wireguard.set_client(uuid, peer).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def wireguard_del_client(uuid: str) -> dict[str, Any]:
    """Delete a WireGuard peer by UUID."""
    return get_client().wireguard.del_client(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def wireguard_toggle_client(uuid: str) -> dict[str, Any]:
    """Toggle a WireGuard peer enabled state."""
    return get_client().wireguard.toggle_client(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def wireguard_psk() -> dict[str, Any]:
    """Generate a new WireGuard pre-shared key."""
    return get_client().wireguard.psk()


@mcp.tool()
@handle_opnsense_errors
def wireguard_list_servers() -> dict[str, Any]:
    """List available WireGuard servers (for peer assignment)."""
    return get_client().wireguard.list_servers()


# ---- Service -----------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def wireguard_start() -> dict[str, Any]:
    """Start the WireGuard service."""
    return get_client().wireguard.start().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def wireguard_stop() -> dict[str, Any]:
    """Stop the WireGuard service."""
    return get_client().wireguard.stop().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def wireguard_restart() -> dict[str, Any]:
    """Restart the WireGuard service."""
    return get_client().wireguard.restart().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def wireguard_reconfigure() -> dict[str, Any]:
    """Apply pending WireGuard configuration changes. Call after any mutation."""
    return get_client().wireguard.reconfigure().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def wireguard_show() -> dict[str, Any]:
    """Show WireGuard interface status (wg show)."""
    return get_client().wireguard.show()


@mcp.tool()
@handle_opnsense_errors
def wireguard_status() -> dict[str, Any]:
    """Get WireGuard service status."""
    return get_client().wireguard.status()
