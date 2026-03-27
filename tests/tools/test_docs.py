from __future__ import annotations

import textwrap
from pathlib import Path

import pytest

from opnsense_mcp.tools.docs import docs_search, docs_read


@pytest.fixture
def docs_dir(tmp_path: Path) -> Path:
    """Create a minimal fake docs tree for testing."""
    (tmp_path / "manual").mkdir()
    (tmp_path / "development" / "api" / "core").mkdir(parents=True)

    (tmp_path / "intro.md").write_text(textwrap.dedent("""\
        # Introduction
        Welcome to OPNsense documentation.
        This covers firewall and routing.
    """))
    (tmp_path / "manual" / "aliases.md").write_text(textwrap.dedent("""\
        # Aliases
        Aliases are named lists used in firewall rules.
        You can create host, network, and port aliases.
        Aliases simplify rule management significantly.
    """))
    (tmp_path / "development" / "api" / "core" / "firewall.md").write_text(textwrap.dedent("""\
        # Firewall API
        The firewall API provides alias and rule management.
        POST /api/firewall/alias/add_item
        GET  /api/firewall/alias/get_item
    """))
    return tmp_path


@pytest.fixture(autouse=True)
def patch_docs_root(docs_dir: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("OPNSENSE_DOCS_PATH", str(docs_dir))


# ---- docs_search -------------------------------------------------------------

def test_search_finds_match():
    result = docs_search("firewall")
    assert result["total"] > 0
    paths = [r["path"] for r in result["results"]]
    assert any("intro.md" in p or "firewall.md" in p for p in paths)


def test_search_case_insensitive():
    result = docs_search("ALIASES")
    assert result["total"] > 0
    assert any("aliases.md" in r["path"] for r in result["results"])


def test_search_no_match():
    result = docs_search("xyznonexistent123")
    assert result["total"] == 0
    assert result["results"] == []


def test_search_section_narrows_scope():
    result = docs_search("firewall", section="manual")
    # manual/aliases.md mentions firewall but development/api/core/firewall.md should not appear
    paths = [r["path"] for r in result["results"]]
    assert not any("development" in p for p in paths)


def test_search_section_not_found():
    with pytest.raises(ValueError, match="not found"):
        docs_search("anything", section="nonexistent/path")


def test_search_snippet_contains_match():
    result = docs_search("alias")
    assert result["total"] > 0
    for file_result in result["results"]:
        for match in file_result["matches"]:
            assert "alias" in match["snippet"].lower()


def test_search_returns_section_in_result():
    result = docs_search("firewall", section="development/api/core")
    assert result["section"] == "development/api/core"


# ---- docs_read ---------------------------------------------------------------

def test_read_existing_file():
    result = docs_read("intro.md")
    assert result["path"] == "intro.md"
    assert "OPNsense" in result["content"]


def test_read_nested_file():
    result = docs_read("development/api/core/firewall.md")
    assert "Firewall API" in result["content"]


def test_read_file_not_found():
    with pytest.raises(ValueError, match="not found"):
        docs_read("nonexistent.md")


def test_read_non_md_rejected():
    with pytest.raises(ValueError, match="Only .md"):
        docs_read("intro.txt")


def test_read_path_traversal_rejected(docs_dir: Path, tmp_path: Path):
    # Write a file outside the docs root
    outside = tmp_path.parent / "secret.md"
    outside.write_text("secret")
    with pytest.raises(ValueError, match="traversal"):
        docs_read("../../secret.md")
