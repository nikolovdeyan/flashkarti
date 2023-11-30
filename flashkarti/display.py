"""
Stores the GUI of the game.
"""
from os import path
import json
import PySimpleGUI as sg
import logging

sg.theme("SandyBeach")   # Add a touch of color
sg.SetOptions (font = ("Helvetica", 12, "bold"))

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
            if event in ("Card"):
                self.window.close()
                self.window = None
                self.window = self.create_game_window()
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

    def __repr__(self):
        return f"GUI with game: {self.game}"
    
    def create_main_window(self):
        sg.theme(self.game.settings.gui_theme)
        layout = [
            [sg.Menu([["File", ["Deck", "Settings", "Quit"]], ["Help", "About"],])],
            [sg.VPush()],
            [sg.Text("Welcome to Flashkarti!", size=(50,3), font=("Helvetica", 16, "bold"))],
            [sg.Push(), 
            sg.Frame("", [
                [sg.Text("Please load a deck and press 'start'!", size=(50,2), font=("Helvetica", 14, "bold"))],
                [sg.Button("Change", k="-CHANGE PLAYER-"), sg.Text("Selected Player: None", k="-SELECTED PLAYER-", size=80)],
                [sg.Button("Change", k="-CHANGE DECK-"), sg.Text("Selected Deck: None", k="-SELECTED DECK-", size=80)],
                [sg.Push()],
            ]),
            sg.Push()],
            [sg.VPush()],
        ]
        return sg.Window("Flashkarti Game", layout, size=(WIN_WIDTH, WIN_HEIGHT))
    
    def create_game_window(self):
        layout = [
            [sg.Menu([["File", ["Deck", "Settings", "Quit"]], ["Help", "About"],])],
            [sg.VPush()],
            [sg.VPush()],
        ]
        return sg.Window("Flashkarti Game", layout, size=(WIN_WIDTH, WIN_HEIGHT))


def persist_answer(window, event, values):
    if event in ("-PREV-", "-NEXT-"):
        answer = values.get("-ANSWER-")
        if answer: 
            print(f"Persisting answer: {answer}")
            window["-ANSWER-"].update("")  # clear answer window

def update_card(window, event, values, card):
    print(card)
    window["-QUIZ_TITLE-"].update(card.get("quiz_title"))
    window["-CARD_TITLE-"].update(card.get("card_title"))
    window["-CARD_CONTENTS-"].update(card.get("card_contents"))
    window["-CARD_ADDCONTENTS-"].update(card.get("card_addcontents"))

def card_window(): 
    layout = [
        [sg.Menu([["File", ["End Round"]]])],
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
    window = sg.Window("Flashkarti Game", layout, size=(WIN_WIDTH-50, WIN_HEIGHT-50))

    curr_card_index = -1
    while True:
        event, values = window.read()
        logging.debug(f"Event: {event}; Values: {values}")

        if event == "Themes":
            theme_browser_window()

        if event == "-NEXT-":
            curr_card_index += 1
            update_card(window, event, values, temp_cards[curr_card_index])
        if event == "-PREV-":
            curr_card_index -= 1
            update_card(window, event, values, temp_cards[curr_card_index])

        persist_answer(window, event, values)

        if event == sg.WIN_CLOSED or event == "End Round": # if user closes window or clicks cancel
            break

    window.close()