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
    def __init__(self, settings):
        self.settings = settings
        self.deck = None
        self.player = Player(settings.player_name)
        self._gui = None

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

    def create_player(self):
        pass

    def select_player(self):
        pass

    def delete_player(self):
        pass

    def __repr__(self):
        return f"Game with deck: {self.deck}, player: {self.player} and settings: {self.settings}"

