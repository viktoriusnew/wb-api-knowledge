#!/usr/bin/env python3
"""Copy the repository skill into the local Codex skills directory."""

from __future__ import annotations

import shutil
from pathlib import Path


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def main() -> int:
    root = repo_root()
    source = root / "skills" / "wb-api-knowledge"
    target = Path.home() / ".codex" / "skills" / "wb-api-knowledge"
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(source, target)
    print(f"Installed skill to {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
