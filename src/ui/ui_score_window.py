# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'score_window.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenu, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QStatusBar, QTextBrowser, QWidget)

class Ui_ScoreWindow(object):
    def setupUi(self, ScoreWindow):
        if not ScoreWindow.objectName():
            ScoreWindow.setObjectName(u"ScoreWindow")
        ScoreWindow.resize(963, 640)
        self.actionExit_Scoring = QAction(ScoreWindow)
        self.actionExit_Scoring.setObjectName(u"actionExit_Scoring")
        self.actionQuit = QAction(ScoreWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionAbout = QAction(ScoreWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(ScoreWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.score_deck_title_label = QLabel(self.centralwidget)
        self.score_deck_title_label.setObjectName(u"score_deck_title_label")
        self.score_deck_title_label.setGeometry(QRect(20, 20, 901, 21))
        font = QFont()
        font.setPointSize(14)
        self.score_deck_title_label.setFont(font)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 60, 921, 451))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.score_card_title_label = QLabel(self.frame)
        self.score_card_title_label.setObjectName(u"score_card_title_label")
        self.score_card_title_label.setGeometry(QRect(10, 16, 891, 21))
        font1 = QFont()
        font1.setPointSize(12)
        self.score_card_title_label.setFont(font1)
        self.score_card_question_field = QTextBrowser(self.frame)
        self.score_card_question_field.setObjectName(u"score_card_question_field")
        self.score_card_question_field.setGeometry(QRect(10, 50, 441, 391))
        self.score_card_answer_field = QPlainTextEdit(self.frame)
        self.score_card_answer_field.setObjectName(u"score_card_answer_field")
        self.score_card_answer_field.setGeometry(QRect(470, 70, 441, 161))
        self.score_card_expected_answer_field = QPlainTextEdit(self.frame)
        self.score_card_expected_answer_field.setObjectName(u"score_card_expected_answer_field")
        self.score_card_expected_answer_field.setGeometry(QRect(470, 280, 441, 161))
        self.score_card_title_label_2 = QLabel(self.frame)
        self.score_card_title_label_2.setObjectName(u"score_card_title_label_2")
        self.score_card_title_label_2.setGeometry(QRect(470, 40, 261, 21))
        self.score_card_title_label_2.setFont(font1)
        self.score_card_title_label_3 = QLabel(self.frame)
        self.score_card_title_label_3.setObjectName(u"score_card_title_label_3")
        self.score_card_title_label_3.setGeometry(QRect(470, 250, 261, 21))
        self.score_card_title_label_3.setFont(font1)
        self.score_next_card_btn = QPushButton(self.centralwidget)
        self.score_next_card_btn.setObjectName(u"score_next_card_btn")
        self.score_next_card_btn.setGeometry(QRect(840, 520, 101, 31))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.score_next_card_btn.sizePolicy().hasHeightForWidth())
        self.score_next_card_btn.setSizePolicy(sizePolicy)
        self.score_next_card_btn.setFont(font1)
        self.score_prev_card_btn = QPushButton(self.centralwidget)
        self.score_prev_card_btn.setObjectName(u"score_prev_card_btn")
        self.score_prev_card_btn.setGeometry(QRect(730, 520, 101, 31))
        sizePolicy.setHeightForWidth(self.score_prev_card_btn.sizePolicy().hasHeightForWidth())
        self.score_prev_card_btn.setSizePolicy(sizePolicy)
        self.score_prev_card_btn.setFont(font1)
        self.end_scoring_btn = QPushButton(self.centralwidget)
        self.end_scoring_btn.setObjectName(u"end_scoring_btn")
        self.end_scoring_btn.setGeometry(QRect(840, 560, 101, 31))
        sizePolicy.setHeightForWidth(self.end_scoring_btn.sizePolicy().hasHeightForWidth())
        self.end_scoring_btn.setSizePolicy(sizePolicy)
        self.end_scoring_btn.setFont(font1)
        self.score_answer_complete_btn = QPushButton(self.centralwidget)
        self.score_answer_complete_btn.setObjectName(u"score_answer_complete_btn")
        self.score_answer_complete_btn.setGeometry(QRect(200, 520, 101, 31))
        sizePolicy.setHeightForWidth(self.score_answer_complete_btn.sizePolicy().hasHeightForWidth())
        self.score_answer_complete_btn.setSizePolicy(sizePolicy)
        self.score_answer_complete_btn.setFont(font1)
        self.score_card_title_label_4 = QLabel(self.centralwidget)
        self.score_card_title_label_4.setObjectName(u"score_card_title_label_4")
        self.score_card_title_label_4.setGeometry(QRect(20, 520, 161, 31))
        self.score_card_title_label_4.setFont(font1)
        self.score_answer_partial_btn = QPushButton(self.centralwidget)
        self.score_answer_partial_btn.setObjectName(u"score_answer_partial_btn")
        self.score_answer_partial_btn.setGeometry(QRect(310, 520, 101, 31))
        sizePolicy.setHeightForWidth(self.score_answer_partial_btn.sizePolicy().hasHeightForWidth())
        self.score_answer_partial_btn.setSizePolicy(sizePolicy)
        self.score_answer_partial_btn.setFont(font1)
        self.score_answer_incomplete_btn = QPushButton(self.centralwidget)
        self.score_answer_incomplete_btn.setObjectName(u"score_answer_incomplete_btn")
        self.score_answer_incomplete_btn.setGeometry(QRect(420, 520, 101, 31))
        sizePolicy.setHeightForWidth(self.score_answer_incomplete_btn.sizePolicy().hasHeightForWidth())
        self.score_answer_incomplete_btn.setSizePolicy(sizePolicy)
        self.score_answer_incomplete_btn.setFont(font1)
        ScoreWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(ScoreWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 963, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        ScoreWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(ScoreWindow)
        self.statusbar.setObjectName(u"statusbar")
        ScoreWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionExit_Scoring)
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(ScoreWindow)

        QMetaObject.connectSlotsByName(ScoreWindow)
    # setupUi

    def retranslateUi(self, ScoreWindow):
        ScoreWindow.setWindowTitle(QCoreApplication.translate("ScoreWindow", u"MainWindow", None))
        self.actionExit_Scoring.setText(QCoreApplication.translate("ScoreWindow", u"Exit Scoring", None))
        self.actionQuit.setText(QCoreApplication.translate("ScoreWindow", u"Quit", None))
        self.actionAbout.setText(QCoreApplication.translate("ScoreWindow", u"About", None))
        self.score_deck_title_label.setText(QCoreApplication.translate("ScoreWindow", u"TextLabel", None))
        self.score_card_title_label.setText(QCoreApplication.translate("ScoreWindow", u"TextLabel", None))
        self.score_card_title_label_2.setText(QCoreApplication.translate("ScoreWindow", u"Your Answer:", None))
        self.score_card_title_label_3.setText(QCoreApplication.translate("ScoreWindow", u"Expected Answer", None))
        self.score_next_card_btn.setText(QCoreApplication.translate("ScoreWindow", u"Next", None))
        self.score_prev_card_btn.setText(QCoreApplication.translate("ScoreWindow", u"Previous", None))
        self.end_scoring_btn.setText(QCoreApplication.translate("ScoreWindow", u"End Scoring", None))
        self.score_answer_complete_btn.setText(QCoreApplication.translate("ScoreWindow", u"Complete", None))
        self.score_card_title_label_4.setText(QCoreApplication.translate("ScoreWindow", u"Score Your Answer:", None))
        self.score_answer_partial_btn.setText(QCoreApplication.translate("ScoreWindow", u"Partial", None))
        self.score_answer_incomplete_btn.setText(QCoreApplication.translate("ScoreWindow", u"Incomplete", None))
        self.menuFile.setTitle(QCoreApplication.translate("ScoreWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("ScoreWindow", u"Help", None))
    # retranslateUi

