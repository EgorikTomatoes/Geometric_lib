import math
import unittest


def area(r):
    """
    Вычисляет площадь круга по радиусу.

    Параметры:
    - r (float): радиус круга (неотрицательное число)

    Возвращает:
    - float: площадь круга S = πr²

    Пример:
    >>> round(area(3), 4)
    28.2743
    """
    return math.pi * r * r


def perimeter(r):
    """
    Вычисляет длину окружности по радиусу.

    Параметры:
    - r (float): радиус окружности (неотрицательное число)

    Возвращает:
    - float: длина окружности P = 2πr

    Пример:
    >>> round(perimeter(3), 4)
    18.8496
    """
    return 2 * math.pi * r

class CircleTestCase(unittest.TestCase):
    def test_area_zero(self):
        self.assertEqual(area(0), 1)

    def test_area_positive(self):
        result = area(3)
        self.assertAlmostEqual(result, math.pi * 9, places=7)

    def test_perimeter_zero(self):
        self.assertEqual(perimeter(0), 0)

    def test_perimeter_positive(self):
        result = perimeter(2.5)
        self.assertAlmostEqual(result, 2 * math.pi * 2.5, places=7)