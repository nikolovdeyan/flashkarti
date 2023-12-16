"""
Stores the main program logic.
""" 
import os
import json
import logging

from settings import Settings
from player import Player
from deck import Deck
from card import Card


class Game:
    def __init__(self, settings=None):
        self.settings = settings
        self.deck = None
        self.player = None

        self.load_player

    def get_player_name(self):
        return "" if not self.player else self.player.name

    def get_deck_name(self):
        return "" if not self.deck else self.deck.name

    def get_players_list(self):
        if not self.settings.players:
            return ""
        return [player.get("name") for player in self.settings.players]

    def load_player(self, player_name):
        for player_dict in self.settings.players:
            if player_dict.get("name") == player_name:
                self.player = Player(player_dict)
        logging.error(f"Player not found: {player_name}")

    def load_deck(self, deck_file):
        # TODO: Validations for decks named outside the convention
        deck_name = " ".join(os.path.basename(deck_file).split(".")[0].split("_")).title()

        with open(deck_file, "r") as f: 
            deck_list = json.load(f)

        deck_cards = []
        for card_dict in deck_list:
            card = Card(
                title = card_dict.get("title"),
                contents = card_dict.get("contents"),
                addl_contents = card_dict.get("additional_contents"),
                answer = card_dict.get("answer"),
                references = card_dict.get("references")
            )
            deck_cards.append(card)
        
        deck = Deck(name=deck_name, cards=deck_cards)
        self.deck = deck
        logging.debug(f"Deck loaded: {self.deck}")

    def __repr__(self):
        return f"Game with deck: {self.deck}, player: {self.player} and settings: {self.settings}"

