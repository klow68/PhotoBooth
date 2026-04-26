from pathlib import Path
from typing import Any

import tomli


def read_config(project_path:Path) -> dict[str, Any]:
    with open(project_path / "settings.toml", "rb") as f:
        settings: dict[str, Any] = tomli.load(f)
    return settings
