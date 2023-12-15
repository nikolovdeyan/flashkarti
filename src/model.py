import logging

from PySide6 import QtCore

logger = logging.getLogger(__name__)


class FkModel(QtCore.QObject):
    def __init__(self):
        super(FkModel, self).__init__()

    def quit(self):
        pass
