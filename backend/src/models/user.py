from dataclasses import dataclass


@dataclass
class User:
    id: int
    email: str
    display_name: str
    paypal_link: str
