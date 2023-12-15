import logging
from PySide6 import QtCore, QtGui, QtWidgets

logger = logging.getLogger(__name__)

class FkPresenter(QtCore.QObject):
    def __init__(self, model, view, app):
        super(FkPresenter, self).__init__()

        self.model = model
        self.view = view
        self.app = app

        self.mainwindow_presenter = MainWindowPresenter(model, view, app)

        self.view.mainwindow.show()


class MainWindowPresenter(QtCore.QObject):
    def __init__(self, model, view, app):
        super(MainWindowPresenter, self).__init__()

        self.model = model
        self.view = view
        self.app = app

        self.connectSignals()

    def connectSignals(self):
        self.view.mainwindow.myQuitSignal.connect(self.quit)
        self.view.mainwindow.quit_btn.clicked.connect(self.quit)
        self.view.mainwindow.player_btn.clicked.connect(self.select_player)
        self.view.mainwindow.deck_btn.clicked.connect(self.select_deck)

    def quit(self):
        self.model.quit()
        logger.debug("Calling quit application")
        QtWidgets.QApplication.quit()

    def select_player(self):
        logger.debug("Calling select_player")
        return "Deo"

    def select_deck(self):
        logger.debug("Calling select_deck")
        return "Python"

