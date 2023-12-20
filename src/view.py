import logging

from typing import List

from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import (
    QMainWindow,
    QDialog,
    QDialogButtonBox,
    QVBoxLayout,
    QLabel,
    QListWidget,
    QButtonGroup,
)

from ui.ui_main_window import Ui_MainWindow
from ui.ui_quiz_window import Ui_QuizWindow
from ui.ui_score_window import Ui_ScoreWindow

logger = logging.getLogger(__name__)


class FkView(QtCore.QObject):
    def __init__(self):
        super(FkView, self).__init__()
        self.mainwindow = MainWindowView()
        self.quizwindow = QuizWindowView()
        self.scorewindow = ScoreWindowView()

    def select_player(self, players_list: List) -> str:
        """Provides a list dialog to select a player from a provided list.

        ### Args:
            `players_list (List)`: The list to be shown in the list dialog window.

        ### Returns:
            `str`: The name of the player selected.
        """
        return self.mainwindow.select_player_dialog(players_list)

    def start_quiz(self) -> None:
        """Starts a new quiz round."""
        self.mainwindow.hide()
        self.quizwindow.show()
        self.quizwindow.quiz_progress_bar.setValue(0)

    def start_scoring(self) -> None:
        """Starts a new scoring window."""
        self.quizwindow.hide()
        self.scorewindow.show()


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

    def select_deck_dialog(self, decks_list):
        dialog = SelectDeckDialog(decks_list)
        if dialog.exec():
            selected_deck = dialog.get_selected_deck()
            dialog.close()
        return selected_deck

    def closeEvent(self, event):
        """
        This method overrides the mainwindow's closeEvent method
        which gets called when the user tries to close the mainwindow
        """
        logger.debug("closeEvent called")
        event.ignore()
        self.myQuitSignal.emit()


class QuizWindowView(QMainWindow, Ui_QuizWindow):
    myQuitSignal = QtCore.Signal()

    def __init__(self):
        super(QuizWindowView, self).__init__()
        self.setupUi(self)


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
