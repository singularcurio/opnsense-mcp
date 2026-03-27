from __future__ import annotations

import json
from typing import Any

from opnsense_py.models.base import SearchRequest

from opnsense_mcp.context import get_client
from opnsense_mcp.errors import handle_opnsense_errors
from opnsense_mcp.tools.registry import get_module_registrar
mcp = get_module_registrar(__name__)


# ---- Users -------------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def auth_search_users(search_phrase: str = "") -> dict[str, Any]:
    """Search local user accounts."""
    result = get_client().auth.search_users(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": list(result.rows)}


@mcp.tool()
@handle_opnsense_errors
def auth_get_user(uuid: str) -> dict[str, Any]:
    """Get a user account by UUID."""
    return get_client().auth.get_user(uuid)


@mcp.tool()
@handle_opnsense_errors
def auth_add_user(data_json: str) -> dict[str, Any]:
    """Create a user account. data_json: JSON with user fields (name, password, etc.)."""
    return get_client().auth.add_user(json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def auth_set_user(uuid: str, data_json: str) -> dict[str, Any]:
    """Update a user account. data_json: JSON with user fields."""
    return get_client().auth.set_user(uuid, json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def auth_del_user(uuid: str) -> dict[str, Any]:
    """Delete a user account by UUID."""
    return get_client().auth.del_user(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def auth_download_users() -> dict[str, Any]:
    """Export all user accounts as JSON."""
    return get_client().auth.download_users()


@mcp.tool()
@handle_opnsense_errors
def auth_new_otp_seed() -> dict[str, Any]:
    """Generate a new OTP seed for TOTP authentication."""
    return get_client().auth.new_otp_seed()


@mcp.tool()
@handle_opnsense_errors
def auth_search_api_keys() -> dict[str, Any]:
    """List all API keys."""
    return get_client().auth.search_api_keys()


@mcp.tool()
@handle_opnsense_errors
def auth_add_api_key(username: str) -> dict[str, Any]:
    """Generate a new API key for a user."""
    return get_client().auth.add_api_key(username).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def auth_del_api_key(key_id: str) -> dict[str, Any]:
    """Delete an API key by ID."""
    return get_client().auth.del_api_key(key_id).model_dump(exclude_none=True)


# ---- Groups ------------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def auth_search_groups(search_phrase: str = "") -> dict[str, Any]:
    """Search local user groups."""
    result = get_client().auth.search_groups(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": list(result.rows)}


@mcp.tool()
@handle_opnsense_errors
def auth_get_group(uuid: str) -> dict[str, Any]:
    """Get a user group by UUID."""
    return get_client().auth.get_group(uuid)


@mcp.tool()
@handle_opnsense_errors
def auth_add_group(data_json: str) -> dict[str, Any]:
    """Create a user group. data_json: JSON with group fields (name, description, etc.)."""
    return get_client().auth.add_group(json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def auth_set_group(uuid: str, data_json: str) -> dict[str, Any]:
    """Update a user group. data_json: JSON with group fields."""
    return get_client().auth.set_group(uuid, json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def auth_del_group(uuid: str) -> dict[str, Any]:
    """Delete a user group by UUID."""
    return get_client().auth.del_group(uuid).model_dump(exclude_none=True)


# ---- Privileges --------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def auth_search_privileges() -> dict[str, Any]:
    """List all available privileges."""
    return get_client().auth.search_privileges()


@mcp.tool()
@handle_opnsense_errors
def auth_get_privilege(priv_id: str) -> dict[str, Any]:
    """Get a privilege definition by ID."""
    return get_client().auth.get_privilege(priv_id)
