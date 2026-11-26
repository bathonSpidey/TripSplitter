from src.models.money import Money


class BalanceCalculator:
    def balances(self, trip):
        nothing = Money(0, trip.base_currency)
        result = {}
        counted = [e for e in trip.expenses if e.counts()]
        ids = [expense.id for expense in counted]
        for expense in counted:
            who = expense.paid_by
            result[who] = result.get(who, nothing) + expense.amount
        for share in trip.shares:
            if share.expense_id in ids:
                who = share.user_id
                result[who] = result.get(who, nothing) - share.amount
        return result
