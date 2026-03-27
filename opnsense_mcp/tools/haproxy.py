from __future__ import annotations

import json
from typing import Any

from opnsense_py.models.base import SearchRequest

from opnsense_mcp.context import get_client
from opnsense_mcp.errors import handle_opnsense_errors
from opnsense_mcp.tools.registry import get_module_registrar
mcp = get_module_registrar(__name__)


# ---- Global settings ---------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def haproxy_get_settings() -> dict[str, Any]:
    """Get HAProxy global settings."""
    return get_client().haproxy.get()


@mcp.tool()
@handle_opnsense_errors
def haproxy_set_settings(data_json: str) -> dict[str, Any]:
    """Update HAProxy global settings. data_json: JSON with settings fields.
    Call haproxy_reconfigure after."""
    return get_client().haproxy.set(json.loads(data_json)).model_dump(exclude_none=True)


# ---- Frontends ---------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def haproxy_search_frontends(search_phrase: str = "") -> dict[str, Any]:
    """Search HAProxy frontend definitions."""
    result = get_client().haproxy.search_frontends(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": list(result.rows)}


@mcp.tool()
@handle_opnsense_errors
def haproxy_get_frontend(uuid: str) -> dict[str, Any]:
    """Get an HAProxy frontend by UUID."""
    return get_client().haproxy.get_frontend(uuid)


@mcp.tool()
@handle_opnsense_errors
def haproxy_add_frontend(data_json: str) -> dict[str, Any]:
    """Create an HAProxy frontend. data_json: JSON with frontend fields.
    Call haproxy_reconfigure after."""
    return get_client().haproxy.add_frontend(json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def haproxy_set_frontend(uuid: str, data_json: str) -> dict[str, Any]:
    """Update an HAProxy frontend. data_json: JSON with frontend fields.
    Call haproxy_reconfigure after."""
    return get_client().haproxy.set_frontend(uuid, json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def haproxy_del_frontend(uuid: str) -> dict[str, Any]:
    """Delete an HAProxy frontend by UUID. Call haproxy_reconfigure after."""
    return get_client().haproxy.del_frontend(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def haproxy_toggle_frontend(uuid: str) -> dict[str, Any]:
    """Toggle an HAProxy frontend enabled state. Call haproxy_reconfigure after."""
    return get_client().haproxy.toggle_frontend(uuid).model_dump(exclude_none=True)


# ---- Backends ----------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def haproxy_search_backends(search_phrase: str = "") -> dict[str, Any]:
    """Search HAProxy backend definitions."""
    result = get_client().haproxy.search_backends(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": list(result.rows)}


@mcp.tool()
@handle_opnsense_errors
def haproxy_get_backend(uuid: str) -> dict[str, Any]:
    """Get an HAProxy backend by UUID."""
    return get_client().haproxy.get_backend(uuid)


@mcp.tool()
@handle_opnsense_errors
def haproxy_add_backend(data_json: str) -> dict[str, Any]:
    """Create an HAProxy backend. data_json: JSON with backend fields.
    Call haproxy_reconfigure after."""
    return get_client().haproxy.add_backend(json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def haproxy_set_backend(uuid: str, data_json: str) -> dict[str, Any]:
    """Update an HAProxy backend. data_json: JSON with backend fields.
    Call haproxy_reconfigure after."""
    return get_client().haproxy.set_backend(uuid, json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def haproxy_del_backend(uuid: str) -> dict[str, Any]:
    """Delete an HAProxy backend by UUID. Call haproxy_reconfigure after."""
    return get_client().haproxy.del_backend(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def haproxy_toggle_backend(uuid: str, enabled: bool | None = None) -> dict[str, Any]:
    """Toggle an HAProxy backend enabled state. Call haproxy_reconfigure after."""
    return get_client().haproxy.toggle_backend(uuid, enabled).model_dump(exclude_none=True)


# ---- Servers -----------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def haproxy_search_servers(search_phrase: str = "") -> dict[str, Any]:
    """Search HAProxy server definitions."""
    result = get_client().haproxy.search_servers(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": list(result.rows)}


@mcp.tool()
@handle_opnsense_errors
def haproxy_get_server(uuid: str) -> dict[str, Any]:
    """Get an HAProxy server by UUID."""
    return get_client().haproxy.get_server(uuid)


@mcp.tool()
@handle_opnsense_errors
def haproxy_add_server(data_json: str) -> dict[str, Any]:
    """Create an HAProxy server. data_json: JSON with server fields.
    Call haproxy_reconfigure after."""
    return get_client().haproxy.add_server(json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def haproxy_set_server(uuid: str, data_json: str) -> dict[str, Any]:
    """Update an HAProxy server. data_json: JSON with server fields.
    Call haproxy_reconfigure after."""
    return get_client().haproxy.set_server(uuid, json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def haproxy_del_server(uuid: str) -> dict[str, Any]:
    """Delete an HAProxy server by UUID. Call haproxy_reconfigure after."""
    return get_client().haproxy.del_server(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def haproxy_toggle_server(uuid: str, enabled: bool | None = None) -> dict[str, Any]:
    """Toggle an HAProxy server enabled state. Call haproxy_reconfigure after."""
    return get_client().haproxy.toggle_server(uuid, enabled).model_dump(exclude_none=True)


# ---- ACLs --------------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def haproxy_search_acls(search_phrase: str = "") -> dict[str, Any]:
    """Search HAProxy ACL definitions."""
    result = get_client().haproxy.search_acls(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": list(result.rows)}


@mcp.tool()
@handle_opnsense_errors
def haproxy_add_acl(data_json: str) -> dict[str, Any]:
    """Create an HAProxy ACL. data_json: JSON with ACL fields.
    Call haproxy_reconfigure after."""
    return get_client().haproxy.add_acl(json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def haproxy_set_acl(uuid: str, data_json: str) -> dict[str, Any]:
    """Update an HAProxy ACL. data_json: JSON with ACL fields.
    Call haproxy_reconfigure after."""
    return get_client().haproxy.set_acl(uuid, json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def haproxy_del_acl(uuid: str) -> dict[str, Any]:
    """Delete an HAProxy ACL by UUID. Call haproxy_reconfigure after."""
    return get_client().haproxy.del_acl(uuid).model_dump(exclude_none=True)


# ---- Actions -----------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def haproxy_search_actions(search_phrase: str = "") -> dict[str, Any]:
    """Search HAProxy action definitions."""
    result = get_client().haproxy.search_actions(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": list(result.rows)}


@mcp.tool()
@handle_opnsense_errors
def haproxy_add_action(data_json: str) -> dict[str, Any]:
    """Create an HAProxy action. data_json: JSON with action fields.
    Call haproxy_reconfigure after."""
    return get_client().haproxy.add_action(json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def haproxy_set_action(uuid: str, data_json: str) -> dict[str, Any]:
    """Update an HAProxy action. data_json: JSON with action fields.
    Call haproxy_reconfigure after."""
    return get_client().haproxy.set_action(uuid, json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def haproxy_del_action(uuid: str) -> dict[str, Any]:
    """Delete an HAProxy action by UUID. Call haproxy_reconfigure after."""
    return get_client().haproxy.del_action(uuid).model_dump(exclude_none=True)


# ---- Health checks -----------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def haproxy_search_healthchecks(search_phrase: str = "") -> dict[str, Any]:
    """Search HAProxy health check definitions."""
    result = get_client().haproxy.search_healthchecks(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": list(result.rows)}


@mcp.tool()
@handle_opnsense_errors
def haproxy_add_healthcheck(data_json: str) -> dict[str, Any]:
    """Create an HAProxy health check. data_json: JSON with health check fields.
    Call haproxy_reconfigure after."""
    return get_client().haproxy.add_healthcheck(json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def haproxy_set_healthcheck(uuid: str, data_json: str) -> dict[str, Any]:
    """Update an HAProxy health check. data_json: JSON with health check fields.
    Call haproxy_reconfigure after."""
    return get_client().haproxy.set_healthcheck(uuid, json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def haproxy_del_healthcheck(uuid: str) -> dict[str, Any]:
    """Delete an HAProxy health check by UUID. Call haproxy_reconfigure after."""
    return get_client().haproxy.del_healthcheck(uuid).model_dump(exclude_none=True)


# ---- Users -------------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def haproxy_search_users(search_phrase: str = "") -> dict[str, Any]:
    """Search HAProxy user list definitions."""
    result = get_client().haproxy.search_users(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": list(result.rows)}


@mcp.tool()
@handle_opnsense_errors
def haproxy_add_user(data_json: str) -> dict[str, Any]:
    """Create an HAProxy user. data_json: JSON with user fields.
    Call haproxy_reconfigure after."""
    return get_client().haproxy.add_user(json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def haproxy_set_user(uuid: str, data_json: str) -> dict[str, Any]:
    """Update an HAProxy user. data_json: JSON with user fields.
    Call haproxy_reconfigure after."""
    return get_client().haproxy.set_user(uuid, json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def haproxy_del_user(uuid: str) -> dict[str, Any]:
    """Delete an HAProxy user by UUID. Call haproxy_reconfigure after."""
    return get_client().haproxy.del_user(uuid).model_dump(exclude_none=True)


# ---- Mailers -----------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def haproxy_search_mailers(search_phrase: str = "") -> dict[str, Any]:
    """Search HAProxy mailer definitions."""
    result = get_client().haproxy.search_mailers(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": list(result.rows)}


@mcp.tool()
@handle_opnsense_errors
def haproxy_add_mailer(data_json: str) -> dict[str, Any]:
    """Create an HAProxy mailer. data_json: JSON with mailer fields.
    Call haproxy_reconfigure after."""
    return get_client().haproxy.add_mailer(json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def haproxy_set_mailer(uuid: str, data_json: str) -> dict[str, Any]:
    """Update an HAProxy mailer. data_json: JSON with mailer fields.
    Call haproxy_reconfigure after."""
    return get_client().haproxy.set_mailer(uuid, json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def haproxy_del_mailer(uuid: str) -> dict[str, Any]:
    """Delete an HAProxy mailer by UUID. Call haproxy_reconfigure after."""
    return get_client().haproxy.del_mailer(uuid).model_dump(exclude_none=True)


# ---- Resolvers ---------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def haproxy_search_resolvers(search_phrase: str = "") -> dict[str, Any]:
    """Search HAProxy resolver definitions."""
    result = get_client().haproxy.search_resolvers(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": list(result.rows)}


@mcp.tool()
@handle_opnsense_errors
def haproxy_add_resolver(data_json: str) -> dict[str, Any]:
    """Create an HAProxy resolver. data_json: JSON with resolver fields.
    Call haproxy_reconfigure after."""
    return get_client().haproxy.add_resolver(json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def haproxy_set_resolver(uuid: str, data_json: str) -> dict[str, Any]:
    """Update an HAProxy resolver. data_json: JSON with resolver fields.
    Call haproxy_reconfigure after."""
    return get_client().haproxy.set_resolver(uuid, json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def haproxy_del_resolver(uuid: str) -> dict[str, Any]:
    """Delete an HAProxy resolver by UUID. Call haproxy_reconfigure after."""
    return get_client().haproxy.del_resolver(uuid).model_dump(exclude_none=True)


# ---- Maintenance / Statistics ------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def haproxy_get_maintenance() -> dict[str, Any]:
    """Get HAProxy maintenance mode settings."""
    return get_client().haproxy.get_maintenance()


@mcp.tool()
@handle_opnsense_errors
def haproxy_server_state() -> dict[str, Any]:
    """Get current runtime state of all HAProxy servers."""
    return get_client().haproxy.server_state()


@mcp.tool()
@handle_opnsense_errors
def haproxy_stat_counters() -> dict[str, Any]:
    """Get HAProxy statistics counters."""
    return get_client().haproxy.stat_counters()


@mcp.tool()
@handle_opnsense_errors
def haproxy_stat_info() -> dict[str, Any]:
    """Get HAProxy process information."""
    return get_client().haproxy.stat_info()


@mcp.tool()
@handle_opnsense_errors
def haproxy_export_config() -> dict[str, Any]:
    """Export the rendered HAProxy configuration."""
    return get_client().haproxy.export_config()


# ---- Service -----------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def haproxy_configtest() -> dict[str, Any]:
    """Test the HAProxy configuration for syntax errors."""
    return get_client().haproxy.configtest()


@mcp.tool()
@handle_opnsense_errors
def haproxy_start() -> dict[str, Any]:
    """Start the HAProxy service."""
    return get_client().haproxy.start().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def haproxy_stop() -> dict[str, Any]:
    """Stop the HAProxy service."""
    return get_client().haproxy.stop().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def haproxy_restart() -> dict[str, Any]:
    """Restart the HAProxy service."""
    return get_client().haproxy.restart().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def haproxy_reconfigure() -> dict[str, Any]:
    """Apply pending HAProxy configuration changes. Call after any mutation."""
    return get_client().haproxy.reconfigure().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def haproxy_status() -> dict[str, Any]:
    """Get HAProxy service status."""
    return get_client().haproxy.status()
