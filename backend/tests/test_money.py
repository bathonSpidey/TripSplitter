import pytest

from src.models.money import Money


def test_twelve_euros_seventy_four_is_1274_cents():
    assert Money.parse("12.74", "EUR") == Money(1274, "EUR")


def test_euros_and_francs_do_not_add_up():
    with pytest.raises(ValueError):
        Money(9000, "EUR") + Money(9000, "CHF")


def test_no_cent_gets_lost():
    assert Money.parse("19.99", "EUR") == Money(1999, "EUR")


@pytest.mark.parametrize("text", ["12.745", "12,74", "abc", "", "NaN"])
def test_unclear_amounts_are_refused(text):
    with pytest.raises(ValueError):
        Money.parse(text, "EUR")


def test_a_floating_point_number_is_refused():
    with pytest.raises(TypeError):
        Money.parse(12.74, "EUR")


def test_cents_are_whole_numbers():
    with pytest.raises(TypeError):
        Money(12.74, "EUR")


def test_not_every_currency_has_two_decimals():
    assert Money.parse("500", "JPY") == Money(500, "JPY")
    assert Money.parse("1.250", "KWD") == Money(1250, "KWD")


def test_money_speaks_to_people():
    assert str(Money(1274, "EUR")) == "12.74 EUR"
