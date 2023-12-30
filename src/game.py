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

    def load_player(self, player_name: str) -> None:
        """Loads a player with the provided name in the game.

        ### Args:
            `player_name (str)`: The name of the player to be loaded.

        ### Raises:
            `ValueError`: If the provided name doesn't exist in the game settings.
        """
        players_list = self.list_player_names()
        players_info = self.settings.players

        if not player_name in players_list:
            raise ValueError("Can't set an unknown player. Create the player first.")

        player_info = players_info[players_list.index(player_name)]
        self.player = Player(player_info.get("name"), player_info.get("stats"))
        logging.debug(f"Player loaded: {self.player}")

    def load_deck(self, deck_title: str) -> None:
        """Loads a deck with the provided title in the game.

        TODO: This method is hard to test with all the instantiation going on inside it.

        ### Args:
            `deck_title (str)`: The title of the deck to be loaded.

        ### Raises:
            `ValueError`: If the provided deck doesn't exist in the decks dir.
        """
        deck_title_to_files = self._get_deck_title_to_files_mapping()
        deck_file = deck_title_to_files.get(deck_title)

        if not deck_file:
            raise ValueError("Can't set an unknown deck. Create the deck first.")

        with open(deck_file, "r") as f:
            deck_list = json.load(f)

        deck_cards = self._load_deck_cards(deck_list)

        deck = Deck(title=deck_title, cards=deck_cards)
        self.deck = deck
        logger.debug(f"Deck loaded: {self.deck}")

    def save_deck(self) -> None:
        deck_filename = "_".join(self.deck.title.lower().split()) + ".json"
        with open(os.path.join(DECKS_DIR, deck_filename), "w") as f:
            cards = [card.to_dict() for card in self.deck.cards]
            json.dump(cards, f, indent=4)
        logger.debug(f"File {deck_filename} saved")

    def get_player_name(self) -> str:
        """Returns the player name of the player set in the game, else "".

        ### Returns:
            `str`: The player name loaded in the game.
        """
        return "" if not self.player else self.player.name

    def get_deck_title(self) -> str:
        """Returns the deck title of the deck set in the game, else "".

        ### Returns:
            `str`: The deck title loaded in the game.
        """
        return "" if not self.deck else self.deck.title

    def list_player_names(self) -> List[str]:
        """Returns a list of the player names available in the settings, else [].

        ### Returns:
            `List[str]`: A list of player names.
        """
        if not self.settings.players:
            return []
        return [player.get("name") for player in self.settings.players]

    def list_card_titles(self) -> List[str]:
        """Returns a list of the card titles available in the loaded deck.

        Returns:
            `List[str]`: A list of card titles.
        """
        return [card.title for card in self.deck.cards]

    ### ------ CURRENT LINE  ------ ###

    def get_card_display_data(self, card: Card) -> dict:
        # ? get_quiz_card_display
        question_number = f"{self.deck.get_current_card_number()} of {self.deck.size}"
        logger.debug(f"Current card: {card}")
        result = {
            "deck_title": self.deck.title,
            "question_number": question_number,
            "card_title": card.title,
            "card_contents": card.contents,
            "answer": card.answer,
            "user_answer": card.user_answer,
            "answer_score": card.answer_score,
            "num_answered_cards": self.deck.get_progress_percentage(),
        }
        return result

    def set_current_card(self, card_values: dict) -> None:
        card = self.deck.get_current_card()
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

    def create_new_card(self):
        card = Card("New Card", "New Question", "New Answer", "New References")
        self.deck.add_card(card)

    def start_quiz(self) -> None:
        self.deck.shuffle()
        num_cards_to_draw = int(self.settings.num_questions_per_round)
        self.deck = self._draw_quiz_cards(self.deck, num_cards_to_draw)
        logger.info(f"Game starting: {self}")
        logger.debug(f"Game started with cards: {self.deck.cards}")

    def _get_deck_title_to_files_mapping(self) -> dict:
        """A helper function returning a mapping of deck title to a respective filepath."""
        result = {}
        for f in os.listdir(DECKS_DIR):
            if os.path.isfile(os.path.join(DECKS_DIR, f)):
                title = " ".join(os.path.basename(f).split(".")[0].split("_")).title()
                result[title] = os.path.abspath(os.path.join(DECKS_DIR, f))
        return result

    def _load_deck_cards(self, cards_info: List[dict]) -> List[Card]:
        """A helper function to create a collection of cards.

        Args:
            `cards_info (List)`: A collection containing the cards' infomation.

        Returns:
            `List[Card]`: A collection of Card objects.
        """
        result = []
        for card_dict in cards_info:
            card = Card(
                title=card_dict.get("title"),
                contents=card_dict.get("contents"),
                answer=card_dict.get("answer"),
                references=card_dict.get("references"),
            )
            result.append(card)
        return result

    def _draw_quiz_cards(self, deck: Deck, num_cards: int) -> Deck:
        """Creates a new Deck containing only the randomly drawn cards.

        Args:
            `deck (Deck)`: A deck of cards to draw from.
            `num_cards (int)`: The number of cards to be drawn.
        """
        quiz_cards = random.sample(deck.cards, num_cards)
        result = Deck(deck.title, quiz_cards)
        return result

    def __repr__(self):
        return f"Game with deck: {self.deck.title}, player: {self.player} and settings: {self.settings}"
