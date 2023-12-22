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
    - `quiz_size (int)`: The number of cards selected for the quiz.
    """

    def __init__(self, title=None, cards=None):
        self.title = title
        self.size = 0
        self.quiz_size = 0
        self._cards = cards if cards else []
        self._curr_card_index = 0
        self._quiz_cards = []
        self._num_answered_cards = 0
        self._update_size()

    def add_card(self, card: Card) -> None:
        """Adds a card to the deck.

        ### Args:
            `card (Card)`: The card to be added to the deck.
        """
        self._cards.append(card)
        self._update_size()

    def remove_card(self, card: Card) -> None:
        """Removes a provided card from the deck.

        ### Args:
            `card (Card)`: The card to be removed from the deck.
        """
        for deck_card in self._cards:
            if deck_card.title == card.title:
                self._cards.remove(deck_card)
                self._update_size()

    def draw_quiz_cards(self, num_cards: int) -> None:
        self._quiz_cards = random.sample(self._cards, num_cards)
        self._update_quiz_size()

    def draw_current_card(self):
        return self._quiz_cards[self._curr_card_index]

    def next_card(self):
        if self._curr_card_index >= self.quiz_size - 1:
            self._curr_card_index = 0
        else:
            self._curr_card_index += 1

    def prev_card(self):
        if self._curr_card_index == 0:
            self._curr_card_index = self.quiz_size - 1
        else:
            self._curr_card_index -= 1

    def get_current_card_number(self):
        return str(self._curr_card_index + 1)

    def get_progress(self):
        return int(round(self._num_answered_cards / self.quiz_size, 2) * 100)

    def shuffle_deck(self):
        random.shuffle(self._cards)

    def _update_size(self):
        self.size = len(self._cards)

    def _update_quiz_size(self):
        self.quiz_size = len(self._quiz_cards)

    def _update_num_answered_cards(self):
        result = 0
        for card in self._cards:
            if card.user_answer:
                result += 1
        self._num_answered_cards = result

    def __repr__(self):
        return f"Deck: {self.title}: {[card for card in self._cards]}"
