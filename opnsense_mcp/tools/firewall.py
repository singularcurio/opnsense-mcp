from __future__ import annotations

import json
from typing import Any

from opnsense_py.models.base import SearchRequest
from opnsense_py.models.firewall import (
    DNatRule,
    FilterRule,
    FirewallAlias,
    FirewallCategory,
    NPTRule,
    OneToOneRule,
    SNatRule,
)

from opnsense_mcp.context import get_client
from opnsense_mcp.errors import handle_opnsense_errors
from opnsense_mcp.tools.registry import get_module_registrar
mcp = get_module_registrar(__name__)

# ---- Savepoint / apply -------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def firewall_create_savepoint(controller: str = "filter") -> dict[str, Any]:
    """Create a firewall savepoint. Returns {"revision": "..."}.

    Use the revision token with firewall_apply and firewall_cancel_rollback.
    The server auto-reverts after 60 s unless cancel_rollback is called.
    controller: "filter" (default), "d_nat", "source_nat", etc.
    """
    with get_client().firewall.savepoint(controller) as revision:
        return {"revision": revision}


@mcp.tool()
@handle_opnsense_errors
def firewall_apply(rollback_revision: str | None = None, controller: str = "filter") -> dict[str, Any]:
    """Apply pending firewall changes. Pass rollback_revision to make a savepoint permanent."""
    return get_client().firewall.apply(rollback_revision, controller).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def firewall_cancel_rollback(rollback_revision: str, controller: str = "filter") -> dict[str, Any]:
    """Cancel a scheduled rollback, making the savepoint changes permanent."""
    return get_client().firewall.cancel_rollback(rollback_revision, controller).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def firewall_revert(revision: str, controller: str = "filter") -> dict[str, Any]:
    """Revert firewall configuration to a previously saved revision."""
    return get_client().firewall.revert(revision, controller).model_dump(exclude_none=True)


# ---- Aliases -----------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def firewall_search_aliases(search_phrase: str = "") -> dict[str, Any]:
    """Search firewall aliases."""
    result = get_client().firewall.search_aliases(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": [r.model_dump(exclude_none=True) for r in result.rows]}


@mcp.tool()
@handle_opnsense_errors
def firewall_get_alias(uuid: str) -> dict[str, Any]:
    """Get a firewall alias by UUID."""
    return get_client().firewall.get_alias(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def firewall_add_alias(
    name: str,
    type: str,
    content: str = "",
    enabled: str = "1",
    proto: str | None = None,
    interface: str | None = None,
    counters: str | None = None,
    updatefreq: str | None = None,
    categories: str | None = None,
    description: str | None = None,
) -> dict[str, Any]:
    """Create a firewall alias. type: host, network, port, url, urltable, geoip, etc.
    content: newline-separated list of values."""
    alias = FirewallAlias(
        name=name, type=type, content=content or None, enabled=enabled,
        proto=proto, interface=interface, counters=counters,
        updatefreq=updatefreq, categories=categories, description=description,
    )
    return get_client().firewall.add_alias(alias).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def firewall_set_alias(
    uuid: str,
    name: str | None = None,
    type: str | None = None,
    content: str | None = None,
    enabled: str | None = None,
    proto: str | None = None,
    interface: str | None = None,
    counters: str | None = None,
    updatefreq: str | None = None,
    categories: str | None = None,
    description: str | None = None,
) -> dict[str, Any]:
    """Update a firewall alias."""
    alias = FirewallAlias(
        name=name, type=type, content=content, enabled=enabled,
        proto=proto, interface=interface, counters=counters,
        updatefreq=updatefreq, categories=categories, description=description,
    )
    return get_client().firewall.set_alias(uuid, alias).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def firewall_del_alias(uuid: str) -> dict[str, Any]:
    """Delete a firewall alias by UUID."""
    return get_client().firewall.del_alias(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def firewall_toggle_alias(uuid: str, enabled: bool | None = None) -> dict[str, Any]:
    """Toggle a firewall alias enabled state."""
    return get_client().firewall.toggle_alias(uuid, enabled).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def firewall_reconfigure_aliases() -> dict[str, Any]:
    """Apply pending alias changes."""
    return get_client().firewall.reconfigure_aliases().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def firewall_get_alias_uuid(name: str) -> dict[str, Any]:
    """Look up the UUID of an alias by name."""
    return get_client().firewall.get_alias_uuid(name)


@mcp.tool()
@handle_opnsense_errors
def firewall_alias_util_list(alias: str) -> dict[str, Any]:
    """List the current contents (resolved IPs/networks) of an alias."""
    return get_client().firewall.alias_util_list(alias)


@mcp.tool()
@handle_opnsense_errors
def firewall_alias_util_add(alias: str, data_json: str = "{}") -> dict[str, Any]:
    """Add an entry to an alias table. data_json: JSON object, e.g. {"address": "1.2.3.4"}."""
    return get_client().firewall.alias_util_add(alias, json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def firewall_alias_util_delete(alias: str, data_json: str = "{}") -> dict[str, Any]:
    """Remove an entry from an alias table. data_json: JSON object, e.g. {"address": "1.2.3.4"}."""
    return get_client().firewall.alias_util_delete(alias, json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def firewall_alias_util_flush(alias: str) -> dict[str, Any]:
    """Flush all entries from an alias table."""
    return get_client().firewall.alias_util_flush(alias).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def firewall_alias_util_aliases() -> dict[str, Any]:
    """List all available aliases (name and type)."""
    return get_client().firewall.alias_util_aliases()


@mcp.tool()
@handle_opnsense_errors
def firewall_list_countries() -> dict[str, Any]:
    """List available GeoIP country codes for use in aliases."""
    return get_client().firewall.list_countries()


@mcp.tool()
@handle_opnsense_errors
def firewall_export_aliases() -> dict[str, Any]:
    """Export all aliases as JSON."""
    return get_client().firewall.export_aliases()


# ---- Categories --------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def firewall_search_categories(search_phrase: str = "") -> dict[str, Any]:
    """Search firewall categories."""
    result = get_client().firewall.search_categories(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": [r.model_dump(exclude_none=True) for r in result.rows]}


@mcp.tool()
@handle_opnsense_errors
def firewall_add_category(name: str, color: str | None = None, auto: str | None = None) -> dict[str, Any]:
    """Create a firewall category."""
    return get_client().firewall.add_category(FirewallCategory(name=name, color=color, auto=auto)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def firewall_del_category(uuid: str) -> dict[str, Any]:
    """Delete a firewall category by UUID."""
    return get_client().firewall.del_category(uuid).model_dump(exclude_none=True)


# ---- Filter rules ------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def firewall_search_filter_rules(search_phrase: str = "") -> dict[str, Any]:
    """Search firewall filter rules."""
    result = get_client().firewall.search_filter_rules(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": [r.model_dump(exclude_none=True) for r in result.rows]}


@mcp.tool()
@handle_opnsense_errors
def firewall_get_filter_rule(uuid: str) -> dict[str, Any]:
    """Get a firewall filter rule by UUID."""
    return get_client().firewall.get_filter_rule(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def firewall_add_filter_rule(
    action: str,
    interface: str,
    enabled: str = "1",
    sequence: str | None = None,
    quick: str | None = None,
    direction: str | None = None,
    ipprotocol: str | None = None,
    protocol: str | None = None,
    source_net: str | None = None,
    source_not: str | None = None,
    source_port: str | None = None,
    destination_net: str | None = None,
    destination_not: str | None = None,
    destination_port: str | None = None,
    gateway: str | None = None,
    log: str | None = None,
    statetype: str | None = None,
    categories: str | None = None,
    description: str | None = None,
) -> dict[str, Any]:
    """Create a firewall filter rule. action: pass, block, reject. Call firewall_apply after."""
    rule = FilterRule(
        action=action, interface=interface, enabled=enabled, sequence=sequence,
        quick=quick, direction=direction, ipprotocol=ipprotocol, protocol=protocol,
        source_net=source_net, source_not=source_not, source_port=source_port,
        destination_net=destination_net, destination_not=destination_not,
        destination_port=destination_port, gateway=gateway, log=log,
        statetype=statetype, categories=categories, description=description,
    )
    return get_client().firewall.add_filter_rule(rule).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def firewall_set_filter_rule(
    uuid: str,
    action: str | None = None,
    interface: str | None = None,
    enabled: str | None = None,
    sequence: str | None = None,
    quick: str | None = None,
    direction: str | None = None,
    ipprotocol: str | None = None,
    protocol: str | None = None,
    source_net: str | None = None,
    source_not: str | None = None,
    source_port: str | None = None,
    destination_net: str | None = None,
    destination_not: str | None = None,
    destination_port: str | None = None,
    gateway: str | None = None,
    log: str | None = None,
    statetype: str | None = None,
    categories: str | None = None,
    description: str | None = None,
) -> dict[str, Any]:
    """Update a firewall filter rule. Call firewall_apply after."""
    rule = FilterRule(
        action=action, interface=interface, enabled=enabled, sequence=sequence,
        quick=quick, direction=direction, ipprotocol=ipprotocol, protocol=protocol,
        source_net=source_net, source_not=source_not, source_port=source_port,
        destination_net=destination_net, destination_not=destination_not,
        destination_port=destination_port, gateway=gateway, log=log,
        statetype=statetype, categories=categories, description=description,
    )
    return get_client().firewall.set_filter_rule(uuid, rule).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def firewall_del_filter_rule(uuid: str) -> dict[str, Any]:
    """Delete a firewall filter rule by UUID. Call firewall_apply after."""
    return get_client().firewall.del_filter_rule(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def firewall_toggle_filter_rule(uuid: str, enabled: bool | None = None) -> dict[str, Any]:
    """Toggle a filter rule enabled state. Call firewall_apply after."""
    return get_client().firewall.toggle_filter_rule(uuid, enabled).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def firewall_filter_rule_stats() -> dict[str, Any]:
    """Get per-rule packet/byte counters for filter rules."""
    return get_client().firewall.filter_rule_stats()


@mcp.tool()
@handle_opnsense_errors
def firewall_get_filter_interface_list() -> dict[str, Any]:
    """List interfaces available for filter rules."""
    return get_client().firewall.get_filter_interface_list()


# ---- Firewall groups ---------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def firewall_search_groups(search_phrase: str = "") -> dict[str, Any]:
    """Search firewall interface groups."""
    result = get_client().firewall.search_groups(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": result.rows}


@mcp.tool()
@handle_opnsense_errors
def firewall_get_group(uuid: str) -> dict[str, Any]:
    """Get a firewall interface group by UUID."""
    return get_client().firewall.get_group(uuid)


@mcp.tool()
@handle_opnsense_errors
def firewall_add_group(data_json: str) -> dict[str, Any]:
    """Create a firewall interface group. data_json: JSON object with group fields."""
    return get_client().firewall.add_group(json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def firewall_set_group(uuid: str, data_json: str) -> dict[str, Any]:
    """Update a firewall interface group. data_json: JSON object with group fields."""
    return get_client().firewall.set_group(uuid, json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def firewall_del_group(uuid: str) -> dict[str, Any]:
    """Delete a firewall interface group by UUID."""
    return get_client().firewall.del_group(uuid).model_dump(exclude_none=True)


# ---- DNAT (port forwarding) --------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def firewall_search_dnat_rules(search_phrase: str = "") -> dict[str, Any]:
    """Search destination NAT (port forward) rules."""
    result = get_client().firewall.search_dnat_rules(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": [r.model_dump(exclude_none=True) for r in result.rows]}


@mcp.tool()
@handle_opnsense_errors
def firewall_get_dnat_rule(uuid: str) -> dict[str, Any]:
    """Get a DNAT rule by UUID."""
    return get_client().firewall.get_dnat_rule(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def firewall_add_dnat_rule(
    interface: str,
    target: str,
    local_port: str,
    protocol: str | None = None,
    ipprotocol: str | None = None,
    sequence: str | None = None,
    disabled: str | None = None,
    nordr: str | None = None,
    log: str | None = None,
    natreflection: str | None = None,
    descr: str | None = None,
) -> dict[str, Any]:
    """Create a destination NAT (port forward) rule. Call firewall_apply after."""
    rule = DNatRule(
        interface=interface, target=target, local_port=local_port,
        protocol=protocol, ipprotocol=ipprotocol, sequence=sequence,
        disabled=disabled, nordr=nordr, log=log, natreflection=natreflection, descr=descr,
    )
    return get_client().firewall.add_dnat_rule(rule).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def firewall_del_dnat_rule(uuid: str) -> dict[str, Any]:
    """Delete a DNAT rule by UUID. Call firewall_apply after."""
    return get_client().firewall.del_dnat_rule(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def firewall_toggle_dnat_rule(uuid: str, disabled: bool | None = None) -> dict[str, Any]:
    """Toggle a DNAT rule. disabled=True disables it. Call firewall_apply after."""
    return get_client().firewall.toggle_dnat_rule(uuid, disabled).model_dump(exclude_none=True)


# ---- SNAT (outbound NAT) -----------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def firewall_search_snat_rules(search_phrase: str = "") -> dict[str, Any]:
    """Search source NAT (outbound) rules."""
    result = get_client().firewall.search_snat_rules(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": [r.model_dump(exclude_none=True) for r in result.rows]}


@mcp.tool()
@handle_opnsense_errors
def firewall_add_snat_rule(
    interface: str,
    target: str,
    enabled: str = "1",
    nonat: str | None = None,
    sequence: str | None = None,
    ipprotocol: str | None = None,
    protocol: str | None = None,
    source_net: str | None = None,
    source_not: str | None = None,
    source_port: str | None = None,
    destination_net: str | None = None,
    destination_not: str | None = None,
    destination_port: str | None = None,
    target_port: str | None = None,
    staticnatport: str | None = None,
    log: str | None = None,
    categories: str | None = None,
    description: str | None = None,
) -> dict[str, Any]:
    """Create a source NAT (outbound) rule. Call firewall_apply after."""
    rule = SNatRule(
        interface=interface, target=target, enabled=enabled, nonat=nonat, sequence=sequence,
        ipprotocol=ipprotocol, protocol=protocol, source_net=source_net, source_not=source_not,
        source_port=source_port, destination_net=destination_net, destination_not=destination_not,
        destination_port=destination_port, target_port=target_port, staticnatport=staticnatport,
        log=log, categories=categories, description=description,
    )
    return get_client().firewall.add_snat_rule(rule).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def firewall_del_snat_rule(uuid: str) -> dict[str, Any]:
    """Delete a source NAT rule by UUID. Call firewall_apply after."""
    return get_client().firewall.del_snat_rule(uuid).model_dump(exclude_none=True)


# ---- NPT rules ---------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def firewall_search_npt_rules(search_phrase: str = "") -> dict[str, Any]:
    """Search NPT (network prefix translation) rules."""
    result = get_client().firewall.search_npt_rules(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": [r.model_dump(exclude_none=True) for r in result.rows]}


@mcp.tool()
@handle_opnsense_errors
def firewall_add_npt_rule(
    interface: str,
    source_net: str,
    destination_net: str,
    enabled: str = "1",
    log: str | None = None,
    sequence: str | None = None,
    trackif: str | None = None,
    categories: str | None = None,
    description: str | None = None,
) -> dict[str, Any]:
    """Create an NPT (network prefix translation) rule. Call firewall_apply after."""
    rule = NPTRule(
        interface=interface, source_net=source_net, destination_net=destination_net,
        enabled=enabled, log=log, sequence=sequence, trackif=trackif,
        categories=categories, description=description,
    )
    return get_client().firewall.add_npt_rule(rule).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def firewall_del_npt_rule(uuid: str) -> dict[str, Any]:
    """Delete an NPT rule by UUID. Call firewall_apply after."""
    return get_client().firewall.del_npt_rule(uuid).model_dump(exclude_none=True)


# ---- One-to-one NAT ----------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def firewall_search_one_to_one_rules(search_phrase: str = "") -> dict[str, Any]:
    """Search 1:1 NAT rules."""
    result = get_client().firewall.search_one_to_one_rules(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": [r.model_dump(exclude_none=True) for r in result.rows]}


@mcp.tool()
@handle_opnsense_errors
def firewall_add_one_to_one_rule(
    interface: str,
    source_net: str,
    destination_net: str,
    external: str,
    enabled: str = "1",
    type: str | None = None,
    log: str | None = None,
    sequence: str | None = None,
    source_not: str | None = None,
    destination_not: str | None = None,
    natreflection: str | None = None,
    categories: str | None = None,
    description: str | None = None,
) -> dict[str, Any]:
    """Create a 1:1 NAT rule. Call firewall_apply after."""
    rule = OneToOneRule(
        interface=interface, source_net=source_net, destination_net=destination_net,
        external=external, enabled=enabled, type=type, log=log, sequence=sequence,
        source_not=source_not, destination_not=destination_not, natreflection=natreflection,
        categories=categories, description=description,
    )
    return get_client().firewall.add_one_to_one_rule(rule).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def firewall_del_one_to_one_rule(uuid: str) -> dict[str, Any]:
    """Delete a 1:1 NAT rule by UUID. Call firewall_apply after."""
    return get_client().firewall.del_one_to_one_rule(uuid).model_dump(exclude_none=True)


# ---- Misc --------------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def firewall_list_network_aliases() -> dict[str, Any]:
    """List network-type aliases available for use in rules."""
    return get_client().firewall.list_network_aliases()


@mcp.tool()
@handle_opnsense_errors
def firewall_get_table_size() -> dict[str, Any]:
    """Get current pf table size statistics."""
    return get_client().firewall.get_table_size()


@mcp.tool()
@handle_opnsense_errors
def firewall_get_geo_ip() -> dict[str, Any]:
    """Get GeoIP database status and info."""
    return get_client().firewall.get_geo_ip()
