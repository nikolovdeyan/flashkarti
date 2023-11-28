"""
Stores the main program logic.
""" 
import os
import json
import logging

from settings import Settings

GAME_DIR = os.path.dirname(os.path.realpath(__file__))


class Game:
    def __init__(self):
        self.deck = None
        self.player = None
        self.settings = None
        self._gui = None
        self.load_settings()

    def select_deck(self):
        pass

    def select_player(self):
        pass

    def load_settings(self, settings_file=None):
        settings_dir = os.path.join(GAME_DIR, "settings")
        default_settings_filename = "default_settings.json"

        if not settings_file:
            settings_file = os.path.join(settings_dir, default_settings_filename)
        else: 
            settings_file = os.path.join(settings_dir, settings_file)

        with open(settings_file, "r") as f: 
            settings_dict = json.load(f)
        logging.debug(settings_dict)
        self.settings = Settings(settings_dict)


    def __repr__(self):
        return f"Game with deck: {self.deck} and player: {self.player}"


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)

    fk = Game()
    logging.debug(f"fk: {fk}")
    logging.debug(f"Game dir: {GAME_DIR}")
    logging.debug(f"Settings loaded: {fk.settings}")