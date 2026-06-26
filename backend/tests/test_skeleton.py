"""Skeleton validation tests for the Phase 2 project structure."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_phase_two_skeleton_paths_exist() -> None:
    """Verify the documented Phase 2 skeleton directories remain present."""
    expected_paths = [
        ROOT / "backend" / "api",
        ROOT / "backend" / "ai",
        ROOT / "backend" / "planner",
        ROOT / "backend" / "database",
        ROOT / "backend" / "updater",
        ROOT / "backend" / "roku",
        ROOT / "backend" / "models",
        ROOT / "backend" / "utils",
        ROOT / "frontend" / "roku-app",
        ROOT / "frontend" / "assets",
        ROOT / "config",
        ROOT / "scripts",
        ROOT / "docs",
    ]

    missing_paths = [path for path in expected_paths if not path.exists()]

    assert missing_paths == []
