from src.logic.splitter import ExpenseSplitter


def test_ninety_euros_split_in_three():
    splitter = ExpenseSplitter()
    shares = splitter.split_equally(1, 9000, [1, 2, 3])
    cents = [share.share_cents for share in shares]
    assert cents == [3000, 3000, 3000]


def test_the_leftover_cent_goes_to_the_first_friend():
    splitter = ExpenseSplitter()
    shares = splitter.split_equally(1, 10000, [1, 2, 3])
    cents = [share.share_cents for share in shares]
    assert cents == [3334, 3333, 3333]


def test_shares_always_add_up_to_the_amount():
    splitter = ExpenseSplitter()
    shares = splitter.split_equally(1, 10001, [1, 2, 3, 4])
    assert sum(share.share_cents for share in shares) == 10001


def test_ninety_euros_split_in_two():
    splitter = ExpenseSplitter()
    shares = splitter.split_equally(1, 9000, [1, 2])
    cents = [share.share_cents for share in shares]
    assert cents == [4500, 4500]
