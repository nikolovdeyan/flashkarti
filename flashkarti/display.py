"""
Stores the GUI of the game.
"""
from os import path
import json
import PySimpleGUI as sg
import logging

sg.SetOptions (
    font = ("Helvetica", 12, "bold"),
    element_padding = (8, 8),
    )

WIN_WIDTH = 950
WIN_HEIGHT = 800


class GUI:
    def __init__(self, game):
        self.game = game
        self.window = None
        self.main()

    def main(self):
        while True:
            if self.window is None:
                self.window = self.create_main_window()

            event, values = self.window.read()
            logging.debug(f"|EVENT:| {event:25}|VALUES:| {values}")
            
            match self.window.Title.title():
                case "Flashkarti Main":
                    self.handle_main_window(event, values)
                case "Flashkarti Quiz":
                    self.handle_game_window(event, values)
                case "Flashkarti Answers":
                    pass
                case _:
                    logging.error("No matching window found!")

            # Main Handlers
            if event in ("Settings"):
                event, values = self.create_settings_window().read(close=True)
                logging.debug(f"Settings event {event}; values {values}")
                self.handle_settings_window(event, values)
            if event in ("-START QUIZ-"):
                self.window.close()
                self.window = None
                self.window = self.create_game_window()
            if event in(sg.WIN_CLOSED, "Quit"):
                break
        self.window.close()

    def create_settings_window(self):
        def TextLabel(text): 
            return sg.Text(text+":", justification="r", size=(30,1))

        layout = [  [sg.Text("Settings", font="Any 15")],
                    [TextLabel("Player Name"),sg.Input(key="-PLAYER NAME-")],
                    [TextLabel("Number of questions per round"), sg.Input(key="-NUM QUESTIONS-")],
                    [TextLabel("Settings file"),sg.Input(key="-SETTINGS FILE-"), sg.FileBrowse(target="-SETTINGS FILE-")],
                    [TextLabel("Theme"),sg.Combo(sg.theme_list(), size=(20, 20), key="-THEME-")],
                    [sg.Button("Save"), sg.Button("Close")]  ]

        window = sg.Window("Flashkarti Settings", layout, keep_on_top=True, modal=True, finalize=True)
        window["-PLAYER NAME-"].update(value=self.game.settings.player_name)
        window["-NUM QUESTIONS-"].update(value=self.game.settings.num_questions_per_round)
        window["-SETTINGS FILE-"].update(value=self.game.settings.filename)
        window["-THEME-"].update(value=self.game.settings.gui_theme)

        return window

    def handle_settings_window(self, event, values):
        if event == "Save":
            self.window.close()
            self.window = None
            self.game.settings.player_name = values["-PLAYER NAME-"]
            self.game.settings.num_questions_per_round = values["-NUM QUESTIONS-"]
            self.game.settings.filename = values["-SETTINGS FILE-"]
            self.game.settings.gui_theme = values["-THEME-"]
            self.game.settings.save()

    def create_main_window(self):
        sg.theme(self.game.settings.gui_theme)
        layout = [
            [sg.Menu([["File", ["Deck", "Settings", "Quit"]], ["Help", "About"],])],
            [sg.VPush()],
            [sg.Push(), sg.Text("Welcome to Flashkarti!", size=(20,2), font=("Helvetica", 16, "bold")), sg.Push()],
            [sg.Push(), 
            sg.Frame("", [
                [sg.Text("Please load a deck and press 'start'!", size=(50,2), font=("Helvetica", 14, "bold"))],
                [sg.Button("Player", size=8, k="-CHANGE PLAYER-"), sg.Text("Selected Player: None", k="-SELECTED PLAYER-", size=80)],
                [sg.Input(key="-DECK BROWSE-", enable_events=True, visible=False)],[sg.FileBrowse("Deck", size=8, target="-DECK BROWSE-"), sg.Text("Selected Deck:", k="-SELECTED DECK-", size=80)],
                [sg.Button("Designer", size=8, k="-DECK DESIGNER-", disabled=True), sg.Text("Deck Designer: Coming Soon!", size=80)],
                [sg.Button("Settings", size=8)],
                [sg.Button("Quit", size=8)],
                [sg.Push(), sg.Button("Start Quiz", k="-START QUIZ-", disabled=True)],
                [sg.Push()],]),sg.Push()],
            [sg.VPush()],
        ]
        return sg.Window("Flashkarti Main", layout, size=(WIN_WIDTH, WIN_HEIGHT), finalize=True)
    
    def handle_main_window(self, event, values):
        self.window["-SELECTED PLAYER-"].update(f"Selected Player: {self.game.player.name}")
        
        if not self.game.deck:
            self.window["-SELECTED DECK-"].update("Selected Deck: None")
        else: 
            self.window["-SELECTED DECK-"].update(f"Selected Deck: {self.game.deck.name}")
        if event in ("-DECK BROWSE-"):
            deck_file = values.get("-DECK BROWSE-")
            self.game.load_deck(deck_file)
            self.window["-SELECTED DECK-"].update(value=self.game.deck.name)
            self.game.deck.draw_quiz_cards(5)
            self.window["-START QUIZ-"].update(disabled=False)

    def create_game_window(self):
        layout = [
            [sg.Menu([["File", ["Deck", "Settings", "Quit"]], ["Help", "About"],])],
            [sg.Text("", k="-QUIZ_TITLE-")],
            [sg.Text("", k="-QUESTION NUM-"), sg.Text("", k="-CARD_TITLE-")],
            [
                sg.Column([[sg.Frame("Question Contents", [[sg.Text("", size=(60,20), k="-CARD_CONTENTS-")]])]]),
                sg.Column([[sg.Frame("Additional Contents", [[sg.Text("", size=(57,20), k="-CARD_ADDCONTENTS-")]])]])
            ],
            [sg.Frame("Answer Contents", [
                [sg.Multiline(size=(WIN_WIDTH,10), key="-ANSWER-")],
                [
                    sg.Button("< Previous", k="-PREV-"),
                    sg.Push(),
                    sg.Text("00:02:20"),
                    sg.Push(),
                    sg.Button("Next >", k="-NEXT-")]
                ])],
            [sg.Frame("Progress:", [[sg.ProgressBar(100, orientation='h', s=(WIN_WIDTH,20), k='-PBAR-')]])],
        ]
        return sg.Window("Flashkarti Quiz", layout, size=(WIN_WIDTH, WIN_HEIGHT), finalize=True)

    def handle_game_window(self, event, values):
        current_card = self.game.deck.draw_current_card()
        self.window["-QUESTION NUM-"].update(self.game.deck.get_current_card_index_str())
        self.window["-QUIZ_TITLE-"].update(self.game.deck.name)
        self.window["-CARD_TITLE-"].update(current_card.title)
        self.window["-CARD_CONTENTS-"].update(current_card.contents)
        self.window["-CARD_ADDCONTENTS-"].update(current_card.addl_contents)

        if event == "-NEXT-":
            self.game.deck.draw_next_card()
        if event == "-PREV-":
            self.game.deck.draw_prev_card()
        if event in ("-PREV-", "-NEXT-"):
            answer = values.get("-ANSWER-")
            if answer: 
                print(f"Persisting answer: {answer}")
                self.window["-ANSWER-"].update("")  # clear answer window
    
    def __repr__(self):
        return f"GUI with game: {self.game}"
