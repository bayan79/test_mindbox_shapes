import math

from shapes.base import BaseShape


class Circle(BaseShape):
    def __init__(self, r: float):
        self.r = r

    def check_is_valid(self) -> bool:
        return self.r >= 0

    def calc_shape(self) -> float:
        return self.r**2 * math.pi
