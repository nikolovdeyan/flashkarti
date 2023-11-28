"""
Holds the game settings.
"""

class Settings:
    def __init__(self, settings):
        self.name = settings.get("name")
        self.num_questions_per_round = settings.get("num_questions_per_round")
        self.gui_theme = settings.get("gui_theme")

    def __repr__(self):
        return(f"Settings: {self.name}")