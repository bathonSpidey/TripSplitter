from datetime import date

from src.logic.balances import BalanceCalculator
from src.logic.splitter import ExpenseSplitter
from src.models.expense import Expense
from src.models.money import Money
from src.models.trip import Trip


def trip_with_dinner():
    trip = Trip(id=1, title="Prague", base_currency="EUR")
    dinner = Expense(
        id=1,
        trip_id=1,
        title="Dinner",
        date=date(2026, 6, 14),
        paid_by=1,
        amount=Money.parse("90", "EUR"),
    )
    shares = ExpenseSplitter().split_equally(1, dinner.amount, [1, 2, 3])
    trip.add_expense(dinner, shares)
    return trip, dinner


def test_the_payer_is_owed_what_the_others_owe():
    trip, _ = trip_with_dinner()
    assert BalanceCalculator().balances(trip) == {
        1: Money(6000, "EUR"),
        2: Money(-3000, "EUR"),
        3: Money(-3000, "EUR"),
    }


def test_a_disputed_expense_leaves_no_balance():
    trip, dinner = trip_with_dinner()
    dinner.dispute()
    assert BalanceCalculator().balances(trip) == {}
