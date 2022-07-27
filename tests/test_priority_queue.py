from src.a_star import PriorityQueue


def test_priority_queue_is_empty():
    queue = PriorityQueue()
    assert queue.is_empty()


def test_priority_queue_is_not_empty():
    queue = PriorityQueue()
    queue.insert(1)
    assert not queue.is_empty()


def test_insert_and_get_first_item_from_priority_queue():
    queue = PriorityQueue()
    queue.insert(1)
    assert queue.get_first() == 1


def test_priority_queue_contains_item():
    queue = PriorityQueue()
    queue.insert(1)
    assert queue.contains(1)


def test_priority_queue_not_contains_item():
    queue = PriorityQueue()
    queue.insert(1)
    assert not queue.contains(2)


def test_priority_get_first_returns_lowest_valued_item():
    queue = PriorityQueue()
    queue.insert(10)
    queue.insert(1)
    queue.insert(100)
    assert queue.get_first() == 1
