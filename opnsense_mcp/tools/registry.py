from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable

# ---------------------------------------------------------------------------
# Read-only inference
# ---------------------------------------------------------------------------

# Tool name fragments (split on "_") that indicate a mutating operation.
# Anything NOT matching is considered read-only.
_MUTATING_WORDS: frozenset[str] = frozenset({
    # CRUD
    "add", "set", "del", "toggle",
    # Apply / rollback
    "reconfigure", "apply", "cancel", "revert", "savepoint", "flushreload",
    # Service lifecycle
    "start", "stop", "restart", "reboot", "poweroff", "halt",
    # Package / firmware
    "install", "remove", "lock", "unlock", "upgrade", "update",
    # Key / token generation
    "generate", "new",
    # Session management
    "connect", "disconnect", "logon", "logoff",
    # Data modification
    "save", "upload", "expire", "drop", "flush", "sync",
})


def _infer_readonly(tool_name: str) -> bool:
    """Return True if the tool name contains no mutating word fragments."""
    return not bool(frozenset(tool_name.split("_")) & _MUTATING_WORDS)


# ---------------------------------------------------------------------------
# Catalog entry
# ---------------------------------------------------------------------------


@dataclass
class CatalogEntry:
    fn: Callable[..., Any]
    name: str
    module: str
    description: str
    readonly: bool


_catalog: dict[str, CatalogEntry] = {}

# ---------------------------------------------------------------------------
# Per-module descriptions (shown by list_modules / describe_module)
# ---------------------------------------------------------------------------

MODULE_DESCRIPTIONS: dict[str, str] = {
    "auth": "Local users, groups, API keys, and privilege management",
    "captiveportal": "Captive portal zones, client sessions, and vouchers",
    "core": "System status, services, tunables, and configuration backups",
    "cron": "Scheduled cron job management",
    "dhcrelay": "DHCP relay destinations and relay interfaces",
    "diagnostics": "Read-only system diagnostics: firewall states/logs, ARP/NDP, interfaces, traffic",
    "docs": "Search and read OPNsense documentation markdown files",
    "dnsmasq": "DNSmasq host overrides, domain overrides, and DHCP leases",
    "firewall": "Firewall filter rules, aliases, NAT rules (DNAT/SNAT/NPT/1:1), and categories",
    "firmware": "Firmware updates, package management, health checks, and reboot/poweroff",
    "haproxy": "HAProxy load balancer: frontends, backends, servers, ACLs, and health checks",
    "hostdiscovery": "Passive host discovery scanning and discovered host list",
    "ids": "Suricata IDS/IPS: policies, rules, alerts, and service control",
    "interfaces": "Network interfaces: bridges, GIF/GRE tunnels, LAGG, loopbacks, VIPs, VLANs, VXLANs",
    "ipsec": "IPsec VPN: connections, pools, sessions, key pairs, and PSKs",
    "kea": "Kea DHCPv4/v6: subnets, reservations, leases, and service control",
    "monit": "Monit service monitoring: checks, tests, alerts, and daemon status",
    "ntpd": "NTP daemon status: GPS sources, peer metadata",
    "openvpn": "OpenVPN instances, static keys, client overwrites, and session management",
    "radvd": "Router Advertisement daemon entries and service control",
    "routes": "Static routes and gateway status",
    "routing": "Gateway definitions (add/update/delete gateways)",
    "syslog": "Remote syslog destinations and syslogd service control",
    "trafficshaper": "Traffic shaper pipes, queues, rules, and statistics",
    "trust": "PKI: certificate authorities, certificates, and CRLs",
    "unbound": "Unbound DNS resolver: host overrides, ACLs, DNSBL, DoT, forwards, diagnostics",
    "wireguard": "WireGuard VPN servers, peers, key pairs, and service control",
}

# ---------------------------------------------------------------------------
# ModuleRegistrar — drop-in replacement for FastMCP used by tool files
# ---------------------------------------------------------------------------


class ModuleRegistrar:
    """Mimics FastMCP's .tool() decorator interface.

    Instead of registering functions with FastMCP immediately, it stores them
    in the global catalog so they can be loaded on demand via load_tool().
    """

    def __init__(self, module: str) -> None:
        self.module = module

    def tool(
        self,
        name: str | None = None,
        title: str | None = None,
        description: str | None = None,
        readonly: bool | None = None,
        **_kwargs: Any,
    ) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
        def decorator(fn: Callable[..., Any]) -> Callable[..., Any]:
            tool_name = name or fn.__name__
            tool_desc = (description or fn.__doc__ or "").strip()
            is_readonly = readonly if readonly is not None else _infer_readonly(tool_name)
            _catalog[tool_name] = CatalogEntry(
                fn=fn,
                name=tool_name,
                module=self.module,
                description=tool_desc,
                readonly=is_readonly,
            )
            return fn

        return decorator


def get_module_registrar(dotted_name: str) -> ModuleRegistrar:
    """Return a ModuleRegistrar for the given dotted module name.

    Usage in tool files (replaces ``from opnsense_mcp.server import mcp``)::

        from opnsense_mcp.tools.registry import get_module_registrar
        mcp = get_module_registrar(__name__)
    """
    module = dotted_name.rsplit(".", 1)[-1]
    return ModuleRegistrar(module)
