from dataclasses import dataclass


@dataclass
class Trip:
    id: int
    title: str
    base_currency: str
