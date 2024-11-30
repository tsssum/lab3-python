import math

def pi_decorator(func):
    def wrapper(arg):
        return func(math.pi, arg)
    return wrapper

class AreaCalculator:
    def __init__(self):
        pass
    
    @staticmethod
    def triangle_area(a: float, b: float, c: float) -> float:
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))

    @staticmethod
    def rectangle_area(length: float, width: float) -> float:
        return length * width

    @pi_decorator
    @staticmethod
    def circle_area(pi: float, radius: float) -> float:
        return pi * radius ** 2
    
    @staticmethod
    def __str__():
        return "Класс AreaCalculator - статический класс для вычисления площадей треугольника, прямоугольника и круга."
