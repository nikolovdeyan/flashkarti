# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(946, 640)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.settings_btn = QPushButton(self.centralwidget)
        self.settings_btn.setObjectName(u"settings_btn")
        self.settings_btn.setGeometry(QRect(20, 330, 101, 31))
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.settings_btn.sizePolicy().hasHeightForWidth())
        self.settings_btn.setSizePolicy(sizePolicy)
        self.settings_btn.setMinimumSize(QSize(100, 30))
        font = QFont()
        font.setPointSize(12)
        self.settings_btn.setFont(font)
        self.quit_btn = QPushButton(self.centralwidget)
        self.quit_btn.setObjectName(u"quit_btn")
        self.quit_btn.setGeometry(QRect(20, 370, 101, 31))
        sizePolicy.setHeightForWidth(self.quit_btn.sizePolicy().hasHeightForWidth())
        self.quit_btn.setSizePolicy(sizePolicy)
        self.quit_btn.setMinimumSize(QSize(100, 30))
        self.quit_btn.setFont(font)
        self.start_quiz_btn = QPushButton(self.centralwidget)
        self.start_quiz_btn.setObjectName(u"start_quiz_btn")
        self.start_quiz_btn.setGeometry(QRect(820, 500, 101, 31))
        sizePolicy.setHeightForWidth(self.start_quiz_btn.sizePolicy().hasHeightForWidth())
        self.start_quiz_btn.setSizePolicy(sizePolicy)
        self.start_quiz_btn.setMinimumSize(QSize(100, 30))
        self.start_quiz_btn.setFont(font)
        self.welcome_label = QLabel(self.centralwidget)
        self.welcome_label.setObjectName(u"welcome_label")
        self.welcome_label.setGeometry(QRect(360, 20, 231, 81))
        font1 = QFont()
        font1.setPointSize(16)
        self.welcome_label.setFont(font1)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 250, 558, 33))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.deck_btn = QPushButton(self.layoutWidget)
        self.deck_btn.setObjectName(u"deck_btn")
        sizePolicy.setHeightForWidth(self.deck_btn.sizePolicy().hasHeightForWidth())
        self.deck_btn.setSizePolicy(sizePolicy)
        self.deck_btn.setMinimumSize(QSize(100, 30))
        self.deck_btn.setFont(font)

        self.horizontalLayout_2.addWidget(self.deck_btn)

        self.deck_label = QLabel(self.layoutWidget)
        self.deck_label.setObjectName(u"deck_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.deck_label.sizePolicy().hasHeightForWidth())
        self.deck_label.setSizePolicy(sizePolicy1)
        self.deck_label.setMinimumSize(QSize(450, 0))
        self.deck_label.setFont(font)

        self.horizontalLayout_2.addWidget(self.deck_label)

        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 210, 558, 33))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.player_btn = QPushButton(self.layoutWidget1)
        self.player_btn.setObjectName(u"player_btn")
        sizePolicy.setHeightForWidth(self.player_btn.sizePolicy().hasHeightForWidth())
        self.player_btn.setSizePolicy(sizePolicy)
        self.player_btn.setMinimumSize(QSize(100, 30))
        self.player_btn.setFont(font)

        self.horizontalLayout.addWidget(self.player_btn)

        self.player_label = QLabel(self.layoutWidget1)
        self.player_label.setObjectName(u"player_label")
        sizePolicy1.setHeightForWidth(self.player_label.sizePolicy().hasHeightForWidth())
        self.player_label.setSizePolicy(sizePolicy1)
        self.player_label.setMinimumSize(QSize(450, 0))
        self.player_label.setFont(font)

        self.horizontalLayout.addWidget(self.player_label)

        self.layoutWidget2 = QWidget(self.centralwidget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(20, 290, 558, 33))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.designer_btn = QPushButton(self.layoutWidget2)
        self.designer_btn.setObjectName(u"designer_btn")
        sizePolicy.setHeightForWidth(self.designer_btn.sizePolicy().hasHeightForWidth())
        self.designer_btn.setSizePolicy(sizePolicy)
        self.designer_btn.setMinimumSize(QSize(100, 30))
        self.designer_btn.setFont(font)

        self.horizontalLayout_3.addWidget(self.designer_btn)

        self.designer_label = QLabel(self.layoutWidget2)
        self.designer_label.setObjectName(u"designer_label")
        sizePolicy1.setHeightForWidth(self.designer_label.sizePolicy().hasHeightForWidth())
        self.designer_label.setSizePolicy(sizePolicy1)
        self.designer_label.setMinimumSize(QSize(450, 0))
        self.designer_label.setFont(font)

        self.horizontalLayout_3.addWidget(self.designer_label)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 946, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.settings_btn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.quit_btn.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.start_quiz_btn.setText(QCoreApplication.translate("MainWindow", u"Start Quiz", None))
        self.welcome_label.setText(QCoreApplication.translate("MainWindow", u"Welcome to FlashKarti", None))
        self.deck_btn.setText(QCoreApplication.translate("MainWindow", u"Deck", None))
        self.deck_label.setText(QCoreApplication.translate("MainWindow", u"Selected deck: None", None))
        self.player_btn.setText(QCoreApplication.translate("MainWindow", u"Player", None))
        self.player_label.setText(QCoreApplication.translate("MainWindow", u"Selected player: None", None))
        self.designer_btn.setText(QCoreApplication.translate("MainWindow", u"Designer", None))
        self.designer_label.setText(QCoreApplication.translate("MainWindow", u"Deck Designer: Create and Edit Decks", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

Error: main_window.ui: Warning: The name 'layoutWidget' (QWidget) is already in use, defaulting to 'layoutWidget1'.
main_window.ui: Warning: The name 'layoutWidget' (QWidget) is already in use, defaulting to 'layoutWidget2'.

while executing '/home/deo/WORKSPACE/flashkarti/ve_fkarti/lib/python3.11/site-packages/PySide6/Qt/libexec/uic -g python main_window.ui'
