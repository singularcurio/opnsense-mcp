import httpx
import respx

from opnsense_mcp.tools.cron import (
    cron_search_jobs,
    cron_get_job,
    cron_add_job,
    cron_del_job,
    cron_toggle_job,
    cron_reconfigure,
)

UUID = "aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee"


def test_search_jobs_empty(mcp_client, mock_api: respx.MockRouter):
    mock_api.post("/api/cron/settings/search_jobs").mock(
        return_value=httpx.Response(200, json={"total": 0, "rowCount": 0, "current": 1, "rows": []})
    )
    result = cron_search_jobs()
    assert result == {"total": 0, "rows": []}


def test_search_jobs_with_results(mcp_client, mock_api: respx.MockRouter):
    row = {"uuid": UUID, "command": "my-cmd", "description": "test job", "enabled": "1"}
    mock_api.post("/api/cron/settings/search_jobs").mock(
        return_value=httpx.Response(200, json={"total": 1, "rowCount": 1, "current": 1, "rows": [row]})
    )
    result = cron_search_jobs(search_phrase="test")
    assert result["total"] == 1
    assert result["rows"][0]["uuid"] == UUID


def test_get_job(mcp_client, mock_api: respx.MockRouter):
    mock_api.get(f"/api/cron/settings/get_job/{UUID}").mock(
        return_value=httpx.Response(200, json={"job": {"command": "my-cmd", "description": "test"}})
    )
    result = cron_get_job(UUID)
    assert result["command"] == "my-cmd"


def test_add_job(mcp_client, mock_api: respx.MockRouter):
    mock_api.post("/api/cron/settings/add_job").mock(
        return_value=httpx.Response(200, json={"result": "saved", "uuid": UUID})
    )
    result = cron_add_job(
        command="my-cmd",
        description="test job",
        minutes="0",
        hours="*",
        days="*",
        months="*",
        weekdays="*",
    )
    assert result["result"] == "saved"
    assert result["uuid"] == UUID


def test_del_job(mcp_client, mock_api: respx.MockRouter):
    mock_api.post(f"/api/cron/settings/del_job/{UUID}").mock(
        return_value=httpx.Response(200, json={"result": "deleted"})
    )
    result = cron_del_job(UUID)
    assert result["result"] == "deleted"


def test_toggle_job(mcp_client, mock_api: respx.MockRouter):
    mock_api.post(f"/api/cron/settings/toggle_job/{UUID}").mock(
        return_value=httpx.Response(200, json={"result": "ok"})
    )
    result = cron_toggle_job(UUID)
    assert result["result"] == "ok"


def test_reconfigure(mcp_client, mock_api: respx.MockRouter):
    mock_api.post("/api/cron/service/reconfigure").mock(
        return_value=httpx.Response(200, json={"result": "ok"})
    )
    result = cron_reconfigure()
    assert result["result"] == "ok"
