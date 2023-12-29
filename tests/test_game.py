import pytest

from src.game import Game


@pytest.fixture
def fx_settings(mocker):
    fake_settings = mocker.patch("src.settings.Settings")
    fake_settings.players = [
        {
            "name": "Fake Player 1",
            "stats": {
                "rounds_played": 0,
                "total_score": 0,
                "total_correct": 0,
                "total_partial": 0,
                "total_incorrect": 0,
                "average_correct": 0,
            },
        },
        {
            "name": "Fake Player 2",
            "stats": {
                "rounds_played": 2,
                "total_score": 12.5,
                "total_correct": 9,
                "total_partial": 7,
                "total_incorrect": 2,
                "average_correct": 70.84,
            },
        },
    ]
    yield fake_settings


def test__init__without_settings__raises_AttributeError():
    with pytest.raises(AttributeError):
        Game()


def test__load_player__with_unknown_player_name__raises_ValueError(fx_settings):
    game = Game(fx_settings)

    with pytest.raises(ValueError):
        game.load_player("Unknown Player")


def test__load_player__with_player_name__sets_player(fx_settings):
    game = Game(fx_settings)
    expected_result = "Fake Player 1"

    game.load_player("Fake Player 1")
    result = game.player.name

    assert result == expected_result


def test__get_player_name__with_unset_player__returns_empty_string(fx_settings):
    game = Game(fx_settings)
    expected_result = ""

    result = game.get_player_name()

    assert type(result) is str
    assert result == expected_result


def test__get_player_name__with_set_player__returns_player_name(mocker, fx_settings):
    expected_result = "Fake Player 0"
    fake_player = mocker.patch("src.player.Player")
    fake_player.name = expected_result
    game = Game(fx_settings)
    game.player = fake_player

    result = game.get_player_name()

    assert result == expected_result


def test__list_player_names__without_settings_loaded__returns_empty_list(mocker):
    fake_settings = mocker.patch("src.settings.Settings")  # settings with no players
    expected_result = []
    game = Game(fake_settings)

    result = game.list_player_names()

    assert result == expected_result


def test__list_player_names__with_settings_loaded__returns_players_list(fx_settings):
    expected_result = ["Fake Player 1", "Fake Player 2"]
    game = Game(fx_settings)

    result = game.list_player_names()

    assert result == expected_result


def test__get_deck_title__with_unset_deck__returns_empty_string(fx_settings):
    game = Game(fx_settings)
    expected_result = ""

    result = game.get_deck_title()

    assert type(result) is str
    assert result == expected_result


def test__get_deck_title__with_set_deck__returns_deck_name(mocker, fx_settings):
    expected_result = "Fake Deck"
    fake_deck = mocker.patch("src.deck.Deck")
    fake_deck.title = expected_result
    game = Game(fx_settings)
    game.deck = fake_deck

    result = game.get_deck_title()

    assert result == expected_result
