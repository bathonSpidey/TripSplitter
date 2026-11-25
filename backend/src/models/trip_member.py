from dataclasses import dataclass


@dataclass
class TripMember:
    trip_id: int
    user_id: int
