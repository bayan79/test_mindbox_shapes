import math

from shapes.base import BaseShape


class Triangle(BaseShape):
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c

    @property
    def edges(self):
        return [self.a, self.b, self.c]

    def check_is_valid(self) -> bool:
        sorted_edges = sorted(self.edges)
        return (
            sorted_edges[0] >= 0
            and sorted_edges[0] + sorted_edges[1] >= sorted_edges[2]
        )

    def calc_shape(self) -> float:
        s = sum(self.edges) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def check_is_right(self) -> bool:
        sides = sorted(self.edges)
        return math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2)
