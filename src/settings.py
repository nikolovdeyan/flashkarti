"""
Holds the game settings.
"""
import os
import json

GAME_DIR = os.path.dirname(os.path.realpath(__file__))
DEFAULT_FILENAME = "default_settings.json"

class Settings:
    def __init__(self, filename=None):
        self.filename = filename if filename else DEFAULT_FILENAME
        self.player_name = None
        self.num_questions_per_round = None
        self.gui_theme = None
        self.load(filename)

    def load(self, filename):
        settings_dir = os.path.join(GAME_DIR, "settings")
        if not filename:
            settings_file = os.path.join(settings_dir, DEFAULT_FILENAME)
        else:
            settings_file = os.path.join(settings_dir, filename)
        with open(settings_file, "r") as f: 
            settings_dict = json.load(f)

        self.player_name = settings_dict.get("player_name")
        self.num_questions_per_round = settings_dict.get("num_questions_per_round")
        self.gui_theme = settings_dict.get("gui_theme")


    def save(self):
        settings_dir = os.path.join(GAME_DIR, "settings")
        settings_dict = {
            "player_name": self.player_name,
            "num_questions_per_round": self.num_questions_per_round,
            "gui_theme": self.gui_theme,
        }

        settings_file = os.path.join(settings_dir, self.filename)
        with open(settings_file, "w") as f:
            json.dump(settings_dict, f, indent=4)

    def __repr__(self):
        return(f"Settings: {self.player_name}")