import math
import random
from unittest import TestCase

from shape_area.shapes import BaseShape, Circle, Triangle


class ShapeCreationTest(TestCase):
    def test_triangle_creation_success(self):
        self.assertIsNotNone(Triangle.build_and_validate(3, 4, 5))

    def test_circle_creation_success(self):
        self.assertIsNotNone(Circle.build_and_validate(10))

    def test_triangle_creation_non_valid(self):
        with self.assertRaises(ValueError):
            Triangle.build_and_validate(1, 3, 5)

    def test_circle_creation_non_valid(self):
        with self.assertRaises(ValueError):
            Circle.build_and_validate(-1)

    def test_random_shape_creation(self):
        def gen_triangle_args():
            # get random coords dots
            x = [random.random() * 100 for _ in range(3)]
            y = [random.random() * 100 for _ in range(3)]

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
            return ("Triangle", *edges)

        def gen_circle_args():
            return ("Circle", random.random() * 100)

        for i in range(20):
            shape_type, *args = gen_triangle_args() if i % 2 else gen_circle_args()
            BaseShape.get_registered(shape_type).build_and_validate(*args)
