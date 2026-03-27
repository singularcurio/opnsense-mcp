from __future__ import annotations

import os
import re
from pathlib import Path
from typing import Any

from opnsense_mcp.tools.registry import get_module_registrar

mcp = get_module_registrar(__name__)

# Default: sibling opnsense-py/opnsense-docs relative to this repo layout.
# Override with OPNSENSE_DOCS_PATH for other install locations.
_DEFAULT_DOCS = Path(__file__).parents[3] / "opnsense-py" / "opnsense-docs"

_MAX_FILES = 20
_MAX_SNIPPETS_PER_FILE = 3
_SNIPPET_CONTEXT = 2  # lines before/after match


def _docs_root() -> Path:
    path = Path(os.environ.get("OPNSENSE_DOCS_PATH", str(_DEFAULT_DOCS)))
    if not path.is_dir():
        raise ValueError(
            f"Docs directory not found: {path}. "
            "Set OPNSENSE_DOCS_PATH to point at the opnsense-docs directory."
        )
    return path


@mcp.tool()
def docs_search(query: str, section: str = "") -> dict[str, Any]:
    """Search OPNsense documentation markdown files for a query string.

    Returns up to 20 matching files, each with up to 3 line-level snippets showing
    context around each match. Use section to narrow scope.

    Args:
        query: Search terms (case-insensitive substring match).
        section: Optional subdirectory to restrict search, e.g. 'development/api/core',
                 'manual', 'development'. Leave empty to search all docs.
    """
    root = _docs_root()
    search_root = (root / section) if section else root
    if not search_root.is_dir():
        raise ValueError(
            f"Section {section!r} not found. "
            "Try: 'development/api/core', 'development/api/plugins', 'manual', 'development'."
        )

    pattern = re.compile(re.escape(query), re.IGNORECASE)
    results: list[dict[str, Any]] = []

    for md_file in sorted(search_root.rglob("*.md")):
        if ".doctrees" in md_file.parts:
            continue
        lines = md_file.read_text(errors="replace").splitlines()
        snippets: list[dict[str, Any]] = []
        for i, line in enumerate(lines):
            if pattern.search(line):
                start = max(0, i - _SNIPPET_CONTEXT)
                end = min(len(lines), i + _SNIPPET_CONTEXT + 1)
                snippets.append({
                    "line": i + 1,
                    "snippet": "\n".join(lines[start:end]),
                })
                if len(snippets) >= _MAX_SNIPPETS_PER_FILE:
                    break
        if snippets:
            results.append({
                "path": str(md_file.relative_to(root)),
                "matches": snippets,
            })
        if len(results) >= _MAX_FILES:
            break

    return {"query": query, "section": section or "(all)", "total": len(results), "results": results}


@mcp.tool()
def docs_read(path: str) -> dict[str, Any]:
    """Read a specific OPNsense documentation file by its relative path.

    Use docs_search() first to discover paths.

    Args:
        path: Relative path from docs root, e.g. 'development/api/core/firewall.md'
    """
    root = _docs_root()
    target = (root / path).resolve()
    if not str(target).startswith(str(root.resolve())):
        raise ValueError("Path traversal not allowed.")
    if target.suffix != ".md":
        raise ValueError(f"Only .md files are supported, got: {target.suffix!r}")
    if not target.exists():
        raise ValueError(f"File not found: {path!r}. Use docs_search() to find valid paths.")
    return {
        "path": path,
        "content": target.read_text(errors="replace"),
    }
