from src.heuristic import naismith_estimate
from src.models import Coordinate


def test_naismith_distance_estimate_1d():
    position_1 = Coordinate(x=0, y=0, z=0)
    position_2 = Coordinate(x=1000, y=0, z=0)

    expected_result = 15
    calculated_result = naismith_estimate(position_1, position_2)
    assert calculated_result == expected_result


def test_naismith_distance_estimate_2d():
    position_1 = Coordinate(x=0, y=0, z=0)
    position_2 = Coordinate(x=3000, y=4000, z=0)

    expected_result = 75
    calculated_result = naismith_estimate(position_1, position_2)
    assert calculated_result == expected_result


def test_naismith_elevation_estimate_ascending():
    position_1 = Coordinate(x=0, y=0, z=0)
    position_2 = Coordinate(x=0, y=0, z=100)

    expected_result = 10
    calculated_result = naismith_estimate(position_1, position_2)
    assert calculated_result == expected_result


def test_naismith_elevation_estimate_descending():
    position_1 = Coordinate(x=0, y=0, z=1000)
    position_2 = Coordinate(x=0, y=0, z=0)

    expected_result = 0
    calculated_result = naismith_estimate(position_1, position_2)
    assert calculated_result == expected_result


def test_naismith_combined_distance_and_elevation_estiamte():
    position_1 = Coordinate(x=0, y=0, z=0)
    position_2 = Coordinate(x=3000, y=4000, z=100)

    expected_result = 85
    calculated_result = naismith_estimate(position_1, position_2)
    assert calculated_result == expected_result
