"""
Main entry point for Flashkarti
"""
import sys
import logging

from PySide6 import QtWidgets

from view import FkView
from presenter import FkPresenter
from model import FkModel

logging_format = "%(asctime)s|%(name)s|%(levelname)s|%(message)s"
logging.basicConfig(level=logging.DEBUG, format=logging_format)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    model = FkModel()
    view = FkView()
    presenter = FkPresenter(model, view, app)

    sys.exit(app.exec())
