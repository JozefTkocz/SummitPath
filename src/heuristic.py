import numpy as np

from src.models import Coordinate

from typing import Callable

Heuristic = Callable[[Coordinate, Coordinate], float]


def naismith_estimate(point_1: Coordinate,
                      point_2: Coordinate) -> float:
    minutes_per_km = 15
    minutes_per_m_elevation = 0.1

    horizontal_distance_km = 1.0e-3 * np.sqrt((point_2.x - point_1.x) ** 2 + (point_2.y - point_1.y) ** 2)
    elevation_difference = point_2.z - point_1.z
    elevation_time = elevation_difference * minutes_per_m_elevation * (elevation_difference > 0)
    return horizontal_distance_km * minutes_per_km + elevation_time
