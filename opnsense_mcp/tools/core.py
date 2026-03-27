from __future__ import annotations

import json
from typing import Any

from opnsense_py.models.base import SearchRequest

from opnsense_mcp.context import get_client
from opnsense_mcp.errors import handle_opnsense_errors
from opnsense_mcp.tools.registry import get_module_registrar
mcp = get_module_registrar(__name__)

# ---- System ------------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def core_system_status() -> dict[str, Any]:
    """Get OPNsense system status overview."""
    return get_client().core.system_status()


@mcp.tool()
@handle_opnsense_errors
def core_reboot() -> dict[str, Any]:
    """Reboot the system."""
    return get_client().core.reboot().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def core_halt() -> dict[str, Any]:
    """Halt (power off) the system."""
    return get_client().core.halt().model_dump(exclude_none=True)


# ---- Services ----------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def core_search_services() -> dict[str, Any]:
    """List all system services and their current state."""
    result = get_client().core.search_services()
    return {"total": result.total, "rows": [r.model_dump(exclude_none=True) for r in result.rows]}


@mcp.tool()
@handle_opnsense_errors
def core_start_service(name: str, service_id: str = "") -> dict[str, Any]:
    """Start a system service by name."""
    return get_client().core.start_service(name, service_id).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def core_stop_service(name: str, service_id: str = "") -> dict[str, Any]:
    """Stop a system service by name."""
    return get_client().core.stop_service(name, service_id).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def core_restart_service(name: str, service_id: str = "") -> dict[str, Any]:
    """Restart a system service by name."""
    return get_client().core.restart_service(name, service_id).model_dump(exclude_none=True)


# ---- Tunables ----------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def core_search_tunables(search_phrase: str = "") -> dict[str, Any]:
    """Search system tunables (sysctl)."""
    result = get_client().core.search_tunables(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": [r.model_dump(exclude_none=True) for r in result.rows]}


@mcp.tool()
@handle_opnsense_errors
def core_get_tunable(uuid: str) -> dict[str, Any]:
    """Get a system tunable by UUID."""
    return get_client().core.get_tunable(uuid)


@mcp.tool()
@handle_opnsense_errors
def core_add_tunable(data_json: str) -> dict[str, Any]:
    """Create a system tunable. data_json: JSON with tunable fields (tunable, value, descr)."""
    return get_client().core.add_tunable(json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def core_set_tunable(uuid: str, data_json: str) -> dict[str, Any]:
    """Update a system tunable. data_json: JSON with tunable fields."""
    return get_client().core.set_tunable(uuid, json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def core_del_tunable(uuid: str) -> dict[str, Any]:
    """Delete a system tunable by UUID."""
    return get_client().core.del_tunable(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def core_reconfigure_tunables() -> dict[str, Any]:
    """Apply pending tunable changes."""
    return get_client().core.reconfigure_tunables().model_dump(exclude_none=True)


# ---- Backups -----------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def core_list_backups(host: str) -> dict[str, Any]:
    """List available configuration backups for a host."""
    return get_client().core.list_backups(host)


@mcp.tool()
@handle_opnsense_errors
def core_backup_providers() -> dict[str, Any]:
    """List available backup providers."""
    return get_client().core.backup_providers()
