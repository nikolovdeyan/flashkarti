"""
Main entry point for Flashkarti
"""
import os
import logging
import json

from game import Game
from display import GUI
from settings import Settings


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    settings = Settings()
    game = Game(settings)

    logging.debug(f"Game loaded: {game}")

    gui = GUI(game)
