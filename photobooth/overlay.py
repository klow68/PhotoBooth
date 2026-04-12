"""Overlay for the image before printing"""

import asyncio
import datetime as dt
from pathlib import Path

from PIL import Image


async def add_overlay(photo_path: Path, overlay_path: Path, save_path: Path | None = None) -> None | Path:
    """
    Add the overlay to the photo and save it if there is a path given

    To debug, use the function show on the image
    """
    await asyncio.sleep(3)
    background = Image.open(overlay_path)
    background_copy = Image.open(overlay_path)
    photo = Image.open(photo_path)
    photo.thumbnail((884, 884))
    background.paste(photo, (70, 120))  # 110,120
    # Override again the img1 on top to remove any overlapping photo
    background.paste(background_copy, (0, 0), mask=background_copy)

    if save_path:
        current_date = dt.datetime.now().strftime("%d-%m-%Y_%H%M%S")
        background.convert("RGB")
        background.save(save_path / (current_date + ".png"))
        return save_path / (current_date + ".png")
    return None
