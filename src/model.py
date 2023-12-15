import logging

from PySide6 import QtCore

from game import Game

logger = logging.getLogger(__name__)


class FkModel(QtCore.QObject):
    def __init__(self):
        super(FkModel, self).__init__()
        self.game = Game()

    def quit(self):
        pass
