from src.models.trip import Trip


def test_trip_keeps_its_details():
    trip = Trip(id=1, title="Prague", base_currency="EUR")
    assert trip.title == "Prague"
    assert trip.base_currency == "EUR"
