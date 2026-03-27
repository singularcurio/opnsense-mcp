from __future__ import annotations

import functools
from typing import Any, Callable, TypeVar

from opnsense_py.exceptions import (
    OPNsenseAuthError,
    OPNsenseError,
    OPNsenseNotFoundError,
    OPNsenseValidationError,
)

F = TypeVar("F", bound=Callable[..., Any])


def handle_opnsense_errors(f: F) -> F:
    """Catch OPNsense exceptions and re-raise as ValueError with a human-readable message.

    The MCP SDK converts unhandled exceptions from tool functions into error responses.
    Raising ValueError with a clear message is sufficient.
    """

    @functools.wraps(f)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        try:
            return f(*args, **kwargs)
        except OPNsenseValidationError as exc:
            fields = "; ".join(f"{k}: {v}" for k, v in exc.validations.items())
            raise ValueError(f"Validation failed: {fields}") from exc
        except OPNsenseAuthError as exc:
            raise ValueError(
                f"Authentication failed. Check OPNSENSE_API_KEY and OPNSENSE_API_SECRET. ({exc})"
            ) from exc
        except OPNsenseNotFoundError as exc:
            raise ValueError(f"Resource not found: {exc}") from exc
        except OPNsenseError as exc:
            raise ValueError(f"OPNsense API error: {exc}") from exc

    return wrapper  # type: ignore[return-value]
