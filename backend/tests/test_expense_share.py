from src.models.expense_share import ExpenseShare
from src.models.money import Money


def test_a_share_says_who_owes_how_much():
    share = ExpenseShare(1, 2, Money.parse("30", "EUR"))
    assert share.user_id == 2
    assert share.amount == Money(3000, "EUR")
