from __future__ import annotations

import json
from typing import Any

from opnsense_py.models.base import SearchRequest
from opnsense_py.models.monit import MonitAlert, MonitService, MonitTest

from opnsense_mcp.context import get_client
from opnsense_mcp.errors import handle_opnsense_errors
from opnsense_mcp.tools.registry import get_module_registrar
mcp = get_module_registrar(__name__)

# ---- Services ----------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def monit_search_services(search_phrase: str = "") -> dict[str, Any]:
    """Search Monit service checks."""
    result = get_client().monit.search_services(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": [r.model_dump(exclude_none=True) for r in result.rows]}


@mcp.tool()
@handle_opnsense_errors
def monit_get_service(uuid: str) -> dict[str, Any]:
    """Get a Monit service check by UUID."""
    return get_client().monit.get_service(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def monit_add_service(data_json: str) -> dict[str, Any]:
    """Create a Monit service check. data_json: JSON with service fields.
    Call monit_reconfigure after."""
    svc = MonitService.model_validate(json.loads(data_json))
    return get_client().monit.add_service(svc).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def monit_del_service(uuid: str) -> dict[str, Any]:
    """Delete a Monit service check by UUID. Call monit_reconfigure after."""
    return get_client().monit.del_service(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def monit_toggle_service(uuid: str, enabled: bool | None = None) -> dict[str, Any]:
    """Toggle a Monit service check enabled state. Call monit_reconfigure after."""
    return get_client().monit.toggle_service(uuid, enabled).model_dump(exclude_none=True)


# ---- Tests -------------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def monit_search_tests(search_phrase: str = "") -> dict[str, Any]:
    """Search Monit service tests."""
    result = get_client().monit.search_tests(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": [r.model_dump(exclude_none=True) for r in result.rows]}


@mcp.tool()
@handle_opnsense_errors
def monit_add_test(data_json: str) -> dict[str, Any]:
    """Create a Monit test. data_json: JSON with test fields. Call monit_reconfigure after."""
    test = MonitTest.model_validate(json.loads(data_json))
    return get_client().monit.add_test(test).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def monit_del_test(uuid: str) -> dict[str, Any]:
    """Delete a Monit test by UUID. Call monit_reconfigure after."""
    return get_client().monit.del_test(uuid).model_dump(exclude_none=True)


# ---- Alerts ------------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def monit_search_alerts(search_phrase: str = "") -> dict[str, Any]:
    """Search Monit alert configurations."""
    result = get_client().monit.search_alerts(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": [r.model_dump(exclude_none=True) for r in result.rows]}


@mcp.tool()
@handle_opnsense_errors
def monit_add_alert(data_json: str) -> dict[str, Any]:
    """Create a Monit alert. data_json: JSON with alert fields. Call monit_reconfigure after."""
    alert = MonitAlert.model_validate(json.loads(data_json))
    return get_client().monit.add_alert(alert).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def monit_del_alert(uuid: str) -> dict[str, Any]:
    """Delete a Monit alert by UUID. Call monit_reconfigure after."""
    return get_client().monit.del_alert(uuid).model_dump(exclude_none=True)


# ---- Status / Service --------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def monit_get_status(fmt: str = "xml") -> dict[str, Any]:
    """Get Monit monitoring status. fmt: xml (default) or json."""
    return get_client().monit.get_status(fmt)


@mcp.tool()
@handle_opnsense_errors
def monit_start() -> dict[str, Any]:
    """Start the Monit service."""
    return get_client().monit.start().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def monit_stop() -> dict[str, Any]:
    """Stop the Monit service."""
    return get_client().monit.stop().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def monit_restart() -> dict[str, Any]:
    """Restart the Monit service."""
    return get_client().monit.restart().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def monit_reconfigure() -> dict[str, Any]:
    """Apply pending Monit configuration changes. Call after any mutation."""
    return get_client().monit.reconfigure().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def monit_status() -> dict[str, Any]:
    """Get Monit daemon service status."""
    return get_client().monit.status()
