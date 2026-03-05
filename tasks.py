from pathlib import Path

from invoke.context import Context
from invoke.tasks import task

# from photobooth.utils.make_exe import make_exe
from photobooth.utils.qml import generate_qrc_file # generate_qmldir_files

ROOT_DIR = Path(__file__).parent
SOURCE_DIR = ROOT_DIR / "photobooth"

MAIN_VIEWS_DIRECTORY = SOURCE_DIR / "view"



@task
def generate_qmldir(c: Context):
    """TODO script to generate qmldir"""


@task
def generate_qrc(c: Context):
    """
    Generate a dummy qrc file that you should clean afterwards
    Also, the following command must be run on it and the qrc.py file must be replaced by the result:
    pyside6-rcc.exe ./photobooth/.qrc -o ./photobooth/qrc.py
    """
    generate_qrc_file(SOURCE_DIR, MAIN_VIEWS_DIRECTORY.parent)
    # TODO add run of the pyside6-rcc.exe command

@task
def make_exe(c: Context):
    """
    Generate the executable
    """
    # TODO


@task
def run(c: Context):
    """Run the application."""
    c.run("toto")
