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
        self.quizwindow_presenter = QuizWindowPresenter(model, view, app)

        self.connectSignals()
        self.view.mainwindow.show()

    def connectSignals(self):
        self.view.mainwindow.myQuitSignal.connect(self.quit)
        self.view.quizwindow.myQuitSignal.connect(self.quit)
        self.view.mainwindow.actionQuit.triggered.connect(self.quit)
        self.view.quizwindow.actionQuit.triggered.connect(self.quit)
        self.view.mainwindow.start_quiz_btn.clicked.connect(self.start_quiz)

    def start_quiz(self):
        self.model.game.start_game()
        self.view.mainwindow.hide()
        self.view.quizwindow.show()
        self.quizwindow_presenter.update_quiz()

    def quit(self):
        self.model.quit()
        QtWidgets.QApplication.quit()


class QuizWindowPresenter(QtCore.QObject):
    def __init__(self, model, view, app):
        super(QuizWindowPresenter, self).__init__()

        self.model = model
        self.view = view
        self.app = app

        self.connectSignals()

    def update_quiz(self):
        current_card = self.model.game.get_current_card_display()
        self.view.quizwindow.deck_title_label.setText(current_card.get("deck_title"))
        self.view.quizwindow.card_title_label.setText(current_card.get("card_title"))
        self.view.quizwindow.card_question_field.setText(current_card.get("card_contents"))

    def connectSignals(self):
        self.view.quizwindow.actionEnd_Round.triggered.connect(self.end_round)
        self.view.quizwindow.next_card_btn.clicked.connect(self.next_card)
        self.view.quizwindow.prev_card_btn.clicked.connect(self.prev_card)

    def end_round(self):
        self.view.quizwindow.hide()
        self.view.mainwindow.show()

    def next_card(self):
        self.model.game.deck.next_card()
        self.model.game.get_current_card_display()
        self.update_quiz()

    def prev_card(self):
        self.model.game.deck.prev_card()
        self.model.game.get_current_card_display()
        self.update_quiz()

    def quit(self):
        self.model.quit()
        QtWidgets.QApplication.quit()


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
        self.view.mainwindow.quit_btn.clicked.connect(self.quit)
        self.view.mainwindow.actionAbout.triggered.connect(self.about)
        self.view.mainwindow.player_btn.clicked.connect(self.select_player)
        self.view.mainwindow.deck_btn.clicked.connect(self.select_deck)

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

    def quit(self):
        self.model.quit()
        QtWidgets.QApplication.quit()