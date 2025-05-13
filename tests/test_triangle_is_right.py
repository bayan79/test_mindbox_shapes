from unittest import TestCase

from shape_area import Triangle


class TriangleIsRightTest(TestCase):
    def test_triangle_is_right(self):
        t = Triangle(3, 4, 5)
        self.assertTrue(t.check_is_right())

    def test_triangle_is_not_right(self):
        t: Triangle = Triangle(3, 4, 6)
        self.assertFalse(t.check_is_right())
