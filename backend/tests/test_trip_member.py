from src.models.trip_member import TripMember


def test_a_member_links_a_user_to_a_trip():
    member = TripMember(trip_id=1, user_id=2)
    assert member.trip_id == 1
    assert member.user_id == 2
