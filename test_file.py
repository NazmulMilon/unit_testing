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


# the test function to be executed by Pytest
def test_normal_case():
    rectangle = Rectangle(4, 6)
    assert rectangle.get_area() == 55, "incorrect area"


def main():
    test_normal_case()


if '__name__' == '__main__':
    main()
