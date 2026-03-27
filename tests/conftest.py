import pytest
import respx

from opnsense_py import OPNsenseClient

import opnsense_mcp.context as ctx_module


@pytest.fixture(autouse=True)
def reset_client_singleton():
    """Reset the lazy client singleton before each test."""
    ctx_module.reset_client()
    yield
    ctx_module.reset_client()


@pytest.fixture
def mock_api():
    with respx.mock(base_url="https://opnsense.test:443", assert_all_called=False) as mock:
        yield mock


@pytest.fixture
def mcp_client(mock_api: respx.MockRouter, monkeypatch: pytest.MonkeyPatch) -> OPNsenseClient:
    """Inject a pre-built client that uses the respx-mocked transport."""
    client = OPNsenseClient(
        host="opnsense.test",
        api_key="testkey",
        api_secret="testsecret",
        verify_ssl=False,
    )
    monkeypatch.setattr(ctx_module, "_client", client)
    return client
