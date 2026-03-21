#!/usr/bin/env python3
"""Install the self-contained WB API skill into the local Codex skills directory."""

from __future__ import annotations

import shutil
from pathlib import Path


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def main() -> int:
    root = repo_root()
    source = root / "skills" / "wb-api-knowledge"
    target = Path.home() / ".codex" / "skills" / "wb-api-knowledge"
    required_paths = [
        source / "SKILL.md",
        source / "indexes",
        source / "knowledge",
        source / "scripts" / "search_knowledge.py",
    ]
    missing = [str(path) for path in required_paths if not path.exists()]
    if missing:
        raise SystemExit(
            "Skill source is incomplete. Missing required bundled paths:\n"
            + "\n".join(missing)
        )
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(source, target)
    print(f"Installed self-contained skill to {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
