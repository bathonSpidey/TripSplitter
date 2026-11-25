from src.models.user import User


def test_user_keeps_its_details():
    user = User(
        id=1,
        email="anna@example.com",
        display_name="Anna",
        paypal_link="paypal.me/anna",
    )
    assert user.display_name == "Anna"
