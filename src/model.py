import logging
from typing import List, Dict

from PySide6 import QtCore

from game import Game
from settings import Settings

logger = logging.getLogger(__name__)


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

    def get_player(self):
        pass

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
        """Calls the game method to return a list of available decks.

        The list consists of the available deck files contained in the decks directory.

        ### Returns:
            `List[str]`: The list of available decks.
        """
        return self.game.get_decks_list()

    def get_deck_name(self) -> str:
        """
        Returns the name of the current deck loaded in the game.

        ### Returns:
            `str`: The name of the deck loaded.
        """
        return self.game.get_deck_title()

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
