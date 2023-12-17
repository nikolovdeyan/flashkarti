import logging
from PySide6 import QtCore, QtGui
from PySide6.QtWidgets import (
    QMainWindow,
    QDialog,
    QDialogButtonBox,
    QVBoxLayout,
    QLabel,
    QListWidget,
)

from ui.ui_main_window import Ui_MainWindow
from ui.ui_quiz_window import Ui_QuizWindow

logger = logging.getLogger(__name__)


class FkView(QtCore.QObject):
    def __init__(self):
        super(FkView, self).__init__()
        self.mainwindow = MainWindowView()
        self.quizwindow = QuizWindowView()


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
