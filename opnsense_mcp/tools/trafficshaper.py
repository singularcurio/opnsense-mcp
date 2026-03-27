from __future__ import annotations

import json
from typing import Any

from opnsense_py.models.base import SearchRequest

from opnsense_mcp.context import get_client
from opnsense_mcp.errors import handle_opnsense_errors
from opnsense_mcp.tools.registry import get_module_registrar
mcp = get_module_registrar(__name__)

# ---- Pipes -------------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def trafficshaper_search_pipes(search_phrase: str = "") -> dict[str, Any]:
    """Search traffic shaper pipes."""
    result = get_client().trafficshaper.search_pipes(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": [r.model_dump(exclude_none=True) for r in result.rows]}


@mcp.tool()
@handle_opnsense_errors
def trafficshaper_get_pipe(uuid: str) -> dict[str, Any]:
    """Get a traffic shaper pipe by UUID."""
    return get_client().trafficshaper.get_pipe(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def trafficshaper_add_pipe(data_json: str) -> dict[str, Any]:
    """Create a traffic shaper pipe. data_json: JSON with pipe fields (bandwidth, description, etc.).
    Call trafficshaper_reconfigure after."""
    from opnsense_py.models.trafficshaper import ShaperPipe
    pipe = ShaperPipe.model_validate(json.loads(data_json))
    return get_client().trafficshaper.add_pipe(pipe).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def trafficshaper_del_pipe(uuid: str) -> dict[str, Any]:
    """Delete a traffic shaper pipe by UUID. Call trafficshaper_reconfigure after."""
    return get_client().trafficshaper.del_pipe(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def trafficshaper_toggle_pipe(uuid: str, enabled: bool | None = None) -> dict[str, Any]:
    """Toggle a traffic shaper pipe enabled state. Call trafficshaper_reconfigure after."""
    return get_client().trafficshaper.toggle_pipe(uuid, enabled).model_dump(exclude_none=True)


# ---- Queues ------------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def trafficshaper_search_queues(search_phrase: str = "") -> dict[str, Any]:
    """Search traffic shaper queues."""
    result = get_client().trafficshaper.search_queues(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": [r.model_dump(exclude_none=True) for r in result.rows]}


@mcp.tool()
@handle_opnsense_errors
def trafficshaper_add_queue(data_json: str) -> dict[str, Any]:
    """Create a traffic shaper queue. data_json: JSON with queue fields.
    Call trafficshaper_reconfigure after."""
    from opnsense_py.models.trafficshaper import ShaperQueue
    queue = ShaperQueue.model_validate(json.loads(data_json))
    return get_client().trafficshaper.add_queue(queue).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def trafficshaper_del_queue(uuid: str) -> dict[str, Any]:
    """Delete a traffic shaper queue by UUID. Call trafficshaper_reconfigure after."""
    return get_client().trafficshaper.del_queue(uuid).model_dump(exclude_none=True)


# ---- Rules -------------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def trafficshaper_search_rules(search_phrase: str = "") -> dict[str, Any]:
    """Search traffic shaper rules."""
    result = get_client().trafficshaper.search_rules(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": [r.model_dump(exclude_none=True) for r in result.rows]}


@mcp.tool()
@handle_opnsense_errors
def trafficshaper_add_rule(data_json: str) -> dict[str, Any]:
    """Create a traffic shaper rule. data_json: JSON with rule fields.
    Call trafficshaper_reconfigure after."""
    from opnsense_py.models.trafficshaper import ShaperRule
    rule = ShaperRule.model_validate(json.loads(data_json))
    return get_client().trafficshaper.add_rule(rule).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def trafficshaper_del_rule(uuid: str) -> dict[str, Any]:
    """Delete a traffic shaper rule by UUID. Call trafficshaper_reconfigure after."""
    return get_client().trafficshaper.del_rule(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def trafficshaper_toggle_rule(uuid: str, enabled: bool | None = None) -> dict[str, Any]:
    """Toggle a traffic shaper rule enabled state. Call trafficshaper_reconfigure after."""
    return get_client().trafficshaper.toggle_rule(uuid, enabled).model_dump(exclude_none=True)


# ---- Service -----------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def trafficshaper_statistics() -> dict[str, Any]:
    """Get traffic shaper pipe/queue statistics."""
    return get_client().trafficshaper.statistics()


@mcp.tool()
@handle_opnsense_errors
def trafficshaper_reconfigure() -> dict[str, Any]:
    """Apply pending traffic shaper configuration changes. Call after any mutation."""
    return get_client().trafficshaper.reconfigure().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def trafficshaper_flushreload() -> dict[str, Any]:
    """Flush and reload traffic shaper rules immediately."""
    return get_client().trafficshaper.flushreload().model_dump(exclude_none=True)
