from PyQt5.QtCore import pyqtSignal, QObject

class Communicate(QObject):
    update_signal = pyqtSignal()
    progress_signal = pyqtSignal(int)
    complete_signal = pyqtSignal(str, bool)