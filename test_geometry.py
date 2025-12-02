import math
import unittest

import circle
import square


class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(circle.area(0), 0)

    def test_area_positive(self):
        result = circle.area(3)
        self.assertAlmostEqual(result, math.pi * 9, places=7)

    def test_perimeter_zero(self):
        self.assertEqual(circle.perimeter(0), 0)

    def test_perimeter_positive(self):
        result = circle.perimeter(2.5)
        self.assertAlmostEqual(result, 2 * math.pi * 2.5, places=7)



class SquareTestCase(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(square.area(0), 0)

    def test_area_positive(self):
        self.assertEqual(square.area(4), 16)

    def test_area_fractional(self):
        self.assertAlmostEqual(square.area(2.5), 6.25)

    def test_perimeter_zero(self):
        self.assertEqual(square.perimeter(0), 0)

    def test_perimeter_positive(self):
        self.assertEqual(square.perimeter(7), 28)


if __name__ == "__main__":
    unittest.main()
