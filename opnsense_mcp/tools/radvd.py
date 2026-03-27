from __future__ import annotations

import json
from typing import Any

from opnsense_py.models.base import SearchRequest

from opnsense_mcp.context import get_client
from opnsense_mcp.errors import handle_opnsense_errors
from opnsense_mcp.tools.registry import get_module_registrar
mcp = get_module_registrar(__name__)


@mcp.tool()
@handle_opnsense_errors
def radvd_get_settings() -> dict[str, Any]:
    """Get RADVd global settings."""
    return get_client().radvd.get()


@mcp.tool()
@handle_opnsense_errors
def radvd_set_settings(data_json: str) -> dict[str, Any]:
    """Update RADVd global settings. data_json: JSON object with settings fields.
    Call radvd_reconfigure after."""
    import json as _json
    return get_client().radvd.set(_json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def radvd_search_entries(search_phrase: str = "") -> dict[str, Any]:
    """Search RADVd advertisement entries."""
    result = get_client().radvd.search_entries(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": [r.model_dump(exclude_none=True) for r in result.rows]}


@mcp.tool()
@handle_opnsense_errors
def radvd_get_entry(uuid: str) -> dict[str, Any]:
    """Get a RADVd advertisement entry by UUID."""
    return get_client().radvd.get_entry(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def radvd_add_entry(data_json: str) -> dict[str, Any]:
    """Create a RADVd advertisement entry. data_json: JSON with entry fields.
    Call radvd_reconfigure after."""
    from opnsense_py.models.radvd import RadvdEntry
    entry = RadvdEntry.model_validate(json.loads(data_json))
    return get_client().radvd.add_entry(entry).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def radvd_set_entry(uuid: str, data_json: str) -> dict[str, Any]:
    """Update a RADVd advertisement entry. data_json: JSON with entry fields.
    Call radvd_reconfigure after."""
    from opnsense_py.models.radvd import RadvdEntry
    entry = RadvdEntry.model_validate(json.loads(data_json))
    return get_client().radvd.set_entry(uuid, entry).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def radvd_del_entry(uuid: str) -> dict[str, Any]:
    """Delete a RADVd advertisement entry by UUID. Call radvd_reconfigure after."""
    return get_client().radvd.del_entry(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def radvd_toggle_entry(uuid: str, enabled: bool | None = None) -> dict[str, Any]:
    """Toggle a RADVd advertisement entry enabled state. Call radvd_reconfigure after."""
    return get_client().radvd.toggle_entry(uuid, enabled).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def radvd_start() -> dict[str, Any]:
    """Start the RADVd service."""
    return get_client().radvd.start().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def radvd_stop() -> dict[str, Any]:
    """Stop the RADVd service."""
    return get_client().radvd.stop().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def radvd_restart() -> dict[str, Any]:
    """Restart the RADVd service."""
    return get_client().radvd.restart().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def radvd_reconfigure() -> dict[str, Any]:
    """Apply pending RADVd configuration changes. Call after any mutation."""
    return get_client().radvd.reconfigure().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def radvd_status() -> dict[str, Any]:
    """Get RADVd service status."""
    return get_client().radvd.status()
