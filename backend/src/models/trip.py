from dataclasses import dataclass, field


@dataclass
class Trip:
    id: int
    title: str
    base_currency: str
    _expenses: list = field(default_factory=list, init=False)
    _shares: list = field(default_factory=list, init=False)

    @property
    def expenses(self):
        return tuple(self._expenses)  # you can look, not push

    @property
    def shares(self):
        return tuple(self._shares)

    def add_expense(self, expense, shares):
        if expense.amount.currency != self.base_currency:
            raise ValueError(f"this trip only takes {self.base_currency}")
        if not expense.is_covered_by(shares):
            raise ValueError("shares do not add up")
        self._expenses.append(expense)
        self._shares.extend(shares)
