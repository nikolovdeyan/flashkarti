import logging

from PySide6 import QtCore

from game import Game
from settings import Settings

logger = logging.getLogger(__name__)


class FkModel(QtCore.QObject):
    def __init__(self):
        super(FkModel, self).__init__()
        self.settings = Settings()
        self.game = Game(self.settings)

    def quit(self):
        pass
