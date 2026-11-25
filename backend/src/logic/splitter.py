from src.models.expense_share import ExpenseShare


class ExpenseSplitter:
    def split_equally(self, expense_id, total, user_ids):
        each, leftover = divmod(total, len(user_ids))
        shares = []
        for place, user_id in enumerate(user_ids):
            extra = 1 if place < leftover else 0
            cents = each + extra
            share = ExpenseShare(expense_id, user_id, cents)
            shares.append(share)
        return shares
