from src.a_star import a_star_search
from src.heuristic import naismith_estimate
from src.models import Coordinate, MapGrid
import numpy as np


def test_a_star_low_cost_path_diagnonal():
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

    expected_result = [Coordinate(x=4, y=4, z=10),
                       Coordinate(x=3, y=3, z=10),
                       Coordinate(x=2, y=2, z=10),
                       Coordinate(x=1, y=1, z=10),
                       Coordinate(x=0, y=0, z=10)]
    assert coords == expected_result


def test_a_star_low_cost_path_around_edge():
    grid = np.array([[10., 0., 0.],
                     [10., 0., 0.],
                     [0., 10., 10.]])
    my_grid = MapGrid(data=grid,
                      bottom_left=Coordinate(0, 0),
                      top_right=Coordinate(0.1, 0.1))

    start = Coordinate(x=0, y=0)
    end = Coordinate(x=2, y=2)
    coords, distance = a_star_search(map_grid=my_grid,
                                     start_grid_position=start,
                                     end_grid_position=end,
                                     heuristic=naismith_estimate)

    expected_result = [Coordinate(x=2, y=2, z=10),
                       Coordinate(x=1, y=2, z=10),
                       Coordinate(x=0, y=1, z=10),
                       Coordinate(x=0, y=0, z=10)]

    assert coords == expected_result


def test_a_follow_meandering_hill_climb():
    grid = np.array([[90., 91., 92., 93., 94., 0.],
                     [0., 0., 0., 0., 0., 95.],
                     [0., 0., 0., 0., 96., 0.],
                     [0., 0., 0., 97., 0., 0.],
                     [0., 0., 0., 98., 0., 0.],
                     [0., 0., 0., 0., 99., 100.]])

    my_grid = MapGrid(data=grid,
                      bottom_left=Coordinate(0, 0),
                      top_right=Coordinate(1, 1))

    start = Coordinate(x=0, y=0)
    end = Coordinate(x=5, y=5)
    coords, distance = a_star_search(map_grid=my_grid,
                                     start_grid_position=start,
                                     end_grid_position=end,
                                     heuristic=naismith_estimate)

    expected_result = [Coordinate(x=5, y=5, z=100.),
                       Coordinate(x=4, y=5, z=99.),
                       Coordinate(x=3, y=4, z=98.),
                       Coordinate(x=3, y=3, z=97.),
                       Coordinate(x=4, y=2, z=96.),
                       Coordinate(x=5, y=1, z=95.),
                       Coordinate(x=4, y=0, z=94.),
                       Coordinate(x=3, y=0., z=93.),
                       Coordinate(x=2, y=0, z=92.),
                       Coordinate(x=1, y=0, z=91.),
                       Coordinate(x=0, y=0, z=90.)]
    assert coords == expected_result


def test_a_star_returns_correct_distance():
    grid = np.array([[10., 10., 10.],
                     [0., 0., 0.],
                     [0., 0., 0.]])
    # a 1 km grid
    my_grid = MapGrid(data=grid,
                      bottom_left=Coordinate(0, 0),
                      top_right=Coordinate(1000, 1000))
    # The shortest distance is 1 km in a straight line
    start = Coordinate(x=0, y=0)
    end = Coordinate(x=2, y=0)

    coords, distance = a_star_search(map_grid=my_grid,
                                     start_grid_position=start,
                                     end_grid_position=end,
                                     heuristic=naismith_estimate)
    # 1 km takes 15 mins by Naismith's rule -but each step is from the centre of one grid point to the centre of the
    # next, so we've only moved 2/3rds of that distance
    assert distance == 10


def test_a_star_returns_correct_distance_including_elevation():
    grid = np.array([[10., 60., 10.],
                     [0., 0., 0.],
                     [0., 0., 0.]])
    # a 1 km grid
    my_grid = MapGrid(data=grid,
                      bottom_left=Coordinate(0, 0),
                      top_right=Coordinate(1000, 1000))
    # The shortest distance is 1 km in a straight line
    start = Coordinate(x=0, y=0)
    end = Coordinate(x=2, y=0)

    coords, distance = a_star_search(map_grid=my_grid,
                                     start_grid_position=start,
                                     end_grid_position=end,
                                     heuristic=naismith_estimate)
    # 1 km takes 15 mins by Naismith's rule -but each step is from the centre of one grid point to the centre of the
    # next, so we've only moved 2/3rds of that distance. Add 5 minutes for the 50m elevation gain
    assert distance == 15
