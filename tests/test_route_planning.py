import pandas as pd

from src.route_planning import pair_combinations, get_summit_coordinate
from src.models import Coordinate


def test_pair_combinations():
    input_list = ['a', 'b', 'c']
    expected_result = (('a', 'b'),
                       ('a', 'c'),
                       ('b', 'a'),
                       ('b', 'c'),
                       ('c', 'a'),
                       ('c', 'b'))
    calculated_result = pair_combinations(input_list)
    assert calculated_result == expected_result


def test_get_summit_coordinate():
    example_database = pd.DataFrame({
        'Name': ['Summit A', 'Summit B'],
        'Xcoord': [0, 1],
        'Ycoord': [0, 1]
    })

    expected_result = Coordinate(x=1, y=1)
    calculated_result = get_summit_coordinate('Summit B', example_database)
    assert calculated_result == expected_result
