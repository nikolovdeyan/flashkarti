# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu_window.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MenuWindow(object):
    def setupUi(self, MenuWindow):
        if not MenuWindow.objectName():
            MenuWindow.setObjectName(u"MenuWindow")
        MenuWindow.resize(946, 640)
        self.actionQuit = QAction(MenuWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionAbout = QAction(MenuWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.MenuWidget = QWidget(MenuWindow)
        self.MenuWidget.setObjectName(u"MenuWidget")
        self.MenuWidget.setGeometry(QRect(10, 80, 941, 551))
        self.start_quiz_btn = QPushButton(self.MenuWidget)
        self.start_quiz_btn.setObjectName(u"start_quiz_btn")
        self.start_quiz_btn.setGeometry(QRect(820, 500, 101, 31))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_quiz_btn.sizePolicy().hasHeightForWidth())
        self.start_quiz_btn.setSizePolicy(sizePolicy)
        self.start_quiz_btn.setMinimumSize(QSize(100, 30))
        font = QFont()
        font.setPointSize(12)
        self.start_quiz_btn.setFont(font)
        self.welcome_label = QLabel(self.MenuWidget)
        self.welcome_label.setObjectName(u"welcome_label")
        self.welcome_label.setGeometry(QRect(360, 20, 231, 81))
        font1 = QFont()
        font1.setPointSize(16)
        self.welcome_label.setFont(font1)
        self.layoutWidget = QWidget(self.MenuWidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 210, 591, 181))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.player_btn = QPushButton(self.layoutWidget)
        self.player_btn.setObjectName(u"player_btn")
        sizePolicy.setHeightForWidth(self.player_btn.sizePolicy().hasHeightForWidth())
        self.player_btn.setSizePolicy(sizePolicy)
        self.player_btn.setMinimumSize(QSize(100, 30))
        self.player_btn.setFont(font)

        self.gridLayout.addWidget(self.player_btn, 0, 0, 1, 1)

        self.player_label = QLabel(self.layoutWidget)
        self.player_label.setObjectName(u"player_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.player_label.sizePolicy().hasHeightForWidth())
        self.player_label.setSizePolicy(sizePolicy1)
        self.player_label.setMinimumSize(QSize(450, 0))
        self.player_label.setFont(font)

        self.gridLayout.addWidget(self.player_label, 0, 1, 1, 1)

        self.deck_btn = QPushButton(self.layoutWidget)
        self.deck_btn.setObjectName(u"deck_btn")
        sizePolicy.setHeightForWidth(self.deck_btn.sizePolicy().hasHeightForWidth())
        self.deck_btn.setSizePolicy(sizePolicy)
        self.deck_btn.setMinimumSize(QSize(100, 30))
        self.deck_btn.setFont(font)

        self.gridLayout.addWidget(self.deck_btn, 1, 0, 1, 1)

        self.deck_label = QLabel(self.layoutWidget)
        self.deck_label.setObjectName(u"deck_label")
        sizePolicy1.setHeightForWidth(self.deck_label.sizePolicy().hasHeightForWidth())
        self.deck_label.setSizePolicy(sizePolicy1)
        self.deck_label.setMinimumSize(QSize(450, 0))
        self.deck_label.setFont(font)

        self.gridLayout.addWidget(self.deck_label, 1, 1, 1, 1)

        self.designer_btn = QPushButton(self.layoutWidget)
        self.designer_btn.setObjectName(u"designer_btn")
        sizePolicy.setHeightForWidth(self.designer_btn.sizePolicy().hasHeightForWidth())
        self.designer_btn.setSizePolicy(sizePolicy)
        self.designer_btn.setMinimumSize(QSize(100, 30))
        self.designer_btn.setFont(font)

        self.gridLayout.addWidget(self.designer_btn, 2, 0, 1, 1)

        self.designer_label = QLabel(self.layoutWidget)
        self.designer_label.setObjectName(u"designer_label")
        sizePolicy1.setHeightForWidth(self.designer_label.sizePolicy().hasHeightForWidth())
        self.designer_label.setSizePolicy(sizePolicy1)
        self.designer_label.setMinimumSize(QSize(450, 0))
        self.designer_label.setFont(font)

        self.gridLayout.addWidget(self.designer_label, 2, 1, 1, 1)

        self.settings_btn = QPushButton(self.layoutWidget)
        self.settings_btn.setObjectName(u"settings_btn")
        sizePolicy.setHeightForWidth(self.settings_btn.sizePolicy().hasHeightForWidth())
        self.settings_btn.setSizePolicy(sizePolicy)
        self.settings_btn.setMinimumSize(QSize(100, 30))
        self.settings_btn.setFont(font)

        self.gridLayout.addWidget(self.settings_btn, 3, 0, 1, 1)

        self.quit_btn = QPushButton(self.layoutWidget)
        self.quit_btn.setObjectName(u"quit_btn")
        sizePolicy.setHeightForWidth(self.quit_btn.sizePolicy().hasHeightForWidth())
        self.quit_btn.setSizePolicy(sizePolicy)
        self.quit_btn.setMinimumSize(QSize(100, 30))
        self.quit_btn.setFont(font)

        self.gridLayout.addWidget(self.quit_btn, 4, 0, 1, 1)

        self.settings_label = QLabel(self.layoutWidget)
        self.settings_label.setObjectName(u"settings_label")
        sizePolicy1.setHeightForWidth(self.settings_label.sizePolicy().hasHeightForWidth())
        self.settings_label.setSizePolicy(sizePolicy1)
        self.settings_label.setMinimumSize(QSize(450, 0))
        self.settings_label.setFont(font)

        self.gridLayout.addWidget(self.settings_label, 3, 1, 1, 1)

        self.menubar = QMenuBar(MenuWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 946, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.statusbar = QStatusBar(MenuWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setGeometry(QRect(0, 0, 3, 22))

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MenuWindow)

        QMetaObject.connectSlotsByName(MenuWindow)
    # setupUi

    def retranslateUi(self, MenuWindow):
        MenuWindow.setWindowTitle(QCoreApplication.translate("MenuWindow", u"MainWindow", None))
        self.actionQuit.setText(QCoreApplication.translate("MenuWindow", u"Quit", None))
        self.actionAbout.setText(QCoreApplication.translate("MenuWindow", u"About", None))
        self.start_quiz_btn.setText(QCoreApplication.translate("MenuWindow", u"Start Quiz", None))
        self.welcome_label.setText(QCoreApplication.translate("MenuWindow", u"Welcome to FlashKarti", None))
        self.player_btn.setText(QCoreApplication.translate("MenuWindow", u"Player", None))
        self.player_label.setText(QCoreApplication.translate("MenuWindow", u"Selected player: None", None))
        self.deck_btn.setText(QCoreApplication.translate("MenuWindow", u"Deck", None))
        self.deck_label.setText(QCoreApplication.translate("MenuWindow", u"Selected deck: None", None))
        self.designer_btn.setText(QCoreApplication.translate("MenuWindow", u"Designer", None))
        self.designer_label.setText(QCoreApplication.translate("MenuWindow", u"Deck Designer: Create and edit decks", None))
        self.settings_btn.setText(QCoreApplication.translate("MenuWindow", u"Settings", None))
        self.quit_btn.setText(QCoreApplication.translate("MenuWindow", u"Quit", None))
        self.settings_label.setText(QCoreApplication.translate("MenuWindow", u"Change game settings", None))
        self.menuFile.setTitle(QCoreApplication.translate("MenuWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MenuWindow", u"Help", None))
    # retranslateUi

