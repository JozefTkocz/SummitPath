from src.models import Coordinate


def test_add_coordinate_2d():
    c_1 = Coordinate(x=1, y=1)
    c_2 = Coordinate(x=2, y=2)

    assert c_1 + c_2 == Coordinate(x=3, y=3)


def test_add_coordinate_3d():
    c_1 = Coordinate(x=1, y=1, z=1)
    c_2 = Coordinate(x=2, y=2, z=-1)

    assert c_1 + c_2 == Coordinate(x=3, y=3, z=0)


def test_add_coordinate_2d_and_3d():
    c_1 = Coordinate(x=1, y=1)
    c_2 = Coordinate(x=2, y=2, z=-1)

    assert c_1 + c_2 == Coordinate(x=3, y=3, z=-1)


def test_sub_coordinate_2d():
    c_1 = Coordinate(x=1, y=1)
    c_2 = Coordinate(x=2, y=2)

    assert c_1 - c_2 == Coordinate(x=-1, y=-1)


def test_sub_coordinate_3d():
    c_1 = Coordinate(x=1, y=1, z=1)
    c_2 = Coordinate(x=2, y=2, z=-1)

    assert c_1 - c_2 == Coordinate(x=-1, y=-1, z=2)


def test_sub_coordinate_2d_and_3d():
    c_1 = Coordinate(x=1, y=1)
    c_2 = Coordinate(x=2, y=2, z=-1)

    assert c_1 - c_2 == Coordinate(x=-1, y=-1, z=1)
