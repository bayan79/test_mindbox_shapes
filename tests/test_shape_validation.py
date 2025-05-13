from unittest import TestCase

from shapes import Circle, Triangle


class ShapeValidationTest(TestCase):
    def test_circle_success(self):
        c = Circle(42)
        self.assertTrue(c.check_is_valid())

    def test_triangle_success(self):
        t = Triangle(3, 4, 5)
        self.assertTrue(t.check_is_valid())

    def test_circle_non_valid(self):
        c = Circle(-42)
        self.assertFalse(c.check_is_valid())

    def test_triangle_non_valid(self):
        t: Triangle = Triangle(1, 3, 5)
        self.assertFalse(t.check_is_valid())
