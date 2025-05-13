import math
import random
from unittest import TestCase

from shape_area.shapes import Circle, Triangle


class SquareCalcTest(TestCase):
    def test_circle_square_calc_success(self):
        for _ in range(10):
            radius = random.random() * 100
            self.assertAlmostEqual(
                radius * radius * math.pi,
                Circle(radius).calc_square(),
            )
        self.assertAlmostEqual(0, Circle(0).calc_square())

    def test_triangle_square_calc_success(self):
        for _ in range(10):
            # get random coords dots
            x = [random.random() * 100 for _ in range(3)]
            y = [random.random() * 100 for _ in range(3)]

            # calc test area by coords
            area = (
                abs(x[0] * (y[1] - y[2]) + x[1] * (y[2] - y[0]) + x[2] * (y[0] - y[1]))
                / 2
            )

            # calc edges
            edges = [
                math.hypot(
                    x[_dot_index1] - x[_dot_index2],
                    y[_dot_index1] - y[_dot_index2],
                )
                for (_dot_index1, _dot_index2) in [
                    (0, 1),
                    (0, 2),
                    (1, 2),
                ]
            ]

            self.assertAlmostEqual(area, Triangle(*edges).calc_square())

        self.assertAlmostEqual(0, Triangle(0, 0, 0).calc_square())
