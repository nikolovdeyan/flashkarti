# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designer_window.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTextEdit, QToolBar, QVBoxLayout, QWidget)

class Ui_DesignerWindow(object):
    def setupUi(self, DesignerWindow):
        if not DesignerWindow.objectName():
            DesignerWindow.setObjectName(u"DesignerWindow")
        DesignerWindow.resize(946, 640)
        self.actionExit_Designer = QAction(DesignerWindow)
        self.actionExit_Designer.setObjectName(u"actionExit_Designer")
        self.actionQuit = QAction(DesignerWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionAbout = QAction(DesignerWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(DesignerWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.deck_designer_label = QLabel(self.centralwidget)
        self.deck_designer_label.setObjectName(u"deck_designer_label")
        self.deck_designer_label.setGeometry(QRect(400, 10, 151, 31))
        font = QFont()
        font.setPointSize(16)
        self.deck_designer_label.setFont(font)
        self.new_deck_btn = QPushButton(self.centralwidget)
        self.new_deck_btn.setObjectName(u"new_deck_btn")
        self.new_deck_btn.setGeometry(QRect(10, 540, 111, 31))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.new_deck_btn.sizePolicy().hasHeightForWidth())
        self.new_deck_btn.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(12)
        self.new_deck_btn.setFont(font1)
        self.new_deck_btn.setCheckable(False)
        self.new_deck_btn.setChecked(False)
        self.load_deck_btn = QPushButton(self.centralwidget)
        self.load_deck_btn.setObjectName(u"load_deck_btn")
        self.load_deck_btn.setGeometry(QRect(130, 540, 111, 31))
        sizePolicy.setHeightForWidth(self.load_deck_btn.sizePolicy().hasHeightForWidth())
        self.load_deck_btn.setSizePolicy(sizePolicy)
        self.load_deck_btn.setFont(font1)
        self.load_deck_btn.setCheckable(False)
        self.load_deck_btn.setChecked(False)
        self.deck_cards_listview = QListWidget(self.centralwidget)
        self.deck_cards_listview.setObjectName(u"deck_cards_listview")
        self.deck_cards_listview.setGeometry(QRect(10, 50, 231, 481))
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(359, 49, 571, 481))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 6, 551, 461))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.card_title_label = QLabel(self.layoutWidget)
        self.card_title_label.setObjectName(u"card_title_label")
        self.card_title_label.setFont(font1)

        self.verticalLayout.addWidget(self.card_title_label)

        self.card_title_lineedit = QLineEdit(self.layoutWidget)
        self.card_title_lineedit.setObjectName(u"card_title_lineedit")

        self.verticalLayout.addWidget(self.card_title_lineedit)

        self.question_label = QLabel(self.layoutWidget)
        self.question_label.setObjectName(u"question_label")
        self.question_label.setFont(font1)

        self.verticalLayout.addWidget(self.question_label)

        self.question_textedit = QTextEdit(self.layoutWidget)
        self.question_textedit.setObjectName(u"question_textedit")

        self.verticalLayout.addWidget(self.question_textedit)

        self.expected_answer_label = QLabel(self.layoutWidget)
        self.expected_answer_label.setObjectName(u"expected_answer_label")
        self.expected_answer_label.setFont(font1)

        self.verticalLayout.addWidget(self.expected_answer_label)

        self.expected_answer_textedit = QTextEdit(self.layoutWidget)
        self.expected_answer_textedit.setObjectName(u"expected_answer_textedit")

        self.verticalLayout.addWidget(self.expected_answer_textedit)

        self.exit_designer_btn = QPushButton(self.centralwidget)
        self.exit_designer_btn.setObjectName(u"exit_designer_btn")
        self.exit_designer_btn.setGeometry(QRect(820, 540, 111, 31))
        sizePolicy.setHeightForWidth(self.exit_designer_btn.sizePolicy().hasHeightForWidth())
        self.exit_designer_btn.setSizePolicy(sizePolicy)
        self.exit_designer_btn.setFont(font1)
        self.exit_designer_btn.setCheckable(False)
        self.exit_designer_btn.setChecked(False)
        self.add_card_btn = QPushButton(self.centralwidget)
        self.add_card_btn.setObjectName(u"add_card_btn")
        self.add_card_btn.setGeometry(QRect(250, 50, 101, 31))
        sizePolicy.setHeightForWidth(self.add_card_btn.sizePolicy().hasHeightForWidth())
        self.add_card_btn.setSizePolicy(sizePolicy)
        self.add_card_btn.setFont(font1)
        self.add_card_btn.setCheckable(False)
        self.add_card_btn.setChecked(False)
        self.delete_card_btn = QPushButton(self.centralwidget)
        self.delete_card_btn.setObjectName(u"delete_card_btn")
        self.delete_card_btn.setGeometry(QRect(250, 90, 101, 31))
        sizePolicy.setHeightForWidth(self.delete_card_btn.sizePolicy().hasHeightForWidth())
        self.delete_card_btn.setSizePolicy(sizePolicy)
        self.delete_card_btn.setFont(font1)
        self.delete_card_btn.setCheckable(False)
        self.delete_card_btn.setChecked(False)
        self.save_card_btn = QPushButton(self.centralwidget)
        self.save_card_btn.setObjectName(u"save_card_btn")
        self.save_card_btn.setGeometry(QRect(250, 130, 101, 31))
        sizePolicy.setHeightForWidth(self.save_card_btn.sizePolicy().hasHeightForWidth())
        self.save_card_btn.setSizePolicy(sizePolicy)
        self.save_card_btn.setFont(font1)
        self.save_card_btn.setCheckable(False)
        self.save_card_btn.setChecked(False)
        DesignerWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(DesignerWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 946, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        DesignerWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(DesignerWindow)
        self.statusbar.setObjectName(u"statusbar")
        DesignerWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(DesignerWindow)
        self.toolBar.setObjectName(u"toolBar")
        DesignerWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionExit_Designer)
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(DesignerWindow)

        QMetaObject.connectSlotsByName(DesignerWindow)
    # setupUi

    def retranslateUi(self, DesignerWindow):
        DesignerWindow.setWindowTitle(QCoreApplication.translate("DesignerWindow", u"MainWindow", None))
        self.actionExit_Designer.setText(QCoreApplication.translate("DesignerWindow", u"Exit Designer", None))
        self.actionQuit.setText(QCoreApplication.translate("DesignerWindow", u"Quit", None))
        self.actionAbout.setText(QCoreApplication.translate("DesignerWindow", u"About", None))
        self.deck_designer_label.setText(QCoreApplication.translate("DesignerWindow", u"Deck Designer", None))
        self.new_deck_btn.setText(QCoreApplication.translate("DesignerWindow", u"New Deck", None))
        self.load_deck_btn.setText(QCoreApplication.translate("DesignerWindow", u"Load Deck", None))
        self.card_title_label.setText(QCoreApplication.translate("DesignerWindow", u"Card Title", None))
        self.question_label.setText(QCoreApplication.translate("DesignerWindow", u"Question", None))
        self.expected_answer_label.setText(QCoreApplication.translate("DesignerWindow", u"Expected Answer", None))
        self.exit_designer_btn.setText(QCoreApplication.translate("DesignerWindow", u"Exit Designer", None))
        self.add_card_btn.setText(QCoreApplication.translate("DesignerWindow", u"Add Card", None))
        self.delete_card_btn.setText(QCoreApplication.translate("DesignerWindow", u"Delete Card", None))
        self.save_card_btn.setText(QCoreApplication.translate("DesignerWindow", u"Save Card", None))
        self.menuFile.setTitle(QCoreApplication.translate("DesignerWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("DesignerWindow", u"Help", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("DesignerWindow", u"toolBar", None))
    # retranslateUi

