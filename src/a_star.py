import bisect
from typing import Any, Callable, List

import numpy as np

from src.models import Coordinate, MapGrid, Node, NodeGraph


def reconstruct_path(node: Node):
    complete = False
    coords = []
    current_node = node
    while not complete:
        coords.append(current_node.location)
        current_node = current_node.came_from
        if current_node is None:
            complete = True

    return coords, node.distance_from_start


def a_star_search(map_grid: MapGrid,
                  start_grid_position: Coordinate,
                  end_grid_position: Coordinate,
                  heuristic: Callable[[Coordinate, Coordinate], float]):
    open_set = PriorityQueue()

    spatial_coordinate_end = map_grid.spatial_coordinate_at(end_grid_position)
    spatial_coordinate_start = map_grid.spatial_coordinate_at(start_grid_position)

    start_node = Node(location=start_grid_position,
                      heuristic_weight=heuristic(spatial_coordinate_start, spatial_coordinate_end),
                      distance_from_start=0.)
    start_node.location.z = spatial_coordinate_start.z

    end_node = Node(location=end_grid_position,
                    heuristic_weight=0.,
                    distance_from_start=np.inf)
    end_node.location.z = spatial_coordinate_end.z

    node_graph = NodeGraph.from_map_grid(map_grid)
    node_graph.upsert(start_node)
    node_graph.upsert(end_node)

    open_set.insert(start_node)
    while not open_set.is_empty():
        current_node: Node = open_set.get_first()
        if current_node.location == end_node.location:
            return reconstruct_path(current_node)

        spatial_coordinate_current = map_grid.spatial_coordinate_at(current_node.location)
        for neighbour in node_graph.get_neighbours(current_node):
            spatial_coordinate_neighbour = map_grid.spatial_coordinate_at(neighbour.location)
            distance_to_neighbour_via_current = current_node.distance_from_start + heuristic(spatial_coordinate_current,
                                                                                             spatial_coordinate_neighbour)

            if distance_to_neighbour_via_current < neighbour.distance_from_start:
                neighbour.distance_from_start = distance_to_neighbour_via_current
                neighbour.heuristic_weight = neighbour.distance_from_start + heuristic(spatial_coordinate_neighbour,
                                                                                       spatial_coordinate_end)
                neighbour.came_from = current_node
                node_graph.upsert(neighbour)

                if not open_set.contains(neighbour):
                    open_set.insert(neighbour)

    print('Got to the end and nothing happened')
    return False


class PriorityQueue:
    def __init__(self):
        self.data: List[Any] = []

    def is_empty(self) -> bool:
        return len(self.data) == 0

    def get_first(self) -> Any:
        return self.data.pop(0)

    def contains(self, item: Any) -> bool:
        return item in self.data

    def insert(self, item: Any):
        bisect.insort(self.data, item)
