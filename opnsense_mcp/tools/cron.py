from __future__ import annotations

from typing import Any

from opnsense_py.models.base import SearchRequest
from opnsense_py.models.cron import CronJob

from opnsense_mcp.context import get_client
from opnsense_mcp.errors import handle_opnsense_errors
from opnsense_mcp.tools.registry import get_module_registrar
mcp = get_module_registrar(__name__)


@mcp.tool()
@handle_opnsense_errors
def cron_search_jobs(search_phrase: str = "") -> dict[str, Any]:
    """Search cron jobs. Returns total count and list of job objects."""
    result = get_client().cron.search_jobs(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": [r.model_dump(exclude_none=True) for r in result.rows]}


@mcp.tool()
@handle_opnsense_errors
def cron_get_job(uuid: str) -> dict[str, Any]:
    """Get a single cron job by UUID."""
    return get_client().cron.get_job(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def cron_add_job(
    command: str,
    minutes: str = "*",
    hours: str = "*",
    days: str = "*",
    months: str = "*",
    weekdays: str = "*",
    who: str = "root",
    parameters: str = "",
    description: str = "",
    enabled: str = "1",
) -> dict[str, Any]:
    """Create a new cron job. Returns the new UUID on success.

    enabled: "1" = enabled, "0" = disabled.
    """
    job = CronJob(
        command=command,
        minutes=minutes,
        hours=hours,
        days=days,
        months=months,
        weekdays=weekdays,
        who=who,
        parameters=parameters or None,
        description=description or None,
        enabled=enabled,
    )
    return get_client().cron.add_job(job).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def cron_set_job(
    uuid: str,
    command: str | None = None,
    minutes: str | None = None,
    hours: str | None = None,
    days: str | None = None,
    months: str | None = None,
    weekdays: str | None = None,
    who: str | None = None,
    parameters: str | None = None,
    description: str | None = None,
    enabled: str | None = None,
) -> dict[str, Any]:
    """Update an existing cron job. Only provided fields are changed."""
    job = CronJob(
        command=command,
        minutes=minutes,
        hours=hours,
        days=days,
        months=months,
        weekdays=weekdays,
        who=who,
        parameters=parameters,
        description=description,
        enabled=enabled,
    )
    return get_client().cron.set_job(uuid, job).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def cron_del_job(uuid: str) -> dict[str, Any]:
    """Delete a cron job by UUID."""
    return get_client().cron.del_job(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def cron_toggle_job(uuid: str, enabled: bool | None = None) -> dict[str, Any]:
    """Toggle a cron job enabled state. Pass enabled=True/False to force a specific state."""
    return get_client().cron.toggle_job(uuid, enabled=enabled).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def cron_reconfigure() -> dict[str, Any]:
    """Apply pending cron configuration changes (writes crontab). Call after any mutation."""
    return get_client().cron.reconfigure().model_dump(exclude_none=True)
