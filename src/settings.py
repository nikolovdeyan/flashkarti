"""
Holds the game settings.
"""
import os
import json

from player import Player

GAME_DIR = os.path.dirname(os.path.realpath(__file__))
SETTINGS_FILE = os.path.abspath(os.path.join(GAME_DIR, "settings", "fk_settings.json"))


class Settings:
    def __init__(self, filename=None):
        self.settings_file = filename if filename else SETTINGS_FILE
        self.current_player_name = None
        self.num_questions_per_round = None
        self.players = None
        self.load_from_file()

    def load_from_file(self):
        with open(self.settings_file, "r") as f:
            settings_dict = json.load(f)
        game_settings = settings_dict.get("game_settings")
        self.players = settings_dict.get("players")
        self.current_player_name = game_settings.get("current_player")
        self.num_questions_per_round = game_settings.get("num_questions_per_round")

    def save_to_file(self, current_player: Player):
        game_settings = {
            "current_player": self.current_player_name,
            "num_questions_per_round": self.num_questions_per_round,
        }

        players = self.players

        for player in players:
            if player.get("name") == current_player.name:
                player["rounds_played"] += 1
                player["total_score"] += current_player._total_score

        settings_dict = {
            "game_settings": game_settings,
            "players": players,
        }
        with open(self.settings_file, "w") as f:
            json.dump(settings_dict, f, indent=4)

    def __repr__(self):
        return f"Settings: current_player_name: {self.current_player_name}"
