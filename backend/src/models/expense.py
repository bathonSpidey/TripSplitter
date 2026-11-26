from dataclasses import dataclass
from datetime import date

from src.models.expense_status import ExpenseStatus
from src.models.money import Money


@dataclass
class Expense:
    id: int
    trip_id: int
    title: str
    date: date
    paid_by: int
    amount: Money
    source: str = "manual"
    status: ExpenseStatus = ExpenseStatus.ADDED

    def __post_init__(self):
        self.status = ExpenseStatus(self.status)  # a typo stops here

    def dispute(self):
        self.status = ExpenseStatus.DISPUTED

    def counts(self):
        return self.status != ExpenseStatus.DISPUTED

    def is_covered_by(self, shares):
        nothing = Money(0, self.amount.currency)
        total = sum((share.amount for share in shares), nothing)
        return total == self.amount
