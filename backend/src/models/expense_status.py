from enum import Enum


class ExpenseStatus(Enum):
    ADDED = "added"
    DISPUTED = "disputed"
    SETTLED = "settled"
