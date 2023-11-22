from math import pi


class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return pi * self.r ** 2

    def perimeter(self):
        return 2 * pi * self.r


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * (self.a + self.b)


def print_shape(shape):
    print(f'{shape.__class__.__name__}:\nПлощадь:{shape.area()}'
          f'\nПериметер:{shape.perimeter()}')


rect = Rectangle(3, 4)
circ = Circle(10)
print_shape(rect)
print_shape(circ)