"""
Represents a player of the game.
"""
import logging

logger = logging.getLogger(__name__)


class Player:
    def __init__(self, name: str, stats: dict):
        self.name = name
        self.rounds_played = stats.get("rounds_played", 0)
        self.total_score = stats.get("total_score", 0)
        self.total_correct = stats.get("total_correct", 0)
        self.total_partial = stats.get("total_partial", 0)
        self.total_incorrect = stats.get("total_incorrect", 0)
        self.average_correct = stats.get("average_correct", 0)

    def update_scores(self, correct, partial, incorrect, num_questions):
        logger.debug("before update_scores:")
        logger.debug(
            f"self.total_correct: {self.total_correct}, self.total_partial: {self.total_partial}"
        )
        self.update_average_correct(correct, partial, num_questions)
        self.rounds_played += 1
        self.total_correct += correct
        self.total_partial += partial
        self.total_incorrect += incorrect
        logger.debug("after update_scores:")
        logger.debug(
            f"self.total_correct: {self.total_correct}, self.total_partial: {self.total_partial}"
        )
        self.update_total_score()

    def update_total_score(self):
        self.total_score = self.total_correct + (self.total_partial / 2)

    def update_average_correct(self, correct, partial, num_questions):
        round_points = correct + (partial / 2)
        this_round_percentage = round(round_points / num_questions * 100, 2)
        average_correct = (
            self.average_correct * self.rounds_played + this_round_percentage
        ) / (self.rounds_played + 1)
        self.average_correct = round(average_correct, 2)

    def __repr__(self):
        return f"Player: {self.name}, Average Score: {self.average_correct}"
