from dataclasses import dataclass

from src.models.money import Money


@dataclass
class ExpenseShare:
    expense_id: int
    user_id: int
    amount: Money
