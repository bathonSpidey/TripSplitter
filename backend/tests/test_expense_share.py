from src.models.expense_share import ExpenseShare


def test_a_share_says_who_owes_how_many_cents():
    share = ExpenseShare(expense_id=1, user_id=2, share_cents=3000)
    assert share.user_id == 2
    assert share.share_cents == 3000
