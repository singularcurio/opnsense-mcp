from __future__ import annotations

import json
from typing import Any

from opnsense_py.models.base import SearchRequest
from opnsense_py.models.ids import IDSPolicy, IDSUserRule

from opnsense_mcp.context import get_client
from opnsense_mcp.errors import handle_opnsense_errors
from opnsense_mcp.tools.registry import get_module_registrar
mcp = get_module_registrar(__name__)

# ---- Settings ----------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def ids_get_settings() -> dict[str, Any]:
    """Get global IDS/IPS (Suricata) settings."""
    return get_client().ids.get()


# ---- Policies ----------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def ids_search_policies(search_phrase: str = "") -> dict[str, Any]:
    """Search IDS/IPS policies."""
    result = get_client().ids.search_policies(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": [r.model_dump(exclude_none=True) for r in result.rows]}


@mcp.tool()
@handle_opnsense_errors
def ids_get_policy(uuid: str) -> dict[str, Any]:
    """Get an IDS/IPS policy by UUID."""
    return get_client().ids.get_policy(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def ids_add_policy(data_json: str) -> dict[str, Any]:
    """Create an IDS/IPS policy. data_json: JSON with policy fields."""
    policy = IDSPolicy.model_validate(json.loads(data_json))
    return get_client().ids.add_policy(policy).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def ids_del_policy(uuid: str) -> dict[str, Any]:
    """Delete an IDS/IPS policy by UUID."""
    return get_client().ids.del_policy(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def ids_toggle_policy(uuid: str, enabled: bool | None = None) -> dict[str, Any]:
    """Toggle an IDS/IPS policy enabled state."""
    return get_client().ids.toggle_policy(uuid, enabled).model_dump(exclude_none=True)


# ---- User rules --------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def ids_search_user_rules(search_phrase: str = "") -> dict[str, Any]:
    """Search IDS/IPS custom user rules."""
    result = get_client().ids.search_user_rules(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": [r.model_dump(exclude_none=True) for r in result.rows]}


@mcp.tool()
@handle_opnsense_errors
def ids_add_user_rule(data_json: str) -> dict[str, Any]:
    """Create a custom IDS/IPS rule. data_json: JSON with rule fields (action, source_ip, etc.)."""
    rule = IDSUserRule.model_validate(json.loads(data_json))
    return get_client().ids.add_user_rule(rule).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def ids_del_user_rule(uuid: str) -> dict[str, Any]:
    """Delete a custom IDS/IPS rule by UUID."""
    return get_client().ids.del_user_rule(uuid).model_dump(exclude_none=True)


# ---- Rulesets ----------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def ids_list_rulesets() -> dict[str, Any]:
    """List all available IDS/IPS rulesets."""
    return get_client().ids.list_rulesets()


@mcp.tool()
@handle_opnsense_errors
def ids_toggle_ruleset(filenames: str, enabled: bool | None = None) -> dict[str, Any]:
    """Enable or disable an IDS/IPS ruleset by filename."""
    return get_client().ids.toggle_ruleset(filenames, enabled).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def ids_search_installed_rules(data_json: str = "{}") -> dict[str, Any]:
    """Search installed IDS/IPS rules. data_json: optional JSON filter."""
    return get_client().ids.search_installed_rules(json.loads(data_json))


@mcp.tool()
@handle_opnsense_errors
def ids_get_alert_logs() -> dict[str, Any]:
    """Get IDS/IPS alert log files."""
    return get_client().ids.get_alert_logs()


@mcp.tool()
@handle_opnsense_errors
def ids_query_alerts(data_json: str = "{}") -> dict[str, Any]:
    """Query IDS/IPS alerts. data_json: optional JSON filter."""
    return get_client().ids.query_alerts(json.loads(data_json))


@mcp.tool()
@handle_opnsense_errors
def ids_drop_alert_log() -> dict[str, Any]:
    """Clear the IDS/IPS alert log."""
    return get_client().ids.drop_alert_log().model_dump(exclude_none=True)


# ---- Service -----------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def ids_start() -> dict[str, Any]:
    """Start the IDS/IPS (Suricata) service."""
    return get_client().ids.start().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def ids_stop() -> dict[str, Any]:
    """Stop the IDS/IPS service."""
    return get_client().ids.stop().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def ids_restart() -> dict[str, Any]:
    """Restart the IDS/IPS service."""
    return get_client().ids.restart().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def ids_reconfigure() -> dict[str, Any]:
    """Apply pending IDS/IPS configuration changes. Call after any mutation."""
    return get_client().ids.reconfigure().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def ids_reload_rules() -> dict[str, Any]:
    """Reload IDS/IPS rules without full restart."""
    return get_client().ids.reload_rules().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def ids_update_rules(wait: bool | None = None) -> dict[str, Any]:
    """Update IDS/IPS rules from configured sources."""
    return get_client().ids.update_rules(wait).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def ids_status() -> dict[str, Any]:
    """Get IDS/IPS service status."""
    return get_client().ids.status()
