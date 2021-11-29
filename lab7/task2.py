import math
import pytest


def roots(a, b, c):
    if (type(a) != int and type(a) != float) or (type(b) != int and type(b) != float) or (type(c) != int and type(c) != float):
        return
    d = b * b - 4 * a * c
    if a == 0 or (a == 0 and b == 0 and c == 0) or d < 0:
        return
    x1, x2 = (-b + math.sqrt(d)) / (2 * a), (-b - math.sqrt(d)) / (2 * a)
    if x1 < x2:
        return x1, x2
    return x2, x1


def test_all_zero():
    assert roots(0, 0, 0) == None


def test_a_zero():
    assert roots(0, 2, -5) == None


def test_a_d_ls_zero():
    assert roots(3, 2, 5) == None


def test_one_root():
    assert roots(1, 2, 1) == (-1, -1)


def test_two_roots():
    assert roots(1, 3, 0) == (-3, 0)


def test_float():
    x1, x2 = roots(2, 3, 0)
    assert x1, x2 == pytest.approx((-1.5, 0))


def test_float_params():
    x1, x2 = roots(1, -3, 2.25)
    assert x1, x2 == pytest.approx((1.5, 1.5))


def test_str():
    assert roots('1', 2, 3) == None


def test_list():
    assert roots(1, [2, 3], 3) == None
