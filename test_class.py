import pytest
from triangle_class import Triangle
from triangle_func import IncorrectTriangleSides
class TestTrianglePositive:
    
    def test_create_equilateral_triangle(self):
        triangle = Triangle(3, 3, 3)
        assert triangle.side1 == 3
        assert triangle.side2 == 3
        assert triangle.side3 == 3
    
    def test_create_isosceles_triangle(self):
        triangle = Triangle(5, 5, 8)
        assert triangle.side1 == 5
        assert triangle.side2 == 5
        assert triangle.side3 == 8
    
    def test_create_nonequilateral_triangle(self):
        triangle = Triangle(3, 4, 5)
        assert triangle.side1 == 3
        assert triangle.side2 == 4
        assert triangle.side3 == 5
    
    def test_triangle_type_equilateral(self):
        triangle = Triangle(4, 4, 4)
        assert triangle.triangle_type() == "equilateral"
    
    def test_triangle_type_isosceles(self):
        triangle = Triangle(5, 5, 6)
        assert triangle.triangle_type() == "isosceles"
    
    def test_triangle_type_nonequilateral(self):
        triangle = Triangle(6, 8, 10)
        assert triangle.triangle_type() == "nonequilateral"
    
    def test_perimeter_equilateral(self):
        triangle = Triangle(4, 4, 4)
        assert triangle.perimeter() == 12
    
    def test_perimeter_isosceles(self):
        triangle = Triangle(5, 5, 6)
        assert triangle.perimeter() == 16
    
    def test_perimeter_nonequilateral(self):
        triangle = Triangle(3, 4, 5)
        assert triangle.perimeter() == 12
    
    def test_perimeter_with_floats(self):
        triangle = Triangle(2.5, 3.5, 4.0)
        assert triangle.perimeter() == 10.0

class TestTriangleNegative:
    
    def test_invalid_type_string(self):
        with pytest.raises(IncorrectTriangleSides):
            Triangle("3", 4, 5)
        with pytest.raises(IncorrectTriangleSides):
            Triangle(3, "4", 5)
        with pytest.raises(IncorrectTriangleSides):
            Triangle(3, 4, "5")
    
    def test_invalid_type_none(self):
        with pytest.raises(IncorrectTriangleSides):
            Triangle(None, 4, 5)
    
    def test_zero_side(self):
        with pytest.raises(IncorrectTriangleSides):
            Triangle(0, 4, 5)
        with pytest.raises(IncorrectTriangleSides):
            Triangle(3, 0, 5)
        with pytest.raises(IncorrectTriangleSides):
            Triangle(3, 4, 0)
    
    def test_negative_side(self):
        with pytest.raises(IncorrectTriangleSides):
            Triangle(-1, 4, 5)
        with pytest.raises(IncorrectTriangleSides):
            Triangle(3, -2, 5)
        with pytest.raises(IncorrectTriangleSides):
            Triangle(3, 4, -3)
    
    def test_triangle_inequality_violation_sum_equal(self):
        with pytest.raises(IncorrectTriangleSides):
            Triangle(1, 2, 3)  # 1 + 2 = 3
    
    def test_triangle_inequality_violation_sum_less(self):
        with pytest.raises(IncorrectTriangleSides):
            Triangle(1, 1, 5)
        with pytest.raises(IncorrectTriangleSides):
            Triangle(2, 3, 10)
    
    def test_triangle_inequality_violation_with_floats(self):
        with pytest.raises(IncorrectTriangleSides):
            Triangle(1.5, 2.5, 4.1)

@pytest.mark.parametrize("a,b,c,expected_type", [
    (3, 3, 3, "equilateral"),
    (5, 5, 5, "equilateral"),
    (1, 1, 1, "equilateral"),
    (5, 5, 7, "isosceles"),
    (6, 8, 6, "isosceles"),
    (4, 3, 3, "isosceles"),
    (3, 4, 5, "nonequilateral"),
    (6, 8, 10, "nonequilateral"),
    (7, 8, 9, "nonequilateral"),
])
def test_triangle_type_parametrized(a, b, c, expected_type):
    triangle = Triangle(a, b, c)
    assert triangle.triangle_type() == expected_type


@pytest.mark.parametrize("a,b,c,expected_perimeter", [
    (3, 3, 3, 9),
    (4, 4, 4, 12),
    (5, 5, 6, 16),
    (3, 4, 5, 12),
    (6, 8, 10, 24),
    (2.5, 3.5, 4.0, 10.0),
])
def test_perimeter_parametrized(a, b, c, expected_perimeter):
    triangle = Triangle(a, b, c)
    assert triangle.perimeter() == expected_perimeter


@pytest.mark.parametrize("a,b,c", [
    (0, 4, 5),
    (3, 0, 5),
    (3, 4, 0),
    (-1, 4, 5),
    (3, -2, 5),
    (1, 1, 3),
    (2, 3, 6),
    (10, 1, 1),
    ("3", 4, 5),
    (3, "4", 5),
    (None, 4, 5),
])
def test_invalid_triangle_creation(a, b, c):
    with pytest.raises(IncorrectTriangleSides):
        Triangle(a, b, c)
