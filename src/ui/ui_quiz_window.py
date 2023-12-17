# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'quiz_window.ui'
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
    QMenu, QMenuBar, QPlainTextEdit, QProgressBar,
    QPushButton, QSizePolicy, QStatusBar, QTextBrowser,
    QWidget)

class Ui_QuizWindow(object):
    def setupUi(self, QuizWindow):
        if not QuizWindow.objectName():
            QuizWindow.setObjectName(u"QuizWindow")
        QuizWindow.resize(963, 600)
        self.actionEnd_Round = QAction(QuizWindow)
        self.actionEnd_Round.setObjectName(u"actionEnd_Round")
        self.actionQuit = QAction(QuizWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionAbout = QAction(QuizWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(QuizWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.deck_title_label = QLabel(self.centralwidget)
        self.deck_title_label.setObjectName(u"deck_title_label")
        self.deck_title_label.setGeometry(QRect(30, 16, 901, 21))
        font = QFont()
        font.setPointSize(14)
        self.deck_title_label.setFont(font)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 50, 921, 441))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.card_title_label = QLabel(self.frame)
        self.card_title_label.setObjectName(u"card_title_label")
        self.card_title_label.setGeometry(QRect(10, 16, 891, 21))
        font1 = QFont()
        font1.setPointSize(12)
        self.card_title_label.setFont(font1)
        self.card_question_field = QTextBrowser(self.frame)
        self.card_question_field.setObjectName(u"card_question_field")
        self.card_question_field.setGeometry(QRect(10, 50, 441, 381))
        self.card_answer_field = QPlainTextEdit(self.frame)
        self.card_answer_field.setObjectName(u"card_answer_field")
        self.card_answer_field.setGeometry(QRect(470, 50, 441, 381))
        self.next_card_btn = QPushButton(self.centralwidget)
        self.next_card_btn.setObjectName(u"next_card_btn")
        self.next_card_btn.setGeometry(QRect(840, 500, 101, 31))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.next_card_btn.sizePolicy().hasHeightForWidth())
        self.next_card_btn.setSizePolicy(sizePolicy)
        self.next_card_btn.setFont(font1)
        self.prev_card_btn = QPushButton(self.centralwidget)
        self.prev_card_btn.setObjectName(u"prev_card_btn")
        self.prev_card_btn.setGeometry(QRect(20, 500, 101, 31))
        sizePolicy.setHeightForWidth(self.prev_card_btn.sizePolicy().hasHeightForWidth())
        self.prev_card_btn.setSizePolicy(sizePolicy)
        self.prev_card_btn.setFont(font1)
        self.quiz_progress_bar = QProgressBar(self.centralwidget)
        self.quiz_progress_bar.setObjectName(u"quiz_progress_bar")
        self.quiz_progress_bar.setGeometry(QRect(130, 500, 701, 31))
        self.quiz_progress_bar.setFont(font1)
        self.quiz_progress_bar.setValue(24)
        QuizWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(QuizWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 963, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        QuizWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(QuizWindow)
        self.statusbar.setObjectName(u"statusbar")
        QuizWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionEnd_Round)
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(QuizWindow)

        QMetaObject.connectSlotsByName(QuizWindow)
    # setupUi

    def retranslateUi(self, QuizWindow):
        QuizWindow.setWindowTitle(QCoreApplication.translate("QuizWindow", u"MainWindow", None))
        self.actionEnd_Round.setText(QCoreApplication.translate("QuizWindow", u"End Round", None))
        self.actionQuit.setText(QCoreApplication.translate("QuizWindow", u"Quit", None))
        self.actionAbout.setText(QCoreApplication.translate("QuizWindow", u"About", None))
        self.deck_title_label.setText(QCoreApplication.translate("QuizWindow", u"TextLabel", None))
        self.card_title_label.setText(QCoreApplication.translate("QuizWindow", u"TextLabel", None))
        self.next_card_btn.setText(QCoreApplication.translate("QuizWindow", u"Next", None))
        self.prev_card_btn.setText(QCoreApplication.translate("QuizWindow", u"Previous", None))
        self.menuFile.setTitle(QCoreApplication.translate("QuizWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("QuizWindow", u"Help", None))
    # retranslateUi
