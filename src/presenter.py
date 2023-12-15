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

        self.update_player()
        self.connectSignals()

    def connectSignals(self):
        self.view.mainwindow.myQuitSignal.connect(self.quit)
        self.view.mainwindow.actionQuit.triggered.connect(self.quit)
        self.view.mainwindow.quit_btn.clicked.connect(self.quit)
        self.view.mainwindow.player_btn.clicked.connect(self.select_player)
        self.view.mainwindow.deck_btn.clicked.connect(self.select_deck)
        self.view.mainwindow.start_quiz_btn.clicked.connect(self.start_quiz)

    def quit(self):
        self.model.quit()
        logger.debug("Calling quit application")
        QtWidgets.QApplication.quit()

    def select_player(self):
        pass

    def update_player(self):
        player = self.model.game.player.name
        self.view.mainwindow.player_label.setText(f"Selected player: {player}")

    def select_deck(self):
        pass

    def update_deck(self):
        deck = self.model.game.deck.name if self.model.game.deck else "None"
        self.view.mainwindow.deck_label.setText(f"Selected deck: {deck}")


    def start_quiz(self):
        pass