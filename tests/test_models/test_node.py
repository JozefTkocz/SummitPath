import numpy as np

from src.models import Coordinate, Node


def test_node_greater_than_comparison():
    node_1 = Node(location=Coordinate(x=0, y=0), heuristic_weight=1, distance_from_start=np.inf)
    node_2 = Node(location=Coordinate(x=0, y=0), heuristic_weight=2, distance_from_start=np.inf)
    assert node_2 > node_1


def test_node_less_than_comparison():
    node_1 = Node(location=Coordinate(x=0, y=0), heuristic_weight=1, distance_from_start=np.inf)
    node_2 = Node(location=Coordinate(x=0, y=0), heuristic_weight=2, distance_from_start=np.inf)
    assert node_1 < node_2


def test_node_equality_comparison():
    node_1_a = Node(location=Coordinate(x=0, y=0), heuristic_weight=1, distance_from_start=np.inf)
    node_1_b = Node(location=Coordinate(x=0, y=0), heuristic_weight=1, distance_from_start=np.inf)
    assert node_1_a == node_1_b


def test_nodes_can_be_sorted():
    node_1 = Node(location=Coordinate(x=0, y=0), heuristic_weight=1, distance_from_start=np.inf)
    node_2 = Node(location=Coordinate(x=0, y=0), heuristic_weight=2, distance_from_start=np.inf)
    node_3 = Node(location=Coordinate(x=0, y=0), heuristic_weight=3, distance_from_start=np.inf)
    node_4 = Node(location=Coordinate(x=0, y=0), heuristic_weight=4, distance_from_start=np.inf)

    unordered_node_list = [node_3, node_1, node_4, node_2]
    expected_result = [node_1, node_2, node_3, node_4]
    calculated_result = sorted(unordered_node_list)
    assert calculated_result == expected_result
