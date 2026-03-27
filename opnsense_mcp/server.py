from __future__ import annotations

import os

from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    "opnsense",
    instructions=(
        "Tools for managing an OPNsense firewall. "
        "Start with list_modules() to discover available capabilities, "
        "then describe_module() to see tools in a module, "
        "then load_module() or load_tool() to make them available. "
        "After loading, write operations (add/set/del/toggle) require a "
        "follow-up reconfigure call to apply changes."
    ),
)

# Discovery meta-tools are always available — import first so mcp is defined.
from opnsense_mcp.tools import discovery  # noqa: E402, F401

# Import all tool modules to populate the catalog (registry.py).
# These do NOT register with FastMCP — they use ModuleRegistrar instead.
from opnsense_mcp.tools import (  # noqa: E402, F401
    auth,
    captiveportal,
    core,
    docs,
    cron,
    dhcrelay,
    diagnostics,
    dnsmasq,
    firewall,
    firmware,
    haproxy,
    hostdiscovery,
    ids,
    interfaces,
    ipsec,
    kea,
    monit,
    ntpd,
    openvpn,
    radvd,
    routes,
    routing,
    syslog,
    trafficshaper,
    trust,
    unbound,
    wireguard,
)

# Preload configured modules at startup so they appear in the initial tool list.
# Override with OPNSENSE_MCP_PRELOAD=module1,module2 or set to "" to disable.
_PRELOAD_DEFAULT = (
    "core,cron,diagnostics,docs,firewall,hostdiscovery,interfaces,"
    "kea,ntpd,radvd,routes,routing,syslog,unbound"
)
_preload_env = os.environ.get("OPNSENSE_MCP_PRELOAD", _PRELOAD_DEFAULT)
if _preload_env.strip():
    discovery.preload_modules([m.strip() for m in _preload_env.split(",") if m.strip()])


def main() -> None:
    transport = os.environ.get("OPNSENSE_MCP_TRANSPORT", "stdio")
    if transport == "sse":
        mcp.settings.host = os.environ.get("OPNSENSE_MCP_HOST", "127.0.0.1")
        mcp.settings.port = int(os.environ.get("OPNSENSE_MCP_PORT", "8000"))
    mcp.run(transport=transport)  # type: ignore[arg-type]


if __name__ == "__main__":
    main()
