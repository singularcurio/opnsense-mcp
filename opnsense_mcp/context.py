from __future__ import annotations

import os
import tomllib
from pathlib import Path

from opnsense_py import OPNsenseClient

_CONFIG_PATH = Path.home() / ".config" / "opnsense-py" / "config.toml"
_client: OPNsenseClient | None = None


def _load_config_file(profile: str) -> dict[str, str]:
    """Load connection settings from the shared TOML config file for the given profile."""
    if not _CONFIG_PATH.exists():
        return {}
    with _CONFIG_PATH.open("rb") as f:
        data = tomllib.load(f)
    return {k: str(v) for k, v in data.get(profile, {}).items()}


def get_client() -> OPNsenseClient:
    """Return the singleton OPNsenseClient, building it on first call."""
    global _client
    if _client is not None:
        return _client

    profile = os.environ.get("OPNSENSE_PROFILE", "default")
    cfg = _load_config_file(profile)

    host = os.environ.get("OPNSENSE_HOST") or cfg.get("host")
    api_key = os.environ.get("OPNSENSE_API_KEY") or cfg.get("api_key")
    api_secret = os.environ.get("OPNSENSE_API_SECRET") or cfg.get("api_secret")

    env_verify = os.environ.get("OPNSENSE_VERIFY_SSL")
    if env_verify is not None:
        verify_ssl = env_verify.lower() not in ("0", "false", "no")
    else:
        cfg_verify = cfg.get("verify_ssl", "true")
        verify_ssl = cfg_verify.lower() not in ("0", "false", "no")

    env_https = os.environ.get("OPNSENSE_HTTPS")
    if env_https is not None:
        https = env_https.lower() not in ("0", "false", "no")
    else:
        cfg_https = cfg.get("https", "true")
        https = cfg_https.lower() not in ("0", "false", "no")

    missing = [
        name
        for name, val in [("host", host), ("api_key", api_key), ("api_secret", api_secret)]
        if not val
    ]
    if missing:
        raise ValueError(
            f"OPNsense connection not configured. Missing: {', '.join(missing)}. "
            f"Set OPNSENSE_HOST, OPNSENSE_API_KEY, OPNSENSE_API_SECRET env vars "
            f"or add a [default] profile to ~/.config/opnsense-py/config.toml."
        )

    _client = OPNsenseClient(
        host=host,  # type: ignore[arg-type]
        api_key=api_key,  # type: ignore[arg-type]
        api_secret=api_secret,  # type: ignore[arg-type]
        verify_ssl=verify_ssl,
        https=https,
    )
    return _client


def reset_client() -> None:
    """Reset the singleton client. Used in tests."""
    global _client
    _client = None
