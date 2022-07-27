from dataclasses import dataclass
from typing import List

import numpy as np


@dataclass
class Coordinate:
    x: float = 0.
    y: float = 0.
    z: float = 0.

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __add__(self, other):
        return Coordinate(x=self.x + other.x, y=self.y + other.y, z=self.z + other.z)

    def __sub__(self, other):
        return Coordinate(x=self.x - other.x, y=self.y - other.y, z=self.z - other.z)


@dataclass
class Node:
    location: Coordinate
    heuristic_weight: float
    distance_from_start: float
    came_from: 'Node' = None

    def __eq__(self, other):
        return self.heuristic_weight == other.heuristic_weight

    def __lt__(self, other):
        return self.heuristic_weight < other.heuristic_weight


class MapGrid:
    def __init__(self, data: np.array,
                 bottom_left: Coordinate,
                 top_right: Coordinate):
        self.grid = data

        self.x_spacing = None
        self.y_spacing = None
        self.x_coords = None
        self.y_coords = None
        self.x_size = None
        self.y_size = None
        self._set_boundary_sizes()
        self._populate_grid_coordinates(bottom_left, top_right)

    def _populate_grid_coordinates(self, bottom_left: Coordinate, top_right: Coordinate):
        self.x_spacing = (top_right.x - bottom_left.x) / self.x_size
        self.y_spacing = (top_right.y - bottom_left.y) / self.y_size

        self.x_coords = np.linspace(bottom_left.x + self.x_spacing, top_right.x, self.grid.shape[0])
        self.y_coords = np.linspace(bottom_left.y + self.y_spacing, top_right.y, self.grid.shape[1])

    def _set_boundary_sizes(self):
        self.x_size = self.grid.shape[0]
        self.y_size = self.grid.shape[1]

    def coordinate_to_grid_position(self, coordinate: Coordinate) -> Coordinate:
        x, y = np.argmin(np.abs(self.x_coords - coordinate.x)), np.argmin(np.abs(self.y_coords - coordinate.y))
        return Coordinate(x=x, y=y)

    def elevation_at(self, coordinate: Coordinate) -> float:
        grid_position = self.coordinate_to_grid_position(coordinate)
        return self.grid[grid_position.x][grid_position.y]

    def spatial_coordinate_at(self, position: Coordinate) -> Coordinate:
        x = self.x_coords[position.x]
        y = self.y_coords[position.y]
        return Coordinate(x=x, y=y, z=self.elevation_at(Coordinate(x=x, y=y)))

    def contains_position(self, position: Coordinate) -> bool:
        contains_x = 0. <= position.x <= self.x_size
        contains_y = 0. <= position.y <= self.y_size
        return contains_x and contains_y


class NodeGraph:
    def __init__(self, grid: np.array):
        self.grid = grid
        self.x_size = None
        self.y_size = None
        self._set_boundary_sizes()

    @classmethod
    def from_map_grid(cls, grid: MapGrid) -> 'NodeGraph':
        node_grid = np.ndarray((grid.x_size, grid.y_size), dtype=np.object)
        for x_position in range(0, grid.x_size):
            for y_position in range(0, grid.y_size):
                height = grid.grid[x_position][y_position]
                node_grid[x_position][y_position] = Node(location=Coordinate(x=x_position, y=y_position, z=height),
                                                         heuristic_weight=np.inf, distance_from_start=np.inf)
        return cls(node_grid)

    def _set_boundary_sizes(self):
        self.x_size = self.grid.shape[0]
        self.y_size = self.grid.shape[1]

    def contains_position(self, position: Coordinate) -> bool:
        contains_x = 0. <= position.x < self.x_size
        contains_y = 0. <= position.y < self.y_size
        return contains_x and contains_y

    def upsert(self, node: Node):
        x_postion = node.location.x
        y_position = node.location.y
        self.grid[x_postion][y_position] = node

    def get_node_at(self, location: Coordinate) -> Node:
        return self.grid[location.x][location.y]

    def get_neighbours(self, node: Node) -> List[Node]:
        x_offset = Coordinate(x=1, y=0)
        y_offset = Coordinate(x=0, y=1)
        location = node.location
        candidate_neighbour_locations = [location + x_offset,
                                         location - x_offset,
                                         location + y_offset,
                                         location - y_offset,
                                         location + x_offset + y_offset,
                                         location + x_offset - y_offset,
                                         location - x_offset + y_offset,
                                         location - x_offset - y_offset]
        return [self.get_node_at(l) for l in candidate_neighbour_locations if self.contains_position(l)]