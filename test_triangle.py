import math
from triangle import classify_triangle, is_valid_triangle


def test_equilateral():
    assert classify_triangle(5, 5, 5) == "Equilateral"


def test_invalid_triangle():
    assert classify_triangle(1, 2, 3) == "Invalid"
    assert classify_triangle(-1, 2, 3) == "Invalid"
    assert classify_triangle(0, 2, 3) == "Invalid"

def test_isosceles():
    assert classify_triangle(5, 5, 8) == "Isosceles"

def test_scalene():
    assert classify_triangle(3, 4, 5) == "Right Scalene"
    assert classify_triangle(5, 6, 7) == "Scalene"

def test_right_triangle_non_integer():
    assert classify_triangle(1.5, 2.0, math.sqrt(1.5**2 + 2.0**2)) == "Right Scalene"


def test_right_isosceles_non_integer():
    assert classify_triangle(5, 5, 5 * math.sqrt(2)) == "Right Isosceles"


def test_triangle_inequality_boundary():
    assert classify_triangle(2, 3, 4) == "Scalene"
    assert classify_triangle(2, 3, 5) == "Invalid"
    assert classify_triangle(2, 3, 6) == "Invalid"