class Rectangle:

    name = "Rectangle"

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        print("Area of", self.name, self.height * self.width)


class Square(Rectangle):

    name = "Square"

    def __init__(self, size):
        super().__init__(size, size)


square = Square(5)
square.area()
