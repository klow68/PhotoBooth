from __future__ import annotations

from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QUrl
import PySide6.QtAsyncio as QtAsyncio

from pathlib import Path

import sys

from photobooth.backend.backend import Backend

__RUNNING_FROM_BUNDLE__: bool = getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS")

_PROJECT_ROOT_PATH = Path.cwd() / Path(sys._MEIPASS) if __RUNNING_FROM_BUNDLE__ else Path.cwd()
VIEW_PATH = _PROJECT_ROOT_PATH if __RUNNING_FROM_BUNDLE__ else _PROJECT_ROOT_PATH / "photobooth" / "view"
QML_PATH = VIEW_PATH / "qml"

# WEBCAM_CAPTURE_FOLDER

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    backend = Backend()
    
    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.addImportPath("qrc:/")
    engine.addImportPath(VIEW_PATH)
    engine.rootContext().setContextProperty("backend", backend)
    engine.load(QUrl.fromLocalFile(QML_PATH / "main.qml"))




    QtAsyncio.run(handle_sigint=True)