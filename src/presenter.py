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
        self.model.start_quiz()
        self.view.mainwindow.hide()
        self.view.quizwindow.show()
        self.view.quizwindow.quiz_progress_bar.setValue(0)
        self.quizwindow_presenter.update_quiz(self.model.get_current_card())

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

    def update_quiz(self, current_card):
        self.view.quizwindow.deck_title_label.setText(current_card.get("deck_title"))
        self.view.quizwindow.card_title_label.setText(current_card.get("card_title"))
        self.view.quizwindow.card_question_field.setText(
            current_card.get("card_contents")
        )
        self.view.quizwindow.card_answer_field.setPlainText(
            current_card.get("user_answer")
        )
        self.view.quizwindow.quiz_progress_bar.setValue(
            current_card.get("num_answered_cards")
        )

    def connectSignals(self):
        self.view.quizwindow.actionAbout.triggered.connect(self.about)
        self.view.quizwindow.actionEnd_Round.triggered.connect(self.end_round)
        self.view.quizwindow.end_quiz_btn.clicked.connect(self.end_round)
        self.view.quizwindow.next_card_btn.clicked.connect(self.next_card)
        self.view.quizwindow.prev_card_btn.clicked.connect(self.prev_card)

    def end_round(self):
        confirm = QtWidgets.QMessageBox.information(
            self.view.quizwindow,
            "End the Quiz?",
            "Are you sure you want to end the quiz and proceed to the scoring window?",
            QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel,
        )

        if confirm == QtWidgets.QMessageBox.Ok:
            logger.debug("User chose OK")
            self.view.quizwindow.hide()
            self.view.mainwindow.show()
        else:
            logger.debug("User chose Cancel")
            return

    def next_card(self):
        current_card = {
            "user_answer": self.view.quizwindow.card_answer_field.toPlainText(),
        }
        self.model.set_current_card(current_card)
        self.view.quizwindow.card_answer_field.clear()
        self.update_quiz(self.model.get_next_card())

    def prev_card(self):
        current_card = {
            "user_answer": self.view.quizwindow.card_answer_field.toPlainText(),
        }
        self.model.set_current_card(current_card)
        self.view.quizwindow.card_answer_field.clear()
        self.update_quiz(self.model.get_prev_card())
        return current_card

    def about(self):
        QtWidgets.QMessageBox.information(
            self.view.quizwindow,
            "About title",  # TODO: About title
            "About message",  # TODO: About message
        )

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

    def select_player(self):
        players_list = self.model.get_players_list()
        player_name = self.view.mainwindow.select_player_dialog(players_list)
        self.model.set_player(player_name)
        self.update_player()

    def update_player(self):
        player = self.model.get_player_name()
        self.view.mainwindow.player_label.setText(f"Selected player: {player}")

    def select_deck(self):
        decks_list = self.model.get_decks_list()
        deck_name = self.view.mainwindow.select_deck_dialog(decks_list)
        self.model.set_deck(deck_name)
        self.update_deck()

    def update_deck(self):
        deck = self.model.get_deck_name()
        if not deck:
            self.view.mainwindow.start_quiz_btn.setEnabled(False)
        else:
            self.view.mainwindow.start_quiz_btn.setEnabled(True)
        self.view.mainwindow.deck_label.setText(f"Selected deck: {deck}")

    def about(self):
        QtWidgets.QMessageBox.information(
            self.view.mainwindow,
            "About title",  # TODO: About title
            "About message",  # TODO: About message
        )

    def quit(self):
        self.model.quit()
        QtWidgets.QApplication.quit()
