"""PhotoBooth Main"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import PySide6.QtAsyncio as QtAsyncio
from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

import photobooth.qrc  # noqa: F401
from photobooth.backend.backend import QtBackend
#from photobooth.utils.toml_config import read_config

__RUNNING_FROM_BUNDLE__: bool = getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS")

PROJECT_PATH = Path.cwd() / Path(sys._MEIPASS) if __RUNNING_FROM_BUNDLE__ else Path(__file__).parent
VIEW_PATH = PROJECT_PATH if __RUNNING_FROM_BUNDLE__ else PROJECT_PATH / "view"
QML_PATH = VIEW_PATH / "qml"


async def startup(backend: QtBackend) -> None:
    """Start the backend"""
    backend.init()


def start_qt_engine(config: dict[str, Any]) -> None:
    app = QGuiApplication(sys.argv)
    backend = QtBackend(config)

    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.addImportPath("qrc:/")
    engine.addImportPath(VIEW_PATH)
    engine.addImportPath(str(QML_PATH))
    engine.rootContext().setContextProperty("backend", backend)
    engine.load(QUrl.fromLocalFile(QML_PATH / "Main.qml"))

    QtAsyncio.run(startup(backend), handle_sigint=True)  # type: ignore


def main() -> None:
    """Initialize and run the app."""
    config = {}#read_config(PROJECT_PATH / ".." / "..")
    start_qt_engine(config)


if __name__ == "__main__":
    main()
