"""
Represents a flashcard, storing the attributes of a single card.
"""
from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class Card:
    """A Card represents a single question from the FlashKarti game.

    A Card stores in itself information about the question, its answer, what the
    user answer was, and how was it scored. It is a simple dataclass without any
    additional functionality.

    ### Attributes:
    - `title (str)`: The title of the card.
    - `contents (str)`: The contents of the card's question. This field can contain rich
    text to be visualized in the card window.
    - `answer (str)`: The expected answer of the card's question. The user can review
    their answer agains this text at the end of the quiz at the scoring phase.
    - `user_answer (str)`: The answer provided by the user for this card's question.
    - `answer_score (float)`: The score that has been assigned to this card's
    `user_answer` during the scoring phase. This will be used at the end of the scoring
    to calculate the total score for the quiz.
    """

    title: str
    contents: str
    answer: str
    references: str
    user_answer: Optional[str] = None
    answer_score: Optional[float] = None

    def to_dict(self) -> dict:
        """Extract the fields to save as dictionary.

        ### Returns:
            `dict`: A dictionary including the fields to be saved.
        """
        result = asdict(self)
        fields_to_save = ["title", "contents", "answer", "references"]
        return dict((k, result[k]) for k in fields_to_save if k in result)

    def __repr__(self) -> str:
        """Returns a screen representation of a Card.

        Returns:
            `str`: A screen representation of a Card.
        """
        return f"Card: {self.title}"
