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


# The test based on unittest module
class UnitTestForRectangle(unittest.TestCase):
    def test_1(self):
        rectangle = Rectangle(16,2)
        self.assertEqual(rectangle.get_area(), 32, "Test Case Failed")

    def test_2(self):
        rectangle = Rectangle(12, 3)
        self.assertEqual(rectangle.get_area(), 36, "incorrect area")

    def test_3(self):
        """expect -1 as output to denote error when looking at negative area"""
        rectangle = Rectangle(-2, 1)
        self.assertEqual(rectangle.get_area(), -2, "incorrect negative output")

    def test_4(self):
        rectangle = Rectangle(5.5, 4.4)
        self.assertEqual(rectangle.get_area(), 24.200000000000003, "Float value not match")

    def test_5(self):
        rectangle = Rectangle(9,4)
        self.assertEqual(rectangle.get_area(), 36, "Integer test case failed")

    def test_6(self):
        rectangle = Rectangle(20, 5)
        self.assertEqual(rectangle.get_area(), 100, "Test-6 failed")

    def test_geq(self):
        rectangle = Rectangle(20, 5)
        """tests if value is greater than or equal to a particular target"""
        self.assertGreaterEqual(rectangle.get_area(), -1)

    def test_assert_raises(self):
        rectangle = Rectangle(100,5)
        """using assertRaises to detect if an expected error is raised when running a particular block of code"""
        with self.assertRaises(ZeroDivisionError):
            a = 1 / 0

# run the test
unittest.main()