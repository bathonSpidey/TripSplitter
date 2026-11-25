from dataclasses import dataclass
from datetime import date


@dataclass
class Expense:
    id: int
    trip_id: int
    title: str
    date: date
    paid_by: int
    amount_cents: int
    currency: str
    source: str = "manual"
    status: str = "added"
