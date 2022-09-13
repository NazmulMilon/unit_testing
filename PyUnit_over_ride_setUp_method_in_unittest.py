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
    def setUp(self):
        self.rectangle=Rectangle(0,0)

    def test_normal_case(self):
        self.rectangle.set_height(6)
        self.rectangle.set_width(4)
        self.assertEqual(self.rectangle.get_area(), 24, "incorrect area")

    def test_negative_case(self):
        """expect -1 as output to denote error when looking at negative area"""
        self.rectangle.set_width(-1)
        self.rectangle.set_height(2)
        self.assertEqual(self.rectangle.get_area(), -1, "incorrect negative output")


unittest.main()