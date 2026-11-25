from dataclasses import dataclass


@dataclass
class ExpenseShare:
    expense_id: int
    user_id: int
    share_cents: int
