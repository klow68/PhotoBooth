from pathlib import Path

from PySide6.QtCore import QObject, Signal, Slot

# from PySide6.QtCore import QAbstractListModel, Signal, SignalInstance, Slot


class Backend(QObject):
    """Qt Backend for the Photo Booth"""

    sProjectPath = Signal(str)

    def __init__(
        self,
    ) -> None:
        super().__init__()

    def init(self) -> None:
        """initialize the project"""
        self.sProjectPath.emit(str(Path().cwd().absolute()))

    @Slot()
    def test2(self) -> None:
        """test slot"""
        print("this is a test")
