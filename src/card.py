"""
Represents a flashcard, storing the properties of a single card.
"""


class Card:
    def __init__(self, title, contents, addl_contents, answer, references):
        self.title = title
        self.contents = contents
        self.addl_contents = addl_contents
        self.answer = answer
        self.references = references
        self.user_answer = None
        self.answer_score = None

    def __repr__(self):
        return f"Card: {self.title}"
