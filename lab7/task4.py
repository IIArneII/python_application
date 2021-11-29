import pytest


class Rectangle:
    def __init__(self, w, h):
        if (type(w) != int and type(w) != float) or (type(h) != int and type(h) != float):
            raise TypeError(f'Expected int, float')
        if w < 0 or h < 0:
            raise ValueError("Expected positive values")
        self.w = w
        self.h = h

    def get_area(self):
        return self.w * self.h

    def get_perimeter(self):
        return self.w * 2 + self.h * 2


@pytest.fixture(scope='module')
def rec():
    return Rectangle(5, 10)


def test_1(rec: Rectangle):
    assert rec.get_area() == 50


def test_2(rec: Rectangle):
    assert rec.get_perimeter() == 30


def test_3():
    with pytest.raises(TypeError):
        Rectangle('1', '1')


def test_4():
    with pytest.raises(ValueError):
        Rectangle(-10, -10)
