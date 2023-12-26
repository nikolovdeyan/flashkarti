"""
Represents a deck of cards, storing its state and possible actions.
"""
import random
import logging

from card import Card

logger = logging.getLogger(__name__)


class Deck:
    """A Deck represents a collection of cards on a topic in the FlashKarti game.

    The Deck stores information about the set of cards that are loaded in the current
    quiz of a FlashKarti game. Each deck holds cards on a specific topic and a subset of
    all cards can be selected to be used in the quiz. The Deck additionally supports
    functionality to add, remove, and edit cards.

    ### Attributes:
    - `title (str)`: The title of the deck.
    - `size (int)`: The number of cards in the deck.
    """

    def __init__(self, title=None, cards=None):
        self.title = title
        self.size = 0
        self._cards = cards if cards else []
        self._curr_card_index = 0
        self._num_answered_cards = 0
        self._update_size()

    def add_card(self, card: Card) -> None:
        """Adds a card to the deck.

        ### Args:
            `card (Card)`: The card to be added to the deck.
        """
        self._cards.append(card)
        self._update_size()
        self._curr_card_index = len(self._cards) - 1

    def remove_card(self, card: Card) -> None:
        """Removes a provided card from the deck.

        ### Args:
            `card (Card)`: The card to be removed from the deck.
        """
        for deck_card in self._cards:
            if deck_card.title == card.title:
                self._cards.remove(deck_card)
                self._update_size()

    def draw_current_card(self) -> Card:
        return self._cards[self._curr_card_index]

    def set_current_card_index(self, card_title) -> None:
        logger.debug(f"Requesting card title: {card_title}")
        try:
            self._curr_card_index = [card.title for card in self._cards].index(
                card_title
            )
        except ValueError:
            logger.error("Unknown card title requested")
            return

    def draw_card(self, card_title) -> Card:
        try:
            index = [card.title for card in self._cards].index(card_title)
        except ValueError:
            logger.error("Unknown card title requested")
            return
        return self._cards[index]

    def next_card(self):
        if self._curr_card_index >= self.size - 1:
            self._curr_card_index = 0
        else:
            self._curr_card_index += 1

    def prev_card(self):
        if self._curr_card_index == 0:
            self._curr_card_index = self.size - 1
        else:
            self._curr_card_index -= 1

    def get_current_card_number(self):
        return str(self._curr_card_index + 1)

    def get_progress(self):
        if not self.size:
            return 0
        return int(round(self._num_answered_cards / self.size, 2) * 100)

    def shuffle_deck(self):
        random.shuffle(self._cards)

    def _update_size(self):
        self.size = len(self._cards)

    def _update_num_answered_cards(self):
        result = 0
        for card in self._cards:
            if card.user_answer:
                result += 1
        self._num_answered_cards = result

    def __repr__(self):
        return f"Deck: {self.title}: {[card for card in self._cards]}"
