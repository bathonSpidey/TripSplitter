class BalanceCalculator:
    def balances(self, expenses, shares):
        result = {}
        counted = []
        for expense in expenses:
            if expense.status != "disputed":
                counted.append(expense)
        ids = [expense.id for expense in counted]
        for expense in counted:
            who = expense.paid_by
            total = result.get(who, 0)
            result[who] = total + expense.amount_cents
        for share in shares:
            if share.expense_id in ids:
                who = share.user_id
                total = result.get(who, 0)
                result[who] = total - share.share_cents
        return result
