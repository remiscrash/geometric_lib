import unittest
from src.triangle import area, perimeter

class TriangleAreaTestCases(unittest.TestCase):
    def test_triangle_int_first(self):
        self.assertEqual(area(5, 8), 5 * 8 / 2)

    def test_triangle_int_second(self):
        self.assertEqual(area(57285, 38752), 57285 * 38752 / 2)

    def test_triangle_string_first(self):
        with self.assertRaises(TypeError):
            area("85", 91)

    def test_triangle_string_second(self):
        with self.assertRaises(TypeError):
            area("ITM0", "kdjf")

    def test_triangle_bool_first(self):
        with self.assertRaises(TypeError):
            area(True, False)

    def test_triangle_bool_second(self):
        with self.assertRaises(TypeError):
            area(False, False)

    def test_triangle_negative_int_first(self):
        with self.assertRaises(ValueError):
            area(-5, 85)

    def test_triangle_negative_int_second(self):
        with self.assertRaises(ValueError):
            area(-59853, -158)

    def test_triangle_zero_int(self):
        with self.assertRaises(ValueError):
            area(0, 6)

class TrianglePerimeterTestCases(unittest.TestCase):
    def test_triangle_int_first(self):
        self.assertEqual(perimeter(9, 8, 1), 9 + 8 + 1)

    def test_triangle_int_second(self):
        self.assertEqual(perimeter(394732, 1985321, 38529999), 394732 + 38529999 + 1985321)

    def test_triangle_string_first(self):
        with self.assertRaises(TypeError):
            perimeter("85", "35", "15")

    def test_triangle_string_second(self):
        with self.assertRaises(TypeError):
            perimeter("ITM0", "IS", "M3108")

    def test_triangle_bool_first(self):
        with self.assertRaises(TypeError):
            perimeter(True, True, True)

    def test_triangle_bool_second(self):
        with self.assertRaises(TypeError):
            perimeter(False, False, False)

    def test_triangle_negative_int_first(self):
        with self.assertRaises(ValueError):
            perimeter(-5, 158, 29)

    def test_triangle_negative_int_second(self):
        with self.assertRaises(ValueError):
            perimeter(-59853, -15, -25)

    def test_triangle_zero_int(self):
        with self.assertRaises(ValueError):
            perimeter(0, 19, 10)

if __name__ == '__main__':
    unittest.main()