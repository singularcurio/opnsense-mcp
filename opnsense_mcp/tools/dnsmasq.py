from __future__ import annotations

import json
from typing import Any

from opnsense_py.models.base import SearchRequest
from opnsense_py.models.dnsmasq import DnsmasqDomainOverride, DnsmasqHost

from opnsense_mcp.context import get_client
from opnsense_mcp.errors import handle_opnsense_errors
from opnsense_mcp.tools.registry import get_module_registrar
mcp = get_module_registrar(__name__)

# ---- Hosts -------------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def dnsmasq_search_hosts(search_phrase: str = "") -> dict[str, Any]:
    """Search dnsmasq DNS/DHCP host entries."""
    result = get_client().dnsmasq.search_hosts(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": [r.model_dump(exclude_none=True) for r in result.rows]}


@mcp.tool()
@handle_opnsense_errors
def dnsmasq_get_host(uuid: str) -> dict[str, Any]:
    """Get a dnsmasq host entry by UUID."""
    return get_client().dnsmasq.get_host(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def dnsmasq_add_host(data_json: str) -> dict[str, Any]:
    """Create a dnsmasq host entry. data_json: JSON with host fields.
    Call dnsmasq_reconfigure after."""
    host = DnsmasqHost.model_validate(json.loads(data_json))
    return get_client().dnsmasq.add_host(host).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def dnsmasq_set_host(uuid: str, data_json: str) -> dict[str, Any]:
    """Update a dnsmasq host entry. data_json: JSON with host fields.
    Call dnsmasq_reconfigure after."""
    host = DnsmasqHost.model_validate(json.loads(data_json))
    return get_client().dnsmasq.set_host(uuid, host).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def dnsmasq_del_host(uuid: str) -> dict[str, Any]:
    """Delete a dnsmasq host entry by UUID. Call dnsmasq_reconfigure after."""
    return get_client().dnsmasq.del_host(uuid).model_dump(exclude_none=True)


# ---- Domains -----------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def dnsmasq_search_domains(search_phrase: str = "") -> dict[str, Any]:
    """Search dnsmasq domain overrides."""
    result = get_client().dnsmasq.search_domains(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": [r.model_dump(exclude_none=True) for r in result.rows]}


@mcp.tool()
@handle_opnsense_errors
def dnsmasq_add_domain(data_json: str) -> dict[str, Any]:
    """Create a dnsmasq domain override. data_json: JSON with domain fields.
    Call dnsmasq_reconfigure after."""
    domain = DnsmasqDomainOverride.model_validate(json.loads(data_json))
    return get_client().dnsmasq.add_domain(domain).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def dnsmasq_del_domain(uuid: str) -> dict[str, Any]:
    """Delete a dnsmasq domain override by UUID. Call dnsmasq_reconfigure after."""
    return get_client().dnsmasq.del_domain(uuid).model_dump(exclude_none=True)


# ---- Leases ------------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def dnsmasq_search_leases() -> dict[str, Any]:
    """List current DHCP leases from dnsmasq."""
    return get_client().dnsmasq.search_leases()


# ---- Service -----------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def dnsmasq_start() -> dict[str, Any]:
    """Start the dnsmasq service."""
    return get_client().dnsmasq.start().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def dnsmasq_stop() -> dict[str, Any]:
    """Stop the dnsmasq service."""
    return get_client().dnsmasq.stop().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def dnsmasq_restart() -> dict[str, Any]:
    """Restart the dnsmasq service."""
    return get_client().dnsmasq.restart().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def dnsmasq_reconfigure() -> dict[str, Any]:
    """Apply pending dnsmasq configuration changes. Call after any mutation."""
    return get_client().dnsmasq.reconfigure().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def dnsmasq_status() -> dict[str, Any]:
    """Get dnsmasq service status."""
    return get_client().dnsmasq.status()
