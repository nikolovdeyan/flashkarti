![flashkarti logo](/resources/fk_logo.png)

# FlashKarti
A study helper app built with Qt.


## Project Description

### Flashcards as a study tool

Flashcards are a tool and method for retaining information by employing the process of active recall (given a prompt, one produces an answer). Good information on what a flashcard is and how one is used is available on [Wikipedia](https://en.wikipedia.org/wiki/Flashcard):

> A flashcard or flash card is a card bearing information on both sides, which is intended to be used as an aid in memorization. Each flashcard typically bears a question or definition on one side and an answer or target term on the other. Flashcards are often used to memorize vocabulary, historical dates, formulae or any subject matter that can be learned via a question-and-answer format. Flashcards can be virtual (part of a flashcard software), or physical. 

> The [testing effect](https://en.wikipedia.org/wiki/Testing_effect) (also known as retrieval practice, active recall, practice testing, or test-enhanced learning) suggests long-term memory is increased when part of the learning period is devoted to retrieving information from memory.

This application employs the concepts described above to present the user with a GUI application where flashcards can be created, edited, answered and scored. The cards are stored in decks, based on their respective topic.

### FlashKarti application
FlashKarti is built with Python and the [PySide6](https://pypi.org/project/PySide6/) bindings for the Qt framework.

FlashKarti uses the [Model-View-Presenter (MVP)](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93presenter) architectural pattern for its GUI in order to separate its program logic from the user interface. 

![mvp pattern](/resources/mvp_pattern.png)

The application is fully event-driven, where an action in the UI triggers an event (in QT called a signal), which is then processed by the presenter's event-handler function (in QT called a slot). The presenter then makes the necessary changes to the model. The state change in the model triggers the presenter to then update the view to reflect the changes.

## Installation

To install the requirements in your Virtual Environment:

```pip install -r requirements.txt```


## Usage

In the main program directory type:

```python flashkarti.py```

## License
