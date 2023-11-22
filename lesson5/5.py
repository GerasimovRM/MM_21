from math import pi
import abc


class Shape:
    def __str__(self):
        return (f'{self.__class__.__name__}:\nПлощадь:{self.area()}'
                f'\nПериметер:{self.perimeter()}')

    @abc.abstractmethod
    def area(self):
        ...

    @abc.abstractmethod
    def perimeter(self):
        ...


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return pi * self.r ** 2

    def perimeter(self):
        return 2 * pi * self.r


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * (self.a + self.b)



rect = Rectangle(3, 4)
circ = Circle(10)
print(rect)
print(circ)