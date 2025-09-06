from abc import ABC, abstractmethod
import math


class Figure(ABC):
    """Базовый класс"""

    @abstractmethod
    def square(self) -> float:
        """Вычисление площади"""
        pass

    @property
    @abstractmethod
    def geometry_type(self) -> str:
        """Тип фигуры"""
        pass


class Circle(Figure):
    """Класс для расчета площади круга"""

    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError('Число больше 0')
        self._radius = radius

    @property
    def radius_attr(self) -> float:
        """Радиус круга"""
        return  self._radius

    def square(self) -> float:
        """Вычисление площади круга: p * radius ** 2"""
        return math.pi * self._radius **2

    @property
    def geometry_type(self) -> str:
        """Возращение типа фигуры"""
        return "Круг"


class Triangle(Figure):
    """Класс для расчета площади треугольника"""
    def __init__(self, a: float, b: float, c : float):
        if not self._check_parameters(a, b, c):
            raise  ValueError("Стороны должны быть больше 0")
        self._sides = sorted([a,b,c])
        self._a, self._b, self._c = self._sides

    @staticmethod
    def _check_parameters(a: float, b: float, c: float) -> bool:
        if not all(parameter > 0 for parameter in [a, b, c]):
            return  False

        return (a + b > c and a + c > b and b + c > a)

    def square(self) -> float:
        """Вычисление площади (Герона) для любого треугольника"""
        half_perimeter = sum(self._sides) / 2
        area_squared = ( half_perimeter *
                        (half_perimeter - self._a) *
                        (half_perimeter - self._b) *
                        (half_perimeter - self._c))

        return math.sqrt(area_squared)

    def is_triangle_straigt(self) -> bool:
        """Выявление типа треугольника (прямоугольный)"""
        a, b, c = self._sides

        return abs(a ** 2 + b ** 2 - c ** 2) < 1e-10


    @property
    def geometry_type(self) -> str:
        return "Треугольник"


class Rectangle(Figure):
    """Класс для расчета площади прямоугольника"""

    def __init__(self, width: float, height: float):
        if width <= 0 or height <= 0:
            raise ValueError("Ширина и высота должны быть больше 0")
        self._width = width
        self._height = height

    def square(self) -> float:
        """Вычисление площади прямоугольника"""
        return self._width * self._height

    @property
    def geometry_type(self) -> str:
        return "Прямоугольник"

def calculate_square(figure: Figure) -> float:
    """Вычисление типа фигуры"""
    return figure.square()


if __name__ == "__main__":

    circle = Circle(5.0)
    triangle = Triangle(3.0, 4.0, 5.0)
    rectangle = Rectangle(4.0, 6.0)

    figures = [circle, triangle, rectangle]

    for figure in figures:
        area = calculate_square(figure)
        print(f"{figure.geometry_type}: площадь = {area:.2f}")

    print(f"\nДополнительная информация:")
    print(f"Радиус круга: {circle.radius_attr}")
    print(f"Треугольник прямоугольный: {'Да' if triangle.is_triangle_straigt() else 'Нет'}")

    