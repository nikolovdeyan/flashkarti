import logging
from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import QMainWindow

from ui.ui_main_window import Ui_MainWindow

logger = logging.getLogger(__name__)


class FkView(QtCore.QObject):
    def __init__(self):
        super(FkView, self).__init__()
        self.mainwindow = MainWindowView()


class MainWindowView(QMainWindow, Ui_MainWindow):

    myQuitSignal = QtCore.Signal()

    def __init__(self):
        super(MainWindowView, self).__init__()
        self.setupUi(self)

    def closeEvent(self, event):
        """
            This method overrides the mainwindow's closeEvent method
            which gets called when the user tries to close the mainwindow
        """
        logger.debug("closeEvent called")
        event.ignore()
        self.myQuitSignal.emit()
