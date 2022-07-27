from src.models import Coordinate, MapGrid
import numpy as np


def test_map_grid_initialises_coordinates_for_square_grid():
    example_data = np.zeros([10, 10])
    example_map = MapGrid(data=example_data,
                          bottom_left=Coordinate(x=0, y=0),
                          top_right=Coordinate(x=10, y=10))
    expected_result = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    calculated_result = example_map.y_coords
    np.testing.assert_array_equal(calculated_result, expected_result)

    calculated_result = example_map.x_coords
    np.testing.assert_array_equal(calculated_result, expected_result)


def test_map_grid_initialises_coordinates_for_rectangular_grid():
    example_data = np.zeros([10, 5])
    print(example_data)
    example_map = MapGrid(data=example_data,
                          bottom_left=Coordinate(x=0, y=0),
                          top_right=Coordinate(x=5, y=10))

    expected_result = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    calculated_result = example_map.y_coords
    np.testing.assert_array_equal(calculated_result, expected_result)

    expected_result = np.array([1, 2, 3, 4, 5])
    calculated_result = example_map.x_coords
    np.testing.assert_array_equal(calculated_result, expected_result)


def test_map_grid_coordinate_to_grid_when_coord_in_grid_centre():
    example_data = np.zeros([10, 10])
    # Define a map with 10 points in each direction, over a 5 m square
    example_map = MapGrid(data=example_data,
                          bottom_left=Coordinate(x=0, y=0),
                          top_right=Coordinate(x=5, y=5))

    # Find the grid coordinates for spatial coordinate (2.5, 2.5), halfway in each direction (remember zero indexing)
    expected_result = Coordinate(x=4, y=4)
    calculated_result = example_map.coordinate_to_grid_position(Coordinate(x=2.5, y=2.5))
    assert calculated_result == expected_result


def test_map_grid_coordinate_to_grid_when_coord_is_out_of_bounds():
    example_data = np.zeros([10, 10])
    # Define a map with 10 points in each direction, over a 5 m square
    example_map = MapGrid(data=example_data,
                          bottom_left=Coordinate(x=0, y=0),
                          top_right=Coordinate(x=5, y=5))

    # Find the grid coordinates for spatial coordinate (6, 6). Out of bounds, so should be top right corner of grid
    expected_result = Coordinate(x=9, y=9)
    calculated_result = example_map.coordinate_to_grid_position(Coordinate(x=6, y=6))
    assert calculated_result == expected_result


def test_map_grid_spatial_coordinate_at():
    example_data = np.zeros([10, 10])
    # Define a map with 10 points in each direction, over a 5 m square
    example_data[4][3] = 10
    example_map = MapGrid(data=example_data,
                          bottom_left=Coordinate(x=0, y=0),
                          top_right=Coordinate(x=5, y=5))

    expected_result = Coordinate(x=2., y=2.5, z=10)
    # remember arrays are zero indexed
    calculated_result = example_map.spatial_coordinate_at(Coordinate(x=3, y=4))
    assert calculated_result == expected_result


def test_map_grid_spatial_coordinate_at_on_rectangular_grid():
    grid = np.array([[0., 0., 0.],
                     [0., 0., 0.],
                     [0., 0., 0.],
                     [0., 0., 0.],
                     [0., 0., 5.],
                     [0., 0., 0.]])

    my_grid = MapGrid(data=grid,
                      bottom_left=Coordinate(x=0, y=0),
                      top_right=Coordinate(x=3, y=6))
    expected_result = Coordinate(x=3, y=5, z=5)
    # remember arrays are zero indexed
    calculated_result = my_grid.spatial_coordinate_at(Coordinate(x=2, y=4))
    assert calculated_result == expected_result



def test_map_grid_contains_position():
    example_data = np.zeros([10, 10])
    # Define a map with 10 points in each direction, over a 5 m square
    example_map = MapGrid(data=example_data,
                          bottom_left=Coordinate(x=0, y=0),
                          top_right=Coordinate(x=5, y=5))

    # This is a 10 by 10 grid, so it should have an entry at (3, 3)
    assert example_map.contains_position(Coordinate(x=3, y=3))


def test_map_grid_not_contains_position():
    example_data = np.zeros([10, 10])
    # Define a map with 10 points in each direction, over a 5 m square
    example_map = MapGrid(data=example_data,
                          bottom_left=Coordinate(x=0, y=0),
                          top_right=Coordinate(x=5, y=5))

    # This is a 10 by 10 grid, so it should not have an entry at (11, 11)
    assert not example_map.contains_position(Coordinate(x=11, y=11))
