import asyncio
from pathlib import Path
from typing import Any

from PySide6.QtCore import QObject, Signal, Slot

from photobooth.overlay import add_overlay

# TODO add overlay path to config
OVERLAY_PHOTO = Path().cwd() / "photobooth" / "view" / "assets" / "cadre_photo_clean.png"
OVERLAY_PHOTO_FOLDER = Path().cwd() / "photos" / "photos_overlay"


class QtBackend(QObject):
    """Qt Backend for the Photo Booth"""

    sProjectPath = Signal(str)
    sPhotoOverlayReady = Signal(str)

    def __init__(self, config: dict[str, Any], *args, **kwargs) -> None:  # type: ignore
        super().__init__(*args, **kwargs)  # type: ignore
        self.config: dict[str, Any] = config
        print(config)

    def init(
        self,
    ) -> None:
        """initialize the project"""
        self.sProjectPath.emit(str(Path().cwd().absolute()))

    @Slot(str)
    def add_overlay(self, photo_path: str) -> None:
        """Add the overlay to the photo"""
        path_photo_with_overlay = asyncio.create_task(
            add_overlay(Path(photo_path), OVERLAY_PHOTO, OVERLAY_PHOTO_FOLDER)
        )
        path_photo_with_overlay.add_done_callback(self.photo_with_overlay_ready)

    def photo_with_overlay_ready(self, task: asyncio.Task) -> None:
        """Trigger the signal sPhotoOverlayReady with the path of the image with the overlay"""
        self.sPhotoOverlayReady.emit(str(task.result()))
