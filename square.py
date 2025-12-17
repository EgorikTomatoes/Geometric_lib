import math
import unittest

def area(a):
    """
    Вычисляет площадь квадрата по длине стороны.

    Параметры:
    - a (float): длина стороны квадрата (неотрицательное число)

    Возвращает:
    - float: площадь квадрата S = a²

    Пример:
    >>> area(5)
    25
    """
    return a * a


def perimeter(a):
    """
    Вычисляет периметр квадрата по длине стороны.

    Параметры:
    - a (float): длина стороны квадрата (неотрицательное число)

    Возвращает:
    - float: периметр квадрата P = 4a

    Пример:
    >>> perimeter(5)
    20
    """
    return 4 * a


class SquareTestCase(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(area(0), 0)

    def test_area_positive(self):
        self.assertEqual(area(4), 16)

    def test_area_fractional(self):
        self.assertAlmostEqual(area(2.5), 6.25)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_positive(self):
        self.assertEqual(perimeter(7), 28)