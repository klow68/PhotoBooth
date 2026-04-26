"""Tasks of the PhotoBooth"""

import subprocess
from pathlib import Path

from invoke.context import Context
from invoke.tasks import task

from photobooth.utils.qml import generate_qrc_file

ROOT_DIR = Path(__file__).parent
SOURCE_DIR = ROOT_DIR / "src" / "photobooth"

MAIN_VIEWS_DIRECTORY = SOURCE_DIR / "view"


@task
def generate_qrc(_: Context) -> None:
    """
    Generate a dummy qrc file that you should clean afterwards
    """
    generate_qrc_file(SOURCE_DIR, MAIN_VIEWS_DIRECTORY.parent)
    subprocess.run(["uv", "run", "pyside6-rcc", "./src/photobooth/.qrc", "-o", "./src/photobooth/qrc.py"], check=True)


@task
def make_exe(_: Context) -> None:
    """
    Generate the executable
    """
    # TODO
