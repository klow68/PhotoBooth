"""PhotoBooth Main"""

from __future__ import annotations

import sys
from pathlib import Path

import cups  # noqa: F401
import PySide6.QtAsyncio as QtAsyncio
from PIL import Image  # noqa: F401
from PySide6.QtCore import QUrl
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine

import photobooth.qrc  # noqa: F401
from photobooth.backend.backend import Backend
from photobooth.printer import print_image  # noqa: F401

__RUNNING_FROM_BUNDLE__: bool = getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS")

PROJECT_PATH = Path.cwd() / Path(sys._MEIPASS) if __RUNNING_FROM_BUNDLE__ else Path.cwd()
VIEW_PATH = PROJECT_PATH if __RUNNING_FROM_BUNDLE__ else PROJECT_PATH / "photobooth" / "view"
QML_PATH = VIEW_PATH / "qml"


async def startup(backend: Backend) -> None:
    """Start the backend"""
    backend.init()


# QT
def main() -> None:
    """Initialize and run the app."""
    app = QGuiApplication(sys.argv)
    backend = Backend()

    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.addImportPath("qrc:/")
    engine.addImportPath(VIEW_PATH)
    engine.rootContext().setContextProperty("backend", backend)
    engine.load(QUrl.fromLocalFile(QML_PATH / "Main.qml"))

    QtAsyncio.run(startup(backend), handle_sigint=True)  # type: ignore


# PRINTER
# def example_printer():
# conn = cups.Connection()
# printers = conn.getPrinters()

# image_path = Path("photos.jpg")
# print(str(image_path.absolute()))
# print_image(image_path.absolute(), "Cups-PDF")


# Overlay image
def example_overlay_image() -> None:
    background = Image.open(Path().cwd() / "photobooth" / "view" / "assets" / "cadre_photo_clean.png")
    background_copy = Image.open(Path().cwd() / "photobooth" / "view" / "assets" / "cadre_photo_clean.png")
    photo = Image.open(Path().cwd() / "photobooth" / "view" / "assets" / "photos.jpg")
    photo.thumbnail((884, 884))
    background.paste(photo, (70, 120))  # 110,120
    # Override again the img1 on top to remove any overlapping photo
    background.paste(background_copy, (0, 0), mask=background_copy)
    background.show()


if __name__ == "__main__":
    main()
