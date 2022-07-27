from src.a_star import a_star_search
from src.heuristic import naismith_estimate
from src.models import Coordinate, MapGrid
import numpy as np


def test_a_star_cardinal_directions_only_returns_correct_distance():
    grid = np.array([[10., 0., 0., 0., 0.],
                     [0., 10., 0., 0., 0.],
                     [0., 0., 10., 0., 0.],
                     [0., 0., 0., 10., 0.],
                     [0., 0., 0., 0., 10.]])
    my_grid = MapGrid(data=grid,
                      bottom_left=Coordinate(0, 0),
                      top_right=Coordinate(500, 500))

    start = Coordinate(x=0, y=0)
    end = Coordinate(x=4, y=4)
    coords, distance = a_star_search(map_grid=my_grid,
                                     start_grid_position=start,
                                     end_grid_position=end,
                                     heuristic=naismith_estimate)

    expected_result = [Coordinate(x=4, y=4),
                       Coordinate(x=3, y=3),
                       Coordinate(x=2, y=2),
                       Coordinate(x=1, y=1),
                       Coordinate(x=0, y=0)]
    assert coords == expected_result


def test_a_star_again():
    grid = np.array([[10., 0., 0.],
                     [10., 0., 0.],
                     [0., 10., 10.]])
    my_grid = MapGrid(data=grid,
                      bottom_left=Coordinate(0, 0),
                      top_right=Coordinate(1, 1))

    start = Coordinate(x=0, y=0)
    end = Coordinate(x=2, y=2)
    coords, distance = a_star_search(map_grid=my_grid,
                                     start_grid_position=start,
                                     end_grid_position=end,
                                     heuristic=naismith_estimate)

    expected_result = [Coordinate(x=2, y=2),
                       Coordinate(x=2, y=1),
                       Coordinate(x=1, y=0),
                       Coordinate(x=0, y=0)]
    assert coords == expected_result


def test_a_star_again_again():
    grid = np.array([[90., 91., 92., 93., 94., 0.],
                     [0., 97., 0., 0., 0., 95.],
                     [0., 0., 97., 0., 96., 0.],
                     [0., 0., 0., 97., 0., 0.],
                     [0., 0., 0., 98., 0., 0.],
                     [0., 0., 0., 0., 99., 100.]])
    # x->
    # y
    # \
    my_grid = MapGrid(data=grid,
                      bottom_left=Coordinate(0, 0),
                      top_right=Coordinate(1, 1))

    start = Coordinate(x=0, y=0)
    end = Coordinate(x=5, y=5)
    coords, distance = a_star_search(map_grid=my_grid,
                                     start_grid_position=start,
                                     end_grid_position=end,
                                     heuristic=naismith_estimate)

    expected_result = [Coordinate(x=2, y=2),
                       Coordinate(x=2, y=1),
                       Coordinate(x=1, y=0),
                       Coordinate(x=0, y=0)]
    assert coords == expected_result
