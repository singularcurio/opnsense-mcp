from __future__ import annotations

import json
from typing import Any

from opnsense_mcp.context import get_client
from opnsense_mcp.errors import handle_opnsense_errors
from opnsense_mcp.tools.registry import get_module_registrar
mcp = get_module_registrar(__name__)

# ---- System ------------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def diagnostics_system_information() -> dict[str, Any]:
    """Get system information (hostname, version, CPU, memory, uptime, etc.)."""
    return get_client().diagnostics.system_information()


@mcp.tool()
@handle_opnsense_errors
def diagnostics_system_memory() -> dict[str, Any]:
    """Get detailed memory usage statistics."""
    return get_client().diagnostics.system_memory()


@mcp.tool()
@handle_opnsense_errors
def diagnostics_system_disk() -> dict[str, Any]:
    """Get disk usage statistics."""
    return get_client().diagnostics.system_disk()


@mcp.tool()
@handle_opnsense_errors
def diagnostics_system_resources() -> dict[str, Any]:
    """Get system resource utilization (CPU, memory, swap)."""
    return get_client().diagnostics.system_resources()


@mcp.tool()
@handle_opnsense_errors
def diagnostics_system_temperature() -> dict[str, Any]:
    """Get system temperature sensors."""
    return get_client().diagnostics.system_temperature()


@mcp.tool()
@handle_opnsense_errors
def diagnostics_system_time() -> dict[str, Any]:
    """Get current system time and NTP status."""
    return get_client().diagnostics.system_time()


@mcp.tool()
@handle_opnsense_errors
def diagnostics_get_activity() -> dict[str, Any]:
    """Get current system activity (top-like output)."""
    return get_client().diagnostics.get_activity()


# ---- Firewall states & logs --------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def diagnostics_get_firewall_log() -> dict[str, Any]:
    """Get recent firewall log entries."""
    return get_client().diagnostics.get_firewall_log()


@mcp.tool()
@handle_opnsense_errors
def diagnostics_get_pf_states() -> dict[str, Any]:
    """Get current pf firewall state table."""
    return get_client().diagnostics.get_pf_states()


@mcp.tool()
@handle_opnsense_errors
def diagnostics_get_pf_statistics(section: str | None = None) -> dict[str, Any]:
    """Get pf statistics. section: optional section filter (e.g. 'timeouts', 'memory')."""
    return get_client().diagnostics.get_pf_statistics(section)


@mcp.tool()
@handle_opnsense_errors
def diagnostics_get_firewall_stats() -> dict[str, Any]:
    """Get firewall statistics counters."""
    return get_client().diagnostics.get_firewall_stats()


@mcp.tool()
@handle_opnsense_errors
def diagnostics_query_states(data_json: str = "{}") -> dict[str, Any]:
    """Query firewall states with optional filters. data_json: JSON filter object."""
    return get_client().diagnostics.query_states(json.loads(data_json))


@mcp.tool()
@handle_opnsense_errors
def diagnostics_flush_states() -> dict[str, Any]:
    """Flush all firewall state table entries."""
    return get_client().diagnostics.flush_states().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def diagnostics_kill_states(data_json: str = "{}") -> dict[str, Any]:
    """Kill specific firewall states matching filter. data_json: JSON filter object."""
    return get_client().diagnostics.kill_states(json.loads(data_json)).model_dump(exclude_none=True)


# ---- Interface / ARP / NDP ---------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def diagnostics_get_arp() -> dict[str, Any]:
    """Get ARP table entries."""
    return get_client().diagnostics.get_arp()


@mcp.tool()
@handle_opnsense_errors
def diagnostics_flush_arp() -> dict[str, Any]:
    """Flush the ARP table."""
    return get_client().diagnostics.flush_arp().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def diagnostics_get_ndp() -> dict[str, Any]:
    """Get NDP (IPv6 neighbor discovery) table entries."""
    return get_client().diagnostics.get_ndp()


@mcp.tool()
@handle_opnsense_errors
def diagnostics_get_routes() -> dict[str, Any]:
    """Get the current kernel routing table."""
    return get_client().diagnostics.get_routes()


@mcp.tool()
@handle_opnsense_errors
def diagnostics_get_interface_config() -> dict[str, Any]:
    """Get interface configuration details."""
    return get_client().diagnostics.get_interface_config()


@mcp.tool()
@handle_opnsense_errors
def diagnostics_get_interface_names() -> dict[str, Any]:
    """Get a mapping of interface names to descriptions."""
    return get_client().diagnostics.get_interface_names()


@mcp.tool()
@handle_opnsense_errors
def diagnostics_get_interface_statistics() -> dict[str, Any]:
    """Get per-interface packet and byte counters."""
    return get_client().diagnostics.get_interface_statistics()


@mcp.tool()
@handle_opnsense_errors
def diagnostics_get_vip_status() -> dict[str, Any]:
    """Get CARP/VIP status for all virtual IPs."""
    return get_client().diagnostics.get_vip_status()


@mcp.tool()
@handle_opnsense_errors
def diagnostics_get_protocol_statistics() -> dict[str, Any]:
    """Get per-protocol network statistics (netstat -s)."""
    return get_client().diagnostics.get_protocol_statistics()


# ---- Traffic -----------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def diagnostics_traffic_interface() -> dict[str, Any]:
    """Get current traffic rates per interface."""
    return get_client().diagnostics.traffic_interface()


@mcp.tool()
@handle_opnsense_errors
def diagnostics_traffic_top(interfaces: str) -> dict[str, Any]:
    """Get top talkers on specified interfaces. interfaces: comma-separated list."""
    return get_client().diagnostics.traffic_top(interfaces)
