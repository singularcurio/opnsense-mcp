from __future__ import annotations

import json
from typing import Any

from opnsense_py.models.base import SearchRequest
from opnsense_py.models.unbound import HostAlias, HostOverride, UnboundAcl, UnboundDnsbl, UnboundDot

from opnsense_mcp.context import get_client
from opnsense_mcp.errors import handle_opnsense_errors
from opnsense_mcp.tools.registry import get_module_registrar
mcp = get_module_registrar(__name__)

# ---- Global settings ---------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def unbound_get_settings() -> dict[str, Any]:
    """Get global Unbound DNS resolver settings."""
    return get_client().unbound.get()


@mcp.tool()
@handle_opnsense_errors
def unbound_set_settings(data_json: str) -> dict[str, Any]:
    """Update global Unbound settings. data_json: JSON object with settings fields."""
    return get_client().unbound.set(json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def unbound_get_nameservers() -> dict[str, Any]:
    """Get configured nameservers."""
    return get_client().unbound.get_nameservers()


@mcp.tool()
@handle_opnsense_errors
def unbound_update_blocklist() -> dict[str, Any]:
    """Trigger an update of the DNS blocklist."""
    return get_client().unbound.update_blocklist().model_dump(exclude_none=True)


# ---- Host overrides ----------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def unbound_search_host_overrides(search_phrase: str = "") -> dict[str, Any]:
    """Search DNS host overrides."""
    result = get_client().unbound.search_host_overrides(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": [r.model_dump(exclude_none=True) for r in result.rows]}


@mcp.tool()
@handle_opnsense_errors
def unbound_get_host_override(uuid: str) -> dict[str, Any]:
    """Get a host override by UUID."""
    return get_client().unbound.get_host_override(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def unbound_add_host_override(
    hostname: str,
    domain: str,
    server: str,
    enabled: str = "1",
    rr: str | None = None,
    mxprio: int | None = None,
    mx: str | None = None,
    ttl: int | None = None,
    txtdata: str | None = None,
    addptr: str | None = None,
    description: str | None = None,
) -> dict[str, Any]:
    """Create a DNS host override. Call unbound_reconfigure after."""
    host = HostOverride(
        hostname=hostname, domain=domain, server=server, enabled=enabled,
        rr=rr, mxprio=mxprio, mx=mx, ttl=ttl, txtdata=txtdata,
        addptr=addptr, description=description,
    )
    return get_client().unbound.add_host_override(host).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def unbound_set_host_override(
    uuid: str,
    hostname: str | None = None,
    domain: str | None = None,
    server: str | None = None,
    enabled: str | None = None,
    rr: str | None = None,
    mxprio: int | None = None,
    mx: str | None = None,
    ttl: int | None = None,
    txtdata: str | None = None,
    addptr: str | None = None,
    description: str | None = None,
) -> dict[str, Any]:
    """Update a DNS host override. Call unbound_reconfigure after."""
    host = HostOverride(
        hostname=hostname, domain=domain, server=server, enabled=enabled,
        rr=rr, mxprio=mxprio, mx=mx, ttl=ttl, txtdata=txtdata,
        addptr=addptr, description=description,
    )
    return get_client().unbound.set_host_override(uuid, host).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def unbound_del_host_override(uuid: str) -> dict[str, Any]:
    """Delete a DNS host override by UUID. Call unbound_reconfigure after."""
    return get_client().unbound.del_host_override(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def unbound_toggle_host_override(uuid: str, enabled: bool | None = None) -> dict[str, Any]:
    """Toggle a host override enabled state. Call unbound_reconfigure after."""
    return get_client().unbound.toggle_host_override(uuid, enabled).model_dump(exclude_none=True)


# ---- Host aliases ------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def unbound_search_host_aliases(search_phrase: str = "") -> dict[str, Any]:
    """Search DNS host aliases."""
    result = get_client().unbound.search_host_aliases(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": [r.model_dump(exclude_none=True) for r in result.rows]}


@mcp.tool()
@handle_opnsense_errors
def unbound_add_host_alias(
    host: str,
    hostname: str,
    domain: str,
    enabled: str = "1",
    description: str | None = None,
) -> dict[str, Any]:
    """Create a DNS host alias (CNAME-like). host: UUID of the target host override.
    Call unbound_reconfigure after."""
    alias = HostAlias(host=host, hostname=hostname, domain=domain, enabled=enabled, description=description)
    return get_client().unbound.add_host_alias(alias).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def unbound_del_host_alias(uuid: str) -> dict[str, Any]:
    """Delete a DNS host alias by UUID. Call unbound_reconfigure after."""
    return get_client().unbound.del_host_alias(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def unbound_toggle_host_alias(uuid: str, enabled: bool | None = None) -> dict[str, Any]:
    """Toggle a host alias enabled state. Call unbound_reconfigure after."""
    return get_client().unbound.toggle_host_alias(uuid, enabled).model_dump(exclude_none=True)


# ---- ACLs --------------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def unbound_search_acls(search_phrase: str = "") -> dict[str, Any]:
    """Search Unbound access control lists."""
    result = get_client().unbound.search_acls(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": [r.model_dump(exclude_none=True) for r in result.rows]}


@mcp.tool()
@handle_opnsense_errors
def unbound_add_acl(
    name: str,
    action: str,
    networks: str,
    enabled: str = "1",
    description: str | None = None,
) -> dict[str, Any]:
    """Create an Unbound ACL. action: allow, deny, refuse, allow_snoop, etc.
    Call unbound_reconfigure after."""
    acl = UnboundAcl(name=name, action=action, networks=networks, enabled=enabled, description=description)
    return get_client().unbound.add_acl(acl).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def unbound_del_acl(uuid: str) -> dict[str, Any]:
    """Delete an Unbound ACL by UUID. Call unbound_reconfigure after."""
    return get_client().unbound.del_acl(uuid).model_dump(exclude_none=True)


# ---- Forwards ----------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def unbound_search_forwards(search_phrase: str = "") -> dict[str, Any]:
    """Search Unbound DNS forwards (DoT / upstream resolvers)."""
    result = get_client().unbound.search_forwards(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": [r.model_dump(exclude_none=True) for r in result.rows]}


@mcp.tool()
@handle_opnsense_errors
def unbound_add_forward(
    server: str,
    enabled: str = "1",
    type: str | None = None,
    domain: str | None = None,
    port: str | None = None,
    verify: str | None = None,
    forward_tcp_upstream: str | None = None,
    forward_first: str | None = None,
    description: str | None = None,
) -> dict[str, Any]:
    """Add an Unbound DNS forward or DoT server. Call unbound_reconfigure after."""
    dot = UnboundDot(
        server=server, enabled=enabled, type=type, domain=domain, port=port,
        verify=verify, forward_tcp_upstream=forward_tcp_upstream,
        forward_first=forward_first, description=description,
    )
    return get_client().unbound.add_forward(dot).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def unbound_del_forward(uuid: str) -> dict[str, Any]:
    """Delete an Unbound forward by UUID. Call unbound_reconfigure after."""
    return get_client().unbound.del_forward(uuid).model_dump(exclude_none=True)


# ---- DNSBL -------------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def unbound_search_dnsbl(search_phrase: str = "") -> dict[str, Any]:
    """Search Unbound DNS blocklist entries."""
    result = get_client().unbound.search_dnsbl(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": [r.model_dump(exclude_none=True) for r in result.rows]}


@mcp.tool()
@handle_opnsense_errors
def unbound_add_dnsbl(
    type: str,
    enabled: str = "1",
    lists: str | None = None,
    allowlists: str | None = None,
    blocklists: str | None = None,
    wildcards: str | None = None,
    source_nets: str | None = None,
    address: str | None = None,
    nxdomain: str | None = None,
    cache_ttl: int | None = None,
    description: str | None = None,
) -> dict[str, Any]:
    """Add an Unbound DNS blocklist. Call unbound_reconfigure after."""
    bl = UnboundDnsbl(
        type=type, enabled=enabled, lists=lists, allowlists=allowlists,
        blocklists=blocklists, wildcards=wildcards, source_nets=source_nets,
        address=address, nxdomain=nxdomain, cache_ttl=cache_ttl, description=description,
    )
    return get_client().unbound.add_dnsbl(bl).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def unbound_del_dnsbl(uuid: str) -> dict[str, Any]:
    """Delete an Unbound DNS blocklist entry by UUID. Call unbound_reconfigure after."""
    return get_client().unbound.del_dnsbl(uuid).model_dump(exclude_none=True)


# ---- Diagnostics -------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def unbound_dump_cache() -> dict[str, Any]:
    """Dump the Unbound DNS cache contents."""
    return get_client().unbound.dump_cache()


@mcp.tool()
@handle_opnsense_errors
def unbound_diag_stats() -> dict[str, Any]:
    """Get Unbound resolver statistics."""
    return get_client().unbound.diag_stats()


@mcp.tool()
@handle_opnsense_errors
def unbound_is_enabled() -> dict[str, Any]:
    """Check if Unbound is enabled."""
    return get_client().unbound.is_enabled()


# ---- Service -----------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def unbound_start() -> dict[str, Any]:
    """Start the Unbound DNS resolver service."""
    return get_client().unbound.start().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def unbound_stop() -> dict[str, Any]:
    """Stop the Unbound DNS resolver service."""
    return get_client().unbound.stop().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def unbound_restart() -> dict[str, Any]:
    """Restart the Unbound DNS resolver service."""
    return get_client().unbound.restart().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def unbound_reconfigure() -> dict[str, Any]:
    """Apply pending Unbound configuration changes. Call after any mutation."""
    return get_client().unbound.reconfigure().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def unbound_status() -> dict[str, Any]:
    """Get Unbound service status."""
    return get_client().unbound.status()
