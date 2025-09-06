import unittest
import math
from Square_Geometry import Circle, Triangle, Rectangle, calculate_square


class TestCircle(unittest.TestCase):
    """Тесты для класса Circle"""

    def test_circle_creation_valid_radius(self):
        """Тест создания круга с корректным радиусом"""
        circle = Circle(5.0)
        self.assertEqual(circle.radius_attr, 5.0)
        self.assertEqual(circle.geometry_type, "Круг")

    def test_circle_creation_invalid_radius(self):
        """Тест создания круга с некорректным радиусом"""
        with self.assertRaises(ValueError):
            Circle(0)
        with self.assertRaises(ValueError):
            Circle(-5)

    def test_circle_area_calculation(self):
        """Тест вычисления площади круга"""
        circle = Circle(5.0)
        expected_area = math.pi * 25
        self.assertAlmostEqual(circle.square(), expected_area, places=7)

        circle_unit = Circle(1.0)
        self.assertAlmostEqual(circle_unit.square(), math.pi, places=7)


class TestTriangle(unittest.TestCase):
    """Тесты для класса Triangle"""

    def test_triangle_area_calculation(self):
        """Тест вычисления площади треугольника"""
        # Прямоугольный
        triangle = Triangle(3, 4, 5)
        expected_area = 6.0
        self.assertAlmostEqual(triangle.square(), expected_area, places=7)

        # Равносторонний треугольник
        triangle_eq = Triangle(6, 6, 6)
        expected_area_eq = (math.sqrt(3) / 4) * 36
        self.assertAlmostEqual(triangle_eq.square(), expected_area_eq, places=7)

    def test_right_triangle_detection(self):
        """Тест определения прямоугольного треугольника"""
        # Прямоугольный треугольник
        right_triangle = Triangle(3, 4, 5)
        self.assertTrue(right_triangle.is_triangle_straigt())

        # Не прямоугольный треугольник
        non_right_triangle = Triangle(3, 4, 6)
        self.assertFalse(non_right_triangle.is_triangle_straigt())


class TestRectangle(unittest.TestCase):
    """Тесты для класса Rectangle"""

    def test_rectangle_area_calculation(self):
        """Тест вычисления площади прямоугольника"""
        rectangle = Rectangle(4, 6)
        self.assertEqual(rectangle.square(), 24)


class TestPolymorphism(unittest.TestCase):
    """Тесты общей функции (полиморфизм)"""

    def test_calculate_square_function(self):
        """Тест функции calculate_square"""
        circle = Circle(2)
        triangle = Triangle(3, 4, 5)
        rectangle = Rectangle(3, 7)

        # Проверяем, что функция работает с любыми фигурами
        self.assertAlmostEqual(calculate_square(circle), math.pi * 4, places=7)
        self.assertAlmostEqual(calculate_square(triangle), 6.0, places=7)
        self.assertEqual(calculate_square(rectangle), 21)


if __name__ == '__main__':
    unittest.main()

