import logging

from typing import List

from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QDialog,
    QDialogButtonBox,
    QVBoxLayout,
    QLabel,
    QListWidget,
    QButtonGroup,
    QMessageBox,
)

from ui.ui_main_window import Ui_MainWindow
from ui.ui_quiz_window import Ui_QuizWindow
from ui.ui_score_window import Ui_ScoreWindow
from ui.ui_designer_window import Ui_DesignerWindow

logger = logging.getLogger(__name__)


class FkView(QtCore.QObject):
    def __init__(self):
        super(FkView, self).__init__()
        self.mainwindow = MainWindowView()
        self.quizwindow = QuizWindowView()
        self.scorewindow = ScoreWindowView()
        self.designerwindow = DesignerWindowView()

    def select_player(self, players_list: List) -> str:
        """Provides a list dialog to select a player from a provided list.

        ### Args:
            `players_list (List)`: The list to be shown in the list dialog window.

        ### Returns:
            `str`: The name of the player selected.
        """
        return self.mainwindow.select_player_dialog(players_list)

    def select_deck_dialog(self, decks_list):
        dialog = SelectDeckDialog(decks_list)
        if dialog.exec():
            selected_deck = dialog.get_selected_deck()
            dialog.close()
        return selected_deck

    def start_quiz(self) -> None:
        """Starts a new quiz round."""
        self.mainwindow.hide()
        self.quizwindow.show()
        self.quizwindow.quiz_progress_bar.setValue(0)

    def start_designer(self) -> None:
        """Starts the designer window."""
        self.mainwindow.hide()
        self.designerwindow.show()

    def start_scoring(self) -> None:
        """Starts a new scoring window."""
        self.quizwindow.hide()
        self.scorewindow.show()

    def show_confirm_start_scoring_message(self) -> bool:
        confirm = QMessageBox.information(
            self.quizwindow,
            "Proceed to Scoring?",
            "Are you sure you want to end the quiz and proceed to scoring?",
            QMessageBox.Ok | QMessageBox.Cancel,
        )

        if confirm == QMessageBox.Ok:
            return True
        else:
            return False

    def show_about_message(self, window) -> bool:
        QMessageBox.information(
            window,
            "About title",  # TODO: About title
            "About message",  # TODO: About message
        )

    def quit(self):
        QApplication.quit()


class MainWindowView(QMainWindow, Ui_MainWindow):
    myQuitSignal = QtCore.Signal()

    def __init__(self):
        super(MainWindowView, self).__init__()
        self.setupUi(self)

    def select_player_dialog(self, players_list):
        dialog = SelectPlayerDialog(players_list)
        if dialog.exec():
            selected_player = dialog.get_selected_player()
            dialog.close()
        return selected_player

    def closeEvent(self, event):
        """
        This method overrides the mainwindow's closeEvent method
        which gets called when the user tries to close the mainwindow
        """
        logger.debug("closeEvent called")
        event.ignore()
        self.myQuitSignal.emit()


class DesignerWindowView(QMainWindow, Ui_DesignerWindow):
    myQuitSignal = QtCore.Signal()

    def __init__(self):
        super(DesignerWindowView, self).__init__()
        self.setupUi(self)

    def closeEvent(self, event):
        """
        This method overrides the mainwindow's closeEvent method
        which gets called when the user tries to close the mainwindow
        """
        logger.debug("closeEvent called")
        event.ignore()
        self.myQuitSignal.emit()

    def display_deck_cards(self, deck: list) -> None:
        self.deck_cards_listwidget.addItems(deck)

    def clear_deck_cards(self) -> None:
        self.deck_cards_listwidget.clear()

    def display_card(self, card_data: dict) -> None:
        self.card_title_lineedit.setText(card_data.get("card_title"))
        self.question_textedit.setHtml(card_data.get("card_contents"))
        self.expected_answer_textedit.setHtml(card_data.get("answer"))


class QuizWindowView(QMainWindow, Ui_QuizWindow):
    myQuitSignal = QtCore.Signal()

    def __init__(self):
        super(QuizWindowView, self).__init__()
        self.setupUi(self)

    def show_confirm_exit_quiz_message(self) -> bool:
        confirm = QMessageBox.information(
            self,
            "End the Quiz?",
            "Are you sure you want to end the quiz and return to the main menu?",
            QMessageBox.Ok | QMessageBox.Cancel,
        )

        if confirm == QMessageBox.Ok:
            return True
        else:
            return False

    def display_quiz_card(self, card_data):
        self.deck_title_label.setText(card_data.get("deck_title"))
        self.card_title_label.setText(card_data.get("card_title"))
        self.card_question_field.setText(card_data.get("card_contents"))
        self.card_answer_field.setPlainText(card_data.get("user_answer"))
        self.quiz_progress_bar.setValue(card_data.get("num_answered_cards"))


class ScoreWindowView(QMainWindow, Ui_ScoreWindow):
    myQuitSignal = QtCore.Signal()

    def __init__(self):
        super(ScoreWindowView, self).__init__()
        self.setupUi(self)

        # Scoring buttons are grouped in a QButtonGroup to take advantage of its
        # `exclusive` property allowing only one of them to be checked at a time.
        self.answer_buttons = QButtonGroup(self)
        self.answer_buttons.addButton(self.score_answer_complete_btn)
        self.answer_buttons.addButton(self.score_answer_partial_btn)
        self.answer_buttons.addButton(self.score_answer_incomplete_btn)

    def uncheck_answer_buttons(self):
        # The QButtonGroup will always have a checked button when set to exclusive.
        # To show a card where an answer has not been selected yet we use a little hack
        # where we disable the exclusivity of the box, set the buttons to unchecked and
        # then enable the exclusivity back again.
        # See: https://stackoverflow.com/a/1732385
        self.answer_buttons.setExclusive(False)
        self.score_answer_complete_btn.setChecked(False)
        self.score_answer_partial_btn.setChecked(False)
        self.score_answer_incomplete_btn.setChecked(False)
        self.answer_buttons.setExclusive(True)

    def display_scoring_card(self, current_card):
        self.deck_title_label.setText(current_card.get("deck_title"))
        self.score_card_title_label.setText(current_card.get("card_title"))
        self.score_card_question_field.setText(current_card.get("card_contents"))
        self.score_card_answer_field.setPlainText(current_card.get("user_answer"))
        self.score_card_expected_answer_field.setPlainText(current_card.get("answer"))
        match current_card.get("answer_score"):
            case 1:
                self.score_answer_complete_btn.setChecked(True)
            case 0.5:
                self.score_answer_partial_btn.setChecked(True)
            case 0:
                self.score_answer_incomplete_btn.setChecked(True)
            case None:
                self.uncheck_answer_buttons()

    def show_score_result_dialog(self):
        dialog = ScoreResultDialog()
        dialog.raise_()
        if dialog.exec():
            dialog.close()
        return


class ScoreResultDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setModal(True)
        self.setMinimumWidth(300)
        self.setWindowTitle("Quiz Results")
        results_label = QLabel("Quiz Results:")

        ok_btn = QDialogButtonBox.Ok
        self.button_box = QDialogButtonBox(ok_btn)

        self.layout = QVBoxLayout()
        self.layout.addWidget(results_label)
        self.layout.addWidget(self.button_box)

        self.button_box.accepted.connect(self.accept)

        self.setLayout(self.layout)


class SelectPlayerDialog(QDialog):
    def __init__(self, players_list):
        super().__init__()

        self.setMinimumWidth(300)
        self.setWindowTitle("Select player")
        message = QLabel("Please select player")

        q_btn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.button_box = QDialogButtonBox(q_btn)

        self.players_list = QListWidget()
        self.players_list.addItems(players_list)

        self.layout = QVBoxLayout()
        self.layout.addWidget(message)
        self.layout.addWidget(self.players_list)
        self.layout.addWidget(self.button_box)

        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        self.setLayout(self.layout)

    def get_selected_player(self):
        if self.players_list.currentItem():
            return self.players_list.currentItem().text()
        else:
            return ""


class SelectDeckDialog(QDialog):
    def __init__(self, decks_list):
        super().__init__()

        self.setMinimumWidth(300)
        self.setWindowTitle("Select deck")
        message = QLabel("Please select deck")

        q_btn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.button_box = QDialogButtonBox(q_btn)

        self.decks_list = QListWidget()
        self.decks_list.addItems(decks_list)

        self.layout = QVBoxLayout()
        self.layout.addWidget(message)
        self.layout.addWidget(self.decks_list)
        self.layout.addWidget(self.button_box)

        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        self.setLayout(self.layout)

    def get_selected_deck(self):
        if self.decks_list.currentItem():
            return self.decks_list.currentItem().text()
        else:
            return ""
