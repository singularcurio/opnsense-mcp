from __future__ import annotations

import json
from typing import Any

from opnsense_py.models.base import SearchRequest

from opnsense_mcp.context import get_client
from opnsense_mcp.errors import handle_opnsense_errors
from opnsense_mcp.tools.registry import get_module_registrar
mcp = get_module_registrar(__name__)


# ---- Certificate Authorities -------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def trust_search_cas(search_phrase: str = "") -> dict[str, Any]:
    """Search certificate authorities."""
    result = get_client().trust.search_cas(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": list(result.rows)}


@mcp.tool()
@handle_opnsense_errors
def trust_get_ca(uuid: str) -> dict[str, Any]:
    """Get a certificate authority by UUID."""
    return get_client().trust.get_ca(uuid)


@mcp.tool()
@handle_opnsense_errors
def trust_add_ca(data_json: str) -> dict[str, Any]:
    """Create a certificate authority. data_json: JSON with CA fields."""
    return get_client().trust.add_ca(json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def trust_set_ca(uuid: str, data_json: str) -> dict[str, Any]:
    """Update a certificate authority. data_json: JSON with CA fields."""
    return get_client().trust.set_ca(uuid, json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def trust_del_ca(uuid: str) -> dict[str, Any]:
    """Delete a certificate authority by UUID."""
    return get_client().trust.del_ca(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def trust_ca_info(caref: str) -> dict[str, Any]:
    """Get detailed information about a CA by its reference ID."""
    return get_client().trust.ca_info(caref)


@mcp.tool()
@handle_opnsense_errors
def trust_ca_list() -> dict[str, Any]:
    """List all certificate authorities."""
    return get_client().trust.ca_list()


@mcp.tool()
@handle_opnsense_errors
def trust_raw_dump_ca(uuid: str) -> dict[str, Any]:
    """Get the raw PEM dump of a CA certificate."""
    return get_client().trust.raw_dump_ca(uuid)


# ---- Certificates ------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def trust_search_certs(search_phrase: str = "") -> dict[str, Any]:
    """Search certificates."""
    result = get_client().trust.search_certs(SearchRequest(searchPhrase=search_phrase))
    return {"total": result.total, "rows": list(result.rows)}


@mcp.tool()
@handle_opnsense_errors
def trust_get_cert(uuid: str) -> dict[str, Any]:
    """Get a certificate by UUID."""
    return get_client().trust.get_cert(uuid)


@mcp.tool()
@handle_opnsense_errors
def trust_add_cert(data_json: str) -> dict[str, Any]:
    """Create a certificate. data_json: JSON with certificate fields."""
    return get_client().trust.add_cert(json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def trust_set_cert(uuid: str, data_json: str) -> dict[str, Any]:
    """Update a certificate. data_json: JSON with certificate fields."""
    return get_client().trust.set_cert(uuid, json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def trust_del_cert(uuid: str) -> dict[str, Any]:
    """Delete a certificate by UUID."""
    return get_client().trust.del_cert(uuid).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def trust_cert_ca_list() -> dict[str, Any]:
    """List CAs available for signing certificates."""
    return get_client().trust.cert_ca_list()


@mcp.tool()
@handle_opnsense_errors
def trust_cert_user_list() -> dict[str, Any]:
    """List users that can be associated with certificates."""
    return get_client().trust.cert_user_list()


@mcp.tool()
@handle_opnsense_errors
def trust_raw_dump_cert(uuid: str) -> dict[str, Any]:
    """Get the raw PEM dump of a certificate."""
    return get_client().trust.raw_dump_cert(uuid)


# ---- CRLs --------------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def trust_search_crls() -> dict[str, Any]:
    """List all Certificate Revocation Lists."""
    return get_client().trust.search_crls()


@mcp.tool()
@handle_opnsense_errors
def trust_get_crl(caref: str) -> dict[str, Any]:
    """Get a CRL by CA reference ID."""
    return get_client().trust.get_crl(caref)


@mcp.tool()
@handle_opnsense_errors
def trust_set_crl(caref: str, data_json: str) -> dict[str, Any]:
    """Update a CRL. data_json: JSON with CRL fields."""
    return get_client().trust.set_crl(caref, json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def trust_del_crl(caref: str) -> dict[str, Any]:
    """Delete a CRL by CA reference ID."""
    return get_client().trust.del_crl(caref).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def trust_raw_dump_crl(caref: str) -> dict[str, Any]:
    """Get the raw PEM dump of a CRL."""
    return get_client().trust.raw_dump_crl(caref)


# ---- Settings ----------------------------------------------------------------


@mcp.tool()
@handle_opnsense_errors
def trust_get_settings() -> dict[str, Any]:
    """Get trust/PKI global settings."""
    return get_client().trust.get_settings()


@mcp.tool()
@handle_opnsense_errors
def trust_set_settings(data_json: str) -> dict[str, Any]:
    """Update trust/PKI global settings. data_json: JSON with settings fields."""
    return get_client().trust.set_settings(json.loads(data_json)).model_dump(exclude_none=True)


@mcp.tool()
@handle_opnsense_errors
def trust_reconfigure() -> dict[str, Any]:
    """Apply pending trust/PKI configuration changes."""
    return get_client().trust.reconfigure().model_dump(exclude_none=True)
