from datetime import date

import pytest

from src.logic.splitter import ExpenseSplitter
from src.models.expense import Expense
from src.models.expense_share import ExpenseShare
from src.models.money import Money
from src.models.trip import Trip


def prague():
    return Trip(id=1, title="Prague", base_currency="EUR")


def dinner(currency="EUR"):
    return Expense(
        id=1,
        trip_id=1,
        title="Dinner",
        date=date(2026, 6, 14),
        paid_by=1,
        amount=Money.parse("90", currency),
    )


def test_trip_keeps_its_details():
    assert prague().title == "Prague"
    assert prague().base_currency == "EUR"


def test_shares_must_add_up_to_the_amount():
    one_euro = ExpenseShare(1, 2, Money.parse("1", "EUR"))
    with pytest.raises(ValueError):
        prague().add_expense(dinner(), [one_euro])


def test_a_trip_only_takes_its_own_currency():
    francs = Money.parse("90", "CHF")
    shares = ExpenseSplitter().split_equally(1, francs, [1, 2, 3])
    with pytest.raises(ValueError):
        prague().add_expense(dinner("CHF"), shares)


def test_there_is_no_window_into_a_trip():
    with pytest.raises(AttributeError):
        prague().expenses.append(dinner())
