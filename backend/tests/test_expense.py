from datetime import date

import pytest

from src.models.expense import Expense
from src.models.expense_status import ExpenseStatus
from src.models.money import Money


def make_expense(**changes):
    details = dict(
        id=1,
        trip_id=1,
        title="Dinner",
        date=date(2026, 6, 14),
        paid_by=1,
        amount=Money.parse("90", "EUR"),
    )
    return Expense(**{**details, **changes})


def test_money_is_stored_in_whole_cents():
    assert make_expense().amount.cents == 9000


def test_a_new_expense_starts_as_added():
    assert make_expense().status == ExpenseStatus.ADDED


def test_a_disputed_expense_does_not_count():
    expense = make_expense()
    expense.dispute()
    assert not expense.counts()


def test_a_typo_is_not_a_status():
    with pytest.raises(ValueError):
        make_expense(status="dispute")
