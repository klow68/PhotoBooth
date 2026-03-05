from PySide6.QtCore import QSize, Qt, Slot, QObject
from PySide6.QtWidgets import QTabWidget, QWidget
# from PySide6.QtCore import QAbstractListModel, Signal, SignalInstance, Slot

class Backend(QObject):
    """Qt Backend for the Photo Booth"""

    def __init__(self,) -> None:
        super().__init__()


    @Slot()
    def test2(self):
        print("this is a test")