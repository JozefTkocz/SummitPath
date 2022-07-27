from src.models import Coordinate, MapGrid, Node, NodeGraph
import numpy as np


def test_node_grid_initialisation():
    example_data = np.zeros([10, 10])
    example_map = MapGrid(data=example_data,
                          bottom_left=Coordinate(x=0, y=0),
                          top_right=Coordinate(x=10, y=10))
    node_grid = NodeGraph.from_map_grid(example_map)
    assert node_grid.grid[5][5].location == Coordinate(x=5, y=5)
    assert node_grid.grid[5][5].heuristic_weight == np.inf
    assert node_grid.grid[5][5].distance_from_start == np.inf


def test_node_grid_upsert():
    example_data = np.zeros([10, 10])
    example_map = MapGrid(data=example_data,
                          bottom_left=Coordinate(x=0, y=0),
                          top_right=Coordinate(x=10, y=10))
    node_grid = NodeGraph.from_map_grid(example_map)
    new_node = Node(location=Coordinate(x=0, y=0), heuristic_weight=100., distance_from_start=12.)
    node_grid.upsert(new_node)
    assert node_grid.grid[0][0].heuristic_weight == 100.


def test_node_grid_get_node_at():
    example_data = np.zeros([10, 10])
    example_map = MapGrid(data=example_data,
                          bottom_left=Coordinate(x=0, y=0),
                          top_right=Coordinate(x=10, y=10))
    node_grid = NodeGraph.from_map_grid(example_map)
    new_node = Node(location=Coordinate(x=0, y=0), heuristic_weight=100., distance_from_start=12.)
    node_grid.upsert(new_node)
    assert node_grid.get_node_at(new_node.location).heuristic_weight == 100.


def test_node_grid_get_neighbours_returns_8_neighbours_if_in_centre_of_grid():
    example_data = np.zeros([10, 10])
    example_map = MapGrid(data=example_data,
                          bottom_left=Coordinate(x=0, y=0),
                          top_right=Coordinate(x=10, y=10))
    node_grid = NodeGraph.from_map_grid(example_map)
    centre_node = node_grid.get_node_at(Coordinate(x=4, y=4))
    neighbours = node_grid.get_neighbours(centre_node)
    assert len(neighbours) == 8


def test_node_grid_get_neighbours_returns_5_neighbours_if_in_centre_edge_of_grid():
    example_data = np.zeros([10, 10])
    example_map = MapGrid(data=example_data,
                          bottom_left=Coordinate(x=0, y=0),
                          top_right=Coordinate(x=10, y=10))
    node_grid = NodeGraph.from_map_grid(example_map)
    centre_node = node_grid.get_node_at(Coordinate(x=0, y=4))
    neighbours = node_grid.get_neighbours(centre_node)
    assert len(neighbours) == 5


def test_node_grid_get_neighbours_returns_3_neighbours_if_in_corner_of_grid():
    example_data = np.zeros([10, 10])
    example_map = MapGrid(data=example_data,
                          bottom_left=Coordinate(x=0, y=0),
                          top_right=Coordinate(x=10, y=10))
    node_grid = NodeGraph.from_map_grid(example_map)
    centre_node = node_grid.get_node_at(Coordinate(x=0, y=0))
    neighbours = node_grid.get_neighbours(centre_node)
    assert len(neighbours) == 3
