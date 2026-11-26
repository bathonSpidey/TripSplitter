from src.logic.splitter import ExpenseSplitter
from src.models.money import Money


def test_ninety_euros_split_in_three():
    splitter = ExpenseSplitter()
    shares = splitter.split_equally(1, Money(9000, "EUR"), [1, 2, 3])
    cents = [share.amount.cents for share in shares]
    assert cents == [3000, 3000, 3000]


def test_the_leftover_cent_goes_to_the_first_friend():
    splitter = ExpenseSplitter()
    shares = splitter.split_equally(1, Money(10000, "EUR"), [1, 2, 3])
    cents = [share.amount.cents for share in shares]
    assert cents == [3334, 3333, 3333]


def test_shares_always_add_up_to_the_amount():
    splitter = ExpenseSplitter()
    shares = splitter.split_equally(1, Money(10001, "EUR"), [1, 2, 3, 4])
    assert sum(share.amount.cents for share in shares) == 10001


def test_ninety_euros_split_in_two():
    splitter = ExpenseSplitter()
    shares = splitter.split_equally(1, Money(9000, "EUR"), [1, 2])
    cents = [share.amount.cents for share in shares]
    assert cents == [4500, 4500]


def test_the_shares_always_add_up_to_the_total():
    splitter = ExpenseSplitter()
    shares = splitter.split_equally(1, Money(10001, "EUR"), [1, 2, 3])
    cents = [share.amount.cents for share in shares]
    assert sum(cents) == 10001


def test_everyone_can_pay_for_what_they_had():
    had = {1: "60", 2: "26", 3: "4"}
    amounts = {who: Money.parse(text, "EUR") for who, text in had.items()}
    shares = ExpenseSplitter().split_individually(1, amounts)
    assert [share.amount.cents for share in shares] == [6000, 2600, 400]
