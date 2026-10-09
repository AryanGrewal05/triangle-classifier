from triangle import classify_triangle


def test_stained_glass_customer_requirements():
    # Right-angle pieces must be identified
    assert classify_triangle(3, 4, 5) == "Right Scalene"

    # Invalid triangles must return a message without crashing
    assert classify_triangle(1, 2, 3) == "Invalid"

    # Valid triangles must have the correct shape
    assert classify_triangle(5, 5, 5) == "Equilateral"