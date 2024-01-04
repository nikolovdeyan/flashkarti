import logging
from PySide6 import QtCore

logger = logging.getLogger(__name__)


class FkPresenter(QtCore.QObject):
    def __init__(self, model, view, app) -> None:
        super(FkPresenter, self).__init__()

        self.model = model
        self.view = view
        self.app = app

        self.menuwindow_presenter = MenuWindowPresenter(model, view, app)
        self.quizwindow_presenter = QuizWindowPresenter(model, view, app)
        self.scoringwinow_presenter = ScoringWindowPresenter(model, view, app)
        self.designerwindow_presenter = DesignerWindowPresenter(model, view, app)

        self.view.start_menu()


class MenuWindowPresenter(QtCore.QObject):
    def __init__(self, model, view, app) -> None:
        super(MenuWindowPresenter, self).__init__()

        self.model = model
        self.view = view
        self.app = app

        self.update_player_display()
        self.update_deck_display()
        self.update_start_quiz_btn_display()
        self.connectSignals()

    def connectSignals(self) -> None:
        self.view.menuwindow.myQuitSignal.connect(self.quit)
        self.view.menuwindow.actionQuit.triggered.connect(self.quit)
        self.view.menuwindow.quit_btn.clicked.connect(self.quit)
        self.view.menuwindow.actionAbout.triggered.connect(self.about)
        self.view.menuwindow.player_btn.clicked.connect(self.on_select_player_clicked)
        self.view.menuwindow.deck_btn.clicked.connect(self.on_select_deck_clicked)
        self.view.menuwindow.designer_btn.clicked.connect(self.on_designer_clicked)
        self.view.menuwindow.start_quiz_btn.clicked.connect(self.on_start_quiz_clicked)

    def on_select_deck_clicked(self) -> None:
        decks_list = self.model.get_decks_list()
        deck_name = self.view.select_deck_dialog(decks_list)
        self.model.load_deck(deck_name)
        self.update_deck_display()
        self.update_start_quiz_btn_display()

    def on_select_player_clicked(self) -> None:
        players_list = self.model.list_players_names()
        player_name = self.view.select_player(players_list)
        self.model.load_player(player_name)
        self.update_player_display()
        self.update_start_quiz_btn_display()

    def on_designer_clicked(self) -> None:
        self.view.start_designer()

    def on_start_quiz_clicked(self) -> None:
        self.model.start_quiz()
        self.view.start_quiz()
        self.view.quizwindow.display_quiz_card(self.model.get_current_card_display())

    def update_deck_display(self) -> None:
        deck = self.model.get_deck_name()
        self.view.menuwindow.deck_label.setText(f"Selected deck: {deck}")

    def update_player_display(self) -> None:
        player = self.model.current_player_name()
        self.view.menuwindow.player_label.setText(f"Selected player: {player}")

    def update_start_quiz_btn_display(self) -> None:
        player = self.model.current_player_name()
        deck = self.model.get_deck_name()
        if deck and player:
            self.view.menuwindow.start_quiz_btn.setEnabled(True)
        else:
            self.view.menuwindow.start_quiz_btn.setEnabled(False)

    def about(self) -> None:
        self.view.show_about_message(self.view.menuwindow)

    def quit(self) -> None:
        self.model.quit()
        self.view.quit()


class QuizWindowPresenter(QtCore.QObject):
    def __init__(self, model, view, app):
        super(QuizWindowPresenter, self).__init__()

        self.model = model
        self.view = view
        self.app = app

        self.connectSignals()

    def connectSignals(self) -> None:
        self.view.quizwindow.myQuitSignal.connect(self.quit)
        self.view.quizwindow.actionQuit.triggered.connect(self.quit)
        self.view.quizwindow.actionExit_Quiz.triggered.connect(
            self.on_exit_quiz_clicked
        )
        self.view.quizwindow.actionAbout.triggered.connect(self.about)
        self.view.quizwindow.next_card_btn.clicked.connect(self.on_next_card_clicked)
        self.view.quizwindow.prev_card_btn.clicked.connect(self.on_prev_card_clicked)
        self.view.quizwindow.start_scoring_btn.clicked.connect(
            self.on_start_scoring_clicked
        )

    def on_exit_quiz_clicked(self) -> None:
        confirm = self.view.quizwindow.show_confirm_exit_quiz_message()
        if confirm:
            self.view.start_menu()
        else:
            return

    def on_next_card_clicked(self) -> None:
        self.model.set_current_card(
            {"user_answer": self.view.quizwindow.card_answer_field.toPlainText()}
        )
        self.view.quizwindow.card_answer_field.clear()
        self.view.quizwindow.display_quiz_card(self.model.get_next_card_display())

    def on_prev_card_clicked(self) -> None:
        self.model.set_current_card(
            {"user_answer": self.view.quizwindow.card_answer_field.toPlainText()}
        )
        self.view.quizwindow.card_answer_field.clear()
        self.view.quizwindow.display_quiz_card(self.model.get_prev_card_display())

    def on_start_scoring_clicked(self) -> None:
        self.model.set_current_card(
            {"user_answer": self.view.quizwindow.card_answer_field.toPlainText()}
        )
        confirm = self.view.show_confirm_start_scoring_message()
        if confirm:
            self.view.scorewindow.display_scoring_card(
                self.model.get_current_card_display()
            )
            self.view.start_scoring()
        else:
            return

    def about(self) -> None:
        self.view.show_about_message(self.view.quizwindow)

    def quit(self) -> None:
        self.model.quit()
        self.view.quit()


class ScoringWindowPresenter(QtCore.QObject):
    def __init__(self, model, view, app):
        super(ScoringWindowPresenter, self).__init__()

        self.model = model
        self.view = view
        self.app = app

        self.connectSignals()

    def connectSignals(self) -> None:
        self.view.scorewindow.myQuitSignal.connect(self.quit)
        self.view.scorewindow.actionQuit.triggered.connect(self.quit)
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

    def on_score_next_card_clicked(self) -> None:
        score = self.score_answer()
        self.model.set_current_card({"answer_score": score})
        self.view.scorewindow.display_scoring_card(self.model.get_next_card_display())

    def on_score_prev_card_clicked(self) -> None:
        score = self.score_answer()
        self.model.set_current_card({"answer_score": score})
        self.view.scorewindow.display_scoring_card(self.model.get_prev_card_display())

    def on_exit_scoring_clicked(self) -> None:
        self.view.start_menu()

    def on_end_scoring_clicked(self) -> None:
        score = self.score_answer()
        self.model.set_current_card({"answer_score": score})
        quiz_scores = self.model.calculate_quiz_scores()

        num_correct = 0
        num_partial = 0
        num_incorrect = 0
        for question in quiz_scores:
            if question[1] == 1:
                num_correct += 1
            elif question[1] == 0.5:
                num_partial += 1
            elif question[1] == 0:
                num_incorrect += 1

        self.model.update_player_scores(num_correct, num_partial, num_incorrect)
        self.view.scorewindow.show_score_result_dialog(quiz_scores)
        self.view.start_menu()

    def score_answer(self) -> float:
        if self.view.scorewindow.score_answer_complete_btn.isChecked():
            return 1
        elif self.view.scorewindow.score_answer_partial_btn.isChecked():
            return 0.5
        elif self.view.scorewindow.score_answer_incomplete_btn.isChecked():
            return 0

    def about(self) -> None:
        self.view.show_about_message(self.view.scorewindow)

    def quit(self) -> None:
        self.model.quit()
        self.view.quit()


class DesignerWindowPresenter(QtCore.QObject):
    def __init__(self, model, view, app):
        super(DesignerWindowPresenter, self).__init__()

        self.model = model
        self.view = view
        self.app = app

        self.connectSignals()

    def connectSignals(self) -> None:
        self.view.designerwindow.myQuitSignal.connect(self.quit)
        self.view.designerwindow.actionExit_Designer.triggered.connect(
            self.on_exit_designer_clicked
        )
        self.view.designerwindow.actionQuit.triggered.connect(self.quit)
        self.view.designerwindow.actionAbout.triggered.connect(self.about)
        self.view.designerwindow.new_deck_btn.clicked.connect(self.on_new_deck_button)
        self.view.designerwindow.load_deck_btn.clicked.connect(
            self.on_load_deck_clicked
        )
        self.view.designerwindow.save_deck_btn.clicked.connect(
            self.on_save_deck_clicked
        )
        self.view.designerwindow.add_card_btn.clicked.connect(self.on_add_card_clicked)
        self.view.designerwindow.delete_card_btn.clicked.connect(
            self.on_delete_card_clicked
        )
        self.view.designerwindow.save_card_btn.clicked.connect(
            self.on_save_card_clicked
        )
        self.view.designerwindow.toggle_card_preview_btn.toggled.connect(
            self.on_card_preview_clicked
        )
        self.view.designerwindow.exit_designer_btn.clicked.connect(
            self.on_exit_designer_clicked
        )
        self.view.designerwindow.deck_cards_listwidget.itemClicked.connect(
            self.on_deck_cards_item_clicked
        )

    def on_deck_cards_item_clicked(self, item) -> None:
        card_title = item.text()
        self.model.set_current_card_index(card_title)
        self.view.designerwindow.display_card(
            self.model.get_card_display_by_card_title(card_title)
        )

    def on_new_deck_button(self) -> None:
        deck_title = self.view.designerwindow.new_deck_dialog()
        self.model.new_deck(deck_title)

    def on_load_deck_clicked(self) -> None:
        decks_list = self.model.get_decks_list()
        deck_title = self.view.select_deck_dialog(decks_list)
        self.model.load_deck(deck_title)
        self.view.designerwindow.display_deck_title(deck_title)
        self.view.designerwindow.clear_deck_cards()
        self.view.designerwindow.display_deck_cards(self.model.list_card_titles())

    def on_save_deck_clicked(self) -> None:
        confirm = self.view.designerwindow.show_confirm_save_deck_message()
        if confirm:
            self.model.save_deck()
        else:
            return

    def on_add_card_clicked(self) -> None:
        self.model.create_new_card()
        self.view.designerwindow.clear_deck_cards()
        self.view.designerwindow.display_deck_cards(self.model.list_card_titles())

    def on_delete_card_clicked(self) -> None:
        self.model.delete_card_by_title(self.view.designerwindow.get_selected_card())
        self.view.designerwindow.clear_deck_cards()
        self.view.designerwindow.display_deck_cards(self.model.list_card_titles())

    def on_save_card_clicked(self) -> None:
        self.model.set_current_card(
            {
                "card_title": self.view.designerwindow.card_title_lineedit.text(),
                "card_contents": self.view.designerwindow.question_textedit.toPlainText(),
                "answer": self.view.designerwindow.expected_answer_textedit.toPlainText(),
            }
        )
        self.view.designerwindow.clear_deck_cards()
        self.view.designerwindow.display_deck_cards(self.model.list_card_titles())

    def on_card_preview_clicked(self) -> None:
        card_title = self.view.designerwindow.get_selected_card()
        if not card_title:
            return
        self.view.designerwindow.display_card(
            self.model.get_card_display_by_card_title(card_title)
        )

    def on_exit_designer_clicked(self) -> None:
        self.model.clear_deck()
        self.view.start_menu()

    def about(self) -> None:
        self.view.show_about_message(self.view.menuwindow)

    def quit(self) -> None:
        self.model.quit()
        self.view.quit()
