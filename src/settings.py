"""
Holds the game settings.
"""
import os
import json
import logging

from player import Player

GAME_DIR = os.path.dirname(os.path.realpath(__file__))
SETTINGS_FILE = os.path.abspath(os.path.join(GAME_DIR, "settings", "fk_settings.json"))

logger = logging.getLogger(__name__)


class Settings:
    def __init__(self, filename=None):
        self.settings_file = filename if filename else SETTINGS_FILE
        self.num_questions_per_round = None
        self.players = None
        self.load_from_file()

    def load_from_file(self):
        with open(self.settings_file, "r") as f:
            settings_dict = json.load(f)
        game_settings = settings_dict.get("game_settings")
        self.players = settings_dict.get("players")
        self.num_questions_per_round = game_settings.get("num_questions_per_round")

    def save_to_file(self, current_player: Player):
        game_settings = {
            "num_questions_per_round": self.num_questions_per_round,
        }

        players = self.players

        for player in players:
            if player.get("name") == current_player.name:
                player["stats"]["rounds_played"] += 1
                player["stats"]["total_score"] += current_player.total_score
                player["stats"]["average_correct"] = current_player.average_correct

        settings_dict = {
            "game_settings": game_settings,
            "players": players,
        }
        with open(self.settings_file, "w") as f:
            json.dump(settings_dict, f, indent=4)

    def __repr__(self):
        return f"Settings: "
