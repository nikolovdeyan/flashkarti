import pytest

from src.deck import Deck


@pytest.fixture
def fx_cards(mocker):
    fake_card1 = mocker.patch("src.card.Card")
    fake_card1.title = "Fake Card 1"
    fake_card1.contents = "Fake Contents 1"
    fake_card1.answer = "Fake Answer 1"
    fake_card1.references = "Fake References 1"
    fake_card2 = mocker.patch("src.card.Card")
    fake_card2.title = "Fake Card 2"
    fake_card2.contents = "Fake Contents 2"
    fake_card2.answer = "Fake Answer 2"
    fake_card2.references = "Fake References 2"

    fake_cards = [fake_card1, fake_card2]

    yield fake_cards


def test__add_card__with_card_added__appends_card(fx_cards):
    deck = Deck()
    fake_card = fx_cards[0]

    deck.add_card(fake_card)

    assert fake_card in deck.cards


def test__add_card__with_card_added__updates_size(fx_cards):
    deck = Deck()
    fake_card = fx_cards[0]

    assert deck.size == 0

    deck.add_card(fake_card)

    assert deck.size == 1


def test__remove_card__with_existing_card__removes_card(fx_cards):
    deck = Deck()
    fake_card = fx_cards[0]
    deck.cards.append(fake_card)
    deck.size = 1

    deck.remove_card(fake_card)

    assert fake_card not in deck.cards


def test__remove_card__with_existing_card__updates_size(fx_cards):
    deck = Deck()
    fake_card = fx_cards[0]
    deck.cards.append(fake_card)
    deck.size = 1

    deck.remove_card(fake_card)

    assert deck.size == 0
