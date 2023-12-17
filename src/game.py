"""
Stores the main program logic.
""" 
import os
import json
import logging

from player import Player
from deck import Deck
from card import Card

logger = logging.getLogger(__name__)

GAME_DIR = os.path.dirname(os.path.realpath(__file__))
DECKS_DIR = os.path.abspath(os.path.join(GAME_DIR, os.pardir, "decks"))

class Game:
    def __init__(self, settings=None):
        self.settings = settings
        self.deck = None
        self.player = None

    def get_player_name(self):
        return "" if not self.player else self.player.name

    def get_deck_name(self):
        return self.deck.name if self.deck else "--"

    def get_players_list(self):
        if not self.settings.players:
            return ""
        return [player.get("name") for player in self.settings.players]

    def get_decks_list(self):
        decks_list = []
        for f in os.listdir(DECKS_DIR):
            if os.path.isfile(os.path.join(DECKS_DIR, f)):
                deck_name = " ".join(os.path.basename(f).split(".")[0].split("_")).title()
                decks_list.append(deck_name)
        return decks_list

    def get_current_card_display(self):
        logger.debug("Game status:")
        logger.debug(f"Player: {self.player}")
        logger.debug(f"Deck: {self.deck}")
        current_card = self.deck.draw_current_card()
        card_title = f"Question {self.deck.get_current_card_number()} of {self.deck.quiz_size}: {current_card.title}"
        return {
            "deck_title": self.deck.name,
            "card_title": card_title,
            "card_contents": current_card.contents,
        }


    def load_player(self, player_name):
        for player_dict in self.settings.players:
            if player_dict.get("name") == player_name:
                self.player = Player(player_dict)
                logging.debug(f"Player loaded: {self.player}")
                return
            else: 
                logging.error(f"Player not found: {player_name}")

    def load_deck(self, deck_name):
        decks_dict = {}
        for f in os.listdir(DECKS_DIR):
            if os.path.isfile(os.path.join(DECKS_DIR, f)):
                deck_name = " ".join(os.path.basename(f).split(".")[0].split("_")).title()
                decks_dict[deck_name] = os.path.abspath(os.path.join(DECKS_DIR, f))

        deck_file = decks_dict.get(deck_name)
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
        logger.debug(f"Deck loaded: {self.deck}")

    def start_game(self):
        self.deck.shuffle_deck()
        self.deck.draw_quiz_cards(int(self.settings.num_questions_per_round))
        logger.debug("Game starting")

    def __repr__(self):
        return f"Game with deck: {self.deck}, player: {self.player} and settings: {self.settings}"
