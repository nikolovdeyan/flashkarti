import pytest

from src.game import Game


def test__pytest():
    expected_type = Game

    result = Game()

    assert isinstance(result, expected_type)
