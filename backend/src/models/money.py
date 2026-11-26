from dataclasses import dataclass
from decimal import Decimal, InvalidOperation

# how many digits each currency has after the point
DECIMALS = {"EUR": 2, "CHF": 2, "USD": 2, "JPY": 0, "KWD": 3}


@dataclass(frozen=True)
class Money:
    cents: int  # the smallest unit: cents for euros
    currency: str

    def __post_init__(self):
        if not isinstance(self.cents, int):
            raise TypeError("cents must be a whole number")

    @classmethod
    def parse(cls, text, currency):
        if not isinstance(text, str):
            raise TypeError("give Money a text, not a number")
        try:
            amount = Decimal(text)
        except InvalidOperation:
            raise ValueError(f"not an amount: {text!r}")
        if not amount.is_finite():
            raise ValueError(f"not an amount: {text!r}")
        cents = amount.scaleb(DECIMALS[currency])
        if cents != cents.to_integral_value():
            raise ValueError(f"too many decimals for {currency}: {text}")
        return cls(int(cents), currency)

    def __add__(self, other):
        self._check_currency(other)
        return Money(self.cents + other.cents, self.currency)

    def __sub__(self, other):
        self._check_currency(other)
        return Money(self.cents - other.cents, self.currency)

    def __str__(self):
        places = DECIMALS[self.currency]
        amount = Decimal(self.cents).scaleb(-places)
        return f"{amount:.{places}f} {self.currency}"

    def _check_currency(self, other):
        if other.currency != self.currency:
            raise ValueError("cannot mix different currencies")
