class Vector:
    def __init__(self, *args):
        if len(args) == 2:
            self.x = args[0]
            self.y = args[1]
        elif len(args) == 1 and isinstance(args[0], (list, tuple)):
            self.x = args[0][0]
            self.y = args[0][1]
        else:
            raise ValueError

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __str__(self):
        return f'Vector: {self.x} {self.y}'

    @staticmethod
    def vector_add(vec1, vec2):
        return Vector(vec1.x + vec2.x, vec1.y + vec2.y)

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        elif isinstance(other, (list, tuple)) and len(other) == 2:
            return Vector(self.x + other[0], self.y + other[1])
        else:
            raise ValueError("Не вижу вектора!")

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self



vec1 = Vector(4, 10)
vec2 = Vector([1, 1])
vec3 = vec1 + [1, 2]  # vec1.__add__(vec2)
vec4 = [1, 2] + vec1
print(abs(vec1))  # [1, 2].__add__(vec1)
print(vec3)

print(vec1)
vec1 += vec2
print(vec1)

print("введите компоненты ерез пробел")
comps = list(map(float, input().split()))
vec5 = Vector(comps)
print(vec5)