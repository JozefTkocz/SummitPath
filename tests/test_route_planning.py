from src.route_planning import summit_permutations


def test_summit_permutations():
    input_list = ['a', 'b', 'c']
    expected_result = [('a', 'b'),
                       ('a', 'b'),
                       ('b', 'a'),
                       ('b', 'c'),
                       ('c', 'a'),
                       ('c', 'b')]
    calculated_result = summit_permutations(expected_result)
    assert calculated_result == expected_result
