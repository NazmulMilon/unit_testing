# Our code for tested
class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def get_area(self):
        return self.height * self.width

    def set_height(self, height):
        self.height = height

    def set_width(self, width):
        self.width = width


# PyTest also supports grouping functions together in classes, but the class should be named with prefix “Test”
class TestGetAreaRectangle:
    # the test function to be executed by Pytest
    def test_normal_case(self):
        rectangle = Rectangle(4, 6)
        assert rectangle.get_area() == 24, "incorrect area"

    def test_negative_case(self):
        '''expect -1 as output to denote error when looking at negative area'''
        rectangle= Rectangle(-2, 1)
        assert rectangle.get_area() == -2, "incorrect negative output"


obj = TestGetAreaRectangle()
# obj.test_normal_case()
# obj.test_negative_case()


def main():
    #test_normal_case()
    obj.test_normal_case()
    obj.test_negative_case()


if '__name__' == '__main__':
    main()
