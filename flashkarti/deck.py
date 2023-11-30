"""
Represents a deck of cards, storing its state and possible actions.
"""
import random

class Deck:
    def __init__(self, name=None, cards=None):
        self.name = name
        self.size = 0
        self.quiz_size = 0
        self._cards = cards if cards else []
        self._curr_card_index = 0
        self._quiz_cards = []
        self._num_answered_cards = 0
        self._update_size()
        self.shuffle_deck()
    
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

    def _update_quiz_size(self):
        self.quiz_size = len(self._quiz_cards)

    def draw_quiz_cards(self, num_cards):
        self._quiz_cards = [random.choice(self._cards) for _ in range(num_cards)]
        self._update_quiz_size()

    def draw_current_card(self):
        return self._quiz_cards[self._curr_card_index]

    def draw_next_card(self):
        if self._curr_card_index >= self.quiz_size - 1:
            self._curr_card_index = 0
        else: 
            self._curr_card_index += 1
        return self.draw_current_card()

    def draw_prev_card(self):
        if self._curr_card_index == 0:
            self._curr_card_index = self.quiz_size - 1
        else:
            self._curr_card_index -= 1
        return self.draw_current_card()

    def get_current_card_index_str(self):
        return f"Question {self._curr_card_index + 1} of {self.quiz_size}:"


    def shuffle_deck(self):
        random.shuffle(self._cards)
        
    def __repr__(self):
        return f"Deck: {self.name}: {[card for card in self._cards]}"