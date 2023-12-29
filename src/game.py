"""
Stores the main program logic.
"""
import os
import json
import random
from typing import List
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

        if not self.settings:
            raise AttributeError("Game instantiated without provided settings.")

    def draw_quiz_cards(self, num_cards: int) -> None:
        quiz_cards = random.sample(self.deck._cards, num_cards)
        new_deck = Deck(self.deck.title, quiz_cards)
        self.deck = new_deck

    def set_player(self, player_name: str) -> None:
        player_info = self.get_player_info(player_name)
        self.player = Player(player_info.get("name"), player_info.get("stats"))
        logging.debug(f"Player loaded: {self.player}")

    def get_player_info(self, player_name: str) -> dict:
        players_list = self.get_players_list()
        players_info = self.settings.players
        if not player_name in players_list:
            raise ValueError("Can't set an unknown player. Create the player first.")
        player_dict = players_info[players_list.index(player_name)]
        return player_dict

    def get_player_name(self) -> str:
        """Returns the player name if a player is set, else "".

        ### Returns:
            `str`: The player name loaded in the game.
        """
        return "" if not self.player else self.player.name

    def get_players_list(self) -> List[str]:
        """Returns a list of the player names available in the settings.

        ### Returns:
            `List[str]`: A list of player names.
        """
        if not self.settings.players:
            return []
        return [player.get("name") for player in self.settings.players]

    def get_deck_title(self) -> str:
        """Returns the deck title if a deck is set, else "".

        ### Returns:
            `str`: The deck title loaded in the game.
        """
        return "" if not self.deck else self.deck.title

    def get_cards_names(self) -> List[str]:
        return [card.title for card in self.deck._cards]

    def get_card_display(self, card):
        card_title = f"Question {self.deck.get_current_card_number()} of {self.deck.size}: {card.title}"
        logger.debug(f"Current card: {card}")
        return {
            "deck_title": self.deck.title,
            "card_title": card_title,
            "card_contents": card.contents,
            "answer": card.answer,
            "user_answer": card.user_answer,
            "answer_score": card.answer_score,
            "num_answered_cards": self.deck.get_progress(),
        }

    def get_current_card(self) -> Card:
        return self.deck.draw_current_card()

    def get_card_by_title(self, card_title) -> Card:
        return self.deck.draw_card(card_title)

    def set_current_card(self, card_values: dict) -> None:
        card = self.deck.draw_current_card()
        if card_values.get("card_title") is not None:
            card.title = card_values.get("card_title")
        if card_values.get("card_contents") is not None:
            card.contents = card_values.get("card_contents")
        if card_values.get("answer") is not None:
            card.answer = card_values.get("answer")
        if card_values.get("user_answer") is not None:
            card.user_answer = card_values.get("user_answer")
        if card_values.get("answer_score") is not None:
            card.answer_score = card_values.get("answer_score")
        self.deck._update_num_answered_cards()

    def set_current_card_index(self, card_title: str):
        self.deck.set_current_card_index(card_title)

    def get_next_card(self) -> Card:
        self.deck.next_card()
        return self.deck.draw_current_card()

    def get_prev_card(self) -> Card:
        self.deck.prev_card()
        return self.deck.draw_current_card()

    def set_deck(self, deck_title):
        decks_dict = {}
        for f in os.listdir(DECKS_DIR):
            if os.path.isfile(os.path.join(DECKS_DIR, f)):
                deck_title = " ".join(
                    os.path.basename(f).split(".")[0].split("_")
                ).title()
                decks_dict[deck_title] = os.path.abspath(os.path.join(DECKS_DIR, f))

        deck_file = decks_dict.get(deck_title)
        with open(deck_file, "r") as f:
            deck_list = json.load(f)

        deck_cards = []
        for card_dict in deck_list:
            card = Card(
                title=card_dict.get("title"),
                contents=card_dict.get("contents"),
                answer=card_dict.get("answer"),
                references=card_dict.get("references"),
            )
            deck_cards.append(card)

        deck = Deck(title=deck_title, cards=deck_cards)
        self.deck = deck
        logger.debug(f"Deck loaded: {self.deck}")

    def create_new_card(self):
        card = Card("New Card", "New Question", "New Answer", "New References")
        self.deck.add_card(card)

    def start_quiz(self):
        self.deck.shuffle_deck()
        self.draw_quiz_cards(int(self.settings.num_questions_per_round))
        logger.debug(f"Game starting: {self}")
        logger.debug(f"Game started with cards: {self.deck._cards}")

    def __repr__(self):
        return f"Game with deck: {self.deck.title}, player: {self.player} and settings: {self.settings}"
