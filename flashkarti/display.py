"""
Stores the GUI of the game.
"""
from os import path
import json
import PySimpleGUI as sg
import logging

sg.theme("SandyBeach")   # Add a touch of color
sg.SetOptions (
    font = ("Helvetica", 12, "bold"),
    element_padding = (4, 8),
    )

WIN_WIDTH = 950
WIN_HEIGHT = 800

temp_cards = [
    {
        "quiz_title": "Python Basics Quiz",
        "card_title": "Question Title 1",
        "card_contents": "Question Contents 1",
        "card_addcontents": None,
    },
    {
        "quiz_title": "Python Basics Quiz",
        "card_title": "Question Title 2",
        "card_contents": "Question Contents 2",
        "card_addcontents": None,
    },
    {
        "quiz_title": "Python Basics Quiz",
        "card_title": "Question Title 3",
        "card_contents": "Question Contents 3",
        "card_addcontents": None,
    },
    {
        "quiz_title": "Python Basics Quiz",
        "card_title": "Question Title 4",
        "card_contents": "Question Contents 4",
        "card_addcontents": None,
    },
]

class GUI:
    def __init__(self, game):
        self.game = game
        self.window = None
        self.main()

    def main(self):
        while True:
            if self.window is None:
                self.window = self.create_main_window()
                self.update_main_window()
            event, values = self.window.read()

            logging.debug(f"|EVENT:| {event:30}|VALUES:| {values}")

            if event in (sg.WIN_CLOSED, "Quit"):
                break
            if event in ("Settings"):
                event, values = self.create_settings_window().read(close=True)
                if event == "Save":
                    self.window.close()
                    self.window = None
                    self.game.settings.player_name = values["-PLAYER NAME-"]
                    self.game.settings.num_questions_per_round = values["-NUM QUESTIONS-"]
                    self.game.settings.filename = values["-PLAYER FILE-"]
                    self.game.settings.gui_theme = values["-THEME-"]
                    self.game.settings.save()
            if event in ("-DECK BROWSE-"):
                deck_file = values.get("-DECK BROWSE-")
                self.game.load_deck(deck_file)
                self.window["-SELECTED DECK-"].update(value=self.game.deck.name)
            if event in ("-START QUIZ-"):
                self.window.close()
                self.window = None
                self.window = self.create_game_window()

                curr_card_index = -1
                while True:
                    event, values = self.window.read()
                    logging.debug(f"Event: {event}; Values: {values}")
                    if event in (sg.WIN_CLOSED, "Quit"):
                        break
                    if event == "Themes":
                        theme_browser_window()
                    if event == "-NEXT-":
                        curr_card_index += 1
                        update_card(self.window, event, values, temp_cards[curr_card_index])
                    if event == "-PREV-":
                        curr_card_index -= 1
                        update_card(self.window, event, values, temp_cards[curr_card_index])
                    persist_answer(self.window, event, values)

                    if event == sg.WIN_CLOSED or event == "End Round": # if user closes window or clicks cancel
                        break

        self.window.close()

    def create_settings_window(self):
        sg.theme(self.game.settings.gui_theme)

        def TextLabel(text): 
            return sg.Text(text+":", justification="r", size=(30,1))

        layout = [  [sg.Text("Settings", font="Any 15")],
                    [TextLabel("Player Name"),sg.Input(key="-PLAYER NAME-")],
                    [TextLabel("Number of questions per round"), sg.Input(key="-NUM QUESTIONS-")],
                    [TextLabel("User settings file"),sg.Input(key="-PLAYER FILE-"), sg.FileBrowse(target="-PLAYER FILE-")],
                    [TextLabel("Theme"),sg.Combo(sg.theme_list(), size=(20, 20), key="-THEME-")],
                    [sg.Button("Save"), sg.Button("Close")]  ]

        window = sg.Window("Settings", layout, keep_on_top=True, modal=True, finalize=True)
        try:
            window["-PLAYER NAME-"].update(value=self.game.settings.player_name)
            window["-NUM QUESTIONS-"].update(value=self.game.settings.num_questions_per_round)
            window["-PLAYER FILE-"].update(value=self.game.settings.filename)
            window["-THEME-"].update(value=self.game.settings.gui_theme)
        except Exception as e:
            print(f'Problem updating PySimpleGUI window from settings. Key = {key}')

        return window

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
                [sg.Push()],]),sg.Push()],
            [sg.Push(), sg.Button("Start Quiz", k="-START QUIZ-")],
            [sg.VPush()],
        ]
        return sg.Window("Flashkarti Game", layout, size=(WIN_WIDTH, WIN_HEIGHT), finalize=True)
    
    def create_game_window(self):
        layout = [
            [sg.Menu([["File", ["Deck", "Settings", "Quit"]], ["Help", "About"],])],
            [sg.Text("", k="-QUIZ_TITLE-")],
            [sg.Text("", k="-CARD_TITLE-")],
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
        return sg.Window("Flashkarti Game", layout, size=(WIN_WIDTH, WIN_HEIGHT))


    def update_main_window(self):
        self.window["-SELECTED PLAYER-"].update(f"Selected Player: {self.game.player.name}")
        
        if not self.game.deck:
            self.window["-SELECTED DECK-"].update("Selected Deck: None")
        else: 
            self.window["-SELECTED DECK-"].update(f"Selected Deck: {self.game.deck}")

    def __repr__(self):
        return f"GUI with game: {self.game}"


def persist_answer(window, event, values):
    if event in ("-PREV-", "-NEXT-"):
        answer = values.get("-ANSWER-")
        if answer: 
            print(f"Persisting answer: {answer}")
            window["-ANSWER-"].update("")  # clear answer window

def update_card(window, event, values, card):
    window["-QUIZ_TITLE-"].update(card.get("quiz_title"))
    window["-CARD_TITLE-"].update(card.get("card_title"))
    window["-CARD_CONTENTS-"].update(card.get("card_contents"))
    window["-CARD_ADDCONTENTS-"].update(card.get("card_addcontents"))
