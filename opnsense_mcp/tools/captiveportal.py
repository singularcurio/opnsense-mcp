from __future__ import annotations

import json
from typing import Any

from opnsense_py.models.base import SearchRequest

from opnsense_mcp.context import get_client
from opnsense_mcp.errors import handle_opnsense_errors
from opnsense_mcp.tools.registry import get_module_registrar
mcp = get_module_registrar(__name__)


# ---- Zones -------------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def captiveportal_search_zones(search_phrase: str = "") -> dict[str, Any]:
    """Search captive portal zones."""
    result = get_client().captiveportal.search_zones(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": [r.model_dump(exclude_none=True) for r in result.rows]}


@mcp.tool()
@handle_opnsense_errors
def captiveportal_get_zone(uuid: str) -> dict[str, Any]:
    """Get a captive portal zone by UUID."""
    return get_client().captiveportal.get_zone(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def captiveportal_add_zone(data_json: str) -> dict[str, Any]:
    """Create a captive portal zone. data_json: JSON with zone fields.
    Call captiveportal_reconfigure after."""
    from opnsense_py.models.captiveportal import CaptivePortalZone
    zone = CaptivePortalZone.model_validate(json.loads(data_json))
    return get_client().captiveportal.add_zone(zone).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def captiveportal_set_zone(uuid: str, data_json: str) -> dict[str, Any]:
    """Update a captive portal zone. data_json: JSON with zone fields.
    Call captiveportal_reconfigure after."""
    from opnsense_py.models.captiveportal import CaptivePortalZone
    zone = CaptivePortalZone.model_validate(json.loads(data_json))
    return get_client().captiveportal.set_zone(uuid, zone).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def captiveportal_del_zone(uuid: str) -> dict[str, Any]:
    """Delete a captive portal zone by UUID. Call captiveportal_reconfigure after."""
    return get_client().captiveportal.del_zone(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def captiveportal_toggle_zone(uuid: str, enabled: bool | None = None) -> dict[str, Any]:
    """Toggle a captive portal zone enabled state. Call captiveportal_reconfigure after."""
    return get_client().captiveportal.toggle_zone(uuid, enabled).model_dump(exclude_none=True)


# ---- Sessions ----------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def captiveportal_list_sessions(zone_id: int = 0) -> dict[str, Any]:
    """List active sessions in a captive portal zone."""
    return get_client().captiveportal.list_sessions(zone_id)


@mcp.tool()
@handle_opnsense_errors
def captiveportal_search_sessions() -> dict[str, Any]:
    """Search all captive portal sessions across zones."""
    return get_client().captiveportal.search_sessions()


@mcp.tool()
@handle_opnsense_errors
def captiveportal_list_zones() -> dict[str, Any]:
    """List all captive portal zone IDs and names."""
    return get_client().captiveportal.list_zones()


@mcp.tool()
@handle_opnsense_errors
def captiveportal_disconnect_session(zone_id: str = "", data_json: str = "{}") -> dict[str, Any]:
    """Disconnect a client session from a captive portal zone.
    data_json: JSON with session identifier fields."""
    return get_client().captiveportal.disconnect_session(zone_id, json.loads(data_json)).model_dump(exclude_none=True)


# ---- Vouchers ----------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def captiveportal_list_voucher_providers() -> dict[str, Any]:
    """List all voucher providers configured in captive portal."""
    return get_client().captiveportal.list_voucher_providers()


@mcp.tool()
@handle_opnsense_errors
def captiveportal_list_voucher_groups(provider: str) -> dict[str, Any]:
    """List voucher groups for a provider."""
    return get_client().captiveportal.list_voucher_groups(provider)


@mcp.tool()
@handle_opnsense_errors
def captiveportal_list_vouchers(provider: str, group: str) -> dict[str, Any]:
    """List vouchers in a group for a provider."""
    return get_client().captiveportal.list_vouchers(provider, group)


@mcp.tool()
@handle_opnsense_errors
def captiveportal_generate_vouchers(provider: str, data_json: str) -> dict[str, Any]:
    """Generate vouchers for a provider. data_json: JSON with count, validity, group fields."""
    return get_client().captiveportal.generate_vouchers(provider, json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def captiveportal_expire_voucher(provider: str, data_json: str) -> dict[str, Any]:
    """Expire a voucher. data_json: JSON with voucher identifier."""
    return get_client().captiveportal.expire_voucher(provider, json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def captiveportal_drop_voucher_group(provider: str, group: str) -> dict[str, Any]:
    """Delete all vouchers in a group."""
    return get_client().captiveportal.drop_voucher_group(provider, group).model_dump(exclude_none=True)


# ---- Service -----------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def captiveportal_start() -> dict[str, Any]:
    """Start the captive portal service."""
    return get_client().captiveportal.start().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def captiveportal_stop() -> dict[str, Any]:
    """Stop the captive portal service."""
    return get_client().captiveportal.stop().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def captiveportal_restart() -> dict[str, Any]:
    """Restart the captive portal service."""
    return get_client().captiveportal.restart().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def captiveportal_reconfigure() -> dict[str, Any]:
    """Apply pending captive portal configuration changes. Call after any mutation."""
    return get_client().captiveportal.reconfigure().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def captiveportal_status() -> dict[str, Any]:
    """Get captive portal service status."""
    return get_client().captiveportal.status()
