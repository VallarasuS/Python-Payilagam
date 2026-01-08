class Circle:

    PI = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Area of circle: ", self.PI * (self.radius**2))


circle_one = Circle(5)
circle_one.area()


class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        print("Area of Rectangle:", self.width * self.height)


rectangle = Rectangle(5, 3)
rectangle.area()


class Square:

    def __init__(self, size):
        self.size = size

    def area(self):
        print("Area of Square: ", self.size**2)


square = Square(5)
square.area()
