from math import *


class Vector:
    def __init__(self, x: float = 0, y: float = 0):
        self.x, self.y = x, y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mod__(self, other) -> float:
        return self.x * other.y - self.y * other.x

    def len(self) -> float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def norm(self):
        l = self.len()
        if l == 0:
            return Vector(0, 0)
        return Vector(self.x / l, self.y / l)

    def rotate(self, ang: float):
        ang = ang / 180 * pi
        self.x, self.y = cos(ang) * self.x - sin(ang) * self.y, sin(ang) * self.x + cos(ang) * self.y

    def copy(self):
        return Vector(self.x, self.y)


def get_s(s: Vector, e: Vector, a: Vector):
    l = ((e - s) % (a - s)) / (e - s).len()
    return sqrt((a - s).len() ** 2 - l ** 2) / (e - s).len()
