import httpx
import pytest
import respx

from opnsense_mcp.tools.cron import cron_search_jobs


def test_auth_error_raises_value_error(mcp_client, mock_api: respx.MockRouter):
    mock_api.post("/api/cron/settings/search_jobs").mock(
        return_value=httpx.Response(401, text="Unauthorized")
    )
    with pytest.raises(ValueError, match="Authentication failed"):
        cron_search_jobs()


def test_not_found_raises_value_error(mcp_client, mock_api: respx.MockRouter):
    mock_api.post("/api/cron/settings/search_jobs").mock(
        return_value=httpx.Response(404, text="Not Found")
    )
    with pytest.raises(ValueError, match="not found"):
        cron_search_jobs()


def test_server_error_raises_value_error(mcp_client, mock_api: respx.MockRouter):
    mock_api.post("/api/cron/settings/search_jobs").mock(
        return_value=httpx.Response(500, text="Internal Server Error")
    )
    with pytest.raises(ValueError, match="OPNsense API error"):
        cron_search_jobs()
