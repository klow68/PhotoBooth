from pathlib import Path
from typing import Any

import tomli


def read_config() -> dict[str, Any]:
    with open(Path("settings.toml"), "rb") as f:
        settings: dict[str, Any] = tomli.load(f)
    return settings
