from src.models.expense_share import ExpenseShare
from src.models.money import Money


class ExpenseSplitter:
    def split_equally(self, expense_id, total, user_ids):
        if not user_ids:
            raise ValueError("nobody to split the bill between")
        each, leftover = divmod(total.cents, len(user_ids))
        shares = []
        for place, user_id in enumerate(user_ids):
            extra = 1 if place < leftover else 0
            amount = Money(each + extra, total.currency)
            share = ExpenseShare(expense_id, user_id, amount)
            shares.append(share)
        return shares

    def split_individually(self, expense_id, amounts):
        return [
            ExpenseShare(expense_id, user_id, amount)
            for user_id, amount in amounts.items()
        ]
