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
        self.update_deck()
        self.connectSignals()

    def connectSignals(self):
        self.view.mainwindow.myQuitSignal.connect(self.quit)
        self.view.mainwindow.actionQuit.triggered.connect(self.quit)
        self.view.mainwindow.actionAbout.triggered.connect(self.about)
        self.view.mainwindow.quit_btn.clicked.connect(self.quit)
        self.view.mainwindow.player_btn.clicked.connect(self.select_player)
        self.view.mainwindow.deck_btn.clicked.connect(self.select_deck)
        self.view.mainwindow.start_quiz_btn.clicked.connect(self.start_quiz)

    def quit(self):
        self.model.quit()
        QtWidgets.QApplication.quit()

    def about(self):
        QtWidgets.QMessageBox.information(
            self.view.mainwindow,
            "About title",  # TODO: About title
            "About message" # TODO: About message
            )

    def select_player(self):
        players_list = self.model.game.get_players_list()
        player_name = self.view.mainwindow.select_player_dialog(players_list)
        self.model.game.load_player(player_name)
        self.update_player()

    def update_player(self):
        player = self.model.game.get_player_name()
        self.view.mainwindow.player_label.setText(f"Selected player: {player}")

    def select_deck(self):
        decks_list = self.model.game.get_decks_list()
        deck_name = self.view.mainwindow.select_deck_dialog(decks_list)
        self.model.game.load_deck(deck_name)
        self.update_deck()

    def update_deck(self):
        deck = self.model.game.get_deck_name()
        if not deck:
            self.view.mainwindow.start_quiz_btn.setEnabled(False)
        else:
            self.view.mainwindow.start_quiz_btn.setEnabled(True)
        self.view.mainwindow.deck_label.setText(f"Selected deck: {deck}")

    def start_quiz(self):
        logger.debug("start_quiz_btn clicked")