import unittest
from triangle_func import get_triangle_type, IncorrectTriangleSides


class TestGetTriangleType(unittest.TestCase):
    
    def test_equilateral_triangle(self):
        self.assertEqual(get_triangle_type(3, 3, 3), "equilateral")
        self.assertEqual(get_triangle_type(5.5, 5.5, 5.5), "equilateral")
        self.assertEqual(get_triangle_type(1, 1, 1), "equilateral")
    
    def test_isosceles_triangle(self):
        self.assertEqual(get_triangle_type(3, 3, 4), "isosceles")
        self.assertEqual(get_triangle_type(5, 6, 5), "isosceles")
        self.assertEqual(get_triangle_type(7, 4, 4), "isosceles")
    
    def test_nonequilateral_triangle(self):
        self.assertEqual(get_triangle_type(3, 4, 5), "nonequilateral")
        self.assertEqual(get_triangle_type(6, 8, 10), "nonequilateral")
        self.assertEqual(get_triangle_type(5, 7, 9), "nonequilateral")

    def test_invalid_type_string(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type("3", 4, 5)
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(3, "4", 5)
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(3, 4, "5")
    
    def test_invalid_type_none(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(None, 4, 5)
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(3, None, 5)
    
    def test_zero_side(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(0, 4, 5)
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(3, 0, 5)
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(3, 4, 0)
    
    def test_negative_side(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(-1, 4, 5)
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(3, -2, 5)
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(3, 4, -3)
    
    def test_triangle_inequality_violation(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 1, 3)
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(2, 3, 6)
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(10, 1, 1)


if __name__ == "__main__":
    unittest.main()