from dataclasses import dataclass

from src.models.money import Money


@dataclass
class ExpenseShare:
    expense_id: int
    user_id: int
    amount: Money

    def __post_init__(self):
        if self.amount.cents < 0:
            raise ValueError("a share cannot be negative")
