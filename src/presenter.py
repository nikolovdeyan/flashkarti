import logging
from PySide6 import QtCore

logger = logging.getLogger(__name__)


class FkPresenter(QtCore.QObject):
    def __init__(self, model, view, app):
        super(FkPresenter, self).__init__()

        self.model = model
        self.view = view
        self.app = app

        self.mainwindow_presenter = MainWindowPresenter(model, view, app)
        self.quizwindow_presenter = QuizWindowPresenter(model, view, app)
        self.scoringwinow_presenter = ScoringWindowPresenter(model, view, app)

        self.connectSignals()
        self.view.mainwindow.show()

    def connectSignals(self):
        self.view.mainwindow.myQuitSignal.connect(self.quit)
        self.view.quizwindow.myQuitSignal.connect(self.quit)
        self.view.scorewindow.myQuitSignal.connect(self.quit)
        self.view.mainwindow.actionQuit.triggered.connect(self.quit)
        self.view.quizwindow.actionQuit.triggered.connect(self.quit)
        self.view.scorewindow.actionQuit.triggered.connect(self.quit)
        self.view.mainwindow.start_quiz_btn.clicked.connect(self.on_start_quiz_clicked)
        self.view.quizwindow.start_scoring_btn.clicked.connect(
            self.on_start_scoring_clicked
        )

    def on_start_quiz_clicked(self):
        self.model.start_quiz()
        self.view.start_quiz()
        self.quizwindow_presenter.update_quiz_display(
            self.model.get_current_card_display()
        )

    def on_start_scoring_clicked(self):
        self.model.set_current_card(
            {"user_answer": self.view.quizwindow.card_answer_field.toPlainText()}
        )
        confirm = self.view.show_confirm_start_scoring_message()
        if confirm:
            self.scoringwinow_presenter.update_scoring_display(
                self.model.get_current_card_display()
            )
            self.view.quizwindow.hide()
            self.view.scorewindow.show()
        else:
            return

    def quit(self):
        self.model.quit()
        self.view.quit()


class ScoringWindowPresenter(QtCore.QObject):
    def __init__(self, model, view, app):
        super(ScoringWindowPresenter, self).__init__()

        self.model = model
        self.view = view
        self.app = app

        self.connectSignals()

    def connectSignals(self):
        self.view.scorewindow.actionAbout.triggered.connect(self.about)
        self.view.scorewindow.actionExit_Scoring.triggered.connect(
            self.on_exit_scoring_clicked
        )
        self.view.scorewindow.end_scoring_btn.clicked.connect(
            self.on_end_scoring_clicked
        )
        self.view.scorewindow.score_next_card_btn.clicked.connect(
            self.on_score_next_card_clicked
        )
        self.view.scorewindow.score_prev_card_btn.clicked.connect(
            self.on_score_prev_card_clicked
        )

    def update_scoring_display(self, current_card):
        self.view.scorewindow.deck_title_label.setText(current_card.get("deck_title"))
        self.view.scorewindow.score_card_title_label.setText(
            current_card.get("card_title")
        )
        self.view.scorewindow.score_card_question_field.setText(
            current_card.get("card_contents")
        )
        self.view.scorewindow.score_card_answer_field.setPlainText(
            current_card.get("user_answer")
        )
        self.view.scorewindow.score_card_expected_answer_field.setPlainText(
            current_card.get("answer")
        )
        logger.debug(
            f"got a card with answer_score: {current_card.get('answer_score')}"
        )
        match current_card.get("answer_score"):
            case 1:
                self.view.scorewindow.score_answer_complete_btn.setChecked(True)
            case 0.5:
                self.view.scorewindow.score_answer_partial_btn.setChecked(True)
            case 0:
                self.view.scorewindow.score_answer_incomplete_btn.setChecked(True)
            case None:
                self.view.scorewindow.uncheck_answer_buttons()

    def on_score_next_card_clicked(self):
        score = self.score_answer()
        self.model.set_current_card({"answer_score": score})
        self.update_scoring_display(self.model.get_next_card_display())

    def on_score_prev_card_clicked(self):
        score = self.score_answer()
        self.model.set_current_card({"answer_score": score})
        self.update_scoring_display(self.model.get_prev_card_display())

    def on_exit_scoring_clicked(self):
        logger.debug("on_exit_scoring_clicked called")

    def on_end_scoring_clicked(self):
        logger.debug("on_end_scoring_clicked called")

    def score_answer(self) -> float:
        if self.view.scorewindow.score_answer_complete_btn.isChecked():
            return 1
        elif self.view.scorewindow.score_answer_partial_btn.isChecked():
            return 0.5
        elif self.view.scorewindow.score_answer_incomplete_btn.isChecked():
            return 0

    def about(self):
        self.view.show_about_message(self.view.scorewindow)

    def quit(self):
        self.model.quit()
        self.view.quit()


class QuizWindowPresenter(QtCore.QObject):
    def __init__(self, model, view, app):
        super(QuizWindowPresenter, self).__init__()

        self.model = model
        self.view = view
        self.app = app

        self.connectSignals()

    def connectSignals(self):
        self.view.quizwindow.actionAbout.triggered.connect(self.about)
        self.view.quizwindow.actionExit_Quiz.triggered.connect(
            self.on_exit_quiz_clicked
        )
        self.view.quizwindow.next_card_btn.clicked.connect(self.on_next_card_clicked)
        self.view.quizwindow.prev_card_btn.clicked.connect(self.on_prev_card_clicked)

    def on_exit_quiz_clicked(self):
        confirm = self.view.quizwindow.show_confirm_exit_quiz_message()
        if confirm:
            self.view.quizwindow.hide()
            self.view.mainwindow.show()
        else:
            return

    def on_next_card_clicked(self):
        self.model.set_current_card(
            {"user_answer": self.view.quizwindow.card_answer_field.toPlainText()}
        )
        self.view.quizwindow.card_answer_field.clear()
        self.update_quiz_display(self.model.get_next_card_display())

    def on_prev_card_clicked(self):
        self.model.set_current_card(
            {"user_answer": self.view.quizwindow.card_answer_field.toPlainText()}
        )
        self.view.quizwindow.card_answer_field.clear()
        self.update_quiz_display(self.model.get_prev_card_display())

    def update_quiz_display(self, current_card):
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

    def about(self):
        self.view.show_about_message(self.view.quizwindow)

    def quit(self):
        self.model.quit()
        self.view.quit()


class MainWindowPresenter(QtCore.QObject):
    def __init__(self, model, view, app):
        super(MainWindowPresenter, self).__init__()

        self.model = model
        self.view = view
        self.app = app

        self.update_player_display()
        self.update_deck_display()
        self.connectSignals()

    def connectSignals(self):
        self.view.mainwindow.quit_btn.clicked.connect(self.quit)
        self.view.mainwindow.actionAbout.triggered.connect(self.about)
        self.view.mainwindow.player_btn.clicked.connect(self.on_select_player_clicked)
        self.view.mainwindow.deck_btn.clicked.connect(self.on_select_deck_clicked)

    def on_select_deck_clicked(self):
        decks_list = self.model.get_decks_list()
        deck_name = self.view.mainwindow.select_deck_dialog(decks_list)
        self.model.set_deck(deck_name)
        self.update_deck_display()

    def on_select_player_clicked(self):
        players_list = self.model.get_players_list()
        player_name = self.view.select_player(players_list)
        self.model.set_player(player_name)
        self.update_player_display()

    def update_deck_display(self):
        deck = self.model.get_deck_name()
        if not deck:
            self.view.mainwindow.start_quiz_btn.setEnabled(False)
        else:
            self.view.mainwindow.start_quiz_btn.setEnabled(True)
        self.view.mainwindow.deck_label.setText(f"Selected deck: {deck}")

    def update_player_display(self):
        player = self.model.get_player_name()
        self.view.mainwindow.player_label.setText(f"Selected player: {player}")

    def about(self):
        self.view.show_about_message(self.view.mainwindow)

    def quit(self):
        self.model.quit()
        self.view.quit()
