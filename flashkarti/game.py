"""
Stores the main program logic.
""" 
import os
import json
import logging

from settings import Settings
from player import Player


class Game:
    def __init__(self, settings):
        self.settings = settings
        self.deck = None
        self.player = Player(settings.player_name)
        self._gui = None

    def select_deck(self):
        pass

    def create_player(self):
        pass

    def select_player(self):
        pass

    def delete_player(self):
        pass

    def __repr__(self):
        return f"Game with deck: {self.deck}, player: {self.player} and settings: {self.settings}"

