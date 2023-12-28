"""
Represents a player of the game.
"""


class Player:
    def __init__(self, name):
        self.name = name
        self._num_rounds = 0
        self._total_score = 0
        self._total_correct = 0
        self._total_partial = 0
        self._total_incorrect = 0
        self._average_correct = 0

    def update_scores(self, correct, partial, incorrect, num_questions):
        self._num_rounds += 1
        self._total_correct += correct
        self._total_partial += partial
        self._total_incorrect += incorrect
        self._update_total_scores()
        self._update_average_correct(correct, partial, num_questions)

    def _update_total_scores(self):
        self._total_score = self._total_correct + (self._total_partial / 2)

    def _update_average_correct(self, correct, partial, num_questions):
        round_points = correct + (partial / 2)
        self._average_correct = round(round_points / num_questions * 100, 2)

    def __repr__(self):
        return f"Player: {self.name}"
