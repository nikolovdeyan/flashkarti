"""
Main entry point for Flashkarti
"""
import os
import sys
import logging

from PySide6 import QtWidgets

from view import FkView
from presenter import FkPresenter
from model import FkModel

logging_format = "%(asctime)s|%(name)-10s|%(levelname)-10s|%(message)s"
logging.basicConfig(level=logging.DEBUG, format=logging_format)

GAME_DIR = os.path.dirname(os.path.realpath(__file__))
STYLES_DIR = os.path.abspath(os.path.join(GAME_DIR, os.pardir, "styles"))

logger = logging.getLogger(__name__)


def apply_style(app):
    with open(os.path.join(STYLES_DIR, "fk_default.qss"), "r") as f:
        style = f.read()
        app.setStyleSheet(style)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    apply_style(app)

    model = FkModel()
    view = FkView()
    presenter = FkPresenter(model, view, app)

    sys.exit(app.exec())
