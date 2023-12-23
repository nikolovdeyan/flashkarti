import os
import json
import logging
from typing import List, Dict

from PySide6 import QtCore

from card import Card
from game import Game
from deck import Deck
from settings import Settings

logger = logging.getLogger(__name__)

GAME_DIR = os.path.dirname(os.path.realpath(__file__))
DECKS_DIR = os.path.abspath(os.path.join(GAME_DIR, os.pardir, "decks"))


class FkModel(QtCore.QObject):
    def __init__(self):
        super(FkModel, self).__init__()
        self.settings = Settings()
        self.game = Game(self.settings)

    def set_player(self, player_name: str) -> None:
        """
        Calls the game method to create a player from the provided string.

        ### Args:
            `player_name` (str): The name of the player to be created.
        """
        self.game.set_player(player_name)

    def get_players_list(self) -> List[str]:
        """
        Calls the game method to return a list of available players.

        The list consists of the created players residing in the settings file.

        ### Returns:
            `List[str]`: The list of available players.
        """
        return self.game.get_players_list()

    def get_player_name(self) -> str:
        """
        Returns the name of the current player loaded in the game.

        ### Returns:
            `str`: The name of the player.
        """
        return self.game.get_player_name()

    def get_decks_list(self) -> List[str]:
        """Returns a list of deck names available in the decks directory.

        ### Returns:
            `List[str]`: A list of available deck names.
        """
        decks_list = []
        for f in os.listdir(DECKS_DIR):
            if os.path.isfile(os.path.join(DECKS_DIR, f)):
                deck_name = " ".join(
                    os.path.basename(f).split(".")[0].split("_")
                ).title()
                decks_list.append(deck_name)
        return decks_list

    def get_deck_name(self) -> str:
        """
        Returns the name of the current deck loaded in the game.

        ### Returns:
            `str`: The name of the deck loaded.
        """
        return self.game.get_deck_title()

    def open_deck_by_name(self, deck_title: str) -> Deck:
        deck_filename = "_".join(deck_title.lower().split(" ")) + ".json"
        logger.debug(deck_filename)

        deck_file = os.path.join(DECKS_DIR, deck_filename)
        logger.debug(deck_file)

        try:
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
        except:
            logger.error(f"Could not open file {deck_file}")
        return deck

    def set_deck(self, deck_title: str) -> None:
        """Calls the game method to load a deck from the decks dir.

        ### Args:
            `deck_title (str)`: The name of the deck to be loaded.
        """
        self.game.set_deck(deck_title)

    def start_quiz(self) -> None:
        """
        Calls the game method to begin the quiz.
        """
        self.game.start_quiz()

    def get_next_card_display(self) -> dict:
        """
        Returns the display information of the next card in the deck.

        ### Returns:
            `dict`: The display information of the next card in the deck.
        """
        return self.game.get_card_display(self.game.get_next_card())

    def get_prev_card_display(self) -> dict:
        """
        Returns the display information of the previous card in the deck.

        ### Returns:
            `dict`: The display information of the previous card in the deck.
        """
        return self.game.get_card_display(self.game.get_prev_card())

    def get_current_card_display(self) -> dict:
        """
        Returns the display information of the current card in the deck.

        ### Returns:
            `dict`: The display information of the current card in the deck.
        """
        return self.game.get_card_display(self.game.get_current_card())

    def set_current_card(self, current_card: dict) -> None:
        """Persists the state of the current card in the deck.

        ### Args:
            `current_card: (dict)` The card information to be persisted.
        """
        self.game.set_current_card(current_card)

    def quit(self):
        pass
