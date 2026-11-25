from datetime import date

from src.logic.balances import BalanceCalculator
from src.logic.splitter import ExpenseSplitter
from src.models.expense import Expense


def dinner(status="added"):
    return Expense(
        id=1,
        trip_id=1,
        title="Dinner",
        date=date(2026, 6, 14),
        paid_by=1,
        amount_cents=9000,
        currency="EUR",
        status=status,
    )


def shares_of_dinner():
    return ExpenseSplitter().split_equally(1, 9000, [1, 2, 3])


def test_the_payer_is_owed_what_the_others_owe():
    result = BalanceCalculator().balances(
        [dinner()], shares_of_dinner()
    )
    assert result == {1: 6000, 2: -3000, 3: -3000}


def test_a_disputed_expense_does_not_count():
    result = BalanceCalculator().balances(
        [dinner("disputed")], shares_of_dinner()
    )
    assert result == {}
