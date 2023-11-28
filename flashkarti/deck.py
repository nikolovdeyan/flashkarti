"""
Represents a deck of cards, storing its state and possible actions.
"""
from random import shuffle
from card import Card

class Deck:
    def __init__(self, cards=None):
        self.size = 0
        self._cards = cards if cards else []
        self._curr_card_index = 0
        self._update_size()
    
    def add_card(self, card):
        self._cards.append(card)
        self._update_size()
    
    def remove_card(self, card):
        for deck_card in self._cards:
            if deck_card.title == card.title:
                self._cards.remove(deck_card)
                self._update_size()
    
    def _update_size(self):
        self.size = len(self._cards)

    def draw_next_card(self):
        card_to_return = self._cards[self._curr_card_index]
        if self._curr_card_index == self.size - 1:
            self._curr_card_index = 0
        else: 
            self._curr_card_index += 1
        return card_to_return

    def draw_prev_card(self):
        card_to_return = self._cards[self._curr_card_index]
        if self._curr_card_index == 0:
            self._curr_card_index = len(self._cards) - 1
        else:
            self._curr_card_index -= 1
        return card_to_return

    def shuffle_deck(self):
        shuffle(self._cards)
        
    def __repr__(self):
        return f"Deck: {[card for card in self._cards]}"