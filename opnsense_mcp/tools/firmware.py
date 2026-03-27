from __future__ import annotations

from typing import Any

from opnsense_mcp.context import get_client
from opnsense_mcp.errors import handle_opnsense_errors
from opnsense_mcp.tools.registry import get_module_registrar
mcp = get_module_registrar(__name__)


@mcp.tool()
@handle_opnsense_errors
def firmware_info() -> dict[str, Any]:
    """Get firmware information (current version, upgrade availability)."""
    return get_client().firmware.info()


@mcp.tool()
@handle_opnsense_errors
def firmware_check() -> dict[str, Any]:
    """Check for available firmware updates. Poll firmware_running for completion."""
    return get_client().firmware.check()


@mcp.tool()
@handle_opnsense_errors
def firmware_running() -> dict[str, Any]:
    """Check if a firmware operation is currently running."""
    return get_client().firmware.running()


@mcp.tool()
@handle_opnsense_errors
def firmware_upgradestatus() -> dict[str, Any]:
    """Poll upgrade progress and log after calling firmware_upgrade."""
    return get_client().firmware.upgradestatus()


@mcp.tool()
@handle_opnsense_errors
def firmware_status() -> dict[str, Any]:
    """Get firmware update status."""
    return get_client().firmware.status()


@mcp.tool()
@handle_opnsense_errors
def firmware_update() -> dict[str, Any]:
    """Trigger a firmware update. Poll firmware_running for completion."""
    return get_client().firmware.update()


@mcp.tool()
@handle_opnsense_errors
def firmware_upgrade() -> dict[str, Any]:
    """Trigger a major firmware upgrade. Poll firmware_upgradestatus for progress."""
    return get_client().firmware.upgrade()


@mcp.tool()
@handle_opnsense_errors
def firmware_health() -> dict[str, Any]:
    """Run a firmware health check. Poll firmware_running for completion."""
    return get_client().firmware.health()


@mcp.tool()
@handle_opnsense_errors
def firmware_audit() -> dict[str, Any]:
    """Run a firmware security audit. Poll firmware_running for completion."""
    return get_client().firmware.audit()


@mcp.tool()
@handle_opnsense_errors
def firmware_changelog(version: str) -> dict[str, Any]:
    """Get changelog for a specific firmware version."""
    return get_client().firmware.changelog(version)


@mcp.tool()
@handle_opnsense_errors
def firmware_package_details(pkg_name: str) -> dict[str, Any]:
    """Get details for a specific package."""
    return get_client().firmware.package_details(pkg_name)


@mcp.tool()
@handle_opnsense_errors
def firmware_install_package(pkg_name: str) -> dict[str, Any]:
    """Install a package by name. Poll firmware_running for completion."""
    return get_client().firmware.install_package(pkg_name)


@mcp.tool()
@handle_opnsense_errors
def firmware_remove_package(pkg_name: str) -> dict[str, Any]:
    """Remove a package by name. Poll firmware_running for completion."""
    return get_client().firmware.remove_package(pkg_name)


@mcp.tool()
@handle_opnsense_errors
def firmware_lock_package(pkg_name: str) -> dict[str, Any]:
    """Lock a package to prevent automatic updates."""
    return get_client().firmware.lock_package(pkg_name)


@mcp.tool()
@handle_opnsense_errors
def firmware_unlock_package(pkg_name: str) -> dict[str, Any]:
    """Unlock a previously locked package."""
    return get_client().firmware.unlock_package(pkg_name)


@mcp.tool()
@handle_opnsense_errors
def firmware_reboot() -> dict[str, Any]:
    """Reboot the system via the firmware API."""
    return get_client().firmware.reboot().model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def firmware_poweroff() -> dict[str, Any]:
    """Power off the system."""
    return get_client().firmware.poweroff().model_dump(exclude_none=True)
