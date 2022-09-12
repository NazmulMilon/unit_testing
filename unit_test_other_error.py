import unittest


class Rectangle:

    def __init__(self, height, width):
        self.height = height
        self.width = width

    def get_area(self):
        return self.height * self.width

    def set_height(self, height):
        self.height=height

    def set_width(self, width):
        self.width = width


class UnitTestForRectangle(unittest.TestCase):

    def test_6(self):
        rectangle = Rectangle(20, 5)
        self.assertEqual(rectangle.get_area(), 100, "Test-6 failed")

    def test_geq(self):
        rectangle = Rectangle(200, 5)
        """tests if value is greater than or equal to a particular target"""
        self.assertGreaterEqual(rectangle.get_area(), -1)

    def test_assert_raises(self):
        rectangle = Rectangle(100,5)
        """using assertRaises to detect if an expected error is raised when running a particular block of code"""
        with self.assertRaises(ZeroDivisionError):
            a = 1 / 0


unittest.main()