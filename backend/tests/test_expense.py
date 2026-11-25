from datetime import date

from src.models.expense import Expense


def make_expense():
    return Expense(
        id=1,
        trip_id=1,
        title="Dinner",
        date=date(2026, 6, 14),
        paid_by=1,
        amount_cents=9000,
        currency="EUR",
    )


def test_money_is_stored_in_whole_cents():
    assert make_expense().amount_cents == 9000


def test_a_new_expense_starts_as_added():
    assert make_expense().status == "added"
